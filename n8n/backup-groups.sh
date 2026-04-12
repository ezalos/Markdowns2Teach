#!/usr/bin/env bash
# ABOUTME: Backs up all student group workflows from n8n into .private/student_submissions/GXX/.
# ABOUTME: Read-only on the server — only GET requests. Safe to re-run (idempotent).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SUBMISSIONS_DIR="$PROJECT_ROOT/.private/student_submissions"
BACKUP_TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Admin credentials (local Docker instance, also in README.md)
N8N_EMAIL="${N8N_EMAIL:-louis@sorbonne.fr}"
N8N_PASSWORD="${N8N_PASSWORD:-N8n-Sorbonne-2026}"

# ── Resolve n8n URL ────────────────────────────────────────────────
if [ -z "${N8N_URL:-}" ]; then
    echo "Resolving n8n container IP..."
    CONTAINER_IP=$(docker inspect n8n-n8n-1 --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' 2>/dev/null || true)
    if [ -z "$CONTAINER_IP" ]; then
        echo "ERROR: Could not find n8n-n8n-1 container. Set N8N_URL manually."
        exit 1
    fi
    N8N_URL="http://${CONTAINER_IP}:5678"
    echo "  → $N8N_URL"
fi

# ── Preflight checks ──────────────────────────────────────────────
for cmd in jq curl; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

# ── Authenticate ───────────────────────────────────────────────────
COOKIE_JAR=$(mktemp)
cleanup() { rm -f "$COOKIE_JAR"; }
trap cleanup EXIT

echo "Logging in as $N8N_EMAIL..."
LOGIN_RESP=$(curl -s -c "$COOKIE_JAR" \
    -H "Content-Type: application/json" \
    -d "{\"emailOrLdapLoginId\": \"$N8N_EMAIL\", \"password\": \"$N8N_PASSWORD\"}" \
    "$N8N_URL/rest/login")

LOGIN_ID=$(echo "$LOGIN_RESP" | jq -r '.data.id // empty')
if [ -z "$LOGIN_ID" ] || [ "$LOGIN_ID" = "null" ]; then
    echo "ERROR: Login failed."
    echo "  $(echo "$LOGIN_RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
    exit 1
fi
echo "  → Authenticated (user $LOGIN_ID)"

# ── Fetch all workflows ───────────────────────────────────────────
echo ""
echo "Fetching workflow list..."
WF_LIST=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/workflows")
WF_COUNT=$(echo "$WF_LIST" | jq '.data | length')
echo "  → $WF_COUNT workflows found"

# ── Process each workflow ─────────────────────────────────────────
echo ""
declare -A GROUP_OK GROUP_FAIL GROUP_SKIP
TOTAL_OK=0
TOTAL_FAIL=0
TOTAL_SKIP=0

# Build per-group manifest data in temp files
MANIFEST_DIR=$(mktemp -d)
trap "rm -f '$COOKIE_JAR'; rm -rf '$MANIFEST_DIR'" EXIT

for i in $(seq 0 $((WF_COUNT - 1))); do
    WF_META=$(echo "$WF_LIST" | jq -c ".data[$i]")
    WF_ID=$(echo "$WF_META" | jq -r '.id')
    WF_NAME=$(echo "$WF_META" | jq -r '.name')
    PROJECT_NAME=$(echo "$WF_META" | jq -r '.homeProject.name // "unknown"')

    # Extract group number from "Groupe XX <groupXX@n8n.local>"
    if [[ "$PROJECT_NAME" =~ group([0-9]{2}) ]]; then
        GROUP_NUM="${BASH_REMATCH[1]}"
    else
        echo "  SKIP: \"$WF_NAME\" ($WF_ID) — owner: $PROJECT_NAME"
        TOTAL_SKIP=$((TOTAL_SKIP + 1))
        continue
    fi

    GROUP_DIR="$SUBMISSIONS_DIR/G${GROUP_NUM}"
    mkdir -p "$GROUP_DIR"

    # Sanitize workflow name for filename: lowercase, replace non-alnum with dashes, collapse
    SAFE_NAME=$(echo "$WF_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9._-]/-/g; s/--*/-/g; s/^-//; s/-$//')
    FILENAME="${SAFE_NAME}_${WF_ID}.json"
    FILEPATH="$GROUP_DIR/$FILENAME"

    echo -n "  G${GROUP_NUM}: \"$WF_NAME\" → $FILENAME ... "

    # Fetch full workflow
    WF_FULL=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/workflows/$WF_ID")

    # Validate JSON and extract .data
    WF_DATA=$(echo "$WF_FULL" | jq '.data' 2>/dev/null)
    if [ $? -ne 0 ] || [ "$WF_DATA" = "null" ]; then
        echo "FAILED (invalid response)"
        TOTAL_FAIL=$((TOTAL_FAIL + 1))
        GROUP_FAIL[$GROUP_NUM]=$(( ${GROUP_FAIL[$GROUP_NUM]:-0} + 1 ))
        continue
    fi

    # Write to file
    echo "$WF_DATA" | jq '.' > "$FILEPATH"

    # Verify the written file is valid JSON
    if jq '.' "$FILEPATH" > /dev/null 2>&1; then
        echo "OK"
        TOTAL_OK=$((TOTAL_OK + 1))
        GROUP_OK[$GROUP_NUM]=$(( ${GROUP_OK[$GROUP_NUM]:-0} + 1 ))

        # Append to manifest temp file
        echo "$WF_DATA" | jq -c "{id: .id, name: .name, active: .active, createdAt: .createdAt, updatedAt: .updatedAt, filename: \"$FILENAME\"}" \
            >> "$MANIFEST_DIR/G${GROUP_NUM}.jsonl"
    else
        echo "FAILED (JSON validation)"
        TOTAL_FAIL=$((TOTAL_FAIL + 1))
        GROUP_FAIL[$GROUP_NUM]=$(( ${GROUP_FAIL[$GROUP_NUM]:-0} + 1 ))
        # Remove invalid file
        rip "$FILEPATH" 2>/dev/null || rm -f "$FILEPATH"
    fi
done

# ── Write per-group manifests ─────────────────────────────────────
echo ""
echo "Writing manifests..."
for GROUP_NUM in 01 02 03 04 05 06 07; do
    GROUP_DIR="$SUBMISSIONS_DIR/G${GROUP_NUM}"
    MANIFEST="$GROUP_DIR/manifest.json"
    MANIFEST_SRC="$MANIFEST_DIR/G${GROUP_NUM}.jsonl"

    if [ -f "$MANIFEST_SRC" ]; then
        jq -n --arg ts "$BACKUP_TIMESTAMP" --arg group "G${GROUP_NUM}" \
            --slurpfile wfs <(jq -s '.' "$MANIFEST_SRC") \
            '{backup_timestamp: $ts, group: $group, workflow_count: ($wfs[0] | length), workflows: $wfs[0]}' \
            > "$MANIFEST"
        echo "  G${GROUP_NUM}/manifest.json — $(jq '.workflow_count' "$MANIFEST") workflows"
    else
        # Empty manifest for groups with no workflows
        jq -n --arg ts "$BACKUP_TIMESTAMP" --arg group "G${GROUP_NUM}" \
            '{backup_timestamp: $ts, group: $group, workflow_count: 0, workflows: []}' \
            > "$MANIFEST"
        echo "  G${GROUP_NUM}/manifest.json — 0 workflows (⚠ EMPTY)"
    fi
done

# ── Summary ───────────────────────────────────────────────────────
echo ""
echo "========================================="
echo "  BACKUP SUMMARY — $BACKUP_TIMESTAMP"
echo "========================================="
echo "Total exported: $TOTAL_OK"
echo "Failed:         $TOTAL_FAIL"
echo "Skipped:        $TOTAL_SKIP (admin/teacher-owned)"
echo ""
echo "Per group:"
for GROUP_NUM in 01 02 03 04 05 06 07; do
    OK=${GROUP_OK[$GROUP_NUM]:-0}
    FAIL=${GROUP_FAIL[$GROUP_NUM]:-0}
    if [ "$FAIL" -gt 0 ]; then
        echo "  G${GROUP_NUM}: $OK exported, $FAIL FAILED"
    else
        echo "  G${GROUP_NUM}: $OK exported"
    fi
done
echo ""
echo "Output: $SUBMISSIONS_DIR/G*/"
