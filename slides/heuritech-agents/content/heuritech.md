<!-- ABOUTME: Merged, theory-only content blueprint for the Heuritech talk "AI Agents — From Theory to Loops". -->
<!-- ABOUTME: Built from capgemini latest.md (base) + 2026-06-10-original.md (more-technical) + a new Loops section (PostHog). Practice/sprint content cut; technical framing kept. -->

# AI Agents — From Theory to Loops

> Portable talk content (Louis Develle), technical / theory-only, build-system-agnostic.
> Merged source of truth for the HTML builder. Provenance is tagged per slide in a
> trailing `<!-- provenance: ... -->` comment.
> Merge inputs:
> - BASE: `slides/capgemini-ai-agents/content/latest.md` (38 slides)
> - MERGE-IN: `slides/capgemini-ai-agents/content/2026-06-10-original.md` (37 slides, more technical)
> - NEW: Loops section from PostHog — "Why we're bullish on loops", Ian Vanagas (6 slides)
> Scope: technical audience (Heuritech), theory only. No hands-on, no sprints, no demos-time,
> no take-home. Sprints / knowledge-work practice content removed; the new-hire knowledge-work
> metaphor on the harness slide is re-framed as a purely technical decomposition.

---

## 01 — Cover

**Title:** AI Agents — From Theory to Loops
**Kicker:** Technical Talk · AI Agents

**On-slide content:**
- Understand how AI agents really work, from the agent loop to the harness — then the **loops** that let agents run long-running tasks and run many in parallel.
- Presenter: **Louis Develle**
- Audience: **Heuritech** · technical
- Footer: AI Agents — From Theory to Loops

**Presenter notes:**
> Theory-only technical talk. Promise: a clean mental model of what an agent is, the harness that makes it act, the loops that make it autonomous, and the build method that follows. No hands-on.

<!-- provenance: source: latest s01 (cover retitled, presenter Louis, audience Heuritech, practice-promise removed) -->

---

## 02 — Instructor

**Title:** Your instructor today

**On-slide content:**

*Louis Develle — Research engineer & teacher*
- Created the AI curriculum for the 42 Network, 25,000+ students worldwide
- AI Lead at Station F, Europe's largest startup campus
- Teaches the M2 ML & DeepTech track at the Sorbonne

**Presenter notes:**
> 30 seconds: who runs the talk today. Louis = 42 Network curriculum / Station F / Sorbonne. Instructors = Louis only.

<!-- provenance: source: latest s02 -->

---

## 03 — Agenda

**Eyebrow:** How the talk runs
**Title:** A theory tour of agents

**On-slide content:**
- **State of play** — Why agents, why now: intelligence as a commodity, the numbers, the trajectory, the economics.
- **What an agent is** — The definition, the agent loop, and agent = LLM + harness.
- **The harness in depth** — Each block of the harness: sandbox, instructions, memory, skills, tools (MCP), orchestration, context, permissions, models.
- **Loops** — The theoretical bridge: don't prompt agents to write code, build loops that prompt themselves.
- **The build method** — Clarify, build, evaluate, observe, improve, understand.
- **Advanced cards** — Sovereignty, data hygiene, orchestration patterns, LLM-as-judge, meta-improvement.

**Presenter notes:**
> Theory-only rhythm — no sprints, no build hour, no demos-time. Announce the five movements so the room can follow the arc: state of play → what an agent is → the harness → loops → method → advanced.

<!-- provenance: source: latest s03 (agenda rewritten theory-only; sprints/build/demos removed) -->

---

## 04 — Intelligence is a Commodity

**Eyebrow:** The shift underneath everything
**Title:** Intelligence is now a commodity

**On-slide content:**
- *Until now* — **Buying intelligence meant hiring someone.** Scarce, slow to recruit, one person at a time. Your output scaled with your headcount.
- *Today* — **You buy it like a raw material.** On tap, by the unit, as much as you want. A new input for everything your teams produce.
- Raw intelligence only talks. **An agent is what puts it to work,** acting on the world to deliver value with it. That is what this talk is about.

**Presenter notes:**
> The framing hook: intelligence used to mean hiring, now you buy it like a raw material. Agents are how you act on the world with it.

<!-- provenance: source: latest s04 -->

---

## 05 — Crazy Numbers

**Eyebrow:** Why agents, why now
**Title:** Agents are already doing the work

**On-slide content:**
- **Commit-share progression** (the merged element): 0% → (~1 year) → 4% → (6 weeks) → **10%** "of all public GitHub commits, authored by Claude Code alone, within a year of launch." [1][2][5]
- **10% of all commits** — of all public GitHub commits are now authored by Claude Code, one single agent — a share that jumped from 4% in six weeks. [1][2][5] (SemiAnalysis · CoreMention, Feb–Mar 2026)
- **$2.5B revenue** — annualized revenue for Claude Code alone, less than a year after launch. Value people actually pay for. [3] (VentureBeat, Feb 2026)
- **76% support resolution** — of support conversations resolved autonomously by Intercom's Fin, at $0.99 per resolution, paid only on success. [4] (Intercom, vendor-reported)
- Measured, already-happening numbers, not projections. This is the commodity at work: agents commit code, resolve customers and file briefings in production, every day.

**Image:** ../assets/figures/claudecode-mascot.svg *(small Claude Code mark next to the 10%-of-commits stat)*

**Diagram:** Commit-share progression rail (merged from original s04) — 0% → 4% → 10%, with the two interval labels "~1 year" then "6 weeks", emphasizing the acceleration into the 10% figure.

**Sources:** [1] semianalysis.com · [2] coremention.com · [3] venturebeat.com · [4] fin.ai · [5] anthropic.com

**Presenter notes:**
> 120 seconds. Figures verified June 10, 2026. The merged element: show the commit-share PROGRESSION (0→4%→10%, the last jump in 6 weeks) as the headline, then the revenue + Fin numbers. Caveats out loud: commit share counts public repos + Claude co-author tags only, true AI share is higher (Codex/Copilot/Cursor leave no signature). Fin resolution rate is vendor-defined. Bonus ammo: Anthropic $30B run rate (80x in 27 months), execs claiming 20-90% of code AI-written (Microsoft 20-30% per Nadella, Airbnb ~60%, Anthropic 90%+ per CFO), ~49% of occupations already use Claude for a quarter of their tasks.

<!-- provenance: source: latest s05 + MERGED original s04 (commit-share progression added as a marked Diagram element) -->

---

## 06 — METR Curve

**Eyebrow:** Trajectory
**Title:** Agents run longer and longer on their own

**Image:** ../assets/figures/metr-time-horizon.png

**Diagram:** METR time-horizon chart — "Length of tasks completed autonomously · 50% success" (Source: METR, time-horizon benchmark, "Time Horizon 1.1, 50% success"). Task length completed at 50% success doubles every ~7 months, reaching multi-hour tasks in 2026.

**On-slide content:**
- In 2023, an agent could hold a task for **a few minutes**. Today it holds **hours of autonomous work**.
- A clean exponential: the autonomy window doubles roughly every seven months, **about 3× faster than Moore's Law**, and it has not bent yet. [1][2]

**Sources:** [1] metr.org · [2] arxiv.org/2503.14499

**Presenter notes:**
> METR benchmark, official figure: length of tasks agents complete at 50% success doubles every ~7 months, ~3x faster than Moore's Law. Swap the PNG if METR publishes a newer one before the day.

<!-- provenance: source: latest s06 (+ original s05 "3x faster than Moore's Law" line merged in) -->

---

## 07 — Cost Collapse

**Eyebrow:** Economics
**Title:** The same intelligence, 9× to 900× cheaper every year [1]

**Image:** ../assets/figures/epoch-inference.png

**Diagram:** Epoch AI chart — "Price for the same benchmark score · $ per million tokens" (Source: Epoch AI — log scale). Inference price for a fixed capability level falls 9x to 900x per year across benchmarks.

**On-slide content:**
- Capability climbs while price collapses. What is **premium today is commodity next year**, and open-weights track close behind. [1][2]
- *The takeaway:* "Too hard" or "too expensive" are bad reasons not to start. Build the use case now, time alone takes care of both.

**Sources:** [1] epoch.ai · [2] mistral.ai

**Presenter notes:**
> Epoch AI figure: cost for the same intelligence drops ~10x per year, up to 900x on some benchmarks, open-weights track close behind. Takeaway: 'too hard or too expensive' is a bad excuse, time alone takes care of both.

<!-- provenance: source: latest s07 (+ original s06 open-weights line merged) -->

---

## 08 — Definition

**Eyebrow:** Definition
**Title:** What is an agent? [1]

**On-slide content (revealed fragment by fragment):**
1. An agent is a **system**
2. which uses **tools**
3. to interact **repeatedly**
4. with its **environment**
5. to accomplish its **goal**
- Not a chatbot, not a single prompt. A loop that acts, observes, and acts again until the goal is reached.

**Steps:** (reveal the definition fragment by fragment)
1. An agent is a **system**
2. which uses **tools**
3. to interact **repeatedly**
4. with its **environment**
5. to accomplish its **goal**

**Sources:** [1] anthropic.com

**Presenter notes:**
> The formal definition. Read the five fragments slowly, every part of this talk maps back to it.

<!-- provenance: source: latest s09 -->

---

## 09 — Agent Loop

**Eyebrow:** A simple example
**Title:** One goal, many small steps [1]
*(STEPPED — 10 steps; one Think/Act/Observe beat per click, then Answer.)*

**Diagram:** Loop diagram — Thought ("what next?") → Action ("use a tool") → Observation ("read the result"), cycling "until the goal is reached". A progress rail tracks: Think · Act · Observe · Think · Act · Observe · Think · Act · Observe · Answer.

**Steps:** (reveal in order — 10 steps; Goal + the 3 tools are visible from the start, then one Think/Act/Observe beat per click, then Answer)
1. **Think:** To reach the goal, I should search the web first…
2. **Act:** search_web "best Asian restaurants Paris"
3. **Observe:** result #2: a top-10 of Asian restaurants in Paris
4. **Think:** The right one is probably in that list — let me read it.
5. **Act:** read_url the top-10 article
6. **Observe:** Bim Bim Bap, Châtelet, looks ideal
7. **Think:** Before I recommend it, I should check it's open Tuesday night.
8. **Act:** google_maps "Bim Bim Bap Châtelet" — opening hours
9. **Observe:** open every day of the week
10. **Answer:** Book Bim Bim Bap at Châtelet

**On-slide content:**
- Goal (visible from start): Find an Asian restaurant for Tuesday night in Paris
- Tools (visible from start): search_web · read_url · google_maps
- Think: To reach the goal, I should search the web first…
- Act: search_web "best Asian restaurants Paris"
- Observe: result #2: a top-10 of Asian restaurants in Paris
- Think: The right one is probably in that list — let me read it.
- Act: read_url the top-10 article
- Observe: Bim Bim Bap, Châtelet, looks ideal
- Think: Before I recommend it, I should check it's open Tuesday night.
- Act: google_maps "Bim Bim Bap Châtelet" — opening hours
- Observe: open every day of the week
- **Answer:** Book Bim Bim Bap at Châtelet — open Tuesday night, great reviews, fits your group.

**Sources:** [1] arxiv.org (ReAct, 2210.03629)

**Presenter notes:**
> STEPPED — one beat per click (Think/Act/Observe ×3, then Answer). The loop diagram highlights the current phase; the rail top-right tracks position. Goal + the 3 tools are visible from the start. This is the loop that grounds the whole talk.

<!-- provenance: source: latest s10 (original s08 transcript variant available as an alternate, not merged to avoid duplicate worked example) -->

---

## 10 — Agent = LLM + harness

**Eyebrow:** The anatomy
**Title:** Agent = LLM + harness
*(STEPPED — the harness blocks reveal one at a time, anchoring the slides that follow.)*

**On-slide content:**
- **LLM** — The reasoning engine. Brilliant, but alone it can only talk. **You buy that part; everything else is the harness.**
- The harness, six parts (a model that talks → a system that acts) — each is a slide that follows:
  - **Instructions** — CLAUDE.md, standing instructions read at every session.
  - **Tools** — How it touches the world: CLI, APIs, MCP connectors.
  - **Memory** — What it keeps between sessions, plain files first.
  - **Skills** — Recipes it knows how to follow, plain markdown.
  - **Sandbox** — Where its code runs, and how far it can reach.
  - **Orchestration** — Subagents it briefs, runs and coordinates.
- The harness is what turns a model that talks into a system that acts. [1] **We walk each part in turn.**

**Steps:** (reveal in order — the LLM card, then the six harness parts one at a time, then the closing "harness is their sum" line)
1. **LLM** card visible from start
2. **Instructions** (CLAUDE.md)
3. **Tools** (CLI, APIs, MCP connectors)
4. **Memory** (files kept between sessions)
5. **Skills** (markdown recipes)
6. **Sandbox** (where its code runs)
7. **Orchestration** (subagents); the closing "harness is their sum" line lands

**Sources:** [1] sebastianraschka.com

**Presenter notes:**
> Technical framing — the new-hire / office metaphor is dropped as the frame. The model alone is a brain in a jar; the harness around it makes it an agent. Keep the six-part decomposition intact: instructions, tools, memory, skills, sandbox, orchestration — each is a slide ahead. This is the skeleton of the harness section.

<!-- provenance: source: latest s08 + original s09 (knowledge-work "new hire" metaphor softened to a technical agent=LLM+harness framing; 6-part decomposition kept) -->

---

## 11 — Thinking Models

**Eyebrow:** Settings that matter
**Title:** The model and the brain

**On-slide content:**
- *The model* — Build with the best model available, today Claude Fable 5 leads FrontierCode Diamond, the hardest production-code benchmark. [1] You want to see the ceiling of what is possible, not the average. Cheaper models come later, in production, once your tests can prove they are good enough.
- *Thinking effort* — How long the model reasons before acting. For design and debugging, set it to **max**, you trade minutes for quality.
- The trade-off is honest: more intelligence and more thinking burn more tokens, **your subscription is a budget of intelligence.** Spend it where quality matters, save the cheap settings for routine runs.

**Sources:** [1] llm-stats.com/frontiercode

**Presenter notes:**
> The model and the brain: build with the best model, set thinking effort to max. Cheaper models come later, in production, once tests can prove them. Close on the budget-of-intelligence trade-off. (Lab-only "/fast mode" line dropped — theory-only audience.)

<!-- provenance: source: latest s12 + original s19 (both technical takes; lab-only /fast mode line removed) -->

---

## 12 — Sandbox

**Eyebrow:** Harness · Sandbox · where it acts
**Title:** The sandbox, where it acts

**On-slide content:**
- The code runs **on your machine, scoped to the folder you launch it in** — not in someone else's cloud.
- **Diagram (nested reach):** outer "Your machine" ⊃ middle "Other folders · system · network (*permission required*)" ⊃ inner "The launch folder — the agent's reach" containing project files, `skills/`, `CLAUDE.md`.
- By default it is **scoped to the folder where you launched it** — that folder is its whole reach.
- Anything beyond the folder is a **right you grant explicitly** — which is exactly what the permissions part is about.

**Presenter notes:**
> Where code actually executes: the local machine, scoped to the launch folder = the agent's reach. This is the moment they get that rights exist, prepares the permissions slide. (Starter-repo tree and copy-prompt dropped — theory-only.)

<!-- provenance: source: latest s13 + original s13 (both technical takes; lab starter-repo + Copy-prompt removed) -->

---

## 13 — Preview

**Eyebrow:** Harness · See it run
**Title:** See the agent's work as it happens

**On-slide content:**
1. A live preview panel renders the app as the agent edits it — every change lands in real time.
2. The same panel menu holds **Diff, Terminal, Files, Background tasks and Plan** — the surfaces you watch an agent through.
3. Keeping it open is how you observe an agent at work rather than reading after the fact.

**Image:** ../assets/figures/claude-code-screenshot.png

**Diagram:** The Claude Code app with the top-right panel menu open: Preview, Diff, Terminal, Files, Background tasks, Plan.

**Presenter notes:**
> Technical framing of observability surfaces: Preview / Diff / Terminal / Files / Background tasks / Plan are how you watch an agent act. Kept as a concept slide (not a "click here during the build" instruction).

<!-- provenance: source: latest s14 (re-framed from lab instruction to observability concept) -->

---

## 14 — CLAUDE.md (instructions)

**Eyebrow:** Harness · Instructions
**Title:** CLAUDE.md, standing instructions

**On-slide content:**
- **CLAUDE.md is the standing-instructions file** — read at every session start, global for you or per project. [1]
- The home of everything you would otherwise **repeat in every prompt**: context, rules, conventions, commands.
- Per project, so each agent carries **its own ground truth**, on top of a global one for your machine.
- Example (`radar/CLAUDE.md` — a press-review agent):
  - `# Radar — press review agent`
  - `This repo builds a daily executive press briefing.`
  - `## Rules`
  - `- Sources: at least 3 independent outlets, articles < 7 days old`
  - `- Voice: executive briefing, no jargon, sourced claims`
  - `- Test cases live in tests/, replay them after every change`
  - `## Commands`
  - `- Run the briefing: follow skills/press-briefing`
- *Reference:* Andrej Karpathy publishes his own CLAUDE.md, a great model to steal from.

**Sources:** [1] docs.claude.com

**Presenter notes:**
> CLAUDE.md = standing instructions read at every session start. Use the radar/CLAUDE.md example (rules + commands). Mention global-vs-project split, and Karpathy's published CLAUDE.md as a model to steal from. (Office/exec-team "Paul" example from base dropped in favor of the more technical radar/ example.)

<!-- provenance: source: original s16 (radar/ technical example) + latest s15 (global-vs-project + Karpathy ref) -->

---

## 15 — Memory

**Eyebrow:** Harness · Memory
**Title:** Memory, what it keeps between sessions
*(STEPPED — 4 steps.)*

**Steps:** (reveal in order — 4 steps)
1. The intro line + **Start simple — plain files** (markdown / JSON the agent edits itself)
2. The `memory/MEMORY.md` example file (index up top, one file per fact) + the copy-button memory rule
3. **Scale later — databases** (FTS5 full-text or semantic search, only once files stop being enough)
4. *Why it matters:* written knowledge is the load-bearing asset

**On-slide content:**
- **That experience, the agent writes down and reuses** — start simple, scale only when it earns its place.
- **Start simple — plain files:** Markdown and JSON. Readable, diffable, versionable, and the agent edits them itself. [1]
- Example file `memory/MEMORY.md` (an index up top, detail in one file per fact — loaded on demand):
  - `# Memory index`
  - We contract on the Microsoft suite only, never Google Workspace → it-stack.md
  - Meeting invites to the VP need an agenda and one decision → vp.md
  - Competitor watchlist, agreed Jan 2026 → 3aa91f02.md
- Copy button — the memory rule: *"We operate exclusively on Microsoft / Azure. We CANNOT sign with a counterparty that hosts or routes our data on Google Cloud / Google Workspace — doing so is impossible and deleterious."*
- **Scale later — databases:** full-text search (FTS5) or semantic search, only once plain files stop being enough.
- *Why it matters:* **A culture of written knowledge is the load-bearing asset.** What is written down, the agent reads, reuses, and keeps current.

**Copy button:** the memory rule (text above) — paste as a memory entry. *(Don't display the prompt text on-slide; carry it as a copy button.)*

**Sources:** [1] anthropic.com/engineering

**Presenter notes:**
> Memory = what the agent keeps between sessions. Both technical takes merged: start simple (markdown/JSON, the base's Level-01/02), scale later (FTS5 / semantic, the original's "scale later"). The copy-button memory rule stays. Start dumb: plain files.

<!-- provenance: source: latest s16 + original s12 (both technical takes; "start simple → scale later" from original merged with base's index/levels) -->

---

## 16 — Skills

**Eyebrow:** Harness · Skills
**Title:** Skills, recipes your agent follows

**On-slide content:**
- A skill is **just a markdown recipe** — one folder, one markdown file. Anyone can write one. [1]
- Example file `skills/contract-review/SKILL.md`:
  - name: contract-review
  - description: Review a contract, flag risky clauses, report on one page
  - *(below: loaded on demand)*
  - 1. Read the contract, map the parties and scopes
  - 2. Walk every clause: IP, liability, insurance, data
  - 3. Flag each risk with the clause it comes from
  - 4. Cross-check company memory for conflicts
  - 5. Write a one-page report, risks first
- Second example `skills/translate-document/SKILL.md` (one recipe, five steps): read the file → detect source language from the first 500 characters → translate section by section preserving formatting → write the output suffixed with the target language → report what was done.
- The agent sees **name + description** up front, and loads the steps when relevant (→ context engineering).
- Ready-made libraries exist: **superpowers**, **frontend-design** (claude.com/plugins).
- *Security:* External skills are instructions you didn't write. Read them before installing, same reflex as external tools. [2]

**Sources:** [1] agentskills.io · [2] snyk.io

**Presenter notes:**
> A skill is just a markdown recipe. Both decks' example skills kept (contract-review from base, translate-document from original) — owner trims later. Agent sees only name+description up front, loads the rest on demand (→ context engineering). Security: read external skills before installing. (Live NDA demo removed — theory-only.)

<!-- provenance: source: latest s17 + original s11 (both example skills kept; live "review an NDA" demo removed) -->

---

## 17 — Tools (MCP)

**Eyebrow:** Harness · Tools
**Title:** Tools, how an agent touches the world — and MCP

**On-slide content:**
- *Three ways to plug in:*
  - **CLI** — Anything your terminal can do: scripts, git, files.
  - **API** — Web search, internal services, SaaS endpoints, called directly.
  - **MCP** — A standard plug: one connector per tool, shared by every agent. [1]
- **MCP, taught through two schemas:**
  - **Without MCP · M × N connectors** — every agent wired directly to every tool. N agents, M tools → M × N bespoke integrations, a mesh that grows quadratically.
  - **With MCP · M + N connectors** — agents and tools both wire through a central MCP hub. Each agent speaks MCP once, each tool exposes MCP once → M + N connectors. The standard plug collapses the mesh into a hub.
- *Security:* Every external tool or MCP server runs with your agent's permissions. Default to read-only, treat third-party tools as attack surface, install only what you trust.

**Diagram:** Two graphs side by side — **"Without MCP · M × N connectors"** (every agent wired to every tool, a full mesh) vs **"With MCP · M + N connectors"** (agents and tools both wire through a central MCP hub). These two schemas ARE the teaching content of the slide.

**Sources:** [1] anthropic.com/news (Model Context Protocol)

**Presenter notes:**
> Tools = how an agent touches the world: CLI / API / MCP. Teach MCP via the TWO SCHEMAS (M×N mesh vs M+N hub) — this replaces the base's tool-list / logo-bench entirely. MCP turns M×N integrations into M+N. Voice-over security: external tools and MCP servers run with the agent's permissions, attack surface.

<!-- provenance: source: original s10 (two MCP schemas REPLACE base s18 tool-list/logo-bench) -->

---

## 18 — Orchestration

**Eyebrow:** Harness · Orchestration
**Title:** Orchestration, agents that multiply

**On-slide content:**
- **Subagents** — An agent can staff other agents: brief specialists in parallel, collect their findings, merge. You stay the one giving the goal. [1]
- **On a schedule** — Cron jobs and routines: the same agent runs unattended (a briefing that builds and emails itself; a weekly recap) — the mechanism, shown as concept here.
- The promotion analogy in one line: too competent to do it all alone, so it staffs others.

**Sources:** [1] sebastianraschka.com

**Presenter notes:**
> Orchestration = subagents + scheduled runs. Subagents: brief N specialists in parallel, merge. Schedules/cron: the same agent runs unattended. (Live 3-subagent negotiation demo removed — theory-only; scheduled-run "we set one up at the end" teaser dropped.)

<!-- provenance: source: latest s19 + original s14 (both technical takes; live demo + end-of-lab routine teaser removed) -->

---

## 19 — Context Engineering

**Eyebrow:** Context engineering
**Title:** What the model actually sees

**Build note:** recolour using original s17's palette.

**On-slide content:**
- *The context window* (rebuilt every turn [1]) — four colour-coded blocks plus free space:
  - **System** — CLAUDE.md (project rules & conventions) · Environment (cwd, OS, git state, date) · Skills index (name + description, loaded on demand) · Memory index (one line per fact)
  - **Tools** — search_web(q) → results · fetch_page(url) → page content · read_file(path) → text · edit · bash · … (~18 typed tools)
  - **Conversation** — User (your message) · Thinking (private reasoning) · Tool use (structured call) · Tool result (observation fed back) · Agent (the answer · then repeat × many turns)
  - **Free space** — what is left before the window is full
- *The four ideas:*
  1. **One text, stateless** — The whole thing is rebuilt and re-sent at every single turn. The model remembers nothing by itself.
  2. **Four blocks** — System, tools, conversation, and the free space left. Everything the agent 'is' lives in one of them.
  3. **Progressive disclosure** — Indexes up top, detail on demand. That is exactly the SKILL.md and MEMORY.md you just saw — name and one line each, steps loaded when needed.
  4. **A finite window** — There is a hard size limit, so you manage what earns its place in it.

**Sources:** [1] anthropic.com/engineering

**Presenter notes:**
> The big mental model. ONE text rebuilt & re-sent every turn (stateless). Four colour-coded blocks. Progressive disclosure: the SKILL.md and MEMORY.md they saw are the example — index up top, detail on demand. Finite window → manage what is in it. BUILD NOTE for the HTML builder: recolour this slide using original s17's palette.

<!-- provenance: source: latest s22 + original s17 (build note: recolour with original s17 palette; original's 4-block colour-coded window merged) -->

---

## 20 — Permissions & Auto Mode

**Eyebrow:** Rights
**Title:** Permissions & auto mode

**On-slide content:**
- By default the agent **asks before acting**: every file write, every command. [1]
- **Auto mode** pre-approves actions inside the sandbox, the loop runs uninterrupted.
- Extra rights are granted **in plain language**, in the prompt: "you may write to the reports folder".
- The sandbox is what makes auto mode safe — it keeps an uninterrupted loop contained.
- (App example — permission request: prompt "Draft the briefing and save it to reports/" → "Claude wants to write: reports/briefing-06-18.md" with Allow once / Allow always / Deny; mode: ask ← · plan · auto)

**Sources:** [1] docs.claude.com (iam)

**Presenter notes:**
> By default the agent asks before each action; auto mode pre-approves within the sandbox; extra rights are granted in plain language in the prompt. Sets the autonomy dial. This is the bridge into loops: an uninterrupted loop needs the sandbox + auto mode. (Lab "turn it on now" instruction softened to concept.)

<!-- provenance: source: latest s23 + original s18 (both technical takes; lab "for the lab, turn it on" softened) -->

---

## 21 — Loops · Main

**Eyebrow:** Loops · The thesis
**Title:** Don't prompt agents to write code — build loops

**On-slide content:**
- **The thesis:** Don't prompt agents to write code one task at a time. **Build LOOPS that prompt themselves** — so agents do long-running tasks, and so you can run many of them in parallel.
- Two builders converging on the same idea, independently:
  - **Peter Steinberger (OpenClaw)** — loops as the way to keep an agent productive over long horizons.
  - **Boris Cherny (Claude Code)** — loops built into the harness itself.
- The shift: from "write this for me" (one prompt, one task) to "keep working toward this" (a loop that re-prompts itself until the goal is met).
- This section is the **theoretical bridge** to the build method: once you see loops, the method that follows is how you engineer one well.

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops MAIN — the thesis. Don't prompt agents to write code; build loops that prompt themselves → long-running tasks + parallelism. Steinberger (OpenClaw) and Cherny (Claude Code) both converging on loops, independently. This sets up the four-part loops breakdown and bridges into the build method. Cite PostHog on every loops slide.

<!-- provenance: source: PostHog -->

---

## 22 — Loops · Part 1 — Engineering a loop

**Eyebrow:** Loops · Part 1
**Title:** Engineering a loop — the four ingredients

**On-slide content:**
- A loop has **four ingredients**:
  1. **A Goal** — what the loop is driving toward. *"A loop without a goal is a slop cannon."* The goal is what makes the self-prompting converge instead of wander.
  2. **Context** — the fuel: tools, skills, analytics, errors, memories. Curate it and feed it throughout; the agent fetches more and reacts to it as the loop runs. Context is consumed and replenished, not loaded once.
  3. **Evaluation** — the agent checks itself: tests, evals, metrics, LLM-as-judge. **Agents do the verification, not engineers** — that is what lets the loop run unattended.
  4. **An Agent** — the thing that runs the loop:
     - *Basic:* Claude Code in a `while true` (the "Ralph" pattern), or a `/goal` command.
     - *Advanced:* a purpose-built harness + curated context; a cron pulling product signals → subagents; the loop codegens its own tests.
- **Loop examples** (what people actually run): a **PR babysitter**, a **bug fixer**, a **flaky-test hunter**, a **performance autoresearcher** — Karpathy's autoresearcher fixed a **3-year-old bug** and found an **11% performance** win.

**Diagram:** The four ingredients arranged around the loop — Goal (steering) → Context (fuel) → Agent (engine) → Evaluation (self-check) → back to Goal. Annotate Evaluation with "agent verifies, not the engineer".

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops PART 1 — engineering a loop. The four ingredients: Goal ("a loop without a goal is a slop cannon"), Context (fuel — tools/skills/analytics/errors/memories, curated and fed throughout, agent fetches+reacts), Evaluation (agent self-checks: tests/evals/metrics/LLM-judge — agents verify, not engineers), An Agent (basic: Claude Code while-true/Ralph or /goal; advanced: purpose-built harness + context, cron pulling product signals → subagents, loop codegens its own tests). Name the examples: PR babysitter, bug fixer, flaky-test hunter, performance autoresearcher (Karpathy: 3-yr-old bug + 11% perf).

<!-- provenance: source: PostHog -->

---

## 23 — Loops · Part 2 — Why now

**Eyebrow:** Loops · Part 2
**Title:** Why now — real capability gains

**On-slide content:**
- Loops work **now** because of real capability gains, not hype:
  - **Models are better at long tasks** — METR: Opus 4.6 completes 50% of **12-hour** tasks, ~**6× Opus 4**. The autonomy window is what loops cash in.
  - **Huge tasks already shipped** — a **Stripe codebase migration in a day** (vs ~2 months by hand); **Lovable one-shots apps**.
  - **Loops are built in** — Claude Code `/loop`, automations, the **Ralph plugin**. You no longer hand-roll the loop.
  - **Subagents separate the loop from the work** — the loop driver stays small while subagents do the heavy lifting: saves tokens, prevents context degradation.
  - **Harnesses are maturing** — compaction, skills + MCP, cloud execution. The infrastructure caught up to the idea.

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops PART 2 — why now. It works because of real capability gains: models better at long tasks (METR: Opus 4.6 does 50% of 12-hour tasks, ~6x Opus 4); huge tasks shipped (Stripe migration in a day vs 2 months; Lovable one-shots apps); loops built-in (Claude Code /loop, automations, Ralph plugin); subagents separate loop from work (save tokens, prevent degradation); harnesses maturing (compaction, skills+MCP, cloud execution). Ties straight back to the METR curve from the state-of-play section.

<!-- provenance: source: PostHog -->

---

## 24 — Loops · Part 3 — Self-driving products

**Eyebrow:** Loops · Part 3
**Title:** Self-driving products

**On-slide content:**
- The bigger goal than tokenmaxxing: **the agent prompts itself, and the product improves without input.**
- Product engineers **already run this loop manually**:
  - **Collect data** — analytics + talk to users
  - **Build / ship**
  - **Evaluate**
  - **Repeat**
  - A loop just runs that cycle continuously.
- **Limits (state them plainly):**
  - It is **not eliminating engineering.**
  - It puts the **1% gains on cruise control** — bugs, UX, paper cuts, conversion.
  - It **frees engineers' time** for impactful work.
- What **"self"** means here: autonomy from **user-instruction as the starting point**, not autonomy from the engineer.

**Diagram:** The product-engineering loop — Collect data (analytics + users) → Build / ship → Evaluate → (repeat). Label it "the loop engineers already run by hand; a self-driving product runs it continuously."

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops PART 3 — self-driving products. Bigger goal than tokenmaxxing: agent prompts itself, product improves without input. Product engineers already do this loop manually: collect data (analytics + talk to users) → build/ship → evaluate → repeat. Limits: not eliminating engineering; puts the 1% gains (bugs, UX, paper cuts, conversion) on cruise control; frees time for impactful work. "self" = autonomy from user-instruction as the starting point, NOT from the engineer.

<!-- provenance: source: PostHog -->

---

## 25 — Loops · Part 4 — Code was never the problem

**Eyebrow:** Loops · Part 4
**Title:** Code was never the problem

**On-slide content:**
- The opposition to loops: it **feels like replacement** — work abstracted away from writing code.
- But **product engineers already showed code is a small part** of the job.
- What endures in a loop-driven future is the part that was always the real work:
  - **Direction** — deciding what to build and why.
  - **Taste** — knowing good from good-enough.
  - **Empathy** — understanding the user the loop serves.
- Code was never the problem; abstracting it away just surfaces what mattered all along.

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops PART 4 — code was never the problem. The opposition = feels like replacement / work abstracted from writing code. But product engineers already showed code is a small part. Direction, taste, empathy endure in a loop-driven future. This is the reassurance beat before the synthesis.

<!-- provenance: source: PostHog -->

---

## 26 — Loops · Synthesis

**Eyebrow:** Loops · Synthesis
**Title:** Loops are real industry progress

**On-slide content:**
- Loops are **not a couple of tweets** — they are an **expression of real industry progress**: longer autonomy windows, built-in loop tooling, maturing harnesses, subagents.
- Everything in the harness section feeds a loop: tools, skills, memory, context, orchestration, permissions.
- This is the **foundation for the build method that follows** — the method is how you engineer a loop that actually works.

**Footer / Source:** Source: PostHog — "Why we're bullish on loops", Ian Vanagas

**Presenter notes:**
> Loops SYNTHESIS — loops are an expression of real industry progress (not a couple of tweets). This is the foundation for the build METHOD that follows. Hand off: "now, how do you engineer a loop that works? — the method."

<!-- provenance: source: PostHog -->

---

## 27 — Method Overview

**Eyebrow:** The build method
**Title:** Build agents that actually work

**Diagram:** The spine — 01 Clarify › 02 Draft › 03 Evaluate › 06 Understand. Optional loop hanging off Evaluate: 03 Evaluate › 04 Observe › 05 Improve › back to Evaluate ("Repeat until it is good enough").

**On-slide content:**
- The method, end to end: **Clarify → Draft → Evaluate → Understand**, with an inner **Evaluate → Observe → Improve** loop.
- What you are building: **a skill, or a small collection of skills**, plus the tools it needs and the data it can access.
- This is how you engineer the loop from the previous section so it converges on a goal you can trust.

**Presenter notes:**
> Method overview — USE THE ORIGINAL s21 spine (Clarify › Draft › Evaluate › Understand, with the Evaluate→Observe→Improve loop hanging off). Preferred over base s25's linear four-step. Deliverable = a skill (or a few) + tools + data access. This is the engineering of a loop, made concrete.

<!-- provenance: source: original s21 (USED as the method-overview, preferred over base s25) -->

---

## 28 — Step 1: Clarify the goal

**Section:** Method · Step 1
**Title:** Clarify the goal
**Goal line:** Know what a great result looks like, before a single line is built.

**On-slide content:**
- Run a **deep research** on the task: what separates a great output from an average one.
- Extract the **Pareto**: the 20% of qualities that make 80% of the value.
- Turn them into **binary checks** that sum to a score — your evaluation for the rest of the method.
- It works best on a task **you know how to do well yourself**.
- Example (`research/what-makes-a-great-briefing.md`):
  - `# A great executive press briefing`
  - `## Binary checks (score = sum)`
  - `[ ] ≥ 3 independent outlets per theme`
  - `[ ] Every article less than 7 days old`
  - `[ ] Each claim carries its source`
  - `[ ] One actionable implication per theme`
  - `[ ] Reads in under 3 minutes`

**Presenter notes:**
> Step 1 — Clarify. Deep research → the Pareto of what makes a great output → binary eval criteria. Works best on tasks you know how to do well yourself. (The lab's long deep-research Copy-button prompt is dropped — theory-only; the binary-checks example carries the concept.)

<!-- provenance: source: original s22 + latest s26 (technical clarify; lab deep-research Copy-button prompt removed) -->

---

## 29 — Step 2: First Draft

**Section:** Method · Step 2
**Title:** Get a first draft, A to Z
**Goal line:** A rough version that runs end to end beats a perfect fragment.

**On-slide content:**
- Give the agent the `research.md` from step 1; `/brainstorm` the workflow into simple skill steps.
- Aim for a **minimal but Pareto-efficient first version**: the smallest thing that runs A→Z. Text output only — it renders faster.
- **Wire the tools and data access now,** not later.
- The **evaluation layer is non-negotiable:** build the binary checks in from this very first run.
- *Secrets & blast radius:* no passwords or API keys in the repo; know what your agent can send or delete before you let it run.

**Presenter notes:**
> Step 2 — first draft, A→Z. Give the agent the research .md, /brainstorm the skill steps, wire tools & data NOW, build the binary checks in from run one. Voice-over: secrets & blast radius. Text-only output first. (Lab Copy-button build prompt dropped.)

<!-- provenance: source: original s23 + latest s27 (technical build step; lab Copy-button prompt removed) -->

---

## 30 — Step 3: Evaluate

**Section:** Method · Step 3
**Title:** Evaluate on 3 fresh examples
**Goal line:** The skill must do the work, not the leftovers of your conversation.

**On-slide content:**
- `/clear` or open a fresh session before each test. Otherwise the **context, not the skill,** carries the result — and it "mysteriously" breaks tomorrow.
- Keep your examples in a folder; you will **replay them after every change, forever.**
- Good enough? Move to delivery. Not yet? Next step.
- *Why three test cases:* they cost nothing today and save a paralyzed migration in six months, when a cheaper model shows up.

**Presenter notes:**
> Step 3 — evaluate. /clear or a fresh session before each test, otherwise leftover context does the work and it 'mysteriously' breaks later. 3 fresh examples, kept in a folder to replay forever. This is the agent-does-verification beat from the loops section, made concrete.

<!-- provenance: source: original s24 (+ latest s28 test-and-improve framing) -->

---

## 31 — Step 4: Observability

**Section:** Method · Step 4
**Title:** See inside your agent
**Goal line:** Score every example at once. A criterion that fails across the board is the systematic weakness, not bad luck on one run.

**On-slide content:**
- Ask for a visual dashboard (`/frontend-design`): **criteria down, examples across.**
- Read it **by row** — a red row is a systematic gap. Read it **by column** to spot a broken example.
- The **average is your single number to move;** the red rows tell you where.
- **Diagram:** "radar — evaluation matrix" — criteria (rows) × examples E1–E5 (cols), ✓/✗ cells, per-row pass rate, per-column score, overall average. Criteria: ≥ 3 outlets per theme · Articles < 7 days old · Each claim sourced · 1 implication per theme · Reads in under 3 min.
- Note: "Row 'each claim sourced' is red across the board — that is the bottleneck."

**Presenter notes:**
> Step 4 — Observability (original s25, high-value). See inside: a dashboard of intermediary steps, red/green per criterion, criteria × examples. Red row = systematic gap; column = broken example. The average is the single number to move. This is observability as engineering, not vibes.

<!-- provenance: source: original s25 (INCLUDED — high-value observability insight) -->

---

## 32 — Step 5: Improve one bottleneck

**Section:** Method · Step 5
**Title:** Improve one bottleneck at a time
**Goal line:** Several problems will show up. Pick the most pressing one, ignore the rest.

**On-slide content:**
- Expert on the task? **Try your instinct first** — the change or new step you suspect, before anything else.
- Otherwise, deep-research things to try **on that one problem,** and hand the list to the agent to iterate on autonomously.
- **Validate against your tests.** Found a new failure mode? Add it as a test case.
- **Complexity must earn its place:** a change that doesn't move the tests doesn't stay.
- *Why the discipline:* it feels slow and it is the opposite — each accepted change is proven, so you never re-debug the same thing twice.
- **Diagram:** The inner loop — 03 Evaluate on fresh examples → 04 Observe what fails inside → 05 Improve the one bottleneck. "Repeat until the tests pass."

**Presenter notes:**
> Step 5 — one bottleneck at a time, the most pressing one. Deep-research things-to-try, let the agent iterate autonomously against the tests. Complexity must earn its place. Loop 3→5. This IS the loop's inner cycle.

<!-- provenance: source: original s26 (+ latest s28 improve framing) -->

---

## 33 — Step 6: Understand what you built

**Section:** Method · Step 6
**Title:** Understand what you built
**Goal line:** The agent did the typing. Make sure you still own the thinking.

**On-slide content:**
- **Thinking is not understanding.** A system you can't explain is a system you can't fix or defend.
- Ask the agent to **teach you** what is in place: skills like `teach-me` or `make-me-understand` quiz you progressively.
- Have it **generate diagrams** of the workflow — great to onboard the next person too.
- Example (radar — understanding pass):
  - Prompt: "Teach me how the press-briefing skill works, step by step. Quiz me."
  - "Q1: when an article has no named author, what does the pipeline do with it?"
  - Reply: "It gets dropped at the filter step?"
  - "Almost: it is kept but flagged, the sourcing check is what fails it. Want the diagram of the four steps?"

**Presenter notes:**
> Step 6 — Understand (original s27, high-value). Don't ship what you can't explain. teach-me / make-me-understand skills, generated diagrams. Thinking is not understanding. The taste/direction/empathy from loops Part 4 lives here.

<!-- provenance: source: original s27 (INCLUDED — high-value "understand what you built" insight) -->

---

## 34 — Loop Recap

**Eyebrow:** Recap
**Title:** The method, end to end

**Diagram:** The spine — 01 Clarify → 02 Draft → 03 Evaluate → 04 Observe → 05 Improve → 06 Understand, with the Evaluate → Observe → Improve inner loop highlighted.

**On-slide content:**
- **Clarify** — Deep research, the Pareto, binary checks.
- **Draft** — A minimal A→Z version, tools and eval wired in.
- **Evaluate** — 3 fresh examples, clean context, scored.
- **Observe** — Dashboard the steps, find the red row.
- **Improve** — One bottleneck, proven by the matrix.
- **Understand** — Have it teach you the system.
- Loop: **Evaluate → Observe → Improve** turns until it is good enough.

**Presenter notes:**
> The whole method on one line. Steps 3-5 loop until tests pass. This is the engineered loop, fully assembled — the answer to "how do you build a loop that works".

<!-- provenance: source: original s28 + latest s30 (method recap) -->

---

## 35 — Sovereignty

**Eyebrow:** Data sovereignty
**Title:** The sovereign path exists

**On-slide content:**
- When you industrialize internally, the **sovereign chain is ready:**
  - **01 A model-agnostic agent** — OpenCode, open source, deployable internally, plugs into any provider. (opencode.ai)
  - **02 Sovereign inference** — Self-hosted vLLM, or EU sovereign APIs: Mistral La Plateforme [1], Scaleway [2]. EU-hosted, GDPR, OpenAI-compatible.
  - **03 Open-weight models** — Mistral, Qwen, Gemma — shortlist per use case, runnable locally via Ollama. (ollama run …)
- *Field note:* Seen at a large enterprise: organization policy mandates API keys and blocks local models. Plan for the sovereign-API scenario as much as the local one.

**Sources:** [1] help.mistral.ai · [2] scaleway.com

**Presenter notes:**
> Advanced card. The sovereign path when industrializing: OpenCode (model-agnostic) → vLLM self-hosted or EU APIs (Mistral, Scaleway) → open-weight models (Mistral/Qwen/Gemma, local via Ollama). Field note: a large enterprise mandates API keys and blocks local models.

<!-- provenance: source: original s29 + latest s32 (both technical takes) -->

---

## 36 — Data Hygiene

**Eyebrow:** Data hygiene
**Title:** Four reflexes that age well

**On-slide content:**
- **01 Separate primary from processed** — Primary sources on one side, AI-generated outputs on the other, never mixed. Once they blur, you can't trust either.
- **02 Keep sensitive data out of context** — `.claudeignore` excludes folders from the agent's sight, same spirit as `.gitignore`.
- **03 Read-only by default** — Reference data is mounted read-only, the agent reads it, never rewrites it.
- **04 Mind the destination** — Sensitive code and data don't leave for non-EU clouds — that's what the sovereign path is for.

**Presenter notes:**
> Advanced card. Separate primary sources from AI-processed outputs. .claudeignore for sensitive data, read-only mounts, nothing sensitive to non-EU clouds.

<!-- provenance: source: original s30 + latest s33 (identical technical takes) -->

---

## 37 — Orchestration Patterns

**Eyebrow:** Orchestration patterns
**Title:** Five patterns, endless mileage
*(STEPPED — 5 steps; patterns rise one at a time, in increasing autonomy.)*

**Diagram:** Five canonical Anthropic schemas ("Building Effective Agents", official figures):
- **Prompt chaining** — sequential calls, a gate check between each
- **Routing** — classify first, then send to a specialist
- **Parallelization** — same task split, or voted by several
- **Orchestrator – workers** — the agent decomposes at runtime
- **Evaluator – optimizer** — one generates, one scores, loop

**Image:** ../assets/figures/orch-prompt-chaining.png · ../assets/figures/orch-routing.png · ../assets/figures/orch-parallelization.png · ../assets/figures/orch-orchestrator-workers.png · ../assets/figures/orch-evaluator-optimizer.png

**Steps:** (reveal in order — 5 steps; the schemas rise one at a time, in increasing autonomy, then the takeaway card)
1. **Prompt chaining** (orch-prompt-chaining.png) — sequential calls, a gate check between each
2. **Routing** (orch-routing.png) — classify first, then send to a specialist
3. **Parallelization** (orch-parallelization.png) — same task split, or voted by several
4. **Orchestrator – workers** (orch-orchestrator-workers.png) — the agent decomposes at runtime
5. **Evaluator – optimizer** (orch-evaluator-optimizer.png) — one generates, one scores, loop
6. Takeaway card — "all five are doable with skills, no framework required"

**On-slide content:**
- Anthropic's five canonical patterns, in increasing autonomy. [1] **All five are doable with skills, no framework required.** Start at the top, only climb the ladder when the simpler pattern stops being enough.

**Sources:** [1] anthropic.com/research/building-effective-agents

**Presenter notes:**
> Advanced card, STEPPED — the five Anthropic schemas rise one at a time, in increasing autonomy: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer. All doable with skills, no framework. Evaluator-optimizer is the loop pattern from earlier, formalized.

<!-- provenance: source: original s31 + latest s34 (both technical takes) -->

---

## 38 — LLM as Judge

**Eyebrow:** LLM as judge
**Title:** Never trust one vote

**On-slide content:**
- An LLM judging an output is **noisy:** ask the same judge twice, it changes its mind.
- So sample it **3 or 5 times, an odd number,** and take the majority vote.
- A small **law of large numbers,** for the price of a few extra calls.
- A small model like **Haiku is usually enough:** sharpen the question into a simple, unambiguous criterion before reaching for a bigger model.
- *Always validate the judge:* during observability, check the judge's majority vote against your own labels on your examples. Only trust it past **≥ 80% agreement.** [1]
- **Diagram:** Vote example — "Is this briefing properly sourced?" → ✓ ✓ ✗ ✓ ✗ → ✓ yes (3 / 5). "Five samples, one stable verdict. Use it inside your binary checks whenever a criterion needs judgment."

**Sources:** [1] hamel.dev

**Presenter notes:**
> Advanced card (original s32, high-value). An LLM judge is noisy. Sample 3-5 times (odd number), majority vote. Small law of large numbers. Haiku usually enough; sharpen the criterion first. Validate the judge against your own labels (≥80% agreement). This is the Evaluation ingredient of a loop, done right.

<!-- provenance: source: original s32 (INCLUDED — high-value; richer than base s35) -->

---

## 39 — Meta-Improvement

**Eyebrow:** Meta
**Title:** Agents that improve themselves

**On-slide content:**
- **lessons.md** — Referenced from CLAUDE.md, the agent writes down what it learns: every mistake becomes a rule.
- **Wrap-up skill** — A skill that runs at session end: update the lessons, file the test cases, leave the repo clean.
- **Auto-improve** — Hand the agent its own eval scores and let it iterate on its skills against the tests.
- **Ablation** — Regularly try removing complexity. If the tests still pass without it, it never earned its place.

**Presenter notes:**
> Advanced card (original s33, high-value). lessons.md referenced from CLAUDE.md, wrap-up skill at session end, auto-improve loops, ablation: try removing complexity, keep what survives the tests. This is the self-driving-product loop, scoped to the agent itself — closes the arc back to the loops section.

<!-- provenance: source: original s33 (INCLUDED — high-value; richer than base s36) -->

---

## 40 — Close

**Eyebrow:** The whole arc
**Title:** From the loop, to the harness, to the loops

**On-slide content:**
- One mental model, end to end: an **agent is a loop** (think → act → observe), wrapped in a **harness** (instructions, tools, memory, skills, sandbox, orchestration, context, permissions).
- The frontier is **loops that prompt themselves** — long-running, parallel, self-evaluating — built on real industry progress, not hype.
- The **method** is how you engineer one that converges: clarify → draft → evaluate → observe → improve → understand.
- What endures is **direction, taste, empathy** — code was never the problem.

**Presenter notes:**
> Theory close (NOT take-home / demo). Recap the arc: agent = loop, wrapped in a harness; the frontier is self-prompting loops; the method engineers a loop that converges; direction/taste/empathy endure. End on the through-line, no logistics.

<!-- provenance: source: latest s38 + original s37 (re-framed from take-home logistics into a theory close) -->
