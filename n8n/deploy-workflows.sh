#!/usr/bin/env bash
# ABOUTME: Deploys teacher example workflow JSONs from workflows/ into the running n8n instance.
# ABOUTME: Patches credential IDs before importing. Use --clean to delete all existing workflows first.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKFLOW_DIR="$SCRIPT_DIR/workflows"
N8N_URL="${N8N_URL:-http://localhost:1111}"
CLEAN_MODE=false

# ── Parse arguments ──────────────────────────────────────────────────
for arg in "$@"; do
    case "$arg" in
        --clean) CLEAN_MODE=true ;;
        *) echo "Unknown argument: $arg"; echo "Usage: $0 [--clean]"; exit 1 ;;
    esac
done

# ── Preflight checks ────────────────────────────────────────────────
for cmd in jq curl; do
    command -v "$cmd" >/dev/null 2>&1 || { echo "ERROR: $cmd is required but not installed."; exit 1; }
done

if [ ! -d "$WORKFLOW_DIR" ]; then
    echo "ERROR: $WORKFLOW_DIR not found. Run generate_teacher_examples.py first."
    exit 1
fi

# ── Credentials ──────────────────────────────────────────────────────
if [ -z "${N8N_EMAIL:-}" ] || [ -z "${N8N_PASSWORD:-}" ]; then
    echo "N8N_EMAIL and N8N_PASSWORD must be set."
    echo "Usage: N8N_EMAIL=you@example.com N8N_PASSWORD=secret $0 [--clean]"
    exit 1
fi

# ── Login to n8n ─────────────────────────────────────────────────────
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

# ── Clean mode: delete all existing workflows ────────────────────────
if [ "$CLEAN_MODE" = true ]; then
    echo ""
    echo "Clean mode: deleting all existing workflows..."
    EXISTING=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/workflows")
    EXISTING_IDS=$(echo "$EXISTING" | jq -r '.data[]?.id // empty')

    if [ -z "$EXISTING_IDS" ]; then
        echo "  No existing workflows to delete."
    else
        DELETED=0
        for wf_id in $EXISTING_IDS; do
            WF_NAME=$(echo "$EXISTING" | jq -r ".data[] | select(.id == \"$wf_id\") | .name")
            echo -n "  Deleting $WF_NAME (id=$wf_id) ... "
            # n8n requires deactivate → archive → delete
            curl -s -b "$COOKIE_JAR" -X PATCH -H "Content-Type: application/json" \
                -d '{"active": false}' "$N8N_URL/rest/workflows/$wf_id" >/dev/null 2>&1
            curl -s -b "$COOKIE_JAR" -X POST "$N8N_URL/rest/workflows/$wf_id/archive" >/dev/null 2>&1
            DEL_RESP=$(curl -s -b "$COOKIE_JAR" -X DELETE "$N8N_URL/rest/workflows/$wf_id")
            if echo "$DEL_RESP" | jq -e '.data' >/dev/null 2>&1; then
                echo "OK"
                DELETED=$((DELETED + 1))
            else
                echo "FAILED"
            fi
        done
        echo "  Deleted $DELETED workflow(s)."
    fi
fi

# ── Discover credential IDs ─────────────────────────────────────────
echo ""
echo "Fetching credentials..."

CREDS_RESP=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/credentials")

# HuggingFace bearer auth — first httpBearerAuth credential (not named OpenRouter)
BEARER_ID=$(echo "$CREDS_RESP" | jq -r '
    [.data[] | select(.type == "httpBearerAuth") | select(.name | test("openrouter|open.router"; "i") | not)] | .[0].id // empty
')

# Telegram API
TELEGRAM_ID=$(echo "$CREDS_RESP" | jq -r '.data[] | select(.type == "telegramApi") | .id' | head -1)

# OpenRouter native credential (for LangChain nodes)
OPENROUTER_API_ID=$(echo "$CREDS_RESP" | jq -r '.data[] | select(.type == "openRouterApi") | .id' | head -1)

# OpenRouter bearer auth — httpBearerAuth credential with "openrouter" in the name (for eval HTTP requests)
OPENROUTER_BEARER_ID=$(echo "$CREDS_RESP" | jq -r '
    [.data[] | select(.type == "httpBearerAuth") | select(.name | test("openrouter|open.router"; "i"))] | .[0].id // empty
')

if [ -z "$BEARER_ID" ] || [ "$BEARER_ID" = "null" ]; then
    echo "WARNING: No HuggingFace Bearer Auth credential found. HF workflows will have PLACEHOLDER."
else
    echo "  HuggingFace Bearer Auth ID: $BEARER_ID"
fi

if [ -z "$TELEGRAM_ID" ] || [ "$TELEGRAM_ID" = "null" ]; then
    echo "WARNING: No Telegram API credential found. Telegram paths will have PLACEHOLDER."
    TELEGRAM_ID=""
else
    echo "  Telegram API credential ID: $TELEGRAM_ID"
fi

if [ -z "$OPENROUTER_API_ID" ] || [ "$OPENROUTER_API_ID" = "null" ]; then
    echo "WARNING: No OpenRouter API credential found. LangChain OpenRouter nodes will have PLACEHOLDER."
    OPENROUTER_API_ID=""
else
    echo "  OpenRouter API credential ID: $OPENROUTER_API_ID"
fi

if [ -z "$OPENROUTER_BEARER_ID" ] || [ "$OPENROUTER_BEARER_ID" = "null" ]; then
    echo "WARNING: No OpenRouter Bearer Auth credential found (need httpBearerAuth with 'openrouter' in name)."
    echo "         OpenRouter Eval will have PLACEHOLDER_OPENROUTER. Set it manually in n8n."
    OPENROUTER_BEARER_ID=""
else
    echo "  OpenRouter Bearer Auth ID: $OPENROUTER_BEARER_ID"
fi

# ── Import workflows ─────────────────────────────────────────────────
echo ""
echo "Importing teacher example workflows..."

SUCCESS=0
FAIL=0

for f in "$WORKFLOW_DIR"/*.json; do
    BASENAME=$(basename "$f")
    echo -n "  $BASENAME ... "

    # Read and patch the workflow JSON
    PATCHED=$(jq \
        --arg bid "${BEARER_ID:-PLACEHOLDER}" \
        --arg tid "${TELEGRAM_ID:-PLACEHOLDER}" \
        --arg orid "${OPENROUTER_API_ID:-PLACEHOLDER}" \
        --arg orbid "${OPENROUTER_BEARER_ID:-PLACEHOLDER_OPENROUTER}" \
        '
        # Remove fields that conflict with import
        del(.id, .versionId) |
        del(.meta.instanceId) |
        # Patch HuggingFace Bearer Auth credential IDs
        (.nodes[] |
            select(.credentials.httpBearerAuth.id == "PLACEHOLDER") |
            .credentials.httpBearerAuth.id) |= $bid |
        # Patch OpenRouter Bearer Auth credential IDs (for eval HTTP requests)
        (.nodes[] |
            select(.credentials.httpBearerAuth.id == "PLACEHOLDER_OPENROUTER") |
            .credentials.httpBearerAuth.id) |= $orbid |
        # Patch Telegram credential IDs
        (.nodes[] |
            select(.credentials.telegramApi.id == "PLACEHOLDER") |
            .credentials.telegramApi.id) |= $tid |
        # Patch OpenRouter API credential IDs (for LangChain nodes)
        (.nodes[] |
            select(.credentials.openRouterApi.id == "PLACEHOLDER") |
            .credentials.openRouterApi.id) |= $orid
        ' "$f")

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
TOTAL=$(ls "$WORKFLOW_DIR"/*.json 2>/dev/null | wc -l)
echo "Done: $SUCCESS imported, $FAIL failed (out of $TOTAL total)"
echo ""
echo "NOTE: All workflows are imported as INACTIVE."
echo "Activate only one Telegram-based workflow at a time (webhook limitation)."
echo "Eval workflows can be run manually (Manual Trigger) without activation."
