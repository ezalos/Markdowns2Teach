# What actually measures frontier AI capability in September 2026, now that METR's time-horizon benchmark is overfit?

## Decision this feeds

A talk to startup founders at the Incubateur 42 / Station F on 2026-09-02 opens with a
"state of play" movement. Its trajectory slide has used METR's time-horizon curve (task
length completed at 50% success doubles every ~7 months) since early 2026. The speaker's
judgment is that **METR stopped being a valid frontier indicator around April 2026 because
labs began optimising for it — it is now an overfit benchmark.** The decision this research
feeds: **which one or two evaluations replace it on that slide**, and what the honest
current numbers are. The slide must survive a room of technical founders who follow this
space daily, and every figure must carry a clickable exact primary URL plus a verbatim
quote (project citation rule).

Explicitly NOT wanted: preference/human-likeness leaderboards (LMArena/Chatbot Arena
Elo and equivalents) as the headline measure. The speaker considers those a measure of
human-likeness and style, not capability. Report on them only to explain why they are
the wrong instrument, and only briefly.

## Must answer

- **Is the overfit claim true, and what is the evidence?** Document what happened to METR's time-horizon benchmark between roughly March 2026 and now: methodology critiques, evidence of labs targeting it, task-set contamination, saturation, divergence between benchmark score and real-world autonomy. Name who made each critique and when, include METR's own responses and any methodology revisions they published. If the claim is weaker than stated, say so plainly — the speaker would rather correct his own belief than assert a wrong one on stage.
- **Which evaluations do credible practitioners now use to track frontier capability?** For each: what it measures, who runs it, how it resists gaming (held-out/private sets, rotating tasks, human-expert baselines, contamination controls), current top scores with model names and dates, and known weaknesses. Cover at minimum: long-horizon agentic work, real economic/professional tasks, software engineering beyond SWE-bench, research capability, and any held-out/uncontaminated general benchmark.
- **Which of them are contamination- and Goodhart-resistant by construction?** Rank the candidates on that specific axis and explain the mechanism — this is the property that makes a benchmark worth putting on a September-2026 slide.
- **The single best chart to show capability trajectory today**: identify a specific, currently maintained, publicly published figure or dataset (exact URL plus licence/attribution terms) that a talk can reproduce or rebuild. If no single chart works and the trajectory needs 2-3 measures side by side, say that and name them.
- **Price × capability**: the current defensible way to show capability-per-dollar still collapsing, given that cross-generation inference-price comparisons are contested. Name the specific dataset or leaderboard (Epoch AI inference-price work, agentic-coding leaderboards publishing $/task alongside accuracy) with current numbers.
- **What the frontier labs themselves report** in their September-2026 model cards and system cards as capability evidence — which evals appear there, and what that says about which measures the field now treats as load-bearing.
- **The honest ceiling**: the strongest published evidence that current agents still fail at something economically important (long-horizon reliability, novel discovery, error compounding) — one or two crisp, citable results.

## Source bar

tier: Primary and independent first. Benchmark operators' own pages and papers
(metr.org, arcprize.org, epoch.ai, benchmark leaderboard sites), arXiv papers, lab model
cards and system cards, and named practitioners with verifiable track records. Reputable
technical press (Bloomberg, The Information, SemiAnalysis) only for corroboration of
facts, never as the sole source for a number. Vendor blog posts are acceptable ONLY when
clearly labelled as self-reported, and every self-reported figure must be marked as such
in the report.

recency: The core answer must reflect the state as of September 2026. Anything older
than 2026-06-01 must be labelled with its date and justified as still current. Where a
leaderboard is live and moves weekly, record the exact snapshot date and the URL so the
figure can be re-checked the day before the talk.

## Deliverable

A Markdown report with:
- A 5-line executive answer: what replaced METR, and the one or two measures to put on
  the slide.
- A verdict on the overfit claim, with the evidence for and against, stated flat.
- A comparison table of candidate evaluations: name · what it measures · operator ·
  gaming-resistance mechanism · current top score + model + date · exact URL · weakness.
- For every number that could go on a slide: the exact clickable URL AND a verbatim
  quote from that page containing the number (this feeds a citation registry that greps
  the quote character-by-character — a paraphrase fails the gate).
- A "chart candidates" section with direct figure/dataset URLs and their attribution terms.
- A "re-check before the talk" list: which live leaderboards move, and their URLs.

## Out of scope

- Preference/Elo leaderboards as a headline measure (covered only as a brief "why not").
- Benchmark results for image, video, audio or robotics models.
- Any recommendation about which model to buy or use.
- Building the chart itself — this run produces the sourced material, not the artifact.
