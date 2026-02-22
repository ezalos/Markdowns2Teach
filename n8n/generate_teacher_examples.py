# ABOUTME: Generates 5 teacher example n8n workflow JSONs for classroom demos.
# ABOUTME: Covers HuggingFace API, OpenRouter LLM, and a simple HelloWorld workflow.

import json
import uuid
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "workflows")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def uid():
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Shared sentiment dataset (reused by both eval workflows)
# ---------------------------------------------------------------------------

DATASET_SENTIMENT = [
    # 10 POSITIVE
    {"input": "Absolutely love this product, best purchase I've made all year!", "expected": "POSITIVE"},
    {"input": "Fast shipping and the quality exceeded my expectations.", "expected": "POSITIVE"},
    {"input": "My kids are obsessed with this toy, great value for the price.", "expected": "POSITIVE"},
    {"input": "The battery lasts forever and the screen is gorgeous.", "expected": "POSITIVE"},
    {"input": "Customer service was super helpful when I had a question.", "expected": "POSITIVE"},
    {"input": "Surprisingly good for the price, would buy again.", "expected": "POSITIVE"},
    {"input": "Perfect fit and very comfortable, exactly as described.", "expected": "POSITIVE"},
    {"input": "This cookbook has become my go-to, every recipe turns out great.", "expected": "POSITIVE"},
    {"input": "Easy to set up and works right out of the box.", "expected": "POSITIVE"},
    {"input": "Bought this as a gift and they absolutely loved it.", "expected": "POSITIVE"},
    # 10 NEGATIVE
    {"input": "Broke after two days, complete waste of money.", "expected": "NEGATIVE"},
    {"input": "The instructions were impossible to follow and pieces were missing.", "expected": "NEGATIVE"},
    {"input": "Terrible quality, the stitching came apart on the first wash.", "expected": "NEGATIVE"},
    {"input": "Ordered a medium but it fits like an extra small.", "expected": "NEGATIVE"},
    {"input": "The app crashes constantly and support never responds.", "expected": "NEGATIVE"},
    {"input": "Looks nothing like the photos, very misleading listing.", "expected": "NEGATIVE"},
    {"input": "Arrived damaged and the return process was a nightmare.", "expected": "NEGATIVE"},
    {"input": "Way too loud and the build quality feels cheap.", "expected": "NEGATIVE"},
    {"input": "Stopped working after a week and no warranty support.", "expected": "NEGATIVE"},
    {"input": "Paid premium price for something that feels like a dollar store item.", "expected": "NEGATIVE"},
]


# ---------------------------------------------------------------------------
# Shared format expression for HuggingFace classification responses
# ---------------------------------------------------------------------------

FORMAT_CLASSIFICATION = (
    "={{ (() => {\n"
    "  const results = $json[0] || $json;\n"
    "  const lines = (Array.isArray(results) ? results : [results])\n"
    "    .map(r => `${r.label}: ${(r.score * 100).toFixed(1)}%`)\n"
    "    .join('\\n');\n"
    "  return JSON.stringify({ output: lines });\n"
    "})() }}"
)


# ---------------------------------------------------------------------------
# Helper: wrap nodes + connections into a full workflow object
# ---------------------------------------------------------------------------

def _wrap(name, nodes, connections):
    return {
        "name": name,
        "nodes": nodes,
        "pinData": {},
        "connections": connections,
        "active": False,
        "settings": {"executionOrder": "v1", "availableInMCP": False},
        "meta": {"templateCredsSetupCompleted": True},
        "tags": [],
    }


# ---------------------------------------------------------------------------
# 1. TEACHER_EXAMPLE-Prod-HuggingFace (7 nodes)
#    Sentiment via HF DistilBERT API — same structure as template A
# ---------------------------------------------------------------------------

def make_prod_huggingface():
    model_url = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

    nodes = [
        # Telegram Trigger
        {
            "parameters": {"updates": ["message"], "additionalFields": {}},
            "type": "n8n-nodes-base.telegramTrigger",
            "typeVersion": 1.2,
            "position": [0, 300],
            "id": uid(),
            "name": "Telegram Trigger",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
        # Chat Trigger
        {
            "parameters": {"options": {}},
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "typeVersion": 1.4,
            "position": [0, 0],
            "id": uid(),
            "name": "When chat message received",
            "webhookId": uid(),
        },
        # Classify Sentiment (Chat)
        {
            "parameters": {
                "method": "POST",
                "url": model_url,
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": "={{ JSON.stringify({ inputs: $json.chatInput }) }}",
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 0],
            "id": uid(),
            "name": "Classify Sentiment",
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format Response (Chat)
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_CLASSIFICATION},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 0],
            "id": uid(),
            "name": "Format Response",
        },
        # Classify Sentiment (Telegram)
        {
            "parameters": {
                "method": "POST",
                "url": model_url,
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": "={{ JSON.stringify({ inputs: $json.message.text }) }}",
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 300],
            "id": uid(),
            "name": "Classify Sentiment (Telegram)",
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format for Telegram
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_CLASSIFICATION},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 300],
            "id": uid(),
            "name": "Format for Telegram",
        },
        # Send Telegram message
        {
            "parameters": {
                "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
                "text": "={{ $json.output }}",
                "additionalFields": {},
            },
            "type": "n8n-nodes-base.telegram",
            "typeVersion": 1.2,
            "position": [660, 300],
            "id": uid(),
            "name": "Send a text message",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
    ]

    connections = {
        "When chat message received": {
            "main": [[{"node": "Classify Sentiment", "type": "main", "index": 0}]]
        },
        "Classify Sentiment": {
            "main": [[{"node": "Format Response", "type": "main", "index": 0}]]
        },
        "Telegram Trigger": {
            "main": [[{"node": "Classify Sentiment (Telegram)", "type": "main", "index": 0}]]
        },
        "Classify Sentiment (Telegram)": {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap("TEACHER_EXAMPLE-Prod-HuggingFace", nodes, connections)


# ---------------------------------------------------------------------------
# 2. TEACHER_EXAMPLE-Eval-HuggingFace (5 nodes)
#    Eval runner for HF sentiment — same 20-item dataset
# ---------------------------------------------------------------------------

def make_eval_huggingface():
    model_url = "https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    dataset_js = json.dumps(DATASET_SENTIMENT, indent=2)

    load_dataset_code = (
        f"const dataset = {dataset_js};\n"
        "\n"
        "return dataset.map(item => ({json: item}));"
    )

    compute_score_code = (
        'const dataset = $("Load Dataset").all();\n'
        "const responses = $input.all();\n"
        "\n"
        "const details = [];\n"
        "let pass = 0;\n"
        "let fail = 0;\n"
        "\n"
        "for (let i = 0; i < dataset.length; i++) {\n"
        "  const expected = dataset[i].json.expected;\n"
        "  const input = dataset[i].json.input;\n"
        "  const response = responses[i].json;\n"
        "\n"
        "  // HF classification: response is [[{label, score}, ...]] or [{label, score}, ...]\n"
        "  const results = Array.isArray(response[0]) ? response[0] : response;\n"
        "  const predicted = results[0].label;\n"
        "\n"
        '  const status = (predicted.toLowerCase() === expected.toLowerCase()) ? "PASS" : "FAIL";\n'
        '  if (status === "PASS") pass++; else fail++;\n'
        "\n"
        "  details.push({input: input.substring(0, 60), expected, predicted, status});\n"
        "}\n"
        "\n"
        "const total = dataset.length;\n"
        'const accuracy = ((pass / total) * 100).toFixed(1) + "%";\n'
        "\n"
        "return [{json: {total, pass, fail, accuracy, details}}];"
    )

    nodes = [
        {
            "parameters": {},
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [0, 300],
            "id": uid(),
            "name": "Manual Trigger",
        },
        {
            "parameters": {"jsCode": load_dataset_code},
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [220, 300],
            "id": uid(),
            "name": "Load Dataset",
        },
        {
            "parameters": {"batchSize": 1, "options": {}},
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [440, 300],
            "id": uid(),
            "name": "Loop Over Items",
        },
        {
            "parameters": {
                "method": "POST",
                "url": model_url,
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": "={{ JSON.stringify({ inputs: $json.input }) }}",
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [660, 460],
            "id": uid(),
            "name": "Call HuggingFace",
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        {
            "parameters": {"jsCode": compute_score_code},
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [660, 140],
            "id": uid(),
            "name": "Compute Score",
        },
    ]

    connections = {
        "Manual Trigger": {
            "main": [[{"node": "Load Dataset", "type": "main", "index": 0}]]
        },
        "Load Dataset": {
            "main": [[{"node": "Loop Over Items", "type": "main", "index": 0}]]
        },
        "Loop Over Items": {
            "main": [
                [{"node": "Compute Score", "type": "main", "index": 0}],
                [{"node": "Call HuggingFace", "type": "main", "index": 0}],
            ]
        },
        "Call HuggingFace": {
            "main": [[{"node": "Loop Over Items", "type": "main", "index": 0}]]
        },
    }

    return _wrap("TEACHER_EXAMPLE-Eval-HuggingFace", nodes, connections)


# ---------------------------------------------------------------------------
# 3. TEACHER_EXAMPLE-Prod-OpenRouter (~9 nodes)
#    Sentiment via OpenRouter + LangChain structured output
#
#    Chat path: Chat Trigger → Basic LLM Chain (+ sub-nodes: model + parser)
#    Telegram path: Telegram Trigger → Basic LLM Chain TG (+ sub-nodes) → Format → Send
# ---------------------------------------------------------------------------

OPENROUTER_PROMPT = (
    "Classify the sentiment of the following text as POSITIVE or NEGATIVE. "
    "Return JSON with fields: label (string, must be POSITIVE or NEGATIVE) "
    "and confidence (number 0-1).\n\n"
    "Text: {text}"
)

STRUCTURED_OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "label": {
            "type": "string",
            "description": "Sentiment label: POSITIVE or NEGATIVE",
        },
        "confidence": {
            "type": "number",
            "description": "Confidence score between 0 and 1",
        },
    },
    "required": ["label", "confidence"],
}


def make_prod_openrouter():
    # Sub-node IDs need to be stable so connections can reference them
    chat_model_id = uid()
    chat_parser_id = uid()
    chat_chain_id = uid()
    tg_model_id = uid()
    tg_parser_id = uid()
    tg_chain_id = uid()

    nodes = [
        # ---- Chat path ----
        # Chat Trigger
        {
            "parameters": {"options": {}},
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "typeVersion": 1.4,
            "position": [0, 0],
            "id": uid(),
            "name": "When chat message received",
            "webhookId": uid(),
        },
        # Basic LLM Chain (Chat) — prompt uses {text} placeholder
        {
            "parameters": {
                "prompt": "={{ 'Classify the sentiment of the following text as POSITIVE or NEGATIVE. Return JSON with fields: label (string, must be POSITIVE or NEGATIVE) and confidence (number 0-1).\\n\\nText: ' + $json.chatInput }}",
                "hasOutputParser": True,
            },
            "type": "@n8n/n8n-nodes-langchain.chainLlm",
            "typeVersion": 1.4,
            "position": [220, 0],
            "id": chat_chain_id,
            "name": "Classify Sentiment",
        },
        # OpenRouter Chat Model (sub-node for Chat chain)
        {
            "parameters": {
                "model": "mistralai/mistral-small-3.1-24b-instruct:free",
                "options": {},
            },
            "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
            "typeVersion": 1,
            "position": [140, 220],
            "id": chat_model_id,
            "name": "OpenRouter Chat Model",
            "credentials": {
                "openRouterApi": {"id": "PLACEHOLDER", "name": "OpenRouter account"}
            },
        },
        # Structured Output Parser (sub-node for Chat chain)
        {
            "parameters": {
                "schemaType": "manual",
                "inputSchema": json.dumps(STRUCTURED_OUTPUT_SCHEMA),
            },
            "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
            "typeVersion": 1.2,
            "position": [300, 220],
            "id": chat_parser_id,
            "name": "Structured Output Parser",
        },
        # ---- Telegram path ----
        # Telegram Trigger
        {
            "parameters": {"updates": ["message"], "additionalFields": {}},
            "type": "n8n-nodes-base.telegramTrigger",
            "typeVersion": 1.2,
            "position": [0, 500],
            "id": uid(),
            "name": "Telegram Trigger",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
        # Basic LLM Chain (Telegram)
        {
            "parameters": {
                "prompt": "={{ 'Classify the sentiment of the following text as POSITIVE or NEGATIVE. Return JSON with fields: label (string, must be POSITIVE or NEGATIVE) and confidence (number 0-1).\\n\\nText: ' + $json.message.text }}",
                "hasOutputParser": True,
            },
            "type": "@n8n/n8n-nodes-langchain.chainLlm",
            "typeVersion": 1.4,
            "position": [220, 500],
            "id": tg_chain_id,
            "name": "Classify Sentiment (Telegram)",
        },
        # OpenRouter Chat Model (sub-node for TG chain)
        {
            "parameters": {
                "model": "mistralai/mistral-small-3.1-24b-instruct:free",
                "options": {},
            },
            "type": "@n8n/n8n-nodes-langchain.lmChatOpenRouter",
            "typeVersion": 1,
            "position": [140, 720],
            "id": tg_model_id,
            "name": "OpenRouter Chat Model TG",
            "credentials": {
                "openRouterApi": {"id": "PLACEHOLDER", "name": "OpenRouter account"}
            },
        },
        # Structured Output Parser (sub-node for TG chain)
        {
            "parameters": {
                "schemaType": "manual",
                "inputSchema": json.dumps(STRUCTURED_OUTPUT_SCHEMA),
            },
            "type": "@n8n/n8n-nodes-langchain.outputParserStructured",
            "typeVersion": 1.2,
            "position": [300, 720],
            "id": tg_parser_id,
            "name": "Structured Output Parser TG",
        },
        # Format for Telegram — extract label + confidence from chain output
        {
            "parameters": {
                "mode": "raw",
                "jsonOutput": (
                    "={{ (() => {\n"
                    "  const parsed = typeof $json.output === 'string' ? JSON.parse($json.output) : $json.output;\n"
                    "  const label = parsed.label || 'UNKNOWN';\n"
                    "  const confidence = parsed.confidence !== undefined\n"
                    "    ? (parsed.confidence * 100).toFixed(1) + '%'\n"
                    "    : 'N/A';\n"
                    "  return JSON.stringify({ output: `${label} (${confidence})` });\n"
                    "})() }}"
                ),
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 500],
            "id": uid(),
            "name": "Format for Telegram",
        },
        # Send Telegram message
        {
            "parameters": {
                "chatId": "={{ $('Telegram Trigger').item.json.message.chat.id }}",
                "text": "={{ $json.output }}",
                "additionalFields": {},
            },
            "type": "n8n-nodes-base.telegram",
            "typeVersion": 1.2,
            "position": [660, 500],
            "id": uid(),
            "name": "Send a text message",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
    ]

    connections = {
        # Chat path: trigger → chain (chain auto-returns to chat UI)
        "When chat message received": {
            "main": [[{"node": "Classify Sentiment", "type": "main", "index": 0}]]
        },
        # Sub-node connections for Chat chain
        "OpenRouter Chat Model": {
            "ai_languageModel": [[{"node": "Classify Sentiment", "type": "ai_languageModel", "index": 0}]]
        },
        "Structured Output Parser": {
            "ai_outputParser": [[{"node": "Classify Sentiment", "type": "ai_outputParser", "index": 0}]]
        },
        # Telegram path: trigger → chain → format → send
        "Telegram Trigger": {
            "main": [[{"node": "Classify Sentiment (Telegram)", "type": "main", "index": 0}]]
        },
        "Classify Sentiment (Telegram)": {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        # Sub-node connections for TG chain
        "OpenRouter Chat Model TG": {
            "ai_languageModel": [[{"node": "Classify Sentiment (Telegram)", "type": "ai_languageModel", "index": 0}]]
        },
        "Structured Output Parser TG": {
            "ai_outputParser": [[{"node": "Classify Sentiment (Telegram)", "type": "ai_outputParser", "index": 0}]]
        },
        # Format → Send
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap("TEACHER_EXAMPLE-Prod-OpenRouter", nodes, connections)


# ---------------------------------------------------------------------------
# 4. TEACHER_EXAMPLE-Eval-OpenRouter (5 nodes)
#    Eval runner using OpenRouter chat completions API via HTTP Request
# ---------------------------------------------------------------------------

def make_eval_openrouter():
    dataset_js = json.dumps(DATASET_SENTIMENT, indent=2)

    load_dataset_code = (
        f"const dataset = {dataset_js};\n"
        "\n"
        "return dataset.map(item => ({json: item}));"
    )

    # HTTP body for OpenRouter chat completions API
    openrouter_body = (
        '={{ JSON.stringify({\n'
        '  model: "mistralai/mistral-small-3.1-24b-instruct:free",\n'
        '  response_format: { type: "json_object" },\n'
        '  messages: [\n'
        '    {\n'
        '      role: "system",\n'
        '      content: "You are a sentiment classifier. Classify the input text as POSITIVE or NEGATIVE. '
        'Return JSON with fields: label (POSITIVE or NEGATIVE) and confidence (number 0-1). '
        'Return ONLY the JSON object, nothing else."\n'
        '    },\n'
        '    {\n'
        '      role: "user",\n'
        '      content: $json.input\n'
        '    }\n'
        '  ]\n'
        '}) }}'
    )

    compute_score_code = (
        'const dataset = $("Load Dataset").all();\n'
        "const responses = $input.all();\n"
        "\n"
        "const details = [];\n"
        "let pass = 0;\n"
        "let fail = 0;\n"
        "\n"
        "for (let i = 0; i < dataset.length; i++) {\n"
        "  const expected = dataset[i].json.expected;\n"
        "  const input = dataset[i].json.input;\n"
        "  const response = responses[i].json;\n"
        "\n"
        "  // OpenRouter chat completions: parse JSON from message content\n"
        "  let predicted = 'UNKNOWN';\n"
        "  try {\n"
        "    const content = response.choices[0].message.content;\n"
        "    const parsed = JSON.parse(content);\n"
        "    predicted = parsed.label || 'UNKNOWN';\n"
        "  } catch (e) {\n"
        "    predicted = 'PARSE_ERROR';\n"
        "  }\n"
        "\n"
        '  const status = (predicted.toLowerCase() === expected.toLowerCase()) ? "PASS" : "FAIL";\n'
        '  if (status === "PASS") pass++; else fail++;\n'
        "\n"
        "  details.push({input: input.substring(0, 60), expected, predicted, status});\n"
        "}\n"
        "\n"
        "const total = dataset.length;\n"
        'const accuracy = ((pass / total) * 100).toFixed(1) + "%";\n'
        "\n"
        "return [{json: {total, pass, fail, accuracy, details}}];"
    )

    nodes = [
        {
            "parameters": {},
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [0, 300],
            "id": uid(),
            "name": "Manual Trigger",
        },
        {
            "parameters": {"jsCode": load_dataset_code},
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [220, 300],
            "id": uid(),
            "name": "Load Dataset",
        },
        {
            "parameters": {"batchSize": 1, "options": {}},
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [440, 300],
            "id": uid(),
            "name": "Loop Over Items",
        },
        {
            "parameters": {
                "method": "POST",
                "url": "https://openrouter.ai/api/v1/chat/completions",
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": openrouter_body,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [660, 460],
            "id": uid(),
            "name": "Call OpenRouter",
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER_OPENROUTER", "name": "OpenRouter Bearer Auth"}
            },
        },
        {
            "parameters": {"jsCode": compute_score_code},
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [660, 140],
            "id": uid(),
            "name": "Compute Score",
        },
    ]

    connections = {
        "Manual Trigger": {
            "main": [[{"node": "Load Dataset", "type": "main", "index": 0}]]
        },
        "Load Dataset": {
            "main": [[{"node": "Loop Over Items", "type": "main", "index": 0}]]
        },
        "Loop Over Items": {
            "main": [
                [{"node": "Compute Score", "type": "main", "index": 0}],
                [{"node": "Call OpenRouter", "type": "main", "index": 0}],
            ]
        },
        "Call OpenRouter": {
            "main": [[{"node": "Loop Over Items", "type": "main", "index": 0}]]
        },
    }

    return _wrap("TEACHER_EXAMPLE-Eval-OpenRouter", nodes, connections)


# ---------------------------------------------------------------------------
# 5. TEACHER_EXAMPLE-HelloWorld (4 nodes)
#    Simple input → if/else → output
# ---------------------------------------------------------------------------

def make_hello_world():
    nodes = [
        # Chat Trigger
        {
            "parameters": {
                "options": {
                    "responseMessage": "Type something! Try saying 'hello'.",
                },
            },
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "typeVersion": 1.4,
            "position": [0, 300],
            "id": uid(),
            "name": "When chat message received",
            "webhookId": uid(),
        },
        # If node — check if input contains "hello" (case insensitive)
        {
            "parameters": {
                "conditions": {
                    "options": {"caseSensitive": False, "leftValue": "", "typeValidation": "strict"},
                    "conditions": [
                        {
                            "id": uid(),
                            "leftValue": "={{ $json.chatInput.toLowerCase() }}",
                            "rightValue": "hello",
                            "operator": {
                                "type": "string",
                                "operation": "contains",
                            },
                        }
                    ],
                    "combinator": "and",
                },
            },
            "type": "n8n-nodes-base.if",
            "typeVersion": 2.2,
            "position": [220, 300],
            "id": uid(),
            "name": "Contains Hello?",
        },
        # Set — Hello response (true branch)
        {
            "parameters": {
                "mode": "raw",
                "jsonOutput": '={{ JSON.stringify({ output: "Hello World! 👋" }) }}',
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 200],
            "id": uid(),
            "name": "Hello Response",
        },
        # Set — Default response (false branch)
        {
            "parameters": {
                "mode": "raw",
                "jsonOutput": "={{ JSON.stringify({ output: \"I only understand 'hello' — try again!\" }) }}",
            },
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 400],
            "id": uid(),
            "name": "Default Response",
        },
    ]

    connections = {
        "When chat message received": {
            "main": [[{"node": "Contains Hello?", "type": "main", "index": 0}]]
        },
        "Contains Hello?": {
            "main": [
                # Output 0: true → Hello Response
                [{"node": "Hello Response", "type": "main", "index": 0}],
                # Output 1: false → Default Response
                [{"node": "Default Response", "type": "main", "index": 0}],
            ]
        },
    }

    return _wrap("TEACHER_EXAMPLE-HelloWorld", nodes, connections)


# ---------------------------------------------------------------------------
# Generate all 5 workflows
# ---------------------------------------------------------------------------

WORKFLOWS = [
    ("TEACHER_EXAMPLE-Prod-HuggingFace.json", make_prod_huggingface),
    ("TEACHER_EXAMPLE-Eval-HuggingFace.json", make_eval_huggingface),
    ("TEACHER_EXAMPLE-Prod-OpenRouter.json", make_prod_openrouter),
    ("TEACHER_EXAMPLE-Eval-OpenRouter.json", make_eval_openrouter),
    ("TEACHER_EXAMPLE-HelloWorld.json", make_hello_world),
]


def main():
    for filename, gen_fn in WORKFLOWS:
        workflow = gen_fn()
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            json.dump(workflow, f, indent=2)
        node_count = len(workflow["nodes"])
        print(f"  {filename} ({node_count} nodes)")
    print(f"\nAll {len(WORKFLOWS)} teacher example workflows written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
