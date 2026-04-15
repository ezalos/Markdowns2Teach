<!-- ABOUTME: Single source of truth for the Station F course (2026-04-15). -->
<!-- ABOUTME: Regenerates the Marp decks. Citation-complete. See "Regeneration prompt" section to rebuild decks from scratch. -->

# Station F — Course Spec (2026-04-15)

## Audience & goal

**Event**: 1-hour talk at Station F, Wednesday April 15, 2026.
**Audience**: Startup founders, technically literate (ex-42 profile and similar). Most have shipped code. Most have used LLMs. Most are weighing "should my product bet on AI, and how deep?"
**Language**: English (this deck is a scoped exception from the repo's French-body convention).
**Primary intent**: give founders a tight, citation-solid mental model of where LLMs and agents actually are in 2026, what it takes to ship with them, and what the Klarna-style mistakes look like.

## Learning outcomes

By the end of the hour, a founder should be able to:

1. Describe the current cost/capability trajectory of LLMs in one paragraph, with numbers they'd trust in a pitch meeting.
2. Name the six components of a coding agent (Raschka framing) and explain why "a lot of apparent model quality is really context quality."
3. Pick the right MVP pattern (Wizard of Oz → Prompt-engineering MVP → API wrapper) for their idea.
4. Recite one augmentation-vs-automation failure (Klarna) and one success (L'Oréal / Doctolib) in 30 seconds each.
5. Know the EU AI Act enforcement deadline (Aug 2026) and whether their product sits in the high-risk category.

## Session flow (timed)

Two decks presented back-to-back, no break. Target 58 minutes of content + buffer.

### Deck A — `slides/station-f/A-state-of-the-field.md` (~25 slides, 30 min)

| # | Block | Duration | Slides |
|---|-------|----------|--------|
| A-00 | Title + hook + positioning | 3 min | 2–3 |
| A-01 | Where LLMs are going | 10 min | 6–8 |
| A-02 | Agents: definition → orchestration → components → wild | 17 min | 14–16 |

### Deck B — `slides/station-f/B-building-with-ai.md` (~20 slides, 28 min)

| # | Block | Duration | Slides |
|---|-------|----------|--------|
| B-00 | Title + bridge | 1 min | 1 |
| B-01 | Methodology & MVP patterns | 12 min | 8–10 |
| B-02 | Business reality + brief EU regs | 10 min | 6–8 |
| B-03 | Close / what to build next week | 3 min | 2 |

## Slide-by-slide content

> Each entry follows: **title** · *class* · body (English final copy) · **Citations** (references to index below) · **Reuse** (origin path or "new") · **Image** (if any).

### Deck A — State of the Field

#### A-00 — Title slide
*class: title* · *paginate: skip*

```
Building With AI, for Founders
Station F · April 15, 2026
```

**Reuse**: new.

---

#### A-01 — Hook (why this talk, why now)

- In 2024, Klarna's CEO said AI would replace 700 agents. In 2025, he hired humans back [KLARNA-REHIRE].
- In 2026, Anthropic accidentally shipped Claude Code's source map. The surprise wasn't the model — it was the 18 tools and 5-level permission system around it [LS-LEAK].
- Both stories are the same lesson: **the model is not the product**. The system around it is.

**Reuse**: new (synthesizes session-04/C slide 07 + Latent Space framing).

---

#### A-02 — What you'll leave with

- A numbers-trustable take on where LLMs are heading in 2026
- A six-part mental model for what's actually in a coding agent
- The MVP pattern list: Wizard of Oz → Prompt-eng → API wrapper
- Klarna + L'Oréal + Doctolib as your references for pitch-room war stories
- EU AI Act: the one date you need to remember

**Reuse**: new.

---

#### A-03 through A-10 — Where LLMs are going (6–8 slides)

> **Fill from**: Sorbonne extraction of `session-02/A-llms.md` slides 01, 02, 13, 14, 15, 16, 17, 28, 29, 30. Translate to English. Curate down to 6–8 slides for tech-founder relevance (benchmarks, cost curves, model selection).
>
> **Selection criteria**: keep slides that answer "what do I need to decide about as a founder?" — cost trends, open vs closed, model sizing. Drop architectural deep dives (MoE, quantization math).

**Citations to preserve**: inherited from source slides. Copy verbatim from `_sorbonne-extracted.md`.

**Reuse**: `slides/session-02/A-llms.md` slides 01-02, 13-17, 28-30.

---

#### A-11 — Agents: what counts as one

- A plain LLM call is not an agent. An **agent** is a loop: observe → inspect → choose → act, repeatedly, against an environment [RASCHKA-AGENT].
- The **agent harness** is the scaffolding around the model: prompts, tools, state, control flow [RASCHKA-AGENT].
- The **coding harness** is a task-specific harness for software engineering [RASCHKA-AGENT].

> Claude Code and the same API model in ChatGPT are *the same LLM*. What you notice is the harness. [RASCHKA-INTRO]

**Citations**: RASCHKA-AGENT, RASCHKA-INTRO.
**Reuse**: hybrid (`session-03/C-agents.md` slide 01 + new framing from Raschka).
**Image**: `docs/station-f/sources/raschka-coding-agent/images/02-llm-reasoning-agent-relationship.png` (copy to `slides/station-f/assets/raschka/`).

---

#### A-12 — Spectrum of agency

> **Fill from**: Sorbonne extraction of `session-03/C-agents.md` slides 02-03 (spectrum of agency — classification → research agent).
> Preserve the original citations.

**Reuse**: `slides/session-03/C-agents.md` slides 02-03.

---

#### A-13 — Orchestration patterns (overview)

> **Fill from**: Sorbonne extraction of `session-03/C-agents.md` slides 17-18. Keep the 5-pattern table (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer).

**Citations**: ANTHROPIC-AGENTS (preserve).
**Reuse**: `slides/session-03/C-agents.md` slides 17-18.

---

#### A-14 — Orchestration patterns in detail (1/2: chaining + routing)

> **Fill from**: `session-03/C-agents.md` slides 19-20. Translate, preserve citations.

**Reuse**: `session-03/C-agents.md` slides 19-20.

---

#### A-15 — Orchestration patterns in detail (2/2: parallelization + orch-workers + eval-opt)

> **Fill from**: `session-03/C-agents.md` slides 21-22-23. Translate, preserve citations.

**Reuse**: `session-03/C-agents.md` slides 21-23.

---

#### A-16 — Anatomy of a coding agent: 6 components

- A coding agent's capability comes less from the model and more from the surrounding system [RASCHKA-INTRO].
- Six recurring components across Claude Code, Codex CLI, and the Mini Coding Agent [RASCHKA-COMPONENTS]:
  1. Live Repo Context
  2. Prompt Shape + Cache Reuse
  3. Tool Access + Permissions
  4. Context Compaction
  5. Structured Session Memory
  6. Bounded Subagents

> "A lot of apparent 'model quality' is really context quality." — Raschka [RASCHKA-CONTEXT].

**Citations**: RASCHKA-INTRO, RASCHKA-COMPONENTS, RASCHKA-CONTEXT.
**Image**: Raschka figure 4 (`04-six-harness-features.png`) OR figure 13 (`13-six-features-summary.png`).
**Reuse**: new.

---

#### A-17 — Component 1+2: Live Repo Context + Prompt Prefix

*class: cols*

**Left — Live Repo Context**:
- Agent collects stable facts once: Git state, repo layout, AGENTS.md / CLAUDE.md conventions [RASCHKA-REPO-CONTEXT].
- "Fix the tests" is not self-contained; meaning comes from context [RASCHKA-REPO-CONTEXT].

**Right — Stable Prompt Prefix + Cache Reuse**:
- Stable prefix (instructions + tools + repo summary) reused via prompt caching [RASCHKA-PROMPT-SHAPE].
- Only the session state (recent transcript + newest request) changes each turn.

**Citations**: RASCHKA-REPO-CONTEXT, RASCHKA-PROMPT-SHAPE.
**Image**: Raschka figure 7 (`07-stable-prompt-prefix.png`) on the right.
**Reuse**: new.

---

#### A-18 — Component 3: Tool Access and Permissions

- Tools are the line between chat and agency [RASCHKA-TOOLS].
- Harness exposes a **typed, named tool list**; model emits structured actions; runtime validates before executing [RASCHKA-TOOLS].
- Claude Code ships with ~18 tools: `AgentTool`, `BashTool`, `FileEditTool`, `WebFetchTool`, `TodoWriteTool`, `AskUserQuestionTool`, `SkillTool`, `EnterPlanModeTool`, etc. [LS-TOOLS].
- Claude Code uses a **5-level permission system** to decide what's auto-approved vs prompted [LS-PERMISSIONS].

> "The harness is giving the model less freedom, but it also improves the usability at the same time." — Raschka [RASCHKA-TOOLS].

**Citations**: RASCHKA-TOOLS, LS-TOOLS, LS-PERMISSIONS.
**Image**: Raschka figure 8 (`08-tool-use-flow.png`) OR Latent Space image 01 (tools list) or 06 (permissions).
**Reuse**: new.

---

#### A-19 — Component 4: Context Compaction

- Long contexts are expensive and noisy; coding agents bloat fast via repeated reads, long outputs, logs [RASCHKA-COMPACTION].
- Two strategies: **clip** oversized items, **summarize** older transcript entries, and deduplicate repeated file reads [RASCHKA-COMPACTION].
- The Claude Code leak reveals **five distinct compaction types** across the runtime [LS-COMPACTION].

**Citations**: RASCHKA-COMPACTION, LS-COMPACTION.
**Image**: Raschka figure 10 (`10-context-compaction.png`) OR Latent Space image 05 (5 types of compaction).
**Reuse**: new.

---

#### A-20 — Component 5: Structured Session Memory

- Two storage layers, both on-disk JSON [RASCHKA-MEMORY]:
  - **Working memory**: distilled, small, "what matters now"
  - **Full transcript**: all turns, durable, resumable
- Claude Code's leaked architecture shows a **three-layer memory**: `MEMORY.md` index → topic files → session transcripts, with an "autoDream" consolidation mode for merging and pruning [LS-MEMORY].

**Citations**: RASCHKA-MEMORY, LS-MEMORY.
**Image**: Raschka figure 11 (`11-transcript-and-memory.png`) OR Latent Space image 03 (three-layer memory).
**Reuse**: new.

---

#### A-21 — Component 6: Bounded Subagents

- Delegation parallelizes subtasks: "which file defines X?", "why is this test failing?" [RASCHKA-SUBAGENTS].
- Hard part isn't *spawning* subagents, it's *binding* them: enough context to work, tight enough to not explode [RASCHKA-SUBAGENTS].
- Techniques: read-only mode, recursion depth limits, task scoping [RASCHKA-SUBAGENTS].

> "The tricky design problem is not just how to spawn a subagent but also how to bind one :)." — Raschka [RASCHKA-SUBAGENTS].

**Citations**: RASCHKA-SUBAGENTS.
**Image**: Raschka figure 12 (`12-bounded-subagent.png`).
**Reuse**: new.

---

#### A-22 — The leak in one slide: what Claude Code actually runs

- ~500k lines of code reportedly exposed via source-map inclusion [LS-LEAK].
- Tool inventory (sample): `AgentTool`, `BashTool`, `FileEditTool`, `TodoWriteTool`, `WebFetchTool`, `SkillTool`, `AskUserQuestionTool`, `EnterPlanModeTool`, `TaskStopTool` [LS-TOOLS].
- Unreleased / employee-gated features spotted: `autoDream`, `ULTRAPLAN`, `KAIROS`, `MAGIC_DOCS` [LS-FEATURES].
- Subagents use **prompt caching** for fork-join execution [LS-SUBAGENTS-CACHING].
- Two types of plan mode, five-level permission system, explicit retry + resilience [LS-LEAK].

**Citations**: LS-LEAK, LS-TOOLS, LS-FEATURES, LS-SUBAGENTS-CACHING.
**Image**: Latent Space image 01 (tools list) OR 09 (ULTRAPLAN/KAIROS).
**Reuse**: new.

---

#### A-23 — Agents in the wild: Claude Code, OpenClaw, MiroFish, AutoResearch

> **Fill from**: `session-03/C-agents.md` slides 37-41 (existing example set). Add MiroFish as explicit open-source example composing Raschka's six components on top of CAMEL-AI's OASIS [MIROFISH-REPO].

**Citations**: inherited from `session-03/C` slides 37-41 + MIROFISH-REPO.
**Reuse**: `session-03/C-agents.md` slides 37-41 (hybrid with MiroFish addition).

---

#### A-24 — Takeaway: model vs harness

- Vanilla LLMs are converging in raw capability [RASCHKA-HARNESS].
- The harness is the distinguishing factor [RASCHKA-HARNESS].
- Founder implication: **a thin wrapper over GPT-5 is not your moat.** The system around the model is.

**Citations**: RASCHKA-HARNESS.
**Reuse**: new.

---

### Deck B — Building With AI

#### B-00 — Bridge slide

```
From understanding to shipping.
```

**Reuse**: new (transition).

---

#### B-01 — The Bitter Lesson, for founders

> **Fill from**: `session-04/A-methodologie-projet.md` slide 01 (Bitter Lesson). Translate; keep Sutton citation [BITTER-LESSON].

**Citations**: BITTER-LESSON.
**Reuse**: `session-04/A-methodologie-projet.md` slide 01.

---

#### B-02 — Prompt-based development changes the cost structure

> **Fill from**: `session-04/A-methodologie-projet.md` slide 03 + slide 02 (CV before/after). Keep Andrew Ng citation [NG-GENAI].

**Citations**: NG-GENAI.
**Reuse**: `session-04/A-methodologie-projet.md` slides 02-03.

---

#### B-03 — The GenAI lifecycle: Scope → Build → Evaluate → Deploy

> **Fill from**: `session-04/A-methodologie-projet.md` slides 04-08 (condensed). Translate.

**Reuse**: `session-04/A-methodologie-projet.md` slides 04-08 (condensed to 1 slide).

---

#### B-04 — Baseline first, then iterate

> **Fill from**: `session-04/A-methodologie-projet.md` slides 09-10. Translate, preserve callouts.

**Reuse**: `session-04/A-methodologie-projet.md` slides 09-10.

---

#### B-05 — MVP patterns: 5 ways to validate before you build

> **Fill from**: `session-04/A-methodologie-projet.md` slide 11 (MVP Patterns table). Translate headers, keep MIT Sloan + Google Rules of ML citations [MIT-MVP, GOOGLE-RULES-ML, YC-IDEAS, YC-MVP].

**Citations**: MIT-MVP, GOOGLE-RULES-ML, YC-IDEAS, YC-MVP.
**Reuse**: `session-04/A-methodologie-projet.md` slide 11.

---

#### B-06 — Building an MVP: 3 ingredients + the anti-pattern

> **Fill from**: `session-04/A-methodologie-projet.md` slide 12. Translate. Keep the Gmail anecdote callout.

**Reuse**: `session-04/A-methodologie-projet.md` slide 12.

---

#### B-07 — Rapid agent prototyping (Claude Code as harness)

> **Fill from**: `session-04/A-methodologie-projet.md` slide 13 (Jason Liu). Translate, preserve JXNL citation [JASON-LIU-RAPID-AGENT].

**Citations**: JASON-LIU-RAPID-AGENT.
**Reuse**: `session-04/A-methodologie-projet.md` slide 13.

---

#### B-08 — The 6 pitfalls of AI Engineering (Chip Huyen)

> **Fill from**: `session-04/A-methodologie-projet.md` slide 14. Translate, preserve Chip Huyen citation [CHIP-HUYEN-PITFALLS].

**Citations**: CHIP-HUYEN-PITFALLS.
**Reuse**: `session-04/A-methodologie-projet.md` slide 14.

---

#### B-09 — Progression: Prompting → RAG → Fine-tuning

> **Fill from**: `session-04/A-methodologie-projet.md` slide 15. Translate.

**Reuse**: `session-04/A-methodologie-projet.md` slide 15.

---

#### B-10 — Pricing is being reinvented

> **Fill from**: `session-04/C-business-models.md` slide 01 (seat vs outcome). Translate, preserve Gartner + Intercom citations [GARTNER-PRICING, INTERCOM-FIN].

**Citations**: GARTNER-PRICING, INTERCOM-FIN.
**Reuse**: `session-04/C-business-models.md` slide 01.

---

#### B-11 — Klarna: replace → backlash → rehire

> **Fill from**: `session-04/C-business-models.md` slide 07. Translate, preserve Klarna + Entrepreneur citations [KLARNA-AI-ASSIST, KLARNA-REHIRE]. Keep the *"augmentation > full replacement — 2025's most expensive lesson"* callout.

**Citations**: KLARNA-AI-ASSIST, KLARNA-REHIRE.
**Image**: `session-04/assets/infographics/klarna-timeline_run_20260323_143048_2c1e7c.png` (copy to station-f assets).
**Reuse**: `session-04/C-business-models.md` slide 07.

---

#### B-12 — L'Oréal + Doctolib: augmentation that works

- **L'Oréal** — bought ModiFace (AR/AI beauty), 3× conversion with virtual try-on, €150M Beauty Tech revenue segment [LOREAL-AR].
- **Doctolib** — 1.6M AI consultations, 80M users, **€6.5B valuation** — keeps the doctor in the loop [DOCTOLIB-2024].

> Pattern: AI augments a domain expert, doesn't replace them.

**Citations**: LOREAL-AR, DOCTOLIB-2024.
**Reuse**: `session-04/C-business-models.md` slides 08 + 10 (condensed).

---

#### B-13 — 5 structural trends (the founder cheat sheet)

> **Fill from**: `session-04/C-business-models.md` slide 13. Translate the 5 trends. Keep all citations [EPOCH-INFERENCE, A16Z-BIG-IDEAS, GARTNER-PRICING, BLOOMBERG-APPS, CDI-AI-ACT].

**Citations**: EPOCH-INFERENCE, A16Z-BIG-IDEAS, GARTNER-PRICING, BLOOMBERG-APPS, CDI-AI-ACT.
**Reuse**: `session-04/C-business-models.md` slide 13.

---

#### B-14 — EU AI Act: the one date

- Feb 2025: prohibited practices take effect [EU-AI-ACT-TIMELINE].
- **Aug 2026: high-risk conformity obligations + penalties kick in** [EU-AI-ACT-TIMELINE].
- High-risk categories: employment, credit scoring, health, justice, critical infrastructure [EU-AI-ACT-RISK].
- Penalties: up to **€35M or 7% of global revenue** [EU-AI-ACT-TIMELINE].
- Compliance market estimated **€7.6–31B over 5 years** [CDI-AI-ACT].

> EU AI Act applies to any AI sold in the EU, regardless of where the company is based.

**Citations**: EU-AI-ACT-TIMELINE, EU-AI-ACT-RISK, CDI-AI-ACT.
**Reuse**: `session-05/A-regulation-ethique.md` slides 03-04 (condensed to 1 slide).

---

#### B-15 — Key takeaways

1. **The model is not the product** — the harness around it is [RASCHKA-HARNESS].
2. **Augmentation > automation** — Klarna proved it the expensive way [KLARNA-REHIRE].
3. **Start with a Wizard-of-Oz / Prompt-eng MVP** before you build agents [MIT-MVP, JASON-LIU-RAPID-AGENT].
4. **Aug 2026 is the EU AI Act deadline** — know your risk category [EU-AI-ACT-TIMELINE].
5. **Ship something this week.** Claude Code + CLAUDE.md + 3 tools = an agent prototype.

**Citations**: RASCHKA-HARNESS, KLARNA-REHIRE, MIT-MVP, JASON-LIU-RAPID-AGENT, EU-AI-ACT-TIMELINE.
**Reuse**: new synthesis.

---

#### B-16 — Close

```
Questions.
```

**Reuse**: new.

---

## Citation index

> Format: `[TAG]` · **claim category** · display authority · URL · archive path (relative to repo root) · accessed · verbatim quote (if archived).
> Live URLs are kept when the source is already tracked in the Sorbonne citation pool (previously audited per `docs/references/workflow-citation-audit.md`). New sources (Raschka, Latent Space, MiroFish) have local archive paths.

### New sources (archived locally)

**[RASCHKA-INTRO]** · coding-harness framing · Sebastian Raschka, *Components of A Coding Agent*, Ahead of AI.
URL: https://magazine.sebastianraschka.com/p/components-of-a-coding-agent
Archive: `docs/station-f/sources/raschka-coding-agent/README.md`
Accessed: 2026-04-12
Quote: "In many real-world applications, the surrounding system, such as tool use, context management, and memory, plays as much of a role as the model itself."

**[RASCHKA-AGENT]** · agent/harness glossary · same as above.
Quote: "Agent: a loop that uses a model plus tools, memory, and environment feedback." + "Agent harness: the software scaffold around an agent that manages context, tool use, prompts, state, and control flow."

**[RASCHKA-HARNESS]** · vanilla LLMs converge, harness differentiates · same as above.
Quote: "Since, in my view, the vanilla versions of LLMs nowadays have very similar capabilities […], the harness can often be the distinguishing factor that makes one LLM work better than another."

**[RASCHKA-COMPONENTS]** · 6-component list · same as above.
Quote: Raschka's own code-comment block (archived verbatim): "Six Agent Components — 1) Live Repo Context → WorkspaceContext; 2) Prompt Shape And Cache Reuse → build_prefix, memory_text, prompt; 3) Structured Tools, Validation, And Permissions; 4) Context Reduction And Output Management; 5) Transcripts, Memory, And Resumption; 6) Delegation And Bounded Subagents."

**[RASCHKA-REPO-CONTEXT]** · live repo context component · same as above, §1.
Quote: "The coding agent collects info ('stable facts' as a workspace summary) upfront before doing any work, so that it is not starting from zero, without context, on every prompt."

**[RASCHKA-PROMPT-SHAPE]** · stable prefix + cache reuse component · same as above, §2.
Figure ref: `images/07-stable-prompt-prefix.png`.

**[RASCHKA-TOOLS]** · tool access + validation + permissions · same as above, §3.
Quote: "A plain model can suggest commands in prose, but an LLM in a coding harness should do something narrower and more useful and be actually able to execute the command and retrieve the results." + "The harness is giving the model less freedom, but it also improves the usability at the same time."

**[RASCHKA-COMPACTION]** · context bloat mitigation · same as above, §4.
Quote: "A lot of apparent 'model quality' is really context quality."

**[RASCHKA-CONTEXT]** · same passage as RASCHKA-COMPACTION, cited separately for the big pull-quote slide. Same URL/archive.

**[RASCHKA-MEMORY]** · working memory + transcript · same as above, §5.

**[RASCHKA-SUBAGENTS]** · bounded subagents · same as above, §6.
Quote: "The tricky design problem is not just how to spawn a subagent but also how to bind one :)."

**[LS-LEAK]** · Claude Code source leak overview · swyx (Latent Space), *[AINews] The Claude Code Source Leak*, 2026-04-01.
URL: https://www.latent.space/p/ainews-the-claude-code-source-leak
Archive: `docs/station-f/sources/latent-space-claude-code-leak/README.md`
Accessed: 2026-04-12
Note: article body is paywalled; we cite structural metadata + named artifacts that the archive captures.

**[LS-TOOLS]** · 18+ tool inventory enumerated · same as LS-LEAK. Archived tool list (AgentTool, BashTool, FileReadTool, FileEditTool, FileWriteTool, NotebookEditTool, WebFetchTool, WebSearchTool, TodoWriteTool, TaskStopTool, TaskOutputTool, AskUserQuestionTool, SkillTool, EnterPlanModeTool, ExitPlanModeV2Tool, SendMessageTool, BriefTool, ListMcpResourcesTool, ReadMcpResourceTool).

**[LS-PERMISSIONS]** · 5-level permission system · same as LS-LEAK. Image: `06-permission-system.png`.

**[LS-COMPACTION]** · 5 distinct compaction types · same as LS-LEAK. Image: `05-compaction-types.png`.

**[LS-MEMORY]** · three-layer memory, autoDream consolidation · same as LS-LEAK. Images: `02-memory-architecture.png`, `03-memory-3layer.png`.

**[LS-FEATURES]** · autoDream, ULTRAPLAN, KAIROS, MAGIC_DOCS · same as LS-LEAK. Images: `09-ultraplan-kairos.png`, `10-magic-docs.jpeg`.

**[LS-SUBAGENTS-CACHING]** · subagents use prompt caching for fork-join · same as LS-LEAK.

**[MIROFISH-REPO]** · example open-source agent composing the stack · 666ghj, *MiroFish — A Simple and Universal Swarm Intelligence Engine*, GitHub.
URL: https://github.com/666ghj/MiroFish
Archive: `docs/station-f/sources/mirofish/README.md`
Accessed: 2026-04-12
License: AGPL-3.0. Built on CAMEL-AI's OASIS. Stars at archive: 54,113.

### Reused Sorbonne sources (live URLs, previously audited)

Citations tagged below come from Sorbonne deck footers. Full URL is the one printed in the `<small>Sources: …</small>` line of the cited slide. Re-validation runs via `scripts/check-citations.sh` during the build step. Full quotes are in the source slides.

**[BITTER-LESSON]** · Richard Sutton, *The Bitter Lesson* (2019). http://www.incompleteideas.net/IncIdeas/BitterLesson.html
**[NG-GENAI]** · Andrew Ng, *Generative AI for Everyone*, DeepLearning.AI. https://www.coursera.org/learn/generative-ai-for-everyone
**[MIT-MVP]** · MIT Sloan, *What is a Minimum Viable AI Product?* https://sloanreview.mit.edu/article/what-is-a-minimum-viable-ai-product/
**[GOOGLE-RULES-ML]** · Google, *Rules of ML*. https://developers.google.com/machine-learning/guides/rules-of-ml
**[YC-IDEAS]** · Y Combinator, *Startup Ideas* (YouTube).
**[YC-MVP]** · Y Combinator, *Plan an MVP* (YouTube).
**[JASON-LIU-RAPID-AGENT]** · Jason Liu, *Rapid Agent Prototyping*. https://jxnl.co/writing/2025/09/04/context-engineering-rapid-agent-prototyping/
**[CHIP-HUYEN-PITFALLS]** · Chip Huyen, *AI Engineering Pitfalls*. https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html
**[GARTNER-PRICING]** · Gartner, *AI Pricing Tips*. https://www.gartner.com/en/articles/ai-pricing-tips-control-costs-effectively
**[INTERCOM-FIN]** · Intercom Fin. https://fin.ai/
**[KLARNA-AI-ASSIST]** · Klarna press, *AI Assistant Handles Two-Thirds of CS Chats*. https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
**[KLARNA-REHIRE]** · Entrepreneur, *Klarna CEO Reverses Course*. https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
**[LOREAL-AR]** · L'Oréal Annual Report 2024, Beauty Tech Champion. https://www.loreal-finance.com/en/annual-report-2024/beauty-tech-champion/
**[DOCTOLIB-2024]** · Sifted, *Doctolib Results 2024*. https://sifted.eu/articles/doctolib-results-2024
**[EPOCH-INFERENCE]** · Epoch AI, *LLM Inference Price Trends*. https://epoch.ai/data-insights/llm-inference-price-trends
**[A16Z-BIG-IDEAS]** · a16z, *Big Ideas in Tech 2025*. https://a16z.com/big-ideas-in-tech-2025/
**[BLOOMBERG-APPS]** · Bloomberg, *The Hottest AI Companies Right Now Are Apps*. https://www.bloomberg.com/news/articles/2025-03-06/the-hottest-ai-companies-right-now-are-apps
**[CDI-AI-ACT]** · Center for Data Innovation, *The AI Act's Costs* (PDF). https://www2.datainnovation.org/2021-aia-costs.pdf
**[EU-AI-ACT-TIMELINE]** · EU AI Act timeline + penalties — see `session-05/A-regulation-ethique.md` slide 04 for live citation URLs.
**[EU-AI-ACT-RISK]** · EU AI Act 4 risk levels — see `session-05/A-regulation-ethique.md` slide 03.
**[ANTHROPIC-AGENTS]** · Anthropic, *Building Effective Agents* — preserved from `session-03/C-agents.md` original citations.

## Source archive manifest

```
docs/station-f/sources/
├── raschka-coding-agent/
│   ├── README.md                   (citation-ready archive, 2,588 words)
│   └── images/                     (13 figures)
├── latent-space-claude-code-leak/
│   ├── README.md                   (metadata + section outline + named artifacts)
│   └── images/                     (10 figures)
└── mirofish/
    ├── README.md                   (verbatim English README, 925 words)
    └── images/                     (9 images: logo, 6 screenshots, 2 demo covers)
```

All paths resolve as of 2026-04-12.

## Glossary (technical terms kept in English)

- **LLM / Large Language Model** — the raw model weights that predict next tokens.
- **Reasoning model** — LLM optimized for intermediate reasoning steps and self-verification.
- **Agent** — a loop using a model plus tools, memory, and environment feedback.
- **Agent harness** — software scaffolding around an agent (prompts, tools, state, control flow).
- **Coding harness** — agent harness specialized for software engineering.
- **Context window** — the token budget the model sees on a single call.
- **Prompt caching** — reusing a stable prefix across calls to cut cost/latency.
- **Context compaction** — shortening / summarizing / deduplicating items that go into the prompt.
- **Subagent** — a spawned helper agent bound to a narrower task.
- **MVP** — Minimum Viable Product; smallest artifact that tests the core hypothesis.
- **Wizard of Oz** — MVP pattern where a human simulates the AI behind the scenes.
- **RAG / Retrieval-Augmented Generation** — grounding LLM output in retrieved documents.
- **EU AI Act** — European regulation on AI systems, effective staged 2025–2026+.

## Regeneration prompt

> Copy the block below into a fresh Claude Code session at the root of this repository. It is self-contained: it references only files that exist in this repo. It regenerates `slides/station-f/A-state-of-the-field.md` and `slides/station-f/B-building-with-ai.md` from this spec.

```
You are building two Marp slide decks for a 1-hour Station F talk on April 15 2026.
Repository: Markdowns2Teach. Working directory: /home/ezalos/42/Markdowns2Teach/.

Source of truth: docs/station-f/spec.md (this file). Read it fully.
Audience: startup founders, technically literate.
Language: English.
Theme: station-f (CSS at themes/station-f.css — inherits sorbonne.css).

Tasks:

1. For each slide entry in the "Slide-by-slide content" section of spec.md:
   a) Resolve any "Fill from: <path> slides NN" directives by reading the named
      Sorbonne slide and translating its content to English, preserving ALL
      citation markers [N] AND the `<small>Sources: …</small>` footer URLs.
   b) Assemble the Marp markdown for the slide, using the class hints in the
      spec and the slide-creation standards at docs/references/slide-creation-standards.md.
   c) For new slides (marked "Reuse: new" or using citations tagged
      [RASCHKA-*], [LS-*], [MIROFISH-*]), build the slide from the Citation
      index and the short quotes/figures archived under
      docs/station-f/sources/.

2. Slide frontmatter (both decks):
     marp: true
     theme: station-f
     paginate: true
     header: "Building With AI · Station F · 2026-04-15"
     footer: "Sources multiples · See docs/station-f/spec.md"
   First slide: `<!-- _class: title -->` and `<!-- _paginate: skip -->`.
   Use `<!-- ABOUTME: … -->` twice at the top per repo convention.

3. Numbering: content slides use `# 01 — Title`, `# 02 — Title`, etc. (two-digit,
   em dash). Title and section-divider slides are NOT numbered.

4. Every slide with a data claim MUST carry a `<small>Sources : [Authority](url) · …</small>`
   footer. For new slides citing our archived sources, use the live URL
   (e.g. the Raschka Substack URL) — the local archive is a durability backup,
   not the display link.

5. For images originally archived under docs/station-f/sources/<src>/images/:
   copy the specific files referenced in the spec to
   slides/station-f/assets/<src>/ and reference them with
   `![bg right:55% contain](assets/<src>/<filename>)` or as needed.

6. After writing both deck files, run:
     ./scripts/check-overflow.sh slides/station-f
     ./scripts/check-citations.sh slides/station-f
     make build
   Fix any overflow warnings (split slides if needed). Stop on citation errors.

7. Verify by building:
     make html
     make pptx
   Open the generated HTML locally; confirm no broken images and no font overflow.

Do not introduce any source or citation that is not already in spec.md's
Citation index. If a slide requires a claim that isn't covered, add the claim
to spec.md first (with a new [TAG] entry in the Citation index), then
regenerate.
```

## Execution notes (for the next session)

- Translation rule: keep English technical terms (Supervised Learning, Wizard of Oz, etc.) as-is; translate only surrounding French prose.
- Don't alter source-URL text in `<small>Sources: …</small>` lines — those are authority displays, not translations.
- The 1-hour target is tight. If after generation the deck exceeds 45 slides, cut the MoE/quantization deep-dives from Deck A first, then the 2nd orchestration-details slide if still over.
- If any archived image is visually too detailed for a 1280×720 slide, crop to a focused region and store under `slides/station-f/assets/<src>/<name>-crop.png`.
