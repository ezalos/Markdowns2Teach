---
marp: true
theme: station-f
paginate: true
header: "SDXL Optimization · Pruna AI Technical Test"
footer: "Louis Develle · 28 May 2026 · github.com/entropic-gradient/sdxl-inference-optimization"
---

<!-- ABOUTME: Slide deck for Pruna AI technical interview presentation. -->
<!-- ABOUTME: 17 numbered slides — framing, methodology, Tier A/B/C with per-tier Pareto graphs, Pruna recipe comparison, failure modes, full-Pareto synthesis, deployment. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Optimizing SDXL Inference

## Pareto frontiers across caching, compilation, and distillation

Louis Develle · 28 May 2026
Pruna AI · Technical Test

---

# 01 — The brief, in one slide

> **"Make SDXL as efficient as possible. Compress, evaluate, deploy via LitServe. ~3 hours total."**

**Primary objective: latency** — quality-conscious in every trade-off. vRAM & cost measured, but secondary.

**What I optimized for:**
- Multiple Pareto points, not one number
- Paired quality eval at fixed prompt+seed (DreamSim · LPIPS-VGG · PSNR · CLIPScore)
- Real measurements on local hardware (RTX 4090, sm_89 = Ada Lovelace)
- Mechanism-first reporting — including negative results

> Full transparency: I exceeded the 3-hour budget. Next slide explains how I made the extra time productive.

<small>Hardware: RTX 4090 24GB shared with desktop (~8GB pre-occupied) · Container: NGC pytorch:24.10-py3</small>

---

# 02 — Methodology: parallel research × agent loop

<!-- _class: cols -->

<div class="left">

**Each iteration:**

1. I deep-research what to try
2. I hand the agent a playbook + thresholds
3. Agent builds and measures
4. I read results, queue next research

**During each agent run:**
- I research iteration N+1 in parallel
- No blocking time wasted

</div>
<div class="right">

**Three rounds shipped:**

- **Iter 1**: baseline + eval-by-eye mosaic + serving
- **Iter 2**: paired-quality eval + 12 optim configs
- **Iter 3+**: compile recovery + DMD2 + quant sweep + anti-patterns

> Agent does the measurable; I do the unmeasurable.

</div>

---

<!-- _class: section -->

# Framing

---

# 03 — The four orthogonal axes

| Axis | What it changes | Examples |
|------|-----------------|----------|
| **Numerics** | bit-width of weights / activations | fp16, int8, int4, fp8 |
| **Per-step compute** | cost of one UNet forward | `torch.compile`, fused QKV, caching |
| **Schedule** | how many UNet forwards | 30 → 4 → 1 step (distillation) |
| **Pipeline** | aux models & overhead | VAE, text encoders, embedding cache |

> Distillation is the **only axis that reduces *N*** in `O(N × per-step-cost)`.

---

# 04 — Three tiers: what counts as "compressing SDXL"?

| Tier | What's modified | Reading of the brief |
|------|-----------------|---------------------|
| **A** | Original SDXL UNet kept | Strict: "compress *these* weights" |
| **B** | Same UNet + tiny VAE decoder (TAESDXL) | Standard SDXL ecosystem practice |
| **C** | UNet replaced by published distillation | Aggressive — different attractor |

**Today's focus:** Tier A & B in depth (the original engineering work), with one Tier C slide so we have the full picture.

---

# 05 — Evaluation methodology

<!-- _class: cols compact -->

<div class="left">

**Performance (per config):**

- **Latency p50** — median of 30 runs (p95/p99 tracked)
- Peak vRAM (own-process) · $/img (g5.xlarge proxy)

**Quality — paired (fixed prompt + seed):**

- **DreamSim** — perceptual identity; ~96% human-2AFC agreement
- **LPIPS-VGG** — perceptual, texture-sensitive
- **PSNR** — pixel-space sanity check
- **CLIPScore** + per-image win-rate — text alignment

</div>
<div class="right">

**Why these:**

- Paired (fixed prompt+seed) isolates compression drift from seed noise
- DreamSim = strongest off-the-shelf "looks-like-baseline" signal
- Win-rate (per-image binary) resists reward-hacking, unlike means

**Skipped — with reason:**

- **FID** ≥ 10k samples · **CMMD** ≥ 256 prompts
- **HPSv2 / ImageReward** dep-pin conflicts · **GenEval** Mask2Former infra

</div>

<small>8 prompts × 3 seeds = 24 pairs/config · DreamSim < 0.05 ≈ imperceptible · LPIPS < 0.10 ≈ identical, > 0.30 visible · WR 0.50 = parity</small>

---

# 06 — Techniques covered today

<!-- _class: cols -->

<div class="left">

**Tier A & B (deep dive):**

- DeepCache — feature reuse across steps
- `torch.compile` + Inductor
- Fused QKV + channels_last
- TAESDXL — tiny VAE decoder
- Weight quantization study

</div>
<div class="right">

**Tier C (one slide for context):**

- DMD2 1-step + full pipeline compile

**Failure modes (one section):**

- `compile + DeepCache` thrashing
- `compile + monkey-patch` cliffs
- TensorRT silent fallback

</div>

---

<!-- _class: section -->

# Tier A — Original UNet, no swap

![bg right:46% contain](assets/pareto_tier_a.png)

---

# 07 — DeepCache: temporal redundancy in the U-Net

<!-- _class: cols -->

<div class="left">

**Mechanism:**

- Deep U-Net features change slowly across adjacent denoising steps
- Cache them at step `t`, reuse for `t+1 … t+(interval-1)`
- Only recompute shallow down + up blocks

**Math @ interval=3, 30 steps:** 10 full + 20 shallow ≈ **~16 UNet-equivalents**

</div>
<div class="right">

**My measurements (vs baseline):**

| Config | Latency | DreamSim | LPIPS-V |
|---|---|---|---|
| baseline fp16 | 3750 ms | 0.000 | 0.000 |
| DeepCache(2) | 2051 ms | **0.043** | 0.207 |
| DeepCache(3) | 1475 ms | 0.100 | 0.330 |

> Interval=2 halves the perceptual drift (DreamSim 0.043 vs 0.100) — worth the ~580 ms (1.83× vs 2.54×).

</div>

<small>Source : [Ma et al., NUS, NeurIPS 2024](https://arxiv.org/abs/2312.00858)</small>

---

# 08 — Tier A Pareto: caching + fusion

<!-- _class: compact compact-table -->

**Target = speed, quality-conscious. vRAM secondary (shown for completeness).**

| Config | Latency | Speedup | vRAM | DreamSim | LPIPS-V | WR |
|--------|---------|---------|------|---------|---------|-----|
| baseline fp16 | 3750 ms | 1.00× | 9168 MB | 0.000 | 0.000 | — |
| `compile` (lossless) | 3583 ms | 1.05× | 9168 MB | **0.001** | 0.015 | 0.50 |
| `deepcache2` | 2051 ms | 1.83× | 9498 MB | 0.043 | 0.207 | 0.67 |
| **`deepcache_qkv`** | **1645 ms** | **2.28×** | 10129 MB | 0.100 | 0.330 | **0.71** |
| `q_hqq_int4_dc2` | 3121 ms | 1.20× | 7950 MB | 0.092 | 0.325 | **0.75** |

> `compile` alone gives 1.05× — the rest comes from caching. **SDXL UNet fp16 is already tensor-core-saturated on Ada** (Ada = RTX 40-series arch; GEMM = matrix-multiply, the UNet's main op); compile's win is CUDA-Graph launch-overhead removal, not GEMM acceleration. **`deepcache_qkv` is the Tier A speed winner** — note QKV fusion *costs* vRAM (bigger fused activations); `q_hqq_int4_dc2` is the pick for 12 GB cards.

<small>DreamSim/LPIPS-VGG vs baseline, same prompt+seed · DreamSim < 0.05 ≈ imperceptible · WR 0.50 = parity</small>

---

# 09 — Weight quantization on a 4090: a systemic finding

<!-- _class: compact compact-table -->

**Tested standalone on the original UNet:**

| Quantizer | Latency | vRAM | DreamSim | Verdict |
|-----------|---------|------|---------|---------|
| baseline fp16 | 3750 ms | 9168 MB | 0.000 | reference |
| `bnb_int8` (threshold=0) | 7117 ms | 8618 MB | 0.056 | 1.9× **regression** |
| `bnb_nf4` | 8638 ms | 7516 MB | 0.102 | 2.3× regression |
| `hqq_int4` (Marlin verified firing) | 5604 ms | 7608 MB | 0.092 | 1.5× regression |
| `torchao_int8_dynamic` + compile | 3846 ms | 8575 MB | 0.071 | baseline-equal, saves vRAM |

> **Why:** SDXL UNet at batch=1 fp16 on Ada is **compute-bound on tensor cores**, not bandwidth-bound. Quant trades a saturated fp16 path for an equal-or-slower INT path + per-call dequant overhead.

> **Where it wins:** H100/H200 (better INT8 cores), bandwidth-bound DiTs (FLUX, video), batch > 1, **12GB consumer cards** where memory is the binding constraint.

<small>Glossary — bnb = bitsandbytes · int8 = 8-bit + fp16 outliers · nf4 = 4-bit NormalFloat (QLoRA) · hqq = Half-Quadratic Quant (calibration-free, Marlin = fast int4 kernel) · torchao = PyTorch-native quant</small>

---

# 10 — Pruna's own recipe, on my harness

<!-- _class: cols compact -->

<div class="left">

**Their published SmashConfig, run end-to-end:**

```python
sc = SmashConfig()
sc["cacher"] = "deepcache"; sc["deepcache_interval"] = 2
sc["compiler"] = "torch_compile"
sc["quantizer"] = "hqq_diffusers"  # W4, g64, marlin
smash(pipe, sc)  # → my 24 prompt+seed harness
```

- Published **≈2400 ms / 1.56×** → I measure **2489 ms / 1.51×**. Reproduces cleanly.
- Their integration runs **compile + DeepCache together** — the exact combo that thrashed my naive stack (928 s/img). Real engineering.

</div>
<div class="right">

**Head-to-head (their recipe vs my Tier A winner):**

| Metric | `deepcache_qkv` | Pruna Smash |
|---|---|---|
| Latency | **1645 ms** | 2489 ms |
| Speedup | **2.28×** | 1.51× |
| vRAM | 10129 MB | **7948 MB** |
| DreamSim | 0.100 | **0.087** |
| WR | **0.71** | 0.58 |

> On a 4090 I'm faster; their HQQ-int4 recipe wins vRAM by ~2.2 GB — the better 12 GB-card pick.

</div>

<small>SmashConfig per [docs.pruna.ai](https://docs.pruna.ai) · pruna 0.3.3 · same 8 prompts × 3 seeds, same paired metrics</small>

---

<!-- _class: section -->

# Tier B — Tiny VAE swap

![bg right:46% contain](assets/pareto_tier_b.png)

---

# 11 — TAESDXL: a 7MB student of the SDXL VAE

<!-- _class: cols compact -->

<div class="left">

**What it is:**

- Distilled VAE decoder ([`madebyollin/taesdxl`](https://github.com/madebyollin/taesd))
- ~200M params → 7MB (~30× smaller)
- DreamSim vs full VAE ≈ **0.007** (imperceptible)

**When it matters:**

- 30-step baseline: VAE ≈ 3% of total
- 1-step distilled: VAE ≈ 36% of total

> Same UNet — only the decoder swaps.

</div>
<div class="right">

**VAE swap, full vs tiny:**

| Config | Latency | vRAM | WR |
|---|---|---|---|
| baseline (full VAE) | 3750 ms | 9168 MB | — |
| `taesd` (tiny VAE) | 3619 ms | 7218 MB | 0.50 |
| `deepcache` (full) | 1475 ms | 9492 MB | 0.67 |
| **`deepcache_taesd`** | **1352 ms** | 7543 MB | **0.75** |

> Tiny VAE saves ~1.95 GB everywhere; latency only when steps are few.

</div>

---

# 12 — Why `deepcache_taesd` wins Tier B

**All quality numbers are vs the standard fp16, 30-step SDXL baseline (same prompt + seed).**

**The interesting compositional effect:**

- DeepCache(3) alone: WR **0.67** — slight texture drift vs baseline
- DeepCache(3) + TAESDXL: WR **0.75** — texture drift smoothed

> TAESDXL's distilled-smooth decoding acts as an **unintentional regularizer** over the cache-induced artifacts.

**My honest "ship-this-to-production" pick if I cannot swap the UNet:**

- 2.77× speedup at DreamSim 0.103 / LPIPS-VGG 0.358 (subtle drift, invisible at thumbnail size)
- WR 0.75 — alignment *better* than the fp16 baseline on 3 of 4 prompts
- 1.6 GB vRAM freed vs full VAE

---

<!-- _class: section -->

# Tier C — Distilled UNet, briefly

![bg right:46% contain](assets/pareto_tier_c.png)

---

# 13 — DMD2 1-step + full pipeline compile

<!-- _class: cols compact -->

<div class="left">

**Stack:**

- DMD2 1-step UNet (full swap, not LoRA)
- `LCMScheduler`, **1 step at noise level t=399**, CFG=0 (guidance distilled in → no 2nd forward)
- TAESDXL + `torch.compile` (UNet + text encoders + VAE)

**DMD2 vs Lightning, 4-step (paper, COCO-10k FID ↓):**

| Model | FID |
|---|---|
| SDXL teacher (100 steps) | 19.36 |
| **DMD2 (4-step)** | **19.32** |
| Lightning (4-step) | 24.46 |

</div>
<div class="right">

**Resolution sweep — the real "size" lever** (params unchanged at 2.6B):

| Res | Fresh | + cached embeds |
|---|---|---|
| 1024² | **116 ms** (32×) | 99 ms (38×) |
| 768² | 82 ms (46×) | 66 ms (57×) |
| 512²* | 54 ms (69×) | 38 ms (99×) |

**Quality @ 1024² vs baseline:**
DreamSim **0.281** · LPIPS-V **0.591** · PSNR **13.4 dB** · CLIPScore WR **0.75** · vRAM **6962 MB**

> ⚠ **Licence:** DMD2 is cc-by-nc-4.0. Commercial path = Hyper-SDXL (Apache 2.0).

</div>

<small>* 512² off-distribution for SDXL · DreamSim 0.28 = different attractor (1-step distill), not a defect · [Yin et al., NeurIPS 2024](https://arxiv.org/abs/2405.14867)</small>

---

<!-- _class: section -->

# What didn't work (and why)

---

# 14 — Three "should have worked but didn't"

| Combo | Outcome | Root cause |
|-------|---------|------------|
| **`compile + DeepCache`** | 928 sec/img recompilation thrashing | DeepCache's `if t in cached_steps:` is a tensor-value branch → Dynamo specializes per timestep |
| **`compile + Sage`** (monkey-patch) | Quality cliff: LPIPS 0.949, WR 0.00 | Monkey-patched `F.scaled_dot_product_attention` invisible to Dynamo; CUDA Graph captures stale state |
| **TensorRT** via `torch_tensorrt` | +30-41% regression (151 ms) | Silent eager fallback on unsupported ops (fp32 upcast in cross-attn); cudaStreamSync overhead dominates |

> Documented rather than buried — each tells you something structural about how the toolchain interacts with diffusion UNets.

---

# 15 — Anti-pattern: `compile` + custom CUDA Linear

<!-- _class: compact -->

**Three independent reproductions of the same failure:**

- `compile + sage` (monkey-patch) → LPIPS-A 0.949
- `compile + bnb Linear4bit` → LPIPS-A 0.953
- `compile + bnb Linear8bitLt` (threshold=0) → LPIPS-A 0.718

**Unified mechanism** (`bnb` = bitsandbytes):

1. The quantizer keeps its weights/scales in Python objects **outside** the `nn.Module` parameter system
2. `mode="reduce-overhead"` records the GPU work **once** into a CUDA Graph, baking in the tensors' **memory addresses**
3. Between capture and replay, Python frees/relocates those buffers → the replay reads **stale addresses** → garbage → noise

> **Why `torchao` (PyTorch-native quant) does NOT show this:** its quantized matmul is a regular `torch.ops.aten` op and its state lives in `nn.Parameter`s — the graph-capture machinery keeps it alive.

> **Practical rule:** custom-CUDA-Linear quantizers are incompatible with `compile(mode="reduce-overhead")`. Use torch-op-based quantizers (torchao) or per-block AttnProcessor subclassing.

---

<!-- _class: section -->

# Synthesis

---

# 16 — The full Pareto, all tiers

<!-- _class: img-right -->

- Three tiers on one speed × quality plane (DreamSim vs latency, log x)
- **Tier A** clusters at 1.6–3.7 s, DreamSim < 0.10 — near-lossless, modest speed
- **Tier C** jumps to 120–550 ms but DreamSim ~0.20–0.28 — distillation is a *different attractor*, not a defect
- ★ = tier favorite · ◆ = baseline reference

> No single winner — the right point depends on the licence + hardware + quality bar.

![bg right:52% contain](assets/pareto_all.png)

<small>Latency p50 · DreamSim vs SDXL baseline · 8 prompts × 3 seeds / config · live: pruna.develle.fr/sweep</small>

---

# 17 — LitServe deployment + future work

<!-- _class: cols compact -->

<div class="left">

**Shipped:**

- `pruna.develle.fr/predict` — LitServe API
- `pruna.develle.fr/sweep` — mosaic Pareto explorer
- **Three presets, one endpoint**: `baseline` / `deepcache_qkv` / `dmd2_1step_taesd_compile_full` (shared text encoders, hot in 24 GB)
- Behind Cloudflare (HTTPS at CF, proxied to origin)

> One Pareto, pick-per-request. Reviewers want decisions, not menus.

</div>
<div class="right">

**Next iterations:**

- **HPSv2 + ImageReward** (vendored) — 3rd quality axis, catches reward-hacking
- **CMMD** on 256 prompts — distribution-level drift w/ CIs
- **Per-block precision sweep** — INT8 robust blocks, fp16 sensitive ones
- **Per-timestep ε-MSE** — *where* in the trajectory compression bleeds (novel)
- **Hyper-SDXL** — Apache-2.0 swap for non-commercial DMD2
- **Smaller backbone** (Segmind SSD-1B / Vega) — sub-100 ms at 1024² without a distillation licence

</div>
