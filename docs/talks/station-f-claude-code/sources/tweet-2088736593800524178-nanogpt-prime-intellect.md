# Tweet 2088736593800524178 — "NanoGPT research from Prime Intellect" (elie / @eliebakouch)

## Header

- **URL**: https://x.com/eliebakouch/status/2088736593800524178
- **Author**: elie (@eliebakouch) — "training llm @PrimeIntellect (prev: @huggingface)". Verified individual, ~23.8k followers.
- **Date**: Sat Aug 15, 2026, 21:16:25 UTC
- **Engagement** (as of 2026-08-31): 825 likes · 76 RTs · 51 replies · 11 quotes · 457 bookmarks · ~103.0k views
- **Type**: Single long-form note tweet (NOT a thread — no reply chain from the author found), quote-tweeting the official @PrimeIntellect announcement.
- **Fetch method**: fxtwitter API (full JSON saved). Quoted tweet + its 6-tweet thread also captured (fxtwitter + threadreaderapp).

## Full text (verbatim)

> to my knowledge this is the largest open experiment on autonomous agents iterating on a research environment
> 
> we scaled runtime, compute, diversity of models and harnesses. as a comparison, similar tasks on oai/anthropic system cards are anthropic "optimizing an llm training on CPU" and openai gpt 5.6 doing nanogpt track 1 but for less than a day. we also share a lot of the details (traces, scratchpads, ect..) so you can look into how models approach such tasks
> 
> this experiment is quite noisy, one run in the same setting has a ~50 step spread after 24h. i find it super impressive that while models explore relatively the same ideas and the task and environment have a lot of variance, there is still a big gap between different models
> 
> fable 5 closed 82% of the gap to the current human record with kimi K3 being very impressive as well. i'm currently running grok 4.6, deepseek v4 pro, muse spark 1.2, qwen 3.8 max and glm 5.3, expect results next week
> 
> one of my favorite parts is some of the tools that models developed during this experiment, especially with prime agent. for instance kimi K3 created its own experiment API for generating optimizer variants, loss comparisons, Newton Schulz tuning etc.. we also have an early deepseek v4 pro <> prime agent run that did a PSGD experimentation outside the normal nanogpt loop to build intuition before starting gpu runs. other cool examples in the blog with other harnesses as well!
> 
> i'm also very excited about the ideas we have in mind on this subject, we will keep working on understanding the research capabilities of (closed and open) frontier models

### Quoted tweet (verbatim) — @PrimeIntellect, 2088733966904000778

- **URL**: https://x.com/PrimeIntellect/status/2088733966904000778
- **Date**: Sat Aug 15, 2026, 21:05:59 UTC
- **Engagement**: 1,881 likes · 213 RTs · 74 replies · 105 quotes · 1,159 bookmarks · ~584.4k views

> We ran the largest open experiment on how frontier models do AI research.
> 
> 100+ autonomous runs across 10+ models, sandboxed on 8xH200s for up to 8 days, iterating on the nanoGPT optimizer track.
> 
> Best runs closed 82% of the gap to a record built by dozens of humans over months.

### The @PrimeIntellect announcement thread (full, via threadreaderapp — tweets 2–6 paraphrase-verified summary; tweet 1 verbatim above)

1. (verbatim above — "We ran the largest open experiment…")
2. "The task: iterate on a 124M GPT training recipe from a shared baseline, only changing optimizer related hyperparameters, no internet access. We tested Fable 5, Opus 5, GPT-5.6 Sol, Kimi K3, Grok 4.5, GLM 5.2, Muse Spark 1.1, DeepSeek V4 Pro, Grok 4.6, Muse Spark 1.2, Qwen 3.8 Max."
3. "What separated the strongest models: which experiments to run, how to navigate the benchmark's inherent noise, and which old negatives to revisit as the recipe changed. Some even built small simulations to isolate a mechanism before deciding if another GPU run was worth it."
4. (describes the Prime Agent harness with persistent IPython kernel enabling models like Kimi K3 to build research tools and revise hypotheses iteratively)
5. (discusses multi-agent harnesses as a research direction to reduce costs)
6. "We release everything: full traces, scratchpads, reasoning streams from open-weight models, and our experiment setup." Links: primeintellect.ai/research/nanogpt-speedrun · primeintellect.ai/blog/measuring-autonomous-research

Note: Louis got the full head tweet + quote verbatim; PI thread tweets 2, 3 and 6 are verbatim per threadreaderapp, tweets 4–5 only as summaries (threadreaderapp's extractor summarized them). For slide use, quote tweets 1–3 or the blog itself.

## Media described

Two images downloaded to `sources/videos/`:

1. **`tweet-2088736593800524178-elie-photo.jpg`** (3196x4096, attached to elie's tweet) — light-mode screenshot of the "NanoGPT Speedrun Frontier" leaderboard page. Header: "Baseline 3,290 steps · human record 2,600". Chart "Share of the human record gap closed" (y: 0–100%, "human record 100%") vs "Agent time (log scale)" (x: 3h → 9d). Step-line per model, best-so-far record over time: **Fable 5 tops out ≈82% at ~8–9 days** (clear outlier, own orange line well above the pack); Opus 5 ≈53%; Kimi K3 · prime-agent ≈52%; Kimi K3 ≈46%; Opus 4.8 ≈39%; GPT-5.6 Sol ≈35% (out to ~6d); GPT-5.6 Sol Pro ≈34%; Sonnet 5 ≈26%; Grok 4.5 ≈24%; Qwen3.8 Max ≈23%; GLM 5.2 ≈20%; DeepSeek V4 Pro ≈13%; Grok 4.6 ≈11%; Muse Spark 1.1 ≈8%; Kimi K2.7 / GPT-5.5 / Muse Spark 1.2 / GPT-5.6 Terra at the bottom. Below the chart: tabbed examples ("PSGD rule lab", "Noisy quadratic", "Polynomial search", "Shape simulator", "Controlled spectra") — shown: "Screening PSGD recursions in a synthetic covariance lab" (Prime Agent · IPython laboratory · DeepSeek V4 Pro 0813), with actual torch code screening 4 candidate PSGD update rules on 20,000 CPU samples, plus a CONSTRUCT → OBSERVE → REVISE → REVISE AGAIN research-loop panel — i.e. the model built itself a cheap CPU lab before spending GPU money.
2. **`tweet-2088733966904000778-primeintellect-photo.jpg`** (2048x1404, attached to the PI quote tweet) — dark-mode version of the same frontier chart, subtitle: "We ran 153 autonomous runs across 18 frontier models on the nanoGPT optimizer speedrun." with a "Read Blog" button. Note: the tweet text says "100+ runs across 10+ models"; the chart says the precise numbers, **153 runs / 18 models**.

## Linked content summaries

### Prime Intellect blog: "Measuring Autonomous AI Research" — https://www.primeintellect.ai/blog/measuring-autonomous-research (live, 200)

- **Setup**: nanoGPT optimizer speedrun — train a 124M-param GPT to validation loss 3.28; score = training steps needed. Baseline 3,290 steps; human record 2,600 (set by dozens of humans over months). 153 autonomous runs, 18 frontier models, sandboxed 8xH200 per run, up to 8 days, multiple seeds per model, **no internet access** (arXiv included — deliberately; they note restricting internet "made models slightly more creative"). Models get the training script, hyperparams and a rulebook (`program.md`) with statistical passing criteria (mean val loss < 3.27859 over eight fixed seeds). Framed as the first large-scale public eval of this kind — prior comparables are Anthropic's system-card task (optimizing an LLM training on CPU) and OpenAI GPT-5.6 on nanoGPT track 1 for <1 day.
- **Results**: Fable 5 best validated 2,726 steps (**81.7% of the human-record gap closed**); Opus 5 2,920 (53.6%); Kimi K3 (prime-agent) 2,930 (52.2%). Bottom models closed 7–12%. All wins were optimizer work: better preconditioning, caps/floors on weight and update magnitudes, LR schedules staying hot longer, weight averaging near end of training.
- **Research behaviors observed**: leading models built reusable tooling inside persistent IPython environments (Kimi K3 wrote its own experiment API — variant construction, loss-curve comparison, baseline restoration; Opus 5 factored recipes into replaceable blocks; GPT-5.6 Sol spawned read-only advisor agents). Stronger models modeled the noise: 3-seed screens before expensive 8-seed validation, shared-seed comparisons exploiting GPU nondeterminism. Top performers re-tested old negative results after the recipe changed ("one late re-probe was worth thirty-one steps"). Several built CPU synthetic labs before touching GPUs ("research taste").
- **Key limitation (their words)**: "None of the runs produced a fundamentally new method; the winning ingredients are all similar to existing ones in the literature." Autonomous execution of the research loop: yes. Algorithmic novelty beyond humans: not yet.
- **Caveats**: high variance (~50-step spread across identical runs after 24h per elie); best-of-seeds selection at 24h sacrifices replication; minor launcher-logic changes mid-run; independent LLM auditor found no cheating/sandbox escapes.
- **Artifacts**: full traces, scratchpads, open-weights reasoning streams, monitor reports, per-run ledger + harness released.

### Interactive leaderboard — https://www.primeintellect.ai/research/nanogpt-speedrun (live, 200)

Record-over-time and record-over-tokens charts, per-model stats, clickable per-run traces.

### Code — https://github.com/PrimeIntellect-ai/experiments-autonomous-speedrunning (verified via GitHub API: "autonomous nanogpt optimizer speedrun", 110 stars)

## Relevance to the talk

- Directly on-theme for "state of AI" to founders using agents: the strongest concrete public datapoint (Aug 2026) on **how far autonomous agents get at multi-day, open-ended R&D** — Fable 5 closes 82% of a months-of-human-effort gap in ~8 days of unattended agent time, but produces zero fundamentally new methods.
- Great "agentic best practices" mirror: what separates top agents = experiment selection, noise handling, revisiting old negatives, building their own tools/simulations first — exactly the harness/scaffolding lessons that transfer to Claude Code usage (persistent state, cheap probes before expensive runs, self-built tooling).
- The gap between models on the SAME task/harness is a clean argument that model choice still dominates.

## Freshness & sourcing gaps

- **Fresh**: published 2026-08-15, two weeks before the talk. Elie says grok 4.6, deepseek v4 pro, muse spark 1.2, qwen 3.8 max, glm 5.3 results were still running ("expect results next week") — **check the leaderboard page for updated numbers before the talk**; the 82%/rankings may have moved.
- **Primary source for slides**: the blog + leaderboard page are citable, live, exact links (verify with `check-citation-links.py`). The tweet is just the pointer — cite primeintellect.ai, not x.com, for the numbers.
- **Discrepancy to resolve on any slide**: tweet says "100+ runs / 10+ models"; the chart and blog say **153 runs / 18 models** — use the blog figure.
- **Human record moving target**: "human record 2,600 steps" is the modded-nanoGPT speedrun community record *at experiment time* (Keller Jordan's leaderboard, github.com/KellerJordan/modded-nanogpt) — deep-research needed: confirm current human record hasn't dropped below 2,600 before quoting "82%".
- Not peer-reviewed; single-org experiment with self-admitted variance and best-of-seeds selection — frame as "Prime Intellect reports", not established benchmark truth.
