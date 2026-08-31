# Tweet 2074078414705955006 — "Fable may run locally in 2 years" (cloud-to-laptop lag chart)

## Header

- **URL**: https://x.com/kimmonismus/status/2074078414705955006
- **Author**: Chubby♨️ (@kimmonismus) — tech analyst/content creator, Editor-in-Chief @getsuperintel; 137.7K followers, verified
- **Date**: 2026-07-06 10:30 UTC
- **Engagement**: 2,846 likes · 208 RT · 70 quotes · 194 replies · 836 bookmarks · 480.0K views
- **Fetch method**: fxtwitter API (full note-tweet text + media); threadreaderapp had no unroll; fxtwitter shows `replying_to: null` and no self-thread was found — treated as a SINGLE tweet (full text captured, no thread)
- **Thread status**: single tweet (head only, complete)

## Full text (verbatim)

"Fable 5 probably running locally in about two years.

That is the projection in this r/LocalLLaMA chart. It tracks how long it takes for cloud-frontier capability to become broadly comparable in laptop-runnable open-weight models. The observed average lag: ~24.8 months.

GPT-3-class capability: 37 months.
GPT-3.5-class: 17 months.
GPT-4-class: ~24 months.

The projection puts Fable / Mythos 5-class capability on high-end consumer hardware around July 2028."

## Media described

**Chart screenshot** (saved: `videos/tweet-2074078414705955006-local-lag-chart.jpg`, 1448x1194): a screenshot of an X "News"-tab card showing an **r/LocalLLaMA post by u/PetersOdyssey** titled "If trends hold, Mythos-class capability may be running on high-end consumer hardware within ~2 years". The embedded chart, "**From frontier to running on a laptop**":
- **Axes**: x = calendar year (2019–2029); y = capability generations as rows (GPT-2, GPT-3, ChatGPT/GPT-3.5, GPT-4, Claude 3.5/GPT-4o, GPT-5/Claude 4, Fable/Mythos). Each row: black dot = frontier launch, green square = laptop-runnable open-weight equivalent, solid blue line = observed lag, dashed line = projected lag. Header: "Observed average lag: 24.8 months".
- **Data points**: GPT-2 laptop-runnable at release (Feb 2019, 0 months — excluded from the average). GPT-3 API Jun 2020 → Llama 2 70B class Jul 2023 = **37 months**. ChatGPT/GPT-3.5 Nov 2022 → Llama 3 70B class Apr 2024 = **17 months**. GPT-4 Mar 2023 → Gemma 3 / Qwen3 class Mar 2025 = **24 months**. Claude 3.5 Sonnet Jun 2024 → Gemma 4 31B Apr 2026 = **21 months**. Projected: Claude 4 / GPT-5 May 2025 → laptop match ~Jun 2027 (~25 months); **Fable / Mythos 5 Jun 2026 → projected laptop match ~Jul 2028 (~25 months)**.
- **Fine print**: "Equivalent" = broad practical comparability, not full parity across multimodal, tool-use, safety, latency, or product behavior; laptop-runnable can mean a high-RAM laptop with quantized weights; dashed rows are estimates based on the updated observed average.

## Linked content summaries

No external link in the tweet itself; the substantive source is the r/LocalLLaMA post the screenshot shows.
- **Original post**: r/LocalLLaMA, u/PetersOdyssey, ~2026-07-05/06 — exact post URL NOT recovered (Reddit search via tavily did not surface it; would need a Reddit search session to pin the permalink).
- **Context coverage found**: explainx.ai blog "Fable 5 Local by 2028? r/LocalLLaMA Lag Chart" (https://explainx.ai/blog/claude-fable-5-local-hardware-projection-2028-localllama-2026) documents the virality (X news tab, 153+ posts, Polymarket amplification, this kimmonismus tweet) and stresses the chart's limits: it is a **historical lag average, not a claim that Claude Fable weights will be released** — it projects when *open-weight models of comparable capability* run on consumer hardware.
- **Complicating data point**: an earlier r/LocalLLaMA post (https://www.reddit.com/r/LocalLLaMA/comments/1mrfqsd/) cites **Epoch AI** data showing local/open-weight models lag the frontier by only ~9 months *on benchmarks* — different claim (benchmark parity of any open model vs laptop-RUNNABLE parity), but a slide should not confuse the two lags.

## Relevance to the talk

The "Fable may run locally in 2 years" beat: for founders, the strategic read is that **today's frontier capability becomes commodity, locally-runnable capability in ~2 years** — plan moats accordingly (data, distribution, workflow lock-in — not raw model access). Pairs perfectly with Azeem's thread tweet 11 ("last year's best models commoditize into open weights within a year") and with the Kimi-vs-Fable tweet (the open frontier already matching Fable 5 on DeepSWE at 35% of the price *in the cloud, today*). Note the two tweets give different lags (open-weight benchmark parity: months; laptop-runnable parity: ~2 years) — that contrast is itself a good slide.

## Freshness & sourcing gaps

- **Age**: 1.9 months (2026-07-06). The projection itself is long-horizon, so age matters little; the underlying observed points end Apr 2026 (Gemma 4 31B).
- **Sourcing quality**: WEAK for a citable slide — a community-made chart by a pseudonymous Redditor, relayed by an aggregator account; no methodology beyond the fine print; "class-equivalent" judgments are subjective; n=4 observed lags with high variance (17–37 months) — the "24.8-month average" carries false precision. The claim "Fable 5 running locally" is strictly wrong as worded (it's about equivalent-capability open weights, and Anthropic does not release weights).
- **Gaps / deep research needed**: (1) Recover the exact r/LocalLLaMA permalink (Reddit search) if the chart itself goes on a slide — CLAUDE.md requires an exact clickable source. (2) Better primary source for the same story: **Epoch AI's open-vs-closed capability-lag analyses** (epoch.ai) — quantified, methodology-documented, citable; reconcile the ~9-month benchmark-parity figure with the ~25-month laptop-runnable figure. (3) If the slide needs it, verify the individual anchor dates (Llama 2: Jul 2023; Llama 3: Apr 2024; Gemma 3/Qwen3: Mar 2025 — all easy to source from vendor announcements). Consider rebuilding the chart with deck_chart.py from verified dates rather than screenshotting Reddit.
