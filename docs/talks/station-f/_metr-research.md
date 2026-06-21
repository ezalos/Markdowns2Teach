# METR research extract — for Station F slide A-04

**Canonical source URL**: https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
**Title**: Measuring AI Ability to Complete Long Tasks
**Authors**: Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment, Nate Rush, Sydney Von Arx, Ryan Bloom, Thomas Broadley, Haoxing Du, Brian Goodrich, Nikola Jurkovic, Luke Harold Miles, Seraphina Nix, Tao Lin, Neev Parikh, David Rein, Lucas Jun Koba Sato, Hjalmar Wijk, Daniel M. Ziegler, Elizabeth Barnes, Lawrence Chan (25 authors)
**Publication date**: 2025-03-19
**Accessed**: 2026-04-14

Companion sources used:
- `https://metr.org/time-horizons/` (dedicated time-horizons page, last updated 2026-04-10)
- `https://arxiv.org/abs/2503.14499` (paper, full title: *Measuring AI Ability to Complete Long Software Tasks*, v3 dated 2026-02-25, licensed **CC BY 4.0**)
- `https://metr.org/assets/benchmark_results_1_1.yaml` (raw TH-1.1 datapoints)

## What METR measures

> "The **task-completion time horizon** is the task duration (measured by human expert completion time) at which an AI agent is predicted to succeed with a given level of reliability. For example, the 50%-time horizon is the duration at which an agent is predicted to succeed half the time." (time-horizons page)

> "On a diverse set of multi-step software and reasoning tasks, we record the time needed to complete the task for humans with appropriate expertise. We find that the time taken by human experts is strongly predictive of model success on a given task: current models have almost 100% success rate on tasks taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours." (March 2025 blog post)

> "For each model, we can fit a logistic curve to predict model success probability using human task length. After fixing a success probability, we can then convert each model's predicted success curve into a time duration, by looking at the length of task where the predicted success curve intersects with that probability." (March 2025 blog post)

Task suite: tasks are drawn from **RE-Bench**, **HCAST** (Human-Calibrated Autonomy Software Tasks), and a set of shorter novel software tasks (SWAA) — primarily software engineering, ML, and cybersecurity. The combined benchmark is called **METR-HRS**.

## Headline finding (verbatim)

> "We propose measuring AI performance in terms of the *length* of tasks AI agents can complete. We show that this metric has been consistently exponentially increasing over the past 6 years, **with a doubling time of around 7 months**. Extrapolating this trend predicts that, in under a decade, we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks." — opening summary, 2025-03-19 blog post

> "If we plot this on a logarithmic scale, we can see that the length of tasks models can complete is well predicted by an exponential trend, with a doubling time of around 7 months." — same post, body

Refined figures from the **Time Horizon 1.1** update (2026-01-29 release announcement, reiterated on the live time-horizons page):

> "P50 doubling time [all-time]: 195.8 days [162, 223] (TH1.0) / 196.5 days (TH1.1)" — i.e. ~6.5 months overall
> "P50 doubling time, >=2023: 165.3 days [129, 211] (TH1.0) / 130.8 days [107, 161] (TH1.1)" — ~4.3 months in the recent regime
> "P50 doubling time, >=2024: 108.9 days (TH1.0) / 88.6 days (TH1.1)" — ~2.9 months in 2024+

The "doubled every 7 months, possibly accelerating to every 4 months in 2024" framing is also restated in METR's July 2025 cross-domain follow-up.

## Time-series datapoints (verbatim from benchmark_results_1_1.yaml)

50%-time horizons for state-of-the-art models, Time Horizon 1.1 methodology (minutes of human-expert task length):

| Model | Release date | p50 horizon |
|---|---|---|
| GPT-2 | 2019-02-14 | 0.054 min (~3 s) |
| davinci-002 | 2020-05-28 | 0.144 min (~9 s) |
| GPT-3.5-turbo-instruct | 2022-03-15 | 0.60 min (~36 s) |
| GPT-4 | 2023-03-14 | 3.99 min |
| GPT-4-1106 (turbo preview) | 2023-11-06 | 4.04 min |
| Claude 3 Opus | 2024-03-04 | 3.95 min |
| GPT-4-turbo | 2024-04-09 | 3.73 min |
| GPT-4o | 2024-05-13 | 6.99 min |
| Claude 3.5 Sonnet (June) | 2024-06-20 | 11.4 min |
| o1-preview | 2024-09-12 | 20.3 min |
| Claude 3.5 Sonnet (Oct) | 2024-10-22 | 20.5 min |
| o1 | 2024-12-05 | 38.8 min |
| Claude 3.7 Sonnet | 2025-02-24 | 60.4 min (~1 h) |
| Claude 4 Opus | 2025-05-22 | 100.4 min |
| Claude 4.1 Opus | 2025-08-05 | 100.5 min |
| o3 | 2025-04-16 | 119.7 min (~2 h) |
| GPT-5 | 2025-08-07 | 203.0 min (~3 h 23) |
| Gemini 3 Pro | 2025-11-18 | 224.3 min |
| GPT-5.1-Codex-Max | 2025-11-19 | 223.7 min |
| Claude Opus 4.5 | 2025-11-24 | 293.0 min (~4 h 53) |
| GPT-5.2 | 2025-12-11 | 352.2 min (~5 h 52) |
| GPT-5.3-Codex | 2026-02-05 | 349.5 min |
| Claude Opus 4.6 | 2026-02-05 | 718.8 min (~12 h) |
| GPT-5.4 | 2026-03-05 | 341.7 min |

Raw YAML also reports `doubling_time_in_days.all_time_stitched.point_estimate = 187.778` days and `from_2023_on.point_estimate = 128.744` days [CI 104–158].

For Louis's slide: the "1 minute (2020) → ~4 hours (end 2025)" narrative is fully backed — GPT-3-class models sat at sub-minute in 2020, and by Nov 2025 Claude Opus 4.5 hits ~4h53. Claude Opus 4.6 (Feb 2026) jumps to ~12h but has a very wide CI [316, 3633 min].

## The published chart

- **Chart image URL (primary, time-horizon headline figure)**: the March 2025 blog post embeds the chart inline but does not expose a direct PNG URL in the HTML; the live replacement chart lives on `https://metr.org/time-horizons/` as an interactive D3/Plotly figure, source data at `https://metr.org/assets/task_results_1_1.yaml`. A companion cross-domain image is served at `https://metr.org/assets/images/time-horizon-domains/time-horizons-increasing.png` and the fit-comparison figure at `https://metr.org/assets/images/measuring-ai-ability-to-complete-long-tasks/linear-exponential-hyperbolic-fits.png`.
- **License / attribution requirements**:
  - **metr.org site**: the site footer reads `© 2026 METR. All rights reserved.` No explicit Creative Commons license on the blog post or time-horizons page. Using the metr.org-hosted PNG verbatim would technically need permission or fair-use justification.
  - **arXiv paper (Kwa et al. 2025, arXiv:2503.14499)**: licensed **CC BY 4.0** per the arXiv landing page. Figures from the paper PDF are therefore reusable with attribution.
- **Recommended in-slide treatment**: **both** — (1) use a figure pulled directly from the arXiv PDF (CC BY 4.0 — attribute "Kwa, West et al. 2025, arXiv:2503.14499, CC BY 4.0"), OR (2) redraw via paperbanana using the datapoints above (cleaner, matches slide theme, only needs light attribution). If citing the blog post's chart image, contact METR or treat as illustrative fair-use with prominent source link.

## Quotes worth slide-using

> "The length of tasks models can complete is well predicted by an exponential trend, with a doubling time of around 7 months."

> "Extrapolating this trend predicts that, in under a decade, we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks."

> "Current models have almost 100% success rate on tasks taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours." (March 2025 baseline — already obsolete by 2026)

## Citation footer block (ready to paste into slide)

`<small>Sources : [1] [METR — Measuring AI Ability to Complete Long Tasks](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) · [2] [Kwa et al. 2025, arXiv:2503.14499 (CC BY 4.0)](https://arxiv.org/abs/2503.14499)</small>`

## Notes for Louis

- **Tavily worked for everything**: `tavily_search` located the canonical URL on the first query; `tavily_extract` pulled the full blog post, the time-horizons page, and the raw benchmark YAML. WebFetch was denied for the YAML URL, but Tavily extract handled it. WebFetch **did** work for the arXiv abstract page and gave us the CC BY 4.0 license confirmation — so both tool paths were exercised.
- **Doubling-time caveat**: the "7 months" figure is the headline from March 2025 and remains METR's long-run number (TH1.1 all-time estimate = 196.5 days). If the slide wants a more aggressive recent number, METR explicitly says **~4 months since 2024** (88.6 days under TH1.1 for ≥2024 models). Quote the 7-month number since it's the canonical one, but mention the 4-month acceleration as a parenthetical if there's room.
- **Chart-license gotcha**: metr.org has no site-wide CC license, only the arXiv paper does. If Louis embeds the PNG straight from `metr.org/assets/...` he should note it as "illustrative, © METR" or replace it with a redraw / arXiv version. Safest path = redraw via paperbanana from the datapoints table above.
- **Data freshness**: the raw YAML was fetched 2026-04-14 and includes models up to GPT-5.4 (2026-03-05). The slide can honestly say "the trend has held through 2026" not just "through 2025".
- **Surprise**: Claude Opus 4.6 (Feb 2026) measures at ~12 h p50 horizon but with an extremely wide CI (5.3h–60.5h). Treat the ≥2026 upper end with caution and prefer Claude Opus 4.5 (~5h, Nov 2025) as the clean "late-2025 frontier" datapoint for narrative purposes.
- **Paper title mismatch**: the blog post is titled "Measuring AI Ability to Complete Long **Tasks**", the arXiv paper is titled "Measuring AI Ability to Complete Long **Software** Tasks". The arXiv title is more precise (scope limited to SWE/ML/cybersec tasks). Cite the blog-post title unless accuracy about scope matters on the slide.
