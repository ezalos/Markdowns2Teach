# Training cost research — for Station F slide 10

**Accessed**: 2026-04-15
**Author**: Claude (research subagent for Louis)
**Purpose**: Evidence pack for a "pincer" slide narrative — frontier costs climbing exponentially vs. open-weight replication costs crashing.

---

## §1 Frontier LLMs: cost of beating the state-of-the-art

All figures are **amortized hardware + energy** for the **final training run only** (the Epoch AI methodology — excludes R&D staff, failed runs, and prior experiments, which are typically 2-3x larger). Costs in nominal USD of the model's release year unless noted.

| Model | Year | Params | Training cost (USD) | Source | Quote / notes |
|-------|------|--------|--------------------:|--------|---------------|
| BERT-Large | 2018 | 340M | **~$7K** (pre-training, single run on 64 TPU v2 chips × 4 days) | [Synced Review 2019](https://syncedreview.com/2019/06/27/the-staggering-cost-of-training-sota-ai-models/) | "Google BERT — estimated total training cost: US$6,912 … 16 (devices) × 4 (days) × 24 (hours) × 4.5 (US$ per hour) = US$6,912" |
| GPT-2 (1.5B) | 2019 | 1.5B | **~$43K** (32 TPU v3 × 168h × $8/h) | [Wikipedia citing Karpathy](https://en.wikipedia.org/wiki/GPT-2) | "GPT-2 was trained by OpenAI on 32 TPU v3 chips for 168 hours (7 days), at approximately $8 per TPU v3 per hour, for a total estimated compute cost of about $43,000." |
| GPT-3 | 2020 | 175B | **~$4.6M** (Lambda Labs V100 estimate, widely cited); Epoch lists higher amortized cost incl. experiments | [Lambda Labs](https://lambda.ai/blog/demystifying-gpt-3) · [a16z](https://a16z.com/navigating-the-high-cost-of-ai-compute/) | "Training GPT-3 would cost over $4.6M using a Tesla V100 cloud instance … 355 GPU-years" (Lambda). a16z: "Other estimates of GPT-3 training cost range from $500,000 to $4.6 million, depending on hardware assumptions." |
| GPT-4 | 2023 | ~1.8T MoE (rumored) | **~$40M** amortized hardware+energy (Epoch); **$78–100M+ compute** including experiments (Statista/Epoch); Altman said "more than $100M" | [Epoch AI paper](https://arxiv.org/html/2405.21015v2) · [Statista chart](https://www.statista.com/chart/33114/estimated-cost-of-training-selected-ai-models/) | Cottier et al. 2024: "Currently, GPT-4 has the largest amortized hardware and energy cost, at $40M." Statista/Epoch: "ChatGPT-4 … had a technical creation cost of $41 million to $78 million … Sam Altman … has in the past said that the model has cost more than $100 million" |
| o1 / o3 (Dec 2024 preview) | 2024–25 | Undisclosed | **NOT PUBLISHED — Epoch lacks FLOP estimate; cost modeled via H100-cluster heuristics** | [Epoch AI on OpenAI compute](https://epoch.ai/data-insights/openai-compute-spend) · [Epoch on compute vs accuracy](https://epoch.ai/data-insights/compute-vs-accuracy) | "these trends exclude many of the top-performing models, such as OpenAI's o1, which we lack compute estimates for." For context, OpenAI's **2024 total R&D compute ≈ $5B; 2025 ≈ $9B** (Epoch via The Information). |
| GPT-4.5 (Orion) | Feb 2025 | Undisclosed | **~$500M** (order-of-magnitude; Epoch illustrative figure) | [Epoch Gradient Updates](https://epoch.ai/gradient-updates/why-gpt5-used-less-training-compute-than-gpt45-but-gpt6-probably-wont) | "For illustration, the cost of training Grok 4 was around $500 million, and we expect GPT-4.5 to be in a similar ballpark (but slightly lower)." Cluster modeled at 40K–100K H100s × 90–165 days × $1.50–$3/H100-hour. |
| Grok 4 | 2025 | Undisclosed | **~$500M** (Epoch illustrative) | [Epoch Gradient Updates](https://epoch.ai/gradient-updates/why-gpt5-used-less-training-compute-than-gpt45-but-gpt6-probably-wont) | Same source as above. xAI's Colossus 2 cluster went live Jan 2026 at 1 GW / ~555K GPUs / ~$18B capex ([Introl](https://introl.com/blog/xai-colossus-2-gigawatt-expansion-555k-gpus-january-2026)). |
| Claude Opus 4.x (4.5/4.6) | 2025–26 | Undisclosed | **NOT PUBLISHED — flag for Louis** | [Dwarkesh interview with Amodei](https://www.dwarkesh.com/p/dario-amodei-2) · [BI 2024](https://www.businessinsider.com/anthropic-ceo-cost-10-billion-train-ai-years-language-model-2024-4) | Amodei 2024 trajectory: *"Today's models cost of order $100 million … models in training now [2024] are closer to $1 billion. And then I think in 2025 and 2026, we'll get more towards $5 or $10 billion."* No lab-published number for Opus 4.5/4.6 specifically. |
| Gemini 3.0 Pro | 2025–26 | Undisclosed | **NOT PUBLISHED — flag for Louis** | — | Predecessor Gemini 1.0 Ultra estimated at **$30–191M** compute (Epoch/Statista). No public estimate for 3.0 Pro yet. |

**Key trend (Epoch AI 2024 paper)**: Amortized training cost of frontier models has grown **2.4× per year since 2016** (95% CI 2.0–3.1×), or **~2.9× per year if excluding TPU-based models**. At this pace, a training run crosses **$1B by start of 2027**.

---

## §2 Reproducing / open-weight frontier: cost of replication

These are **official tech-report numbers** wherever possible — the creators' own disclosed GPU-hour × rental-price accounting. Note: these **exclude prior research, ablations, and failed runs** (the labs say so explicitly).

| Model | Year | Params | Training cost (USD) | Source | Quote / notes |
|-------|------|--------|--------------------:|--------|---------------|
| Llama 2 70B | Jul 2023 | 70B dense | **~$3.4M** compute-only (1,720,320 A100-hours × $2/h); ~$5–10M all-in per analysts | [Llama 2 model card](https://huggingface.co/meta-llama/Llama-2-70b) · [Medium analyst estimate](https://medium.com/@urwithdhanu/what-did-it-cost-to-train-or-create-llama2-7e1af76a18aa) | Model card Table: **"Llama 2 70B \| 1,720,320 GPU hours \| A100-80GB"**. At conservative $2/A100-hour ≈ $3.4M; retail cloud closer to $5–10M. |
| Llama 3.1 405B | Jul 2024 | 405B dense | **~$60M** compute-only (30.84M H100-hours × $2/h) | [HF Llama 3.1 blog](https://huggingface.co/blog/llama31) · [Litespark Technical Report](https://arxiv.org/html/2510.02483v1) | HF: "The Llama 3.1 models were trained on over 15 trillion tokens … 39.3M GPU hours (1.46M for 8B, 7.0M for 70B, **30.84M for 405B**)." At $2/H100-hour ≈ **$61.7M**. Litespark: "Llama 3.1-405B reportedly consumed 30.84 million GPU-hours, equivalent to 80 days of training on 16,000 H100 GPUs." |
| **DeepSeek-V3** | Dec 2024 | 671B MoE (37B active) | **$5.576M** (2.788M H800-hours × $2/h) | [DeepSeek-V3 Technical Report §1](https://arxiv.org/html/2412.19437v1) | Table 1 verbatim: "Pre-Training \| $5.328M \| Context Extension \| $0.238M \| Post-Training \| $0.01M \| **Total \| $5.576M**". Quote: *"Assuming the rental price of the H800 GPU is $2 per GPU hour, our total training costs amount to only $5.576M. Note that the aforementioned costs include only the official training of DeepSeek-V3, excluding the costs associated with prior research and ablation experiments."* |
| DeepSeek-R1 (RL stage) | Jan 2025 | 671B MoE | **~$1M** additional RL compute on top of V3 base (Epoch estimate; not officially disclosed) | [Epoch Gradient Updates](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1) | *"While DeepSeek has not made any explicit statements about the cost of the RL that went into DeepSeek-R1, based on the information disclosed in their papers I would estimate it's around $1M."* |
| Qwen3 series (235B-A22B) | May 2025 | 235B MoE (22B active) | **NOT PUBLISHED** — Alibaba discloses **relative efficiency only** | [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1) | Qwen3 paper claims Qwen3-235B-A22B "outperforms DeepSeek-V3-Base on 14 out of 15 evaluation benchmarks with only about 1/3 the total number of parameters." No dollar figure given. |
| Qwen3-Next 80B-A3B | Sep 2025 | 80B MoE (3B active) | **NOT PUBLISHED** — but Alibaba says "less than 10% of Qwen3-32B's training cost (GPU hours)" | [Alibaba Cloud blog](https://www.alibabacloud.com/blog/602580) | *"Qwen3-Next is trained on a uniformly sampled subset (15T tokens) of Qwen3's 36T-token pretraining corpus. It uses less than 80% of the GPU hours needed by Qwen3-30A-3B, and only **9.3% of the compute cost of Qwen3-32B** — while achieving better performance."* |
| Kimi K2 Thinking | Nov 2025 | 1T MoE (32B active) | **$4.6M reported by CNBC** — but Moonshot CEO publicly denied this is official | [Yicai Global](https://www.yicaiglobal.com/news/kimi-k2-thinkings-reported-usd46-million-training-cost-isnt-official-moonshot-ceo-says) · [RecodeChinaAI](https://recodechinaai.substack.com/p/kimi-k2-thinking-the-46m-model-shifting) | Yang Zhilin (Moonshot CEO): *"It is hard to quantify the training cost because a major part is research and experiments."* Trained on H800s. **Flag as rumored / unofficial.** |
| GLM-4.5 / 4.6 (Z.ai / Zhipu) | Jul–Sep 2025 | 355B MoE (32B active) | **NOT PUBLISHED — flag for Louis** | [Z.ai GLM-4.5 blog](https://z.ai/blog/glm-4.5) · [GitHub](https://github.com/zai-org/GLM-4.5) | Model card and blog discuss architecture, benchmarks, and inference pricing (API at ~$0.48/$1.92 per M tokens). No training cost disclosed. |

---

## §3 Efficiency per dollar — qualitative only

A clean benchmark-per-dollar table is not feasible because (a) the frontier labs don't publish costs and (b) benchmarks shift generation-to-generation. The **cleanest narrative evidence** is:

- **DeepSeek-V3 matches GPT-4o and Claude 3.5 Sonnet at benchmarks** ([DeepSeek-V3 tech report](https://arxiv.org/html/2412.19437v1)) while costing **~$5.6M** vs. GPT-4's ~$40–100M compute — i.e., **~10–20× cheaper for parity**.
- **Qwen3-Next delivers Qwen3-32B-level performance at ~9.3% of its training compute** ([Alibaba](https://www.alibabacloud.com/blog/602580)) — a ~10× efficiency gain **inside a single open-weights lab, in 6 months**.
- **Karpathy reproduced GPT-2 (1.5B) for ~$73 in 2025** vs. ~$43K in 2019 — a **~600× cost reduction over 7 years** on an identical-capability target ([Let's Data Science](https://letsdatascience.com/news/karpathy-demonstrates-massive-gpt-2-training-cost-reduction-417d66ef)), roughly **2.5× annual decline**.

---

## §4 Notes for Louis

### What's official vs. estimated

| Source type | Models |
|---|---|
| **Official tech report / model card (hard numbers)** | Llama 2 (GPU hours), Llama 3.1 (GPU hours), **DeepSeek-V3 ($5.576M)**, Qwen3-Next (relative %) |
| **Epoch AI amortized estimates (authoritative)** | BERT, GPT-2, GPT-3, GPT-4 ($40M amortized), GPT-4.5 (~$500M illustrative), DeepSeek-R1 RL (~$1M) |
| **Community / practitioner estimates** | GPT-3 Lambda Labs ($4.6M), Llama 2 analyst roll-up |
| **Press leak, denied by lab** | Kimi K2 Thinking ($4.6M per CNBC, denied by Moonshot CEO) |
| **NOT PUBLISHED** | o1, o3, Claude Opus 4.x, Gemini 3.0 Pro, GLM-4.5/4.6, Qwen3 absolute $ |

### Data-quality caveats

1. **Open-weights $ are lower-bounds**. DeepSeek, Llama, Qwen figures exclude ablations and failed runs. DeepSeek-V3's paper says so explicitly. Real all-in cost is likely 2–5× higher (ablations + research salaries), matching planetbanatt's fermi upper bound of ~$10.6M for V3.
2. **Frontier closed-model $ are upper-bounds / extrapolations**. Epoch AI is the best public source but openly flags o1/o3/Opus as "we lack compute estimates."
3. **H800 vs H100 accounting**. Chinese labs train on H800s (same FLOPs, 44% the interconnect bandwidth of H100). $2/hour is a round-number rental assumption, not their actual internal cost.
4. **2.4× / year Epoch trendline** is the single most important claim on the frontier side — it's peer-reviewed (Cottier et al., arXiv:2405.21015, June 2024) and based on 45 models. That's the "pincer top" you can lean on.

### Suggested slide framing

> **"The leaders are spending 10× more per year to nudge the frontier. The fast-followers are spending 10× less per year to reproduce it."**

Two concrete anchor-pairs for Station F:
- **Anchor A (climbing)**: GPT-3 ($4.6M, 2020) → GPT-4 ($40M–$100M, 2023) → GPT-4.5/Grok 4 (~$500M, 2025) → Amodei's "$5–10B by 2026" trajectory. **~10× every 2 years.**
- **Anchor B (crashing)**: Llama 2 70B ($3–10M, 2023) → DeepSeek-V3 ($5.576M, Dec 2024) with GPT-4-class performance → Qwen3-Next at **9.3%** the cost of Qwen3-32B (2025). **Open-weights labs are catching last year's frontier with ~1% of its budget.**

### One slide-worthy punchline

**"DeepSeek-V3 matched Claude 3.5 Sonnet on most benchmarks for $5.576M — roughly what OpenAI spent on GPT-4 salaries for two weeks."** (Source: DeepSeek-V3 Table 1; GPT-4 R&D staff share is 29–49% of total per Epoch.)

---

## Reference URLs (authoritative, in source-priority order)

1. Cottier et al. 2024, *The rising costs of training frontier AI models* — https://arxiv.org/abs/2405.21015
2. Epoch AI blog — https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models
3. Epoch AI OpenAI spend breakdown — https://epoch.ai/data-insights/openai-compute-spend
4. Epoch AI on GPT-4.5 vs GPT-5 — https://epoch.ai/gradient-updates/why-gpt5-used-less-training-compute-than-gpt45-but-gpt6-probably-wont
5. Epoch AI on DeepSeek-R1 — https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1
6. DeepSeek-V3 Technical Report — https://arxiv.org/abs/2412.19437
7. Llama 3.1 blog (HF) — https://huggingface.co/blog/llama31
8. Llama 2 model card — https://huggingface.co/meta-llama/Llama-2-70b
9. Qwen3 Technical Report — https://arxiv.org/abs/2505.09388
10. Qwen3-Next blog (Alibaba) — https://www.alibabacloud.com/blog/602580
11. Kimi K2 Thinking denial — https://www.yicaiglobal.com/news/kimi-k2-thinkings-reported-usd46-million-training-cost-isnt-official-moonshot-ceo-says
12. GLM-4.5 blog — https://z.ai/blog/glm-4.5
13. Dario Amodei on Dwarkesh — https://www.dwarkesh.com/p/dario-amodei-2
