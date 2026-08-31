<!-- ABOUTME: Full capture of Femke Plantinga's (Slite) "company brains" tweet (2026-08-27), Louis's label "Company brain". -->
<!-- ABOUTME: Source material for the Station F / Incubateur 42 talk (2026-09-02) on Claude Code & agentic best practices. -->

# Tweet — Femke Plantinga on 9+ "company brain" architectures ("Company brain")

## Header

- **URL**: https://x.com/femke_plantinga/status/2092918452423983363
- **Author**: Femke Plantinga (@femke_plantinga) — 13.9K followers; "growth @SliteHQ" (Barcelona). **Vendor-affiliated: this is Slite content marketing** for their ebook launch.
- **Date**: 2026-08-27 10:13:38 UTC
- **Engagement** (as of 2026-08-31): 1,731 likes · 3,929 bookmarks · 96 replies · 200 RTs · 21 quotes · 140,919 views
- **Fetch method**: fxtwitter API (note-tweet, full text); thread check via Tavily extract of the x.com page; ebook landing via Tavily extract
- **Thread**: NO — single long-form note tweet (complete with CTA + link inline). Replies are third-party; no self-thread continuation found.

## Full text (verbatim, single note tweet)

> Everyone's suddenly building company brains.
>
> Nobody agrees on what's inside one. 😵‍💫
>
> So we opened up 9+ company brains to see how they're actually built.
>
> Every single one does the same four things: getting signals, remembering, dreaming & pruning, speaking & searching.
>
> 𝟭. 𝗚𝗕𝗿𝗮𝗶𝗻
> Garry Tan's open-source personal brain. Your email and calendar flow into a git repo, and a nightly job re-links everything and flags what's gone stale.
>
> 𝟮. 𝗺𝗲𝗺𝟬
> A memory library you call from your own code. It only stores what you explicitly tell it to, and ranks fresh facts above idle ones at search time.
>
> 𝟯. 𝗟𝗲𝘁𝘁𝗮
> For building agents that remember across sessions. The agent decides what's worth keeping, and a second agent tidies up its memory in the background.
>
> 𝟰. 𝗭𝗲𝗽 / 𝗚𝗿𝗮𝗽𝗵𝗶𝘁𝗶
> A knowledge graph with a clock in it. When a fact changes, the old one gets an end date instead of being overwritten, so you can still ask what was true last March.
>
> 𝟱. 𝗦𝘆𝗹𝗽𝗵
> A content brain that lives entirely in a git repo. Agents write drafts, humans publish, and afterwards the agent reads your edits to learn what it got wrong.
>
> 𝟲. 𝗗𝗜𝗬 (𝗖𝗹𝗮𝘂𝗱𝗲 𝗖𝗼𝗱𝗲 + 𝗴𝗶𝘁)
> What most engineering teams actually do. Markdown in the repo, grep instead of search, and pull requests as the only thing keeping it honest.
>
> 𝟳. 𝗣𝗹𝗲𝘁𝗼𝗿
> A brand brain for marketing teams. Campaigns, assets and performance data in one tree, and the brand rules only move when a human signs off.
>
> 𝟴. 𝗚𝗼𝗿𝗴𝗶𝗮𝘀 𝗖𝗼𝗿𝘁𝗲𝘅
> Built in-house by an eight-person AI team. 12,000 markdown nodes in GitHub, and every night the questions it got wrong become PRs that fix it.
>
> 𝟵. 𝗦𝗹𝗶𝘁𝗲 𝗔𝗴𝗲𝗻𝘁
> For teams whose knowledge lives in docs and across sources. It watches ~20 connected tools (Slack, Drive, GitHub, Jira, etc.) for what's gone stale and sends the diff to whoever owns the page. Nothing changes without human approval.
>
> We just launched an interactive ebook with architecture notes from real 149 teams of builders and users, interview insights, and the complete research.
>
> The ebook is free, get it here: https://slite.com/ebooks/company-brain?utm_source=twitter&utm_medium=organic-social&utm_campaign=company-brain-ebook&utm_content=femke-honeypot&utm_id=fe08260k
>
> Which brain would you pick? 🧠

(The 𝟭/𝗚𝗕𝗿𝗮𝗶𝗻-style characters are Unicode mathematical-bold, verbatim from the tweet.)

## Media described

- `videos/tweet-2092918452423983363-femke-company-brains.jpg` (2254x2468 JPEG): a polished **"Company Brain" infographic** — headline "9+ must know brains → Every brain has the same 4 parts", with a 4-color legend (orange = getting signals, blue = remembering, pink = dreaming & pruning, yellow = speaking & searching). A 3x3 grid of cards, each with a tagline and a Mondrian-style block diagram whose colored areas show how much of that system each of the 4 parts occupies:
  - **GBrain** — "Thinks while you sleep": git as durable record; scheduled dream cycle maintains the graph, consolidates memory overnight.
  - **mem0** — "Memory as an SDK call": developer memory layer turning conversations into facts, retrieved on demand.
  - **Letta** — "The agent curates itself": agent decides what belongs in memory; a sleep-time agent works on shared context in background.
  - **Zep / Graphiti** — "Facts expire, they don't disappear": temporal graph; old facts marked expired, not deleted.
  - **Sylph** — "Zero automation, on purpose": brain in a git repo you shape yourself; agents draft, people decide what lands.
  - **DIY (Claude Code + git)** — "Markdown, grep, pull requests": brain of Markdown, PRs, plain-file search; stays flexible because an engineer keeps it healthy.
  - **Pletor** — "Multimodal at the core": brand rules, creative refs, performance data as shared memory for creative agents.
  - **Gorgias Cortex** — "Fixes itself by pull request": built from systems teams already use; company knowledge as a graph agents navigate.
  - **Slite Agent** — "Docs with an owner and an expiry": keeps docs people already use, adds review, expiry, maintenance, cited answers.

## Linked content summaries

- **Slite ebook** (https://slite.com/ebooks/company-brain — "The Ontology of the Company Brain", fetched landing page): claims "Company Brain, as a category, is less than 6 months old"; based on a **survey of 149 teams + interviews with 10+ company-brain builders**. Promised contents: what a Company Brain is supposed to do; the four technical components of every brain; build vs buy; "what every builder agrees on, and what none of them can answer". Interactive ebook — full body content is JS-gated; only the landing copy was retrievable non-interactively.
- Named systems all real and independently checkable: GBrain (Garry Tan's open-source personal brain, github.com/garrytan — mid-2026), mem0 (mem0.ai, OSS memory layer), Letta (letta.com, ex-MemGPT), Zep/Graphiti (getzep.com, temporal knowledge graph), Gorgias Cortex (in-house at Gorgias, ecommerce CX company), Slite Agent (the vendor's own product). Sylph and Pletor are smaller/newer. Not fetched individually in this pass.

## Relevance to the talk

- **Memory (core)**: the best available taxonomy of the "company brain / agent memory" design space right now, with a shared 4-function decomposition: **getting signals → remembering → dreaming & pruning (consolidation/forgetting) → speaking & searching (retrieval)**. Maps cleanly onto Claude Code's own memory story (CLAUDE.md, auto-memory, project memory files).
- **Claude Code best practices**: pattern #6, **DIY = Claude Code + git — "what most engineering teams actually do"**: markdown in the repo, grep instead of embeddings, PRs as the honesty mechanism. Third-party confirmation that Louis's own setup (GroundControl/memory-files/lessons.md) is the mainstream engineering answer — great "you already have a company brain" moment for founders.
- **Context engineering**: temporal validity (Zep's facts-with-end-dates), staleness detection, nightly consolidation ("dreaming"), eval-driven repair (Gorgias: wrong answers become PRs overnight) — all concrete mechanisms worth naming.
- **Economic opportunity for founders**: a category "less than 6 months old" with 9+ competing architectures and no agreed definition = open territory. Both an opportunity (build picks-and-shovels or a vertical brain) and a buyer's guide (the 4-part framework tells you what to demand of any vendor). Gorgias data point: 8-person AI team, 12,000 markdown nodes, self-repairing via nightly PRs — an in-house build at a real company.

## Freshness & sourcing gaps

- Fresh: 2026-08-27, five days before the talk.
- **Vendor bias**: this is Slite growth marketing; the "every brain has the same 4 parts" ontology and the "<6 months old" category claim are Slite's framing, and Slite Agent conveniently caps the list. The 149-team survey is proprietary and unaudited. On a slide, attribute the framework to "Slite's Company Brain research (2026)" with the ebook link — do not present it as neutral market research.
- Per-system claims (e.g., Gorgias "12,000 markdown nodes", "questions it got wrong become PRs") are as-told-to-Slite; for slide use, deep-research should chase **primary sources per system**: GBrain GitHub repo/README, mem0 + Letta + Zep/Graphiti docs, a Gorgias engineering blog post or talk on Cortex (if public), Garry Tan's own posts on GBrain. The DIY/Claude-Code pattern can be backed by Anthropic's own memory & CLAUDE.md docs and Claude Code best-practices engineering posts.
- The interactive ebook itself was not fully extracted (JS-gated); if a slide leans on the survey numbers, someone needs to actually open the ebook and pull the exact stats + methodology page.
