# How long does frontier capability take to become runnable on hardware a startup owns?

## Decision this feeds

**S10** of the 2026-09-02 Station F founders' talk, sitting between the cost-collapse slide
and the state-of-play close. The point of the slide is a build-versus-wait decision: if the
capability you need is expensive today, how long until it is cheap or local? The current
source is unusable — an unattributed r/LocalLLaMA chart claiming a ~24.8-month cloud-to-laptop
lag, whose permalink could not be recovered and whose sample is four generations. A sibling
run has already established one replacement anchor: Epoch AI measures open models lagging
frontier closed models by **an average of four months** on its capabilities index. The
decision: **what the slide claims about the lag, on data a founder can check.**

## Must answer

- **Separate the two lags, because the community chart conflates them.** Lag A: an open-weights model matching frontier closed-model capability, at any size. Lag B: that capability fitting on hardware a small team owns (a 128GB workstation, a single H100, a high-memory laptop). Give a current number for each with its measurement and date. Epoch AI's open-versus-closed gap analysis is the starting anchor for Lag A — confirm it is current and find whether anyone measures Lag B systematically.
- **Three verifiable pairs for Lag B**: name specific open-weight models runnable today on named consumer or prosumer hardware, and state which frontier-era capability each matches, with benchmark numbers from a source that evaluated both. Prefer an independent evaluator over model cards.
- **The quantization tax, current numbers**: how much capability is actually lost at 4-bit and similar quantization for agentic and coding work specifically, as opposed to perplexity or short-answer benchmarks. This is where the "runs locally" claim usually breaks.
- **Is the gap closing or widening in 2026?** Reasoning-heavy and agentic workloads may behave differently from the general trend, since test-time compute changes the economics of running anything locally. Report what the data shows, including any evidence the gap is widening for long-horizon agentic tasks.
- **The honest cost comparison**: for a small team, what does it actually cost to run a capable open model locally (hardware amortised, power, throughput) against paying an API for the same work? Any published total-cost analysis, and the break-even shape.
- **EU sovereign options as of September 2026**: which providers serve frontier-class open-weight models from EU-hosted infrastructure with GDPR terms, and what has changed since June 2026.

## Source bar

tier: Independent measurement organisations first, Epoch AI above all for capability-gap trends; then peer-reviewed or preprint evaluations of quantization; then independent benchmark operators. Model cards and vendor blogs are acceptable only for stating what a model is, never for comparative claims. Community charts, Reddit posts and aggregator blogs do not ship, and may be used only to identify a claim worth verifying elsewhere.

recency: September 2026 state of play. Every number carries its date. Where a trend is quoted, give the window it was fitted over.

## Deliverable

A Markdown report with: one headline number for each of the two lags, each with an exact clickable URL and a verbatim quote; a table of three verified model-and-hardware pairs; a short quantization-tax section with agentic-task numbers; a paragraph on whether the gap is closing or widening with the evidence; and an explicit statement of whether the r/LocalLLaMA ~24.8-month claim is supportable, replaceable, or should be dropped from the talk.

## Out of scope

- Model recommendations and hardware purchasing advice.
- Fine-tuning, training costs and distillation methods.
- Anything about closed-model pricing beyond what the cost comparison needs.
