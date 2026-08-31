<!-- ABOUTME: Deep-research brief — how long until frontier-cloud capability runs locally; replace a weak community chart with citable data. -->
<!-- ABOUTME: The r/LocalLLaMA chart ("Fable local in ~2 years") has no recoverable permalink and n=4 datapoints. -->

# Research brief — Frontier → local: the real lag

## Question
How long does it take for frontier-cloud capability to become runnable on consumer/prosumer hardware, on defensible data — and what does that imply for founders' build-vs-wait and sovereignty decisions in 2026?

## Why it matters for the talk
"Fable may run locally in 2 years" is a memorable commoditization beat that extends the cost-collapse slide — but the current source is an unattributed r/LocalLLaMA chart (n=4 generations, false precision, permalink not recoverable). Under the clickable-source rule it CANNOT ship as-is. Epoch AI has real analyses of exactly this.

## What we already have
- `sources/tweet-2074078414705955006-fable-local-in-two-years.md` — Chubby's tweet + full chart description (~24.8-month average lag, Fable-class on laptops ~Jul 2028); file already flags Epoch AI as the citable replacement and notes a conflicting ~9-month open-vs-closed benchmark-parity figure.

## What to find
1. **Epoch AI primaries**: their open-vs-closed capability-lag analysis (the ~1-year-ish benchmark-parity figure — exact number, exact page) and any compute/efficiency-trend piece that bounds "same capability, N× less compute per year".
2. **Distinguish the TWO lags** (the community chart conflates them): (a) open-weights model matching frontier scores (regardless of size), vs (b) that capability fitting in ≤~128GB consumer hardware. Numbers for each.
3. **Concrete 2026 datapoints**: best open-weights model runnable on a 128GB Mac/DGX-Spark-class box today and what frontier-era capability it matches (e.g. Qwen/DeepSeek/Mistral releases vs GPT-4/Claude-3.5-era scores) — 2-3 verifiable pairs.
4. **The quantization tax**: current honest numbers on quality loss at 4-bit for coding/agentic tasks (the April deck had a quantization slide — refresh if reused).
5. **Sovereignty tie-in**: latest EU sovereign-inference options for open-weight frontier-class models (Mistral La Plateforme, Scaleway; anything new since June).

## Acceptance
Either a rebuilt lag chart from citable data (deck_chart.py, only measured points, projections dashed) or an honest "two lags" slide with 3 verified pairs — every number with an exact primary URL + verbatim quote. The Reddit chart ships only if its permalink is recovered AND it's framed as community estimate.

## Method
One deep-research run centered on epoch.ai; the 2-3 hardware datapoints can be verified against model cards + benchmark tables directly.
