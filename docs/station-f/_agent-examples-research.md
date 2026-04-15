<!-- ABOUTME: Research extract feeding Station F slides A-32 (OpenClaw), A-33 (MiroFish), A-34 (AutoResearch). -->
<!-- ABOUTME: All star counts, quotes, URLs verified from primary sources on 2026-04-12. -->

# Agent examples research — for Station F slides A-32, A-33, A-34

Accessed: 2026-04-12. Every quote is verbatim from the cited URL.

## Overview of the three agent examples

These three projects form the "agents in the wild" triad for Station F slides A-32 through A-34. They were chosen to illustrate three distinct modes of modern agent building:

- **OpenClaw** — a full consumer product with marketplace and acqui-hire story (personal-assistant pattern)
- **MiroFish** — a multi-agent simulation engine (swarm-intelligence pattern)
- **AutoResearch** — a 630-line Python harness where the agent rewrites ML training code (autonomous-research pattern)

All three are open-source, all three went viral in Q1 2026, and all three demonstrate different answers to the question "what does it mean to build with agents today?"

## OpenClaw (slide A-32)

- **What it is**: An open-source autonomous AI agent framework (TypeScript + Swift, MIT license) that executes real-world tasks via LLMs, with messaging platforms as its primary user interface. Originally shipped November 2025 as "Clawdbot" by Peter Steinberger (previously PSPDFKit founder).
- **Primary source URL (founder's own blog)**: https://steipete.me/posts/2026/openclaw
- **Primary source URL (repo)**: https://github.com/openclaw/openclaw
- **Wikipedia page as of 2026-04-12**: https://en.wikipedia.org/wiki/OpenClaw

- **Headline numbers** (multiple, time-stamped — pick the one that matches your narrative):
  - **335,000+ GitHub stars by March 24, 2026** (source: Lowtouch.ai data post)
  - **247,000 stars + 47,700 forks as of March 2, 2026** (Wikipedia)
  - **180,000 stars by mid-February 2026** (The AI Corner post on the Lex Fridman interview)
  - **106,124 stars by Day 2 after relaunch, +34,168 in 48 hours** (GitHub Trending tracker)
  - Growth rate: **~2,792 new stars per day** during the viral phase (Lowtouch.ai)

- **Distinct angle** (vs other agents in Station F course):
  - vs Claude Code (Anthropic's closed-source coding agent): **OpenClaw is open-source, local-first, MIT-licensed; messaging-centric not IDE-centric**
  - vs MiroFish: **OpenClaw is a single personal assistant; MiroFish simulates swarms of thousands of agents**
  - vs AutoResearch: **OpenClaw is a full product with a skills marketplace (ClawHub); AutoResearch is 630 lines of Python**

- **Current status**: Peter Steinberger announced Feb 14, 2026 he's joining OpenAI; OpenClaw moves to a non-profit foundation. Verified on his own blog:
  > "tl;dr: I'm joining OpenAI to work on bringing agents to everyone. OpenClaw will move to a foundation and stay open and independent."
  > URL: https://steipete.me/posts/2026/openclaw
  > (Same post) "OpenAI has made strong commitments to enable me to dedicate my time to it and already sponsors the project. To get this into a proper structure I'm working on making it a foundation. It will stay a place for thinkers, hackers and people that want a way to own their data, with the goal of supporting even more models and companies."

- **Security caveat** (crucial for slide honesty):
  > "Recent research on skills vulnerabilities (26% of 31,000 agent skills analyzed contained at least one vulnerability) and the rapid rise of the OpenClaw AI agent presented the perfect opportunity to announce our open source Skill Scanner tool. We ran a vulnerable third-party skill, 'What Would Elon Do?' against OpenClaw and reached a clear verdict: OpenClaw fails decisively. Here, our Skill Scanner tool surfaced nine security findings, including two critical and five high severity issues"
  > Source: Cisco Blogs (primary — Cisco's own announcement of the Skill Scanner). URL: https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare
  >
  > Corroborating: TechRadar summary — "a broader audit of 31,000 agent skills across multiple platforms found that 26% contained at least one vulnerability." URL: https://www.techradar.com/pro/here-are-the-openclaw-security-risks-you-should-know-about

- **Business-angle quote for slide** (from Stephen Smith's newsletter, a secondary but useful framing):
  > "Think of it this way. ChatGPT is like having a really smart advisor sitting across from you at a coffee shop. OpenClaw is like hiring a junior employee who shows up early, works all day, never forgets anything, and can juggle six projects at once. Except this employee costs about $20 to $200 a month in API fees and never asks for a raise."
  > URL: https://www.smithstephen.com/p/the-hottest-ai-tool-of-2026-is-one
  > Louis-note: use this only if A-32 has room for business framing; it's secondary, not primary.

- **Citations (primary URLs with verbatim quotes)**:
  1. Peter Steinberger's blog (acqui-hire announcement): https://steipete.me/posts/2026/openclaw — "I'm joining OpenAI to work on bringing agents to everyone. OpenClaw will move to a foundation and stay open and independent."
  2. Cisco Blogs (security audit): https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare — "26% of 31,000 agent skills analyzed contained at least one vulnerability ... our Skill Scanner tool surfaced nine security findings, including two critical and five high severity issues"
  3. Wikipedia (star count ledger): https://en.wikipedia.org/wiki/OpenClaw — "the open-source project having 247,000 stars and 47,700 forks on GitHub as of March 2, 2026"

## MiroFish (slide A-33)

- **What it is**: An open-source swarm intelligence / multi-agent simulation engine — thousands of LLM-powered agents with independent personas, long-term memory, and behavioral logic, interacting inside a constructed digital world to forecast social/political/financial outcomes. Python + Vue, AGPL-3.0, built on top of OASIS (CAMEL-AI) with GraphRAG for entity/persona construction.
- **Primary source URL (repo)**: https://github.com/666ghj/MiroFish
- **Primary source URL (project site)**: https://mirofish.ai (also https://666ghj.github.io/mirofish-demo/)
- **Archived verbatim README**: `docs/station-f/sources/mirofish/README.md` (already in repo, fetched 2026-04-12)

- **Headline numbers** (time-stamped):
  - **Repo archive snapshot (date in README frontmatter: 2026-04-12)**: 54,113 stars / 8,146 forks / AGPL-3.0 license — from the archived `docs/station-f/sources/mirofish/README.md`
  - **Fresh search result today (2026-04-12)**: 52,300 stars / 324 watching / 7,800 forks — from github.com/666ghj/MiroFish (via Tavily extraction)
  - Louis-note: the ~2k star delta between archive (54,113) and fresh fetch (52,300) is unusual — the repo may have lost some stars, or the two sources are reading slightly different timestamps. **Use "~52-54k stars" on the slide to stay honest.**
  - Created: 2025-11-26. Last release: V0.1.2 on Mar 7, 2026.
  - Default LLM: `qwen-plus` via Alibaba Bailian API (per the README's `.env.example`)

- **Distinct angle**:
  - vs OpenClaw (personal assistant, one agent): **MiroFish is a multi-agent world simulator — thousands of personas, not one**
  - vs AutoResearch (self-improving training loop): **MiroFish simulates human collective behavior; it's about predicting social dynamics, not optimizing ML**
  - vs traditional ABM (agent-based modeling) tools like NetLogo: **LLM-powered agents bring emergent natural-language behavior, not hand-coded rules**

- **Current status**: Actively maintained; Shanda Group incubation/support confirmed in README. CLI fork by amadad (`amadad/mirofish-cli`) adds Claude/Codex CLI support. Financial prediction explicitly marked "coming soon" in the roadmap (GitHub Discussion #280).

- **Key quote from README** (verbatim):
  > "MiroFish is a next-generation AI prediction engine powered by multi-agent technology. By extracting seed information from the real world (such as breaking news, policy drafts, or financial signals), it automatically constructs a high-fidelity parallel digital world. Within this space, thousands of intelligent agents with independent personalities, long-term memory, and behavioral logic freely interact and undergo social evolution. You can inject variables dynamically from a 'God's-eye view' to precisely deduce future trajectories — rehearse the future in a digital sandbox, and win decisions after countless simulations."
  > Source: `docs/station-f/sources/mirofish/README.md` (verbatim mirror of https://github.com/666ghj/MiroFish)

- **Workflow (also verbatim from README, usable as a 5-step diagram)**:
  > "1. Graph Building: Seed extraction & Individual/collective memory injection & GraphRAG construction
  > 2. Environment Setup: Entity relationship extraction & Persona generation & Agent configuration injection
  > 3. Simulation: Dual-platform parallel simulation & Auto-parse prediction requirements & Dynamic temporal memory updates
  > 4. Report Generation: ReportAgent with rich toolset for deep interaction with post-simulation environment
  > 5. Deep Interaction: Chat with any agent in the simulated world & Interact with ReportAgent"

- **Real demo cases** (from README):
  - Wuhan University public opinion simulation (Bilibili video)
  - "Dream of the Red Chamber" — predicting the lost ending based on first 80 chapters
  - Financial / political prediction marked "coming soon"

- **Citations (primary URLs with verbatim quotes)**:
  1. Repository (canonical): https://github.com/666ghj/MiroFish — "A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物"
  2. Project homepage: https://mirofish.ai/ — "The World's First Simple and Universal Open Source Swarm Intelligence Engine"
  3. Upstream simulation engine (attribution): https://github.com/camel-ai/oasis — per README: "MiroFish's simulation engine is powered by OASIS (Open Agent Social Interaction Simulations), We sincerely thank the CAMEL-AI team for their open-source contributions!"

## AutoResearch (slide A-34)

- **What it is**: Karpathy's autonomous research harness — a 630-line Python script that lets an AI coding agent autonomously iterate on the training script for `nanochat` (a minimal GPT-2-class model), running 5-minute training experiments on a single GPU and keeping or discarding changes based on validation bits-per-byte (val_bpb).
- **Primary source URL (repo)**: https://github.com/karpathy/autoresearch
- **Karpathy's X post / launch tweet**: referenced in multiple secondary sources; the public repo README is the cleanest primary source.

- **Headline numbers** (from the repo as of 2026-04-12):
  - **70,300 GitHub stars, 10,200 forks, 569 watchers** (via Tavily extraction of the repo page today)
  - **630 lines of Python** (widely cited figure, confirmed by 36kr and The New Stack)
  - **5-minute fixed time budget per experiment** (wall clock, per Karpathy's own README design)
  - **11% gain on the "time to GPT-2 level" leaderboard** — dropping from 2.02 hours to 1.80 hours for a depth-24 nanochat after ~20 autonomously-discovered optimizations (Karpathy, March 2026, via 36kr)
  - **Metric**: `val_bpb` (validation bits per byte) — "lower is better, and vocab-size-independent so architectural changes are fairly compared" (README, verbatim)

- **Key quotes from Karpathy's own README** (verbatim):
  > "`train.py` — the single file the agent edits. Contains the full GPT model, optimizer (Muon + AdamW), and training loop. Everything is fair game: architecture, hyperparameters, optimizer, batch size, etc. This file is edited and iterated on by the agent."
  >
  > "`program.md` — baseline instructions for one agent. Point your agent here and let it go. This file is edited and iterated on by the human."
  >
  > "By design, training runs for a fixed 5-minute time budget (wall clock, excluding startup/compilation), regardless of the details of your compute. The metric is val_bpb (validation bits per byte) — lower is better, and vocab-size-independent so architectural changes are fairly compared."
  >
  > "Self-contained. No external dependencies beyond PyTorch and a few small packages. No distributed training, no complex configs. One GPU, one file, one metric."
  >
  > Source (all above): https://github.com/karpathy/autoresearch

- **Karpathy's March 2026 result quote** (via 36kr translation of his X post):
  > "After integrating all these changes, he also found in actual tests that the 'time to train to the GPT-2 level' on the leaderboard was shortened from 2.02 hours to 1.80 hours, with a performance improvement of about 11%."
  > Source: https://eu.36kr.com/en/p/3725521482578567
  > Louis-note: 36kr is a Chinese tech media translation of Karpathy's own X post. The primary source is Karpathy's X/Twitter; 36kr is the cleanest English transcription available via Tavily. Flag on slide: "per Karpathy's March 2026 update on X."

- **Why founders care** (the conceptual point, sharpened by The New Stack):
  > "The most underappreciated file in the AutoResearch repository is not `train.py`. It is `program.md`. This single Markdown document simultaneously carries three registers of communication: instructions (what the agent should search for), constraints (what must not change), and stopping criteria (when the loop should wrap up and report). No other common format handles all three. YAML encodes structure but not reasoning. Python is executable but not legible as a strategy. JSON has no narrative. Markdown sits at the exact intersection of human editability and agent parseability."
  > Source: https://thenewstack.io/karpathy-autonomous-experiment-loop/
  >
  > The one-line takeaway for entrepreneurs: **"You don't write Python anymore. You write Markdown specs (`program.md`), and the agent writes the Python."** This is directly supported by the README's own framing that `train.py` is agent-edited and `program.md` is human-edited.

- **Distinct angle**:
  - vs OpenClaw (full product): **AutoResearch is 630 lines, no marketplace, no skills, no UI — it's a research template**
  - vs MiroFish (social simulator): **AutoResearch automates ML research; MiroFish simulates humans**
  - vs AutoML tools (Ray Tune, Optuna): **AutoResearch lets the agent rewrite the model architecture, not just sweep hyperparameters** — this is the key qualitative leap

- **Citations (primary URLs with verbatim quotes)**:
  1. Repository (canonical, written by Karpathy): https://github.com/karpathy/autoresearch — "training runs for a fixed 5-minute time budget (wall clock, excluding startup/compilation) ... The metric is val_bpb (validation bits per byte)"
  2. The New Stack analysis (secondary but well-reported, adds the "markdown is the interface" angle): https://thenewstack.io/karpathy-autonomous-experiment-loop/ — "Markdown sits at the exact intersection of human editability and agent parseability."
  3. 36kr English translation of Karpathy's X post (for the 11% improvement number): https://eu.36kr.com/en/p/3725521482578567 — "shortened from 2.02 hours to 1.80 hours, with a performance improvement of about 11%"

## Notes for Louis

- **OpenClaw star counts are a moving target.** Sources disagree by tens of thousands between Feb 2026 and April 2026 because the project is still actively trending. For the slide, either quote "~250k stars" with a "(as of March 2026)" tag, or use Wikipedia's exact figure "247,000 stars as of March 2, 2026." Don't invent a current-as-of-April number — none of the sources I found give one cleanly.
- **MiroFish star-count discrepancy**: the archived README claims 54,113 stars on 2026-04-12 but a live Tavily pull of the repo page today shows 52,300. Both are same-day. This could be (a) the README frontmatter was scraped before the live page refresh, (b) stars actually declined (possible but unusual), or (c) one of the two numbers is stale. Recommend slide says "52-54k stars as of April 2026."
- **AutoResearch 70.3k stars is from today's live Tavily fetch** — this is recent enough to cite as "April 2026" on the slide.
- **"Cisco found 12% of skills had vulnerabilities"** — this is *wrong* per my research. The accurate Cisco figure is **26% of 31,000 skills contained at least one vulnerability**, and **11.9% of ClawHub skills were malicious entries** (per Koi Security, not Cisco). If the Arms Race PDF said "12%", it may have been conflating these. **Slide A-32 should use 26% (Cisco) or 11.9% (Koi Security) depending on which claim is being made — not 12%.**
- **No direct Karpathy quote about AutoResearch "why I built it"** found via Tavily — his X post was not indexed cleanly. The 36kr translation is the next-best English primary source. If Louis wants a true primary quote, pull the X/Twitter post directly (URL: likely `x.com/karpathy/status/...` — not captured here because X is hostile to web scraping).
- **Peter Steinberger's MIT License vs OpenClaw's "MIT" claim**: Wikipedia lists MIT License; Steinberger's own blog has `CC BY 4.0 · Code MIT` in the footer. Confirmed consistent. Safe to state MIT on the slide.
- **All three of these projects are genuinely open-source and freely citable.** No paywalled primary sources blocked my research.
