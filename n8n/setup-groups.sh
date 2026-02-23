#!/usr/bin/env bash
# ABOUTME: Creates 7 group accounts (G01–G07) in n8n and imports teacher example workflows.
# ABOUTME: Each group gets its own login and a copy of all 5 TEACHER_EXAMPLE workflows.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKFLOW_DIR="$SCRIPT_DIR/workflows"
N8N_URL="${N8N_URL:-http://localhost:1111}"
CRED_FILE="$SCRIPT_DIR/group-credentials.csv"
NUM_GROUPS=7

# ── Preflight checks ────────────────────────────────────────────────
for cmd in jq curl openssl; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

if [ ! -d "$WORKFLOW_DIR" ]; then
    echo "ERROR: $WORKFLOW_DIR not found. Run generate_teacher_examples.py first."
    exit 1
fi

WORKFLOW_COUNT=$(ls "$WORKFLOW_DIR"/*.json 2>/dev/null | wc -l)
if [ "$WORKFLOW_COUNT" -eq 0 ]; then
    echo "ERROR: No workflow JSON files in $WORKFLOW_DIR."
    exit 1
fi
echo "Found $WORKFLOW_COUNT teacher example workflows to import per group."

if [ -z "${N8N_EMAIL:-}" ] || [ -z "${N8N_PASSWORD:-}" ]; then
    echo "N8N_EMAIL and N8N_PASSWORD must be set (source .envrc first)."
    exit 1
fi

# ── Login as owner ──────────────────────────────────────────────────
echo ""
echo "=== Step 1: Login as owner ==="

OWNER_COOKIE=$(mktemp)
trap 'rm -f "$OWNER_COOKIE" /tmp/group_cookie_* 2>/dev/null' EXIT

LOGIN_RESP=$(curl -s -c "$OWNER_COOKIE" \
    -H "Content-Type: application/json" \
    -d "{\"emailOrLdapLoginId\": \"$N8N_EMAIL\", \"password\": \"$N8N_PASSWORD\"}" \
    "$N8N_URL/rest/login")

OWNER_ID=$(echo "$LOGIN_RESP" | jq -r '.data.id // empty')
if [ -z "$OWNER_ID" ]; then
    echo "ERROR: Owner login failed."
    echo "$LOGIN_RESP" | jq . 2>/dev/null || echo "$LOGIN_RESP"
    exit 1
fi
echo "Owner login OK (id=$OWNER_ID)"

# ── Generate passwords ──────────────────────────────────────────────
# n8n requires: 8-64 chars, at least 1 uppercase, at least 1 digit
generate_password() {
    # base64 gives us letters+digits+symbols, append A1 to guarantee constraints
    local raw
    raw=$(openssl rand -base64 9)
    echo "${raw}A1"
}

# ── Create invitations and accept them ──────────────────────────────
echo ""
echo "=== Step 2: Create group accounts ==="

# Initialize CSV
echo "group,email,password" > "$CRED_FILE"

GROUPS_CREATED=0
GROUPS_FAILED=0

for i in $(seq 1 $NUM_GROUPS); do
    GROUP_NUM=$(printf "%02d" "$i")
    GROUP_EMAIL="group${GROUP_NUM}@n8n.local"
    GROUP_PASS=$(generate_password)
    GROUP_FIRST="Groupe"
    GROUP_LAST="$GROUP_NUM"

    echo ""
    echo "--- Group $GROUP_NUM ($GROUP_EMAIL) ---"

    # Create invitation
    echo -n "  Creating invitation... "
    INVITE_RESP=$(curl -s -b "$OWNER_COOKIE" \
        -H "Content-Type: application/json" \
        -d "[{\"email\": \"$GROUP_EMAIL\", \"role\": \"global:member\"}]" \
        "$N8N_URL/rest/invitations")

    INVITEE_ID=$(echo "$INVITE_RESP" | jq -r '.data[0].user.id // empty')
    INVITE_ERROR=$(echo "$INVITE_RESP" | jq -r '.data[0].error // empty')

    if [ -z "$INVITEE_ID" ] || [ "$INVITEE_ID" = "null" ]; then
        echo "FAILED"
        echo "  Error: ${INVITE_ERROR:-$(echo "$INVITE_RESP" | jq -c . 2>/dev/null || echo "$INVITE_RESP")}"
        GROUPS_FAILED=$((GROUPS_FAILED + 1))
        continue
    fi
    echo "OK (inviteeId=$INVITEE_ID)"

    # Accept invitation (sets password, no auth required)
    echo -n "  Accepting invitation... "
    ACCEPT_RESP=$(curl -s -c /dev/null \
        -H "Content-Type: application/json" \
        -d "{
            \"inviterId\": \"$OWNER_ID\",
            \"firstName\": \"$GROUP_FIRST\",
            \"lastName\": \"$GROUP_LAST\",
            \"password\": \"$GROUP_PASS\"
        }" \
        "$N8N_URL/rest/invitations/$INVITEE_ID/accept")

    ACCEPT_ID=$(echo "$ACCEPT_RESP" | jq -r '.data.id // empty')
    if [ -z "$ACCEPT_ID" ] || [ "$ACCEPT_ID" = "null" ]; then
        echo "FAILED"
        echo "  $(echo "$ACCEPT_RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
        GROUPS_FAILED=$((GROUPS_FAILED + 1))
        continue
    fi
    echo "OK (user activated)"

    # Write to CSV
    echo "$GROUP_NUM,$GROUP_EMAIL,$GROUP_PASS" >> "$CRED_FILE"
    GROUPS_CREATED=$((GROUPS_CREATED + 1))

    # ── Login as group and import workflows ─────────────────────────
    echo -n "  Logging in as group... "
    GROUP_COOKIE="/tmp/group_cookie_${GROUP_NUM}"
    GROUP_LOGIN=$(curl -s -c "$GROUP_COOKIE" \
        -H "Content-Type: application/json" \
        -d "{\"emailOrLdapLoginId\": \"$GROUP_EMAIL\", \"password\": \"$GROUP_PASS\"}" \
        "$N8N_URL/rest/login")

    GROUP_LOGIN_ID=$(echo "$GROUP_LOGIN" | jq -r '.data.id // empty')
    if [ -z "$GROUP_LOGIN_ID" ] || [ "$GROUP_LOGIN_ID" = "null" ]; then
        echo "FAILED (cannot import workflows)"
        echo "  $(echo "$GROUP_LOGIN" | jq -r '.message // .' 2>/dev/null | head -1)"
        continue
    fi
    echo "OK"

    # Import each workflow
    WF_SUCCESS=0
    WF_FAIL=0
    for f in "$WORKFLOW_DIR"/*.json; do
        BASENAME=$(basename "$f")
        echo -n "  Importing $BASENAME ... "

        # Strip id/versionId/instanceId so n8n creates fresh copies
        CLEANED=$(jq 'del(.id, .versionId) | del(.meta.instanceId)' "$f")

        RESP=$(echo "$CLEANED" | curl -s -b "$GROUP_COOKIE" \
            -H "Content-Type: application/json" \
            -d @- \
            "$N8N_URL/rest/workflows")

        WF_ID=$(echo "$RESP" | jq -r '.data.id // empty' 2>/dev/null)
        if [ -n "$WF_ID" ]; then
            echo "OK (id=$WF_ID)"
            WF_SUCCESS=$((WF_SUCCESS + 1))
        else
            echo "FAILED"
            echo "    $(echo "$RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
            WF_FAIL=$((WF_FAIL + 1))
        fi
    done
    echo "  Workflows: $WF_SUCCESS imported, $WF_FAIL failed"
done

# ── Summary ─────────────────────────────────────────────────────────
echo ""
echo "========================================="
echo "  SUMMARY"
echo "========================================="
echo "Groups created: $GROUPS_CREATED / $NUM_GROUPS"
echo "Groups failed:  $GROUPS_FAILED"
echo "Workflows per group: $WORKFLOW_COUNT"
echo "Total workflows imported: $((GROUPS_CREATED * WORKFLOW_COUNT))"
echo ""

if [ "$GROUPS_CREATED" -gt 0 ]; then
    echo "Credentials written to: $CRED_FILE"
    echo ""
    echo "--- Credentials (for distribution) ---"
    column -t -s ',' "$CRED_FILE"
    echo ""
    echo "IMPORTANT: Keep this file safe. It contains passwords."
    echo "           It is gitignored and should not be committed."
fi
