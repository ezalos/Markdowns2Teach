<!-- ABOUTME: Documentation for the n8n workflow automation setup and local API interaction. -->
<!-- ABOUTME: Covers Docker access, REST API authentication, workflow management, and the RAG demo. -->

# n8n — Workflow Automation for M2 Course

## Local Access

The n8n instance runs in Docker (`n8n-n8n-1`) on port 5678, exposed externally via Cloudflare Tunnel at `https://n8n.develle.fr`.

**From the local machine**, access n8n via the Docker network IP:

```bash
# Find the container IP
docker inspect n8n-n8n-1 --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'
# → typically 172.19.0.3

N8N_URL="http://172.19.0.3:5678"
```

Port 5678 is NOT mapped to the host — you must use the container IP.

## Cloudflare Access (Zero Trust)

The domain `n8n.develle.fr` is protected by Cloudflare Access to prevent unauthorized access and DDoS attacks (the previous ngrok setup was vulnerable to this).

**What's protected (requires Cloudflare login):**
- The n8n editor UI (`/`)
- The REST API (`/rest/*`)

**What's bypassed (publicly accessible):**
- Production webhooks (`/webhook/*`)
- Test webhooks (`/webhook-test/*`)

The bypass is configured as a separate Access Application in the Cloudflare Zero Trust dashboard with path `webhook*` and a Bypass policy for Everyone. This is safe because webhook URLs contain random IDs and are only active when a workflow is activated.

**If students report webhooks returning HTML instead of JSON**, check that the bypass application still exists in Access → Applications.

## REST API Authentication

n8n v2.x uses cookie-based session auth on the internal `/rest/` API.

### Login

```bash
COOKIE_JAR=$(mktemp)
curl -s -c "$COOKIE_JAR" \
  -H "Content-Type: application/json" \
  -d '{"emailOrLdapLoginId": "louis@sorbonne.fr", "password": "N8n-Sorbonne-2026"}' \
  "$N8N_URL/rest/login"
```

Use `-b "$COOKIE_JAR"` on all subsequent requests.

### Key Endpoints

| Action | Method | Endpoint |
|--------|--------|----------|
| List workflows | GET | `/rest/workflows` |
| Get workflow | GET | `/rest/workflows/{id}` |
| Create workflow | POST | `/rest/workflows` |
| Update workflow | PATCH | `/rest/workflows/{id}` |
| Delete workflow | DELETE | `/rest/workflows/{id}` |
| **Activate** | POST | `/rest/workflows/{id}/activate` |
| **Deactivate** | POST | `/rest/workflows/{id}/deactivate` |
| List credentials | GET | `/rest/credentials` |
| List executions | GET | `/rest/executions?limit=N` |
| Get execution | GET | `/rest/executions/{id}?includeData=true` |

### Activate a Workflow

Requires the `versionId` (get it from `GET /rest/workflows/{id}`):

```bash
# Get versionId
VERSION_ID=$(curl -s -b "$COOKIE_JAR" "$N8N_URL/rest/workflows/$WF_ID" \
  | jq -r '.data.versionId')

# Activate
curl -s -b "$COOKIE_JAR" -X POST \
  -H "Content-Type: application/json" \
  -d "{\"versionId\": \"$VERSION_ID\"}" \
  "$N8N_URL/rest/workflows/$WF_ID/activate"
```

**Note:** `PATCH` with `{"active": true}` does NOT work in n8n v2.x — use the dedicated `/activate` endpoint.

### Import a Workflow

```bash
# Patch credential placeholders and import
PATCHED=$(jq --arg orid "$OPENROUTER_ID" \
  '(.nodes[] | select(.credentials.openRouterApi.id == "PLACEHOLDER") | .credentials.openRouterApi.id) |= $orid' \
  workflows/MY_WORKFLOW.json)

echo "$PATCHED" | curl -s -b "$COOKIE_JAR" \
  -H "Content-Type: application/json" \
  -d @- "$N8N_URL/rest/workflows"
```

## Deploy Scripts

### deploy-workflows.sh — Owner-level deploy

Imports teacher example workflows into the **owner's project** with credential patching.

```bash
N8N_URL="http://172.19.0.3:5678" ./deploy-workflows.sh        # Import all
N8N_URL="http://172.19.0.3:5678" ./deploy-workflows.sh --clean # Delete all, then import
```

### deploy-to-groups.sh — Per-group deploy

Imports teacher example workflows into **each group's personal project** by logging in as each group. Does not create accounts, change passwords, or delete existing workflows.

```bash
N8N_URL="http://172.19.0.3:5678" ./deploy-to-groups.sh
```

Reads credentials from `.private/n8n/group-credentials.csv` (gitignored). Workflows import with PLACEHOLDER credential IDs — students configure their own API keys.

## RAG Demo Workflow

`TEACHER_EXAMPLE-RAG-Wikipedia.json` — a simple RAG system using Wikipedia articles.

### Add a Document

```bash
curl -X POST "$N8N_URL/webhook/rag-add-doc" \
  -H "Content-Type: application/json" \
  -d '{"article": "Machine_learning"}'
# → {"success": true, "title": "Machine learning", "doc_count": 1}
```

### Search

```bash
curl -X POST "$N8N_URL/webhook/rag-search" \
  -H "Content-Type: application/json" \
  -d '{"query": "What is deep learning?"}'
# → {"query": "...", "answer": "...", "sources": [...], "doc_count": 12}
```

### Load Full Corpus

```bash
for a in Machine_learning Deep_learning Artificial_intelligence \
  Natural_language_processing Large_language_model \
  "Transformer_(deep_learning_architecture)" \
  Retrieval-augmented_generation "Neural_network_(machine_learning)" \
  Generative_artificial_intelligence Computer_vision \
  Reinforcement_learning Prompt_engineering; do
  curl -s -X POST "$N8N_URL/webhook/rag-add-doc" \
    -H "Content-Type: application/json" -d "{\"article\": \"$a\"}"
  sleep 0.5
done
```

### Architecture

```
[Add Document]  Webhook POST /rag-add-doc
                  → HTTP Request (Wikipedia REST API)
                  → Code: store in workflow static data

[Search]        Webhook POST /rag-search
                  → Code: TF-IDF search (pure JS, ~50 lines)
                  → HTTP Request (OpenRouter API)
                  → Code: extract and format response

[Init Corpus]   Manual Trigger (in n8n UI)
                  → Code: 12 article slugs
                  → SplitInBatches → HTTP Wikipedia → Code: store
```

### Notes

- Documents persist in `$getWorkflowStaticData('global')` — survives across executions while n8n runs, resets on container restart
- TF-IDF search is pure JavaScript (no imports) — tokenize, term frequency, inverse document frequency, rank
- OpenRouter free tier: 50 req/day on `:free` models. With $10 credit: 1000 req/day
- Wikipedia API requires a `User-Agent` header (returns 403 without it)

## n8n API Documentation

Official docs: https://docs.n8n.io/api/

The Swagger UI is available at `$N8N_URL/api/v1/docs` (requires API key setup in Settings → API).

The internal `/rest/` API is undocumented but matches the n8n source at:
https://github.com/n8n-io/n8n/tree/master/packages/cli/src
