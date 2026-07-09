# RLAIF on a tiny VLM — 2-day hackathon design doc

## 0. Goal & guiding philosophy

Train a tiny VLM with **RLAIF** (AI-generated preferences → DPO) on a single **RTX 3090 (24 GB)**, and — the actual point of this project — do it with **first-class observability of the learning signal**, so that at any moment you can see (a) whether the reward is moving and (b) what the model actually outputs.

Design rules, in priority order:

1. **Simplest loop first.** The Phase-1 run should be almost embarrassingly minimal (tiny model, ~2k pairs, LoRA, offline DPO). It exists to prove the harness, not to win benchmarks.
2. **Add exactly one axis of complexity at a time** — model size → data → method/feedback source. Never two at once, or you can't attribute what changed.
3. **Config-driven.** Everything (model, data slice, LoRA, DPO hyperparams, logging) lives in one YAML. Scaling from 500M to 3B is a one-line edit, not a code change.
4. **Observability is wired from Phase 0**, not bolted on later.

### Why DPO and not GRPO for the baseline

| | DPO (baseline) | GRPO (later) |
|---|---|---|
| Data | static preference set (RLAIF-V) | prompts only; rollouts generated online |
| Generation in loop | no | yes (needs vLLM to be fast) |
| Reward | *implicit*, model-derived (β·log π/π_ref) | *explicit* reward fn per rollout |
| Moving parts | few | many (reward fn, vLLM server, KL control) |
| Stability on 24 GB | high | fiddly |

DPO on the RLAIF-V dataset **is** RLAIF — the preferences were produced by an AI labeler. It's the truest simple starting point. GRPO/MPO are Phase-4 upgrades.

---

## 1. Phased plan

Each phase changes **one** thing and has a hard definition of done (DoD). Branch each phase into its own W&B run so comparisons stay clean, and **keep the probe set frozen across every run** so sample-level comparisons are apples-to-apples.

### Phase 0 — Environment + smoke test  (~30 min)
- Set up env, confirm the 3090 is visible, run **one training step on 8 samples** end-to-end with logging on.
- **DoD:** `make smoke` finishes with no OOM and W&B (or tensorboard) shows the first points.

### Phase 1 — DPO baseline + full observability  (~2–3 h)  ← the real milestone
- Model: `HuggingFaceTB/SmolVLM-500M-Instruct`. LoRA. ~2k RLAIF-V pairs. 1 epoch.
- Wire the **entire** observability harness (§2): reward-margin/accuracy curves, the frozen probe-set generation Table, the step-0 data-sanity Table, and a start/end hallucination proxy.
- **DoD:** reward margin trends up; chosen>rejected accuracy rises above 0.5; probe generations are logged and *visibly change* across steps; a before/after hallucination-proxy number exists. Results can be mediocre — the harness is what's being validated.

### Phase 2 — Scale the model  (~2–4 h)
- Change **one config line**: `model.id → Qwen/Qwen2.5-VL-3B-Instruct`. Enable QLoRA (§4) only if it OOMs. Everything else identical.
- **DoD:** a *meaningful* hallucination delta on an Object-HalBench / AMBER subset, on the same dashboards.

### Phase 3 — Scale the data  (~1–2 h)
- Raise `data.train_size` (2k → 10k → full). Nothing else changes.
- **DoD:** a run-over-run curve comparison answering "does more preference data improve the delta, and where does it plateau."

### Phase 4 — Stretch, pick ONE
- **(a) DPO → MPO.** Add the NLL/BCO terms (roughly a loss-config switch in TRL's DPOTrainer). Directly targets DPO's fluency-degradation failure mode; reported to help multimodal reasoning meaningfully.
- **(b) True closed-loop RLAIF.** Use a stronger VLM — or the model itself, à la RLAIF-V self-feedback — to score sampled pairs of the base model's own outputs, build a *fresh* preference set, and retrain. This is the most impressive demo and the most honest "we did RLAIF" story.
- **DoD:** one clean run of the chosen variant on the same dashboards.

---

## 2. Observability spec  (the priority)

### 2.1 Scalar curves (per step) — and what each one means

DPO has **no external scalar reward**. The "reward over time" you want is the *implicit* reward gap. TRL logs these automatically; here's how to read them:

- **`rewards/margins`** — mean(implicit_reward_chosen − implicit_reward_rejected). **Primary "is it learning" signal. Should trend up.**
- **`rewards/accuracies`** — fraction of the batch where chosen reward > rejected. Rises toward 1.0. A plateau near 0.5 or a drop = it isn't learning / data is noisy.
- **`rewards/chosen` and `rewards/rejected` (separately)** — you want *rejected* to go **down** while chosen stays flat/slightly up. If **both crater**, β is too high or lr too high (over-optimization).
- **`logps/chosen`, `logps/rejected`** — absolute logprob drift. If chosen logprob collapses, you're degrading fluency (classic DPO failure) even if margin looks fine. Watch this alongside the probe generations.
- **`loss`, `grad_norm`, `learning_rate`, `epoch`** — `grad_norm` spikes precede instability; catch them early.

**Map to GRPO (Phase 4b) so the mental model carries over:**

| DPO signal | GRPO equivalent |
|---|---|
| `rewards/margins` | mean reward per step |
| `rewards/accuracies` | reward > baseline fraction |
| implicit reward | actual reward-fn output (log **per component** if multi-part) |
| `logps` drift | KL(π‖π_ref) + completion length |

When you reach GRPO, add: per-reward-component curves, a reward **histogram** per step (not just mean), completion-length, and KL-to-reference.

### 2.2 Sample-level inspection (what makes it *actually* inspectable)

- **Frozen probe set** — 16–32 held-out `(image, prompt)` pairs in `data/probe_set.jsonl`, fixed for the whole project. A callback generates on them every `eval_steps` and logs a **W&B Table** (`step, image, prompt, generation`, optionally a reference-model generation column). Scrubbing the step slider to watch outputs evolve is the single most valuable artifact here.
- **Step-0 data-sanity Table** — log ~8 training pairs (`image, prompt, chosen, rejected`) *before* training. Catches schema/chat-template bugs in seconds instead of after a wasted run.
- **Reward-margin histogram** (optional) — `wandb.Histogram` each eval, to see distribution shift, not just the mean.

### 2.3 Lightweight external eval
- A cheap hallucination proxy (CHAIR-style object precision, or a small Object-HalBench / MMHal-Bench subset) run on the probe set **at step 0 and at end** (mid-run if cheap). Log as a scalar so you have a real before/after number, independent of training-internal metrics. Keep the subset small so it doesn't dominate runtime.

### 2.4 Tooling
- **W&B** (`report_to=["wandb"]`) — live curves + Tables + Histograms. Default choice.
- **Trackio** (`["trackio"]`) — HF's local, wandb-compatible tracker if you want no cloud account.
- **TensorBoard** (`["tensorboard"]`) — zero-dependency local fallback.
- TRL's `LogCompletionsCallback` covers probe generations; a small custom `TrainerCallback` handles the eval proxy + histograms.

---

## 3. Repo layout

```
rlaif-vlm/
  README.md
  DESIGN.md                 # this file
  requirements.txt
  Makefile                  # make smoke / baseline / scale
  configs/
    baseline_smolvlm.yaml
    qwen3b.yaml
  data/
    probe_set.jsonl         # 16-32 FROZEN inspection prompts
    build_dataset.py        # RLAIF-V -> TRL VLM-DPO schema adapter
  src/
    train_dpo.py            # config-driven DPO entrypoint
    callbacks.py            # ProbeGenerationCallback, HalProxyCallback
    eval_hal.py             # cheap CHAIR / Object-HalBench proxy
```

---

## 4. RTX 3090 (24 GB) memory & perf config

Concrete, single-GPU, no DeepSpeed/FSDP needed.

- `torch_dtype = bfloat16` (Ampere supports bf16).
- `attn_implementation = "flash_attention_2"` — Ampere is supported. **Fallback to `"sdpa"`** if the flash-attn wheel won't build on your CUDA 13 / driver 580 stack; do not burn an hour on this.
- **LoRA**: `r=16, alpha=32, dropout=0.05`, target `["q_proj","k_proj","v_proj","o_proj"]` (add gate/up/down proj later if memory allows). **Freeze the vision encoder** to start — cheapest and simplest; only the LLM/projector adapters train.
- **Reference model for free**: pass the PEFT model with `ref_model=None`. TRL computes reference logprobs by *disabling the adapter*, so no second model sits in VRAM. (Alternative: `precompute_ref_log_probs=True` to free it after a precompute pass.)
- `gradient_checkpointing=True` with `use_reentrant=False`.
- `per_device_train_batch_size=1` (DPO is effectively 2× since it processes chosen+rejected), `gradient_accumulation_steps=8–16`.
- Cap sequence length: `max_prompt_length≈512`, `max_length≈1024`.
- **Cap image tokens**: for Qwen2.5-VL set the processor `max_pixels` (e.g. `512*28*28`) to bound vision tokens — the biggest hidden memory driver. SmolVLM already runs low-res.
- `optim="adamw_bnb_8bit"` (8-bit optimizer) to shrink optimizer state.
- **QLoRA fallback** (`load_in_4bit` via bitsandbytes) *only if* the 3B model OOMs after the above. 4-bit + DPO + PEFT works fine.
- **No vLLM for DPO** (it's offline). vLLM is only needed for the GRPO phase.

---

## 5. Starter config (`configs/baseline_smolvlm.yaml`)

```yaml
run_name: rlaif-baseline-smolvlm500m
seed: 0

model:
  id: HuggingFaceTB/SmolVLM-500M-Instruct   # scale-up: Qwen/Qwen2.5-VL-3B-Instruct
  torch_dtype: bfloat16
  attn_implementation: flash_attention_2     # fallback: sdpa
  freeze_vision_encoder: true

data:
  dataset_id: openbmb/RLAIF-V-Dataset        # confirm exact id on the Hub
  train_size: 2000                           # start tiny; raise in Phase 3
  max_prompt_length: 512
  max_length: 1024
  max_pixels: 401408                         # 512*28*28; caps Qwen vision tokens, ignored by SmolVLM

lora:
  r: 16
  alpha: 32
  dropout: 0.05
  target_modules: [q_proj, k_proj, v_proj, o_proj]

dpo:
  beta: 0.1
  learning_rate: 5.0e-6
  per_device_train_batch_size: 1
  gradient_accumulation_steps: 8
  num_train_epochs: 1
  gradient_checkpointing: true
  optim: adamw_bnb_8bit
  bf16: true

logging:
  report_to: [wandb]                          # or [trackio] / [tensorboard]
  logging_steps: 5
  eval_steps: 50
  save_steps: 200
  probe_set_path: data/probe_set.jsonl
  probe_generate_every: 50
```

---

## 6. Skeletons (starting points for Claude Code, not final code)

### `src/train_dpo.py`
```python
import yaml, torch
from datasets import load_dataset
from transformers import AutoModelForImageTextToText, AutoProcessor
from peft import LoraConfig
from trl import DPOConfig, DPOTrainer
from callbacks import ProbeGenerationCallback, HalProxyCallback

cfg = yaml.safe_load(open("configs/baseline_smolvlm.yaml"))

processor = AutoProcessor.from_pretrained(cfg["model"]["id"])
# For Qwen2.5-VL, set processor.image_processor.max_pixels = cfg["data"]["max_pixels"]

model = AutoModelForImageTextToText.from_pretrained(
    cfg["model"]["id"],
    torch_dtype=getattr(torch, cfg["model"]["torch_dtype"]),
    attn_implementation=cfg["model"]["attn_implementation"],
)
if cfg["model"]["freeze_vision_encoder"]:
    ...  # freeze vision tower params

# RLAIF-V -> TRL VLM-DPO schema. Expected columns per row:
#   {"images": [PIL.Image], "prompt": <conversational>, "chosen": <text/turn>, "rejected": <text/turn>}
train_ds = load_dataset(cfg["data"]["dataset_id"], split="train") \
    .select(range(cfg["data"]["train_size"])) \
    .map(to_trl_vlm_dpo_schema)   # implement in data/build_dataset.py; VERIFY one formatted example

peft_cfg = LoraConfig(
    r=cfg["lora"]["r"], lora_alpha=cfg["lora"]["alpha"],
    lora_dropout=cfg["lora"]["dropout"], target_modules=cfg["lora"]["target_modules"],
    task_type="CAUSAL_LM",
)

args = DPOConfig(
    output_dir=f"runs/{cfg['run_name']}",
    beta=cfg["dpo"]["beta"],
    learning_rate=cfg["dpo"]["learning_rate"],
    per_device_train_batch_size=cfg["dpo"]["per_device_train_batch_size"],
    gradient_accumulation_steps=cfg["dpo"]["gradient_accumulation_steps"],
    num_train_epochs=cfg["dpo"]["num_train_epochs"],
    gradient_checkpointing=cfg["dpo"]["gradient_checkpointing"],
    optim=cfg["dpo"]["optim"], bf16=cfg["dpo"]["bf16"],
    max_prompt_length=cfg["data"]["max_prompt_length"],
    max_length=cfg["data"]["max_length"],
    logging_steps=cfg["logging"]["logging_steps"],
    eval_steps=cfg["logging"]["eval_steps"],
    save_steps=cfg["logging"]["save_steps"],
    report_to=cfg["logging"]["report_to"],
)

trainer = DPOTrainer(
    model=model,
    ref_model=None,          # LoRA -> adapter-disable reference, no 2nd model in VRAM
    args=args,
    train_dataset=train_ds,
    processing_class=processor,
    peft_config=peft_cfg,
    callbacks=[
        ProbeGenerationCallback(cfg["logging"]["probe_set_path"],
                                every=cfg["logging"]["probe_generate_every"]),
        HalProxyCallback(cfg["logging"]["probe_set_path"]),   # runs at start + end
    ],
)
trainer.train()
```

### `src/callbacks.py` (interface sketch)
```python
from transformers import TrainerCallback
import wandb

class ProbeGenerationCallback(TrainerCallback):
    """Generate on a FROZEN probe set every `every` steps; log a wandb Table
    (step, image, prompt, generation) so outputs can be watched evolving."""
    def __init__(self, probe_path, every=50): ...
    def on_step_end(self, args, state, control, model=None, **kw):
        if state.global_step % self.every: return
        # generate on probe set -> wandb.log({"probe": wandb.Table(...)}, step=state.global_step)

class HalProxyCallback(TrainerCallback):
    """Cheap CHAIR / Object-HalBench-subset hallucination proxy on the probe set,
    logged as a scalar at train start and train end."""
    def on_train_begin(self, *a, **k): ...   # log baseline
    def on_train_end(self, *a, **k): ...     # log final -> before/after delta
```

---

## 7. Risks & gotchas (ranked by expected time cost)

1. **Chat-template / processor mismatch** — the #1 VLM-DPO time sink. Verify the processor applies the correct template and image tokens; **log one fully-formatted example before training** (the step-0 data-sanity Table catches this).
2. **RLAIF-V → TRL schema conversion** — write `build_dataset.py` first and unit-check a single row (images list + conversational chosen/rejected) before launching anything.
3. **Tiny-model weak signal** — 500M validates plumbing, not hallucination gains. Don't over-interpret Phase-1 quality; the real delta is a Phase-2 (3B) outcome.
4. **DPO over-optimization** — chosen *and* rejected logprobs both collapsing, degenerate/short probe outputs → lower `beta`, lower `lr`, or move to MPO (add an SFT/NLL term).
5. **flash-attn build on CUDA 13 / driver 580** — may need a matching wheel; fall back to `sdpa` rather than debugging the build.
6. **Single GPU** — resist adding DeepSpeed/FSDP; keep it single-process and simple.

---

## 8. First commands

```bash
# Phase 0
make smoke        # 1 step, 8 samples, logging on -> confirm no OOM + curves appear
# Phase 1
make baseline     # SmolVLM-500M + 2k pairs + full observability harness
# Phase 2
make scale        # edit configs/qwen3b.yaml (model.id) -> rerun
```
