# Sorbonne Decks — English Extraction for Station F

Temporary working file. Slides extracted and translated to English for a founder-oriented (ex-42) audience. English technical terms kept as-is per project convention.

---

## A-llms slide 01 — Benchmarks: real progress, visible ceilings

**Original title (FR)**: Benchmarks : progrès réels, plafonds visibles
**English title**: Benchmarks: real progress, visible ceilings
**Slide class** (if any): img-right (implied — uses `![bg right:55%]`)
**Image references**: `![bg right:55% contain](assets/epoch_ai_llm_saturation_benchmarks.jpeg)`

### Body (English)

- MMLU (general knowledge): **saturated at 90%+** — LLMs are catching up with human experts [1]
- Newer, harder benchmarks: Humanity's Last Exam **8.8%**, FrontierMath **2%** [2]
- Efficiency: from **540B** down to **3.8B** params for 60% on MMLU — a **142x** reduction [1]

> Easy benchmarks saturate, but hard problems remain out of reach.

### Citations (verbatim from original)

<small>Sources : [1] [Epoch AI](https://epoch.ai/trends) · [2] [Stanford HAI AI Index 2025](https://aiindex.stanford.edu/report/)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- LLM progress is real on knowledge benchmarks but plateaus on hard reasoning tasks.
- Efficiency gains are dramatic: smaller models today match the performance of much larger ones from a few years ago.

---

## A-llms slide 02 — What LLMs enable

**Original title (FR)**: Ce que les LLMs permettent
**English title**: What LLMs enable
**Slide class** (if any): img-right compact-table
**Image references**: `![bg right:55% contain](assets/ng01/img-026.png)`

### Body (English)

| Category | Examples | Type |
|---|---|---|
| *Writing* | Brainstorming, press releases, translation | Web + App |
| *Reading* | Email classification, summarization, sentiment | Mostly App |
| *Chatting* | Customer support bot, coaching, internal FAQ | Web + App |
| *Coding* | Copilot, Cursor, Claude Code — 76% of devs use AI [1] | Web + App |

*Two modes*:
- *Web-based*: ChatGPT, Claude, Le Chat — direct interaction
- *Software app*: LLM embedded in a product (email routing, analysis)

### Citations (verbatim from original)

<small>Sources : [1] [Stack Overflow 2024](https://survey.stackoverflow.co/2024/ai)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- LLM use cases cluster into four buckets: Writing, Reading, Chatting, Coding.
- Each can be delivered either through a web interface or embedded inside a software app.

---

## A-llms slide 13 — Training cost: from thousands to billions

**Original title (FR)**: Le coût d'entraînement : de milliers à milliards
**English title**: Training cost: from thousands to billions
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

| Model | Year | Params | Cost (compute only) |
|-------|------|--------|---------------------|
| BERT | 2018 | 340M | ~$3,300 |
| GPT-3 | 2020 | 175B | ~$4.6M |
| Llama 2 | 2023 | 70B | ~$3M |
| GPT-4 | 2023 | ~1.8T MoE | **$78M** [1] |
| Llama 3.1 405B | 2024 | 405B | $60–170M |
| DeepSeek-V3 🇨🇳 | 2024 | 671B MoE | **$5.6M** [2] |

- Frontier costs: **2.4x growth per year** since 2016, projection **>$1B** by 2027 [3]
- DeepSeek-V3 ≈ GPT-4o for **14x cheaper** (H800 at $2/h) [2]

### Citations (verbatim from original)

<small>Sources : [1] [Epoch AI](https://arxiv.org/abs/2405.21015) · [2] [DeepSeek-V3](https://arxiv.org/abs/2412.19437) · [3] [Epoch AI](https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Frontier training costs have grown several orders of magnitude in six years — only hyperscalers can afford them.
- DeepSeek-V3 is a notable outlier: GPT-4o-class performance at ~14x lower cost.

---

## A-llms slide 14 — Where does the money go? Anatomy of a training cost

**Original title (FR)**: Où passe l'argent ? Anatomie du coût d'entraînement
**English title**: Where does the money go? Anatomy of a training cost
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/epoch/epoch-training-cost-figure-cost-breakdown.png)`

### Body (English)

Development cost breakdown (GPT-4 / Gemini Ultra) [1]:

- **Hardware**: 47–67% — GPUs (H100, TPU) are the dominant line item
- **R&D staff**: 29–49% — researchers, ML engineers
- **Energy**: only **2–6%** — Gemini Ultra: ~35 MW [1]

> The bottleneck isn't electricity — it's silicon and talent. Only the best-capitalized players can play at the frontier.

### Citations (verbatim from original)

<small>Sources : [1] [Epoch AI](https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Frontier training budgets are dominated by GPU hardware and ML talent, not energy.
- The frontier is capital- and talent-gated — the moat is money and researchers, not electricity.

---

## A-llms slide 15 — Efficiency is exploding: reproducing GPT-2 for ~$60

**Original title (FR)**: L'efficience explose : reproduire GPT-2 pour ~$60
**English title**: Efficiency is exploding: reproducing GPT-2 for ~$60
**Slide class** (if any): cols
**Image references**: (none)

### Body (English)

<div class="left">

**Reproducing costs less and less**:
- GPT-2: $50K → **~$60** (Karpathy, 2025) — 2h on 8×H100 [1]
- BERT: $3,300 → **$20** (MosaicBERT) [2]
- DeepSeek-R1 RL: **$294K** on V3 [3]

</div>
<div class="right">

**But the frontier keeps exploding**:
- Frontier cost: **×2 every 8 months** [4]
- MMLU 60%: 540B → **3.8B** params = 142× [5]
- Next generation: **$500M–1B+** expected

</div>

> Two opposing trends: leaders spend more, but reproducing their level gets cheaper every year.

### Citations (verbatim from original)

<small>Sources : [1] [Karpathy](https://x.com/kaboruka/status/1891680241001140367) · [2] [Databricks](https://www.databricks.com/blog/mosaicbert) · [3] [Nature/DeepSeek](https://www.nature.com/articles/s41586-025-09422-z) · [4][5] [Stanford HAI 2025](https://aiindex.stanford.edu/report/)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Reproducing yesterday's frontier is exponentially cheaper — great news for open-source and founders.
- Pushing the new frontier is exponentially more expensive — concentrated among a few players.

---

## A-llms slide 16 — Training data: a limited resource?

**Original title (FR)**: Les données d'entraînement : une ressource limitée ?
**English title**: Training data: a limited resource?
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/epoch/epoch-data-limits-03.png)`

### Body (English)

Stock of high-quality public text: **~300 trillion tokens** (90% CI: 100T–1,000T) [1]

- Training compute grows at **4–5x per year** [1]
- Estimated exhaustion (80% CI): **2026–2032**
  - Compute-optimal scenario: **2028**
  - With 5x overtraining: as early as **2027** [1]
- Multi-epoch training extends the stock by **2–5x** [1]

> "Five years and four orders of magnitude of compute separate GPT-2 from GPT-4" — the data wall is approaching.

### Citations (verbatim from original)

<small>Sources : [1] [Epoch AI](https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- The public internet text corpus will be exhausted for training within a few years at current growth rates.
- Multi-epoch training buys extra time but is not a long-term solution.

---

## A-llms slide 17 — Synthetic Data: the answer to the data wall

**Original title (FR)**: Synthetic Data : la réponse au mur des données
**English title**: Synthetic Data: the answer to the data wall
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

The Web lacks certain reasoning primitives — no amount of scaling closes that gap. **Synthetic Data** changes the paradigm [1]:

- **"Upward training"**: **3B–12B** models generate data used to train larger models [1]
- **Phi-1.5** (Microsoft): 1.3B params on 30B tokens → performance of models **10x** larger [1]
- **Seed-Prover**: **230M+** geometry problems generated in 7 days [1]
- Labs in 2025: Nemotron-3, DeepSeek-Prover-V2, Claude 4, Kimi 2.5 [1]

> We no longer just scrape the Web and hope — we **design** training data. "Organic data is fundamentally data engineering outsourcing."

### Citations (verbatim from original)

<small>Sources : [1] [VintageData](https://vintagedata.org/blog/posts/synthetic-pretraining)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Synthetic data lets small, cheap models bootstrap large frontier models past the data wall.
- The frontier is shifting from "data scraping" to "data engineering".

---

## A-llms slide 28 — The right model for the right task

**Original title (FR)**: Le bon modèle pour la bonne tâche
**English title**: The right model for the right task
**Slide class** (if any): cols
**Image references**: (none)

### Body (English)

<div class="left">

| Model | Input / 1M | Output / 1M |
|--------|-----------|-------------|
| Qwen3 30B MoE | $0.06 | $0.22 |
| GPT-4o mini | $0.15 | $0.60 |
| Claude Sonnet 4.5 | $3.00 | $15.00 |
| Claude Opus 4.6 | $15.00 | $75.00 |

</div>
<div class="right">

- **Support** → Mistral Small
- **Analysis** → o3 / Opus
- **Code** → Claude / Devstral

> **1,250x** gap between the cheapest and the most expensive.

</div>

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- Price-per-token spans three orders of magnitude across frontier APIs — choose per task, not per brand.
- Route cheap tasks to cheap models; save premium models for deep analysis or code.

---

## A-llms slide 29 — Exercise: estimate the cost of an AI product

**Original title (FR)**: Exercice : estimer le coût d'un produit IA
**English title**: Exercise: estimate the cost of an AI product
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

**Scenario**: a customer support chatbot, 1,000 conversations/day.

**Assumptions**:
- Average conversation: ~500 words input + ~300 words output
- ~500 words input → ~670 tokens (500 × 4/3) + ~400 tokens output

**With GPT-4o mini**:
- Input: 670K tokens/day × $0.15/1M = **$0.10/day**
- Output: 400K tokens/day × $0.60/1M = **$0.24/day**
- **Total: ~$0.34/day, i.e. ~$10/month**

> For 1,000 conversations per day, the AI cost is **$10/month**. Compare with the cost of a human agent (~$3,000/month).

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- A concrete unit-economics exercise: support chatbot at scale can cost ~$10/month in LLM tokens.
- The economics vs. human agents are stark — 300x cost difference for comparable volume.

---

## A-llms slide 30 — David beats Goliath: small models that surprise

**Original title (FR)**: David bat Goliath : les petits modèles qui surprennent
**English title**: David beats Goliath: the small models that surprise
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

| Model | Params | Performance | Compared to |
|--------|--------|-------------|-----------|
| **Mistral Small 3** 🇫🇷 | 24B | MMLU 81%, **3x faster** | Llama 3.3 70B (×3 larger) [1] |
| **Phi-4 Reasoning** | 14B | AIME 2024: **75.3%** | o1-mini 63.6% (much larger) [2] |
| **DeepSeek-R1 distilled** | 7B | AIME 2024: **55.5%** | QwQ-32B-Preview 50.0% (×4.5 larger) [3] |
| **DeepSeek-R1 distilled** | 14B | AIME 2024: **69.7%** | o1-mini 63.6% [3] |

> In 2025, *training methodology* and *data quality* matter more than raw model size. A well-trained 14B beats a 671B on specific tasks.

### Citations (verbatim from original)

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-small-3) · [2] [Microsoft Research](https://www.microsoft.com/en-us/research/articles/phi-reasoning-once-again-redefining-what-is-possible-with-small-and-efficient-ai/) · [3] [DeepSeek](https://arxiv.org/abs/2501.12948)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Small, well-trained models (14B–24B) outperform giants on targeted tasks — size isn't the whole story.
- Training recipe and data curation are the new moats, not parameter count.

---

## C-agents slide 01 — The analogy: Alfred, the AI assistant

**Original title (FR)**: L'analogie : Alfred, l'assistant IA
**English title**: The analogy: Alfred, the AI assistant
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/agent-alfred-narrative.png)`

### Body (English)

You tell Alfred: **"Organize a business dinner for Thursday."**

Alfred doesn't ask you anything back:
1. **Understands** the request and identifies sub-tasks
2. **Reasons and plans** the order of actions
3. **Uses tools** (email, calendar, reservation)
4. **Delivers the result** — confirmation sent

> An Agent = an LLM that can **reason**, **plan** and **interact with its environment** to reach a goal [1].

### Citations (verbatim from original)

<small>Sources : [1] [HuggingFace — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/what-are-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- An agent autonomously decomposes, plans, acts, and delivers — no step-by-step hand-holding.
- Intuitive framing: like a capable human assistant given a goal and a set of tools.

---

## C-agents slide 02 — The agency spectrum: 5 levels

**Original title (FR)**: Le spectre d'agence : 5 niveaux
**English title**: The agency spectrum: 5 levels
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/agency-spectrum-5-levels.png)`

### Body (English)

Not every AI system is an agent. **Agency** is a spectrum [1]:

- **☆☆☆** Simple processor — the output affects nothing
- **★☆☆** Router — the output determines the flow
- **★★☆** Tool Caller — the output triggers a function
- **★★★** Multi-step Agent — the output controls the iteration
- **★★★** Multi-Agent — one agent spawns other agents

> **Most business use cases sit at ★☆☆ and ★★☆.** Multi-step agents are the frontier of what works in production.

### Citations (verbatim from original)

<small>Sources : [1] [HuggingFace — smolagents](https://huggingface.co/docs/smolagents/)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Agency is a continuum, not a binary — most real products live at the lower levels.
- Multi-step autonomy is still the production frontier; don't jump straight there.

---

## C-agents slide 03 — The agent cycle: Think → Act → Observe

**Original title (FR)**: Le cycle agent : Think → Act → Observe
**English title**: The agent cycle: Think → Act → Observe
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/agent-cycle-hf.gif)`

### Body (English)

The fundamental loop of any agent [1][2]:

1. **Think** — the model reasons about the task
2. **Act** — it executes an action (search, API, computation)
3. **Observe** — it analyzes the result
4. **"Did I reach my goal?"** → if not, back to Think

**Example**:
- *Think*: "I need to find Mistral AI's revenue"
- *Act*: Web search → "Mistral AI revenue"
- *Observe*: "Mistral reached $300M ARR"
- *Think*: "I have the answer, I can synthesize"

### Citations (verbatim from original)

<small>Sources : [1] [HuggingFace — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) · [2] [ReAct — Princeton/Google](https://arxiv.org/abs/2210.03629)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Every agent is a loop: reason → act → observe → check goal → repeat.
- This is the ReAct pattern — the canonical building block behind all agent architectures.

---

## C-agents slide 04 — The Augmented LLM: the 3 extensions

**Original title (FR)**: Le LLM Augmenté : les 3 extensions
**English title**: The Augmented LLM: the 3 extensions
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/augmented-llm-3-extensions.png)`

### Body (English)

Every agentic system relies on an LLM **augmented** with 3 capabilities [1]:

- **Retrieval** — inject knowledge (RAG, covered in Deck B)
- **Tools** — act on the world (APIs, search, code)
- **Memory** — retain information across interactions

> Before you build an agent, you need a well-augmented LLM. The 3 extensions are the foundation. Retrieval = what you already mastered in Deck B.

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- An agent starts with an LLM augmented by Retrieval, Tools, and Memory.
- Get these foundations right before chasing complex orchestration patterns.

---

## C-agents slide 05 — Discussion: agent or not agent?

**Original title (FR)**: Discussion : agent ou pas agent ?
**English title**: Discussion: agent or not an agent?
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

> You receive **200 CVs** for a Data Analyst role. You want to shortlist the top 10 candidates.

**Questions for the class**:

- Where on the agency spectrum does this use case sit? (Router? Tool Caller? Multi-step?)
- Would a simple Prompt Chain be enough? At what point would you move to an agent?
- What is the **cost of a mistake** if the agent filters out a good candidate?
- How would you verify that the agent is doing a good job?

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- Forces the audience to place a real use case on the agency spectrum and weigh risk vs. automation.
- Primes the cost-of-error mindset — critical before giving an agent real-world impact.

---

## C-agents slide 17 — The golden rule: start simple

**Original title (FR)**: La règle d'or : commencer simple
**English title**: The golden rule: start simple
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/anthropic-complexity-ladder.png)`

### Body (English)

Anthropic "Building Effective Agents" [1]:

| Level | Pattern |
|---|---|
| 1 | Prompt Chaining |
| 2 | Routing |
| 3 | Parallelization |
| 4 | Orchestrator-Workers |
| 5 | Evaluator-Optimizer |
| 6 | Autonomous agent |

> "The most successful implementations weren't using complex frameworks." — Most business problems get solved at levels 1–3.

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- There's a 6-level complexity ladder; most real business problems stop at level 3.
- Complex frameworks are a trap — simpler composition wins in production.

---

## C-agents slide 18 — Prompt Chaining: the mastered sequence

**Original title (FR)**: Prompt Chaining : la séquence maîtrisée
**English title**: Prompt Chaining: the mastered sequence
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/anthropic/prompt-chaining.png)`

### Body (English)

Break a task into **sequential steps** — each LLM call consumes the output of the previous one [1].

**Business example** — Generating a marketing brief:
1. Analyze the product → 2. Identify the persona → 3. Draft the brief → 4. **Gate check** quality

**Gate checks**: between each step, a validation confirms the output before moving on.

> Prompt Chaining covers **the majority of business use cases** without the complexity of a full agent.

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Prompt chaining = linear pipeline of LLM calls with optional gate checks between stages.
- It handles most business workflows without needing full agency.

---

## C-agents slide 19 — Routing: direct to the right handler

**Original title (FR)**: Routing : diriger vers le bon handler
**English title**: Routing: direct to the right handler
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/anthropic/routing.png)`

### Body (English)

Classify the input, then **route to a specialized handler**. The LLM acts as a switch [1].

**Business example** — Customer support:
- Simple questions → lightweight LLM ($)
- Complex questions → premium LLM ($$)
- Complaints → human escalation

> Routing lets you optimize **cost and quality simultaneously** — easy cases cost less, hard cases get more attention.

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Routing tailors model choice (or human escalation) to the difficulty of each input.
- It jointly optimizes cost and quality — the simplest multi-model pattern that pays back.

---

## C-agents slide 20 — Parallelization: multiple LLMs at once

**Original title (FR)**: Parallélisation : plusieurs LLMs en simultané
**English title**: Parallelization: multiple LLMs at once
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/anthropic/parallelization.png)`

### Body (English)

Two complementary variants [1]:

**Sectioning** — independent sub-tasks in parallel:
- Analyze the legal, financial, and technical aspects of a contract *simultaneously*

**Voting** — same task, run multiple times:
- 3 LLMs do a code review, majority wins

> **When to use it**: when speed or reliability matter more than cost (2–3x) [1].

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Parallelization has two flavors: Sectioning (split the work) and Voting (run the same work multiple times).
- Use it when latency or reliability beats raw cost — you pay 2–3x more tokens.

---

## C-agents slide 21 — Orchestrator-Workers: the AI project manager

**Original title (FR)**: Orchestrator-Workers : le chef de projet IA
**English title**: Orchestrator-Workers: the AI project manager
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/anthropic/orchestrator-workers.png)`

### Body (English)

A central LLM **dynamically decomposes** the task, delegates to specialized workers, and synthesizes the result [1].

**Example** — "Analyze this market":
- The orchestrator decomposes: size, competitors, regulation, trends, risks
- Workers in parallel → coherent synthesis

**Key difference from Parallelization**: the sub-tasks are **not predefined** — the orchestrator decides them at runtime.

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Orchestrator-Workers = one LLM plans and splits the work, then fuses worker outputs.
- Unlike parallelization, the decomposition is dynamic and decided by the model at runtime.

---

## C-agents slide 22 — Evaluator-Optimizer: the improvement loop

**Original title (FR)**: Evaluator-Optimizer : la boucle d'amélioration
**English title**: Evaluator-Optimizer: the improvement loop
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/anthropic/evaluator-optimizer.png)`

### Body (English)

One LLM **generates**, another **evaluates** and gives feedback. Loop until the quality bar is met [1].

**Example** — Drafting a commercial proposal:
- The Generator drafts the proposal
- The Evaluator checks: tone, figures, conformity to the brief
- Feedback → correction → loop again

**Caveat**: every iteration costs money. Add a **circuit breaker** (max 3–5 rounds).

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Generator + Evaluator loop until quality threshold — mimics human editorial review.
- Always bound the loop with a circuit breaker; unbounded loops burn tokens fast.

---

## C-agents slide 23 — Discussion: which pattern for your project?

**Original title (FR)**: Discussion : quel pattern pour votre projet ?
**English title**: Discussion: which pattern for your project?
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

> You're launching an **automated competitive intelligence** service for SMBs. Customers send the name of a competitor and receive a weekly report.

**Questions for the class**:

- Which pattern(s) from the ladder would you use? Why?
- Where would you start? What would be your criterion for moving up a level?
- What circuit breaker would you put in place?

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- Forces the audience to map a realistic B2B product onto the complexity ladder.
- Surfaces the hardest question: when is added complexity worth the operational cost?

---

## C-agents slide 37 — Claude Code: the coding agent

**Original title (FR)**: Claude Code : l'agent qui code
**English title**: Claude Code: the coding agent
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/agent_stack-claude_code.jpeg)`

### Body (English)

A terminal-native agent that reads, writes, and executes code autonomously [1]:

- Reads/writes files, runs bash, manages git
- **CLAUDE.md** — persistent project instructions
- **MEMORY.md** — automatic memory across sessions
- **Skills** — reusable modular capabilities
- **Subagents** — parallelize sub-tasks

**The Knowledge Work Stack** [2]:
1. Model → 2. Harness (Claude Code) → 3. Personal Scaffolding (CLAUDE.md) → 4. MCPs/APIs → 5. Agents

### Citations (verbatim from original)

<small>Sources : [1] [Anthropic — Claude Code](https://www.anthropic.com/) · [2] [Taylor Pearson](https://x.com/TaylorPearsonMe/status/2029996204306866585)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- Claude Code is the canonical terminal-native coding agent, with persistent context and reusable skills.
- It embodies the full "Knowledge Work Stack": model, harness, scaffolding, integrations, subagents.

---

## C-agents slide 38 — OpenClaw: the viral autonomous agent

**Original title (FR)**: OpenClaw : l'agent autonome viral
**English title**: OpenClaw: the viral autonomous agent
**Slide class** (if any): compact
**Image references**: (none)

### Body (English)

**OpenClaw** = local, open-source AI agent that acts on your machine and your services [1][2]:

- **315K+ GitHub stars** in 4 months — the fastest-growing OSS project in history [1]
- Created by Peter Steinberger (founder of PSPDFKit), launched Nov. 2025

**Pulse Files** — the agent's identity memory:
- **SOUL.md** — personality, tone, values, communication preferences
- **IDENTITY.md** — user profile, habits, professional context
- Re-read every session → the agent **remembers who it is and who you are**

**The risks**: Cisco found that **26% of 31,000 Skills** contained vulnerabilities [3]. The MoltMatch incident: an agent created a dating profile without explicit consent [4].

### Citations (verbatim from original)

<small>Sources : [1] [GitHub — OpenClaw](https://github.com/openclaw/openclaw) · [2] [DigitalOcean](https://www.digitalocean.com/resources/articles/what-is-openclaw) · [3] [Cisco](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) · [4] [AFP/Taipei Times](https://www.taipeitimes.com/News/world/archives/2026/02/14/2003852326)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- OpenClaw shows how fast autonomous-agent adoption can explode once a viral open-source harness lands.
- Its identity-file model (SOUL.md / IDENTITY.md) and Skill ecosystem carry real, measurable security risks.

---

## C-agents slide 39 — Discussion: which agent product for your startup?

**Original title (FR)**: Discussion : quel produit agent pour votre startup ?
**English title**: Discussion: which agent product for your startup?
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

> You're launching an **automated legal analysis** startup. You need to decide how to integrate AI into your product.

**Questions for the class**:

- Would you start by prototyping with **Claude Code**, or go straight to a framework like LangGraph?
- What role would **Skills** play in your product? Which would you be willing to share, which would you keep proprietary?
- How would you manage MoltMatch-style security risks — an agent acting beyond what the customer asked for?

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- Pushes founders to choose: agile prototyping (Claude Code) vs. production framework (LangGraph).
- Forces consideration of proprietary-vs-shared Skills and agent-misuse risks from day one.

---

## C-agents slide 40 — Karpathy AutoResearch: autonomous research

**Original title (FR)**: Karpathy AutoResearch : la recherche autonome
**English title**: Karpathy AutoResearch: autonomous research
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/autoresearch-loop.png)`

### Body (English)

**AutoResearch** (Karpathy, March 2026) = an autonomous ML research loop [1]:

- **~630 lines** of Python, 1 GPU (H100), MIT license
- **~12 experiments/hour**, ~100 per night
- **First run**: 126 experiments in 10h [2]
- **Extended run**: ~700 modifications, **11% gain** on "Time to GPT-2" [3]

**"Programming the program"**: the human iterates on `program.md`, the agent iterates on the code [1].

> "You're not touching any of the Python files. You are programming the program.md files that provide context to the AI agents." — Karpathy [1]

### Citations (verbatim from original)

<small>Sources : [1] [Karpathy — AutoResearch](https://github.com/karpathy/autoresearch) · [2] [Discussion #43](https://github.com/karpathy/autoresearch/discussions/43) · [3] [Karpathy — X](https://x.com/karpathy/status/2031135152349524125)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- A ~630-line script can turn an H100 into an overnight ML researcher running 100+ experiments.
- The human's job shifts from writing code to writing the spec (`program.md`) that drives the agent.

---

## C-agents slide 41 — AutoResearch: the lessons

**Original title (FR)**: AutoResearch : les leçons
**English title**: AutoResearch: the lessons
**Slide class** (if any): none
**Image references**: (none)

### Body (English)

What this project teaches us about agents:

- **The agent isn't creative — it's systematic.** 126 experiments = no human would run them in one night. This is intelligent brute force.
- **"Programming the program"**: you describe constraints and goals in natural language. The agent explores the solution space.
- **The Evaluator-Optimizer pattern at scale**: exactly the pattern from slide 22, applied 100 times per night with a 5-minute circuit breaker.

**Applicable beyond ML**: automated A/B tests, marketing campaign optimization, document monitoring, prompt fine-tuning.

> Tobi Lutke (CEO Shopify) applied the pattern: 37 experiments in one night, **19% improvement**, a 0.8B model that beats his previous 1.6B model [1].

### Citations (verbatim from original)

<small>Sources : [1] [Tobi Lutke — X](https://x.com/tobi/status/2030771823151853938)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- The real power of agents is systematic scale — running hundreds of experiments humans never would.
- Evaluator-Optimizer + circuit breakers generalizes beyond ML: marketing, product, research.

---

## B-ecosysteme-ia slide 04 — Overview: the 9 layers of the AI stack

**Original title (FR)**: Vue d'ensemble : les 9 couches du stack IA
**English title**: Overview: the 9 layers of the AI stack
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/ai-stack-9_run_20260216_171301_8858a8.png)`

### Body (English)

**9 layers** structure the ecosystem:

- **0-1 Energy & Hardware** — NVIDIA, TSMC, ASML
- **2-3 Cloud & Data** — AWS, Azure, Scale AI
- **4-5 Models & Hubs** — OpenAI, Mistral, HF
- **6-7 APIs & Safety** — OpenRouter, Giskard
- **8 Applications** — Cursor, Perplexity

> Bottom = more **capital** and concentration. Top = more **differentiation**.

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- The AI industry decomposes into 9 layers, from energy at the bottom to applications at the top.
- Capital intensity decreases and differentiation increases as you move up the stack — where founders can actually compete.

---

## B-ecosysteme-ia slide 16 — (Layer 7) Safety & Compliance — billions in opportunity

**Original title (FR)**: (🔷7) Safety & Compliance — milliards d'opportunite
**English title**: (Layer 7) Safety & Compliance — billions in opportunity
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/safety-layer_run_20260322_230617_919b22.png)`

### Body (English)

The EU AI Act enters into force: **August 2, 2026**, full enforcement for high-risk systems [1].

- **65,000+** high-risk systems to certify [1]
- Compliance market estimated at **EUR 7.6–31 Bn** over 5 years (upper range contested) [1]
- Penalties: up to **EUR 35M** or **7%** of worldwide turnover [1]

**Giskard** (Paris, ~24 people): open-source testing for hallucinations, bias, injections. Clients: **AXA, BNP, Michelin, L'Oreal, Banque de France**. Phare benchmark with **Google DeepMind** [2].

> Regulation **creates** markets. GDPR created a multi-billion privacy market — the AI Act will do the same.

### Citations (verbatim from original)

<small>Sources : [1] [CDI](https://www2.datainnovation.org/2021-aia-costs.pdf) · [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [TechCrunch](https://techcrunch.com/2023/11/14/giskards-open-source-framework-evaluates-ai-models-before-theyre-pushed-into-production/)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- The EU AI Act creates a multi-billion compliance market with 65,000+ systems to certify.
- European players like Giskard are already building the tooling — regulation is a founder opportunity.

---

## B-ecosysteme-ia slide 21 — Discussion: where to position in the stack?

**Original title (FR)**: Discussion : Ou se positionner dans le stack ?
**English title**: Discussion: where to position in the stack?
**Slide class** (if any): compact
**Image references**: (none)

### Body (English)

> **EUR 500K**, **4 technical people**, 18 months of runway.

| Layer | Capital required | Competition | Opportunity |
|--------|---------------|-------------|-------------|
| Hardware | >$1 Bn | Extreme | Nearly impossible |
| Foundation Models | >$100 M | Very strong | Niche (code, medical) |
| Hubs / APIs | $1–10 M | Strong | Orchestration, vertical |
| Safety / Eval. | $500K–5 M | Moderate | EU AI Act, compliance |
| Applications | $200K–5 M | Variable | Vertical + workflow |

**Questions**:
- Which impact/capital ratio is best?
- Safety viable with 4 people? (Giskard: EUR 7.5M raised)

### Citations (verbatim from original)

(no citation line)

### Key ideas (≤2 bullets, for downstream slide designer)

- A capital-vs-competition matrix across stack layers — makes the founder choice concrete.
- With modest runway, Safety/Compliance and vertical Applications are the realistic entry points.

---

## A-regulation-ethique slide 03 — EU AI Act: the 4 risk levels

**Original title (FR)**: EU AI Act : les 4 niveaux de risque
**English title**: EU AI Act: the 4 risk levels
**Slide class** (if any): img-right
**Image references**: `![bg right:55% contain](assets/infographics/eu-ai-act-risk-pyramid_run_20260330_144415_20c1f0.png)`

### Body (English)

- **Prohibited** — manipulation, mass surveillance → **banned** Feb. 2025
- **High-risk** — employment, credit, healthcare → full compliance required [1]
- **Limited** — chatbots, deepfakes → must **identify themselves as AI** to the user
- **Minimal** — spam filters, video games → no obligation (no impact on rights)

> The Commission estimated **5–15%** of systems as high-risk — appliedAI finds **18%** [2].

### Citations (verbatim from original)

<small>Sources : [1] [EU AI Act Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [appliedAI](https://www.appliedai.de/en/hub-en/ai-act-impact-survey)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- The EU AI Act classifies systems into 4 risk tiers — only Prohibited and High-risk carry heavy obligations.
- High-risk is broader than first estimated (18% vs. 5–15%) — likely to catch more founders than expected.

---

## A-regulation-ethique slide 04 — EU AI Act: timeline and costs

**Original title (FR)**: EU AI Act : calendrier et coûts
**English title**: EU AI Act: timeline and costs
**Slide class** (if any): compact
**Image references**: (none)

### Body (English)

| Date | Who is affected | What changes |
|------|-----------------|---------------|
| Feb. 2025 | Everyone | Prohibited practices (social scoring, real-time biometrics) |
| Aug. 2025 | Providers of **GPAI** (General-Purpose AI = foundation models like GPT, Gemini, Mistral) | Technical documentation, energy reporting, training-data summary |
| Aug. 2026 | Providers of **high-risk** systems (recruitment, credit, healthcare...) | Full compliance + fines apply |
| Aug. 2027 | High-risk systems **embedded in an already-regulated product** (medical devices, industrial machinery) | Same compliance, but extended deadline due to double certification (AI Act + MDR/MDR) |

**Costs**: **EUR 193K–330K** per system + **EUR 71K/year** maintenance [1]

### Citations (verbatim from original)

<small>Sources : [1] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/) · [2] [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

### Key ideas (≤2 bullets, for downstream slide designer)

- The EU AI Act rolls out in four phases from Feb. 2025 to Aug. 2027, each adding obligations for a new class of providers.
- Compliance is concrete and expensive: EUR 193K–330K per system up-front, EUR 71K/year ongoing.

---

## URL issues to review

- In A-llms slide 13, citation [1] labeled "Epoch AI" points to `https://arxiv.org/abs/2405.21015` (an arXiv paper, not epoch.ai) — the label/URL mismatch may mislead readers.
- In A-regulation-ethique slide 04, the source line contains reference `[2]` pointing to `https://eur-lex.europa.eu/eli/reg/2024/1689`, but no `[2]` marker appears in the slide body — orphan citation.
- In B-ecosysteme-ia slide 16, the citations footer shows a bare `[EUR-Lex](...)` after `[1]` with no numeric marker, while `[2]` jumps straight to TechCrunch — the EUR-Lex link is neither numbered nor referenced inline.
- In C-agents slide 37, citation [1] for "Anthropic — Claude Code" points to the generic `https://www.anthropic.com/` root rather than the Claude Code product/research page.
