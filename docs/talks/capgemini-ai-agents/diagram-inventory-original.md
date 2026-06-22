<!-- ABOUTME: Exhaustive slide-by-slide inventory of every code-drawn diagram, interactive element, copy-paste prompt, timer, and stepped reveal in the ORIGINAL (origin/slides branch) Capgemini "AI Agents Tech Lab" deck. -->
<!-- ABOUTME: Source: git repo /home/ezalos/Pro/IQxCapG-LabAgent, branch origin/slides, app slides/apps/capgemini-workshop. Detailed enough to recreate each figure in vanilla HTML/CSS/SVG/JS. -->

# Capgemini "AI Agents Tech Lab" — Original Deck Diagram Inventory

Source (read-only): repo `/home/ezalos/Pro/IQxCapG-LabAgent`, branch `origin/slides`, app `slides/apps/capgemini-workshop/src`.
38 slide components (TOTAL_SLIDES = 37 in chrome, but 38 entries in deck.config — the discrepancy is the cover+presenters; the masthead counter derives total from nav position).

## Conventions / shared primitives used throughout

- **Brand color** = orange `#f97316` (a.k.a. `brand`), light orange `#fb923c`/`#fdba74`/`fg-accent`. Gradient text via `bg-grad-text` (orange→light-orange). Page bg near-black `#0a0a0a` / `bg-page`.
- **Amber** (`amber-300/400`) is the ONLY sanctioned secondary accent, scoped to security/risk/"values to verify".
- **Emerald** = pass/green, **Red** = fail, used only in eval matrices and the LLM-judge vote.
- Context-engineering slide (16) deliberately breaks the orange discipline with a 3-family color code (orange/amber = System, sky/cyan = Tools, violet/indigo/fuchsia/purple = Conversation).
- **`Rise`**: every block is wrapped in a staggered fade/translate-in entrance keyed by a `delay` (ms). These are *load* reveals (all play once on slide entry), NOT click-stepped reveals — except where noted. Listed under "Stepped reveals" per slide as the staggered entrance order.
- Fonts: `sp-display` (display serif/sans headline), `sp-mono` (monospace), `sp-tnum` (tabular numerals).
- Reusable atoms: `AppWindow` (fake terminal/app chrome with 3 traffic-light dots + title; `kind="app"` adds a right-aligned "Claude Code" tag), `PromptLine` (orange `❯` + text), `ToolCall` (dim `●` + tool name + detail), `Callout` (bordered strip; tones: security=ShieldAlert+amber, risk=AlertTriangle+amber, tip=Lightbulb+orange), `DiagramFrame` (bordered figure container, optional "Values to verify" amber chip), `BigStat` (gradient 84px figure + label + source), `StepHeader` (mono "Step NN / 06" + progress dots + 64px title + goal line), `Flow` (horizontal numbered progression with connector line + chevrons), `OfferCard` (icon + audience tag + headline + bullets + chip), `LineChart`/`DiagNode`/`DiagEdge` (SVG primitives in `_charts.tsx`).

---

## 01 — Cover (`01-cover`)

- **Diagram/visual**: none drawn in code. Right side is a framed PHOTO (`photos.euronextHackathon2`, "An IQ build session, every participant ships") via `FramedMedia` (rounded border, orange glow, 4 corner ticks, gradient caption strip). NOT a code diagram — a PNG asset.
- Masthead: page counter `01 / NN` + hairline rule underneath (`sp-rule sp-draw`, draws itself in).
- Title "AI Agents / **Tech Lab**" (104px, "Tech Lab" gradient). Dossier strip: `Executive Lab · AI Agents`. Byline "Run by Louis Develle".
- **Stepped reveals (staggered entrance)**: masthead (40ms) → metadata strip (140ms) → title (220ms) → photo (300ms) → subhead (320ms) → byline (420ms) → footer (520ms).
- Prompts/copy buttons: none. Timers: none.

## 01b — Presenters (`01b-presenters`)

- **Diagram/visual**: none code-drawn. Instructor card(s), each a framed square PHOTO + role tag + name + bulleted credentials (orange `→` bullets). Photos are PNG/JPG assets, not figures. [Single-instructor for reuse.]
- Card content (load-bearing labels): Louis Develle — "Research engineer & teacher". [Co-instructor bios removed.]
- **Stepped reveals**: header (120ms) → Louis card (260ms).
- Prompts/timers: none.

## 02 — Agenda (`02-agenda`)

- **DIAGRAM — Flow (horizontal numbered progression)** via `Flow` component. 4 nodes on a single horizontal connector line (gradient orange, runs bubble-1→bubble-N), each node = a 56px circle with 2-digit number `01–04`, a chevron `›` midway between bubbles. Below each: title, mono players line, body.
  - Node 01 "Kick-off" / "10 min · All labs" / "Welcome and the shape of the morning, then each group joins its lab."
  - Node 02 "Framing" / "45 min · This deck" / "What agents are, how Claude Code works, and the method you will build with."
  - Node 03 "Build" / "2 h 15 · Hands on" / "You build a working agent on a real use case, we coach table by table."
  - Node 04 "Demos" / "30 min · Full COMEX" / "Each lab selects 2 projects, presented live to everyone."
  - Layout: CSS grid, `repeat(4, 1fr)`; connector absolute at top 28px. Color: brand orange. (On mobile collapses to single column, connector hidden.)
- One-line rule below: "a finished project beats an impressive one that does not run."
- **Stepped reveals**: header (120ms) → Flow (280ms) → rule line (440ms).
- Prompts/timers: none (durations are static text labels, not countdowns).

## 03 — Crazy Numbers (`03-crazy-numbers`)

Three-up grid of stat visualizations. **THREE code-drawn stat figures:**

1. **DIAGRAM — CommitProgression** (custom): a horizontal progression `0% → 4% → 10%`.
   - 3 gradient percentages (`Pct`, 44px gradient text): "0%", "4%", "10%".
   - Between them: 2 `Arrow` elements — each a small column with a mono accent-orange time label ABOVE a brand-orange `→`. Labels: "~1 year" (between 0% and 4%), "6 weeks" (between 4% and 10%).
   - Caption below: "of all public GitHub commits, authored by Claude Code alone, within a year of launch." + cite `[1,2,5]`.
   - Container: bordered rounded card.
2. **BigStat** "$2.5B" (84px gradient) — "annualized revenue for Claude Code alone, less than a year after launch. Value people actually pay for." cite `[3]`.
3. **BigStat** "76%" (84px gradient) — "of support conversations resolved autonomously by Intercom's Fin, at $0.99 per resolution, paid only on success." cite `[4]`.

- Sources footer line (links): [1] semianalysis.com · [2] coremention.com · [3] venturebeat.com · [4] fin.ai · [5] anthropic.com.
- Closing line: "Measured, already-happening numbers, not projections…".
- **Stepped reveals**: header (120ms) → CommitProgression (260ms) → $2.5B stat (360ms) → 76% stat (460ms) → closing line (580ms).
- Prompts/timers: none.

## 04 — METR Curve (`04-metr-curve`)

- **Visual**: NOT code-drawn — a PNG figure `/figures/metr-time-horizon.png` (METR time-horizon chart, white background, in a framed `<figure>` with orange border + glow). Caption "METR — Time Horizon 1.1, 50% success" cite `[1]`.
  - (Note: `_charts.tsx` provides a `LineChart` SVG primitive with `logY` support designed exactly for this curve, but THIS slide uses the authoritative PNG, not the redraw. Flag for recreation: could be rebuilt with `LineChart` log-Y.)
- Right column: two paragraphs ("In 2023… a few minutes / Today… hours of autonomous work"; "doubles roughly every seven months, ~3× faster than Moore's Law" cite `[2]`).
- Sources: [1] metr.org · [2] arxiv.org/2503.14499.
- **Stepped reveals**: header (120ms) → chart figure (280ms) → text column (420ms).
- Prompts/timers: none.

## 05 — Cost Collapse (`05-cost-collapse`)

- **Visual**: NOT code-drawn — PNG `/figures/epoch-inference.png` (Epoch AI inference-price chart, white bg, framed figure orange border+glow). Caption "Epoch AI — inference price per million tokens" cite `[1]`.
  - (Same note: `LineChart` log-Y primitive exists; this slide uses the authoritative PNG.)
- Right column: paragraph + a **Callout (tone=tip, title="The takeaway")**: "'Too hard' or 'too expensive' are bad reasons not to start. Build the use case now, time alone takes care of both."
- Sources: [1] epoch.ai · [2] mistral.ai.
- **Stepped reveals**: header (120ms) → chart (280ms) → text+callout (420ms).
- Prompts/timers: none.

## 06 — Definition (`06-definition`)

- **DIAGRAM — Definition build-up** (the backbone). 5 numbered fragment rows, each: mono 2-digit index (`01`–`05`) in a fixed-width column + a 52px display-serif clause with one gradient accent word.
  - 01 "An agent is a **system**"
  - 02 "which uses **tools**"
  - 03 "to interact **repeatedly**"
  - 04 "with its **environment**"
  - 05 "to accomplish its **goal**"
- Below: "Not a chatbot, not a single prompt. A loop that acts, observes, and acts again until the goal is reached." cite `[1]`.
- Source: [1] anthropic.com/research (Building Effective Agents).
- **Stepped reveals**: header (120ms) → clause 01 (300ms) → 02 (440) → 03 (580) → 04 (720) → 05 (860) → closing line (1050ms). This is the slow fragment-by-fragment reveal called out in deck notes ("Read the five fragments slowly").
- Prompts/timers: none.

## 07 — Agent Loop (`07-agent-loop` + `LoopDiagram.tsx`)

Two figures side by side.

- **DIAGRAM A — AppWindow transcript** (left, "agent session"): a fake terminal showing the Asian-restaurant example as a think→act→observe trace:
  - `PromptLine`: "Find me an Asian restaurant for Tuesday night"
  - italic dim: "Thinking: near the office, open Tuesday, bookable…"
  - `ToolCall` name `search_web` detail `"asian restaurant Paris 2e open tuesday"` → dim "→ 12 results"
  - italic dim: "Thinking: cross-check ratings and opening hours…"
  - `ToolCall` `fetch_page` detail "top 3 candidates" → "→ one closed Tuesdays, two open"
  - `ToolCall` `check_availability` detail "Tuesday, 8 pm, 2 people"
  - final line (brand ✓): "Booked: Izakaya Jin, Tuesday 8 pm. Confirmation sent."
- **DIAGRAM B — LoopDiagram (SVG, the agent loop)** (right): the think→act→observe cycle drawn natively (replaces the classic agent-cycle gif).
  - viewBox `0 0 540 480`. Center (CX,CY)=(270,240), radius R=150.
  - **3 nodes** placed on the circle at angles: Thought (−90°, top), Action (30°, lower-right), Observation (150°, lower-left). Each node = rounded rect 184×72, fill white/0.03, stroke orange/0.45; node title 22px white + mono 13px sublabel.
    - "Thought" / sub "what next?"
    - "Action" / sub "use a tool"
    - "Observation" / sub "read the result"
  - **3 curved arrows** (clockwise arcs along the radius, 26° gap trimmed each side so they don't touch nodes): Thought→Action (−90→30), Action→Observation (30→150), Observation→Thought (150→270). Arrowheads via `<marker id="loop-arrow">` (orange/0.8). Arc stroke orange/0.55, width 2.2.
  - **Center text** (2 lines, mono 15px, dim): "until the goal" / "is reached".
- Title "One goal, **many small steps**" cite `[1]`. Source: [1] arxiv.org/2210.03629 (ReAct).
- **Stepped reveals**: header (120ms) → AppWindow (280ms) → LoopDiagram (420ms).
- Prompts/timers: none.

## 08 — LLM + Harness (`08-llm-plus-harness`)

- **DIAGRAM — "Agent = LLM + harness" schema** (the anatomy that anchors the next 5 slides):
  - **Top node**: a wide centered card "**LLM**" (44px gradient) + vertical hairline + text "The reasoning engine. Brilliant, but alone it can only **talk**." Border orange/40.
  - **Connector**: a centered vertical gradient line (orange→white, 36px tall) descending from the LLM card.
  - **Bottom row — 5 harness blocks** in a `grid-cols-5`, each a card with a lucide icon (orange), title, body, and a mono footer "3.{i+1} — next" (pointing to the next 5 slides):
    1. **Tools** (Wrench) — "How it touches the world: CLI, APIs, MCP." — footer "3.1 — next"
    2. **Skills** (BookOpen) — "Recipes it knows how to follow, plain markdown." — "3.2 — next"
    3. **Memory** (Database) — "What it keeps between sessions." — "3.3 — next"
    4. **Sandbox** (Box) — "Where its code runs, and how far it can reach." — "3.4 — next"
    5. **Orchestration** (Workflow) — "Schedules and subagents." — "3.5 — next"
  - Closing line: "The harness is what turns a model that talks into a system that **acts**." cite `[1]`.
- Source: [1] sebastianraschka.com.
- **Stepped reveals**: header (120ms) → LLM node (280ms) → connector (380ms) → 5 blocks staggered (440, 530, 620, 710, 800ms) → closing line (900ms).
- Prompts/timers: none.

## 09 — Tools (`09-tools`)

THE M×N vs M+N pair. Two SVG mesh/hub diagrams, drawn with `DiagNode`/`DiagEdge` from `_charts.tsx`.

- Left column: 3 "kind" rows (icon + title + body) — **CLI** (Terminal) "Anything your terminal can do…", **API** (Globe) "Web search, internal services, SaaS endpoints…", **MCP** (Plug) "A standard plug: one connector per tool…" cite `[1]`.
- **DIAGRAM A — MeshDiagram ("Without MCP · M × N connectors")** in a `DiagramFrame`:
  - viewBox `0 0 440 240`.
  - **Top row 3 Agent nodes** at x = 80, 220, 360 (y≈40), labels "Agent 1", "Agent 2", "Agent 3" (118×44, neutral white border).
  - **Bottom row 4 Tool nodes** at x = 45, 162, 278, 395 (y≈200), labels "Tool 1"–"Tool 4" (104×44).
  - **Edges**: FULL MESH — every agent connected to every tool = 3×4 = 12 neutral lines (white/0.16). Visually the M×N tangle.
- **DIAGRAM B — HubDiagram ("With MCP · M + N connectors")** in a `DiagramFrame`:
  - Same 3 agents top, 4 tools bottom.
  - **Center node** "MCP" (130×44, ACCENT orange fill+border) at (220,120).
  - **Edges (all accent orange)**: each of the 3 agents → MCP hub (3 lines), MCP hub → each of 4 tools (4 lines) = 3+4 = 7 lines. Visually the M+N hub-and-spoke.
- Below both: **Callout (tone=security)**: "Every external tool or MCP server runs with your agent's permissions. Treat third-party tools as attack surface, install only what you trust."
- Source: [1] anthropic.com/news (Model Context Protocol).
- **Stepped reveals**: header (120ms) → 3 kinds column (260ms) → both diagrams (400ms) → security callout (560ms).
- Prompts/timers: none.

## 10 — Skills (`10-skills`)

- **DIAGRAM — AppWindow "SKILL.md" walkthrough** (left): fake editor titled `skills/translate-document/SKILL.md`, footer "One folder, one markdown file. That is a skill."
  - `name:` **translate-document**
  - `description:` **Translate a document while preserving its formatting**
  - **Divider with a pill chip**: a centered horizontal rule with a bordered orange pill "below: loaded on demand" (this visually separates always-visible front-matter from on-demand body — the progressive-disclosure idea).
  - Then a 5-step numbered recipe (dim): 1 Read the file / 2 Detect the source language from the first 500 characters / 3 Translate section by section, preserving formatting / 4 Write the output to a file suffixed with the target language / 5 Report what was done.
- Right column: 3 bullets (orange `→`) about skills + a **Callout (tone=security)**: "External skills are instructions you didn't write. Read them before installing…" cite `[2]`. Bullet 3 names mono plugins "superpowers", "frontend-design".
- Sources: [1] agentskills.io · [2] snyk.io.
- **Stepped reveals**: header (120ms) → SKILL.md window (260ms) → bullets+callout (420ms).
- Prompts/timers: none.

## 11 — Memory (`11-memory`)

- Left: two stacked "tier" cards (icon + title + body):
  - **Start simple** (FileText, ACCENT orange border) — "Markdown and JSON files. Readable, diffable, versionable, and the agent edits them itself." cite `[1]`.
  - **Scale later** (Database, neutral border) — "Databases when volume demands it: full-text search (FTS5) or semantic search…"
- **DIAGRAM — AppWindow "MEMORY.md" index** (right): titled `memory/MEMORY.md`, footer "An index up top, detail in one file per fact — loaded on demand". Body:
  - `# Memory index`
  - "- User prefers concise mail recaps → `90a2c384e.md`"
  - "- Formatting rules for quarterly reports → `8cff0c56.md`"
  - "- Competitor watchlist, agreed Jan 2026 → `3aa91f02.md`"
  - (Demonstrates the index→detail-file progressive disclosure pattern.)
- Source: [1] anthropic.com/engineering.
- **Stepped reveals**: header (120ms) → two tier cards (260ms) → MEMORY.md window (420ms).
- Prompts/timers: none.

## 12 — Sandbox (`12-sandbox`)

- **DIAGRAM — Nested-boxes reach diagram (CSS, concentric containment)** (left): three nested bordered boxes showing scope from outside-in:
  - **Outer box** label (mono): "Your machine" (neutral border).
  - **Middle box** (dashed border): "Other folders · system · network" + amber tag "permission required".
  - **Inner box** (ACCENT orange border + orange tint fill): "The launch folder — the agent's reach", containing a 3-up mono grid of chips: "project files", "skills/", "CLAUDE.md".
  - Visual semantics: the agent's default reach = inner orange box only; everything outward requires explicit permission (amber).
- Right column: 3 bullets (orange `→`): "runs on your machine, not someone else's cloud" / "scoped to the folder where you launched it" / "Everything beyond is a right you grant explicitly…".
- No sources. **Stepped reveals**: header (120ms) → nested diagram (280ms) → bullets (440ms).
- Prompts/timers: none.

## 13 — Orchestration (`13-orchestration`)

- Two-up card grid (no fine-grained schema, conceptual cards):
  - **On a schedule** (CalendarClock) — "Cron jobs and routines: the same agent runs every morning at 8, unattended. A press briefing that emails itself, a weekly competitive recap."
  - **Subagents** (GitFork) — "An agent can launch other agents: fan a document out to three specialist readers in parallel, then merge their findings." cite `[1]`.
- Closing line: "You will use **both before noon**, subagents during the build, a routine to close the morning."
- Source: [1] sebastianraschka.com.
- **Stepped reveals**: header (120ms) → schedule card (280ms) → subagents card (400ms) → closing line (540ms).
- Prompts/timers: none.

## 14 — Meet Claude Code (`14-meet-claude-code`)

- **Visual**: PNG screenshot `/figures/claude-code-screenshot.png` (the Claude Code app, white bg, framed). NOT code-drawn.
- Header carries a **"Live demo" pill** (MonitorPlay icon + orange bordered pill) — a static badge, not interactive.
- Right column: "The 5-minute tour" checklist, 5 numbered items (each a 36px circle index + text):
  1. "Send a prompt, watch it think and act"
  2. "Resume a past session, nothing is lost"
  3. "Attach files with @path"
  4. "Browse the project files from the app"
  5. "The modes menu (auto mode comes in a minute)"
- **Stepped reveals**: header (120ms) → screenshot (280ms) → checklist (420ms).
- Prompts/timers: none.

## 15 — CLAUDE.md (`15-claude-md`)

- **DIAGRAM — AppWindow "CLAUDE.md" sample** (left): titled `radar/CLAUDE.md`. Body (markdown rendered as styled lines):
  - `# Radar — press review agent`
  - "This repo builds a daily executive press briefing."
  - `## Rules` → "- Sources: at least 3 independent outlets, articles < 7 days old" / "- Voice: executive briefing, no jargon, sourced claims" / "- Test cases live in tests/, replay them after every change"
  - `## Commands` → "- Run the briefing: follow skills/press-briefing"
- Right: 3 bullets about CLAUDE.md being read at every session start (cite `[1]`), the home of repeated context, per-project ground truth.
- Source: [1] docs.claude.com (memory).
- **Stepped reveals**: header (120ms) → CLAUDE.md window (280ms) → bullets (420ms).
- Prompts/timers: none.

## 16 — Context Engineering (`16-context-engineering`)

THE big mental-model figure. **DIAGRAM — "The context window" stacked color-coded block diagram** (left, ~660px wide):

- Outer panel "The context window" with a small mono badge top-right "rebuilt every turn" (RefreshCw icon).
- **3 color-family blocks**, each `BlockView` = a tinted bordered panel with a header label and rows. Each row = a left-border-accent mono chip with `tag` + dim `detail`:
  - **System** (orange/amber family, header orange-300):
    - `CLAUDE.md` — "project rules & conventions"
    - `Environment` — "cwd, OS, git state, date"
    - `Skills index` — "names + descriptions, loaded on demand"
    - `Memory index` — "one line per fact"
  - **Tools** (sky/cyan family, header sky-300):
    - `search_web(q)` — "→ results"
    - `fetch_page(url)` — "→ page content"
    - `read_file(path)` — "→ text"
    - `edit · bash · …` — "~18 typed tools"
  - **Conversation** (violet/indigo/fuchsia/purple family, header violet-300):
    - `User` — "your message"
    - `Thinking` — "private reasoning"
    - `Tool use` — "structured tool call"
    - `Tool result` — "observation fed back"
    - `Agent` — "the answer · then repeat × many turns"
  - **Free space** — a dashed-border centered strip "Free space — what is left before the window is full".
- Right column: **4 numbered ideas** (36px circle index + title + body):
  1. "One text, stateless" — "The whole thing is rebuilt and re-sent every single turn. The model remembers nothing by itself." cite `[1]`
  2. "Four blocks" — "System, tools, conversation, and the free space left…"
  3. "Progressive disclosure" — "Indexes up top, detail on demand. That is exactly what skills and memory are."
  4. "A finite window" — "There is a hard size limit, so you manage what earns its place in it."
- Source: [1] anthropic.com/engineering.
- **Stepped reveals**: header (120ms) → context-window block diagram (260ms) → 4 ideas (420ms).
- Prompts/timers: none.

## 17 — Permissions (`17-permissions`)

- Left: 3 bullets (ask-by-default cite `[1]`, auto mode pre-approves in sandbox, extra rights in plain language) + **Callout (tone=tip)**: "For the lab: turn auto mode on. The sandbox keeps it contained…".
- **DIAGRAM — AppWindow "permission request" (kind=app)** (right): simulates the real permission dialog:
  - `PromptLine`: "Draft the briefing and save it to reports/"
  - **Permission card** (orange border + tint): "Claude wants to write: reports/briefing-06-18.md" + a 3-button row of mono pill chips: "Allow once" (accent orange), "Allow always" (dim), "Deny" (dim).
  - **Mode strip** (mono): "mode: **ask ←** · plan · auto" (shows the current mode selector, "ask" highlighted with an arrow).
- Source: [1] docs.claude.com (iam).
- **Stepped reveals**: header (120ms) → bullets+callout (260ms) → permission AppWindow (420ms).
- Prompts/timers: none.

## 18 — Thinking Models (`18-thinking-models`)

- Two-up cards:
  - **The model** (Brain) — "Build with the best model available, today Claude Fable 5 leads FrontierCode Diamond, the hardest production-code benchmark." cite `[1]` + "Cheaper models come later, in production, once your tests can prove they are good enough."
  - **Thinking effort** (Gauge) — "How long the model reasons before acting. For design and debugging, set it to `max`…" + "During the lab everything runs at full effort…".
- Source: [1] llm-stats.com/frontiercode.
- **Stepped reveals**: header (120ms) → model card (280ms) → thinking card (400ms).
- Prompts/timers: none. (No diagram; conceptual card slide.)

## 19 — Cowork & Routines (`19-cowork-routines`)

- Two-up cards (teaser):
  - **Cowork** (LayoutGrid, neutral) — "The same agent, pointed at your everyday files: documents, decks, spreadsheets. Agent leverage for non-code work."
  - **Routines** (CalendarClock, ACCENT orange border+tint) — "Schedule an agent run: 'every morning at 8, build my press briefing and email it to me.'" + a mono pill chip "We set one up at the end".
- **Stepped reveals**: header (120ms) → Cowork card (280ms) → Routines card (400ms).
- Prompts/timers: none. (No diagram.)

## 20 — Method Overview (`20-method-overview`)

THE method-cycle "spine + optional loop" figure. **DIAGRAM — Build-method spine with a hanging loop:**

- **Spine** (horizontal): 4 chips with mono index + display title, separated by orange `›` chevrons:
  - `01 Clarify` › `02 Draft` › `03 Evaluate` (HIGHLIGHTED — orange border + tint) › `06 Understand`
  - (Note the deliberate jump 03→06: steps 04/05 live in the loop below.)
- **Optional loop** (hanging off Evaluate): a dashed orange-border rounded panel labeled (mono, Repeat icon) "Optional loop, repeat until it is good enough" containing a horizontal mini-flow:
  - `03 Evaluate` › `04 Observe` › `05 Improve` › chip "back to Evaluate" (CornerLeftUp icon) — i.e. the 03→04→05→03 cycle made visual.
- Intro line: "We build a **Press Review agent live, step by step**…". Closing line: "What you are building: **a skill, or a small collection of skills**, plus the tools it needs and the data it can access."
- **Stepped reveals**: header (120ms) → intro line (280ms) → spine (420ms) → optional-loop panel (560ms) → closing line (680ms).
- Prompts/timers: none.

## 21 — Step 1 Clarify (`21-step1-clarify`)

- `StepHeader` step=1/06 "Clarify the goal" / goal "Know what a great result looks like, before a single line is built." (mono "Step 01 / 06" + 6 progress dots, 1 filled.)
- Left: 4 bullets (deep research, extract the Pareto, binary checks that sum to a score, works best on a task you know well) + **Callout (tone=tip, title="Timing")**: "Deep research runs long. Launch it in advance, ours is already in your starter repo."
- **DIAGRAM — AppWindow "research/what-makes-a-great-briefing.md"** (right): a markdown sample with a **binary-checklist visualization**:
  - `# A great executive press briefing`
  - `## Binary checks (score = sum)`
  - `[ ] ≥ 3 independent outlets per theme` (the `[ ]` rendered in brand orange)
  - `[ ] Every article less than 7 days old`
  - `[ ] Each claim carries its source`
  - `[ ] One actionable implication per theme`
  - `[ ] Reads in under 3 minutes`
- **Stepped reveals**: header (120ms) → bullets+callout (280ms) → research.md window (420ms).
- Prompts/timers: none.

## 22 — Step 2 First Draft (`22-step2-first-draft`)

- `StepHeader` step=2/06 "Get a first draft, A to Z" / goal "A rough version that runs end to end beats a perfect fragment." (2 dots filled.)
- Left: 5 bullets (give CC the research.md; `/brainstorm` the workflow; minimal Pareto-efficient v1, text output only; wire tools+data now; eval layer non-negotiable) + **Callout (tone=risk, title="Secrets & blast radius")**: "No passwords or API keys in the repo. And know what your agent can send or delete before you let it run."
- **DIAGRAM — AppWindow "radar — first draft" (kind=app)** (right): a simulated build transcript:
  - `PromptLine`: "Read @research/what-makes-a-great-briefing.md, then /brainstorm a press-briefing skill"
  - dim italic: "Proposing 4 steps: collect → filter → synthesize → format…"
  - `PromptLine`: "Build it and run it once, A to Z, text output only"
  - reply: "Draft briefing generated — 2 themes, 5 sources. Two checks fail: outlet diversity, claim sourcing."
  - ✓ line: "Good. Now we know exactly what to fix."
- **Copy-paste / prompts**: these are rendered transcript `PromptLine`s, NOT copy buttons. No copy button. (See MASTER LIST note: the original deck has NO copy-to-clipboard buttons anywhere — prompts are illustrative transcript text.)
- **Stepped reveals**: header (120ms) → bullets+callout (280ms) → first-draft window (420ms).
- Timers: none.

## 23 — Step 3 Test (`23-step3-test`)

- `StepHeader` step=3/06 "Evaluate on 3 fresh examples" / goal "The skill must do the work, not the leftovers of your conversation." (3 dots filled.)
- Left: 3 bullets (`/clear` or fresh session, keep examples in a folder, good-enough?→delivery else next step) + **Callout (tone=tip)**: "Three test cases cost nothing today and save a paralyzed migration in six months…".
- **DIAGRAM — AppWindow "radar — clean-room test" (kind=app)** (right):
  - `PromptLine`: "/clear" → "Context cleared."
  - `PromptLine`: "Run the press-briefing skill on tests/example-2.md" → "Briefing generated. Checks: 4 / 5 pass."
  - **ASCII file-tree visualization** (mono): `tests/ ├─ example-1.md · AI in banking / ├─ example-2.md · EU tech regulation / └─ example-3.md · competitor moves`.
- **Stepped reveals**: header (120ms) → bullets+callout (280ms) → clean-room window (420ms).
- Prompts (transcript only, no copy button)/timers: none.

## 24 — Step 4 Observability (`24-step4-observability`)

THE eval/observability matrix drawn as a component. **DIAGRAM — Evaluation matrix (criteria × examples), CSS grid:**

- `StepHeader` step=4/06 "See inside your agent" / goal "Score every example at once. A criterion that fails across the board is the systematic weakness, not bad luck on one run." (4 dots filled.)
- Left: 3 bullets (ask for a visual dashboard with `/frontend-design`; read by row=systematic gap / by column=broken example; the average is the single number to move).
- **Matrix** (right), titled "radar — evaluation matrix", header right shows "average **64%**" (computed):
  - **Rows = 5 criteria** (down): "≥ 3 outlets per theme", "Articles < 7 days old", "Each claim sourced", "1 implication per theme", "Reads in under 3 min".
  - **Columns = 5 examples** (across): E1, E2, E3, E4, E5 + a trailing "rate" column.
  - **Cells** = pass/fail chips: `✓` emerald on emerald-tint / `✗` red on red-tint. The literal GRID (rows×cols, true=pass):
    - Row1 (≥3 outlets): ✓ ✓ ✓ ✓ ✓ → 100%
    - Row2 (<7 days): ✓ ✓ ✗ ✓ ✓ → 80%
    - Row3 (each claim sourced): ✗ ✗ ✓ ✗ ✗ → 20% (the RED ROW = the bottleneck)
    - Row4 (1 implication): ✓ ✓ ✓ ✓ ✗ → 80%
    - Row5 (<3 min read): ✗ ✓ ✓ ✗ ✓ → 60%
  - **Per-row "rate" %** column (right). **Score footer row**: per-column score `n/5` (E1=3/5, E2=4/5, E3=4/5, E4=3/5, E5=4/5) + total average **64%** bottom-right (computed: 16/25).
  - Below the matrix: caption "Row 'each claim sourced' is red across the board, that is the bottleneck."
- Grid template: `minmax(0,1fr) repeat(5, 44px) 64px`. Computed live via `rowRate`/`colScore`/`pct`.
- **Stepped reveals**: header (120ms) → bullets (280ms) → matrix (420ms).
- Prompts/timers: none.

## 25 — Step 5 Bottleneck (`25-step5-bottleneck`)

- `StepHeader` step=5/06 "Improve one bottleneck at a time" / goal "Several problems will show up. Pick the most pressing one, ignore the rest." (5 dots filled.)
- Left: 4 bullets (try your instinct first; else deep-research things-to-try and let the agent iterate; validate against tests, new failure→new test case; complexity must earn its place) + **Callout (tone=tip, title="Why the discipline")**.
- **DIAGRAM — "The inner loop" panel** (right): a bordered rounded card, mono header (Repeat icon) "The inner loop", then 3 vertical numbered rows (mono index + label):
  - `03` "Evaluate on fresh examples"
  - `04` "Observe what fails inside"
  - `05` "Improve the one bottleneck"
  - footer (mono): "Repeat until the tests pass".
  - (The 03→04→05 cycle shown vertically as a stack.)
- **Stepped reveals**: header (120ms) → bullets+callout (280ms) → inner-loop panel (420ms).
- Prompts/timers: none.

## 26 — Step 6 Understand (`26-step6-understand`)

- `StepHeader` step=6/06 "Understand what you built" / goal "The agent did the typing. Make sure you still own the thinking." (6 dots filled, all.)
- Left: 3 bullets ("Thinking is not understanding…"; ask the agent to teach you via `teach-me` / `make-me-understand`; have it generate diagrams).
- **DIAGRAM — AppWindow "radar — understanding pass" (kind=app)** (right): a simulated quiz transcript:
  - `PromptLine`: "Teach me how the press-briefing skill works, step by step. Quiz me."
  - reply Q1: "when an article has no named author, what does the pipeline do with it?"
  - `PromptLine`: "It gets dropped at the filter step?"
  - reply: "Almost: it is kept but flagged, the sourcing check is what fails it. Want the diagram of the four steps?"
- **Stepped reveals**: header (120ms) → bullets (280ms) → understanding-pass window (420ms).
- Prompts (transcript only)/timers: none.

## 27 — Loop Recap (`27-loop-recap`)

- **DIAGRAM — Flow (6-node horizontal progression)** via `Flow`: 6 numbered nodes on one connector line with chevrons:
  - 01 "Clarify" / "Deep research, the Pareto, binary checks."
  - 02 "Draft" / "A minimal A→Z version, tools and eval wired in."
  - 03 "Evaluate" / "3 fresh examples, clean context, scored."
  - 04 "Observe" / "Dashboard the steps, find the red row."
  - 05 "Improve" / "One bottleneck, proven by the matrix."
  - 06 "Understand" / "Have it teach you the system."
- **Loop pill**: a dashed orange-border rounded pill (Repeat icon): "**Evaluate → Observe → Improve** loops until it is good enough".
- Closing line: "This is your map for the next two hours."
- **Stepped reveals**: header (120ms) → Flow (300ms) → loop pill (440ms) → closing line (560ms).
- Prompts/timers: none.

## 28 — Sovereignty (`28-sovereignty`)

- Intro line + 3-up **PATH cards** (sovereign chain), each: mono index `01–03` + title + body + mono footer:
  - 01 "A model-agnostic agent" — "OpenCode, open source, deployable internally, plugs into any provider." — `opencode.ai`
  - 02 "Sovereign inference" — "Self-hosted vLLM, or EU sovereign APIs: Mistral La Plateforme[1], Scaleway[2]. EU-hosted, GDPR, OpenAI-compatible." — `mistral · scaleway`
  - 03 "Open-weight models" — "Mistral, Qwen, Gemma — shortlist per use case, runnable locally via Ollama." — `ollama run …`
- **Callout (tone=security, title="Field note")**: "Seen at a CAC40 client: organization policy mandates API keys and blocks local models…".
- Sources: [1] help.mistral.ai · [2] scaleway.com.
- **Stepped reveals**: header (120ms) → intro (260ms) → 3 cards (360, 470, 580ms) → field-note callout (720ms).
- Prompts/timers: none. (No diagram; conceptual card row.)

## 29 — Data Hygiene (`29-data-hygiene`)

- 2×2 grid of **RULES cards**, each mono index + title + body (+ optional mono code chip):
  - 01 "Separate primary from processed" — "Primary sources on one side, AI-generated outputs on the other, never mixed…"
  - 02 "Keep sensitive data out of context" — "`.claudeignore` excludes folders…" mono `.claudeignore`
  - 03 "Read-only by default" — "Reference data is mounted read-only…"
  - 04 "Mind the destination" — "Sensitive code and data don't leave for non-EU clouds…"
- **Stepped reveals**: header (120ms) → 4 cards (280, 390, 500, 610ms).
- Prompts/timers: none. (No diagram.)

## 30 — Orchestration Patterns (`30-orchestration-patterns`)

- **Visuals**: NOT code-drawn — 5 PNG schema figures (Anthropic "Building Effective Agents" canonical diagrams), each `/figures/orch-*.png` (white bg, cover-cropped to 142px height, in a `Schema` card with name + caption):
  - `orch-prompt-chaining.png` — "Prompt chaining" / "Sequential calls, a gate check between each"
  - `orch-routing.png` — "Routing" / "Classify first, then send to a specialist"
  - `orch-parallelization.png` — "Parallelization" / "Same task split, or voted by several"
  - `orch-orchestrator-workers.png` — "Orchestrator – workers" / "The agent decomposes at runtime"
  - `orch-evaluator-optimizer.png` — "Evaluator – optimizer" / "One generates, one scores, loop"
- **6th grid cell (code-drawn takeaway card)**: orange-border tint card — "All five are **doable with skills**, no framework required." + "Start at the top, only climb the ladder when the simpler pattern stops being enough." cite `[1]`.
- Source: [1] anthropic.com/research/building-effective-agents.
- **Stepped reveals**: header (120ms) → 5 schema cards (240, 330, 420, 510, 600ms) → takeaway card (690ms).
- Prompts/timers: none.
- (NOTE for recreation: the deck title in CLAUDE.md mentions "Three patterns" but the original here renders FIVE PNG schemas. The 5 PNGs are assets; to make this fully code-drawn you'd redraw all five with `DiagNode`/`DiagEdge`.)

## 31 — LLM Judge (`31-llm-judge`)

THE majority-vote visualization. **DIAGRAM — Judge vote row (CSS):**

- Left: 4 bullets (LLM judging is noisy; sample 3 or 5 times, odd number; small law of large numbers; small model like Haiku usually enough) + **Callout (tone=tip, title="Always validate the judge")**: "…check the judge's majority vote against your own labels… Only trust it past **≥ 80% agreement**." cite `[1]`.
- **Vote diagram** (right), bordered card:
  - Mono prompt label: "Is this briefing properly sourced?"
  - **5 vote boxes** in a row (64×64 rounded squares), each ✓ (emerald border+text) or ✗ (red border+text). The literal VOTES: ✓ ✓ ✗ ✓ ✗.
  - A mono `→` arrow, then the **verdict box** (orange border + tint): "✓ yes" + mono "3 / 5".
  - Below: "Five samples, one stable verdict. Use it inside your binary checks whenever a criterion needs judgment."
- Source: [1] hamel.dev.
- **Stepped reveals**: header (120ms) → bullets+callout (260ms) → vote diagram (420ms).
- Prompts/timers: none.

## 32 — Meta Improvement (`32-meta-improvement`)

- 2×2 grid of **PRACTICES cards** (icon + title + body):
  - `lessons.md` (NotebookPen) — "Referenced from CLAUDE.md, the agent writes down what it learns: every mistake becomes a rule."
  - "Wrap-up skill" (CheckCheck) — "A skill that runs at session end: update the lessons, file the test cases, leave the repo clean."
  - "Auto-improve" (RefreshCcw) — "Hand the agent its own eval scores and let it iterate on its skills against the tests."
  - "Ablation" (Scissors) — "Regularly try removing complexity. If the tests still pass without it, it never earned its place."
- **Stepped reveals**: header (120ms) → 4 cards (280, 390, 500, 610ms).
- Prompts/timers: none. (No diagram.)

## 33 — Your Turn (`33-your-turn`)

- 3-up **OfferCard** project cards (icon + audience tag + headline + 3 `→` bullets + chip):
  - **Scout** (Radar icon) — "Competitive intelligence" — bullets: briefing on competitors' AI moves; public data sources; "Demo angle: live briefing on 2 competitors" — chip "Strategy"
  - **Radar** (Newspaper) — "Press review" — bullets: daily executive briefing; news + business press; "Demo angle: today's briefing, generated live" — chip "The one we built together"
  - **Talent** (UserCheck) — "CV scoring" — bullets: score/rank CVs against a role; sample CVs+role cards in repo; "Demo angle: a justified shortlist in minutes" — chip "People"
- Closing line: "All three are **finishable within the time box**… Same method for each: clarify, draft, test, observe, fix, understand."
- **Stepped reveals**: header (120ms) → Scout (280ms) → Radar (400ms) → Talent (520ms) → closing line (660ms).
- Prompts/timers: none. (No diagram.)

## 34 — Starter Kit (`34-starter-kit`)

- **DIAGRAM — AppWindow "lab repo" file tree** (left): titled "lab repo — one folder per project". ASCII tree (mono):
  - `scout/ · radar/ · talent/`
  - `├─ brief.md` — the goal, the demo angle
  - `├─ research/` — deep research, pre-run for you
  - `├─ tests/` — 3 cases: CVs, role cards, themes
  - `├─ CLAUDE.md` — standing instructions, ready
  - `└─ skills/` — empty, that's your job
- Right: 3 bullets (briefs/research/tests already in repo, start at step 2; web search + fetch pre-wired; add new failures to tests/).
- **Stepped reveals**: header (120ms) → repo-tree window (280ms) → bullets (420ms).
- Prompts/timers: none.

## 35 — Demo Time (`35-demo-time`)

- Left: title "**Demo time**", eyebrow "12:00 · all labs reunite", line "Each lab selects **2 projects**…", + a highlighted orange-border tint callout box: "A finished project beats an impressive one that does not run." + "Scope tight, run it end to end twice before you raise your hand."
- Right: framed PHOTO `photos.groupScale` ("Live demos, full room…"). Not code-drawn.
- **Stepped reveals**: header (120ms) → photo (300ms) → 2-projects line (280ms) → highlighted box (400ms).
- Prompts/timers: none. ("12:00" is static text, not a countdown.)

## 36 — Take Home (`36-take-home`)

- Left: title "Take it **home**", 3 takeaway rows (icon + title + body):
  - "Set the routine, now" (CalendarClock) — "Your press briefing emails itself every morning at 8. We configure it together before you leave."
  - "It all runs on your machine" (ShieldCheck) — "Everything you built today is yours…"
  - "IQ stays in the loop" (MessageCircle) — "Questions next week, next quarter: iq-project.ai, we answer."
  - + sign-off mono line "Thank you — IQ Project × Capgemini".
- Right: framed PHOTO `photos.groupCohort` ("See you at the next build"). Not code-drawn.
- **Stepped reveals**: header (120ms) → photo (300ms) → 3 takeaways (280, 400, 520ms) → sign-off (680ms).
- Prompts/timers: none.

---

# Copy-paste prompts / copy buttons — SUMMARY

**There are ZERO copy-to-clipboard buttons in the original deck.** All prompt text appears as illustrative, non-interactive transcript lines (`PromptLine` = orange `❯` prefix) inside `AppWindow` simulations. For completeness, the verbatim prompt-shaped lines shown (slide → text):

- **07** Agent Loop: "Find me an Asian restaurant for Tuesday night"
- **17** Permissions: "Draft the briefing and save it to reports/"
- **22** Step 2: "Read @research/what-makes-a-great-briefing.md, then /brainstorm a press-briefing skill" · "Build it and run it once, A to Z, text output only"
- **23** Step 3: "/clear" · "Run the press-briefing skill on tests/example-2.md"
- **26** Step 6: "Teach me how the press-briefing skill works, step by step. Quiz me." · "It gets dropped at the filter step?"

(If the redesign adds copy buttons, these are the canonical strings to wire.)

# Timers / countdowns — SUMMARY

**There are ZERO live timers/countdowns in the original deck.** All durations are static text labels in the Agenda Flow and headers:
- Slide 02 Agenda: "10 min", "45 min", "2 h 15", "30 min" (static node labels).
- Slide 33 Your Turn: eyebrow "2 h 15 · hands on" (static).
- Slide 35 Demo Time: "12:00" (static text).

# Stepped reveals — SUMMARY

No click-advanced sub-steps exist; every "reveal" is a one-shot staggered `Rise` entrance on slide load (delays listed per slide above). The slowest/most deliberate is **slide 06 Definition** (5 clauses revealed at 300/440/580/720/860ms — the intentional fragment-by-fragment build). Numbered build-ups also on **08** (LLM → connector → 5 blocks) and **16** (window blocks → 4 ideas).

---

# MASTER LIST — every distinct code-drawn diagram component (flat checklist)

SVG / CSS / JS figures drawn in code (NOT PNG assets):

1. [ ] **Flow — Agenda 4-node progression** (slide 02) — horizontal numbered nodes + connector + chevrons (`Flow` atom).
2. [ ] **CommitProgression** (slide 03) — `0% → 4% → 10%` with labeled time arrows ("~1 year", "6 weeks").
3. [ ] **BigStat ×2** (slide 03) — "$2.5B", "76%" gradient stat cards.
4. [ ] **Definition build-up** (slide 06) — 5 numbered gradient clause fragments.
5. [ ] **AppWindow transcript — agent session / Asian restaurant** (slide 07).
6. [ ] **LoopDiagram (SVG) — Think→Act→Observe circle** (slide 07, `LoopDiagram.tsx`) — 3 nodes + 3 curved arrows + center "until the goal is reached".
7. [ ] **Agent = LLM + harness schema** (slide 08) — LLM node + connector + 5 harness block cards (Tools/Skills/Memory/Sandbox/Orchestration).
8. [ ] **MeshDiagram (SVG) — Without MCP, M×N** (slide 09) — 3 agents × 4 tools full mesh (12 edges).
9. [ ] **HubDiagram (SVG) — With MCP, M+N** (slide 09) — 3 agents → MCP hub → 4 tools (7 accent edges).
10. [ ] **AppWindow — SKILL.md walkthrough** (slide 10) — name/description + "loaded on demand" divider pill + 5-step recipe.
11. [ ] **AppWindow — MEMORY.md index** (slide 11) — index lines → hash filenames.
12. [ ] **Sandbox nested-boxes reach diagram (CSS)** (slide 12) — machine ⊃ permissioned ⊃ launch-folder, with chips.
13. [ ] **AppWindow — CLAUDE.md sample** (slide 15) — Radar rules/commands markdown.
14. [ ] **Context-window stacked block diagram** (slide 16) — 3 color-family blocks (System/Tools/Conversation) + Free-space strip + "rebuilt every turn" badge; rows are mono tag+detail chips.
15. [ ] **4 numbered ideas list** (slide 16) — context-engineering principles (numbered circles).
16. [ ] **AppWindow — permission request dialog (kind=app)** (slide 17) — write-request card + Allow once/always/Deny chips + ask·plan·auto mode strip.
17. [ ] **AppWindow — first-draft build transcript** (slide 22).
18. [ ] **AppWindow — clean-room test + ASCII tests/ tree** (slide 23).
19. [ ] **Evaluation matrix (criteria × examples), CSS grid** (slide 24) — 5×5 ✓/✗ cells, per-row rate %, per-col score, computed 64% average, red-row bottleneck.
20. [ ] **Inner-loop panel (vertical 03→04→05)** (slide 25) — "Repeat until the tests pass".
21. [ ] **AppWindow — understanding-pass quiz transcript** (slide 26).
22. [ ] **Method spine + optional loop diagram** (slide 20) — `01 Clarify › 02 Draft › 03 Evaluate › 06 Understand` spine + dashed loop panel `03→04→05→back to Evaluate`.
23. [ ] **Flow — Loop Recap 6-node progression** (slide 27) — Clarify→…→Understand + Evaluate→Observe→Improve loop pill.
24. [ ] **Judge vote row (CSS)** (slide 31) — 5 ✓/✗ boxes → "✓ yes 3/5" verdict box.
25. [ ] **AppWindow — lab repo file tree** (slide 34) — scout/radar/talent project tree.
26. [ ] **Orchestration-patterns takeaway card** (slide 30) — code-drawn 6th cell only (the 5 pattern schemas themselves are PNG assets).

Shared atom-level figures reused above: `BigStat`, `StepHeader` (steps 1–6 progress dots, slides 21–26), `Callout` (security/risk/tip strips throughout), `OfferCard` (slide 33 project cards), `DiagNode`/`DiagEdge` (slides 09), `LineChart` (defined in `_charts.tsx`, NOT used on any slide — slides 04/05 use authoritative PNGs instead).

**PNG-asset visuals (not code diagrams), for completeness:** cover photo (01), 3 presenter photos (01b), METR chart (04), Epoch chart (05), Claude Code screenshot (14), 5 orchestration-pattern schemas (30), demo/cohort photos (35, 36).

---

## Totals

- **Distinct code-drawn diagram components: 26** (master-list items above).
- Plus reused atom figures: 2 `BigStat`, 6 `StepHeader` instances, ~10 `Callout` strips, 3 `OfferCard`s.
- **Copy buttons: 0.** **Live timers/countdowns: 0.** **Click-stepped reveals: 0** (all entrances are one-shot staggered `Rise` animations).
- Inventory file path: `/home/ezalos/42/Markdowns2Teach/docs/talks/capgemini-ai-agents/diagram-inventory-original.md`
