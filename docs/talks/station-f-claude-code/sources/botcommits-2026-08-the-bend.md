<!-- ABOUTME: Source note — botcommits.dev now reports the Claude Code commit curve bending from exponential to sigmoid. -->
<!-- ABOUTME: Contradicts the June-2026 framing in the parent deck; reframes S05 and sharpens the talk's spine. -->

# botcommits.dev, August 2026 — "The Exponential Bent"

**Fetched**: 2026-08-31 · **Page updated**: 2026-08-18 · **Last full month in data**: 2026-07
**URL**: https://botcommits.dev · **Data**: https://botcommits.dev/data.json (downloadable JSON)
**What it is**: monthly counts of AI-attributed commits on public GitHub by tool (Claude Code,
Copilot coding agent, Jules, Codex, Gemini Code Assist, Devin, Aider), Jan 2025 onward.

## Why this matters: it contradicts the deck we inherited

The parent deck (`slides/heuritech-agents`, verified 2026-06-10) teaches an **acceleration**:
0% → 4% → 10% of public commits, the last jump in six weeks. Five more months of data have
bent that curve. The tracker's own headline is now **"The Exponential Bent"**, and its lead
sentence is *"Five more months of data say otherwise"*.

## The numbers (from `data.json`, headline block)

| Figure | Value |
|---|---|
| Claude Code commits, July 2026 (last full month) | **19,804,129** |
| Month-on-month growth, latest | **+14%** (was **+89%** in March) |
| Doubling time, now | **2.62 months** (was **1.22 months** in March) |
| What the March exponential predicted for that month | **98,478,304** — the forecast overshot by ~5× |
| Best-fitting model now | **Gompertz** (sigmoid), for both Claude and the all-tools series |
| Fitted inflection point | **2026-04** |
| Estimated ceiling, public Claude commits/month | **22.5M** (logistic) to **29.6M** (Gompertz) |
| AI share of public push events, latest | **17.8%** |
| Cumulative Claude Code commits since Jan 2025 | **96,418,643** |

**July 2026 (19.8M) already sits at roughly 66-88% of the estimated ceiling.**

## Caveats that must be spoken, not buried

- **August 2026 is a PARTIAL month** in the series (9.0M, `partial: true`, last full index 18).
  It is not a decline. Do not put the August bar on a slide without marking it partial.
- **Instrument change mid-series**: BigQuery / GH Archive through Sep 2025, then windowed
  GitHub Search API counts. The series is not one instrument end to end.
- **The share denominator is genuinely uncertain.** The page states the honest range itself:
  *"~6% of commits at 3:1, ~18% at 1:1"* depending on commits-per-push. The 17.8% figure is
  a share of **push events**, not of commits. Quote the range, not the single number.
- The page notes SemiAnalysis's March-2026 estimate was **4.5% of public commits** for Claude
  Code — which does not agree with the parent deck's "10% of all commits" framing. The parent
  deck's number needs re-checking against its own source before reuse.
- The page dropped its earlier "×2.5 code-volume adjustment" as indefensible.
- **AI-attributed only**: agents that leave no signature (Cursor, most Copilot completion use)
  are invisible here, so the true AI share is higher than any number on this page.

## Registry entry (quote grep-verified 2026-08-31)

The page injects its numbers client-side, which is exactly why the inherited registry quote
now fails: **no number on this page is greppable in the static HTML.** Use a static prose
quote and put the figures in the slide, sourced to the page.

```yaml
  - id: botcommits-the-bend
    url: https://botcommits.dev
    authority: botcommits.dev
    title: "AI-Attributed Commits on GitHub: The Exponential Bent"
    quote: "Five more months of data say otherwise"
```
Verified: `curl -s https://botcommits.dev | grep -c "Five more months of data say otherwise"` → 1.
("The Exponential Bent" also greps → 1, and is the better quote if the title is what we cite.)

## What this does to the talk

It gives M1 a spine that is stronger and more honest than "everything is exponential":

> **Two curves we quoted in April have bent.** The capability benchmark (METR) stopped
> measuring the frontier once labs optimised for it. The adoption curve (agent-authored
> commits) turned out to be a sigmoid whose inflection was April 2026. What still compounds
> is not the trend line — it is the thing you build: the harness, the loop, the written
> memory.

That reframes **S05** from "look how fast this is growing" to "the growth bent, here is what
that means", and it pairs with **S07** (the benchmark treadmill) as the same lesson twice,
from two independent measurements. It is also the most defensible thing a speaker can do in
front of founders who saw the April deck: correct your own slide, on the record, with data.
