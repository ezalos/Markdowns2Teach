# How long does frontier capability take to become runnable on hardware a startup owns?

**Research run:** `local-lag` · **Written:** 2026-09-01 · **For:** S10, Station F founders' talk (2026-09-02)
**Verdict up front:** the r/LocalLLaMA ~24.8-month claim should be **dropped**. It is unverifiable, and every
independent measurement of the 2025–2026 regime puts the lag between **3 and 12 months** — a factor of 2 to 8 lower.

---

## 1. The two lags, separated

The community chart conflated two different questions. They have different answers and different sources.

### Lag A — open weights catching frontier closed models (any size)

> **Four months.**

Epoch AI, measuring day-by-day over **1 January 2026 – 28 May 2026** on the Epoch Capabilities Index: "the most
capable open-weight models have lagged frontier closed models by an average of four months" [1], over an analysis
window of "January 1, 2026, through May 28, 2026" [2]. The vertical gap is "an average ECI gap of 8 points, with a
90% confidence interval of 7 to 11 units" [3] — Epoch notes this is comparable to one minor version step at a
frontier lab.

Three things a founder should know about that number before repeating it:

- **It is a lower bound on the lab-quality gap.** Epoch's own limitations section says "Two factors mean that our
  estimate may tend to understate the true gap between open and closed models" [4] — open models underperform on
  private benchmarks relative to public ones, and closed labs do not always ship their best model.
- **The criterion is generous.** Catch-up is scored when the open model beats the closed one in at least 5% of
  bootstrap samples. Under a strict point-estimate criterion: "We find an average time gap of four months. This
  estimate would grow to six months" [5].
- **It grew.** "This gap between open and closed models is slightly larger than the one we identified in our October
  2025 Data Insight" [6], which found three months over January 2023 – October 2025. The direction of travel in
  2026 is *wider*, not narrower.

**Currency check:** this Data Insight is dated 29 May 2026 and is still the most recent open-vs-closed gap analysis
Epoch has published as of 1 September 2026 (its Open-Weight Models topic index lists nothing newer). So the four-month
figure is roughly three months stale, but it has not been superseded.

### Lag B — that capability fitting on hardware a small team owns

> **6 to 12 months, for a single consumer GPU.**

Yes, someone measures this systematically, and it is Epoch AI again. Their consumer-hardware Data Insight finds that
"anyone can locally run models matching the absolute frontier of LLM performance from just 6 to 12 months ago" [7],
and states the general result as: models runnable on a "consumer GPU typically match the capabilities of frontier
models after an average lag between 6-12 months" [8]. They cross-check it against the size-agnostic figure: "This lag
is consistent with our previous estimate of a 5 to 22 month gap for open-weight models of any size" [9]. Their method
fixes a hardware envelope per GPU generation (a ~40B-parameter ceiling for the RTX 5090 era) and tracks the best open
model inside it across GPQA-Diamond, MMLU-Pro, the Artificial Analysis Intelligence Index and LMArena Elo.

**Two honest caveats.** First, Epoch flags that "small open models are more likely to be optimized for specific
benchmarks" [10], so real-world lag is probably longer than the benchmark lag. Second — and this matters for a
September 2026 talk — **this is an August 2025 insight whose dataset was last updated in November 2025**. It is the
only systematic Lag B measurement I found, and it is a year old. Section 2 is my September 2026 spot-check of whether
it still holds.

---

## 2. Three verified model-and-hardware pairs (September 2026)

Each row pairs an open-weight model with the closed frontier model it matches on the **Artificial Analysis
Intelligence Index v4.1.1** — an independent evaluator that runs all nine of its component evaluations itself
("Artificial Analysis Intelligence Index v4.1.1 incorporates 9 evaluations" [11], including Terminal-Bench v2.1,
τ³-Banking, GDPval-AA v2 and SciCode). Both endpoints of every pair are scored by the same evaluator on the same
index, which is what makes the date difference meaningful. Release months are stated on the same Artificial Analysis
model pages the scores are cited from.

| Hardware you own | Open-weight model | AA Index | Closed model it matches | AA Index | **Lag** |
|---|---|---|---|---|---|
| Single 24–32 GB consumer GPU (RTX 4090/5090 class) | **Qwen3.8 27B (xhigh)**, Aug 2026 — top model in AA's 4B–40B open class [13][14] | **52** [12] | **GPT-5.4 (xhigh)**, Mar 2026 | **53** [15] | **~5 months** |
| Single H100 80 GB, or a 128 GB unified-memory workstation | **Ling 3.0 Flash**, Aug 2026 — 124B total / 5.1B active [17], top model in AA's 40B–150B open class [18] | **38** [16] | **Gemini 3 Pro Preview (high)**, Nov 2025 | **41** [19] | **~9 months** |
| 256–512 GB unified-memory workstation (M5 Ultra Mac Studio class) or 4× 96 GB cards | **GLM-5.3-Flash**, Aug 2026 — 320B total / 18B active [21] | **57** [20] | **Claude Opus 4.8 (max)**, May 2026 | **57** [22] | **~3 months** |

**Memory arithmetic (why the tiers are what they are).** At 4-bit weights a model needs roughly half a byte per
parameter plus KV cache: 27B → ~15 GB (fits a 24 GB card); 124B → ~62 GB (fits one H100 80 GB); 320B → ~160 GB (needs
a 256 GB+ unified-memory box). Note that all three AA scores are measured on **hosted, unquantised** endpoints — the
quantisation you need to fit the model on your own box is a separate tax, priced in §3.

**What the table actually says, and it is the most useful thing on this slide:**

1. **The lag is not one number — it is a function of how much memory you own.** 3 months at the top tier, 9 months in
   the middle. Epoch's 6–12 months holds up as an *average across tiers*, but a founder buying hardware is not buying
   the average.
2. **The middle is the worst deal.** The 40B–150B band — exactly the band a single H100 or a 128 GB workstation buys
   you — lags nearly three times worse than the 4B–40B band. Open labs in 2026 shipped either small dense models or
   very large sparse MoE, and hollowed out the middle.
3. **The cheapest tier is one of the best.** A ~$2,000 consumer GPU running a 27B model is five months behind the
   closed frontier. That is the number that should be on the slide, not 24.8 months.
4. **Ceiling check:** the outright best open-weight models are far above all three rows — "Kimi K3 (max) and GLM-5.3
   (max) are the highest intelligence open source models" [23] — but at 2.8T and 753B parameters those are a
   multi-node purchase, not workstation hardware. They set Lag A, not Lag B.

---

## 3. The quantisation tax, on agentic work specifically

This is where "it runs locally" usually breaks, and the best current evidence is a July 2026 preprint that ran the
experiment properly: **"Flat Score, Amplified Failures: How the Error Budget Masks Damage in Quantized LLM Agents"**
(arXiv:2607.27275, 29 July 2026). Ten model×domain cells on τ²-bench, **456 episodes per arm**, at 16-, 8- and 4-bit
weights, AWQ-quantised, served on vLLM.

**Headline: on the standard metric, 4-bit looks free — and that is the problem.**

- The paper opens by naming the claim it tests: "Post-training quantization to 4-bit weights is widely reported to be
  nearly lossless." [24]
- On task score it replicates: "No cell shows a score change that survives multiple-comparison correction" [25].
- But underneath, in the Gemma-4-31B telecom cell, the share of tool calls invoking a tool outside the agent's tool
  list **doubles from 19.5% to 38.3%** — a 2.5× increase in hallucinated tool calls, +17.6 points per task.
- The damage is amplification, not novelty: "The failure set is the same at every precision" [26] — 0.18% of the
  4-bit agent's hallucinated calls name a tool the 16-bit original never used.
- The score stays flat only because the benchmark tolerates ten failed calls per episode. Shrink the budget to two
  errors and a **17-point score gap reappears**. The authors' own conclusion: "The agreement is an artifact of what
  the score can see." [27]

**The two numbers a founder needs:**

- **8-bit is close to free.** "Sweeping the intermediate precision shows that 8 bits, weight-only" [28] produced no
  significant score change and no channel movement in the telecom domain; the entire jump happened between 8 and 4
  bits. If you have the memory, spend it on precision.
- **4-bit is only free if your deployment forgives retries.** "The masking depends on a forgiving environment." [29]
  Their explicit warning is that many real deployments are not: single-shot interactions, strict error limits,
  irreversible actions, no silent retries. On a benchmark the agentic loop repairs the extra errors before they reach
  the score. In production — an agent that writes to your database, sends an email, files a ticket — it does not.

Practical read for S10: quote the **19.5% → 38.3%** tool-hallucination doubling, not a perplexity delta. It is the
number that survives contact with a real agent.

---

## 4. Is the gap closing or widening in 2026?

**The aggregate gap is widening slightly; the agentic picture is split, and the split is informative.**

**Aggregate: widening.** Epoch's own comparison is the cleanest evidence — three months over Jan 2023 – Oct 2025,
four months over Jan – May 2026 [6]. Small, but the wrong direction.

**Agentic tool use: closed, or near enough.** Open-weight models now lead or sit inside the top three on most of the
agentic benchmarks Artificial Analysis runs:

| Benchmark | Leader (all independently run by AA) | Where open weights sit |
|---|---|---|
| τ³-Banking (Sierra Research) | **Qwen3.8 Max — an open-weight model — leads** [30][31] | **1st** |
| APEX-Agents-AA (long-horizon agentic) | Gemini 3.5 Flash (high), 47.1% [32] | 2nd (Kimi K3) |
| AutomationBench-AA | Gemini 3.7 Flash (high), 62.7% [33] | 2nd (Kimi K3) |
| ITBench-AA (SRE incident RCA) | GPT-5.6 Sol (max), 56.2% [34] | 3rd (Kimi K3) |
| GDPval-AA v2 (real economic tasks) | Claude Opus 5 (max), Elo 1824 [35] | 3rd (GLM-5.3-Flash) |
| Terminal-Bench v2.1 (89 coding/sysadmin tasks [37]) | GPT-5.6 Sol (xhigh), 89.5% [36] | outside top 3 |
| **AA-AnalystAgent pass^5** — must be right **5 times out of 5** [39] | Gemini 3.7 Flash (high), 60.0% [38] | **outside top 3** |
| **AA-Omniscience** (hallucination-penalised) | Claude Fable 5, score 43 [40] | **outside top 3** |

**The pattern is not "agentic vs. not". It is "does the metric punish unreliability?"** On single-attempt agentic
benchmarks open weights are level. On the two benchmarks that penalise being wrong — pass^5, where a model that
solves a question once but not five times out of five scores near zero, and AA-Omniscience, where hallucination costs
you points — open weights fall out of the top three entirely, and the top of AA-Omniscience is swept by one lab.

That is the same failure mode §3 found under quantisation, arriving from a different direction: **the open/local
stack's real deficit in 2026 is consistency across repeated attempts, not peak capability.** For a founder, that maps
directly onto the build-versus-wait call: local is fine for a workflow where a human reviews the output, and risky
for an unattended long-horizon agent.

**Structural view on where this goes.** Epoch's April 2026 analysis of whether compute-poor labs can close the gap
through algorithms, spillover or distillation lands on: "I think compute-poor labs probably" cannot fully make up the
disadvantage, because "compute disadvantage to compete at the frontier. The compute gap is just too large" [41]. His
estimate is that distillation narrows the gap several-fold but not ten-fold. Expect the lag to stay in the
single-digit-months band rather than collapse to zero.

---

## 5. The honest cost comparison

The best published total-cost work is **"Beyond Per-Token Pricing: A Concurrency-Aware Methodology for LLM
Infrastructure Cost Estimation"** (arXiv:2606.11690, June 2026) — 42 benchmark runs on H100, replicated on A100,
with an open-source cost meter.

**Its finding demolishes the usual startup spreadsheet.** Every public LLM cost calculator treats GPU utilisation as
a fixed input. Measure it instead and: "on identical H100 hardware, effective cost spans $0.21 to $15.25 per million
output tokens" [42] — a 70× spread on the same silicon, driven only by how many requests per second you are actually
serving.

**The concrete number for a small team.** A small team's traffic is low-rate and bursty. That is the expensive end:

- "At 1 request/second on an H100, a Mixtral 8x7B FP16 deployment costs $15.25 per million tokens" [43] — at that
  operating point, self-hosting is *more expensive than a frontier API's list output price*.
- Under naive math you would never see this: "Under the naive model, all configurations appear permanently cheaper
  than API alternatives" [44].
- The error is systematic and biased against exactly the reader of this slide: utilisation-naive estimates are "most
  severely over-selling it for low-traffic workloads" [45]. Even where self-hosting still wins, "most of the expected
  advantage evaporates" [46].

**The break-even shape — the sentence to put on the slide:**

> "The crossover is not a point; it is a threshold that moves with traffic and with the reference tier." [47]

Where the threshold sits depends on model and GPU pricing. For the paper's smaller single-GPU configurations, "For
Llama and Qwen models, the lower single-GPU cost means the crossover is below 1 rps" [48] — self-hosting wins even at
minimal traffic, but only under co-tenant GPU pricing; on a dedicated node the whole cost curve doubles. For the
larger Mixtral configuration the crossover sits near 1.5–2 rps.

**Translated for a founder:** sustained load of roughly **1–2 requests per second, 24/7** is the shape of the
break-even. Below that, the GPU idles and you are paying for air. Owning hardware for bursty prototype traffic is
almost always the more expensive choice — and that is before you price the engineer who keeps vLLM running.

---

## 6. EU sovereign options, September 2026

**The material change since June 2026 is speed of availability.** On 26 June 2026 [50] Scaleway put **GLM-5.2** — a
near-frontier open-weight model — on its Generative APIs: "Announced by Z.ai on June 16th and available today on
Scaleway" [49], a **ten-day** gap between global open-weight release and EU-sovereign availability, and "With this
release, Scaleway becomes the first sovereign cloud provider in Europe to offer the model" [51]. The sovereignty
terms are explicit: "all inference runs entirely on Scaleway" [52] sovereign infrastructure located in Europe, with
no third-party routing or telemetry to the model provider.

**Who serves frontier-class open weights from EU infrastructure:**

- **Scaleway (FR)** — Generative APIs, serverless and dedicated-deployment tiers, catalogue page last reviewed
  14 August 2026 [53]. Its most capable text model is GLM-5.2 [49][51]; the same catalogue carries the Qwen3.5/3.6,
  DeepSeek, Gemma-4, Mistral and gpt-oss families (page contents, not separately cited).
- **OVHcloud (FR)** — AI Endpoints. "More than 40 models A constantly updated range of popular, open-weight models."
  [54], with "Zero data retention: We keep only the data required for billing purposes." [55]. Models are served
  quantised (fp8 on the larger entries) — which, per §3, is the precision the quantisation paper found close to free.
- **Mistral AI (FR)** — the only frontier-class vendor that also publishes open weights you can run yourself;
  Mistral-large-3-675b and Mistral-medium-3.5-128b are in Scaleway's EU catalogue.

**The third lag, which nobody names.** The model Scaleway added in this window is GLM-5.2 [49][51], released by Z.ai
on 16 June 2026 [49], while by the time its catalogue page was last reviewed on 14 August 2026 [53] the open-weight
frontier had already moved on to GLM-5.3 and Kimi K3 [23]. So there is a
**Lag C of roughly 1–2 months** between an open-weight model existing and it being servable from EU-sovereign
infrastructure — small, shrinking, and worth stating honestly rather than implying EU parity is instant.

**Regulatory change in the same window.** The EU AI Act's teeth arrived on 2 August 2026: "supervision and
enforcement powers against GPAI model providers will only come into force on 2 August 2026" [56], with fines up to
"3 % of their annual total worldwide turnover in the preceding financial year or EUR 15 000 000, whichever is
higher" [57]. This binds *model providers*, not startups deploying models — but it is why EU-hosted open-weight
serving got commercially serious in this window.

---

## 7. Verdict on the r/LocalLLaMA ~24.8-month claim

**Drop it. Do not try to replace it in place — the framing is wrong, not just the number.**

1. **It cannot be cited.** The permalink is unrecoverable, so it fails the deck's clickable-live-source rule outright.
   No amount of rewording fixes an unlinkable source.
2. **It measures a regime that ended.** The chart's sample is four pre-2025 generations. Every independent
   measurement of 2025–2026 disagrees by a factor of 2–8: Epoch says four months for open-weight-of-any-size [1],
   6–12 months for consumer-GPU-runnable [7], and even the older size-agnostic band was "5 to 22 month" [9] — with
   24.8 sitting above the top of that range.
3. **It conflates the two lags,** which is the substantive error. Lag A and Lag B are different numbers with
   different sources and, as §2 shows, Lag B is not even one number — it varies from 3 to 9 months across three
   hardware tiers a startup might plausibly buy.

**What to put on S10 instead — two numbers and one caveat:**

> **Open weights trail the closed frontier by ~4 months. Getting that capability onto hardware you own costs
> another few months — 3 on a $10k workstation, 5 on a $2k gaming GPU, 9 in the awkward middle.**
> *Caveat:* what you lose locally is consistency, not peak capability — 4-bit quantisation doubles an agent's
> tool-hallucination rate (19.5% → 38.3%) while leaving the benchmark score flat, and open weights fall out of the
> top three exactly on the benchmarks that demand the same answer five times running.

That is a build-versus-wait slide a founder can act on: **wait if you need frontier reliability, build if you need
frontier capability under human review — and check your utilisation before you buy a GPU, because below ~1–2
requests per second the API is cheaper anyway.**

---

## Gaps and limitations of this run

- **No systematic Lag B measurement newer than November 2025 exists.** Epoch's consumer-hardware insight [7][8] is
  the only one, and its dataset ends before the 2026 model generation. The three pairs in §2 are my own September
  2026 spot-check built from Artificial Analysis's published index scores; they are arithmetic on two cited,
  independently-measured endpoints each, not a replication of Epoch's full methodology.
- **The pairs are matched on a composite index**, so they claim "comparable overall capability", not "equivalent on
  your task". A founder should re-check the pair on the specific benchmark they care about.
- **All three open models' index scores were measured on hosted, unquantised endpoints.** Nobody publishes a
  systematic index score for the same models at 4-bit on consumer hardware. §3 quantifies the direction and rough
  size of that tax on agentic work but cannot give a per-model index delta. This is the single biggest hole in any
  "runs locally" claim, including this report's.
- **The quantisation evidence is one preprint** (10 cells, 2 model families, 2 domains), not a literature. Its
  central finding — damage is real but masked by benchmark error budgets — is well-designed and internally
  replicated, but has not been independently reproduced.
- **EU provider claims rest on vendor documentation.** There is no independent auditor of EU-sovereign inference
  claims; [51][52][54][55] are Scaleway's and OVHcloud's own statements about their own services, used only to state
  what the services are, never for comparative claims.
