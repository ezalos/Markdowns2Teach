<!-- ABOUTME: Guide for using the official PaperBanana (dwzhu-pku) for academic diagram generation. -->
<!-- ABOUTME: Covers installation, configuration, JSON input format, CLI usage, image extraction, and gotchas. -->

# Official PaperBanana (dwzhu-pku) — Usage Guide

Reference for running the **original** PaperBanana by Dawei Zhu et al. (Google Research),
installed at `/home/ezalos/42/PaperBanana`.

**Repo**: [dwzhu-pku/PaperBanana](https://github.com/dwzhu-pku/PaperBanana)
**Paper**: [arXiv:2601.23265](https://huggingface.co/papers/2601.23265)
**License**: Apache-2.0

---

## 1. Installation

```bash
cd /home/ezalos/42
git clone https://github.com/dwzhu-pku/PaperBanana.git
cd PaperBanana

# Create venv with Python 3.12
uv venv --python 3.12
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### Dependencies (requirements.txt)

google-genai, streamlit, aiofiles, pillow, numpy, tqdm, json_repair, anthropic,
openai, matplotlib, python-dotenv, pyyaml, google-auth.

---

## 2. Configuration

### API Key

Set `GOOGLE_API_KEY` as an environment variable. If you use `.envrc` from
Markdowns2Teach, it already exports `GOOGLE_API_KEY` from `GEMINI_API_KEY`.

```bash
export GOOGLE_API_KEY="AIzaSy..."
```

### Model Config

Create `configs/model_config.yaml` (gitignored):

```yaml
defaults:
  model_name: "gemini-2.0-flash"
  image_model_name: "gemini-3-pro-image-preview"

api_keys:
  google_api_key: ""  # loaded from GOOGLE_API_KEY env var
  openai_api_key: ""
  anthropic_api_key: ""
```

**Available Gemini image models** (as of 2026-02-28):
- `gemini-3-pro-image-preview` — recommended, best quality
- `gemini-2.5-flash-image` — faster, lower quality
- `gemini-3.1-flash-image-preview` — experimental

> **Warning**: `gemini-2.0-flash-preview-image-generation` returns 404. Don't use it.

---

## 3. Pipeline Architecture

```
Retriever → Planner → (Stylist) → Visualizer ↔ Critic (×N rounds)
```

| Agent | Role | Model |
|-------|------|-------|
| **Retriever** | Selects reference examples from PaperBananaBench (few-shot) | VLM (gemini-2.0-flash) |
| **Planner** | Converts method text + caption into detailed diagram description | VLM |
| **Stylist** | Refines description with NeurIPS-grade aesthetics | VLM |
| **Visualizer** | Renders the description as an image | Image gen (gemini-3-pro-image-preview) |
| **Critic** | Evaluates the image, suggests fixes, produces revised description | VLM |

The Visualizer ↔ Critic loop runs up to N rounds (default 3). If the Critic says
"No changes needed", the loop stops early.

---

## 4. Experiment Modes

| Mode | Pipeline | Evaluation |
|------|----------|------------|
| `vanilla` | Direct generation, no planning | Yes |
| `dev_planner` | Retriever → Planner → Visualizer | Yes |
| `dev_planner_stylist` | Retriever → Planner → Stylist → Visualizer | Yes |
| `dev_planner_critic` | Retriever → Planner → Visualizer → Critic loop | Yes |
| `dev_full` | Full pipeline (all agents) | Yes |
| **`demo_planner_critic`** | Planner → Visualizer → Critic loop | **No** |
| **`demo_full`** | Full pipeline | **No** |

Use **`demo_*` modes** for custom inputs (no ground truth needed).
Use **`dev_*` modes** for benchmark evaluation against PaperBananaBench.

---

## 5. Input Format (JSON)

Place your input JSON at `data/<dataset_name>/<task_name>/<split_name>.json`.

### Schema

```json
[
  {
    "filename": "my-method-name",
    "caption": "Figure 1: Overview of the method...",
    "content": "The full methodology text describing the technique...",
    "visual_intent": "Diagram showing how X works by Y to achieve Z",
    "max_critic_rounds": 3
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| `filename` | string | Unique identifier for this item |
| `caption` | string | Figure caption (used for display/evaluation) |
| `content` | string | Methodology section text (the raw material for the diagram) |
| `visual_intent` | string | Communicative intent — what the diagram should convey |
| `max_critic_rounds` | int | Max Visualizer ↔ Critic iterations (default: 3) |

### Example

```json
[
  {
    "filename": "rocchio",
    "caption": "Figure 1: Rocchio Relevance Feedback",
    "content": "Rocchio relevance feedback modifies a query embedding by moving it toward the centroid of positive examples and away from the centroid of negative examples. The modified query is computed as: q_modified = alpha * q_original + beta * mean(positives) - gamma * mean(negatives), where alpha, beta, gamma control the balance...",
    "visual_intent": "Illustrate how Rocchio relevance feedback modifies a query vector in embedding space by combining weighted centroids of positive and negative examples to produce a refined search query",
    "max_critic_rounds": 3
  }
]
```

### Tips for Writing Good Inputs

- **content**: 300+ words of structured methodology text. More detail = better output.
  Strip code blocks (they confuse the Planner).
- **visual_intent**: Communicative intent, not just a title. Use the formula:
  `"[Verb] [what] by [how] to [goal]"`
  - Good: "Illustrate how RRF combines ranked results from two models into a unified ranking"
  - Bad: "RRF diagram"

---

## 6. Running (CLI)

### Basic Usage

```bash
cd /home/ezalos/42/PaperBanana
source .venv/bin/activate

python main.py \
  --dataset_name "Demo" \
  --task_name "diagram" \
  --split_name "all_methods" \
  --exp_mode "demo_planner_critic" \
  --retrieval_setting "none" \
  --max_critic_rounds 3
```

### CLI Arguments

| Flag | Default | Description |
|------|---------|-------------|
| `--dataset_name` | `PaperBananaBench` | Name of dataset directory under `data/` |
| `--task_name` | `diagram` | `diagram` or `plot` |
| `--split_name` | `test` | JSON filename (without `.json`) |
| `--exp_mode` | `dev` | Experiment mode (see §4) |
| `--retrieval_setting` | `auto` | `auto`, `manual`, `random`, `none` |
| `--max_critic_rounds` | `3` | Max Critic iterations (can be overridden per-item in JSON) |
| `--model_name` | (from yaml) | Override VLM model |

### File Paths

The CLI resolves paths as:
- **Input**: `data/{dataset_name}/{task_name}/{split_name}.json`
- **Output**: `results/{dataset_name}_{task_name}/{timestamp}_{retrieval}ret_{mode}_{split}.json`

### Without PaperBananaBench Dataset

If you don't have the benchmark dataset, use `--retrieval_setting none`. This skips
the Retriever agent entirely. The Planner works without reference examples — quality
is slightly lower but still good.

---

## 7. Running (Streamlit Demo)

```bash
cd /home/ezalos/42/PaperBanana
source .venv/bin/activate
streamlit run demo.py
```

The web UI has two tabs:
1. **Generate Candidates** — paste method text + caption, generate up to 20 parallel candidates
2. **Refine Image** — upload a generated image, describe edits, output at 2K/4K resolution

---

## 8. Extracting Images from Results

Results are saved as JSON with base64-encoded images embedded in the data fields.
To extract them as PNG files:

```python
#!/usr/bin/env python3
"""Extract final diagram images from PaperBanana result JSON."""
import json
import base64
import sys
from pathlib import Path
from PIL import Image
from io import BytesIO

def extract_images(json_path, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(json_path, "r", encoding="utf-8") as f:
        results = json.load(f)

    for item in results:
        filename = item.get("filename", "unknown")

        # Find the best image: last critic round, then planner fallback
        image_b64 = None
        for round_idx in range(3, -1, -1):
            key = f"target_diagram_critic_desc{round_idx}_base64_jpg"
            if key in item and item[key] and len(item[key]) > 100:
                image_b64 = item[key]
                break

        if not image_b64:
            # Fallback to planner output
            key = "target_diagram_desc0_base64_jpg"
            image_b64 = item.get(key)

        if not image_b64 or len(image_b64) < 100:
            print(f"  Skipping {filename}: no valid image")
            continue

        # Decode and save
        img_data = base64.b64decode(image_b64)
        img = Image.open(BytesIO(img_data))
        out_path = output_dir / f"{filename}.png"
        img.save(out_path)
        print(f"  Saved {out_path} ({img.size[0]}x{img.size[1]})")

if __name__ == "__main__":
    extract_images(sys.argv[1], sys.argv[2])
```

Usage:
```bash
python extract_images.py results/Demo_diagram/0228_1139_noneret_demo_planner_critic_all_methods.json ./my_outputs/
```

---

## 9. Concurrency & Rate Limits

- Default concurrency: 10 parallel items (`max_concurrent=10` in `main.py`)
- Each item triggers multiple Gemini API calls (Planner + Stylist + N×Visualizer + N×Critic)
- **Gemini rate limits** (429 errors) are handled with automatic retry (5 attempts, 30s delay)
- For large batches (>10 items), reduce concurrency to avoid quota exhaustion:
  - Edit `concurrent_num = 10` in `main.py` line 119, or
  - Process in smaller splits

---

## 10. Output Structure

### Result JSON Keys (per item)

| Key Pattern | Description |
|-------------|-------------|
| `target_diagram_desc0` | Planner's text description |
| `target_diagram_desc0_base64_jpg` | Planner's rendered image (base64 JPEG) |
| `target_diagram_stylist_desc0` | Stylist's refined description |
| `target_diagram_stylist_desc0_base64_jpg` | Stylist's rendered image |
| `target_diagram_critic_suggestions{N}` | Critic's feedback for round N |
| `target_diagram_critic_desc{N}` | Revised description after round N |
| `target_diagram_critic_desc{N}_base64_jpg` | Re-rendered image after round N |
| `eval_image_field` | Key of the final best image |

The final image is the last successful `critic_desc{N}_base64_jpg`, falling back to
`desc0_base64_jpg` if no critic round succeeded.

---

## 11. Gotchas & Fixes

### Fix: planner_agent.py crashes without PaperBananaBench

**Problem**: When using `--retrieval_setting none`, the Planner agent tries to open
`data/PaperBananaBench/diagram/ref.json` even when no reference IDs were retrieved.

**Fix** (already applied to our local copy): Add `if retrieved_ids:` guard at
`agents/planner_agent.py` line 69:

```python
# Before (crashes):
examples = data.get("retrieved_examples", [])
if not examples:
    retrieved_ids = data.get("top10_references", [])
    with open(...ref.json...) as f:
        ...

# After (safe):
examples = data.get("retrieved_examples", [])
if not examples:
    retrieved_ids = data.get("top10_references", [])
    if retrieved_ids:
        with open(...ref.json...) as f:
            ...
```

### Fix: Image model 404

**Problem**: The default image model name `gemini-2.0-flash-preview-image-generation`
returns 404 NOT_FOUND.

**Fix**: Use `gemini-3-pro-image-preview` in `configs/model_config.yaml`.

### Critic parse failures

The Critic sometimes returns malformed JSON (e.g., unescaped `\` in descriptions).
The code catches this with `json_repair` and treats it as "No changes needed", which
means the iteration stops early. This is harmless — the previous iteration's image
is used as the final output.

### Timezone override

`utils/config.py` line 44 sets `TZ=America/Los_Angeles`. This affects the timestamp
in result filenames. Harmless but worth knowing.

---

## 12. Comparison: Official vs OSS

| Feature | Official (dwzhu-pku) | OSS (llmsresearch) |
|---------|---------------------|--------------------|
| Install | Clone + venv + requirements.txt | `uv tool install paperbanana` |
| Interface | `python main.py` + JSON | `paperbanana generate -i <file> -c "<caption>"` |
| Input format | JSON array with full schema | Plain text file + CLI caption |
| Batch processing | Native (parallel, async) | Sequential (one at a time) |
| Output format | JSON with embedded base64 | PNG files in run directories |
| Output resolution | ~1K (lower, ~200-360 KB) | Higher (~2-3 MB) |
| Agents | Retriever, Planner, Stylist, Visualizer, Critic, Polish | Planner, Stylist, Visualizer, Critic |
| Reference examples | Yes (PaperBananaBench dataset) | No (built-in reference set) |
| Streamlit demo | Yes (`demo.py`) | No |
| Image refinement | Yes (Tab 2 in demo, 2K/4K upscale) | No |
| Speed (10 methods) | ~3.5 min (parallel) | ~45 min (sequential) |

---

## 13. Quick Reference

### Generate diagrams for custom methods (no dataset needed)

```bash
cd /home/ezalos/42/PaperBanana && source .venv/bin/activate

# 1. Create input JSON
cat > data/Demo/diagram/my_input.json << 'EOF'
[
  {
    "filename": "my-method",
    "caption": "Figure 1: My Method",
    "content": "Description of the method (300+ words)...",
    "visual_intent": "Show how X works by Y to achieve Z",
    "max_critic_rounds": 3
  }
]
EOF

# 2. Run generation
python main.py \
  --dataset_name Demo \
  --task_name diagram \
  --split_name my_input \
  --exp_mode demo_planner_critic \
  --retrieval_setting none

# 3. Extract images
python -c "
import json, base64
from PIL import Image
from io import BytesIO
from pathlib import Path

results = json.load(open(list(Path('results/Demo_diagram').glob('*my_input.json'))[-1]))
for item in results:
    for r in range(3, -1, -1):
        key = f'target_diagram_critic_desc{r}_base64_jpg'
        if key in item and item[key] and len(item[key]) > 100:
            img = Image.open(BytesIO(base64.b64decode(item[key])))
            img.save(f'{item[\"filename\"]}.png')
            print(f'Saved {item[\"filename\"]}.png ({img.size[0]}x{img.size[1]})')
            break
"
```
