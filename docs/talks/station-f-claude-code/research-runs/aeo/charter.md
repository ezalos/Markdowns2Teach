# How real is AI-assistant referral traffic in 2026, and what actually moves it?

## Decision this feeds

**S53 "AEO"** in the 2026-09-02 Station F founders' talk — the most directly actionable
slide for the room: schedule an agent to research and improve how AI assistants describe
and recommend your product, weekly, for roughly nothing. The only source so far is one
founder's tweet, including a self-reported projection that answer-engine optimisation will
drive one million dollars of revenue next year and an anecdote of roughly three hundred
customers referred by a chat assistant. The decision: **what measured data carries the
slide**, with the founder's projection demoted to a labelled anecdote on top of it.

## Must answer

- **The traffic curve**: the best measured data on referral traffic from AI assistants (ChatGPT, Claude, Perplexity, Google's AI surfaces) to websites — share of total referrals, growth rate, and how it is measured. Prefer infrastructure-level measurement (Cloudflare Radar and equivalents) and large-scale analytics vendors over search-marketing content.
- **Conversion quality**: published evidence on whether visitors arriving from an AI assistant convert better or worse than visitors from classic search, with the sample and method stated. Several analytics vendors published on this; find the primary.
- **What actually works, with evidence**: which answer-engine-optimisation practices have measured effect rather than folklore. Specifically test the status of llms.txt (is any major assistant documented as reading it?), structured data, documentation and community presence as citation sources, and whether being cited by assistants tracks classic search ranking or diverges from it.
- **How assistants choose what to cite**: what the assistant vendors themselves document about retrieval and citation selection, and any independent study of which sources get cited disproportionately.
- **The self-preference question**: is there evidence that content optimised with one model is disproportionately recommended by that same model? The tweet raises it as an open question; report the evidence on model self-preference in recommendation and judging, or state that the specific question is unanswered.
- **The automation pattern**: documented examples of scheduled agent automations running this kind of weekly research loop, with what they produced and what they cost. Any first-party documentation of scheduled agent runs in the major coding-agent products.
- **The measurement problem**: how a small team can actually attribute AI-assistant referrals, given that many assistants strip or omit referrer headers. The practical method, sourced.

## Source bar

tier: Internet-infrastructure and analytics primaries first (Cloudflare, large analytics platforms, Adobe-scale retail datasets), then assistant vendors' own documentation, then peer-reviewed or preprint studies. Search-engine-optimisation vendor blogs are acceptable only for existence claims and must be labelled as vendor content with a commercial interest. A number without a page quoting it verbatim does not ship.

recency: 2026 measurements strongly preferred; 2025 baselines allowed for showing a trend and must be dated. Note where a measurement predates a major assistant product change.

## Deliverable

A Markdown report with: one headline traffic figure and one conversion figure, each with an exact clickable URL and verbatim quote; a table of practices rated evidence-backed, plausible-but-unmeasured, or folklore, with a source per row; a short section on attribution method; and a paragraph placing the founder's one-million-dollar projection correctly as a labelled anecdote relative to the measured data.

## Out of scope

- Classic search-engine-optimisation tactics unrelated to AI assistants.
- Paid placement and advertising inside assistants.
- Any tool purchase recommendation.
