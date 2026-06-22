<!-- ABOUTME: Exhaustive slide-by-slide inventory of every code-drawn diagram, copy-paste prompt, timer, and stepped reveal in the latest Capgemini "AI Agents Tech Lab" deck. -->
<!-- ABOUTME: Recreation reference — enough detail (nodes, labels, layout, colors, behavior, verbatim prompt text) to rebuild each in vanilla HTML/CSS/SVG/JS without the original. -->

# Capgemini "AI Agents Tech Lab" — Diagram & Interactive Inventory (latest)

Source deck: `/home/ezalos/Pro/wt-iqdeck/apps/iq-project/src/decks/clients/capgemini/`
Deck definition: `tech-lab.ts` (40 slides imported; `31-starter-kit` exists on disk but is **NOT imported** — excluded from the live deck).

Brand palette (shared across all diagrams):
- **Brand orange** `#f97316` (aka `rgba(249,115,22,…)`), light tint `#fb923c` / `#fdba74`.
- **Amber** `#fbbf24` / amber-300/400 — scoped strictly to security / risk / "low-timer" / "values to verify".
- **Emerald** = reserved for "progress / pass"; **red** = "fail".
- Surfaces: `bg-white/[0.02]` cards, `border-white/10` hairlines, black canvas. Mono font for labels/captions, display font for headlines.
- Text tokens: `fg1` brightest → `fg4` dimmest; `fg-accent` = orange text.

Recurring chrome (every non-cover slide) = `Frame` (`_chrome.tsx`): co-branded masthead (IQ logo · divider · Capgemini logo · section eyebrow · `NN / total` page number), a drawn hairline rule, centered content `main`, optional **Sources** footnote line (`[n] domain` links), footer (`IQ Project · AI Agents Tech Lab — Capgemini` / `June 18, 2026`). Not catalogued per-slide below unless load-bearing.

Shared reusable components live in:
- `_atoms.tsx` — Callout, AppWindow, PromptLine, ToolCall, DiagramFrame, FigureImage, StepHeader, **CountdownTimer**, **CopyPromptButton**, BigStat.
- `_charts.tsx` — LineChart, DiagNode, DiagEdge (**all three currently UNUSED** by any live slide; the charts they were built for are now PNG figures rendered via `FigureImage`).
- `_chrome.tsx` — Frame, Eyebrow, DisplayTitle, Grad, Cite, CornerTicks, Rise, FramedMedia, OfferCard, **Flow**.

Stepped slides use deck-kit `<Appear at={k}>` (reveals/reserves layout at step k) and `StepContext` (current step int). `steps:` count is declared in `tech-lab.ts`.

---

## 01 — Cover

- **Diagrams:** none drawn in code. Visual is a framed **photo** (`FramedMedia`, `euronextHackathon2`) — out of scope.
- Custom masthead (not `Frame`): `NN / total`, drawn rule, dossier metadata strip (`Executive Lab · AI Agents`), title `AI Agents / Tech Lab`, byline `Louis Develle`.
- No prompts, timers, steps.

## 02 — Instructors

- **Diagrams:** none. Three bio **cards** (CSS grid, `grid-cols-3`, alternating vertical offset `translate-y-8` on cards 1 & 3 for a staggered look). Each card: square headshot photo (96×96, rounded, orange border), name (display), role (mono orange uppercase), bullet list with orange `→` markers.
- Card data: Louis Develle (Research engineer & teacher). [Single-instructor for reuse — co-instructor bios removed.]
- No prompts, timers, steps.

## 03 — Agenda

- **Diagram — "Morning Flow" (`Flow` component, `_chrome.tsx`).** Horizontal numbered progression, 4 steps left→right.
  - Layout: CSS grid `repeat(4, 1fr)`; a gradient connector line at y≈28px runs from node 1 to node N (`from-brand/10 via-brand/50 to-brand/70`); a `›` chevron sits midway between each pair of bubbles.
  - Each node: a 56×56 circle with 2-digit number (`01`…`04`, display font, orange border `border-brand/40`), then title (display), an orange mono "players" sub-label, and a body line.
  - Steps (title / players / body):
    1. **Understand** — "Demos all along" — "What agents are and how Claude Code works, everything shown live, never just told."
    2. **Sprint 1** — "10 min · Hands on" — "First touch: 80 CVs, one role, you pick the candidates with Claude Code."
    3. **Sprint 2** — "20 min · Your agent" — "You build a press-review agent on your own topics, with the method we show you."
    4. **The build** — "1 h · Slide machine" — "You leave with a slide-generation system in Capgemini colors, plus a morning routine."
  - (`Flow` also supports an emerald "progress" accent variant — not used here.)
- No prompts, timers, steps.

## 04 — Intelligence is now a commodity

- **Diagram — two-card "Until now vs Today" comparison** (CSS `grid-cols-2`).
  - Left card (neutral, `border-white/10`): Brain icon, mono label "Until now", headline "Buying intelligence meant hiring someone", body about scarce/slow/headcount-bound.
  - Right card (accented, `border-brand/40 bg-brand/[0.04]`): ShoppingCart icon, orange label "Today", headline "You buy it like a raw material", body "On tap, by the unit…".
  - Below: full-width callout strip (Zap icon) — "Raw intelligence only talks. An agent is what puts it to work…".
- No prompts, timers, steps.

## 05 — Crazy numbers

- **Diagram — three `BigStat` figure tiles** (`_atoms.tsx`, `grid-cols-3`). Each tile: optional icon, huge gradient number (84px display, orange gradient text), label paragraph with inline `<Cite>` superscripts, mono source line, optional "verify" amber chip.
  - Tile 1: icon = **Claude Code mascot** (`marks.claudeCodeMascot` SVG, 44×44); value **"10% of all commits"**; label "of all public GitHub commits are now authored by Claude Code, one single agent — a share that jumped from 4% in six weeks. [1,2,5]"; source "SemiAnalysis · CoreMention, Feb–Mar 2026".
  - Tile 2: icon = Claude Code mascot; value **"$2.5B revenue"**; label "annualized revenue for Claude Code alone… [3]"; source "VentureBeat, Feb 2026".
  - Tile 3: no icon; value **"76% support resolution"**; label "…resolved autonomously by Intercom's Fin, at $0.99 per resolution, paid only on success. [4]"; source "Intercom, vendor-reported".
- Sources footnote line [1] semianalysis.com [2] coremention.com [3] venturebeat.com [4] fin.ai [5] anthropic.com.
- No prompts, timers, steps.

## 06 — METR curve

- **Figure — METR time-horizon chart (PNG, not code-drawn).** Rendered via `DiagramFrame` wrapper around `FigureImage(figures.metrTimeHorizon)`.
  - `DiagramFrame`: rounded card, title row "Length of tasks completed autonomously · 50% success", mono caption "Source: METR, time-horizon benchmark", optional amber "Values to verify" chip (not set here). `FigureImage` puts the white-bg PNG on a white card so it reads on black.
  - To recreate the underlying chart natively you could use `_charts.tsx`'s `LineChart` with `logY` — but the deck ships a PNG.
- Right column: two prose lines (a few minutes → hours of autonomous work; doubles ~7 months [1,2]).
- No prompts, timers, steps.

## 07 — Cost collapse

- **Figure — Epoch AI inference-price chart (PNG).** Same `DiagramFrame` + `FigureImage(figures.epochInference)` pattern.
  - DiagramFrame title "Price for the same benchmark score · $ per million tokens", caption "Source: Epoch AI — log scale".
- Right column: prose + a **`Callout` (tone="tip", title="The takeaway")** — bordered strip, Lightbulb icon, orange-tinted: "'Too hard' or 'too expensive' are bad reasons not to start…".
- No prompts, timers, steps.

## 08 — LLM + harness ("Your agent is a new hire")  ·  STEPPED (steps: 11)

- **Diagram — six FLIP CARDS** (`FlipCard.tsx`, 3D CSS flip). The signature analogy diagram.
  - Layout: 3×2 CSS grid (`grid-cols-3`), each card 240px tall, `perspective: 1200`, `transformStyle: preserve-3d`, 650ms `rotateY` transition (snaps instantly on backward nav).
  - **Front face = "Your hire" (human)**: neutral border `border-white/12`, grey icon, top-right mono label "Your hire", title (display 32px), body (22px).
  - **Back face = "Your agent" (agent)**: orange border `border-brand/60 bg-brand/[0.05]`, orange icon, top-right orange label "Your agent", same title/body layout (`rotateY(180deg)`, backface hidden).
  - **The six cards (front → back):**
    1. ScrollText **The rulebook** ("Day one: how we work here…") → FileCode2 **Instructions** ("CLAUDE.md, standing instructions read at every session.")
    2. KeyRound **The accesses** ("Your accounts: Teams, SharePoint, Outlook…") → Wrench **Tools** ("How it touches the world: CLI, APIs, MCP connectors.")
    3. NotebookPen **The experience** ("Meeting notes, client quirks…") → Database **Memory** ("What it keeps between sessions, plain files first.")
    4. GraduationCap **The training** ("…review a contract, screen CVs, brief the press.") → BookOpen **Skills** ("Recipes it knows how to follow, plain markdown.")
    5. Laptop **The laptop** ("Your machine, your folders…") → Box **Sandbox** ("Where its code runs, and how far it can reach.")
    6. TrendingUp **The promotion** ("…you staff a team.") → Workflow **Orchestration** ("Subagents it briefs, runs and coordinates.")
  - Note the card order (Memory BEFORE Skills) mirrors the later harness tour.
- **Above the grid — "LLM" capsule**: a centered pill (`border-brand/40`) with big gradient "LLM" + divider + "The hire arrives brilliant… Day one is everything else."
- **STEP CHOREOGRAPHY (11 steps):** card *i* (1-based) **appears** at step `2·i−2` and **flips** to its agent back at step `2·i−1`. Card 1's front is visible at step 0. So the rhythm across steps 1–11 is appear, flip, appear, flip… (`<Appear at={2*i}>` gates appearance; `flipAt={2*i+1}` gates the flip). Print/export shows all six flipped to the agent side.
- Sources: [1] sebastianraschka.com.

## 09 — Definition ("What is an agent?")

- **Diagram — five-fragment numbered build-up** (vertical list, staggered `Rise` reveals via animation delay, NOT step-gated).
  - Each row: a `01`…`05` mono index (dim) + a large display line where one accent word is orange-gradient (`<Grad>`):
    1. "An agent is a **system**"
    2. "which uses **tools**"
    3. "to interact **repeatedly**"
    4. "with its **environment**"
    5. "to accomplish its **goal**"
  - Closing prose: "Not a chatbot, not a single prompt. A loop that acts, observes, and acts again…".
- Sources: [1] anthropic.com (building-effective-agents).
- No copy prompts/timers. (Reveals are time-staggered, not presenter-stepped.)

## 10 — Agent loop ("One goal, many small steps")  ·  STEPPED (steps: 10)

Two synchronized visualizations + a top-right progress rail, all driven by `StepContext`.

- **Diagram A — `LoopDiagram` (`LoopDiagram.tsx`), the Think→Act→Observe cycle drawn natively in SVG.** viewBox `0 0 540 480`.
  - Three rounded-rect **nodes** on a circle (center CX=270, CY=240, radius R=150), each 184×72, rx=14, orange border:
    - top (angle −90): **Thought** / sub "what next?" (`phase: think`)
    - lower-right (angle 30): **Action** / sub "use a tool" (`phase: act`)
    - lower-left (angle 150): **Observation** / sub "read the result" (`phase: observe`)
  - Three **curved arrows** (SVG arcs along radius R, 26° gap trimmed each end, arrowhead marker `loop-arrow`) connecting Thought→Action→Observation→Thought (clockwise).
  - Center text (2 lines): "until the goal / is reached".
  - **Active-phase highlight:** the node matching `activePhase` gets brighter fill/stroke (`rgba(249,115,22,0.10)` fill, near-opaque orange stroke, 2.2 width); the other two dim to opacity 0.35 (400ms transition). `activePhase="done"` lights all three.
- **Diagram B — the transcript inside an `AppWindow`** (terminal chrome: 3 traffic-light dots, mono title "agent session"). Fixed frame visible from step 0:
  - **GoalBar** (orange-tinted box, label "Goal"): "Find an Asian restaurant for Tuesday night in Paris".
  - **ToolStrip** (label "Tools", three pill chips each with an orange dot): `search_web`, `read_url`, `google_maps`.
  - Then 10 step-gated beats (`<Appear at={k}>`), each a `Beat` (Think = italic "Thinking: …"; Observe = "→ …") or a `ToolCall` (dim "● name — detail"):
    - 1 Think "To reach the goal, I should search the web first…"
    - 2 Act `search_web "best Asian restaurants Paris"`
    - 3 Observe "result #2: a top-10 of Asian restaurants in Paris"
    - 4 Think "The right one is probably in that list — let me read it."
    - 5 Act `read_url — the top-10 article`
    - 6 Observe "Bim Bim Bap, Châtelet, looks ideal"
    - 7 Think "Before I recommend it, I should check it's open Tuesday night."
    - 8 Act `google_maps "Bim Bim Bap Châtelet" — opening hours`
    - 9 Observe "open every day of the week"
    - 10 **Answer box** (orange-tinted): "Book Bim Bim Bap at Châtelet — open Tuesday night, great reviews, fits your group."
- **Diagram C — `ProgressRail`** (top-right of header, hidden on mobile): 10 dot+label pairs, label turns orange / dot fills brand when `step >= i+1`. Labels: Think, Act, Observe, Think, Act, Observe, Think, Act, Observe, **Answer**.
- **Step→phase map** (`PHASE_AT`): step 0 nothing; 1 think, 2 act, 3 observe, 4 think, 5 act, 6 observe, 7 think, 8 act, 9 observe, 10 done. One press = one beat across transcript + rail + loop node glow.
- Sources: [1] arxiv.org/abs/2210.03629 (ReAct).
- No copy prompts/timers.

## 11 — Meet Claude Code (LIVE DEMO)

- **Diagrams:** none code-drawn. Left = **screenshot PNG** of the real app (`figures.claudeCodeScreenshot`) in `FramedMedia`. Right = numbered "5-minute tour" checklist (5 items, each a numbered orange-bordered circle + text):
  1. Send a prompt, watch it think and act
  2. Resume a past session, nothing is lost
  3. Attach files with @path
  4. Browse the project files from the app
  5. The modes menu (auto mode comes after your first sprint)
- A "Live demo" pill (MonitorPlay icon) in the header.
- No prompts, timers, steps.

## 12 — Prompt structure ("A good prompt is a good brief")

- **Diagram A — four "parts" cards** (2×2 grid). Each: icon + title + body.
  - Compass **Context** · Target **Task** · ListChecks **Guidelines** · Ban **Constraints**.
- **Diagram B — annotated brief inside an `AppWindow` (kind="app", "one real brief").** A 3-column CSS grid `[auto_1px_1fr]`: left = section name (icon on top, right-justified, orange label) | center = vertical hairline divider | right = the real prompt text, per row:
  - **Context** | "this summary goes to a client COMEX, they read it on their phone between two meetings."
  - **Task** | "summarize the attached 40-page report."
  - **Guidelines** | "lead with the three decisions to make, plain business language, one source per claim."
  - **Constraints** | "one page max, nothing confidential quoted verbatim."
  - Caption below: "That is all prompting is: briefing a very fast intern…".
- No copy buttons (the brief is illustrative, not a copy target), no timers, no steps.

## 13 — Tools ("Harness · 5/6")

- **Diagram A — "Three ways to plug in" mini-list** (left column, ~300px). Three bordered rows, each icon + title + body:
  - Terminal **CLI** ("Anything your terminal can do: scripts, git, files.")
  - Globe **API** ("Web search, internal services, SaaS endpoints, called directly.")
  - Plug **MCP** ("A standard plug: one connector per tool, shared by every agent.")
- **Diagram B — "Tools you could connect today" bench** (right, 3-col grid of `ToolTile`s + one dashed note cell). Each tile: logo on a light chip (Outlook/Tavily/SharePoint/Notion/Teams SVGs from design-system), optional amber "read-only" lock badge, name (display), use line, and a Check + mono support status with `<Cite>`:
  - **Outlook** — "Read & triage mail" — "Official M365 connector" [2] — badge **read-only** (Lock icon).
  - **Tavily Search** — "Live web search & extract" — "Official MCP · claude mcp add" [3].
  - **SharePoint** — "Search docs & sites" — "Official M365 connector" [2].
  - **Notion** — "Read & write pages" — "Official Notion MCP server" [4].
  - **Teams** — "Read channels & chats" — "Official M365 connector" [2].
  - 6th cell (dashed, hidden on mobile): "Each one is proven by a real integration… The footnote links the proof."
- Analogy strip above ("Day one, your hire gets their accesses…") + a "Let's try it · live: read a Notion page" pill.
- **`Callout` (tone="security")** at bottom: "Every external tool or MCP server runs with your agent's permissions. Default to read-only…".
- Sources: [1] anthropic.com (MCP) [2] support.claude.com (M365) [3] github.com/tavily-ai/tavily-mcp [4] github.com/makenotion/notion-mcp-server.
- **No M×N MCP connector diagram in the live deck** (it is *not* present — the slide uses the tool bench above instead).
- No timers/steps. No copy buttons.

## 14 — Memory ("Harness · 3/6")  ·  STEPPED (steps: 4)

- **Diagram — two-level vertical ladder with reveal-on-the-right companions** (2-col grid `[1fr_1.05fr]`).
  - **Level 1** (left, `<Appear at={1}>`): number bubble `01`, players "Step 01 · In the moment", title **"Just ask"**, body "Tell it what to keep: 'remember Muriel reviews every external mail.'…".
  - Companion (right, `<Appear at={2}>`): an `AppWindow` titled **"memory/MEMORY.md"** showing a memory **index**:
    - `# Memory index`
    - "- We contract on the Microsoft suite only, never Google Workspace → it-stack.md"
    - "- Meeting invites to the VP need an agenda and one decision → vp.md"
    - "- Muriel reviews every external mail, keep them short → muriel.md"
    - footer "An index up top, detail in one file per fact — loaded on demand [1]".
  - **Level 2** (left, `<Appear at={3}>`): bubble `02`, players "Step 02 · .txt & .md", title **"Write it down"**, body about plain diffable files / index up top.
  - Companion (right, `<Appear at={4}>`): a **`Callout` (tone="tip", title="Why it matters")** — "A culture of written knowledge is the load-bearing asset…".
- **COPY BUTTON (slide 14):** `CopyPromptButton` label **"Copy the memory rule"** (under the MEMORY.md window, step 2). Copies VERBATIM:
  > We operate exclusively on Microsoft / Azure. We CANNOT sign with a counterparty that hosts or routes our data on Google Cloud / Google Workspace — doing so is impossible and deleterious.
- Sources: [1] anthropic.com (effective context engineering).

## 15 — Skills ("Harness · 4/6", LIVE DEMO)

- **Diagram — example skill inside an `AppWindow` ("skills/contract-review/SKILL.md").**
  - Header lines: `name: contract-review`, `description: Review a contract, flag risky clauses, report on one page` (keys in orange).
  - A divider chip "below: loaded on demand", then the 5 numbered recipe steps (dim):
    1. Read the contract, map the parties and scopes
    2. Walk every clause: IP, liability, insurance, data
    3. Flag each risk with the clause it comes from
    4. **Cross-check company memory for conflicts**  ← this is where the slide-14 memory rule fires
    5. Write a one-page report, risks first
  - Footer: "One folder, one markdown file. That is a skill."
- Right column: 3-bullet takeaway list (a skill is a markdown recipe [1]; agent sees name+description, loads steps on demand; ready-made libraries `superpowers`, `frontend-design`, `knowledge-work`) + **`Callout` (tone="security")** "External skills are instructions you didn't write… [2]".
- Analogy strip + "Let's try it · live: review an NDA" pill.
- **COPY BUTTON (slide 15):** label **"Copy the NDA review prompt"**. Copies VERBATIM:
  > /nda-analysis review @demos/nda-review/contracts/sample-nda.md
- Sources: [1] agentskills.io [2] snyk.io.

## 16 — Sandbox ("Harness · 1/6", LIVE)

- **Diagram — nested "reach" boxes** (concentric containment, the agent's reach diagram).
  - Outer box: mono label "Your machine".
  - Middle box (dashed border): "Other folders · system · network" + amber "permission required".
  - Inner box (orange border `border-brand/50 bg-brand/[0.06]`): label "The launch folder — the agent's reach", containing a commented **file tree** (mono, aligned):
    - `lab3-agentic-capgemini/`
    - `├─ CLAUDE.md   # the rulebook, read every session`
    - `├─ .claude/skills/   # cv-scoring · nda-analysis · press-synthesis…`
    - `├─ projects/   # the three exercises`
    - `└─ docs/   # drop your own files here`  (this row highlighted orange, `hot`)
- Right column: 4-bullet list (runs on your machine; scoped to launch folder; everything pre-wired, drop files in docs/; anything beyond folder is a granted right).
- Analogy strip + "Let's set it up · live" pill.
- **COPY BUTTON (slide 16):** label **"Copy the setup prompt"**. Copies VERBATIM:
  > You are in your working directory, read docs and install the packages, thanks

## (after 16) — Preview ("Harness · See it run")  [deck order: between sandbox and claude-md]

- **Diagrams:** none code-drawn. Left = **screenshot PNG** (`figures.claudeCodePreview`) of the app with the top-right panel menu open, on a white-bg framed figure. Right = numbered 3-point list:
  1. "Click the panel button, top right, then Preview — your app rendered live as the agent edits it."
  2. "Same menu holds Diff, Terminal, Files, Background tasks and Plan."
  3. "Keep it open while you build: every change lands in front of you in real time."
- "Top-right" pill (PanelRight icon).
- No prompts, timers, steps.

## 17 — Orchestration ("Harness · 6/6", LIVE)

- **Diagram — two-card "promotion" comparison** (`grid-cols-2`).
  - Left (neutral): TrendingUp icon, label "Your hire", headline "Too good to do it all alone", body about delegating.
  - Right (orange `border-brand/40`): GitFork icon, label "Your agent", headline "Subagents", body "An agent can staff other agents: brief three specialists in parallel… [1]".
  - Below: prose "Live now: three subagents prepare a negotiation, one on tech news, one on commercial moves, one on product, one hook sentence each."
- Sources: [1] sebastianraschka.com.
- No prompts/timers/steps.

## 18 — CV sprint  ·  TIMER

- **Diagram:** none code-drawn (left = three "challenge" cards: FolderOpen "The pile" + chip `1-talent-cv-scoring/data/cvs/`; FileText "The role · Sales Account Executive" + chip `…/data/jobs/sales-account-executive.md`; Trophy "The ask" + chip `/cv-scoring`).
- **TIMER (slide 18):** `CountdownTimer minutes={10} persistKey="cv-sprint"` — **10:00** countdown, no extend button. Right column, ~640px.
  - Behavior (from `_atoms.tsx`): giant face `clamp(120px,18cqi,260px)`, gradient text while running, **amber when < 60s left or done**; Start/Pause/Reset pill (Play/Pause icon). Deadline-based (no drift); `persistKey` survives navigating away and back (stored in a module-level `Map`). Buttons `stopPropagation` so they don't advance the slide. In PDF export it renders the static `10:00` face.
- No copy buttons. Not declared as `steps`.

## 19 — Permissions & auto mode

- **Diagram — permission-request mock inside an `AppWindow` (kind="app", "permission request").**
  - `PromptLine` (orange `❯`): "Draft the briefing and save it to reports/".
  - Orange-tinted request box: "Claude wants to write: reports/briefing-06-18.md" + three mono pill buttons: **Allow once** (orange), **Allow always** (dim), **Deny** (dim).
  - Mode line: "mode: ask · plan · **auto ←**" (auto highlighted orange).
- Left column: 3-bullet list (asks before acting [1]; auto mode pre-approves inside sandbox; extra rights granted in plain language) + **`Callout` (tone="tip")** "For the lab: turn auto mode on…".
- Sources: [1] docs.claude.com/iam.
- No prompts/timers/steps.

## 20 — CLAUDE.md ("Harness · 2/6")

- **Diagram — CLAUDE.md example inside an `AppWindow` ("~/.claude/CLAUDE.md").** Three commented sections (headers orange `fg1`):
  - `# Who I am` → "Paul, Capgemini COMEX member."
  - `# How you should behave` → "Do not use em-dashes or other AI tells when writing."
  - `# Things you should know` → "All our knowledge is on SharePoint, always check there if unsure."
- Right column: 3-bullet list (read at every session start, global or per-project [1]; home of what you'd repeat in every prompt; per-project ground truth + global) + a "Reference" mini-box: "Andrej Karpathy publishes his own CLAUDE.md… Link in your starter repo."
- Analogy strip above ("Every hire reads the internal rulebook on day one…").
- Sources: [1] docs.claude.com/memory.
- No prompts/timers/steps.

## 21 — Context engineering ("What the model actually sees")

- **Diagram — "The context window" zones column** (left, ~640px, `bg-black/40` framed card).
  - Header row: "The context window" + a "rebuilt every turn [1]" badge (RefreshCw icon, orange).
  - Three stacked **zone boxes**, each label (orange mono) + mono rows:
    - **System** (orange border `border-brand/40`): "CLAUDE.md · environment info" / "Skills index — name + description only" / "Memory index — one line per fact".
    - **Tools** (neutral border): "search_web(query) → results" / "fetch_page(url) → content" / "read_file(path) → text …".
    - **Conversation** (neutral): "Your message" / "Thinking · tool call · tool result (× many)" / "Agent answer · your next message".
  - Trailing dashed box: "Free space before the window is full".
- Right column: four numbered ideas (One text, stateless · Three zones · Progressive disclosure · A finite window).
- Sources: [1] anthropic.com (effective context engineering).
- No prompts/timers/steps.

## 22 — Thinking models ("The model and the brain")  [deck order: right after Meet Claude Code]

- **Diagram — two-card layout** (`grid-cols-2`).
  - Left: Brain icon, "The model", body "…today Claude Fable 5 leads FrontierCode Diamond… [1]" + dim note about cheaper models later.
  - Right: Gauge icon, "Thinking effort", body about reasoning length, set to `max` + dim note "everything runs at full effort".
  - Below: **`Callout` (tone="tip", title="Fast mode")** — "Turn fast mode on (/fast)…" + closing prose on budget-of-intelligence trade-off.
- Sources: [1] llm-stats.com/frontiercode.
- No prompts/timers/steps.

## 23 — Method overview ("Build agents that actually work")

- **Diagram — `MethodCycle` (shared with slide 30, defined at `30-loop-recap/MethodCycle.tsx`).** A native SVG row of **four linear boxes joined by straight arrows** (viewBox `0 0 1640 300`, centers at x = 200/580/960/1340, each box 320×108, rx=16):
  - `01` **Clarify** — sub "research, success criteria" (neutral).
  - `02` **Build** — sub "A→Z, tools wired" (neutral).
  - `03` **Test and improve** — sub "test → investigate → improve" — **accent** (orange fill `0.08`, stroke `0.8`, width 2). The inner loop lives in this subtitle; the diagram itself stays a straight row.
  - `04` **Deliver value** — sub "a deck, or your use case" — **terminal** (strongest orange: fill `0.12`, stroke `0.9`).
  - Arrows: orange lines with `cycle-arrow` arrowhead marker between consecutive boxes.
- Prose above/below describes building the Press Review agent live + "a skill, or a small collection of skills…".
- No prompts/timers/steps.

## 24 — Step 1: Clarify the goal  ·  COPY PROMPT  ·  STEP HEADER + MINI-MAP

- **Diagram A — `StepHeader` (`_atoms.tsx`):** "Step 01 / 04" mono counter + a row of `total` progress dashes (first `step` of them filled orange `bg-brand/80`, rest `bg-white/10`), big 64px title "Clarify the goal", goal line.
- **Diagram B — `MethodMiniMap` (`MethodMiniMap.tsx`), the "you are here" rail.** Absolutely positioned top-right (`right-28 top-[92px]`), hidden on mobile. SVG viewBox `0 0 360 46`: **4 nodes** in a horizontal run (x = 30/130/230/330) joined by short arrows (`minimap-arrow` marker), labels **Clarify · Build · Improve · Deliver**. The `active` node gets a filled orange dot + a soft orange halo ring + bold orange label; the others are dim grey dots / faint labels. Here `active="clarify"`.
- Body: 2-bullet list (use a deep research to clarify success criteria; works best on tasks you do well yourself) + **`Callout` (tone="tip", title="Where this runs")** "In the Claude app (deep research), not Claude Code…".
- **COPY BUTTON #1 (slide 24):** label **"Copy the research prompt"**. Copies VERBATIM (`CLARIFY_PROMPT`):
  > As a non technical person, I will create an agent system with claude code to do the following task:
  >
  > Press briefing, to understand what are the AI initiatives and projects ongoing among Capgemini competitors such as: Deloitte, PwC, EY, Accenture, ...
  >
  > I want you to deep-research about this task on two different axis:
  >
  > - What are the strongest fundamentals to achieve this task (the 20% of effort that produces 80% of the value)? I'm especially keen on using widely recognized frameworks that could be applied.
  > - My agent will iterate autonomously on making this task better, so I will need an excellent evaluation put in place. I'm looking for a sum of binary evaluation criteria. This applies to the complete workflow, as well as to each intermediate step if relevant.
  >
  > To tell you a bit more about myself, I'm a senior executive on the COMEX of Capgemini.
  >
  > Do not hesitate to ask me questions to better understand how this task is useful to me and context about my work so you can deliver the maximum possible value with your deep-research.
- (`StepHeader` total is overridden to 4 here.) No timer/steps.

## 25 — Step 2: Build the skill and use it  ·  TWO COPY PROMPTS

- **Diagrams:** `StepHeader` (Step 02 / 04, "Build the skill and use it") + `MethodMiniMap active="build"`. Body = a lead paragraph + a 3-bullet list (asks where the deep-research file is → minimal MVP; wires tools/data + picks 3 tests; builds and runs A→Z).
- **COPY BUTTON #1 (slide 25) — the big highlighted one:** label **"Don't wait for hours · copy the deep research"**, styled inverted (`!border-brand !bg-brand !text-black`). Copies the **entire raw Markdown file** `24-step1-clarify/deep-research.md` (imported with `?raw`, ~142 lines). It is the pre-run competitive-intelligence deep-research report (TL;DR + Key Findings + AXIS 1 frameworks: CI Cycle, Porter's Four Corners, Minto/BLUF, Admiralty code + AXIS 2: ~45 binary eval criteria). To make the button work, copy that file's full contents verbatim — see `slides/24-step1-clarify/deep-research.md`.
- **COPY BUTTON #2 (slide 25):** label **"Copy the build prompt"**. Copies VERBATIM (`DRAFT_PROMPT`):
  > Where is the deep-research file for this task? Tell me the path (or paste it), and read it first.
  >
  > Then /brainstorming a skill called press-review from that research: the most minimal MVP that can be evaluated against the binary checks in the document. Wire the tools and data access it needs now (web search, the test folder).
  >
  > You must choose three concrete tests that will be used to test and evaluate the skill. Make it easily retestable.
  >
  > Then build it and run it.
- No timer/steps.

## 26 — Step 3: Test and improve  ·  COPY (a full SKILL file)

- **Diagrams:** `StepHeader` (Step 03 / 04, "Test and improve") + `MethodMiniMap active="improve"`. Body = lead line ("improve your output and your workflow") + 3-bullet inner-loop list (shows rendered output in live preview, asks what's weak; you react with taste, fix goes into the skill, re-runs; loop until happy, improvement survives) + **`Callout` (tone="tip", title="Install the skill")** "Copy it into `.claude/skills/refine-from-preview/SKILL.md`, then start a new session so `/refine-from-preview` shows up."
- **COPY BUTTON (slide 26):** label **"Copy the refine-from-preview skill"**. Copies the **entire raw Markdown file** `26-step3-test/refine-from-preview.md` (`?raw`, ~138 lines) — a full `SKILL.md` with YAML front matter (`name: refine-from-preview`, long `description`) and the human-in-the-loop refine procedure. To make the button work, copy that file verbatim — see `slides/26-step3-test/refine-from-preview.md`.
- `tech-lab.ts` marks this slide `steps: 0` (no stepped reveals).

## (29) — Step 4: Deliver value  [component ValueDelivery, deck id "value-delivery"]  ·  COPY PROMPT

- **Diagrams:** `StepHeader` (Step 04 / 04, "Deliver value") + `MethodMiniMap active="deliver"`. Body = 3-bullet list (build a deck with `frontend-design` + `brainstorming`, no special generator; run the same method on it; free to pick a deck or any subject).
- **COPY BUTTON (slide 29):** label **"Copy the deck prompt"**. Copies VERBATIM (`DECK_PROMPT`):
  > /frontend-design use the result from the press briefing to generate a beautiful corporate deck, branded with the Capgemini look. The graphic chart is in @projects/3-deck-pptx-creation/brand/capgemini-brand.md
  > When the code is generated, you can use the boilerplate in @web/app/deck if useful.
- No timer/steps.

## 30 — Loop recap ("The method, end to end")

- **Diagram — `MethodCycle`** (same four-box linear SVG as slide 23, see §23 for full node/label/arrow spec: Clarify → Build → Test and improve(accent) → Deliver value(terminal)).
- Closing prose: "Clarify and build once, then test and improve, turning until every check is green, before value delivery…".
- No prompts/timers/steps.

## 32 — Press sprint ("Build your press agent")  ·  TIMER

- **Diagram:** none code-drawn (left = three cards: Newspaper "Your topics"; Route "The method, end to end"; CalendarClock "If you finish" → set the routine).
- **TIMER (slide 32):** `CountdownTimer minutes={20} extendMinutes={5} persistKey="press-sprint"` — **20:00** countdown WITH a **"+5 min"** extend button (Plus icon). Same behavior/persistence as §18. Eyebrow says "20 min".
- No copy buttons/steps.

## 33 — Deck sprint ("Generate Capgemini-grade decks")  ·  TIMER

- **Diagram:** none code-drawn (right = three big numbered display lines: `01` "Build it with frontend-design and brainstorming." · `02` "Refine it with the method you just learned." · `03` "Make it presentable, then present it.").
- **TIMER (slide 33):** `CountdownTimer minutes={60} extendMinutes={5} persistKey="deck-sprint"` — **60:00** countdown WITH **"+5 min"** extend, on the LEFT, left running through the build. Same behavior/persistence as §18.
- Footer prose teases the joker slides ("data sovereignty, data hygiene, orchestration patterns, LLM as judge, auto-improve").
- No copy buttons/steps.

## 34 — Sovereignty (JOKER)

- **Diagram — three-step "sovereign path" cards** (`grid-cols-3`), each: `01`/`02`/`03` mono index, title, body, mono footer tag:
  1. **A model-agnostic agent** — "OpenCode, open source, deployable internally…" — tag `opencode.ai`.
  2. **Sovereign inference** — "Self-hosted vLLM, or EU sovereign APIs: Mistral La Plateforme, Scaleway… [1,2]" — tag `mistral · scaleway`.
  3. **Open-weight models** — "Mistral, Qwen, Gemma… runnable locally via Ollama." — tag `ollama run …`.
- **`Callout` (tone="security", title="Field note")** "Seen at a CAC40 client: organization policy mandates API keys and blocks local models…".
- Sources: [1] help.mistral.ai [2] scaleway.com.
- No prompts/timers/steps.

## 35 — Data hygiene ("Four reflexes that age well", JOKER)

- **Diagram — four numbered rule cards** (`grid-cols-2`), each `01`–`04` index + title + body (+ optional mono tag):
  1. **Separate primary from processed** — "Primary sources on one side, AI-generated outputs on the other…".
  2. **Keep sensitive data out of context** — ".claudeignore excludes folders…" — tag `.claudeignore`.
  3. **Read-only by default** — "Reference data is mounted read-only…".
  4. **Mind the destination** — "Sensitive code and data don't leave for non-EU clouds…".
- No prompts/timers/steps.

## 36 — Orchestration patterns ("Five patterns, endless mileage", JOKER)  ·  STEPPED (steps: 5)

- **Diagram — five Anthropic schema FIGURES (PNGs) revealed one at a time.** 3-col grid; each cell is a card with a title + sub label and a `FigureImage` (PNG on a white card). `<Appear at={p.at}>` pops them left→right in increasing autonomy:
  1. **Prompt chaining** — sub "fixed steps, gated" (`orchPromptChaining`).
  2. **Routing** — sub "one call picks the lane" (`orchRouting`).
  3. **Parallelization** — sub "you decide the fan-out" (`orchParallelization`).
  4. **Orchestrator – workers** — sub "the agent staffs the work" (`orchOrchestratorWorkers`).
  5. **Evaluator – optimizer** — sub "one proposes, one judges" (`orchEvaluatorOptimizer`).
  - 6th cell (static, not gated): prose "Anthropic's five canonical patterns, in increasing autonomy. [1] All five are doable with skills, no framework required."
- Sources: [1] anthropic.com (building-effective-agents). The schemas themselves are PNG assets, not code-drawn.

## 37 — LLM as judge ("Never trust one vote", JOKER)

- **Diagram — majority-vote visualization** (right card). The exact code-drawn figure:
  - A question label (mono): "Is this briefing properly sourced?"
  - A row of **five vote chips** (80×80 rounded squares): verdicts `[✓, ✓, ✗, ✓, ✗]` — `✓` = emerald border/text, `✗` = red border/text.
  - A large `→` arrow, then a result chip (orange-tinted): "**✓ yes**" + mono "**3 / 5**".
  - Caption: "Five samples, one stable verdict…".
- Left: 3-bullet list (LLM judging is noisy; sample 3 or 5 times, odd number, majority vote [1]; small law of large numbers).
- Sources: [1] hamel.dev/blog/posts/llm-judge.
- No prompts/timers/steps.

## 38 — Meta-improvement ("Agents that improve themselves", JOKER)

- **Diagram — three practice cards** (`grid-cols-3`), each: icon-in-rounded-box + title + body:
  - RefreshCcw **Auto-improve** — "Hand the agent its own eval scores… Your press agent already has the evals, switch this on today."
  - CheckCheck **Wrap-up skill** — "A skill that runs at session end: write down what was learned, file the test cases, leave the repo clean."
  - Scissors **Ablation** — "Regularly try removing complexity. If the tests still pass without it, it never earned its place."
- No prompts/timers/steps.

## 39 — Demo time

- **Diagrams:** none code-drawn. Left = prose + an orange-tinted callout box ("A finished project beats an impressive one that does not run." + scope advice). Right = **photo** (`FramedMedia`, `groupScale`).
- No prompts/timers/steps.

## 40 — Take home

- **Diagrams:** none code-drawn. Left = three takeaway rows (CalendarClock "Set the routine, now"; ShieldCheck "It all runs on your machine"; MessageCircle "IQ stays in the loop") + thank-you line. Right = **photo** (`FramedMedia`, `groupCohort`).
- No prompts/timers/steps.

---

## MASTER LIST — every distinct code-drawn diagram component (flat checklist)

Shared / reusable diagram components:
- [ ] **Flow** (`_chrome.tsx`) — horizontal numbered progression w/ connector + chevrons. Used: slide 03 (Agenda).
- [ ] **MethodCycle** (`30-loop-recap/MethodCycle.tsx`) — native SVG 4-box linear method diagram (Clarify→Build→Test&improve(accent)→Deliver value(terminal)). Used: slides 23, 30.
- [ ] **MethodMiniMap** (`23-…/MethodMiniMap.tsx`, exported from 23 dir) — top-right SVG 4-node "you are here" rail (Clarify·Build·Improve·Deliver). Used: slides 24, 25, 26, 29.
- [ ] **StepHeader** (`_atoms.tsx`) — step counter + progress-dash bar + title/goal. Used: slides 24, 25, 26, 29.
- [ ] **CountdownTimer** (`_atoms.tsx`) — sprint chrono. Used: slides 18, 32, 33.
- [ ] **CopyPromptButton** (`_atoms.tsx`) — copy-to-clipboard prompt button. Used: slides 14, 15, 16, 24, 25(×2), 26, 29.
- [ ] **AppWindow** (+ PromptLine / ToolCall) (`_atoms.tsx`) — Claude Code chrome mock. Used: slides 10, 12, 14, 15, 19, 20, (and unused 31).
- [ ] **Callout** (`_atoms.tsx`) — security/risk/tip strip. Used: slides 07, 13, 14, 19, 22, 24, 26, 34.
- [ ] **BigStat** (`_atoms.tsx`) — headline figure tile. Used: slide 05.
- [ ] **DiagramFrame + FigureImage** (`_atoms.tsx`) — framed white-card wrapper for source PNGs. Used: slides 06, 07; FigureImage also slide 36.

Per-slide bespoke diagram components:
- [ ] **FlipCard** (`08-…/FlipCard.tsx`) — 3D-flip "new hire ↔ agent" onboarding card (×6). Slide 08.
- [ ] **"LLM" capsule** (inline, slide 08) — LLM pill + "day one is everything else".
- [ ] **Definition build-up** (inline, slide 09) — 5 numbered title fragments.
- [ ] **LoopDiagram** (`10-…/LoopDiagram.tsx`) — native SVG Think→Act→Observe circular cycle with phase highlight. Slide 10.
- [ ] **GoalBar / ToolStrip / Beat** (`10-…/parts.tsx`) — transcript atoms inside the agent-session AppWindow. Slide 10.
- [ ] **ProgressRail** (inline, slide 10) — 10-step dot+label rail (Think/Act/Observe ×3 + Answer).
- [ ] **"Until now vs Today" 2-card comparison** (inline, slide 04).
- [ ] **Annotated brief grid** (inline AppWindow, slide 12) — Context/Task/Guidelines/Constraints 3-track grid.
- [ ] **Three-ways-to-plug-in list + ToolTile bench** (inline, slide 13) — CLI/API/MCP + 5 connector tiles.
- [ ] **Memory two-level ladder + MEMORY.md index window** (inline, slide 14).
- [ ] **SKILL.md example window** (inline AppWindow, slide 15).
- [ ] **Nested "reach" boxes + file-tree** (inline, slide 16) — machine ⊃ other-folders ⊃ launch-folder.
- [ ] **Permission-request mock** (inline AppWindow, slide 19) — Allow once/always/Deny + mode line.
- [ ] **CLAUDE.md example window** (inline AppWindow, slide 20).
- [ ] **Context-window zones column** (inline, slide 21) — System/Tools/Conversation zone boxes + free-space.
- [ ] **"Model and brain" 2-card** (inline, slide 22).
- [ ] **"Promotion" 2-card comparison** (inline, slide 17).
- [ ] **Sovereign-path 3-card** (inline, slide 34).
- [ ] **Data-hygiene 4-rule cards** (inline, slide 35).
- [ ] **Five orchestration-pattern figure cards** (inline + FigureImage PNGs, slide 36).
- [ ] **LLM-judge majority-vote viz** (inline, slide 37) — 5 ✓/✗ chips → "✓ yes 3/5".
- [ ] **Meta-improvement 3-card** (inline, slide 38).
- [ ] **Instructor bio cards** (inline, slide 02) — borderline (cards, not a "figure").

Source-figure PNGs (NOT code-drawn — listed for completeness; do not re-create in SVG):
- METR time-horizon chart (06), Epoch inference-price chart (07), Claude Code app screenshot (11), Claude Code preview screenshot (Preview slide), 5 Anthropic orchestration schemas (36). Claude Code mascot SVG used as a BigStat icon (05).

Components defined but UNUSED in the live deck (do not need recreation): **LineChart**, **DiagNode**, **DiagEdge** (`_charts.tsx`); **StarterKit** slide / its AppWindow file-tree (`31-starter-kit`, not imported). **No MCP M×N / M+N connector diagram exists in the current deck** — the Tools slide replaced it with the connector-tile bench (§13).

---

### Tally

Distinct code-drawn diagram components catalogued (shared + bespoke, excluding pure photos and PNG source figures): **~34**
- 10 shared reusable diagram/UI components
- ~24 bespoke per-slide code-drawn figures/diagrams

Interactive elements: **8 CopyPromptButton instances** (7 distinct payloads: memory rule, NDA prompt, setup prompt, research prompt, deep-research.md file, build prompt, refine-from-preview.md file, deck prompt — note slide 25 has two buttons), **3 CountdownTimers** (10 min / 20 min+5 / 60 min+5).
Stepped slides: **08** (11), **10** (10), **14** (4), **36** (5); plus `26` declared `steps: 0`.

File written to: `/home/ezalos/42/Markdowns2Teach/docs/talks/capgemini-ai-agents/diagram-inventory-latest.md`
