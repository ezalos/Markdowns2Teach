<!-- ABOUTME: Research extract feeding Station F slides A-09 to A-12 on LLM deployment economics. -->
<!-- ABOUTME: Primary sources: Qwen3 blog/technical report, HF model card, Spheron/JarvisLabs practitioner guides. -->

# Qwen3 + quantization research — for Station F slides A-09 through A-12

Accessed: 2026-04-12. Primary sources verified against Qwen team's own publications where possible.

## A-09 — B-params → GB-VRAM math

**Formula** (Memory = Parameters × Bytes per Parameter):

- **FP32** (full precision): 4 bytes/param → 7B ≈ 28GB, 32B ≈ 128GB, 70B ≈ 280GB
- **FP16 / BF16** (half precision): 2 bytes/param → 7B ≈ 14GB, 32B ≈ 64GB, 70B ≈ 140GB
- **INT8** (8-bit quantization): 1 byte/param → 7B ≈ 7GB, 32B ≈ 32GB, 70B ≈ 70GB
- **INT4** (AWQ / GPTQ / GGUF Q4): 0.5 bytes/param → 7B ≈ 3.5GB, 32B ≈ 16GB, 70B ≈ 35GB

**Source for the formula** — Spheron (GPU Memory Requirements for LLMs):
> "The formula is straightforward: Memory = Parameters × Bytes per Parameter" — and they publish a table: "FP32 (full precision) | 4 bytes | 280 GB ; FP16 / BF16 (half precision) | 2 bytes | 140 GB ; INT8 (8-bit quantization) | 1 byte | 70 GB ; INT4 (4-bit quantization) | 0.5 bytes | 35 GB" (for a 70B model).
> URL: https://www.spheron.network/blog/gpu-memory-requirements-llm/

**Corroborating source (practitioner napkin math)** — Hivenet compute blog:
> "Baseline weight size for FP16 is ~2 bytes per parameter. 7B model, FP16: ~14 GB for weights ; 7B, int8: ~7–8 GB ; 7B, int4: ~3.5–4 GB"
> URL: https://compute.hivenet.com/post/llm-quantization-guide

**Qwen 3 32B specifics from the same Spheron table** (directly usable on slide):
> "Qwen 3 32B | 32B | ~76 GB [FP16] | ~40 GB [INT8] | ~22 GB [INT4]"
> URL: https://www.spheron.network/blog/gpu-memory-requirements-llm/
> Louis-note: Spheron adds real-world overhead (KV-cache + activations), which is why their 32B FP16 line reads ~76 GB whereas the pure weight-only math is 64 GB. Use Spheron's numbers if you want "to actually run it"; use the napkin math if you're teaching the formula.

**Source for the KV-cache / activations addendum** — Spheron again:
> "GPU memory consumption during LLM inference breaks down into four distinct components, each with different scaling behavior: 1. Model Weights ... Weight memory scales linearly with parameter count and the precision format used to store each parameter."
> The article then enumerates KV cache, activations, and framework overhead as the remaining three components. URL above.

**Alternative formula with a division** — LetsDataScience:
> "Memory (GB) = Parameters × Bits per weight / (8 × 1024³)"
> URL: https://letsdatascience.com/blog/llm-quantization-run-any-model-on-consumer-hardware

## A-10 — Quantization tradeoffs (perplexity vs size)

**Headline benchmark table — JarvisLabs benchmarks on Qwen2.5-32B-Instruct (H200)**:

| Quant | Perplexity (WikiText) | HumanEval Pass@1 | Throughput (tok/s) | Use case |
|-------|-----------------------|-------------------|--------------------|----------|
| FP16 baseline | 6.56 | 56.1% | 461 | Training, pristine serving |
| INT8 (BitsandBytes) | 6.67 | 51.8% | 168 | Production serving, halves VRAM |
| AWQ INT4 | 6.84 | 51.8% | 68 (741 with Marlin kernel) | Self-hosting on consumer GPUs |
| GPTQ INT4 | 6.90 | 46.3% | 277 | Alternative 4-bit |
| GGUF Q4_K_M | 6.74 | 51.8% | 93 | llama.cpp / CPU-fallback |

**Source for every perplexity / Pass@1 / throughput number** — JarvisLabs.ai blog (January 7, 2026):
> "Baseline (FP16) | 6.56 | 56.1% | 461 | 57.7 ... AWQ | 6.84 | 51.8% | 68 | 277.8 ... GPTQ | 6.90 | 46.3% | 277 | 107.1 ... Marlin-AWQ | 6.84 | 51.8% | 741 | 73.5 ... GGUF (Q4_K_M) | 6.74 | 51.8% | 93 | 958.0 ... BitsandBytes | 6.67 | 51.8% | 168 | 135.3"
> And the key takeaway: "Quantization works: All methods kept perplexity within ~6% of baseline. 4-bit quantization is practical for real-world use."
> URL: https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks

**Qwen3-specific quantization caveat** — arXiv empirical study of Qwen3 quantization (2505.02214):
> "Qwen3 maintains competitive performance at higher bit-widths (4-bit and above), it exhibits more pronounced performance degradation compared to previous model generations when quantized to 3-bit or below. ... a more thorough pre-training process likely results in fewer redundant representations in stronger LLMs, making them more sensitive to quantization-induced information loss."
> URL: https://arxiv.org/html/2505.02214v1
> Louis-note: Translate into business-speak — "cutting-edge models are less forgiving of aggressive quantization; stick to 4-bit minimum for Qwen3."

**GGUF perplexity ladder for reference (llama.cpp on Llama-3 8B)** — LessWrong:
> "f16 | 14.97 GB | PPL 6.2331 ; q8_0 | 7.96 GB | 6.2342 ; q6_K | 6.14 GB | 6.2533 ; q5_K_M | 5.33 GB | 6.2886 ; q4_K_M | 4.58 GB | 6.3830 ; q4_0 | 4.34 GB | 6.7001"
> URL: https://www.lesswrong.com/posts/qmPXQbyYA66DuJbht/comparing-quantized-performance-in-llama-models
> This shows q4_K_M gives a ~2.4% perplexity degradation on Llama-3, close to the Qwen2.5-32B number above.

**General "quality vs size" takeaway** — Spheron:
> "Modern 4-bit quantization methods like GPTQ, AWQ, and GGUF maintain excellent output quality, with perplexity increases of only 1-3% on most benchmarks. For production chatbots and Q&A systems, the quality difference is typically imperceptible to end users."
> URL: https://www.spheron.network/blog/gpu-memory-requirements-llm/

## A-11 — Qwen3-32B sweet spot

**Why 32B is the sweet spot for self-hosting**:

- **Fits a single 24GB consumer GPU with INT4 quantization** (~16-22GB after quant, depending on KV cache budget)
- **Licensing: Apache 2.0** — zero commercial friction
- **Dense architecture** (not MoE) — simpler to deploy than Qwen3-30B-A3B or Qwen3-235B-A22B
- **Near-72B-class performance in a 32B footprint** — Qwen's own team explicitly positions it this way

**Primary source — Qwen3 blog (April 29, 2025, 2,036 words, Qwen Team)**:
> "We are open-weighting two MoE models: Qwen3-235B-A22B, a large model with 235 billion total parameters and 22 billion activated parameters, and Qwen3-30B-A3B, a smaller MoE model with 30 billion total parameters and 3 billion activated parameters. Additionally, six dense models are also open-weighted, including Qwen3-32B, Qwen3-14B, Qwen3-8B, Qwen3-4B, Qwen3-1.7B, and Qwen3-0.6B, under Apache 2.0 license."
> URL: https://qwenlm.github.io/blog/qwen3/

**Primary source — Qwen3 Technical Report (arXiv:2505.09388)**:
> "Qwen3-32B-Base outperforms Qwen2.5-32B-Base and Gemma-3-27B Base on most benchmarks. Notably, Qwen3-32B-Base achieves 65.54 on MMLU-Pro and 39.78 on SuperGPQA, significantly outperforming its predecessor Qwen2.5-32B-Base."
> And: "Qwen3-32B-Base achieves competitive results compared to Qwen2.5-72B-Base. Although Qwen3-32B-Base has less than half the number of parameters of Qwen2.5-72B-Base, it outperforms Qwen2.5-72B-Base in 10 of the 15 evaluation benchmarks. On coding, mathematics, and reasoning benchmarks, Qwen3-32B-Base has remarkable advantages."
> URL: https://arxiv.org/html/2505.09388v1

**Primary source — Qwen3-32B HuggingFace model card** (accessed 2026-04-12):
> "Qwen3-32B has the following features: Type: Causal Language Models ; Training Stage: Pretraining & Post-training ; Number of Parameters: 32.8B ; Number of Paramaters (Non-Embedding): 31.2B ; Number of Layers: 64 ; Number of Attention Heads (GQA): 64 for Q and 8 for KV ; Context Length: 32,768 natively and 131,072 tokens with YaRN."
> And: "License: apache-2.0 ... Downloads last month: 2,573,728"
> URL: https://huggingface.co/Qwen/Qwen3-32B

**Secondary source — Qwen3 Instruct benchmark numbers (Design For Online compilation from Artificial Analysis + HF leaderboard)**:
> "SciCode 35.4% ... LiveCodeBench 54.6% ... τ²-Bench 29.8% ... IFBench 36.3%"
> Release date: April 28, 2025. Context length: 40,960 tokens. OpenRouter pricing: $0.08 input / $0.24 output per 1M tokens.
> URL: https://designforonline.com/ai-models/qwen-qwen3-32b/
> Louis-note: These are the Instruct (post-trained) scores, not the Base scores the arXiv report gives. For a business audience, quote MMLU-Pro 65.54 from the tech report since that's from Qwen's own paper.

**Cost vs. Qwen3-14B / Qwen3-72B (doesn't exist) / Qwen3-235B-A22B**:
- Qwen3-14B: smaller, cheaper to serve, MMLU-Pro drops materially
- Qwen3-235B-A22B: MoE; 22B activated params but 235B total → you still need ~470GB VRAM to host
- **There is no Qwen3-72B** in the v1 release — the family goes 32B dense → 235B-A22B MoE. That's why 32B is *the* self-hosting target.
- Confirmed via the Qwen3 blog table listing all 8 released models.

## A-12 — Reading HF model names

Example: `Qwen/Qwen3-32B-Instruct-AWQ-4bit`

- `Qwen` — organization handle on Hugging Face (the Alibaba team's HF org)
- `Qwen3` — model family / generation
- `32B` — parameter count in billions (Qwen3-32B is actually 32.8B, per HF model card)
- `Instruct` — fine-tuning variant
  - `Base` = pretrained only, no SFT/RLHF
  - `Instruct` = instruction-tuned for chat/tool-use
  - `Thinking` / reasoning-tuned = explicit chain-of-thought variant (Qwen3 family has `Qwen3-Thinking-2507` variants)
- `AWQ` — quantization method. Common options you'll see in HF model IDs: `AWQ`, `GPTQ`, `GGUF`, `bnb` (bitsandbytes), `MLX` (Apple Silicon), `FP8`, `NVFP4`, `Q4_K_M` (GGUF K-quant)
- `4bit` — bit width (sometimes written `W4A16` = 4-bit weights, 16-bit activations)

**Primary source for the quantization-method list** — HF Transformers quantization overview page:
> "Transformers supports many quantization methods, each with their pros and cons, so you can pick the best one for your specific use case. ... [table lists] AQLM | AutoRound | AWQ | bitsandbytes | compressed-tensors | EETQ | Four Over Six | FP-Quant | ... GGUF | GPTQ | HIGGS | HQQ | Metal | MXFP4 | Optimum | Quanto | Quark | torchao | SpQR | VPTQ | SINQ"
> URL: https://huggingface.co/docs/transformers/main/en/quantization/overview

**Corroborating — TGI (Text Generation Inference) quantization docs**:
> "TGI offers many quantization schemes ... TGI supports GPTQ, AWQ, bits-and-bytes, EETQ, Marlin, EXL2 and fp8 quantization. To leverage GPTQ, AWQ, Marlin and EXL2 quants, you must provide pre-quantized weights."
> URL: https://huggingface.co/docs/text-generation-inference/conceptual/quantization

**Real-world example from the Qwen3 HF collection** (shows the naming convention in practice):
- `Qwen/Qwen3-32B-MLX-8bit` — Apple MLX format, 8-bit
- `Qwen/Qwen3-32B-MLX-4bit` — Apple MLX format, 4-bit
- `Qwen/Qwen3-32B-MLX-6bit` — Apple MLX format, 6-bit
- `Qwen/Qwen3-32B-MLX-bf16` — Apple MLX format, BF16 (unquantized reference)
- `nvidia/Qwen3-32B-NVFP4` — NVIDIA's FP4 format (third-party quant of same model)
- `mlx-community/Qwen3-32B-8bit` — community-maintained 8-bit MLX
> URL: https://huggingface.co/collections/Qwen/qwen3

## Notes for Louis

- **Qwen3-32B's "headline MMLU"**: the cleanest number from a primary source is **MMLU-Pro 65.54** (Qwen3-32B-Base, from the Qwen Technical Report, arXiv 2505.09388). Qwen does *not* publish plain MMLU prominently for the 32B variant — they've moved up to MMLU-Pro as their reference metric. If you specifically want plain MMLU, you'll need to cite a third-party eval (Artificial Analysis or similar) and flag that it's not first-party.
- **"Qwen3-32B-Instruct" vs just "Qwen3-32B"**: the HF model card at https://huggingface.co/Qwen/Qwen3-32B covers the post-trained (chat-capable, hybrid thinking/non-thinking) model; there's no separate `-Instruct` suffix in the v1 Qwen3 naming. Qwen later released `Qwen3-30B-A3B-Instruct-2507` and `Qwen3-Thinking-2507` as updated variants. For slide A-12's toy example, `Qwen/Qwen3-32B-Instruct-AWQ-4bit` is a pedagogically useful hypothetical that follows HF conventions — but no such exact path exists in the official Qwen org; the closest real path is `Qwen/Qwen3-32B` (instruct-style by default) with community AWQ repos under third-party orgs. Flag this on the slide: "example format, not a literal Qwen repo."
- **Perplexity numbers are from Qwen2.5-32B-Instruct**, not Qwen3-32B. JarvisLabs hasn't published a dedicated Qwen3-32B quantization sweep yet (as of April 2026). The arXiv Qwen3 quantization study (2505.02214) gives qualitative findings but not a clean PPL table for 32B. **Slide A-10 should say "on Qwen2.5-32B as a reference" or generalize to "modern 32B models"** rather than claim Qwen3-specific numbers.
- **Spheron's "~76 GB" for Qwen 3 32B at FP16** includes real-world overhead (KV cache at typical context, CUDA runtime, framework tax). Pure napkin math gives 64 GB. Use whichever framing suits the slide: "weights alone" (64GB) vs "to actually serve it" (~76GB).
- **No "Qwen3-72B" exists.** Do not invent one. Qwen's dense ladder tops out at 32B; above that it's MoE (235B-A22B). This is *the* argument for why 32B is the sweet spot — there is literally no larger dense option in the family.
- **KV cache / activations formula** — Hivenet gives the practitioner rule of thumb: `hidden_size × num_layers × 2 (K/V) × seq_len × batch`. For Qwen3-32B that's 5120 × 64 × 2 × seq_len × batch × 2 bytes (BF16). At seq_len=8192 and batch=1 this is ~10GB extra on top of weights. If you need to show KV on a slide, cite Hivenet and flag precision assumption.
