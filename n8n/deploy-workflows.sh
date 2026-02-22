#!/usr/bin/env bash
# ABOUTME: Deploys all workflow JSON files from workflows/ into the running n8n instance.
# ABOUTME: Patches credential IDs and Telegram bot token before importing.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKFLOW_DIR="$SCRIPT_DIR/workflows"
N8N_URL="${N8N_URL:-http://localhost:1111}"

# ── Preflight checks ──────────────────────────────────────────────────
for cmd in jq curl sed; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

if [ ! -d "$WORKFLOW_DIR" ]; then
    echo "ERROR: $WORKFLOW_DIR not found. Run generate_workflows.py first."
    exit 1
fi

# ── Credentials ───────────────────────────────────────────────────────
# n8n login credentials
if [ -z "${N8N_EMAIL:-}" ] || [ -z "${N8N_PASSWORD:-}" ]; then
    echo "N8N_EMAIL and N8N_PASSWORD must be set."
    echo "Usage: N8N_EMAIL=you@example.com N8N_PASSWORD=secret $0"
    exit 1
fi

# Telegram bot token (needed for Template C multimodal workflows)
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
    echo "WARNING: TELEGRAM_BOT_TOKEN not set."
    echo "Template C workflows (04, 05) will have __TELEGRAM_BOT_TOKEN__ placeholders."
    echo "Set it to patch automatically: TELEGRAM_BOT_TOKEN=123:ABC... $0"
    echo ""
fi

# ── Login to n8n ──────────────────────────────────────────────────────
echo "Logging into n8n at $N8N_URL ..."

COOKIE_JAR=$(mktemp)
trap 'rm -f "$COOKIE_JAR" 2>/dev/null' EXIT

LOGIN_RESP=$(curl -s -c "$COOKIE_JAR" \
    -H "Content-Type: application/json" \
    -d "{\"emailOrLdapLoginId\": \"$N8N_EMAIL\", \"password\": \"$N8N_PASSWORD\"}" \
    "$N8N_URL/rest/login")

if echo "$LOGIN_RESP" | jq -e '.data.id' >/dev/null 2>&1; then
    echo "Login successful."
else
    echo "ERROR: Login failed."
    echo "$LOGIN_RESP" | jq . 2>/dev/null || echo "$LOGIN_RESP"
    exit 1
fi

# ── Discover credential IDs ──────────────────────────────────────────
echo "Fetching credentials..."

CREDS_RESP=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/credentials")

BEARER_ID=$(echo "$CREDS_RESP" | jq -r '.data[] | select(.type == "httpBearerAuth") | .id' | head -1)
TELEGRAM_ID=$(echo "$CREDS_RESP" | jq -r '.data[] | select(.type == "telegramApi") | .id' | head -1)

if [ -z "$BEARER_ID" ] || [ "$BEARER_ID" = "null" ]; then
    echo "ERROR: No Bearer Auth credential found in n8n. Create one first."
    exit 1
fi

if [ -z "$TELEGRAM_ID" ] || [ "$TELEGRAM_ID" = "null" ]; then
    echo "ERROR: No Telegram API credential found in n8n. Create one first."
    exit 1
fi

echo "  Bearer Auth credential ID: $BEARER_ID"
echo "  Telegram API credential ID: $TELEGRAM_ID"

# ── Import workflows ─────────────────────────────────────────────────
echo ""
echo "Importing workflows..."

SUCCESS=0
FAIL=0

for f in "$WORKFLOW_DIR"/*.json; do
    BASENAME=$(basename "$f")
    echo -n "  $BASENAME ... "

    # Read and patch the workflow JSON
    PATCHED=$(jq \
        --arg bid "$BEARER_ID" \
        --arg tid "$TELEGRAM_ID" \
        '
        # Remove fields that conflict with import
        del(.id, .versionId) |
        del(.meta.instanceId) |
        # Patch Bearer Auth credential IDs
        (.nodes[] |
            select(.credentials.httpBearerAuth.id == "PLACEHOLDER") |
            .credentials.httpBearerAuth.id) |= $bid |
        # Patch Telegram credential IDs
        (.nodes[] |
            select(.credentials.telegramApi.id == "PLACEHOLDER") |
            .credentials.telegramApi.id) |= $tid
        ' "$f")

    # Patch Telegram bot token in URL strings (for Template C workflows)
    if [ -n "${TELEGRAM_BOT_TOKEN:-}" ]; then
        PATCHED=$(echo "$PATCHED" | sed "s/__TELEGRAM_BOT_TOKEN__/$TELEGRAM_BOT_TOKEN/g")
    fi

    # Import via REST API
    RESP=$(echo "$PATCHED" | curl -s -b "$COOKIE_JAR" \
        -H "Content-Type: application/json" \
        -d @- \
        "$N8N_URL/rest/workflows")

    WF_ID=$(echo "$RESP" | jq -r '.data.id // empty' 2>/dev/null)

    if [ -n "$WF_ID" ]; then
        WF_NAME=$(echo "$RESP" | jq -r '.data.name')
        echo "OK (id=$WF_ID, name=$WF_NAME)"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "FAILED"
        echo "    $(echo "$RESP" | jq -r '.message // .' 2>/dev/null | head -1)"
        FAIL=$((FAIL + 1))
    fi
done

echo ""
TOTAL=$(ls "$WORKFLOW_DIR"/*.json | wc -l)
EVAL=$(ls "$WORKFLOW_DIR"/eval-*.json 2>/dev/null | wc -l)
STUDENT=$((TOTAL - EVAL))
echo "Done: $SUCCESS imported, $FAIL failed (out of $TOTAL total: $STUDENT student + $EVAL eval)"
echo ""
echo "NOTE: Student workflows are imported as INACTIVE."
echo "Activate only one at a time in the n8n UI (Telegram webhook limitation)."
echo "Eval workflows can be run manually (Manual Trigger) without activation."
