<!-- ABOUTME: Deep-research brief — the evidence base for "automating R&D with agents", the topic Louis promised Chloé by email. -->
<!-- ABOUTME: Prime Intellect + Karpathy are collected; this brief widens to the full 2026 evidence base with honest ceilings. -->

# Research brief — Automating R&D: what the evidence actually supports

> **Charter written** at `../research-runs/autonomous-rnd/charter.md` — queued behind the
> two-run cap. The charter is the launch document; this brief keeps the background.

## Question
What can autonomous agent loops genuinely do in R&D as of September 2026 — optimization, bug-finding, experiment-running, literature work — and where is the measured ceiling?

## Why it matters for the talk
Louis's email to Chloé names "stratégies d'automatisation de la R&D" as a pillar of the talk. We have two strong primaries (Prime Intellect's 153-run study; Karpathy's autoresearch) but the claim "agents automate R&D" deserves the full 2026 evidence base — including the negative result (no fundamentally new methods), which is exactly the honest-broker framing that lands with technical founders.

## What we already have
- `sources/tweet-2088736593800524178-nanogpt-prime-intellect.md` — Prime Intellect "Measuring Autonomous AI Research": 153 runs / 18 models on nanoGPT speedrun, 8×H200 up to 8 days; Fable 5 closed 82% of gap to human record; NO run produced a fundamentally new method. Blog + leaderboard + repo verified. (Leaderboard updates pending — re-check before talk.)
- Heuritech §22: Karpathy autoresearch (+11% nanochat, the 3-year-old PostHog query-engine bug — two stories, keep attributed separately).
- Loops section (PostHog + Anthropic workshop) as the mechanism.

## What to find
1. **METR RE-bench** (or 2026 successor): agents vs human researchers on ML-research tasks — the current honest comparison number.
2. **AlphaEvolve / DeepMind evolution-loop results** (matrix-multiplication, data-center scheduling): what's verified, what's PR; any 2026 follow-up.
3. **Agent-discovered results that held up**: peer-reviewed or independently reproduced discoveries by agent loops in 2026 (materials, math, systems perf). Separate "optimized a known pipeline" from "found something new" — the Prime Intellect distinction, generalized.
4. **Sakana AI Scientist v2/successors + critiques**: where fully-automated paper-writing actually stands (including the acceptance-then-withdrawal saga status).
5. **The practitioner tier**: documented industrial autoresearch loops (PostHog's, any others with write-ups) — what a startup-sized team can copy next week.
6. **Failure/ceiling analyses**: published work on why loops plateau (evaluation bottleneck, novelty vs optimization) — feeds the "evaluation is the moat" argument.

## Acceptance
A 2×2 the talk can teach: {optimization vs novel discovery} × {verified vs vendor-claimed}, each cell with 1-2 examples carrying exact primary URLs + verbatim quotes. The negative results stated as plainly as the positive.

## Method
One deep-research run; primaries: metr.org, deepmind.google/blog, primeintellect.ai, arxiv, karpathy's repos, posthog engineering blog.
