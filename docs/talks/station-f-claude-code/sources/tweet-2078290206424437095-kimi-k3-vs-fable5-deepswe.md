# Tweet 2078290206424437095 — "Price/effort/accuracy graph of the different models" (Kimi K3 vs Fable 5 on DeepSWE)

## Header

- **URL**: https://x.com/togethercompute/status/2078290206424437095
- **Author**: Together AI (@togethercompute) — 62.3K followers, verified org
- **Date**: 2026-07-18 01:26 UTC
- **Engagement**: 3,771 likes · 337 RT · 89 quotes · 93 replies · 878 bookmarks · 769.6K views
- **Quotes**: quote-tweet of the @zainhas deep-dive thread (below)
- **Fetch method**: fxtwitter API (head + quoted tweet) + tavily_extract on x.com (full quoted thread) + Together AI blog (WebFetch + HTML scrape for chart URLs)
- **Thread status**: The Together tweet itself is a single QT; the "thread" it points to is the @zainhas thread — FULL THREAD captured (head + 6 replies, verified gap-free via `replying_to_status` chaining)

## Full text (verbatim)

**Head (Together AI):**
"We analyzed Kimi K3 vs. Claude Fable 5 for software engineering tasks using DeepSWE.

Kimi K3 gets you the same performance as Fable 5 at ~35% of the price, and it actually pulls ahead at higher pass@k's. More insights in the thread!"

**Quoted thread — Zain (@zainhas, AI/ML @togethercompute), 2026-07-18 01:22 UTC, 434 likes / 399.6K views on head:**

1. "Deepdive: Kimi K3 vs. Fable 5 on software engineering/DeepSWE tasks.

   The open frontier isn't 6 months behind anymore!

   full deep-dive 👇(1/n)🧵" *(image: "Kimi K3 (Open source) VS Fable 5 (Closed)" logo card)*

2. "> pass@2: Kimi 82.0 vs Fable 80.2.

   > pass@4: Kimi 89.4 vs Fable 88.5 - above every flagship on the benchmark, incl. GPT-5.6 Sol (85.8).

   best-of-k K3 is the open/closed SOTA!" *(image: pass@k bar chart)*

3. "$4.65/rollout vs $13.41. Per $100 of spend, Kimi solves 14.7 tasks to Fable's 5.3 = 2.8x the work per dollar. A median Kimi rollout takes 66 minutes (Fable: 21). This should improve after the model is released and widely available!" *(image: economics triptych)*

4. "breakdown by programming language! Kimi takes Go, 79 vs 71. Fable holds Python (74-68), JS (70-65), TS (64-60), and Rust (75-65)." *(image: per-language bars)*

5. "Kimi K3 has the highest peak of any model: 89.4% > only 12 tasks it never cracks. Kimi K3 -> 76.6% reliability = 45 tasks solved 4/4 Fable is more reliable -> 79.0% reliability = 58 tasks solved 4/4" *(image: coverage-vs-reliability scatter)*

6. "Per-task correlation between Kimi K3 and Fable: 0.72 - the highest cross-vendor similarity. Zero tasks where one goes 4/4 and the other 0/4. In either direction. signs the benchmark might be saturating!" *(image: agreement scatter)*

7. "what types of mistakes do they make? very similar! > Both lose by near miss 65% of the time. > Both protect the existing test suite (11% vs 10% baseline regressions) earlier opensource models used to break the baseline but this one doesnt!" *(image: failure-anatomy stacked bars)*

## Media described (all saved under `videos/`)

- `tweet-2078289171807150312-kimi-vs-fable-head.jpg` — logo card: "Kimi K3 (Open source) vs Fable 5 (Closed)".
- `zainhas-thread-HNeQ_fJa0AAQK_w.png` — **pass@k bars**: y = % tasks solved; pass@1 (official): Kimi K3 max 68.5 vs Fable 5 xhigh 69.9; pass@2: 82.0 vs 80.2; pass@4: 89.4 vs 88.5.
- `zainhas-thread-HNeQ_wWbEAAKwHL.png` — **economics triptych** "Kimi K3 delivers ~3x the solved work per dollar (but takes 3x the wall-clock)": $/rollout $4.65 vs $13.41; solved rollouts per $100: 14.7 vs 5.3; median minutes/rollout: 66m vs 21m.
- `zainhas-thread-HNeRACPaMAARIxj.png` — **per-language pass rates**: Python 68/74, Go 79/71, TypeScript 60/64, JavaScript 65/70, Rust 65/75 (Kimi/Fable).
- `zainhas-thread-HNeRASwbYAAOpUx.jpg` — **coverage vs reliability scatter**: x = % tasks solved at least once (reach), y = pass rate on reachable tasks; Fable 5 xhigh higher-reliability (~79%, ~88.5 coverage), Kimi K3 max wider-reach (~89.4 coverage, ~76.6 reliability); iso-pass@1 diagonals at 60%/70%.
- `zainhas-thread-HNeRAjRasAAecIz.png` — **per-task agreement scatter** (trials passed of 4, Kimi x vs Fable y): both-96 / Kimi-only-5 / Fable-only-4 / neither-8; corr 0.72; zero opposite-corner tasks.
- `zainhas-thread-HNeRA1LakAAMui-.jpg` — **failure anatomy stacked bars**: near miss 65%/65%, partial 11%/13%, big miss 13%/12%, broke baseline 11%/10% (Kimi/Fable).
- `together-blog-01-scoreboard.png` — Together-branded version of the pass@k chart from the blog post.

### ⚠️ About the graph Louis remembers ("price/effort/accuracy of the different models")

None of the tweet's own charts plots many models at once — they are all Kimi-vs-Fable pairs (each model at its max effort: "Kimi K3 max" vs "Fable 5 xhigh"). The **multi-model price/effort/accuracy view is the DeepSWE leaderboard itself** (https://deepswe.datacurve.ai — live, updated 2026-08-20): 25 models, each row = model[effort] with Pass@1 ± CI, avg cost/task, output tokens, steps. Current top of board: claude-opus-5[max] 74%±4 @ $11.84 · gpt-5.6-sol[max] 73%±3 @ $8.39 · **claude-fable-5[max] 70%±4 @ $21.63** · glm-5.3[max] 69%±3 @ $3.99 · **kimi-k3[max] 69%±5 @ $4.65** · gpt-5.6-luna[max] 67%±4 @ $0.61 · deepseek-v4-pro[max] 63%±6 @ $0.24. Efforts ([medium]/[high]/[xhigh]/[max]) appear as separate configs (44-config export mentioned in Zain's LinkedIn writeup). For an early-talk slide, rebuild this as a cost-vs-accuracy scatter with `scripts/charts/deck_chart.py` from the live leaderboard — it is exactly "price/effort/accuracy of the different models" and is fresher than the tweet.

## Linked content summaries

**Together AI blog: "Kimi K3 vs Claude Fable 5 on DeepSWE: Cost and Coding"** (2026-07-24, Zain Hasan & Shobhit Dixit, https://www.together.ai/blog/kimi-k3-vs-claude-fable-5-on-deepswe-cost-and-coding):
Methodology: DeepSWE = 113 real long-horizon feature requests from live open-source repos, 4 trials each (452 rollouts/model), pass/fail by hidden test suites; Kimi K3 at max vs Fable 5 at xhigh. Full sweep cost: $2,103 (Kimi) vs $6,010 (Fable). All thread numbers above + framing: "Kimi K3 matches Claude Fable 5 on quality, costs a third as much per solved task, and as an open model gives teams full control over their deployment"; Fable is "the more reliable model" (58 vs 45 tasks solved 4/4). Six charts (URLs in repo notes; Webflow CDN).

**DeepSWE benchmark** (Datacurve, https://deepswe.datacurve.ai): contamination-free benchmark, 113 tasks / 91 repos / 5 languages, built to separate frontier models that cluster on SWE-bench. v1.1 revision blog (deepswe.datacurve.ai/blog/deepswe-v1-1) explains score shifts of a few points vs v1.

## Relevance to the talk

Louis wants this early in the talk. Three usable messages for founders: (1) **model choice is now a price/accuracy/effort trade-off, not a single "best model"** — the DeepSWE leaderboard scatter makes this visual; (2) **open-weight caught up**: Kimi K3 within 1.4pt of Fable 5 at pass@1, ahead at pass@2/4, at ~35% of the price — "the open frontier isn't 6 months behind anymore"; (3) **agentic nuance**: reliability vs coverage — Fable steadier per attempt (matters when retries are expensive), Kimi wider net per dollar (matters for retry-tolerant agent loops). Bridges naturally to Claude Code best practices (choosing effort, when retries beat one expensive attempt).

## Freshness & sourcing gaps

- **Age**: 1.5 months (2026-07-18 thread, 07-24 blog). Benchmark ALREADY MOVED: DeepSWE v1.1 (leaderboard updated 2026-08-20) now has claude-opus-5[max] on top at 74%, and Kimi K3 shown at 69%±5 — the thread's exact pass@1 figures (69.9/68.5) are v1-era and superseded. Cite the live leaderboard for numbers, the Together blog for the deep-dive analysis.
- **Sourcing quality**: GOOD for the analysis (vendor-published but methodology-transparent; Together sells Kimi inference — conflict of interest to mention). The DeepSWE leaderboard (Datacurve) is the neutral primary source.
- **Gaps / deep research needed**: (1) Pull the current leaderboard table (all configs incl. effort levels) on talk-eve and regenerate the scatter — numbers churn weekly. (2) If quoting "~35% of the price", note it's cost/rollout at max-vs-xhigh settings on this one benchmark, not list-price tokens (list: K3 $3/$15 vs Fable $10/$50 per Mtok ≈ 70% cheaper). (3) Wall-clock caveat: Kimi 66min vs Fable 21min median rollout at time of test.
