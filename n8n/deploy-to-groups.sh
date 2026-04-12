#!/usr/bin/env bash
# ABOUTME: Deploys teacher example workflows into each group's personal project.
# ABOUTME: Logs in as each group (using group-credentials.csv) and imports workflow JSONs.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
WORKFLOW_DIR="$SCRIPT_DIR/workflows"
CRED_FILE="$PROJECT_ROOT/.private/n8n/group-credentials.csv"
N8N_URL="${N8N_URL:-http://localhost:1111}"

# ── Preflight checks ────────────────────────────────────────────────
for cmd in jq curl; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

if [ ! -d "$WORKFLOW_DIR" ]; then
    echo "ERROR: $WORKFLOW_DIR not found."
    exit 1
fi

WORKFLOW_COUNT=$(ls "$WORKFLOW_DIR"/*.json 2>/dev/null | wc -l)
if [ "$WORKFLOW_COUNT" -eq 0 ]; then
    echo "ERROR: No workflow JSON files in $WORKFLOW_DIR."
    exit 1
fi

if [ ! -f "$CRED_FILE" ]; then
    echo "ERROR: $CRED_FILE not found."
    exit 1
fi

echo "Deploying $WORKFLOW_COUNT teacher example workflows per group."
echo "Reading credentials from: $CRED_FILE"
echo "n8n URL: $N8N_URL"
echo ""

# ── Deploy to each group ────────────────────────────────────────────
GROUPS_OK=0
GROUPS_FAIL=0
TOTAL_WF=0

while IFS=',' read -r group email password; do
    # Skip header
    [ "$group" = "group" ] && continue

    echo "--- Group $group ($email) ---"

    # Login as group
    GROUP_COOKIE=$(mktemp)
    trap "rm -f $GROUP_COOKIE 2>/dev/null" RETURN

    LOGIN_RESP=$(curl -s -c "$GROUP_COOKIE" \
        -H "Content-Type: application/json" \
        -d "{\"emailOrLdapLoginId\": \"$email\", \"password\": \"$password\"}" \
        "$N8N_URL/rest/login")

    LOGIN_ID=$(echo "$LOGIN_RESP" | jq -r '.data.id // empty')
    if [ -z "$LOGIN_ID" ] || [ "$LOGIN_ID" = "null" ]; then
        echo "  LOGIN FAILED — skipping"
        echo "  $(echo "$LOGIN_RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
        GROUPS_FAIL=$((GROUPS_FAIL + 1))
        rm -f "$GROUP_COOKIE"
        continue
    fi

    # Import each workflow
    WF_OK=0
    WF_FAIL=0
    for f in "$WORKFLOW_DIR"/*.json; do
        BASENAME=$(basename "$f")
        echo -n "  $BASENAME ... "

        # Strip id/versionId/instanceId so n8n creates fresh copies
        CLEANED=$(jq 'del(.id, .versionId) | del(.meta.instanceId)' "$f")

        RESP=$(echo "$CLEANED" | curl -s -b "$GROUP_COOKIE" \
            -H "Content-Type: application/json" \
            -d @- \
            "$N8N_URL/rest/workflows")

        WF_ID=$(echo "$RESP" | jq -r '.data.id // empty' 2>/dev/null)
        if [ -n "$WF_ID" ]; then
            echo "OK (id=$WF_ID)"
            WF_OK=$((WF_OK + 1))
        else
            echo "FAILED"
            echo "    $(echo "$RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
            WF_FAIL=$((WF_FAIL + 1))
        fi
    done

    echo "  Result: $WF_OK imported, $WF_FAIL failed"
    TOTAL_WF=$((TOTAL_WF + WF_OK))
    GROUPS_OK=$((GROUPS_OK + 1))
    rm -f "$GROUP_COOKIE"
    echo ""
done < "$CRED_FILE"

# ── Summary ─────────────────────────────────────────────────────────
echo "========================================="
echo "  SUMMARY"
echo "========================================="
echo "Groups processed: $GROUPS_OK (failed: $GROUPS_FAIL)"
echo "Total workflows imported: $TOTAL_WF"
echo ""
echo "NOTE: Workflows imported with PLACEHOLDER credentials."
echo "Students must configure their own API keys in each workflow."
