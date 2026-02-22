# ABOUTME: Generates all 10 n8n workflow JSON files for student projects.
# ABOUTME: Creates 4 template types: text classification, zero-shot, multimodal, and similarity.

import json
import uuid
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "workflows")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def uid():
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Shared format expressions
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

FORMAT_ZERO_SHOT = (
    "={{ (() => {\n"
    "  const labels = $json.labels || [];\n"
    "  const scores = $json.scores || [];\n"
    "  const lines = labels.map((l, i) => "
    "`${l}: ${(scores[i] * 100).toFixed(1)}%`).join('\\n');\n"
    "  return JSON.stringify({ output: lines });\n"
    "})() }}"
)

FORMAT_SIMILARITY = (
    "={{ (() => {\n"
    "  const score = Array.isArray($json) ? $json[0] : $json;\n"
    "  const pct = (score * 100).toFixed(1);\n"
    "  let verdict;\n"
    "  if (score >= 0.7) verdict = 'Strong match';\n"
    "  else if (score >= 0.4) verdict = 'Moderate match';\n"
    "  else verdict = 'Weak match';\n"
    "  return JSON.stringify({ output: `Similarity: ${pct}%\\nVerdict: ${verdict}` });\n"
    "})() }}"
)


# ---------------------------------------------------------------------------
# Template A — Standard text classification (7 nodes)
# ---------------------------------------------------------------------------

def make_template_a(workflow_name, model_id, classify_label):
    """Projects 1, 2, 7, 8, 10."""
    model_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"
    chat_classify = f"Classify {classify_label}"
    tg_classify = f"Classify {classify_label} (Telegram)"

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
        # Classify (Chat)
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
            "name": chat_classify,
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
        # Classify (Telegram)
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
            "name": tg_classify,
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
            "main": [[{"node": chat_classify, "type": "main", "index": 0}]]
        },
        chat_classify: {
            "main": [[{"node": "Format Response", "type": "main", "index": 0}]]
        },
        "Telegram Trigger": {
            "main": [[{"node": tg_classify, "type": "main", "index": 0}]]
        },
        tg_classify: {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap(workflow_name, nodes, connections)


# ---------------------------------------------------------------------------
# Template B — Zero-shot classification (7 nodes)
# ---------------------------------------------------------------------------

def make_template_b(workflow_name, model_id, classify_label, candidate_labels):
    """Projects 3, 6."""
    model_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"
    labels_json = json.dumps(candidate_labels)
    chat_classify = f"Classify {classify_label}"
    tg_classify = f"Classify {classify_label} (Telegram)"

    chat_body = (
        "={{ JSON.stringify({ inputs: $json.chatInput, "
        f"parameters: {{ candidate_labels: {labels_json} }} }}) }}}}"
    )
    tg_body = (
        "={{ JSON.stringify({ inputs: $json.message.text, "
        f"parameters: {{ candidate_labels: {labels_json} }} }}) }}}}"
    )

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
        # Classify (Chat)
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
                "jsonBody": chat_body,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 0],
            "id": uid(),
            "name": chat_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format Response (Chat)
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_ZERO_SHOT},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 0],
            "id": uid(),
            "name": "Format Response",
        },
        # Classify (Telegram)
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
                "jsonBody": tg_body,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 300],
            "id": uid(),
            "name": tg_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format for Telegram
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_ZERO_SHOT},
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
            "main": [[{"node": chat_classify, "type": "main", "index": 0}]]
        },
        chat_classify: {
            "main": [[{"node": "Format Response", "type": "main", "index": 0}]]
        },
        "Telegram Trigger": {
            "main": [[{"node": tg_classify, "type": "main", "index": 0}]]
        },
        tg_classify: {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap(workflow_name, nodes, connections)


# ---------------------------------------------------------------------------
# Template C — Multimodal / binary input (10 nodes)
# ---------------------------------------------------------------------------

def make_template_c(workflow_name, model_id, classify_label, input_type, tg_file_id_expr):
    """Projects 4, 5. Chat accepts a URL; Telegram accepts a file upload."""
    model_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"
    chat_classify = f"Classify {classify_label}"
    tg_classify = f"Classify {classify_label} (Telegram)"

    nodes = [
        # ---- Chat path (4 nodes) ----
        # Chat Trigger
        {
            "parameters": {
                "options": {
                    "responseMessage": f"Send me a URL to a {input_type} file and I'll classify it."
                }
            },
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "typeVersion": 1.4,
            "position": [0, 0],
            "id": uid(),
            "name": "When chat message received",
            "webhookId": uid(),
        },
        # Download File (from URL the user pasted)
        {
            "parameters": {
                "method": "GET",
                "url": "={{ $json.chatInput }}",
                "options": {"response": {"response": {"responseFormat": "file"}}},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 0],
            "id": uid(),
            "name": "Download File",
        },
        # Classify (Chat) — binary POST to HuggingFace
        {
            "parameters": {
                "method": "POST",
                "url": model_url,
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "contentType": "binaryData",
                "sendBody": True,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [440, 0],
            "id": uid(),
            "name": chat_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format Response (Chat)
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_CLASSIFICATION},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [660, 0],
            "id": uid(),
            "name": "Format Response",
        },
        # ---- Telegram path (6 nodes) ----
        # Telegram Trigger
        {
            "parameters": {
                "updates": ["message"],
                "additionalFields": {},
            },
            "type": "n8n-nodes-base.telegramTrigger",
            "typeVersion": 1.2,
            "position": [0, 400],
            "id": uid(),
            "name": "Telegram Trigger",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
        # Get File Info (Telegram API getFile)
        {
            "parameters": {
                "method": "POST",
                "url": "=https://api.telegram.org/bot__TELEGRAM_BOT_TOKEN__/getFile",
                "sendBody": True,
                "specifyBody": "json",
                "jsonBody": f"={{{{ JSON.stringify({{ file_id: {tg_file_id_expr} }}) }}}}",
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 400],
            "id": uid(),
            "name": "Get File Info",
        },
        # Download File (Telegram) — download from Telegram file API
        {
            "parameters": {
                "method": "GET",
                "url": "=https://api.telegram.org/file/bot__TELEGRAM_BOT_TOKEN__/{{ $json.result.file_path }}",
                "options": {"response": {"response": {"responseFormat": "file"}}},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [440, 400],
            "id": uid(),
            "name": "Download File (Telegram)",
        },
        # Classify (Telegram) — binary POST to HuggingFace
        {
            "parameters": {
                "method": "POST",
                "url": model_url,
                "authentication": "genericCredentialType",
                "genericAuthType": "httpBearerAuth",
                "sendHeaders": True,
                "headerParameters": {"parameters": [{}]},
                "contentType": "binaryData",
                "sendBody": True,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [660, 400],
            "id": uid(),
            "name": tg_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format for Telegram
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_CLASSIFICATION},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [880, 400],
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
            "position": [1100, 400],
            "id": uid(),
            "name": "Send a text message",
            "webhookId": uid(),
            "credentials": {
                "telegramApi": {"id": "PLACEHOLDER", "name": "Telegram account"}
            },
        },
    ]

    connections = {
        # Chat path
        "When chat message received": {
            "main": [[{"node": "Download File", "type": "main", "index": 0}]]
        },
        "Download File": {
            "main": [[{"node": chat_classify, "type": "main", "index": 0}]]
        },
        chat_classify: {
            "main": [[{"node": "Format Response", "type": "main", "index": 0}]]
        },
        # Telegram path
        "Telegram Trigger": {
            "main": [[{"node": "Get File Info", "type": "main", "index": 0}]]
        },
        "Get File Info": {
            "main": [[{"node": "Download File (Telegram)", "type": "main", "index": 0}]]
        },
        "Download File (Telegram)": {
            "main": [[{"node": tg_classify, "type": "main", "index": 0}]]
        },
        tg_classify: {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap(workflow_name, nodes, connections)


# ---------------------------------------------------------------------------
# Template D — Sentence similarity (7 nodes)
# ---------------------------------------------------------------------------

SAMPLE_JOB_DESC = (
    "We are looking for a software engineer with experience in Python, "
    "machine learning, and cloud computing. The ideal candidate has "
    "worked with TensorFlow or PyTorch, understands CI/CD pipelines, "
    "and can communicate technical concepts to non-technical stakeholders."
)


def make_template_d(workflow_name, model_id, classify_label):
    """Project 9."""
    model_url = f"https://router.huggingface.co/hf-inference/models/{model_id}"
    chat_classify = f"Classify {classify_label}"
    tg_classify = f"Classify {classify_label} (Telegram)"

    job_escaped = json.dumps(SAMPLE_JOB_DESC)  # already quoted string

    chat_body = (
        "={{ JSON.stringify({ inputs: { "
        f"source_sentence: {job_escaped}, "
        "sentences: [$json.chatInput] } }) }}"
    )
    tg_body = (
        "={{ JSON.stringify({ inputs: { "
        f"source_sentence: {job_escaped}, "
        "sentences: [$json.message.text] } }) }}"
    )

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
            "parameters": {
                "options": {
                    "responseMessage": (
                        "Paste a resume or CV text and I'll score it against "
                        "a sample job description."
                    )
                }
            },
            "type": "@n8n/n8n-nodes-langchain.chatTrigger",
            "typeVersion": 1.4,
            "position": [0, 0],
            "id": uid(),
            "name": "When chat message received",
            "webhookId": uid(),
        },
        # Classify (Chat)
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
                "jsonBody": chat_body,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 0],
            "id": uid(),
            "name": chat_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format Response (Chat)
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_SIMILARITY},
            "type": "n8n-nodes-base.set",
            "typeVersion": 3.4,
            "position": [440, 0],
            "id": uid(),
            "name": "Format Response",
        },
        # Classify (Telegram)
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
                "jsonBody": tg_body,
                "options": {},
            },
            "type": "n8n-nodes-base.httpRequest",
            "typeVersion": 4.3,
            "position": [220, 300],
            "id": uid(),
            "name": tg_classify,
            "credentials": {
                "httpBearerAuth": {"id": "PLACEHOLDER", "name": "Bearer Auth account"}
            },
        },
        # Format for Telegram
        {
            "parameters": {"mode": "raw", "jsonOutput": FORMAT_SIMILARITY},
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
            "main": [[{"node": chat_classify, "type": "main", "index": 0}]]
        },
        chat_classify: {
            "main": [[{"node": "Format Response", "type": "main", "index": 0}]]
        },
        "Telegram Trigger": {
            "main": [[{"node": tg_classify, "type": "main", "index": 0}]]
        },
        tg_classify: {
            "main": [[{"node": "Format for Telegram", "type": "main", "index": 0}]]
        },
        "Format for Telegram": {
            "main": [[{"node": "Send a text message", "type": "main", "index": 0}]]
        },
    }

    return _wrap(workflow_name, nodes, connections)


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
# Define all 10 projects and generate
# ---------------------------------------------------------------------------

WORKFLOWS = [
    # (filename, generator_call)
    (
        "01-sentiment-reviews.json",
        lambda: make_template_a(
            "01 — Sentiment Analysis for Reviews",
            "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
            "Sentiment",
        ),
    ),
    (
        "02-content-moderation.json",
        lambda: make_template_a(
            "02 — Content Moderation (Toxic-BERT)",
            "unitary/toxic-bert",
            "Toxicity",
        ),
    ),
    (
        "03-product-category.json",
        lambda: make_template_b(
            "03 — Product Category Classification",
            "facebook/bart-large-mnli",
            "Category",
            ["electronics", "clothing", "home", "sports"],
        ),
    ),
    (
        "04-audio-genre.json",
        lambda: make_template_c(
            "04 — Audio Genre Classification",
            "MIT/ast-finetuned-audioset-10-10-0.4593",
            "Audio Genre",
            "audio",
            "$json.message.audio ? $json.message.audio.file_id : $json.message.voice.file_id",
        ),
    ),
    (
        "05-plant-disease.json",
        lambda: make_template_c(
            "05 — Plant Disease Detection",
            "linkanjarad/mobilenet_v2_1.0_224-plant-disease-identification",
            "Plant Disease",
            "image",
            "$json.message.photo[$json.message.photo.length - 1].file_id",
        ),
    ),
    (
        "06-intent-classification.json",
        lambda: make_template_b(
            "06 — Intent Classification",
            "facebook/bart-large-mnli",
            "Intent",
            ["billing", "technical support", "returns", "general inquiry"],
        ),
    ),
    (
        "07-hate-speech.json",
        lambda: make_template_a(
            "07 — Hate Speech Detection",
            "facebook/roberta-hate-speech-dynabench-r4-target",
            "Hate Speech",
        ),
    ),
    (
        "08-email-spam.json",
        lambda: make_template_a(
            "08 — Email Spam Detection",
            "mshenoda/roberta-spam",
            "Spam",
        ),
    ),
    (
        "09-resume-screening.json",
        lambda: make_template_d(
            "09 — Resume Screening",
            "sentence-transformers/all-MiniLM-L6-v2",
            "Resume Match",
        ),
    ),
    (
        "10-social-media-sentiment.json",
        lambda: make_template_a(
            "10 — Social Media Sentiment",
            "cardiffnlp/twitter-roberta-base-sentiment-latest",
            "Social Sentiment",
        ),
    ),
]


def main():
    for filename, gen_fn in WORKFLOWS:
        workflow = gen_fn()
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            json.dump(workflow, f, indent=2)
        node_count = len(workflow["nodes"])
        print(f"  {filename} ({node_count} nodes)")
    print(f"\nAll {len(WORKFLOWS)} workflows written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
