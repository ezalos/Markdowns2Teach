# n8n Agent Demo — Design Spec

## Goal

Build two educational n8n workflows demonstrating how AI agents work, for the teacher account on `https://n8n.develle.fr`. The pair shows the same concept (tool-calling agent) at two levels of abstraction:

1. **TEACHER_EXAMPLE-Agent-Simple** — n8n's built-in AI Agent node (black box)
2. **TEACHER_EXAMPLE-Agent-Manual** — explicit ReAct loop with visible nodes (white box)

## Context

- **Course**: Session 3B — "Agents IA : du workflow à l'autonomie"
- **Audience**: M2 business students, non-engineers, already familiar with n8n from Sessions 1–2
- **Purpose**: demonstrate Think→Act→Observe cycle, tool calling, and agent routing
- **Demo flow**: show Workflow 1 ("magic") → "but how does it work?" → Workflow 2 ("under the hood")

## Shared Configuration

- **LLM**: OpenRouter via `mistralai/mistral-small-3.1-24b-instruct:free`
- **Credential**: reuse existing OpenRouter credential from teacher account (query via API)
- **Trigger**: Chat Trigger (n8n chat widget for live demo)
- **Tools**: Calculator + Wikipedia (zero extra API keys)
- **Temperature**: 0 (deterministic for demo reliability)
- **Language**: French responses

### Test Cases

| Input | Expected Tool | Expected Behavior |
|-------|--------------|-------------------|
| "Combien font 15% de 847 ?" | Calculator | Returns 127.05 |
| "Qui est Alan Turing ?" | Wikipedia | Returns biography summary |
| "Quelle est la population de la France ?" | Wikipedia | Returns ~68M figure |

## Workflow 1: TEACHER_EXAMPLE-Agent-Simple

### Architecture

3 visible nodes + 3 sub-nodes:

```
Chat Trigger → AI Agent → (auto-response to chat)
                  ├── OpenAI Chat Model (OpenRouter)
                  ├── Calculator Tool
                  └── Wikipedia Tool
```

### Nodes

| Node | Type | Config |
|------|------|--------|
| Chat Trigger | `@n8n/n8n-nodes-langchain.chatTrigger` | Default |
| AI Agent | `@n8n/n8n-nodes-langchain.agent` | System prompt (French), agent type: tools agent |
| OpenAI Chat Model | `@n8n/n8n-nodes-langchain.lmChatOpenAi` | Base URL: `https://openrouter.ai/api/v1`, model: `mistralai/mistral-small-3.1-24b-instruct:free`, temp: 0 |
| Calculator | `@n8n/n8n-nodes-langchain.toolCalculator` | Default |
| Wikipedia | `@n8n/n8n-nodes-langchain.toolWikipedia` | Default |

### System Prompt

```
Tu es un assistant intelligent. Tu as accès à un calculateur et à Wikipedia.
Utilise tes outils quand c'est pertinent. Réponds en français.
```

## Workflow 2: TEACHER_EXAMPLE-Agent-Manual

### Architecture

~11 nodes, explicit single-round ReAct loop:

```
Chat Trigger
  → Code: "Build Request"
  → HTTP Request: "Call LLM"
  → Code: "Parse Response"
  → Switch: "Tool or Answer?"
      ├─ [tool_call] → Switch: "Which Tool?"
      │     ├─ "calculator" → Code: "Calculator"
      │     └─ "wikipedia"  → HTTP Request: "Wikipedia API"
      │   → Code: "Build Tool Result"
      │   → HTTP Request: "Call LLM Again"
      │   → Respond to Chat
      └─ [final_answer] → Respond to Chat
```

### Nodes Detail

| Node | Type | Purpose |
|------|------|---------|
| Chat Trigger | chatTrigger | Receives user message |
| Build Request | Code | Constructs `messages` array (including system prompt) + `tools` JSON schema |
| Call LLM | HTTP Request | POST to OpenRouter `/chat/completions` with tools |
| Parse Response | Code | Extracts `tool_calls[0]` or `content` from response |
| Tool or Answer? | Switch | Routes on presence of `tool_calls` |
| Which Tool? | Switch | Routes on `tool_calls[0].function.name` |
| Calculator | Code | Evaluates math expression using basic arithmetic parsing (demo-only, teacher-controlled input) |
| Wikipedia API | HTTP Request | GET `fr.wikipedia.org/api/rest_v1/page/summary/{title}` (French Wikipedia; `query` param maps to `{title}` path segment) |
| Build Tool Result | Code | Formats tool result as OpenAI tool message |
| Call LLM Again | HTTP Request | Second POST with original messages + tool call + tool result |
| Respond to Chat | `@n8n/n8n-nodes-langchain.chainRespondToChat` | Returns final answer to chat widget |

### Tool Definitions (in Build Request node)

```json
[
  {
    "type": "function",
    "function": {
      "name": "calculator",
      "description": "Evaluate a mathematical expression",
      "parameters": {
        "type": "object",
        "properties": {
          "expression": {
            "type": "string",
            "description": "The math expression to evaluate, e.g. '0.15 * 847'"
          }
        },
        "required": ["expression"]
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "wikipedia",
      "description": "Search Wikipedia for information about a topic",
      "parameters": {
        "type": "object",
        "properties": {
          "query": {
            "type": "string",
            "description": "The topic to search on Wikipedia"
          }
        },
        "required": ["query"]
      }
    }
  }
]
```

### Limitation

Single round of tool calling — handles 1 tool call per query. This is intentional: keeps the visual flow clear and motivates *why* the AI Agent node (Workflow 1) exists.

### Error Handling

Minimal error paths for live demo reliability:
- **LLM returns malformed response** (no `tool_calls` and no `content`): Parse Response node returns a fallback error message → Respond to Chat with "Erreur : réponse inattendue du modèle"
- **Wikipedia 404** (topic not found): Wikipedia API node → on error, return "Aucun article trouvé" as tool result → LLM handles gracefully
- **Calculator invalid expression**: wrap evaluation in try/catch, return "Expression invalide" as tool result
- **OpenRouter 429/500**: HTTP Request nodes configured with "Continue on Error" for graceful failure message

### System Prompt (Build Request node)

Same as Workflow 1 for behavioral parity:
```
Tu es un assistant intelligent. Tu as accès à un calculateur et à Wikipedia.
Utilise tes outils quand c'est pertinent. Réponds en français.
```

## Implementation Plan

1. **API discovery**: GET `/credentials` and `/workflows` to find OpenRouter credential ID and understand existing structure
2. **Build Workflow 1 JSON** locally → POST `/workflows` → activate → test via chat
3. **Build Workflow 2 JSON** locally → POST `/workflows` → activate → test via chat
4. **Iterate** on any credential/model/parsing issues

## API Details

- **Base URL**: `https://n8n.develle.fr/api/v1`
- **Auth**: API key via `X-N8N-API-KEY` header (preferred). If no API key exists, fall back to session-based login with `N8N_EMAIL` / `N8N_PASSWORD` from `.envrc`
- **Key endpoints**: `GET /credentials`, `GET /workflows`, `POST /workflows`, `POST /workflows/{id}/activate`

## Success Criteria

All 3 test cases pass on both workflows in consecutive runs:
1. Calculator query returns correct numeric result
2. Wikipedia queries return relevant French-language summaries
3. No errors in the n8n execution log
