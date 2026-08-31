<!-- ABOUTME: Deep-research brief — state of agent benchmarks as of Sept 2026, for the talk's state-of-play refresh. -->
<!-- ABOUTME: High leverage: feeds 3-4 slides (METR, price-accuracy frontier, ARC-AGI-3, "update ai agent new benchmarks" intro item). -->

# Research brief — Agent benchmarks, September 2026

## Question
Where do autonomous agents actually stand, on the freshest defensible numbers, as of the first week of September 2026 — and which single chart best shows the capability × price × effort frontier across models?

## Why it matters for the talk
Louis's intro item "update ai agent new benchmarks" has NO source yet. The audience saw the April state-of-the-field deck; repeating April numbers would be a failure. This brief feeds: the METR slide, the price-accuracy frontier slide (the graph Louis wants early), and the ARC-AGI-3 datapoint.

## What we already have (and its staleness)
- `sources/tweet-2078290206424437095-kimi-k3-vs-fable5-deepswe.md` — DeepSWE: Kimi K3 ≈ Fable 5 at ~35% price (Jul 18, superseded); deepswe.datacurve.ai leaderboard is LIVE (Aug 20: Opus 5 at 74%) — 25 models × effort configs × pass@1 × $/task. The real "price/effort/accuracy graph" is a scatter to REBUILD from this leaderboard via `scripts/charts/deck_chart.py`.
- `sources/tweet-2077770348876247502-schema-arc-agi-3.md` — [schema] harness 98.98% RHAE on ARC-AGI-3 Public — SELF-REPORTED, not ARC-Prize-verified. Verified frontier was 0.51% → 7.78% (semi-private).
- Heuritech deck: METR "doubles every ~7 months" — but METR's own newer data shows ~4.3-month doubling; the deck PNG is from Time Horizon 1.1 (Jan 2026). STALE.

## What to find
1. **METR**: latest time-horizon release + current doubling estimate; the newest official figure/PNG; what Opus 5 / Fable 5 score (50% task length in hours).
2. **DeepSWE leaderboard**: snapshot the full table (all models, effort configs, price, pass@1) close to Sept 1; establish who runs it (Datacurve) and methodology credibility; export the data for our own scatter.
3. **ARC-AGI-3**: ARC-Prize-VERIFIED leaderboard as of Sept 1 (not self-reports); what the verified frontier is now; one-line state of the "harness beats raw model" story.
4. **What replaced SWE-bench** as the field's reference for production coding (FrontierCode Diamond? SWE-bench Pro? status of saturation), one number per benchmark for the best current model.
5. **Real-work benchmarks** (GDPval-style, task-completion-in-occupations): any 2026 update worth one founder-legible number.

## Acceptance
Every number carries a clickable exact primary URL (metr.org blog post, arcprize.org leaderboard, deepswe.datacurve.ai, epoch.ai) + a verbatim quote for sources.yml. Flag every vendor self-report as such.

## Method
/research pipeline or one deep-research run; the DeepSWE snapshot is a curl + JSON parse, do it deterministically. Re-check the live leaderboards again on Sept 1 (they move weekly).
