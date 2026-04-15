---
marp: true
theme: station-f
paginate: true
header: "Building With AI · Station F · 2026-04-15"
footer: "Sources multiples · See docs/station-f/spec.md"
---

<!-- ABOUTME: Deck A of the Station F talk — LLMs state of the field + agents (definition, orchestration, components, examples). -->
<!-- ABOUTME: English-language scoped exception. Source of truth: docs/station-f/spec.md. -->

<!-- _class: title -->
<!-- _paginate: skip -->

# Building With AI, for Founders

## Station F · April 15, 2026

---

# 01 — Agenda

1. **Ecosystem momentum** — benchmarks, cost curves, where capability is going
2. **Different types of LLMs** — training pipeline, open vs closed, self-hosting sweet spot
3. **Agent harness** — the 6 components that make a coding agent work
4. **Agent examples** — Claude Code, OpenClaw, MiroFish, AutoResearch
5. **Frontier competition** — 7 battlegrounds, benchmarks that matter, why infra is the new moat

---

<!-- _class: section -->

# Where LLMs are going

---

<!-- _class: img-right -->

# 02 — Benchmarks: real progress, visible ceilings

![bg right:55% contain](assets/epoch_ai_llm_saturation_benchmarks.jpeg)

- MMLU (general knowledge): **saturated at 90%+** — LLMs are catching up with human experts [1]
- Newer, harder benchmarks: Humanity's Last Exam **8.8%**, FrontierMath **2%** [2]
- Efficiency: from **540B** down to **3.8B** params for 60% on MMLU — a **142x** reduction [1]

> Easy benchmarks saturate, but hard problems remain out of reach.

<small>Sources : [1] [Epoch AI](https://epoch.ai/trends) · [2] [Stanford HAI AI Index 2025](https://aiindex.stanford.edu/report/)</small>

---

<!-- _class: img-right -->

# 03 — METR: AI task autonomy doubles every 7 months

![bg right:55% contain](assets/benchmarks/metr-time-horizon-time-horizon-chart.png)

- METR measures the **time-horizon** an AI can complete with 50% reliability [1]
- The 50%-reliability horizon **doubles every ~7 months** over 6 years of data [1]
- 2019 GPT-2: ~3 seconds → Nov 2025 Claude Opus 4.5: **~4h 53min** [1]
- Bengio-led 2026 International AI Safety Report: **3× faster than Moore's Law** [2]

> If the curve holds, multi-day autonomous agents are 18 months away.

<small>Sources : [1] [METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) · [2] [Kwa et al. 2025, arXiv:2503.14499 (CC BY 4.0)](https://arxiv.org/abs/2503.14499)</small>

---

<!-- _class: img-right -->

# 04 — Inference cost is collapsing

![bg right:55% contain](assets/benchmarks/epoch-inference-01.png)

- Cost per million tokens **drops ~10×/year** for equivalent capability [1]
- GPT-3.5 (Dec 2022) → GPT-5-mini (2026): same task, **~100× cheaper** [1]
- Open-weights matched: Mistral Small 3 24B beats Llama 3.3 70B at **1/3 the cost** [2]
- Founder implication: the cost of "smart" approaches zero faster than the cost of "more"

> Build for capability now, expect the price to crater under your feet within 12 months.

<small>Sources : [1] [Epoch AI — LLM inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) · [2] [Mistral Small 3](https://mistral.ai/news/mistral-small-3)</small>

---

<!-- _class: img-right -->

# 05 — Open-source closes the gap to ~3 months

![bg right:55% contain](assets/benchmarks/epoch-os-gap-01.png)

- **Epoch AI (Oct 2025)**: frontier open-weight models lag closed models by **~3 months** on average (ECI metric) [1]
- Capability gap: ~7 ECI points — comparable to o3 vs GPT-5 [1]
- Mistral **Devstral 2** (Mar 2026): top open-weight coder, **4× smaller / 7× cheaper** than Claude Sonnet at comparable scores [2]
- Google **Gemma 4** (Apr 2 2026, Apache 2.0): on-device agentic capabilities [3]
- Founder play: build with open-weights for cost & data residency; switch to closed only when SOTA matters

> The gap is narrow enough to plan around — but it widens whenever a new frontier release lands.

<small>Sources : [1] [Epoch AI — Open-weights vs closed-weights gap](https://epoch.ai/data-insights/open-weights-vs-closed-weights-models/) · [2] [Mistral — Devstral](https://mistral.ai/news/devstral) · [3] [Google — Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)</small>

---

<!-- _class: img-right -->

# 06 — Context windows: from kilobytes to libraries

![bg right:55% contain](assets/context-window-growth.png)

- 2022 GPT-3: 4K tokens (~3 pages)
- 2024 Claude 3 Opus: 200K tokens (~150 pages)
- 2026 Claude Opus 4.6: **1M tokens** native context (~750 pages) [1]
- Gemini 1.5 Pro: **2M tokens** [2]
- Llama 4 family: **10M tokens** for the largest variant [3]
- Founder consequence: "RAG everything" is no longer the only architecture — **direct context-loading** is competitive for many use cases

> 1M tokens = a small codebase, a quarterly report, a year of customer transcripts. All in one prompt.

<small>Sources : [1] [Anthropic — Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) · [2] [Google — Gemini 1.5 Pro 2M](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024/) · [3] [Meta — Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)</small>

---

<!-- _class: img-right compact -->

# 07 — Training compute: 5× per year, since 2020

![bg right:55% contain](assets/benchmarks/epoch-training-compute-figure-compute-trend-frontier-llm.png)

- Frontier-LLM training compute grows **5×/year** since 2020 [1]
- 2018 BERT: ~**$3,300** → 2023 GPT-4: **$78M** → 2027 frontier: **>$1B** projected [2]
- Counter-trend: **DeepSeek-V3** (2024) ≈ GPT-4o for **14× cheaper** ($5.6M total, H800 at $2/h) [3]
- Industry-wide: a **kinked exponential** — pre-2020 a different slope, then 5×/year takes over

> Two curves stacked: the bill keeps doubling for the leaders, while reproducing yesterday's frontier keeps getting cheaper.

<small>Sources : [1] [Epoch AI — Training compute grows 5×/year](https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year/) · [2] [Cottier et al. (Epoch AI)](https://arxiv.org/abs/2405.21015) · [3] [DeepSeek-V3 tech report](https://arxiv.org/abs/2412.19437)</small>

---

<!-- _class: img-right compact-table -->

# 08 — How LLMs are trained: 4 stages

![bg right:55% contain](assets/infographics/training-pipeline.png)

| Stage | What it learns | Data | Result |
|-------|----------------|------|--------|
| **Pretraining** | Language, world knowledge | ~15T tokens [1] | Base model |
| **SFT** | Follow instructions | ~25K–1M examples [2] | Instruct model |
| **RLHF / DPO** | Be helpful, honest, harmless | ~100K–1M pairs [3] | Aligned chatbot |
| **Reasoning** | Think before answering | ~5K seeds → 800K [4] | Thinking model |

> Each stage stacks on the previous — with **exponentially less data** at each step.

<small>Sources : [1] [Meta Llama 3](https://ai.meta.com/blog/meta-llama-3/) · [2] [RLHF Book (arXiv:2504.12501)](https://arxiv.org/abs/2504.12501) · [3] [Anthropic hh-rlhf](https://huggingface.co/datasets/Anthropic/hh-rlhf) · [4] [DeepSeek-R1 (arXiv:2501.12948)](https://arxiv.org/abs/2501.12948)</small>

---

<!-- _class: cols compact -->

# 09 — Training cost: the pincer

<div class="left">

**Frontier climbs — ×2.4/year since 2016** [1]:

- BERT (2018): **~$7K** [2]
- GPT-3 (2020): **~$4.6M** [3]
- GPT-4 (2023): **$40–100M** amortized [1]
- GPT-4.5 / Grok 4 (2025): **~$500M** [4]
- Frontier (2026+): **$5–10B** (Amodei) [5]

*Projection*: a single training run crosses **$1B by 2027** [1].

</div>
<div class="right">

**Reproducing collapses**:

- Llama 2 70B (2023): **~$3M** (1.7M A100-h × $2) [6]
- **DeepSeek-V3** (Dec 2024): **$5.576M** — matches GPT-4o [7]
- Qwen3-Next (Sep 2025): **9.3%** of Qwen3-32B's cost, equal quality [8]
- Karpathy GPT-2 repro: **$43K → $73** in 6 years (≈ **×600** cheaper) [9]

Fast followers catch last year's frontier for **~1%** of its budget.

</div>

> **Leaders spend 10× more per year. Followers spend 10× less per year.**

<small>Sources : [1] [Cottier et al. (Epoch)](https://arxiv.org/abs/2405.21015) · [2] [Synced 2019](https://syncedreview.com/2019/06/27/the-staggering-cost-of-training-sota-ai-models/) · [3] [Lambda Labs](https://lambda.ai/blog/demystifying-gpt-3) · [4] [Epoch Gradient Updates](https://epoch.ai/gradient-updates/why-gpt5-used-less-training-compute-than-gpt45-but-gpt6-probably-wont) · [5] [Amodei — Dwarkesh](https://www.dwarkesh.com/p/dario-amodei-2) · [6] [Llama 2 card](https://huggingface.co/meta-llama/Llama-2-70b) · [7] [DeepSeek-V3 arXiv](https://arxiv.org/abs/2412.19437) · [8] [Qwen3-Next](https://www.alibabacloud.com/blog/602580) · [9] [Karpathy llm.c #677](https://github.com/karpathy/llm.c/discussions/677)</small>

---

<!-- _class: compact compact-table -->

# 10 — Quantization: how much quality do you lose?

Reference benchmarks on Qwen2.5-32B-Instruct (H200 GPU) [1]:

| Quant | Bytes/param | Perplexity (WikiText) | HumanEval Pass@1 | Use case |
|-------|-------------|-----------------------|-------------------|----------|
| FP16 | 2 | 6.56 | 56.1% | Training, pristine serving |
| INT8 (bnb) | 1 | 6.67 | 51.8% | Production, halves VRAM |
| AWQ INT4 | 0.5 | 6.84 | 51.8% | Self-hosting on consumer GPUs |
| GGUF Q4_K_M | ~0.5 | 6.74 | 51.8% | llama.cpp / CPU-fallback |

- AWQ preserves **outlier weights** at higher precision → minimal quality loss
- GGUF (llama.cpp) ships with `ollama`, `lm-studio` — easiest local stack
- Qwen3 specifically: stick to **4-bit minimum** — stronger base models are more sensitive to aggressive quantization [2]

> 4-bit gets you **~96% of FP16 quality** at **25% of VRAM cost**. Default to AWQ or Q4_K_M unless output must be pristine.

<small>Sources : [1] [JarvisLabs — vLLM quantization benchmarks](https://docs.jarvislabs.ai/blog/vllm-quantization-complete-guide-benchmarks) · [2] [Qwen3 quantization study (arXiv:2505.02214)](https://arxiv.org/html/2505.02214v1)</small>

---

<!-- _class: compact -->

# 11 — How much VRAM does my model need?

- Rule of thumb: **GB ≈ params(B) × bytes/param** [1]
- FP16 = 2 bytes/param → 32B model needs **~64GB**
- INT8 = 1 byte/param → 32B fits **~32GB**
- INT4 (AWQ / GGUF Q4) = 0.5 bytes/param → 32B fits **~16GB** — runs on a **single RTX 4090**
- Plus KV-cache + activations: budget **+20-30% headroom** [1]

> Self-hosting is now a desktop sport, not a datacenter sport — for the right model + quant.

<small>Sources : [1] [Spheron — GPU Memory Requirements for LLMs](https://www.spheron.network/blog/gpu-memory-requirements-llm/)</small>

---

<!-- _class: cols compact -->

# 12 — Reading Hugging Face model names

<div class="left">

Example: `Qwen/Qwen3-32B-Instruct-AWQ-4bit`

| Part | Meaning |
|------|---------|
| `Qwen` | HF org handle |
| `Qwen3` | Model family |
| `32B` | Params (billions) |
| `Instruct` | Variant (Base / Instruct / Thinking) |
| `AWQ` | Quantization method |
| `4bit` | Bit width |

*Pedagogical path — Qwen3 v1 actually ships as `Qwen/Qwen3-32B` (no `-Instruct` suffix).*

</div>
<div class="right">

**Other suffixes you'll meet** [1]:

- `Coder`, `Math` — domain fine-tunes
- `Thinking`, `R1`, `o1`-style — reasoning-tuned
- `MoE`, `A22B` — Mixture of Experts
- `GGUF`, `GPTQ`, `bnb`, `MLX`, `FP8` — quant formats
- `Q4_K_M`, `Q5_K_S` — GGUF K-quant variants

> Decoding the name tells you what hardware you need.

</div>

<small>Sources : [1] [Qwen3 collection on Hugging Face](https://huggingface.co/collections/Qwen/qwen35)</small>

---

<!-- _class: img-right compact -->

# 13 — Qwen3-32B: the self-hosting sweet spot

![bg right:55% contain](assets/infographics/mmlu-params-graph.svg)

- Qwen3-32B (Alibaba, **Apache 2.0**): **MMLU-Pro 65.54** [1]
- INT4-quantized: **~16-22GB VRAM** — fits a single RTX 4090 [2]
- Outperforms Qwen2.5-72B-Base on **10 of 15 benchmarks** at less than half the parameters [1]
- 32K context native / **128K with YaRN**, multilingual, function calling [3]
- Dense ladder tops out at 32B — no Qwen3-72B exists; next step up is 235B-A22B MoE (~470GB VRAM)

> Production-grade reasoning without sending a single token to Anthropic or OpenAI.

<small>Sources : [1] [Qwen3 Technical Report (arXiv:2505.09388)](https://arxiv.org/abs/2505.09388) · [2] [Spheron — GPU Memory for LLMs](https://www.spheron.network/blog/gpu-memory-requirements-llm/) · [3] [Qwen3-32B HF card](https://huggingface.co/Qwen/Qwen3-32B)</small>

---

<!-- _class: section -->

# Agents

---

<!-- _class: img-right -->

# 14 — What counts as an agent

![bg right:55% contain](assets/raschka/02-llm-reasoning-agent-relationship.png)

- A plain LLM call is not an agent. An **agent** is a loop: observe → inspect → choose → act, against an environment [1].
- **Agent harness** = scaffolding around the model: prompts, tools, state, control flow [1].
- **Coding harness** = task-specific harness for software engineering [1].

> Claude Code and the same API model in ChatGPT are *the same LLM*. What you notice is the harness. [2]

<small>Sources : [1][2] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right compact -->

# 15 — Untangling an agent: 4 parts around the brain

![bg right:55% contain](assets/anthropic/managed-agents-overview.png)

Anthropic's "managed agents": **decoupled interfaces, not a monolith** [1]:

- **Harness** (brain) — loop calling the model, routing tool calls
- **Session** — append-only event log, outside the context window
- **Tools + Resources** (hands) — typed `execute(name, input)` via MCP
- **Sandbox** — container, phone, CI runner — harness doesn't care
- **Orchestration** — scheduler that wakes sessions (cron, queue, loop)

> **Founder rule**: pick swappable interfaces. New brain tomorrow; session + tools + sandbox survive. [1]

<small>Sources : [1] [Anthropic — Managed agents](https://www.anthropic.com/engineering/managed-agents)</small>

---

<!-- _class: img-right -->

# 16 — The agent cycle: Think → Act → Observe

![bg right:55% contain](assets/agent-cycle-hf.gif)

The fundamental loop of any agent [1][2]:

1. **Think** — reason about the task
2. **Act** — execute (search, API, computation)
3. **Observe** — analyze the result
4. **"Goal reached?"** → if not, back to Think

**Example**: *Think* "find Mistral AI's revenue" → *Act* web search → *Observe* "$300M ARR" → *Think* "synthesize answer".

<small>Sources : [1] [HuggingFace — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) · [2] [ReAct — Princeton/Google](https://arxiv.org/abs/2210.03629)</small>

---

<!-- _class: img-right -->

# 17 — Anatomy of a coding agent: 6 components

![bg right:55% contain](assets/raschka/13-six-features-summary.png)

Capability comes less from the model, more from the surrounding system [1]. Six recurring components across Claude Code, Codex CLI, and the Mini Coding Agent [2]:

1. Live Repo Context
2. Prompt Shape + Cache Reuse
3. Tool Access + Permissions
4. Context Compaction
5. Structured Session Memory
6. Bounded Subagents

> "A lot of apparent 'model quality' is really context quality." — Raschka [3]

<small>Sources : [1][2][3] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 18 — Component 1 — Live Repo Context

![bg right:55% contain](assets/raschka/06-workspace-summary.png)

- The agent collects **stable facts** about your workspace upfront [1]
- Git state, repo layout, AGENTS.md / CLAUDE.md conventions, recent test results
- "Fix the tests" is **not self-contained** — the meaning lives in the repo, not the prompt

> Founder takeaway: this is why a thin chat wrapper around GPT-5 doesn't beat Claude Code. The harness reads your project for you.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 19 — Component 2 — Stable Prompt Prefix + Cache Reuse

![bg right:55% contain](assets/raschka/07-stable-prompt-prefix.png)

- Instructions + tool list + repo summary form a **stable prompt prefix** [1]
- Reused across every turn via **prompt caching** — same bytes, ~10× cheaper, ~2× faster
- Only session state (recent transcript + newest user request) changes turn-to-turn

> The cheap-but-stable part stays cheap. The new-but-small part stays small. That's how you make 100-turn sessions affordable.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 20 — Component 3 — Tool Access

![bg right:65% contain](assets/raschka/08-tool-use-flow-full.png)

- Tools = the line between **chat** and **agency** [1]
- Model emits a structured action → harness **validates** (typed inputs, path checks) → **approves** → **executes** → feeds result back into the loop [1]
- Claude Code ships with **~18 named tools** — `BashTool`, `FileEditTool`, `WebFetchTool`, etc. [2]

> The harness gives the model less freedom — and that's exactly why it ships. [1]

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 21 — Component 4: Context Compaction

![bg right:55% contain](assets/raschka/10-context-compaction.png)

- Long contexts are expensive and noisy; coding agents **bloat fast** via repeated reads, long outputs, logs [1].
- Two core strategies: **clip** oversized items, **summarize** older transcript entries, plus deduplicate repeated file reads [1].
- The Claude Code leak reveals **five distinct compaction types** across the runtime [2] — see next slide.

> Underrated, boring, and decisive — context quality *is* model quality.

<small>Sources : [1] [Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right compact -->

# 22 — The leaked Claude Code compaction stack

![bg right:55% contain](assets/latent-space/05-compaction-types.png)

Latent Space's analysis of the leaked source: **5 distinct compaction strategies** inside Claude Code [1]:

- Per-tool clipping — long tool outputs trimmed before they hit transcript
- Transcript summarization — older turns rewritten as brief summaries
- File-read deduplication — repeated reads collapsed
- Session consolidation (**autoDream**) — merge, dedupe, prune contradictions
- Subagent fork-caching — children reuse parent's prompt cache

> The production agent is a **stack of tiny context-janitors**, not one big summarizer.

<small>Sources : [1] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 23 — Component 5 — Memory part 1: architecture

![bg right:55% contain](assets/raschka/11-transcript-and-memory.png)

- Two storage layers, both on-disk JSON [1]:
  - **Working memory** — distilled, small, "what matters now"
  - **Full transcript** — every turn, append-only, durable, resumable
- Working memory feeds into the next prompt; transcript serves audit + replay

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 24 — Component 5 — Memory part 2: leverage

![bg right:55% contain](assets/latent-space/03-memory-3layer.png)

- Claude Code's leaked architecture: **three layers** [1]
  - `MEMORY.md` index → topic files → session transcripts
- **autoDream** consolidation mode merges, dedupes, prunes contradictions [1]
- **Subagents share parent's prompt cache via fork pattern** — parallelism without re-paying context cost [1][2]
- Founder leverage: write a thoughtful `CLAUDE.md` once, get its benefit on every session

<small>Sources : [1] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak) · [2] [Raschka — bounded subagents](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 25 — Component 6 — Bounded Subagents + resilience

![bg right:55% contain](assets/raschka/12-bounded-subagent.png)

- Delegation parallelizes subtasks: "which file defines X?", "why is this test failing?" [1]
- Hard part isn't *spawning* subagents, it's **binding** them — enough context to work, tight enough to not explode [1]
- Techniques: read-only mode, recursion depth limits, task scoping
- The leaked architecture also reveals **explicit retry + exponential-backoff resilience** at the runtime layer [2]

> "The tricky design problem is not just how to spawn a subagent but also how to bind one :)." — Raschka [1]

<small>Sources : [1] [Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 26 — The 5-level permission system

![bg right:55% contain](assets/latent-space/06-permission-system.png)

<!-- Per-level tool examples are illustrative inferences; the Latent Space archive confirms a 5-level hierarchy but is paywalled on per-level specifics. -->

- Tools aren't yes/no — they live on a **permission spectrum** [1]
- Level 1 — auto-allow (read-only operations: `Read`, `Glob`, `Grep`)
- Level 2 — notify (write inside working directory: `Edit`, `Write`)
- Level 3 — confirm (write outside, network calls: `Bash`, `WebFetch`)
- Level 4 — human-approval (destructive operations: `rm`, `git push`)
- Level 5 — blocked (dangerous patterns: `rm -rf /`, sudo, etc.)

> The permission system is what lets you sleep while Claude Code refactors overnight.

<small>Sources : [1] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 27 — The golden rule: start simple

![bg right:55% contain](assets/infographics/anthropic-complexity-ladder.png)

Anthropic "Building Effective Agents" [1]:

| Level | Pattern |
|---|---|
| 1 | Prompt Chaining |
| 2 | Routing |
| 3 | Parallelization |
| 4 | Orchestrator-Workers |
| 5 | Evaluator-Optimizer |
| 6 | Autonomous agent |

> "The most successful implementations weren't using complex frameworks." Most business problems get solved at levels 1–3.

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 28 — Pattern 1: Prompt Chaining

![bg right:55% contain](assets/anthropic/01-chaining.png)

- Sequential LLM calls, each consumes the previous output [1]
- **Concrete example**: support email triage
  1. Classify the email's intent (refund / bug / complaint)
  2. Extract key facts (order id, dates, customer mood)
  3. Draft a response in the support team's voice
  4. Gate-check before sending: does the response answer the original ask?

> Covers the majority of business workflows. Start here.

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 29 — Pattern 2: Routing

![bg right:55% contain](assets/anthropic/02-routing.png)

- Classify the input, route to a specialized handler [1]
- **Concrete example**: customer-support model routing
  - Simple FAQ → cheap LLM ($0.06/M tokens)
  - Complex case → premium LLM ($15/M tokens)
  - Anything escalation-flagged → human agent
- Optimizes **cost AND quality simultaneously** — the simplest multi-model pattern that pays back

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 30 — Pattern 3: Parallelization

![bg right:55% contain](assets/anthropic/03-parallelization.png)

- *Sectioning*: independent subtasks run in parallel (legal + financial + technical contract review)
- *Voting*: same task, multiple independent runs, majority wins
- **Concrete example**: 3 independent LLM judges score generated marketing copy; ship if 2/3 agree
- 2–3× cost; use when **speed** or **reliability** beats raw cost

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 31 — Pattern 4: Orchestrator-Workers

![bg right:55% contain](assets/anthropic/04-orch-workers.png)

- A central LLM **dynamically decomposes** the task at runtime [1]
- Delegates each piece to a specialized worker, then synthesizes the result
- **Concrete example**: refactor a multi-file PR
  - Orchestrator reads the diff, plans the migration
  - Workers each rewrite one file (parallel)
  - Orchestrator runs the test suite, reconciles failures
- The agentic IDE pattern (Cursor, Cline, Claude Code, etc.)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 32 — Pattern 5: Evaluator-Optimizer

![bg right:55% contain](assets/anthropic/05-eval-opt.png)

- Generator + Evaluator loop, iterating until quality bar met [1]
- **Concrete example**: generate a sales email
  - Generator drafts the email
  - Evaluator scores tone, CTA strength, brand-voice fit
  - Loop until score ≥ threshold OR circuit-breaker (3-5 rounds max)
- Always add a circuit breaker — otherwise you've built an infinite-cost machine

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 33 — Agents in the wild: Claude Code

![bg right:55% contain](assets/agent_stack-claude_code.jpeg)

A terminal-native agent that reads, writes, and executes code autonomously [1]:

- Reads/writes files, runs bash, manages git
- **CLAUDE.md** — persistent project instructions
- **MEMORY.md** — automatic memory across sessions
- **Skills** — reusable modular capabilities
- **Subagents** — parallelize sub-tasks

**The Knowledge Work Stack** [2]: Model → Harness → Personal Scaffolding → MCPs/APIs → Agents.

<small>Sources : [1] [Anthropic — Claude Code](https://www.claude.com/product/claude-code) · [2] [Taylor Pearson](https://x.com/TaylorPearsonMe/status/2029996204306866585)</small>

---

<!-- _class: compact -->

# 34 — Agents in the wild: OpenClaw

- **What it is**: open-source, local-first personal agent (messaging-centric, MIT license) by Peter Steinberger [1]
- **Headline**: **247 000 stars + 47 700 forks** on GitHub as of March 2, 2026 [1]
- **Distinct angle**: vs Claude Code — open + local-first, no IDE lock-in; vs MiroFish — single personal assistant, not a swarm; vs AutoResearch — full product with a skills marketplace (ClawHub)
- **Founders' caveat**: Cisco's Skill Scanner audit found **26% of 31 000 agent skills contained at least one vulnerability**; OpenClaw running a third-party skill produced "nine security findings, including two critical and five high severity issues" [2]
- **Status**: Steinberger joined OpenAI on Feb 14, 2026; OpenClaw moves to a foundation and "will stay open and independent" [3]

> The proof that there's an open-source appetite for personal agents.

<small>Sources : [1] [Wikipedia — OpenClaw](https://en.wikipedia.org/wiki/OpenClaw) · [2] [Cisco — Skill Scanner audit](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) · [3] [Steinberger blog — joining OpenAI](https://steipete.me/posts/2026/openclaw)</small>

---

<!-- _class: img-right -->

# 35 — Agents in the wild: MiroFish

![bg right:55% contain](assets/mirofish/MiroFish_logo_compressed.jpeg)

- **What it is**: open-source swarm-intelligence engine — thousands of LLM personas simulate a digital world to forecast social / political / financial outcomes [1]
- **Headline**: **~52–54k GitHub stars** (Apr 2026); AGPL-3.0; Python + Vue [1]
- **Built on**: CAMEL-AI's OASIS engine + GraphRAG — composes Raschka's six components [1][2]
- **Distinct angle**: multi-agent swarm (not a single assistant); parallel worlds for prediction
- **Real cases**: Wuhan opinion simulation, "Dream of the Red Chamber" lost-ending prediction [1]

> A real-world agent stack assembled from the building blocks we just covered.

<small>Sources : [1] [GitHub — MiroFish](https://github.com/666ghj/MiroFish) · [2] [CAMEL-AI OASIS](https://github.com/camel-ai/oasis)</small>

---

<!-- _class: compact -->

# 36 — Agents in the wild: AutoResearch (Karpathy)

- **What it is**: Karpathy's autonomous ML-research harness — **a 630-line Python script** where the agent edits `train.py` and keeps/discards changes based on `val_bpb` [1]
- **Headline**: **70 300 GitHub stars**, 10 200 forks as of April 2026; **5-minute fixed time budget per experiment**; 1 GPU, 1 file, 1 metric [1]
- **Result**: **11% gain on "time to GPT-2 level"** — from 2.02h down to 1.80h after ~20 autonomously-discovered optimizations [2]
- **Distinct angle**: the "agent-as-script" extreme — no harness framework, no UI, just a clear `program.md` and a tight experimental loop
- **The conceptual shift**: "Markdown sits at the exact intersection of human editability and agent parseability" — you write the `program.md`, the agent writes the Python [3]

> Proof that the harness can be 600 lines of Python — the system matters more than the framework.

<small>Sources : [1] [GitHub — karpathy/autoresearch](https://github.com/karpathy/autoresearch) · [2] [36kr — Karpathy's result](https://eu.36kr.com/en/p/3725521482578567) · [3] [The New Stack](https://thenewstack.io/karpathy-autonomous-experiment-loop/)</small>

---

<!-- _class: section -->

# Frontier — what's next

---

<!-- _class: compact compact-table -->

# 37 — 7 battlegrounds of the agentic race (Q1 2026)

| Battleground | Leaders | Signal |
|---|---|---|
| **Coding agents** | Claude Code, Codex, Cursor | Claude Code ~**$2.5B ARR**; Codex **2M WAU** (+70% MoM); Cursor **$1B ARR** [1][2] |
| **Computer / GUI** | GPT-5.4, Project Mariner | GPT-5.4 first to pass human OSWorld baseline (**75.0%** vs 72.4%) [3][4] |
| **MCP / protocol** | Anthropic (+Linux Foundation) | MCP donated to AAIF (Dec 2025); **10,000+** servers; integrated everywhere [5] |
| **Multi-agent orchestration** | Microsoft, LangChain, CrewAI | Gartner: **+1,445%** enterprise inquiries; MS Agent Framework 1.0 GA [6] |
| **Enterprise agents** | Microsoft, AWS, Cohere | Agent 365 **$15/user/mo** · Bedrock AgentCore GA · North runs on 2 GPUs [7] |
| **Safety & alignment** | Anthropic, OpenAI, METR | Task autonomy **×2 every 7 mo** (3× Moore's) · OpenAI bought Promptfoo [8] |
| **OSS vs proprietary** | Meta, Mistral, Zhipu | Meta acquired Manus for **$2B** · Devstral 2 **72.2% SWE-bench Verified** (open) [9] |

> Closed models lead the benchmarks, open models close the gap in months, and the infrastructure layer is where the $ flows.

<small>Sources : [1] [Anthropic](https://www.anthropic.com/claude-code) · [2] [OpenAI Codex](https://openai.com/index/unrolling-the-codex-agent-loop/) · [3] [OpenAI GPT-5](https://openai.com/index/introducing-gpt-5/) · [4] [Project Mariner](https://deepmind.google/models/project-mariner/) · [5] [Linux Foundation AAIF](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) · [6] [MS Agent Framework](https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/) · [7] [AWS AgentCore GA](https://aws.amazon.com/about-aws/whats-new/2025/10/amazon-bedrock-agentcore-available/) · [8] [METR time-horizon](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) · [9] [Mistral Devstral 2](https://mistral.ai/news/devstral-2-vibe-cli)</small>

---

<!-- _class: img-right -->

# 38 — Benchmark deep-dive: SWE-bench (a family)

![bg right:55% contain](assets/benchmarks/swebench-leaderboard.png)

- SWE-bench isn't one number — it's a **family of benchmarks** [1]
- **Verified** (500 hand-vetted Python issues): saturated, six frontier models within **1.3 points at ~80%** — Claude Opus 4.5 leads at 80.9% [2]
- **Pro** (1,865 tasks across Python/Go/TS/JS, private codebases): leader **GPT-5.4 at 57.7%** — designed to be much harder [2]
- **Multilingual / Multimodal / Lite**: emerging variants tracking specific gaps [1]
- Reading rule: most labs report `Verified`. **`Pro` is the honest signal** for production use

> Same model, same task, very different scores depending on the variant. Always pin the variant when comparing claims.

<small>Sources : [1] [SWE-bench paper (arXiv)](https://arxiv.org/abs/2310.06770) · [2] [SWE-bench leaderboard](https://www.swebench.com/)</small>

---

<!-- _class: img-right -->

# 39 — Benchmark deep-dive: Terminal-Bench

![bg right:55% contain](assets/benchmarks/terminal-bench-01.png)

- **What it measures**: 89 real-world terminal tasks (software engineering, biology, security, gaming) in Docker containers [1]
- **Concrete example**: "Set up a PostgreSQL database with these 4 tables and seed it from this CSV" — agent must work end-to-end in the shell
- **Current SOTA Q1 2026**: Gemini 3.1 Pro = **78.4%** (Forge Code scaffold); GPT-5.3-Codex 77.3%; GPT-5.4 75.1% [1]
- **Hard subset**: GPT-5.4 leads at **57.6%** — agentic coding still has headroom
- **Founder takeaway**: shell-fluent agents are ~80% reliable on standard tasks but break on novel multi-tool workflows

<small>Sources : [1] [Terminal-Bench (Stanford / Laude Institute)](https://www.tbench.ai/)</small>

---

<!-- _class: img-right -->

# 40 — Benchmark deep-dive: OSWorld

![bg right:55% contain](assets/benchmarks/osworld-tasks.png)

- **What it measures**: 369 desktop tasks across Ubuntu, Windows, macOS — multi-app workflows, real GUIs [1]
- **Concrete example**: "Take this CSV, clean it in LibreOffice, paste it into a Slack message"
- **Current SOTA Q1 2026**: GPT-5.4 = **75.0%** — first model to exceed the **72.4% human expert baseline** [1]
- **Trajectory**: 4% (early 2024) → 75% (Mar 2026) — superhuman on a comprehensive computer-use benchmark
- **Founder takeaway**: GUI agents are no longer experimental for mainstream desktop tasks

<small>Sources : [1] [OSWorld (Salesforce / NUS)](https://os-world.github.io/)</small>

---

<!-- _class: img-right -->

# 41 — Benchmark deep-dive: GAIA

![bg right:55% contain](assets/benchmarks/gaia-leaderboard.png)

- **What it measures**: 466 multi-step assistant questions requiring reasoning, web browsing, and tool use [1]
- **Concrete example**: "Find the second-most-cited paper from this 2017 conference and summarize its abstract" — needs search + parse + reasoning
- **Current SOTA Q1 2026**: H2O.ai's h2oGPTe = **75%** on test set — first "C grade" — still far below **92% human baseline** [1]
- **Trajectory**: Manus AI 57.7% on validation set; gap to human baseline still wide for multi-hop tasks
- **Founder takeaway**: don't trust agents alone for research — keep humans in the loop for the final synthesis

<small>Sources : [1] [GAIA leaderboard (HuggingFace)](https://huggingface.co/spaces/gaia-benchmark/leaderboard)</small>

---

<!-- _class: compact -->

# 42 — Infrastructure is the new moat

- Six frontier models cluster within **1.3 points on SWE-bench Verified** [1]
- Same model + different harness = **10–22 point swing** in score (Claude Opus 4.5: 45.9% → 55.4% on SWE-bench Pro) [2]
- Grok 4 self-reports 72-75%; controlled measurement: **58.6%** [2]
- Meta's $2B Manus acquisition: bought the **execution layer**, not the model
- The race shifted from intelligence to infrastructure — harness engineering, protocol integration, governance, safety

> "Better models alone won't get agents to production." — Harrison Chase, LangChain

<small>Sources : [1] [SWE-bench leaderboard](https://www.swebench.com/) · [2] [vals.ai — SWE-bench harness study](https://www.vals.ai/benchmarks/swebench)</small>

---

<!-- _class: highlight -->

# 43 — Takeaway: model vs harness

- Vanilla LLMs are **converging in raw capability** (1.3-point spread on SWE-bench) [1]
- The harness is the distinguishing factor [2]
- Founder implication: **a thin wrapper over GPT-5 is not your moat.** The system around the model is.

> "The harness can often be the distinguishing factor that makes one LLM work better than another." — Raschka [2]

<small>Sources : [1] [SWE-bench leaderboard](https://www.swebench.com/) · [2] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>
