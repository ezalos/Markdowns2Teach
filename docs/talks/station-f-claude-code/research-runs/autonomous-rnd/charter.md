# What can autonomous agent loops actually do in R&D in 2026, and where is the measured ceiling?

## Decision this feeds

**S38 "R&D automation in the wild"** and part of **S11** in the 2026-09-02 Station F
founders' talk. The speaker promised the organiser a talk covering strategies for
automating R&D, so this slide must be evidence-led rather than anecdote-led. Two primaries
are already collected: Prime Intellect's study (153 runs, 18 frontier models on the nanoGPT
speedrun; the best model closed 82% of the gap to the human record; no run produced a
fundamentally new method) and Karpathy's autoresearch loop. The decision: **which examples
go on the slide, and how the ceiling is stated honestly** — the negative result is the part
that earns credibility with technical founders.

## Must answer

- **The current state of agents doing machine-learning research**: beyond Prime Intellect's nanoGPT study, what measured evaluations exist of agents performing research tasks (METR's RE-bench or its 2026 successor, MLE-bench, any lab-run internal evaluation published with numbers)? Give agent-versus-human-expert results with dates.
- **Verified discoveries versus optimisation**: which results claimed for autonomous agent loops in 2025-2026 have been independently reproduced or peer-reviewed, and which remain vendor or self-reported? Cover DeepMind's evolution-loop work (AlphaEvolve and any successor), Sakana's AI Scientist line and its critiques, and any materials or mathematics result. The organising distinction: optimising a known pipeline versus finding something genuinely new.
- **Karpathy's autoresearch, stated precisely**: what the repo actually does, what the measured improvement was and on what task, and separately what the PostHog application of the same loop found. These are two different stories that get merged in circulation — keep them apart, with a source each.
- **Industrial loops with published write-ups**: teams running continuous agent loops against their own codebase or product, with outcomes reported (what it fixed, how much it cost, what it broke). Prefer engineering blogs with numbers over vendor case studies.
- **Why loops plateau**: the strongest published analysis of the ceiling — evaluation as the bottleneck, novelty versus optimisation, error compounding over long horizons, reward hacking in self-evaluated loops. One citable source per mechanism.
- **What a five-person startup can copy next week**: the smallest credible version of an R&D loop, grounded in a documented example rather than invented. What it needs (a goal, a harness, an evaluation, a schedule) and what it costs to run.
- **The reward-hacking evidence**: documented cases where an agent loop optimised the metric and not the goal. This is the failure founders will actually hit and it belongs in the caveat line.

## Source bar

tier: Primary artefacts first — research-lab blogs and papers with methodology (Prime Intellect, DeepMind, METR, Anthropic, OpenAI), arXiv papers with real evaluation, public repositories by the person who built them, and engineering blogs describing systems the author operates. Independent reproduction outranks the original claim. Vendor case studies are usable only when labelled and only for existence claims, never for magnitude.

recency: Focus on 2026, with 2025 foundations allowed where they remain the reference and are dated as such. Any leaderboard that is still moving must be named with its URL and snapshot date.

## Deliverable

A Markdown report with: a two-by-two table (optimisation versus novel discovery, on one axis; independently verified versus self-reported, on the other) with one or two examples per cell, each carrying an exact clickable URL and a verbatim quote. Then a "ceiling" section stating plainly what agent loops still cannot do, with sources. Then a "smallest loop that works" section a founder could copy, grounded in a cited example.

## Out of scope

- Prompt-level tips and framework tutorials.
- Speculation about future capability beyond what a dated published result supports.
- Agent safety and alignment research as a topic in itself, except where reward hacking is the observed failure of a research loop.
