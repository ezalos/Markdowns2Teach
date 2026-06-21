---
marp: true
theme: sorbonne
paginate: true
header: "Building AI Agents · Université Gustave Eiffel · 2026-06-01"
---
<!-- ABOUTME: AI Agents — LLM state, what is an agent, Tools/MCP/Skills, orchestration patterns, agent harness + Raschka anatomy, Hermes deep-dive, memory cognitive taxonomy, MiroFish + AutoResearch, production gap, evaluation. -->
<!-- ABOUTME: 2026-06-01 talk at Université Gustave Eiffel — English-language standalone deck. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Building AI Agents

## From workflow to autonomy

Université Gustave Eiffel · June 1, 2026

---

<!-- _class: compact -->

# 01 — Whoami

**End of studies @ 42**
- Directed 42AI Lab — partnership with CNRS

**Entrepreneurship @ ICONO**
- Built a SOTA video search engine — **100M videos searchable in 3s** at scale
- AI Lead at **Station F**

**ML Research Eng @ Heuritech**
- Novel research methodology — **beat 11 in-house high-scores**
- Built and scaled a **1B+ embedding system**

**Teaching**
- **42** — built the AI curriculum followed by **25K people / year** globally
- **Sorbonne** — M2 ML & DeepTech

🔗 [linkedin.com/in/louis-develle](https://www.linkedin.com/in/louis-develle/)

---

# 02 — Agenda

1. **Where LLMs are going** — benchmarks, cost, open vs closed
2. **What is an agent?** — the control ladder, the ReAct loop
3. **Tools, MCP, Skills** — the building blocks
4. **Agent orchestration patterns** — 5 levels from prompt chains to autonomy
5. **The agent harness** — and the 6-component anatomy of a coding agent
6. **Hermes** — memory and auto-skill generation, the open-source alternative
7. **Agent memory** — a cognitive taxonomy + the real tradeoffs
8. **MiroFish, AutoResearch** — two more agent shapes
9. **Production & evaluation** — the reliability gap and how to close it

---

<!-- _class: section -->

# Where LLMs are going

## Benchmarks, cost, open vs closed

---

<!-- _class: img-right -->

# 03 — Benchmarks: real progress, visible ceilings

![bg right:55% contain](assets/epoch_ai_llm_saturation_benchmarks.jpeg)

- MMLU (general knowledge): **saturated at 90%+** — LLMs catching up with human experts [1]
- New, harder benchmarks: Humanity's Last Exam **8.8%**, FrontierMath **2%** [2]
- Efficiency: from **540B** down to **3.8B** params for 60% on MMLU — a **142× reduction** [1]

> Easy benchmarks saturate, but hard problems remain out of reach.

<small>Sources : [1] [Epoch AI](https://epoch.ai/trends) · [2] [Stanford HAI AI Index 2025](https://aiindex.stanford.edu/report/)</small>

---

<!-- _class: img-right -->

# 04 — METR: task autonomy doubles every 7 months

![bg right:50% contain](assets/benchmarks/metr-time-horizon-linear-2026-06.png)

- METR measures the **time-horizon** an AI completes with 50% reliability [1]
- That horizon **doubles every ~7 months** over 6 years of data — **3× faster than Moore's Law** [2]
- 2019 GPT-2: ~3 seconds → 2025 Claude Opus 4.5: **~4h 53min** [1]
- Time Horizon **1.1** update (Jul 2025): similar trajectory across 9 benchmarks [1]

> If the curve holds, multi-day autonomous agents are 18 months away.

<small>Sources : [1] [METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) · [2] [Kwa et al. 2025, arXiv:2503.14499](https://arxiv.org/abs/2503.14499)</small>

---

<!-- _class: img-right -->

# 05 — Inference cost is collapsing

![bg right:55% contain](assets/benchmarks/epoch-inference-01.png)

- Cost per million tokens **drops ~10×/year** for equivalent capability [1]
- GPT-3.5 (Dec 2022) → GPT-5-mini (2026): same task, **~100× cheaper** [1]
- Open-weights matched: Mistral Small 3 24B beats Llama 3.3 70B at **1/3 the cost** [2]

> Build for capability now — expect the price to crater under your feet within 12 months.

<small>Sources : [1] [Epoch AI — Inference price trends](https://epoch.ai/data-insights/llm-inference-price-trends) · [2] [Mistral Small 3](https://mistral.ai/news/mistral-small-3)</small>

---

<!-- _class: img-right -->

# 06 — Open-source closes the gap — and the headline understates it

![bg right:55% contain](assets/benchmarks/lesswrong-open-vs-closed-gap.png)

- **Epoch AI (May 29, 2026)**: open lags closed by **4 months on public benchmarks** (ECI, 8-point gap) [1]
- **Ihle (LessWrong, May 28, 2026)**: gap is **8–10 months on private benchmarks** — public benchmarks understate it ~2× because open devs optimize for what's measurable [2]
- Mistral **Devstral 2** (Mar 2026): top open coder, **4× smaller / 7× cheaper** than Sonnet [3]

> Real-world gap is probably larger than the headline — closed labs see things you can't [2].

<small>Sources : [1] [Epoch AI — Open vs closed ECI](https://epoch.ai/data-insights/open-closed-eci-gap) · [2] [Ihle — How Far Behind Are Open Models?](https://www.lesswrong.com/posts/rJcCrXyEsJKmmDpWG/how-far-behind-are-open-models) · [3] [Mistral Devstral](https://mistral.ai/news/devstral)</small>

---

<!-- _class: section -->

# What is an agent?

## The new battleground

---

<!-- _class: compact-table -->

# 07 — The control ladder: where the LLM sits in your program

Four levels of LLM usage. The line that matters is the last one [1].

| Level | What it is | Who controls steps | Minimal example |
|-------|-----------|---|---|
| **Single call** | One prompt in, one completion out | The human | "Summarize this email" |
| **Chain / pipeline** | Several LLM calls in a fixed order | The developer | extract → classify → reply |
| **Workflow** | LLM calls + tools, predefined branches | The developer | if intent=refund → run refund flow |
| **Agent** | The LLM **decides** the next step at runtime | The model | "book me dinner Tuesday night" |

> Litmus test: *if you can't predict in advance which tools will be called, in what order, and how many times — it's an agent* [1].

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 08 — The agent loop: Think → Act → Observe

![bg right:40% contain](assets/agent-cycle-hf.gif)

**ReAct** (Reason + Act) [1][2] — Think → Act → Observe → repeat until goal reached.

**Goal**: *"find an Asian restaurant in Paris for Tuesday night"* · **Tools**: `web_search`, `fetch_page`, `query_gmaps`

- *Act* `web_search("asian restaurants paris")`
  *Observe* top results
- *Act* `fetch_page("top-10 list")`
  *Observe* names + addresses
- *Act* `query_gmaps("Restaurant X, Tuesday 8pm")`
  *Observe* open ✓
- → return result · **stop**

> Nobody hardcoded "search → fetch → check gmaps". The model assembled it from the goal and the tools.

<small>Sources : [1] [HuggingFace Agents Course](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) · [2] [ReAct — Yao et al., arXiv:2210.03629](https://arxiv.org/abs/2210.03629)</small>

---

<!-- _class: section -->

# Tools, MCP, Skills

## The building blocks, and the universal standard

---

# 09 — Tools = function calling

A model alone only outputs text. **Function calling** lets it act on the world [1]:

1. You give the model a list of available tools, each with a **name**, **description**, and **JSON schema** for its arguments
2. When the model wants to act, it doesn't *execute* — it **emits a structured request**: `{ "tool": "search_web", "args": { "query": "..." } }`
3. Your surrounding code (the "harness") executes the function and hands the **result back** as the next observation

> **The model proposes; the runtime disposes.** This separation is where most of the safety and permissioning lives.

<small>Sources : [1] [Anthropic — Tool use docs](https://docs.anthropic.com/en/docs/build-with-claude/tool-use)</small>

---

<!-- _class: img-right -->

# 10 — MCP: a universal LLM ↔ tools standard

![bg right:45% vertical contain](assets/mcp-hf/mcp-before-1a.png)
![bg right:45% vertical contain](assets/mcp-with-standard.png)

Without a standard, **every AI app** writes a connector for **every tool** — **M×N** integrations to maintain.

The **Model Context Protocol** (Anthropic, Nov 2024) flips it to **M+N** [1]:

- Each app implements the **client** once
- Each tool implements the **server** once
- Adoption in 2026: Claude, ChatGPT, Gemini, Copilot, Cursor, VS Code, AWS, Cloudflare, Google Cloud, Azure
- Donated to the **AAIF** (Linux Foundation) [2]

> One MCP server = compatible with every agent. Integration drops from weeks to hours [1].

<small>Sources : [1] [Anthropic — MCP](https://www.anthropic.com/news/model-context-protocol) · [2] [AAIF — Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)</small>

---

<!-- _class: cols -->

# 11 — MCP: limits, risks, and the debate

<div class="left">

**3 documented attacks** [1]:
- **Tool Poisoning** — malicious description injects instructions
- **Rug Pull** — tool changes behavior post-approval
- **Cross-Server Shadowing** — server intercepts another's calls
- Cisco audit: **26% of 31K skills** had ≥1 vulnerability [2]

</div>
<div class="right">

**The open debate**:
- Extra abstraction for simple cases
- Native function calling improves fast
- Standardization premature? Field evolves fast
- Risk of de-facto lock-in despite formal openness

</div>

> Inspect tool **descriptions**, not just names. Treat any externally-influenced content as untrusted before it enters memory or runs.

<small>Sources : [1] [Invariant Labs — MCP Security](https://invariantlabs.ai/) · [2] [Cisco — Skill Scanner audit](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare)</small>

---

<!-- _class: compact -->

# 12 — Skills: a tool is "how", a skill is "what to do"

A **Tool** connects the agent to a service. A **Skill** teaches it a **complete process** [1]:

```yaml
---
name: translate-document
description: Translate a document while preserving formatting
---
# Steps
1. Read the source file
2. Detect the source language from the first 500 characters
3. Translate section by section, preserving all markdown
4. Write the output file with suffix _<lang>.md
5. Report: source language, target language, word count
```

> Tool = atomic connectivity (a function). Skill = procedural know-how (a recipe). Skills are **versionable, testable, shareable** — and your proprietary skills are a moat [1].

> ⚠️ **External skills = supply chain.** Snyk's *ToxicSkills* (Feb 2026): of **3,984** ClawHub / skills.sh skills audited, **37% had ≥ 1 security flaw**, **13% critical**, **76 confirmed malicious payloads** [2].

<small>Sources : [1] [Anthropic — Skills (agentskills.io)](https://agentskills.io/) · [2] [Snyk — ToxicSkills (Feb 5, 2026)](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/)</small>

---

<!-- _class: section -->

# Agent orchestration patterns

## From prompt chains to autonomy

---

<!-- _class: cols -->

# 13 — Prompt Chaining + Routing: the simple patterns

<div class="left">

**Prompt Chaining** — sequential steps, gate checks between [1]
![w:480](assets/anthropic/prompt-chaining.png)

*Recruiter screen* — input: Job Description + CV<br>
→ check each requirement appears in the resume<br>
→ assess fit level for each<br>
→ write a 2-liner to the recruiter

</div>
<div class="right">

**Routing** — classify, then send to a specialist [1]
![w:480](assets/anthropic/routing.png)

*Customer support* — evaluate the message<br>
→ light info: SLM<br>
→ complex: reasoning LLM<br>
→ complaint: human

</div>

> Together these cover **most business use cases** without the complexity of an agent.

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: cols -->

# 14 — Parallelization + Orchestrator-Workers: more LLMs at once

<div class="left">

**Parallelization** — same task split or repeated [1]
![w:480](assets/anthropic/parallelization.png)

*Sectioning*: analyze legal / financial / technical of a contract simultaneously · *Voting*: 3 reviewers, majority wins

</div>
<div class="right">

**Orchestrator-Workers** — decompose at runtime [1]
![w:480](assets/anthropic/orchestrator-workers.png)

*Market analysis*: orchestrator picks subtasks (size, competitors, regulation, trends, risks) → workers in parallel → synthesis

</div>

> Subtasks **predefined** = Parallelization. Subtasks **chosen at runtime** = Orchestrator-Workers.

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 15 — Evaluator-Optimizer: the improvement loop

One LLM **generates**, another **evaluates** and gives feedback. Loop until the quality threshold is met [1].

**Example** — drafting a sales proposal:
- Generator drafts the proposal
- Evaluator checks tone, numbers, compliance with the brief
- Feedback → revise → loop

**Caution**: each iteration costs money. Wire in a **circuit breaker** (max 3–5 rounds).

![bg right:55% contain](assets/anthropic/evaluator-optimizer.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: section -->

# The agent harness

## Claude Code as the canonical example

---

<!-- _class: img-right -->

# 16 — Claude Code: a coding agent

![bg right:50% contain](assets/claude-code-anthropic.png)

A terminal-native coding agent built by Anthropic [1]. Point it at a repo, give it a goal; it reads files, runs commands, edits code, runs tests, and iterates until done.

- **Used for**: pair-programming, refactoring, fixing failing tests, multi-file edits, codebase analysis
- **Lives in**: your terminal, alongside your editor — files on disk, git, dev tools
- **Special**: the same LLM you'd talk to in claude.ai — wrapped in a harness designed for code

> *Same LLM, different harness — completely different product.* The next slides explain what's in that harness.

<small>Sources : [1] [Anthropic — Claude Code docs](https://docs.claude.com/en/docs/claude-code)</small>

---

<!-- _class: img-right compact -->

# 17 — What's an agent harness?

![bg right:50% contain](assets/anthropic/managed-agents-overview.png)

A bare LLM only generates text. An **agent harness** is **everything around the LLM** that turns generation into action [1][2]:

- **Tools** — typed functions the model can call (`web_search`, `fetch`, `edit_file`)
- **Memory** — what survives across turns and sessions
- **Context engineering** — *what* goes into the window, *when*, and *how it's compacted*
- **Sandbox** — where tool calls actually run (container, VM, browser, your machine)
- **Orchestration** — when sessions wake (cron, queue, user request)
- **Serving layer** — model routing, prompt caching, retries, observability

> Same LLM, different harness → wildly different product. We'll dissect Claude Code's harness through Raschka's 6-component model [2].

<small>Sources : [1] [Anthropic — Managed agents](https://www.anthropic.com/engineering/managed-agents) · [2] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 18 — Component 1 — Live Repo Context

![bg right:55% contain](assets/raschka/06-workspace-summary.png)

- The agent collects **stable facts** about your workspace upfront [1]
- Git state, repo layout, AGENTS.md / CLAUDE.md conventions, recent test results
- *"Fix the tests"* is **not self-contained** — the meaning lives in the repo, not in the prompt

> A thin chat wrapper around GPT-5 doesn't beat Claude Code because **the harness reads your project for you**.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 19 — Component 2 — Stable Prompt Prefix + Cache Reuse

![bg right:55% contain](assets/raschka/07-stable-prompt-prefix.png)

- Instructions + tool list + repo summary form a **stable prompt prefix** [1]
- Reused across every turn via **prompt caching** — same bytes, **~10× cheaper, ~2× faster**
- Only the session state (recent transcript + newest user request) changes turn-to-turn

> The cheap-but-stable part stays cheap. The new-but-small part stays small. That's how 100-turn sessions stay affordable.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 20 — Component 3 — Tool Access + Permissions

![bg right:65% contain](assets/raschka/08-tool-use-flow-full.png)

- Tools = the line between **chat** and **agency** [1]
- The model emits a structured action → harness **validates** (typed inputs, path checks) → **approves** → **executes** → feeds result back [1]
- Claude Code ships with **~18 named tools** — `BashTool`, `FileEditTool`, `WebFetchTool`, etc. [2]

> The harness gives the model **less** freedom — and that's exactly why it ships [1].

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — Claude Code source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 21 — Component 4 — Context Compaction

![bg right:55% contain](assets/raschka/10-context-compaction.png)

- Long contexts are expensive **and noisy** — coding agents bloat fast via repeated reads, long outputs, logs [1]
- Two core strategies: **clip** oversized items, **summarize** older transcript entries; plus deduplicate repeated file reads [1]
- The Claude Code source leak reveals **five distinct compaction strategies** (per-tool clipping, transcript summarization, file-read dedup, session consolidation aka **autoDream**, subagent fork-caching) [2]

> Underrated, boring, decisive — **context quality *is* model quality**.

<small>Sources : [1] [Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — Claude Code source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>

---

<!-- _class: img-right -->

# 22 — Component 5 — Structured Session Memory

![bg right:55% contain](assets/raschka/11-transcript-and-memory.png)

Two storage layers, both on-disk JSON [1]:

- **Working memory** — distilled, small, "what matters now"
- **Full transcript** — every turn, append-only, durable, resumable

Working memory feeds into the next prompt; the transcript serves audit + replay.

> Re-reading from a transcript on resume is the cheapest, most reliable way to fix the "Monday-morning amnesia" of agents.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# 23 — Component 6 — Bounded Subagents

![bg right:55% contain](assets/raschka/12-bounded-subagent.png)

- Delegation parallelizes subtasks: *"which file defines X?"*, *"why is this test failing?"* [1]
- The hard part isn't *spawning* — it's **binding**: enough context to work, tight enough not to explode [1]
- Techniques: read-only mode, recursion depth limits, scoped task descriptions, parent prompt-cache reuse

> *"The tricky design problem is not just how to spawn a subagent but how to **bind** one."* — Raschka [1]

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: section -->

# Hermes

## The open-source alternative — the agent that learns

---

<!-- _class: compact -->

# 24 — Hermes: the open-source persistent agent

![w:1100](assets/hermes-banner.png)

**Hermes Agent** (Nous Research, launched Feb 25, 2026) — open-source MIT, model-agnostic, server-resident personal agent [1]:

- **Open and model-agnostic** — runs on Hermes 4 open-weights, OpenRouter (200+ models), OpenAI, or your own endpoint. **Switch with `hermes model` — no code changes.**
- **Multi-surface** — single `AIAgent` class drives CLI, IDE (ACP), API, and **20 messaging platforms** (Telegram, Discord, Slack, WhatsApp…)
- **Adoption** — ~**105K GitHub stars** 7 weeks after launch; around May 10, 2026 reportedly **overtook OpenClaw on OpenRouter** daily token volume (~224B vs 186B tokens/day) [2]

> *"The only agent with a built-in learning loop — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations."* — Nous Research README [1]

<small>Sources : [1] [Nous Research — Hermes Agent (GitHub)](https://github.com/NousResearch/hermes-agent) · [2] [kisztof.medium.com (third-party adoption claim)](https://medium.com/@kisztof)</small>

---

<!-- _class: cols compact-table -->

# 25 — Claude Code vs Hermes: depth of learning vs controllable simplicity

<div class="left">

| Dimension | Claude Code | Hermes |
|---|---|---|
| **Lifespan** | Per-session | Always-on |
| **Lives in** | Terminal / IDE | Server you control |
| **Memory** | CLAUDE.md re-read | MEMORY.md frozen + FTS5 |
| **Skills** | Human-written | Agent writes + Curator |
| **Model** | Claude only | Pluggable (200+) |

</div>
<div class="right">

**Same machinery** (model + tools + loop). Very different product shape.

**Claude Code**: auditable, single-process coding agent in the IDE — enterprise-grade controls.

**Hermes**: persistent, multi-surface personal agent that *accumulates competence* across weeks — on your own / open models.

</div>

> "Agent" is an **architecture, not a single product**. The variation is in autonomy, persistence, and where the human sits.

---

<!-- _class: compact -->

# 26 — Hermes memory: bounded, agent-curated, cache-stable

The deliberate bet: **the agent owns its memory**, with hard limits [1]:

- **`MEMORY.md`** (~800 tokens, agent notes) + **`USER.md`** (~500 tokens, user profile) — injected as a **frozen snapshot at session start** → preserves the prompt-prefix cache
- Managed via a `memory` tool (`add` / `replace` / `remove` — no `read`, it's already in the prompt); writes are **security-scanned** for injection / exfiltration
- **FTS5 session search** over `~/.hermes/state.db` — every past session searchable in **~20ms, no LLM cost**
- **8 pluggable external providers** (Honcho, Mem0, …) — one active at a time

> Hard char limits **force consolidation** — the agent must triage what matters [1].

<small>Sources : [1] [Nous Research — Hermes Agent docs](https://hermes-agent.nousresearch.com/docs)</small>

---

<!-- _class: compact -->

# 27 — Hermes auto-skills: the closed learning loop

The unique mechanism: the agent writes its own **procedural memory** [1]:

- **When**: after a complex task (**5+ tool calls**) succeeds, after recovering from errors, or after a user correction
- **How**: the `skill_manage` tool writes a `SKILL.md` with `When to Use` / `Procedure` / `Pitfalls` / `Verification` sections
- **Background Curator (weekly)**: ages agent-created skills `active → stale (30d) → archived (90d)`, consolidates near-duplicates; never auto-deletes, snapshots before each run

> "Self-improving" amplifies the base model — weak model → weak skills. The 40% efficiency claim is a vendor figure, not an independent benchmark [1].

<small>Sources : [1] [Nous Research — Hermes Agent docs](https://hermes-agent.nousresearch.com/docs)</small>

---

<!-- _class: section -->

# Agent memory

## What an agent remembers — and what it has to give up

---

# 28 — Why memory is hard: the finite, degrading, amnesiac window

Every memory system solves the same three problems [1][2]:

- **Finite context window** — token caps + tool schemas + memory files compete for the same budget
- **Context rot** — Chroma (Jul 2025, 18 LLMs incl. GPT-4.1, Claude 4, Gemini 2.5, Qwen3): needle-in-haystack accuracy **drops 20–50% from 10k to 100k+ tokens**. Transformer attention is *n²* [2]
- **Cross-session amnesia** — each new session starts blank ("engineers in shifts with no memory of the previous shift") [1]

> **Long context is not memory.** Bigger windows just let you waste more tokens before it bites you.

<small>Sources : [1] [Anthropic — Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [2] [Hong, Troynikov, Huber — Context Rot (Chroma, Jul 2025)](https://research.trychroma.com/context-rot)</small>

---

<!-- _class: compact-table -->

# 29 — A cognitive taxonomy: 4 types of memory

CoALA (Princeton/CMU, 2023) borrows from cognitive science (Tulving's categories) [1]. **Short-term = working only**; **long-term = the other three** (cheap to hold, must be retrieved):

| Type | Term | Cognitive analogy | Agent example |
|---|---|---|---|
| **Working** | Short | What you hold in mind right now | System prompt + tools + recent turns |
| **Episodic** | Long | "I remember when…" | Session transcripts, error logs |
| **Semantic** | Long | "I know that…" | CLAUDE.md, "user prefers TypeScript" |
| **Procedural** | Long | "I know how to…" | SKILL.md files |

> Procedural says *how*, semantic says *what's true*, episodic says *what happened*, working memory holds the live reasoning. The whole game: **move information between short and long intelligently**.

<small>Sources : [1] [Sumers et al. — CoALA (arXiv:2309.02427, 2023)](https://arxiv.org/abs/2309.02427)</small>

---

<!-- _class: compact-table -->

# 30 — Solutions per cognitive layer

How real systems implement each cognitive type:

| Type | Mechanism | Claude Code's choice | Hermes Agent's choice |
|---|---|---|---|
| **Working** | Prompt prefix + cache, compaction | Server-side compaction near the limit + tool-result clearing | Pre-compaction "memory flush" → agent gets 1 turn to save before context is dropped |
| **Episodic** | Session transcripts | On-disk JSON, append-only | SQLite + FTS5 full-text search (~20ms, no LLM cost) |
| **Semantic** | Persistent files / vector DB | `CLAUDE.md` re-read every session, `/memories` tool | `MEMORY.md` (~800t) + `USER.md` (~500t), frozen snapshot |
| **Procedural** | Skill files | Human-written `SKILL.md` | Agent autonomously writes `SKILL.md` after 5+ tool-call tasks; Curator ages stale ones |

> Same cognitive types, opposite philosophies: **harness-managed lean context** (Claude Code) vs. **agent-owned bounded curation** (Hermes).

<small>Sources : [1] [Anthropic — Claude Code memory docs](https://docs.claude.com/en/docs/claude-code/memory) · [2] [Nous Research — Hermes Agent docs](https://hermes-agent.nousresearch.com/docs)</small>

---

# 31 — Consolidation: making sense of accumulated experience

The newest layer in 2026 agents: **off-line consolidation** — turning raw episodes into durable, generalized knowledge. The cognitive analogy is **sleep**:

- **Claude Code's `autoDream`** [1] — session-end consolidation: merge near-duplicates, prune contradictions, distill the transcript into a smaller working-memory delta
- **Hermes Curator** [2] — weekly LLM review of agent-created skills: consolidates duplicates, archives stale ones (`active → stale 30d → archived 90d`)

> Consolidation is what makes long-running agents **competent** rather than just persistent.

<small>Sources : [1] [Latent Space — Claude Code source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak) · [2] [Hermes docs](https://hermes-agent.nousresearch.com/docs)</small>

---

<!-- _class: compact -->

# 32 — Limits and tradeoffs

The honest picture from the 2026 literature:

- **Lossy compaction** — summarization can drop a critical file path or error code. Mitigation: persist durable rules in files (CLAUDE.md), compact at task boundaries
- **Write-path is the hard part** — *what* to remember matters more than *where*. Storing everything poisons recall and inflates cost
- **Memory is an attack surface** — *Trojan Hippo* (May 2026) demonstrates exfiltration via poisoned memory writes. Scan inputs; treat externally-influenced content as untrusted
- **Token cost is real** — Mem0's 2026 benchmarks show **~90% token-cost reduction vs full-context** on LoCoMo at equivalent quality

> Open problems: continual consolidation, causally-grounded retrieval, multi-agent memory sync.

<small>Sources : [Anthropic — Context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · [Trojan Hippo arXiv:2605.01970](https://arxiv.org/abs/2605.01970) · [Mem0 ECAI 2025, arXiv:2504.19413](https://arxiv.org/abs/2504.19413)</small>

---

<!-- _class: section -->

# Two more agent shapes

## MiroFish (swarm) and AutoResearch (script)

---

<!-- _class: img-right compact -->

# 33 — MiroFish: swarm intelligence as forecasting

![bg right:55% contain](assets/mirofish/MiroFish_logo_compressed.jpeg)

- **What it is**: open-source swarm engine — thousands of LLM personas simulate a digital world to forecast social, political, financial outcomes [1]
- **Headline**: ~**52–54K GitHub stars** (Apr 2026); AGPL-3.0; built on CAMEL-AI's OASIS + GraphRAG [1][2]
- **Distinct angle**: not a single assistant — a **multi-agent swarm** running parallel worlds for prediction
- **Real cases**: Wuhan opinion simulation, "Dream of the Red Chamber" lost-ending prediction [1]

> A reminder that "agent" doesn't only mean assistant — it can mean a population.

<small>Sources : [1] [GitHub — MiroFish](https://github.com/666ghj/MiroFish) · [2] [CAMEL-AI OASIS](https://github.com/camel-ai/oasis)</small>

---

<!-- _class: img-right compact -->

# 34 — Karpathy AutoResearch: agent-as-script

![bg right:55% contain](assets/infographics/autoresearch-loop.png)

- **What it is**: Karpathy's autonomous ML-research harness — a **630-line Python script**; agent edits `train.py`, keeps/discards based on `val_bpb` [1]
- **Headline**: **70,300 GitHub stars** (Apr 2026); 5-min budget per experiment; 1 GPU, 1 file, 1 metric [1]
- **Result**: **11% gain on "Time to GPT-2"** — 2.02h → 1.80h after ~20 auto-discovered optimizations [2]
- **Conceptual shift**: you write the `program.md`, the agent writes the Python [3]

> An effective harness can be 600 lines of Python — the system matters more than the framework.

<small>Sources : [1] [GitHub — karpathy/autoresearch](https://github.com/karpathy/autoresearch) · [2] [36kr](https://eu.36kr.com/en/p/3725521482578567) · [3] [The New Stack](https://thenewstack.io/karpathy-autonomous-experiment-loop/)</small>

---

<!-- _class: section -->

# Agents in production — the reliability gap

## Where the demo breaks

---

<!-- _class: img-right -->

# 35 — The compounding-error problem

![bg right:40% contain](assets/philschmid-pass-at-k.jpg)

Why autonomous agents fail in production: **errors compound** at every step.

- 10 steps × 95% reliability = **60% overall success** (0.95¹⁰)
- 20 steps × 95% = **36%** success
- 50 steps × 95% = **8%** success

**Solutions**:
- **Reduce the number of steps** — simplify the workflow
- **Increase per-step reliability** — better prompts, tools, validation
- **Human-in-the-Loop** at critical points

> Gartner forecasts **40%** of agent projects cancelled by 2027 [1]. Reliability, not sophistication — see also `pass@k` vs `pass^k` [2].

<small>Sources : [1] [Gartner — Predicts 2025: AI Agents](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027) · [2] [Phil Schmid — pass@k vs pass^k](https://www.philschmid.de/agents-pass-at-k-pass-power-k)</small>

---

<!-- _class: cols compact -->

# 36 — Failure modes, guardrails, and when NOT to use an agent

<div class="left">

**Failure modes**:
- **Context Drift** — forgets its goal
- **Infinite Loop** — loops forever
- **Wrong Tool** — wrong tool for the job
- **Hallucinated Success** — declares victory without checking

**Guardrails**:
- Human-in-the-Loop at critical steps
- Retry + escalate (3 tries → human)
- Observability — log every ReAct step
- Budget (tokens / steps) = circuit breaker

</div>
<div class="right">

**Use an agent when** [1]:
- The task needs flexible, unpredictable decisions
- The number of steps can't be defined in advance
- Value justifies the extra cost

**Don't use an agent when**:
- A simple Prompt Chain suffices
- The workflow is predictable and fixed
- Cost of error is high and supervision is hard

</div>

> **1 well-equipped agent > N poorly-coordinated agents** — Cognition (Devin) and Cline both chose Single-Agent [2][3].

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) · [2] [Cognition — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems/) · [3] [Cline — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-i-stopped-using-rag-for-coding-agents-and-you-should-too/)</small>

---

<!-- _class: section -->

# Evaluating an agent

## The difference between an impressive demo and a system in production

---

<!-- _class: compact -->

# 37 — Why this matters (Monte Carlo, Apr 2026)

A recent survey of **260 practitioners at 1,000+-employee orgs** [1]:

- **64% of enterprise leaders & engineers deployed AI agents before they were ready**
- **63%** discovered agents accessing unintended systems
- **36%** can't disable or rollback a failing agent within minutes
- **70%** expect significant system rebuilds post-deployment
- Only **47%** have end-to-end system traceability

> Reliability — not benchmark accuracy — is what separates a demo from production. And the only path to reliability is **proper evaluation**.

<small>Sources : [1] [Monte Carlo — Agents in Production (Apr 28, 2026, via Yahoo Finance)](https://finance.yahoo.com/sectors/technology/articles/two-thirds-64-enterprise-leaders-130000875.html)</small>

---

# 38 — Reliability, not accuracy, is the real target

Princeton's 2026 framework: agent reliability decomposes across **4 dimensions** [1]:

- **Consistency** — same input, same output across runs
- **Robustness** — survives small perturbations
- **Predictability** — bounded, knowable failure modes
- **Safety** — bounded blast radius when things go wrong

**The accuracy trap**: single-run `pass@1` numbers vary **2.2–6.0 percentage points** depending on which run you pick, with standard deviations >1.5pp even at temperature 0 [2].

> A single benchmark number is **misleading**. Report confidence intervals, run multiple trials, and pick `pass@k` (one success matters) or `pass^k` (consistency matters) based on the product need.

<small>Sources : [1] [Rabanser, Kapoor, Narayanan et al. — Science of AI Agent Reliability (Feb 2026)](https://arxiv.org/abs/2602.16666) · [2] [Bjarnason, Silva, Monperrus — On Randomness in Agentic Evals](https://arxiv.org/abs/2602.07150)</small>

---

# 39 — Look at your data first (error analysis)

The highest-leverage move is **manual error analysis**, not infrastructure [1]:

- **Review ≥100 real traces** before writing a single eval
- **Open coding** — domain expert writes free-text notes on the *first* failure in each trace
- **Axial coding** — group notes into a counted failure taxonomy (LLM can help on the second pass, never the first)
- Iterate until **theoretical saturation** (~20 traces with no new category)

> "In the projects we've worked on, we've spent **60–80% of our development time on error analysis and evaluation**. Expect most of your effort to go toward understanding failures rather than building automated checks." — Husain & Shankar (Jan 2026) [1]

<small>Sources : [1] [Husain & Shankar — LLM Evals FAQ (Jan 2026)](https://hamel.dev/blog/posts/llm-evals-faq/)</small>

---

<!-- _class: compact -->

# 40 — Scoring rules of thumb (Anthropic, Jan 2026)

The current state of the art for agent evals [1]:

- **20–50 simple tasks drawn from real failures** is enough to start. Each early change has a large, obvious effect → small samples suffice.
- **Binary > Likert** — pass/fail forces clearer thinking and more consistent labeling. For graded progress, decompose into multiple binary checks ("4 of 5 expected facts included").
- **Outcomes > paths** — grade what the agent *produced*, not the exact tool sequence it followed. Brittle path checks fail on harmless reorderings.
- **Allow partial credit** — multi-step tasks benefit from per-checkpoint scoring.
- **Balance positive/negative cases** — testing only "should search" cases produced an agent that over-searched.

> If you're passing 100% of your evals, you're not challenging the system enough. **70% is a meaningful pass rate.**

<small>Sources : [1] [Anthropic — Demystifying Evals for AI Agents (Jan 2026)](https://www.anthropic.com/research/demystifying-evals)</small>

---

# 41 — LLM-as-judge: useful, but must be validated

The most-abused technique in agent evals [1]:

- **Validate against human labels.** Measure **TPR and TNR** on a held-out labeled set. **Iterate the judge prompt until both ≥ 80%** — budget a day or two.
- **Scope it narrowly.** Judges should do scoped **binary classification**, one rubric dimension at a time.
- **Write your own prompt.** Off-the-shelf "helpfulness / coherence" judges create *false confidence*.
- **Give an "Unknown" escape hatch** — forced grades become hallucinated grades.
- **Known biases**: position, verbosity, recency. Authority hierarchy: **EXPERT > HUMAN > LLM > UNKNOWN** [2].

> A judge whose TPR/TNR you don't know is **not a measurement** — it's a coin flip with a confident voice.

<small>Sources : [1] [Husain & Shankar — LLM Evals FAQ](https://hamel.dev/blog/posts/llm-evals-faq/) · [2] [Eugene Yan — LLM-as-Judge Won't Save the Product](https://eugeneyan.com/writing/eval-process/)</small>

---

<!-- _class: cols -->

# 42 — Offline + online: the Swiss-cheese model

<div class="left">

**Offline (pre-deployment)**:
- **Inspect-AI** (UK AI Security Institute, MIT) — sandboxed harness, 200+ built-in evals
- Run in CI, block merges on regression
- Best for: code-execution, pentest, autoresearch agents

</div>
<div class="right">

**Online (deployed)**:
- **Langfuse / Phoenix / Braintrust** — production tracing + sampled LLM-judges
- Fast deterministic **guardrails** inline (regex, PII, schema)
- Confidence-interval alerting on quality drops

</div>

> **Close the loop**: every production failure becomes a new offline regression case. Anthropic's framing: no single layer catches everything — **defense in depth** [1].

<small>Sources : [1] [Anthropic — Demystifying Evals](https://www.anthropic.com/research/demystifying-evals) · [2] [Inspect-AI (UK AISI)](https://inspect.aisi.org.uk/)</small>

---

<!-- _class: section -->

# Synthesis

---

<!-- _class: compact -->

# 43 — Key takeaways

1. **The control ladder** — single call → chain → workflow → agent. The line that matters: *who decides the next step?*
2. **Tools → MCP → Skills** — atomic functions → universal standard → reusable processes. Your proprietary skills are a moat.
3. **Orchestration patterns** — start with Prompt Chaining; most problems are solved at levels 1–3 of the Anthropic ladder.
4. **The harness is the product** — Raschka's 6 components recur across coding agents. Same LLM, different harness = different product.
5. **Hermes vs Claude Code** — agent-owned bounded learning loop vs. harness-managed lean context. Two valid bets on the same machinery.
6. **Memory has a cognitive taxonomy** — working / episodic / semantic / procedural. *Long context is not memory.* Consolidation is the 2026 frontier.
7. **Less is more** — strip dependencies, fight context bloat, separate research from implementation, treat CLAUDE.md as a directory of rules [1].
8. **Evaluation closes the gap** — most enterprise deployments shipped before ready. Error analysis first, validate your judges, close the loop offline ↔ online.

<small>Sources : [1] [systematicls — Squeezing Every Last Bit Out Of Your Agent (X, May 2026)](https://x.com/systematicls/status/2028814227004395561)</small>

---

# 44 — Questions?

> "The LLM is the consultant. The harness is the office. The agent is the colleague who runs the meeting."

**To explore next**:
- Test Claude Code with a custom `CLAUDE.md` on a real project
- Spin up an existing MCP server (GitHub, Slack, Notion) and connect it
- Read Raschka's "Components of a Coding Agent" — the spine of this talk
- Read Husain & Shankar's "LLM Evals FAQ" before shipping any agent
- Try Hermes if you want a persistent agent that learns across sessions
