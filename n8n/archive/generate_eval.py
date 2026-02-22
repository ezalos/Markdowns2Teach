# ABOUTME: Generates n8n evaluation workflow JSON files for testing HuggingFace models.
# ABOUTME: Creates test runner workflows with embedded datasets for projects 01 and 03.

import json
import uuid
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "workflows")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def uid():
    return str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Datasets — 20 items each
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

DATASET_PRODUCT_CATEGORY = [
    # 5 electronics
    {"input": "Wireless Bluetooth noise-cancelling headphones with 30h battery", "expected": "electronics"},
    {"input": "USB-C fast charger 65W for laptops and phones", "expected": "electronics"},
    {"input": "4K webcam with built-in microphone for video calls", "expected": "electronics"},
    {"input": "Portable SSD 1TB external hard drive", "expected": "electronics"},
    {"input": "Smart LED desk lamp with adjustable brightness", "expected": "electronics"},
    # 5 clothing
    {"input": "Men's slim fit cotton Oxford button-down shirt", "expected": "clothing"},
    {"input": "Women's waterproof winter parka with faux fur hood", "expected": "clothing"},
    {"input": "Casual linen trousers for summer", "expected": "clothing"},
    {"input": "Merino wool crew neck sweater", "expected": "clothing"},
    {"input": "Leather belt with brushed nickel buckle", "expected": "clothing"},
    # 5 home
    {"input": "Stainless steel French press coffee maker 1 litre", "expected": "home"},
    {"input": "Memory foam bed pillow set of 2", "expected": "home"},
    {"input": "Non-stick ceramic frying pan 28cm", "expected": "home"},
    {"input": "Bamboo bathroom organizer shelf unit", "expected": "home"},
    {"input": "Scented soy candle lavender 200g", "expected": "home"},
    # 5 sports
    {"input": "Yoga mat extra thick 6mm with carrying strap", "expected": "sports"},
    {"input": "Adjustable dumbbells set 2-20kg per hand", "expected": "sports"},
    {"input": "Cycling gloves with gel padding and breathable mesh", "expected": "sports"},
    {"input": "Insulated water bottle 750ml for hiking", "expected": "sports"},
    {"input": "Resistance bands set of 5 with different strengths", "expected": "sports"},
]


# ---------------------------------------------------------------------------
# Eval workflow builder
# ---------------------------------------------------------------------------

def make_eval_workflow(workflow_name, model_url, dataset, body_template, score_extractor):
    """Build a 5-node eval workflow: Trigger → Load Dataset → Loop → HTTP → Score.

    Args:
        workflow_name: Display name in n8n.
        model_url: Full HuggingFace inference URL.
        dataset: List of {input, expected} dicts.
        body_template: JS expression for the HTTP request body.
            Use {{INPUT}} as placeholder for the input field reference.
        score_extractor: JS code that extracts the predicted label from the API
            response item. Should assign to `predicted` variable.
    """
    # Node IDs (needed for connections by name, but n8n uses node names)
    dataset_js = json.dumps(dataset, indent=2)

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
        f"  {score_extractor}\n"
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
        # Node 1: Manual Trigger
        {
            "parameters": {},
            "type": "n8n-nodes-base.manualTrigger",
            "typeVersion": 1,
            "position": [0, 300],
            "id": uid(),
            "name": "Manual Trigger",
        },
        # Node 2: Load Dataset (Code)
        {
            "parameters": {
                "jsCode": load_dataset_code,
            },
            "type": "n8n-nodes-base.code",
            "typeVersion": 2,
            "position": [220, 300],
            "id": uid(),
            "name": "Load Dataset",
        },
        # Node 3: Loop Over Items (splitInBatches)
        {
            "parameters": {
                "batchSize": 1,
                "options": {},
            },
            "type": "n8n-nodes-base.splitInBatches",
            "typeVersion": 3,
            "position": [440, 300],
            "id": uid(),
            "name": "Loop Over Items",
        },
        # Node 4: Call HuggingFace (HTTP Request)
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
                "jsonBody": body_template,
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
        # Node 5: Compute Score (Code)
        {
            "parameters": {
                "jsCode": compute_score_code,
            },
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
                # Output 0: done → Compute Score
                [{"node": "Compute Score", "type": "main", "index": 0}],
                # Output 1: loop → Call HuggingFace
                [{"node": "Call HuggingFace", "type": "main", "index": 0}],
            ]
        },
        "Call HuggingFace": {
            "main": [[{"node": "Loop Over Items", "type": "main", "index": 0}]]
        },
    }

    return _wrap(workflow_name, nodes, connections)


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
# Define eval workflows
# ---------------------------------------------------------------------------

EVAL_WORKFLOWS = [
    # Project 01 — Sentiment Analysis (Template A)
    (
        "eval-01-sentiment.json",
        lambda: make_eval_workflow(
            workflow_name="Eval 01 — Sentiment Analysis",
            model_url="https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english",
            dataset=DATASET_SENTIMENT,
            body_template='={{ JSON.stringify({ inputs: $json.input }) }}',
            score_extractor=(
                "// Template A: response is [[{label, score}, ...]] or [{label, score}, ...]\n"
                "const results = Array.isArray(response[0]) ? response[0] : response;\n"
                "const predicted = results[0].label;"
            ),
        ),
    ),
    # Project 03 — Product Category (Template B, zero-shot)
    (
        "eval-03-product-category.json",
        lambda: make_eval_workflow(
            workflow_name="Eval 03 — Product Category",
            model_url="https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli",
            dataset=DATASET_PRODUCT_CATEGORY,
            body_template=(
                '={{ JSON.stringify({ inputs: $json.input, '
                'parameters: { candidate_labels: ["electronics", "clothing", "home", "sports"] } }) }}'
            ),
            score_extractor=(
                "// Template B: response is {labels: [...], scores: [...]}, sorted desc\n"
                "const predicted = response.labels[0];"
            ),
        ),
    ),
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    for filename, gen_fn in EVAL_WORKFLOWS:
        workflow = gen_fn()
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, "w") as f:
            json.dump(workflow, f, indent=2)
        node_count = len(workflow["nodes"])
        print(f"  {filename} ({node_count} nodes)")
    print(f"\nAll {len(EVAL_WORKFLOWS)} eval workflows written to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
