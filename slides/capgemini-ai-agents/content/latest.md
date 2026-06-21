<!-- ABOUTME: Portable teaching content for the "AI Agents & Claude Code — Tech Lab" course (latest version). -->
<!-- ABOUTME: Extracted from a React/TSX deck; build-system-agnostic source of truth for re-rendering. -->

# AI Agents & Claude Code — Tech Lab

> Portable course content (Louis Develle). Build-system-agnostic — the original
> deck was authored in a proprietary React framework; only the teaching content
> (slide copy + presenter notes) is reproduced here. Reusable for any audience.
> Source: ~/Pro/wt-iqdeck @ feat/scroll-nav (5c55c7c) · deck def tech-lab.ts.
> Version: latest (June 17-18 2026 rework, ~38 slides).

---

## 01 — Cover

**Title:** AI Agents Tech Lab
**Kicker:** Executive Lab · AI Agents

**On-slide content:**
- Three hours, hands on. Understand how AI agents really work, then **build your own with Claude Code**, and leave with it running
- (Proof photo: a full room of professionals presenting their AI builds — "Every participant ships")
- Footer: AI Agents Tech Lab

**Presenter notes:**
> Welcome in English. One of 3 labs this morning; ours: AI Agents Tech. Promise: everyone leaves with a working agent project AND a slide-generation system.

---

## 02 — Instructors

**Title:** Your instructor today

**On-slide content:**

*Louis Develle — Research engineer & teacher*
- Created the AI curriculum for the 42 Network, 25,000+ students worldwide
- AI Lead at Station F, Europe's largest startup campus
- Teaches the M2 ML & DeepTech track at the Sorbonne

**Presenter notes:**
> 30 seconds: who runs the lab today. Louis = 42 Network curriculum / Station F / Sorbonne.

---

## 03 — Agenda

**Eyebrow:** How the morning runs
**Title:** Mostly building, briefly talking

**On-slide content:**
- **Understand** (Demos all along) — What agents are and how Claude Code works, everything shown live, never just told.
- **Sprint 1** (10 min · Hands on) — First touch: 80 CVs, one role, you pick the candidates with Claude Code.
- **Sprint 2** (20 min · Your agent) — You build a press-review agent on your own topics, with the method we show you.
- **The build** (1 h · Slide machine) — You leave with a slide-generation system in your company colors, plus a morning routine.
- Around 12:00, demos for the full group. One rule until then: **a finished project beats an impressive one that does not run.**

**Presenter notes:**
> The intro is already done. Announce the rhythm explicitly so nobody is surprised: demos all along, a 10' sprint, a 30' sprint, then a full hour of build. Tease the slide machine now, it keeps the room hooked. 12:30 demos: each lab selects 2 projects for the full group. Finished beats impressive-but-incomplete.

---

## 04 — Intelligence is a Commodity

**Eyebrow:** The shift underneath everything
**Title:** Intelligence is now a commodity

**On-slide content:**
- *Until now* — **Buying intelligence meant hiring someone.** Scarce, slow to recruit, one person at a time. Your output scaled with your headcount.
- *Today* — **You buy it like a raw material.** On tap, by the unit, as much as you want. A new input for everything your teams produce.
- Raw intelligence only talks. **An agent is what puts it to work,** acting on the world to deliver value with it. That is what this morning is about.

**Presenter notes:**
> PF's framing, the hook for non-technicals: intelligence used to mean hiring, now you buy it like a raw material. Agents are how you act on the world with it. Optional color if the room responds: the child analogy — smart at 5, you still teach it tools, skills, priorities.

---

## 05 — Crazy Numbers

**Eyebrow:** Why agents, why now
**Title:** Agents are already doing the work

**On-slide content:**
- **10% of all commits** — of all public GitHub commits are now authored by Claude Code, one single agent — a share that jumped from 4% in six weeks. [1][2][5] (SemiAnalysis · CoreMention, Feb–Mar 2026)
- **$2.5B revenue** — annualized revenue for Claude Code alone, less than a year after launch. Value people actually pay for. [3] (VentureBeat, Feb 2026)
- **76% support resolution** — of support conversations resolved autonomously by Intercom's Fin, at $0.99 per resolution, paid only on success. [4] (Intercom, vendor-reported)
- Measured, already-happening numbers, not projections. This is the commodity at work: agents commit code, resolve customers and file briefings in production, every day.

**Sources:** [1] semianalysis.com · [2] coremention.com · [3] venturebeat.com · [4] fin.ai · [5] anthropic.com

**Presenter notes:**
> 120 seconds on slides 5-7. Figures verified June 10, 2026 (sources: slide0-lecture.md). Caveats to say out loud: commit share counts public repos + Claude co-author tags only, true AI share is higher (Codex/Copilot/Cursor leave no signature). Fin resolution rate is vendor-defined. Bonus ammo if asked: Anthropic $30B run rate (80x in 27 months), execs claiming 50-90% of code AI-written, ~49% of occupations already use Claude for a quarter of their tasks.

---

## 06 — METR Curve

**Eyebrow:** Trajectory
**Title:** Agents run longer and longer on their own

**Diagram:** METR time-horizon chart — "Length of tasks completed autonomously · 50% success" (Source: METR, time-horizon benchmark). Task length completed at 50% success doubles every ~7 months, reaching multi-hour tasks in 2026.

**On-slide content:**
- In 2023, an agent could hold a task for **a few minutes**. Today it holds **hours of autonomous work**.
- A clean exponential: the autonomy window doubles roughly every seven months, and it has not bent yet. [1][2]

**Sources:** [1] metr.org · [2] arxiv.org

**Presenter notes:**
> METR benchmark, official figure (deck-assets): length of tasks agents complete at 50% success doubles every ~7 months. Swap the PNG if METR publishes a newer one before the day.

---

## 07 — Cost Collapse

**Eyebrow:** Economics
**Title:** The same intelligence, 9× to 900× cheaper every year [1]

**Diagram:** Epoch AI chart — "Price for the same benchmark score · $ per million tokens" (Source: Epoch AI — log scale). Inference price for a fixed capability level falls 9x to 900x per year across benchmarks.

**On-slide content:**
- Capability climbs while price collapses. What is **premium today is commodity next year**.
- *The takeaway:* "Too hard" or "too expensive" are bad reasons not to start. Build the use case now, time alone takes care of both.

**Sources:** [1] epoch.ai

**Presenter notes:**
> Epoch AI figure (deck-assets): cost for the same intelligence drops ~10x per year, up to 900x on some benchmarks. Takeaway: 'too hard or too expensive' is a bad excuse, time alone takes care of both.

---

## 08 — LLM + Harness (the new hire)

**Eyebrow:** The anatomy
**Title:** Your agent is a new hire
*(STEPPED — 11 steps; each card flips from its "human" front to its agent equivalent.)*

**On-slide content:**
- **LLM** — The hire arrives brilliant, that part you buy. **Day one is everything else.**

Six onboarding cards (human side → agent equivalent):
- The rulebook (Day one: how we work here, what is expected, what is off-limits.) → **Instructions** — CLAUDE.md, standing instructions read at every session.
- The accesses (Your accounts: Teams, SharePoint, Outlook, the tools of the house.) → **Tools** — How it touches the world: CLI, APIs, MCP connectors.
- The experience (Meeting notes, client quirks, everything you learn on the job.) → **Memory** — What it keeps between sessions, plain files first.
- The training (Competences you build: review a contract, screen CVs, brief the press.) → **Skills** — Recipes it knows how to follow, plain markdown.
- The laptop (Your machine, your folders, IT grants the rest on request.) → **Sandbox** — Where its code runs, and how far it can reach.
- The promotion (One day you stop doing it all yourself, you staff a team.) → **Orchestration** — Subagents it briefs, runs and coordinates.
- Every onboarding step has an exact agent equivalent, and the harness is their sum. [1] **We walk each one this morning, live.**

**Sources:** [1] sebastianraschka.com

**Presenter notes:**
> STEPPED — each advance flips one card from the human side to the agent side. The new-hire analogy is the backbone of the whole morning: rulebook→CLAUDE.md, accesses→tools, experience→memory (BEFORE skills, mirrors the tour), training→skills, laptop→sandbox, promotion→subagents. Take your time, this is the slide that makes the room feel powerful, not small.

---

## 09 — Definition

**Eyebrow:** Definition
**Title:** What is an agent? [1]

**On-slide content (revealed fragment by fragment):**
1. An agent is a **system**
2. which uses **tools**
3. to interact **repeatedly**
4. with its **environment**
5. to accomplish its **goal**
- Not a chatbot, not a single prompt. A loop that acts, observes, and acts again until the goal is reached.

**Sources:** [1] anthropic.com

**Presenter notes:**
> Now that they FEEL what an agent is, the formal definition. Read the five fragments slowly, every demo this morning maps back to it.

---

## 10 — Agent Loop

**Eyebrow:** A simple example
**Title:** One goal, many small steps [1]
*(STEPPED — 10 steps; one Think/Act/Observe beat per click, then Answer.)*

**Diagram:** Loop diagram — Thought ("what next?") → Action ("use a tool") → Observation ("read the result"), cycling. A progress rail tracks: Think · Act · Observe · Think · Act · Observe · Think · Act · Observe · Answer.

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

**Sources:** [1] arxiv.org

**Presenter notes:**
> STEPPED — one beat per click (Think/Act/Observe ×3, then Answer): think → search_web → observe → think → read_url the top-10 → observe → think 'is it open Tuesday?' → google_maps → observe hours → answer. The loop diagram highlights the current phase; the rail top-right tracks position. Goal + the 3 tools are visible from the start.

---

## 11 — Meet Claude Code

**Eyebrow:** The product
**Title:** Meet Claude Code
**Badge:** Live demo

**On-slide content (the 5-minute tour):**
1. Send a prompt, watch it think and act
2. Resume a past session, nothing is lost
3. Attach files with @path
4. Browse the project files from the app
5. The modes menu (auto mode comes after your first sprint)
- (Screenshot: the real Claude Code desktop app — "The real thing — we drive it live on this screen")

**Presenter notes:**
> LIVE DEMO, screen share — the slide shows the real app screenshot, the checklist keeps the tour on rails: send a prompt, resume an old session, attach files with @path, file explorer, the modes menu (keep auto mode for after the CV sprint). Remind: the app hides the folder, show where files live. From here on, every harness block gets its own live demo.

---

## 12 — Thinking Models (The model and the brain)

**Eyebrow:** Settings that matter
**Title:** The model and the brain

**On-slide content:**
- *The model* — Build with the best model available, today Claude Fable 5 leads FrontierCode Diamond, the hardest production-code benchmark. [1] You want to see the ceiling of what is possible, not the average. Cheaper models come later, in production, once your tests can prove they are good enough.
- *Thinking effort* — How long the model reasons before acting. For design and debugging, set it to **max**, you trade minutes for quality. During the lab everything runs at full effort, same logic as the model choice.
- *Fast mode:* Turn **fast mode** on (**/fast**) for the lab, the same top model with faster output, so the live build never waits on you.
- The trade-off is honest: more intelligence and more thinking burn more tokens, **your subscription is a budget of intelligence.** Spend it where quality matters, save the cheap settings for routine runs.

**Sources:** [1] llm-stats.com/frontiercode

**Presenter notes:**
> Moved up, right after meeting Claude Code. The model and the brain: build with the best model, set thinking effort to max, AND turn on fast mode (/fast) for faster output during the live build. Close on the budget-of-intelligence trade-off.

---

## 13 — Sandbox

**Eyebrow:** Harness · 1/6 · Your machine
**Title:** The sandbox, where it acts
**Badge:** Let's set it up · live

**On-slide content:**
- A new hire gets a laptop, not the keys to the building. The code runs **on your machine, scoped to the folder you launch it in** — and that folder is your starter repo.
- **Diagram (nested reach):** Your machine ⊃ Other folders · system · network (*permission required*) ⊃ The launch folder — the agent's reach. Repo tree `lab3-agentic/`:
  - CLAUDE.md — the rulebook, read every session
  - .claude/skills/ — cv-scoring · nda-analysis · press-synthesis…
  - projects/ — the three exercises
  - docs/ — drop your own files here
- Copy-prompt: `You are in your working directory, read docs and install the packages, thanks`
- The code runs **on your machine**, not in someone else's cloud.
- By default it is **scoped to the folder where you launched it** — that folder is its whole reach.
- Everything is pre-wired; drop your own files in **docs/** and the only effort left is the agent itself.
- Anything beyond the folder is a **right you grant explicitly** — the autonomy dial from just before.

**Presenter notes:**
> Harness 1/6 — your machine + the starter repo, set up live. Code runs locally, scoped to the launch folder = the agent's reach. Walk the repo tree (CLAUDE.md, .claude/skills, projects, docs — their files go in docs/), then the copy-prompt that reads docs and installs packages. The Preview slide is next, so end on 'now let's see it run'.

---

## 14 — Preview

**Eyebrow:** Harness · See it run
**Title:** Open the preview
**Badge:** Top-right

**On-slide content:**
1. Click the panel button, top right, then Preview — your app rendered live as the agent edits it.
2. Same menu holds Diff, Terminal, Files, Background tasks and Plan.
3. Keep it open while you build: every change lands in front of you in real time.
- (Screenshot: the Claude Code app with the top-right panel menu open: Preview, Diff, Terminal, Files, Background tasks, Plan)

**Presenter notes:**
> NEW — right after the sandbox. How to actually see the app: click the panel button top-right in Claude Code → Preview (the same menu holds Diff, Terminal, Files, Background tasks, Plan). Keep it open during the build so changes show live. Screenshot is the real menu.

---

## 15 — CLAUDE.md (the rulebook)

**Eyebrow:** Harness · 2/6 · Instructions
**Title:** CLAUDE.md, the rulebook

**On-slide content:**
- Every hire reads the internal rulebook on day one, then never asks those questions again. **CLAUDE.md is that rulebook for your agent.**
- Example file `~/.claude/CLAUDE.md`:
  - `# Who I am` — Paul, member of the executive team.
  - `# How you should behave` — Do not use em-dashes or other AI tells when writing.
  - `# Things you should know` — All our knowledge is on SharePoint, always check there if unsure.
- One file, **read at every session start**, global for you or per project. [1]
- The home of everything you would otherwise **repeat in every prompt**: context, rules, conventions, commands.
- Per project, so each agent carries **its own ground truth**, on top of a global one for your machine.
- *Reference:* Andrej Karpathy publishes his own CLAUDE.md, a great model to steal from. Link in your starter repo.

**Sources:** [1] docs.claude.com

**Presenter notes:**
> Harness 2/6 — Instructions. CLAUDE.md is the agent's rulebook, read at every session start. Walk the Paul/executive-team example: who I am, how to behave (no em-dashes / AI tells), what to know (knowledge lives on SharePoint). Mention global-vs-project split, and Karpathy's published CLAUDE.md as a model to steal from.

---

## 16 — Memory (the experience it builds)

**Eyebrow:** Harness · 3/6 · Memory
**Title:** Memory, the experience it builds
*(STEPPED — 4 steps.)*

**On-slide content:**
- A hire gets better with every meeting: who is picky about what, which rules never bend. **That experience, the agent writes down and reuses** — two rungs, climbed in order.
- **Level 01 · In the moment — Just ask:** Tell it what to keep: "remember Muriel reviews every external mail." It holds that for next time.
- Example file `memory/MEMORY.md` (An index up top, detail in one file per fact — loaded on demand [1]):
  - `# Memory index`
  - We contract on the Microsoft suite only, never Google Workspace → it-stack.md
  - Meeting invites to the VP need an agenda and one decision → vp.md
  - Muriel reviews every external mail, keep them short → muriel.md
- Copy button — the memory rule: *"We operate exclusively on Microsoft / Azure. We CANNOT sign with a counterparty that hosts or routes our data on Google Cloud / Google Workspace — doing so is impossible and deleterious."*
- **Level 02 · .txt & .md — Write it down:** Plain files it edits itself: readable, diffable, versionable — an index up top, one short file per fact, loaded on demand.
- *Why it matters:* **A culture of written knowledge is the load-bearing asset.** What lives only in someone's head, the agent can't use; what is written down, it reads, reuses, and keeps current.

**Sources:** [1] anthropic.com

**Presenter notes:**
> Harness 3/6 — Memory = the experience a hire builds. Demo cue: record live 'we operate exclusively on Microsoft / Azure'. New: a copy button on the slide pastes that exact memory rule. Tell them to keep it in mind — it fires during the skill demo, next. Start dumb: markdown files.

---

## 17 — Skills (the training you give it)

**Eyebrow:** Harness · 4/6 · Skills
**Title:** Skills, the training you give it
**Badge:** Let's try it · live: review an NDA

**On-slide content:**
- You train a hire to review contracts the firm's way. **For the agent, that training is a markdown recipe.**
- Example file `skills/contract-review/SKILL.md` (One folder, one markdown file. That is a skill.):
  - name: contract-review
  - description: Review a contract, flag risky clauses, report on one page
  - *(below: loaded on demand)*
  - 1. Read the contract, map the parties and scopes
  - 2. Walk every clause: IP, liability, insurance, data
  - 3. Flag each risk with the clause it comes from
  - 4. Cross-check company memory for conflicts
  - 5. Write a one-page report, risks first
- Copy the NDA review prompt: `/nda-analysis review @demos/nda-review/contracts/sample-nda.md`
- A skill is **just a markdown recipe**, anyone in this room can write one. [1]
- The agent sees **name + description** up front, and loads the steps when relevant.
- Ready-made libraries exist: **superpowers**, **frontend-design**, **knowledge-work**.
- *Security:* External skills are instructions you didn't write. Read them before installing, same reflex as external tools. [2]

**Sources:** [1] agentskills.io · [2] snyk.io

**Presenter notes:**
> Harness 4/6 — Skills = the training you give a hire. LIVE: run the contract-review skill on an NDA → step 4 cross-checks memory → the Microsoft-only rule fires and the conflict is flagged. The memory×skill crossover IS the wow moment, rehearse it. Plugins to name: superpowers, frontend-design, knowledge-work.

---

## 18 — Tools (how an agent touches the world)

**Eyebrow:** Harness · 5/6 · Tools
**Title:** Tools, how an agent touches the world
**Badge:** Let's try it · live: read a Notion page

**On-slide content:**
- Day one, your hire gets their accesses, Teams, SharePoint, Outlook. **Same move for your agent: you hand it tools.**
- *Three ways to plug in:*
  - **CLI** — Anything your terminal can do: scripts, git, files.
  - **API** — Web search, internal services, SaaS endpoints, called directly.
  - **MCP** — A standard plug: one connector per tool, shared by every agent.
- *Tools you could connect today:*
  - Outlook — Read & triage mail · Official M365 connector [2] · **read-only**
  - Tavily Search — Live web search & extract · Official MCP · claude mcp add [3]
  - SharePoint — Search docs & sites · Official M365 connector [2]
  - Notion — Read & write pages · Official Notion MCP server [4]
  - Teams — Read channels & chats · Official M365 connector [2]
  - Each one is proven by a real integration, an official connector or MCP server, not a promise. The footnote links the proof.
- *Security:* Every external tool or MCP server runs with your agent's permissions. Default to read-only, treat third-party tools as attack surface, install only what you trust.

**Sources:** [1] anthropic.com · [2] support.claude.com · M365 connector (read-only) · [3] github.com/tavily-ai/tavily-mcp · [4] github.com/makenotion/notion-mcp-server

**Presenter notes:**
> Harness 5/6 — Tools, right after Skills (a skill reaches for tools). Concrete connectors an exec would wire to Claude Code: Outlook (read-only), Tavily, SharePoint, Notion, Teams, each with its MCP status + a source. Optional LIVE Notion-MCP demo. Voice-over security: external tools run with the agent's permissions, default read-only.

---

## 19 — Orchestration (The promotion)

**Eyebrow:** Harness · 6/6 · Orchestration
**Title:** The promotion

**On-slide content:**
- *Your hire — Too good to do it all alone:* Tools mastered, experience built, skills sharp. The next step you give them is a team: they stop producing everything themselves and start delegating.
- *Your agent — Subagents:* An agent can staff other agents: brief three specialists in parallel, collect their findings, merge. You stay the one giving the goal. [1]
- Live now: **three subagents prepare a negotiation**, one on tech news, one on commercial moves, one on product, one hook sentence each.

**Sources:** [1] sebastianraschka.com

**Presenter notes:**
> Harness 6/6 — the promotion: too competent to do it all alone, so it staffs others. LIVE: 3 parallel subagents prepare a negotiation — tech news, commercial moves, product news of the counterparty, one hook sentence each. NO routines here (they close the morning).

---

## 20 — Prompt Structure (a good prompt is a good brief)

**Eyebrow:** Talking to your agent
**Title:** A good prompt is a good brief

**On-slide content:**
- *The four parts:*
  - **Context** — What the intern needs to know before starting: who it is for, what exists already.
  - **Task** — The one thing you want done, stated plainly.
  - **Guidelines** — How you like it done: tone, format, sources, examples.
  - **Constraints** — The hard lines: deadline, length, what must not change.
- *One real brief, annotated:*
  - Context: this summary goes to an executive team, they read it on their phone between two meetings.
  - Task: summarize the attached 40-page report.
  - Guidelines: lead with the three decisions to make, plain business language, one source per claim.
  - Constraints: one page max, nothing confidential quoted verbatim.
- That is all prompting is: **briefing a very fast intern.** The structure is a habit, not a ritual, skip it when the ask is obvious.

**Presenter notes:**
> Moved to the END of the harness — the good-prompt recap once all six parts are seen. Prompting = briefing an intern: context · task · guidelines · constraints, then the annotated example. Say it: a good habit, not a ritual.

---

## 21 — CV Sprint (Sprint 1)

**Eyebrow:** Sprint 1 · Hands on
**Title:** 80 CVs, 3 candidates, 10 minutes

**On-slide content:**
- **The pile** (1-talent-cv-scoring/data/cvs/) — 80 real sales CVs, already in your starter folder.
- **The role · Sales Account Executive** (…/data/jobs/sales-account-executive.md) — You are hiring a Sales Account Executive — not a Head of Sales. The job description is in the same project. Read it, or have Claude read it.
- **The ask** (/cv-scoring) — With Claude Code, pick the 3 candidates you would actually interview. Try the cv-scoring skill: point it at the job description and the CVs folder.
- (10-minute countdown timer.)

**Presenter notes:**
> SPRINT 1 — click Start on the 10' timer (it survives navigating away). 80 sales CVs + the job description for a Sales Account Executive (file is projects/1-talent-cv-scoring/data/jobs/sales-account-executive.md). Say the role out loud. They use the /cv-scoring skill: point it at the job description + the CVs folder (data/cvs). Find your 3 candidates. Debrief: criteria matrix, only ~15 CVs pass everything. Dataset: Kaggle resumes, pre-loaded by IT.

---

## 22 — Context Engineering (what the model actually sees)

**Eyebrow:** Context engineering
**Title:** What the model actually sees

**On-slide content:**
- *The context window* (rebuilt every turn [1]) — three zones:
  - **System** — CLAUDE.md · environment info; Skills index — name + description only; Memory index — one line per fact
  - **Tools** — search_web(query) → results; fetch_page(url) → content; read_file(path) → text …
  - **Conversation** — Your message; Thinking · tool call · tool result (× many); Agent answer · your next message
  - Free space before the window is full
- *Four ideas:*
  1. **One text, stateless** — The whole thing is rebuilt and re-sent at every single turn. The model remembers nothing by itself.
  2. **Three zones** — Instructions, tools, conversation. Everything the agent 'is' lives in one of them.
  3. **Progressive disclosure** — Indexes up top, detail on demand. That is exactly the SKILL.md and MEMORY.md you just saw, name and one line each, steps loaded when needed.
  4. **A finite window** — There is a size limit, so you manage what earns its place in it.

**Sources:** [1] anthropic.com

**Presenter notes:**
> The big mental model. ONE text rebuilt & re-sent every turn (stateless). Three zones. Progressive disclosure: the SKILL.md and MEMORY.md they saw are the example — index up top, detail on demand. Finite window → manage what is in it. Say the basics slowly: every call re-sends everything relevant; that is the harness's job.

---

## 23 — Permissions & Auto Mode

**Eyebrow:** Rights
**Title:** Permissions & auto mode

**On-slide content:**
- By default the agent **asks before acting**: every file write, every command. [1]
- **Auto mode** pre-approves actions inside the sandbox, the loop runs uninterrupted.
- Extra rights are granted **in plain language**, in the prompt: "you may write to the reports folder".
- *For the lab:* turn auto mode on. The sandbox keeps it contained, and the build flows much better.
- (App example — permission request: prompt "Draft the briefing and save it to reports/" → "Claude wants to write: reports/briefing-06-18.md" with Allow once / Allow always / Deny; mode: ask · plan · auto ←)

**Sources:** [1] docs.claude.com

**Presenter notes:**
> Permissions & auto mode — moved here, just before the build sprints. By default the agent asks before each action; flip auto mode on (LIVE) to pre-approve within the sandbox; extra rights are granted in plain language in the prompt. Sets the autonomy dial before they build.

---

## 24 — Press Sprint (Sprint 2)

**Eyebrow:** Sprint 2 · Your agent · 20 min
**Title:** Build your press agent

**On-slide content:**
- **Your topics** — A client, a competitor, a deal on the market, a technology you track. Your briefing, not ours.
- **The method, end to end** — The live build you are about to run with us: clarify, build, then test and improve until the checks pass.
- **If you finish** — Set the routine: your briefing lands in your inbox every morning. We help table by table.
- (20-minute countdown timer, +5 min extend.)

**Presenter notes:**
> Before the method walk: name the thing we build together — the Press Review agent — live, while the method is shown step by step on the next slides. Free topic, their folder; co-instructors roam to unblock. The later deck sprint runs on this agent's output.

---

## 25 — Method Overview (the build method)

**Eyebrow:** The build method
**Title:** Build agents that actually work

**Diagram (MethodCycle):** Four linear steps joined by arrows —
01 Clarify (research, success criteria) → 02 Build (A→Z, tools wired) → 03 Test and improve (test → investigate → improve) → 04 Deliver value (a deck, or your use case).

**On-slide content:**
- We build a **Press Review agent live, step by step**, you follow along. Then you run the same method on your own project.
- What you are building: **a skill, or a small collection of skills**, plus the tools it needs and the data it can access.

**Presenter notes:**
> Transition to build. We do the method LIVE on the Press Review agent, step by step — then they redo it. Three steps now: Clarify → Build → Test and improve, then Value delivery. The diagram is linear, the only loop is inside step 3.

---

## 26 — Step 1: Clarify the goal

**Section:** Method · Step 1 of 4
**Title:** Clarify the goal
**Goal line:** Know what a great result looks like, before a single line is built.

**On-slide content:**
- Use a **deep research** to fully understand your subject and make the **success criteria** clear, you know exactly when the task is complete.
- It works best on a task **you know how to do well yourself**.
- *Where this runs:* In the Claude app (deep research), not Claude Code. It runs long, so don't wait for it live, ours is pre-run and you copy it on the next slide. The output feeds every next step.
- Copy the research prompt (the deep-research brief, pasted into the Claude app, not Code):

> As a non technical person, I will create an agent system with claude code to do the following task:
>
> Press briefing, to understand what are the AI initiatives and projects ongoing among my company's competitors such as: Deloitte, PwC, EY, Accenture, ...
>
> I want you to deep-research about this task on two different axis:
>
> - What are the strongest fundamentals to achieve this task (the 20% of effort that produces 80% of the value)? I'm especially keen on using widely recognized frameworks that could be applied.
> - My agent will iterate autonomously on making this task better, so I will need an excellent evaluation put in place. I'm looking for a sum of binary evaluation criteria. This applies to the complete workflow, as well as to each intermediate step if relevant.
>
> To tell you a bit more about myself, I'm a senior executive on the executive team of my company.
>
> Do not hesitate to ask me questions to better understand how this task is useful to me and context about my work so you can deliver the maximum possible value with your deep-research.

**Presenter notes:**
> Step 1 — Clarify. Copy buttons: the research prompt, and the pre-run deep research (Markdown). Say it: deep research runs in the Claude APP, outputs a .md we feed to the code; make the success criteria explicit. Works best on tasks you know how to do well yourself.

---

## 27 — Step 2: Build the skill and use it

**Section:** Method · Step 2 of 4
**Title:** Build the skill and use it
**Goal line:** Turn the research into a first skill that runs end to end.

**On-slide content:**
- Copy the prompt to create the first draft version of your skill, **press-review**, by leveraging the deep research we just did.
- Copy button: "Don't wait for hours · copy the deep research" (pastes the pre-run deep-research Markdown — see Step 1's deep-research output, reproduced in full at the end of this file under *Appendix: Step 1 pre-run deep research*).
- It asks where your **deep-research file** is, then turns it into the most minimal MVP.
- It wires the **tools and data access** now, and picks three concrete tests to evaluate the skill.
- Then it **builds it and runs it**, A to Z.
- Copy the build prompt:

> Where is the deep-research file for this task? Tell me the path (or paste it), and read it first.
>
> Then /brainstorming a skill called press-review from that research: the most minimal MVP that can be evaluated against the binary checks in the document. Wire the tools and data access it needs now (web search, the test folder).
>
> You must choose three concrete tests that will be used to test and evaluate the skill. Make it easily retestable.
>
> Then build it and run it.

**Presenter notes:**
> Step 2 — Build the skill and use it. Copy the build prompt: it asks where the deep-research file is, then /brainstorming the minimal MVP against the binary checks, wires tools & data, chooses 3 concrete tests, builds and runs it. Slide is deliberately simple now (no terminal/secrets box).

---

## 28 — Step 3: Test and improve

**Section:** Method · Step 3 of 4
**Title:** Test and improve
**Goal line:** Judge the output you see, push the fix into the skill, re-run, repeat until it's great.

**On-slide content:**
- Use the skill to improve your **output** and your **workflow**.
- It shows you the rendered output in the **live preview** and asks what's weak, in plain language, no jargon.
- You react with your taste, it pushes the fix **into the skill** (not the one-off output), then re-runs so you re-review.
- Loop until you are happy, every run gets better and the improvement **survives the next one**.
- *Install the skill:* Copy it into your workspace at `.claude/skills/refine-from-preview/SKILL.md`, then start a **new session** so the `/refine-from-preview` command shows up.
- Copy button: "Copy the refine-from-preview skill" (the full SKILL.md is reproduced at the end of this file under *Appendix: refine-from-preview skill*).

**Presenter notes:**
> Step 3 — Test and improve (merged test/observe/fix). Inner loop: test on 3 fresh examples (/clear first) → investigate the red checks → improve one bottleneck → repeat until green. Copy the test-and-improve SKILL (the instructor provides the final skill to paste in). /teach to understand the agent.

---

## 29 — Step 4: Deliver value

**Section:** Method · Step 4 of 4
**Title:** Deliver value
**Goal line:** You have the whole method and the controls. You're there, now make it something you can show.

**On-slide content:**
- Build a deck with the **frontend-design** and **brainstorming** skills, no special generator needed.
- Then run **the same method on it**, clarify, build, test and improve, until it is presentable.
- Free to choose: a deck, or **any subject you care about**, the methodology is the same.
- Copy the deck prompt:

> /frontend-design use the result from the press briefing to generate a beautiful corporate deck, branded with your company look. The graphic chart is in @projects/3-deck-pptx-creation/brand/company-brand.md
> When the code is generated, you can use the boilerplate in @web/app/deck if useful.

**Presenter notes:**
> Value delivery (ex 'Understand what you built'). Build a deck with frontend-design + brainstorming, no special generator, then refine it with the method. Tell them they're there: they have the method and the controls. Free to pick a deck or any use case they care about.

---

## 30 — Loop Recap (the method, end to end)

**Eyebrow:** Recap
**Title:** The method, end to end

**Diagram (MethodCycle):** 01 Clarify → 02 Build → 03 Test and improve (test → investigate → improve) → 04 Deliver value.

**On-slide content:**
- Clarify and build once, then **test and improve, turning until every check is green**, before value delivery. This is your map for the next sprint.

**Presenter notes:**
> The method end to end: clarify and build once, then test and improve until every check is green, before value delivery. This is their map for the sprint.

---

## 31 — Deck Sprint (The build)

**Eyebrow:** The build · ~1 h before the demos
**Title:** Generate company-grade decks

**On-slide content:**
- (60-minute countdown timer, +5 min extend.)
- 01 Build it with frontend-design and brainstorming.
- 02 Refine it with the method you just learned.
- 03 Make it presentable, then present it.
- **We roam the room to help you build your tool**, then around 12:00, the demos. Going further, table by table: data sovereignty, data hygiene, orchestration patterns, LLM as judge, auto-improve — slides ready if the room wants them.

**Presenter notes:**
> THE BUILD — ~1 h before the demos. Build the deck with frontend-design + brainstorming, then refine with the method. Insist on the demo. We roam table by table to help build the tool of their dreams; free choice of use case (advanced tables can take a precise subject). 12:30 demos. Joker slides ready if the room is strong.

---

## 32 — Sovereignty (Joker card)

**Eyebrow:** Data sovereignty
**Title:** The sovereign path exists

**On-slide content:**
- This morning we use the **best models at full effort**, you should see the ceiling. When you industrialize internally, the sovereign chain is ready:
  - **01 A model-agnostic agent** — OpenCode, open source, deployable internally, plugs into any provider. (opencode.ai)
  - **02 Sovereign inference** — Self-hosted vLLM, or EU sovereign APIs: Mistral La Plateforme, Scaleway. EU-hosted, GDPR, OpenAI-compatible. [1][2] (mistral · scaleway)
  - **03 Open-weight models** — Mistral, Qwen, Gemma — shortlist per use case, runnable locally via Ollama. (ollama run …)
- *Field note:* Seen at a CAC40 client: organization policy mandates API keys and blocks local models. Plan for the sovereign-API scenario as much as the local one.

**Sources:** [1] help.mistral.ai · [2] scaleway.com

**Presenter notes:**
> JOKER CARD (this and the next 4): only if the room is strong or asks. Theory, one slide: lead models today for the ceiling; the sovereign path when industrializing: OpenCode → vLLM self-hosted or EU APIs (Mistral, Scaleway) → open-weight models. Field note: a CAC40 client mandates API keys and blocks local models.

---

## 33 — Data Hygiene

**Eyebrow:** Data hygiene
**Title:** Four reflexes that age well

**On-slide content:**
- **01 Separate primary from processed** — Primary sources on one side, AI-generated outputs on the other, never mixed. Once they blur, you can't trust either.
- **02 Keep sensitive data out of context** (.claudeignore) — .claudeignore excludes folders from the agent's sight, same spirit as .gitignore.
- **03 Read-only by default** — Reference data is mounted read-only, the agent reads it, never rewrites it.
- **04 Mind the destination** — Sensitive code and data don't leave for non-EU clouds, that's what the sovereign path is for.

**Presenter notes:**
> Separate primary sources from AI-processed outputs. .claudeignore for sensitive data, read-only mounts, nothing sensitive to non-EU clouds.

---

## 34 — Orchestration Patterns

**Eyebrow:** Orchestration patterns
**Title:** Five patterns, endless mileage
*(STEPPED — 5 steps; patterns pop one at a time, left to right, in increasing autonomy.)*

**Diagram:** Five Anthropic schemas (official figures):
- Prompt chaining — fixed steps, gated
- Routing — one call picks the lane
- Parallelization — you decide the fan-out
- Orchestrator – workers — the agent staffs the work
- Evaluator – optimizer — one proposes, one judges

**On-slide content:**
- Anthropic's five canonical patterns, in increasing autonomy. [1] **All five are doable with skills, no framework required.**

**Sources:** [1] anthropic.com

**Presenter notes:**
> STEPPED — the five Anthropic schemas pop one at a time, left to right, in increasing autonomy: prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer. All doable with skills, no framework.

---

## 35 — LLM as Judge

**Eyebrow:** LLM as judge
**Title:** Never trust one vote

**On-slide content:**
- An LLM judging an output is **noisy**: ask the same judge twice, it changes its mind.
- So sample it **3 or 5 times, an odd number**, and take the majority vote. [1]
- A small **law of large numbers**, for the price of a few extra calls.
- (Worked example: "Is this briefing properly sourced?" → votes ✓ ✓ ✗ ✓ ✗ → ✓ yes (3 / 5). Five samples, one stable verdict. Use it inside your binary checks whenever a criterion needs judgment.)

**Sources:** [1] hamel.dev

**Presenter notes:**
> An LLM judge is noisy, it changes its mind. Sample 3-5 times (odd number), majority vote. Small law of large numbers.

---

## 36 — Meta-improvement (agents that improve themselves)

**Eyebrow:** Meta
**Title:** Agents that improve themselves

**On-slide content:**
- **Auto-improve** — Hand the agent its own eval scores and let it iterate on its skills against the tests. Your press agent already has the evals, you can switch this on today.
- **Wrap-up skill** — A skill that runs at session end: write down what was learned, file the test cases, leave the repo clean.
- **Ablation** — Regularly try removing complexity. If the tests still pass without it, it never earned its place.

**Presenter notes:**
> lessons.md dropped (too abstract for this room). Auto-improve: their press agent already has evals, they can switch it on today. Wrap-up skill at session end. Ablation: try removing complexity, keep what survives the tests.

---

## 37 — Demo Time

**Eyebrow:** ~12:00 · all labs reunite
**Title:** Demo time

**On-slide content:**
- Each lab selects **2 projects**, presented live to the full group.
- **A finished project beats an impressive one that does not run.** Scope tight, run it end to end twice before you raise your hand.
- (Photo: a full room watching live demos — "Live demos, full room — the best part of the day")

**Presenter notes:**
> 12:30 sharp. Each lab selects 2 projects, presented to the full group. A finished project beats an impressive incomplete one, scope accordingly.

---

## 38 — Take Home

**Eyebrow:** Before you go
**Title:** Take it home

**On-slide content:**
- **Set the routine, now** — Your press briefing emails itself every morning at 8. We configure it together before you leave.
- **It all runs on your machine** — Everything you built today is yours: keep iterating, and the sovereign path is there when you industrialize.
- **We stay in the loop** — Questions next week, next quarter: reach out, we answer.
- Thank you
- (Photo: a cohort after a build day — "See you at the next build")

**Presenter notes:**
> Close the loop from the orchestration slide: set up a Routine live, the press briefing emails itself every morning. Everything they built runs on their machine. Stay available for follow-up questions.

---

# Appendix: Step 1 pre-run deep research

> Verbatim Markdown copied by the "copy the deep research" button on Step 2 (lives with Step 1 as `deep-research.md`). This is the pre-run deep-research output the build prompt consumes.

# Building an Autonomous Competitive-AI Intelligence Memo Agent for an Executive Team: Frameworks and Evaluation Design

## TL;DR
- **Axis 1 (Fundamentals):** Anchor the agent on four widely recognized, citable frameworks — the **Competitive Intelligence Cycle** (process), **Porter's Four Corners Model** (competitor analysis), the **Minto Pyramid Principle / BLUF** (executive writing), and the **Admiralty/NATO source-reliability code** (verification). The genuine 80/20 is a tight competitor-by-angle matrix + a "what changed since last period" delta + an explicit "implications for [Company]" section + graded source citations.
- **Axis 2 (Evaluation):** Use a **rubric of atomic binary (pass/fail) criteria** scored by an LLM-as-judge, decomposed across the five workflow steps plus the final memo. Binary checklists outperform Likert scales for reliability, and per-criterion decomposition mirrors the HealthBench/PaperBench rubric approach. Below are ~45 ready-to-drop binary criteria.
- **Decision:** Build the memo template around a fixed one-page skeleton (BLUF → 4-angle competitor matrix → what-changed delta → implications → watch-list, with graded sources). Gate the agent behind the binary rubric and a hard "every claim carries a verifiable, dated citation" rule — the single most important control, given that a peer firm (Deloitte) has already suffered two public hallucination failures in exactly this kind of work.

## Key Findings

1. **A small number of established frameworks cover the whole task.** Competitive intelligence, intelligence-community tradecraft, and consulting communication have each produced a canonical method. You do not need novelty; you need disciplined application of Porter, Heuer, Minto, and the Admiralty code.
2. **Binary criteria are the consensus best practice for LLM-as-judge.** Multiple practitioner and academic sources converge: yes/no checks are more reliable and consistent than 1–5 or 1–100 scales, and decomposing into single-criterion judgments ("don't confuse your judges") improves accuracy.
3. **The judge itself must be de-biased.** Position, verbosity, and self-preference biases are documented with measurable effect sizes; for a single-artifact grading task the main mitigations are explicit rubrics, separating correctness from style, and length discipline.
4. **The subject matter is fast-moving and citation risk is real.** Every major competitor has both an internal assistant and a client-facing AI platform; the differentiators are now scale, partnerships, and proof of value. Two Deloitte reports containing AI-fabricated citations show why "verifiable source" must be a hard gate, not a soft preference.

## Details

### AXIS 1 — The strongest fundamentals (the 20% that drives 80% of value)

#### A. Process framework: the Competitive Intelligence (CI) Cycle
The CI discipline, codified by SCIP (Strategic and Competitive Intelligence Professionals) and authors McGonagle & Vella, defines CI as a continuous five-phase cycle: **(1) Planning & Direction** (define the decision the brief supports), **(2) Collection**, **(3) Processing**, **(4) Analysis**, and **(5) Dissemination**, with a feedback loop. This maps almost one-to-one onto the agent's workflow steps, which is why it should be the organizing backbone. The key discipline from SCIP: start from the decision, not the data — "Tell me everything about Competitor X" is a bad brief; a decision-focused question is a good one. CI also relies exclusively on ethically gathered public sources (press releases, filings, earnings calls, analyst reports), which fits this task.

#### B. Competitor-analysis framework: Porter's Four Corners + supporting models
For the analytical core, **Porter's Four Corners Model** is the best fit because, unlike static SWOT, it is predictive — it asks not just what a competitor is doing but why, and what they will do next. Its four corners are **Drivers** (future goals/motivation), **Management Assumptions**, **Strategy** (current, including the gap between *stated* and *realized* strategy), and **Capabilities**. This is ideal for an AI-initiatives brief: the four task angles (internal transformation, go-to-market, partnerships, strategic narrative) map naturally onto "actions" (strategy + capabilities) and "narrative" (drivers + assumptions). Supporting frameworks to keep in the toolkit but use sparingly (practitioners advise ≤2 frameworks per cycle): **SWOT**, **PESTEL**, **Strategic Group Mapping**, and **Early-Warning/weak-signal analysis** for the watch-list.

#### C. Analytic tradecraft: Heuer's SATs and ACH
From the intelligence community, **Richards Heuer's *Psychology of Intelligence Analysis*** and the **Structured Analytic Techniques (SATs)** he developed with Pherson provide the rigor layer. The most useful single technique is **Analysis of Competing Hypotheses (ACH)**: list hypotheses, array evidence, and favor the hypothesis with the *least inconsistent* evidence rather than the most confirming evidence. For a competitive brief, ACH is the antidote to narrative bias (e.g., "Competitor X is winning AI" — test it against disconfirming evidence). A lightweight **Key Assumptions Check** also belongs in the agent's analysis step.

#### D. Source verification: the Admiralty / NATO code
For credibility grading, the **Admiralty Code (NATO System, codified in STANAG 2511 / AJP-2.1)** is the established standard. It scores each item on two independent axes: **source reliability A–F** (A = completely reliable) and **information credibility 1–6** (1 = confirmed by other sources). The two are kept independent because a reliable source can pass bad information and vice-versa. Applied here, a company press release or 10-K is high reliability for first-party facts; a single unconfirmed news aggregator is lower. This gives the agent a defensible, recognized way to label confidence and to filter noise.

#### E. Executive communication: BLUF + Minto Pyramid + Amazon discipline
- **BLUF (Bottom Line Up Front)** — the U.S. Army standard (Army Regulation 25-50), also used by intelligence analysts writing for busy policymakers: state the key judgment and "so what" first.
- **Minto Pyramid Principle / SCQA** — developed by Barbara Minto at McKinsey: lead with the answer, support with MECE-structured arguments. SCQA (Situation, Complication, Question, Answer) structures the opening. This is the lingua franca of the consulting audience the memo serves.
- **Amazon narrative-memo discipline** — the one-page constraint forces prioritization; narrative prose (not fragmented bullets) forces logical connection and exposes weak thinking. Strip hedging; be specific and measurable.

#### F. The genuine 80/20 and the recommended one-page template
Synthesizing the above, the highest-value elements — the ones that, if done well, deliver most of the value — are:
1. A **tight competitor-by-angle matrix** (scannable, comparable period-over-period).
2. A **"what changed since last period" delta** (the single most valuable recurring-brief feature).
3. An explicit **"implications for [Company] / so-what"** section.
4. **Graded, dated source citations** on every claim.

**Recommended reusable 1-page memo skeleton:**
- **Header / metadata:** subject, date, period covered, prepared-by (agent), overall confidence.
- **BLUF (2–3 sentences):** the single most important judgment + top implication for [Company].
- **What changed since last edition (delta):** 3–5 bullets of net-new moves.
- **Competitor × 4-angle matrix:** rows = competitors (Accenture, Deloitte, PwC, EY, + rotating); columns = Internal AI / Go-to-market / Partnerships & Investments / Strategic narrative. One tight cell each, with a source tag.
- **Implications for [Company] ("so what"):** 3–4 bullets tied to decisions.
- **Watch-list / weak signals:** early-warning items for next period.
- **Sources & confidence:** numbered, dated, Admiralty-graded.

#### G. Grounding examples (so the template ships with real, verified content)
- **Accenture** is the pace-setter. Per its Q4 FY2025 earnings (Sept 25, 2025), CEO Julie Sweet stated: "In fiscal year 2025, we tripled our revenue over fiscal year 2024 from generative AI and, increasingly, agentic AI to $2.7 billion. And we nearly doubled our generative AI bookings to $5.9 billion." Total FY2025 revenue was $69.7 billion. Its platform is **AI Refinery**, backed by a $3 billion multi-year investment and ~77,000 AI/data professionals; it stopped reporting GenAI separately after Q1 FY2026, citing how embedded it has become.
- **McKinsey** runs **Lilli** (built by QuantumBlack). Per McKinsey's own account ("Rewiring the way McKinsey works with Lilli"): "Since Lilli's firmwide rollout in July 2023… with 72 percent of the firm active on the platform, and colleagues reporting up to 30 percent time savings… More than 500,000 prompts every month." Its transformation methodology is "Rewired."
- **PwC** committed $1 billion over three years to GenAI (April 2023), became OpenAI's first reseller and rolled ChatGPT Enterprise to 100,000+ staff, runs internal assistant **ChatPwC**, and expanded its Anthropic alliance (certifying 30,000 professionals on Claude, deploying Claude Code/Cowork).
- **EY** launched the **EY.ai** platform and **EYQ** assistant following a $1.4 billion investment. Per EY's global newsroom (Sept 13, 2023): "EY investments of US$1.4b have provided the foundation for the EY.ai platform," launched alongside EY.ai EYQ after an initial pilot with 4,200 EY technology-focused team members. EY reported AI-related revenue grew ~30% in FY2025 (total revenue US$53.2 billion).
- **Deloitte** committed $3 billion to GenAI through 2030 and made Claude available to 470,000 staff (Oct 2025), running internal tool **PairD** — but suffered two public hallucination incidents that are the cautionary tale justifying the citation gate. Its A$440,000 (~US$290,000) 237-page welfare-system review for Australia's DEWR (July 2025) "contained alleged AI-generated errors, including references to non-existent academic research papers and a fabricated quote from a federal court judgment" (Fortune, Oct 7, 2025); Deloitte refunded the final installment. Separately, its 526-page Newfoundland & Labrador health-workforce report, paid CA$1,598,485 over eight installments, "contained false citations, pulled from made-up academic papers" (Fortune, Nov 25, 2025).
- **KPMG** struck a ~$2 billion Microsoft AI/cloud alliance (2023, projected to unlock >$12B in growth) and runs KymChat (assistant), Clara (audit platform), and Workbench (multi-agent platform). **IBM Consulting** runs **Consulting Advantage** (Jan 2024) across 160,000 consultants on the watsonx portfolio.
- **Your own company's** positioning for comparison: its in-house AI framework and GenAI/agents gallery, team members upskilled, and strategic AI partners (e.g. AWS, Google Cloud, Microsoft, Mistral AI). Fill this in with your firm's actual figures.

### AXIS 2 — Excellent evaluation: a sum of binary criteria

#### Why binary
The consensus across practitioner guides (EvidentlyAI, Monte Carlo, DeepEval) and benchmark papers (HealthBench, PaperBench, ProfBench) is that **binary (pass/fail) criteria are more reliable and consistent** for both LLM and human judges than high-resolution scales, and that **decomposing evaluation into single atomic criteria** ("one criterion per judgment") improves accuracy. Per OpenAI's HealthBench paper (arXiv:2505.08775), the benchmark "evaluates 48,562 unique criteria across all conversations," built from 5,000 conversations with 262 physicians across 60 countries and graded by a model-based grader (GPT-4.1) validated against physician judgment. PaperBench/ProfBench formulate each criterion as a binary entailment ("does the response fulfill this criterion: yes/no"). Score the memo as the weighted sum/percentage of binary criteria passed, with certain criteria designated **hard gates** (any failure = overall fail).

#### Judge-bias controls (important even for single-artifact grading)
Documented biases with measurable effect: **position bias** (~5–15% swing; mitigate by randomizing order in any pairwise/regression test), **verbosity bias** (~10–20%; mitigate by separating correctness from length and penalizing padding), **self-preference** (~10–25%; mitigate by using a judge from a different model family than the author where feasible), and **calibration drift** (pin the judge model version). Additional best practice: give the judge the criterion *without* the full original task prompt where criteria are self-contained, require a one-line evidence/explanation per criterion (chain-of-thought, G-Eval style), and validate the judge against a small human-labeled "golden set."

#### Proposed binary criteria, by workflow step

**Step 1 — Query/topic planning & scoping**
- [ ] The plan names every competitor in scope (Accenture, Deloitte, PwC, EY + any specified others).
- [ ] The plan names all four angles to be covered for each competitor.
- [ ] The plan states the decision/audience the brief serves (the executive team).
- [ ] The plan defines the time window for "recent" (e.g., last quarter) for the delta.

**Step 2 — Information collection / search**
- [ ] At least one source was retrieved for every competitor × angle cell.
- [ ] At least one first-party source (press release, earnings call, filing) was retrieved per competitor.
- [ ] Searches cover the current period (results dated within the defined recency window).
- [ ] No required competitor returned zero sources.

**Step 3 — Source filtering & credibility assessment**
- [ ] Every retained source has a date.
- [ ] Every retained source has a reliability/credibility grade (Admiralty-style).
- [ ] Each key claim is corroborated by ≥1 independent source OR explicitly flagged as single-source.
- [ ] Low-reliability/aggregator sources are excluded or flagged.
- [ ] No source is fabricated (every cited URL/title resolves to a real, retrievable item). **[HARD GATE]**

**Step 4 — Analysis & synthesis**
- [ ] Each competitor cell distinguishes confirmed facts from inference.
- [ ] The analysis applies a competing-hypotheses check on the headline judgment (disconfirming evidence considered).
- [ ] The "what changed" delta is derived by comparison to the prior edition.
- [ ] Each angle yields at least one company-relevant implication.
- [ ] No claim in the analysis lacks a traceable source from Step 3. **[HARD GATE]**

**Step 5 — Memo drafting / formatting**
- [ ] Output fits one page.
- [ ] BLUF appears first and states a judgment + implication.
- [ ] The competitor × 4-angle matrix is present and complete.
- [ ] A "what changed" section is present.
- [ ] An "implications for [Company]" section is present.
- [ ] A watch-list/weak-signals section is present.
- [ ] Sources are listed, numbered, dated, and graded.
- [ ] Prose is free of hedging filler and marketing language.

**Final artifact — content-quality binary checks**
- [ ] **Factual accuracy:** every checkable claim matches its cited source. **[HARD GATE]**
- [ ] **No hallucination:** no claim, quote, statistic, or citation is unsupported. **[HARD GATE]**
- [ ] **Citation present & verifiable:** every claim carries a resolvable, dated source. **[HARD GATE]**
- [ ] **Recency:** all time-sensitive claims fall within the defined window or are dated.
- [ ] **Competitor coverage:** all named competitors appear.
- [ ] **Angle coverage:** all four angles appear for each competitor.
- [ ] **BLUF present.**
- [ ] **Actionable implications present** (tied to company decisions).
- [ ] **Length:** fits one page.
- [ ] **No fluff:** no unsupported superlatives or vendor marketing language.
- [ ] **Comparability:** same structure/fields as prior edition (period-over-period).
- [ ] **Prioritization:** the most important development is clearly flagged as such.
- [ ] **Balanced sourcing:** not over-reliant on a single competitor's self-promotion.

#### Tooling concepts (kept light for a non-technical reader)
- **LLM-as-judge / rubric-based grading:** an LLM scores the output against the checklist above; this is "reference-free" (no gold answer needed), which suits a novel brief each period.
- **Code-based checks where deterministic:** length (one page), presence of required sections, and whether each cited URL resolves are better handled by simple deterministic checks than by the LLM judge.
- **Golden set + human spot-check:** during the light-human-review phase, label ~10–20 example memos pass/fail per criterion to calibrate the judge before full autonomy.

## Recommendations

**Stage 1 — Build the skeleton and the gates (now).** Implement the fixed one-page template (BLUF → delta → matrix → implications → watch-list → graded sources). Implement the three deterministic hard gates first: every claim has a resolvable dated citation; output is one page; all required sections present. *Threshold to proceed:* 100% of hard gates pass on a 10-memo test set.

**Stage 2 — Layer the binary rubric and calibrate the judge.** Encode the ~45 binary criteria; designate the hallucination/accuracy/citation criteria as overall-fail gates. Calibrate the LLM judge against a human-labeled golden set. *Threshold:* judge–human agreement ≥85% on hard gates before reducing human review.

**Stage 3 — Reduce human involvement gradually.** Move from review-every-memo to spot-checking only memos that pass automated gates. *Threshold to go fully autonomous:* ≥95% judge–human agreement on the hard gates over a rolling sample, and zero fabricated-citation escapes in the last N editions. If a hallucination escapes, drop back to mandatory human review.

**Cross-cutting:** Keep the framework set deliberately small (CI Cycle + Four Corners + Minto/BLUF + Admiralty). Version the template so period-over-period comparability is structural. Pin the judge model version to prevent calibration drift.

## Caveats
- **Some sources are secondary or vendor-authored.** Competitor figures from company press releases are first-party (high reliability for the fact of the announcement) but are also marketing; the agent should treat self-reported revenue/booking figures as claims, not audited fact, and grade accordingly.
- **The PwC–Anthropic expansion date needs confirmation.** The "certify 30,000 / Claude Code + Cowork" specifics are confirmed by both companies' press releases, but at least one secondary source dates the expansion to 2026 rather than October 2025 — verify the exact press-release date before publishing.
- **The Admiralty code has documented limitations:** the two axes are often correlated in practice (analysts let source reliability bleed into credibility judgments), so the agent should be instructed to grade them independently.
- **Binary criteria can fragment "completeness" judgments;** for holistic completeness, a detailed-rubric holistic check can complement atomic checks — note this if coverage gaps recur.
- **The competitive landscape moves monthly;** any embedded examples in the template are illustrative and must be refreshed each period — the "what changed" delta is the mechanism that keeps the brief current.

---

# Appendix: refine-from-preview skill

> Verbatim `SKILL.md` copied by the "Copy the refine-from-preview skill" button on Step 3 (Test and improve). Participants paste it into `.claude/skills/refine-from-preview/SKILL.md`.

---
name: refine-from-preview
description: Use to iteratively improve an output-producing skill (default target - competitive-brief) by reviewing its rendered output in the live preview and acting on the user's plain-language critique. Trigger whenever the user wants to refine a skill from what they see in the preview, critique the memo/briefing/output and have the skill re-run, run "the loop again", tighten or re-pitch the output, or make it better against a deep-research quality bar. The user judges the visible output and makes high-level calls; you map those to implementation changes, edit the skill (not the one-off output), and re-run so the user can re-review in the preview.
---

# Refine a skill from its live-preview output

A human-in-the-loop loop for making an output-producing skill better every run — by
showing the user the rendered output in the live preview, hearing what's wrong with what they
see, and pushing those fixes back into the skill so the next run is better. Then re-run and
re-review. Repeat until the user is happy.

Two ideas hold the whole thing together:

1. Improve the skill, not the one-off output. It's tempting to hand-patch the memo in front
   of you. Don't. The point is a skill that produces a great output a thousand times, on inputs
   you'll never see. So every fix goes into the skill (its `SKILL.md` / references / scripts), then
   you re-run to prove it. A hand-edited memo proves nothing about the skill.
2. The user judges the output; you own the implementation. The user reviews what renders in
   the preview and reacts in plain language ("the headline buries the lede", "I can't tell which
   sources to trust"). They do not need to know how the skill works. Your job is to translate
   each reaction into the right change. Never make the user learn the internals to give feedback.

## The three inputs (identify these once, at the start)

- Target skill — the skill being improved. _Default: `competitive-brief` (`.claude/skills/competitive-brief/`)._
- Quality bar — a deep-research markdown the user produced in Claude; its criteria and
  frameworks are the yardstick. _Default: the compass artifact in `docs/` (`docs/compass_artifact_*.md`)._
  Re-read it at the start of every loop. Note: this is a document, not the local
  `deep-research` skill — ignore that skill; it is unrelated here.
- Live preview — the web app that renders the target skill's output. _Default: the `web` server
  (`preview_start` name `web`, http://localhost:3000), which renders each project's `output/` folder._
  Confirm it's running and the latest output is the thing on screen before each review.

> Pointing this at a different skill later? Swap the three inputs above. Everything else is the same.

## The loop

Run one loop at a time. Stop and wait for the user at the two 🛑 points. Don't edit before they react.

### Step 1 — Show, then propose weaknesses 🛑

- Make sure the live preview is up (`preview_start`) and the latest output is what renders. Tell
  the user the URL and exactly what to look at (which project page / which memo).
- Read the current rendered output yourself and hold it against the quality bar and any feedback from
  earlier loops. Find what's genuinely weak.
- Present a short list of candidate weaknesses in plain language, grouped by the part of the output
  the user can see — so they can react to something concrete even without knowing the design space:
  - Headline / bottom line — is the single most important thing first and unmissable?
  - The comparison — is it scannable? complete? are the right things side by side?
  - What changed — does it surface the genuinely new since last time?
  - Implications / "so what" — tied to a real decision, or generic?
  - Sources & trust — can the user tell, at a glance, what's solid vs. shaky?
  - Length & skimmability — one page? reads in 60 seconds? any padding?
  - Tone / voice — right register for the audience? any marketing fluff?
- Keep it to the few that matter; say which you think is most important and why. *No jargon, no
  criterion codes, no implementation.* Ask the user to confirm, drop, reprioritise, and add their own.
- 🛑 Stop and wait.

### Step 2 — Sort the agreed problems: auto-fix vs. taste 🛑

Once the list is agreed, split it:

- Safe fixes — clear, low-risk improvements with an obvious right answer (e.g. surface the top
  development harder, cut padding, add a trust flag to sources). Just do these — don't make the
  user adjudicate the obvious. State in one line what you'll auto-fix.
- Taste calls — real forks only the user can settle (e.g. "lead with the competitor table vs. a
  narrative bottom-line?", "rank competitors by threat vs. keep them neutral?"). For each, give 2-4
  options framed by what the user would GET, not how it's built, one-line trade-off each, and your
  recommended default. Order most- to least-important.
- 🛑 Stop and let the user pick the taste calls. (If there are none, say so and continue.)

### Step 3 — Edit the skill (not the memo)

- Apply every agreed change in the target skill — its `SKILL.md`, references, or scripts — so the
  improvement generalises and survives the next run.
- Ground each change in the quality bar: it should move a real criterion, not be cosmetic. *Resist
  overfitting* to this one example — if a fix only helps this exact memo, it's the wrong fix; reach for
  the more general phrasing or pattern.
- Don't regress the target skill's own guardrails. If it has hard gates / a self-check
  (competitive-brief does), keep them intact and make sure they still pass after your edits.

### Step 4 — Re-run, re-render, report 🛑

- Re-run the target skill on the same example to produce a fresh output. Write it to the `output/`
  folder so the live preview picks it up; confirm it renders, and point the user back to the preview.
- In chat, give only a short changelog — one line per change: what changed + the weakness it fixes.
  Optionally one before/after line on any quality-bar gate that now passes. (The user reads the full
  result in the preview, not in chat.)
- Be honest in the changelog — only claim a fix you actually see in the new output; verify before
  you assert. A confident-but-wrong changelog is worse than none.
- 🛑 Then loop back to Step 1 on the new output, or stop if the user's happy.

## When to stop

Stop the loop when the user says they're satisfied, when a review turns up no real weaknesses, or
when you're no longer making meaningful progress (say so honestly rather than inventing changes).

## Example of one round (illustrative, abbreviated)

Step 1 — weaknesses I'd raise on the rendered brief:

- Bottom line: the headline judgement is there, but the single biggest move this quarter isn't
  flagged as #1 — it reads like all five bullets are equal.
- Sources & trust: every claim is sourced, but a reader can't tell first-party from a blog at a
  glance. (I think this is the most important.)
- Length: the implications section repeats the headline — ~40 words of padding.

Which of these land? Anything you'd add or drop?

Step 2 — after you react:

Auto-fixing (safe): trim the implications padding; add a one-glance trust marker to each source.

One taste call for you:

- How to flag the top move — (A) a one-line "Most important this quarter:" banner above the table
  (recommended — unmissable); (B) bold it in place (subtler, less disruptive); (C) leave as-is.

Step 4 — changelog after re-run:

- Added a "Most important" banner → top development is now unmissable (fixes "bottom line").
- Sources now show a plain trust tag (solid / mixed / weak) → trust readable at a glance.
- Cut 38 words of repeated framing from implications → tighter, still one page (gate still PASS).

Fresh memo is live in the preview — take a look.

## Principles (the why)

- Generalise, don't patch. We're building a skill used many times, not fixing one memo. Overfit
  `ALWAYS`/`NEVER` rules and example-specific hacks make the skill brittle — prefer explaining the
  intent so the model does the right thing on inputs you never tested.
- Keep the user in plain language. They steer with taste; you handle mechanism. If you catch
  yourself asking the user to choose between implementation details, re-frame it as outcomes.
- The preview is the source of truth for review — not a memo pasted into chat. Chat is for the
  question (Step 1), the taste forks (Step 2), and the changelog (Step 4).
- Re-read the quality bar each loop and let it ground your diagnosis — but never lecture the user
  about its criteria; that's your private yardstick.
