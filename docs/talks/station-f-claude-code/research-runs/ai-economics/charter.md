# What are the defensible September-2026 numbers for agent adoption and the AI economy?

## Decision this feeds

Two slides of the 2026-09-02 Station F founders' talk. **S05 "Agents are already doing the
work"** carries the proof-of-reality numbers (share of public GitHub commits authored by an
agent, Claude Code revenue, an autonomous-resolution rate in production) — every figure on
it was verified 2026-06-10 and is now beyond the speaker's three-month staleness bar.
**S06 "The AI economy in dollars"** is a new slide built on Exponential View's "State of the
AI Economy" (revenue, run rate, adoption speed versus prior IT waves, and the CapEx-versus-
revenue tension). The decision: **which numbers go on those two slides, from which primary
pages, with what caveats spoken out loud.** Each figure needs an exact clickable URL and a
verbatim quote, because a citation gate greps the quote character-by-character.

## Must answer

- **Agent-authored code share — and whether the curve bent.** On 2026-08-31 botcommits.dev was re-read and it now reports a bend: Claude Code commits at 19,804,129 in July 2026, month-on-month growth down to +14% from +89% in March, doubling time 2.62 months against 1.22, a Gompertz fit beating the exponential, inflection at 2026-04, and an estimated ceiling of 22.5M to 29.6M commits per month. **Corroborate or contradict this bend with independent sources** — SemiAnalysis, GitHub's own Octoverse reporting, any other AI-commit tracker. Establish the honest current share of public commits attributable to coding agents, and to Claude Code specifically, with the denominator stated (the tracker itself gives a 6% to 18% range depending on commits-per-push). Prior anchor being corrected: the parent deck's "10% of all public commits, up from 4% in six weeks", read 2026-06-10.
- **Claude Code and Anthropic revenue**: latest reported annualised revenue or run rate for Claude Code and for Anthropic overall, from company statements or top-tier financial press. Prior anchors: $2.5B Claude Code annualised (VentureBeat), $30B Anthropic run rate. Mark clearly what is company-reported versus independently verified.
- **Exponential View's State of the AI Economy**: pull the report's own page and confirm or correct these figures with verbatim quotes — $110bn trailing-twelve-month GenAI revenue, $175bn run rate, adoption 3× faster than prior IT waves, ~$2T CapEx against revenue that barely covers depreciation. Note whether the report has been updated since 2026-06-25.
- **The CapEx sustainability tension**: the best-argued current analysis of whether AI infrastructure spending can be earned back, from a source that is neither a vendor nor a permabear. One or two crisp numbers a founder can hold, plus the strongest counter-argument.
- **One production-agent outcome number** better than the current anchor (Intercom Fin: 76% of support conversations resolved autonomously at $0.99 per resolution, vendor-defined). Named company, measured outcome, primary source. If nothing beats it, say so and give the caveat to speak aloud.
- **Enterprise adoption reality**: the most credible September-2026 measure of how many companies actually run agents in production versus pilots, with the survey's method and sample stated, since these surveys vary wildly in quality.

## Source bar

tier: Company investor statements and official blogs for their own revenue; independent measurement projects and research orgs (Epoch AI, SemiAnalysis, academic groups) for cross-cutting figures; Bloomberg, The Information, Financial Times, CNBC for corroboration. Vendor-reported outcome metrics are acceptable only when labelled vendor-reported with their definition stated. Reject any figure that cannot be traced to a page containing it verbatim.

recency: State of play as of September 2026. Every figure carries its measurement date. Anything measured before 2026-06-01 must be flagged as an anchor being updated, not presented as current. Live trackers must be named with their URL so they can be re-checked the day before the talk.

## Deliverable

A Markdown report with: a slide-ready table for S05 and one for S06 — figure · exact clickable URL · verbatim quote containing the figure · measurement date · one-line caveat to speak · self-reported yes/no. Then a short section naming which prior anchors were superseded and by what, and a "re-check before the talk" list of live trackers.

## Out of scope

- Model capability and benchmark scores (a separate run covers those).
- Stock prices, valuations, and investment advice.
- Any number that cannot be sourced to a page quoting it verbatim.
