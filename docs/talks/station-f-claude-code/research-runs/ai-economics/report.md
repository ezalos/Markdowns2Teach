# Defensible September-2026 numbers for agent adoption and the AI economy

Research run for the Station F founders' talk, 2026-09-02 — slides **S05 "Agents are already
doing the work"** and **S06 "The AI economy in dollars"**.
Research executed 2026-08-31. Every figure below was fetched and quoted the same day.

---

## 1. Bottom line, in four sentences

The exponential in agent-authored code **bent**, and the tracker that first reported the
exponential is the one reporting the bend: Claude Code public commits hit **19,804,129 in July
2026** with month-on-month growth down to **+14%** from **+89%** in March, doubling time
**2.62 months** against 1.22, sigmoid fits now beating the exponential with an inflection at
**2026-04** and a ceiling around **22–30M commits/month** [1][2]. The honest share number is a
**range, not a point**: AI-attributed commits are **17.8% of public push events**, which is
**~6% to ~18% of commits** depending on an unresolved commits-per-push ratio [1][2] — so the
deck's old "10% of all public commits" is inside the range but was never a measured point.
On the money side, Anthropic's run rate is **$65bn at the end of July 2026** (told to
investors, reported by Bloomberg and confirmed by CNBC) [9][10], while the last **company-
reported** Claude Code figure is still **$2.5bn from 12 February 2026** [7] — no top-tier
source has published a newer standalone Claude Code number, and the $8bn figure circulating in
SEO aggregators traces to no primary page. Exponential View's June-2026 report holds up
verbatim on all four figures — **$110bn trailing-twelve-month revenue, $175bn run rate, 3x
faster than any prior IT wave, $2 trillion of committed CapEx** — and the sharpest thing in it
is that revenues now cover *ongoing* depreciation with only 19–32% headroom, not the cumulative
bill [11].

---

## 2. Slide-ready table — S05 "Agents are already doing the work"

| # | Figure | Exact URL | Verbatim quote containing the figure | Measured | Caveat to speak | Self-reported |
|---|--------|-----------|--------------------------------------|----------|-----------------|---------------|
| 1 | **19,804,129** Claude Code commits on public GitHub in **July 2026** | [botcommits.dev/data.json](https://botcommits.dev/data.json) | `"claude_last": 19804129,` | July 2026 (last full month); page updated 2026-08-18 [2] | "This is a lower bound with a stated instrument — it counts the trailer Claude Code writes, not AI use." | No — independent tracker |
| 2 | Growth **bent**: +14%/mo now vs **+89%** in March; doubling **2.62 mo** vs 1.22 | [botcommits.dev](https://botcommits.dev/) | "Growth above +50%/month through March 2026; +14–26%/month since April." | Feb 2025 → Jul 2026 series [1] | "The curve bent in April. Sigmoid now beats exponential — same site that called the exponential six months ago." | No |
| 3 | Ceiling **22–30M commits/month**, inflection **April 2026** | [botcommits.dev](https://botcommits.dev/) | "linear-space fits (weighted toward the high-volume months, which is what a ceiling question needs) agree on an April 2026 inflection and a 22–30M ceiling regardless of start month" | Fit to data through Jul 2026 [1] | "A fitted ceiling is a model output, not a measurement — say 'the fits say', never 'it will be'." | No |
| 4 | AI share = **17.8% of public push events** ≈ **6–18% of commits** | [botcommits.dev](https://botcommits.dev/) | "Read the share as a range — ~6% of commits at 3:1, ~18% at 1:1 — until GitHub publishes a monthly commit denominator." | July 2026 [1][2] | "Nobody has the commit denominator. Give the range and name why: GitHub publishes pushes, not monthly commits." | No |
| 5 | Denominator anchor: **986 million commits** pushed in the Octoverse year | [github.blog](https://github.blog/news-insights/octoverse/what-986-million-code-pushes-say-about-the-developer-workflow-in-2025/) | "developers created 230+ repositories per minute and pushed 986 million commits last year" | Octoverse 2025 window, Sep 2024–Aug 2025 [4] | "GitHub's own denominator is a year old — Octoverse 2026 isn't out. That's the whole reason the share is a range." | Yes — GitHub on GitHub |
| 6 | Anthropic run rate **$65bn** at end of July 2026 | [cnbc.com](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html) | "hit $65 billion at the end of July, CNBC confirmed." | End of July 2026; published 2026-08-17 [9] | "This is a figure Anthropic told its investors, confirmed by three sources — not an audited number." | Company-reported, press-confirmed |
| 7 | Claude Code run rate **over $2.5bn** | [anthropic.com Series G](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) | "run-rate revenue has grown to over $2.5 billion; this figure has more than doubled since the beginning of 2026" | 2026-02-12 [7] | **Say the date out loud.** "That's Anthropic's February number — six months old, and it's the newest one anyone has published." | Yes — Anthropic |
| 8 | Salesforce's own help desk: **5 million conversations, 64% resolved autonomously** | [Salesforce Q2 FY27 transcript (PDF)](https://s205.q4cdn.com/626266368/files/doc_financials/2027/q2/Salesforce-Q2-FY27-Earnings-Transcript.pdf) | "Salesforce's help agent has surpassed five million customer conversations with 64% resolved autonomously." | Quarter ended 2026-07-31; call 2026-08-26 [13] | "A public company reporting its *own* support desk on an earnings call — 64%, not the 76% a vendor quotes you." | Yes — but operator on its own desk |

**Optional swap-in for #8 if you want the vendor number for contrast:** Intercom Fin's
**76% average resolution rate** across **7,000+ teams**, from Intercom's own blog, 12 March
2026 [16]. Speak the caveat: Intercom announced in that same post that it is *retiring*
resolution as the pricing metric in favour of "outcomes", so the "$0.99 per resolution" anchor
is being superseded by the vendor itself.

---

## 3. Slide-ready table — S06 "The AI economy in dollars"

| # | Figure | Exact URL | Verbatim quote containing the figure | Measured | Caveat to speak | Self-reported |
|---|--------|-----------|--------------------------------------|----------|-----------------|---------------|
| 1 | **$110bn** trailing-12-month GenAI revenue, at a **$175bn** run rate | [EV report PDF, p.7](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "$110bn trailing 12-month revenues – now at a $175bn pace" | Data to Jun 2026; published 2026-06-25 [11] | "Global ex-China, deduplicated, excludes chips and ad uplift — it's real customer money, not the whole AI economy." | No — independent research |
| 2 | GenAI scaling **3x faster** than any prior IT wave | [EV report PDF, p.9](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "The sector is growing 3x faster than any IT wave before it." | Published 2026-06-25 [11] | "Time-aligned to year zero and inflation-adjusted — a like-for-like curve, not a headline." | No |
| 3 | **$2 trillion** committed CapEx, hyperscalers + neoclouds, through 2026 | [EV report PDF, p.27](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "Hyperscalers & neoclouds have committed to $2 trillion of cumulative CapEx" | Published 2026-06-25 [11] | "Total CapEx is not AI CapEx — this includes pre-planned cloud, logistics and metaverse spend." | No |
| 4 | 2026 depreciation charge approaches **$111 billion** | [EV report PDF, p.32](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "The 2026E depreciation charge approaches $111 billion" | 2026 estimate; published 2026-06-25 [11] | "That's the annual cost of the buildout hitting the P&L — the number revenue has to beat every year." | No |
| 5 | Revenue clears depreciation with **19%** headroom (hyperscalers) / **32%** (all GenAI) | [EV report PDF, p.34](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "GenAI revenues now cover the quarterly depreciation of AI infrastructure. Q1 26 headroom reached 19% for hyperscaler/neocloud revenues and 32% across all GenAI revenues." | Q1 2026; published 2026-06-25 [11] | "It covers the *ongoing* expense, not the cumulative bill — cumulative revenue is still only about half-covered." | No |
| 6 | The counter-argument, in EV's own words: **depreciation absorbs ~81%** of hyperscaler GenAI revenue | [EV report PDF, p.34](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf) | "Coverage remains thin. Depreciation absorbs roughly 81% of hyperscaler/neocloud GenAI revenue and 68% of total GenAI revenue before additional costs." | Q1 2026 [11] | "Before opex. Before power. Before people. That's the honest version of 'it's paying back'." | No |
| 7 | 2026 CapEx guidance **$863bn**, of which **~$550bn** AI-related | [exponentialview.co, 2026-08-10](https://www.exponentialview.co/p/ai-capex-deployment-gap) | "Based on current guidance, the seven largest AI-infrastructure builders expect capital expenditure of $863 billion in 2026 – 88% more than last year." / "We estimate that roughly two-thirds, some $550 billion, will be AI-related." | Guidance as of Aug 2026 [12] | "Guidance, not spend. Companies revise it every quarter — and they have revised it up every quarter." | No |
| 8 | **$315bn** of assets not yet in service; a Meta CapEx dollar waits **~1.7 years** | [exponentialview.co, 2026-08-10](https://www.exponentialview.co/p/ai-capex-deployment-gap) | "assets not yet in service now total $315 billion, up from $281 billion one quarter earlier" / "A dollar of capex spent by Meta now waits some 1.7 years before going live, a year more than in FY2024." | Latest reported quarter, Aug 2026 [12] | "The depreciation bill you see today is from *old* spend. The wave hasn't hit the P&L yet." | No |
| 9 | Demand-side check: **43.5%** of US businesses paid Anthropic in July 2026 | [ramp.com](https://ramp.com/data/ai-index-august-2026) | "43.5% of U.S. businesses paid for subscriptions or tokens from Anthropic, up 1.1 percentage points month-over-month." | July 2026; published 2026-08-12 [18] | "Card-spend data from 70,000+ firms, not a survey — this is money actually leaving accounts." | No — Ramp's own transaction data |
| 10 | The bear note inside the bull data: **median firm spends $11.95 per employee** on AI | [ramp.com](https://ramp.com/data/ai-index-august-2026) | "The median firm spent $11.95 per employee." | July 2026 [18] | "The top 1% spend $7,400 per employee. The median firm spends twelve dollars. Adoption is wide and shallow." | No |

---

## 4. Answers to the must-answer questions

### 4.1 Agent-authored code share — did the curve bend?

**Yes, and it is well-instrumented.** botcommits.dev [1] rebuilt its collector and now reports
Claude Code at **19,804,129 public commits in July 2026** [2], with the fitted models
switching sides: the March-2026 version of the same page fitted an exponential with a 1.22-month
doubling and said the inflection had not been observed; the current page reports the exponential
doubling at **2.62 months**, sigmoid models winning on AIC in **5 of 6** fitting configurations,
a **2026-04 inflection**, and a **22.5M (logistic) to 29.6M (Gompertz) ceiling** [2]. The scale
of the miss is the most persuasive part: the March exponential predicted **98,478,304** commits
for July; the measured number is **19.8M** — a 5x over-prediction in four months [2].

**Corroboration, independent of the tracker:**

- **SemiAnalysis contradicts the bend by projection, not by measurement.** Its February 2026
  piece states "4% of GitHub public commits are being authored by Claude Code right now. At the
  current trajectory, we believe that Claude Code will be 20%+ of all daily commits by the end
  of 2026" [3]. That projection is an extrapolation of the pre-bend exponential. On the
  tracker's own share series the number today is **17.8% of push events / ~6–18% of commits**
  [1][2] — so SemiAnalysis's endpoint is arguably reachable on the loosest denominator and
  clearly not on the tightest. **It has published no update.** Treat "20% by end of 2026" as a
  live disagreement, not a settled figure.
- **Ramp corroborates deceleration on the demand side.** Anthropic's business adoption rose
  **1.1 percentage points month-over-month** to 43.5% in July 2026, and Ramp's lead economist
  titles the letter "Cracks in the AI Thesis", writing that "adoption of OpenAI and to a lesser
  extent, Anthropic, has slowed in recent months" [18]. Different instrument, same direction.
- **Academic work corroborates the *level* and warns the level is too low.** Quispe & Xu
  (arXiv 2605.25438, submitted 2026-05-25) built a GitHub panel of 5,346 developers dated by
  first Claude Code co-authorship across 57 million changed files [6]; botcommits reports that
  their harvest of **7,786,771** Claude co-authored commits for Jan 2025–Jan 2026 matches its
  own series at **7.83M** for the same window [1]. Khosravani & Mockus (arXiv 2606.24429,
  2026-06-23) census 180M+ repositories and find that "bot-account lookup—the signal most
  adoption studies rely on—recovers only 28,154 (3.3%), a 30x relative-recall gap, so
  single-signal prevalence estimates are biased low by at least this factor" [5].

**GitHub's own reporting does not settle it.** Octoverse 2025 is the newest GitHub figure —
"developers created 230+ repositories per minute and pushed 986 million commits last year" [4]
— and it covers Sep 2024–Aug 2025. GitHub has published no monthly commit denominator, which
is exactly why the share must be given as a range [1].

**Honest current share to put on the slide:** *AI-attributed commits are 17.8% of public push
events in July 2026, which is somewhere between ~6% and ~18% of public commits depending on an
unmeasured commits-per-push ratio; Claude Code is the overwhelming majority of that* (19.80M of
20.08M across the six tracked tools) [2].

### 4.2 Claude Code and Anthropic revenue

| Entity | Figure | Date | Source type |
|---|---|---|---|
| Anthropic | **$65bn** run rate | end of July 2026 | Told to investors; Bloomberg first, CNBC confirmed with three sources [9][10] |
| Anthropic | **$11.5bn** preliminary Q2 revenue | Q2 2026 | Same investor update [9] |
| Anthropic | **$47bn** run rate | May 2026 | Anthropic's own Series H post [8] |
| Claude Code | **over $2.5bn** run rate | **12 Feb 2026** | Anthropic's own Series G post [7] |

**The gap, stated plainly:** there is **no September-2026-fresh Claude Code revenue number from
a company statement or top-tier outlet.** The "$8bn by May 2026" figure that dominates search
results appears only in SEO aggregator blogs with no primary citation; I could not trace it to
Anthropic, Bloomberg, CNBC, The Information or the FT, and I am not citing it. If S05 carries a
Claude Code revenue number, it must be **"$2.5bn+, as of February 2026"** with the date spoken.
The supporting company-reported colour is fresher in kind if not in date: "Business
subscriptions to Claude Code have quadrupled since the start of 2026, and enterprise use has
grown to represent over half of all Claude Code revenue" [7].

*Company-reported vs independently verified:* every revenue figure here is **company-reported**.
CNBC's $65bn is company-reported-to-investors and then press-confirmed — the strongest tier
available for a private company. None of it is audited.

### 4.3 Exponential View's State of the AI Economy — all four figures confirmed

The report is dated **June 25, 2026** on its cover [11] and the hosting page still describes it
as "An Exponential View Report · June 2026". **No updated edition exists as of 2026-08-31** —
EV's most recent AI-economy writing (10 August 2026) cites the same "2026 State of the AI
Economy Report" rather than a successor [12]. So the report is **~10 weeks old at talk time**:
usable, but say "as of June".

| Charter's figure | Verdict | Verbatim |
|---|---|---|
| $110bn TTM GenAI revenue | **Confirmed** | "$110bn trailing 12-month revenues – now at a $175bn pace" [11] |
| $175bn run rate | **Confirmed** | same line; and "Generative AI ecosystem revenue has already surpassed $175 billion annualized (after removing double-counting from provider revenues)" [11] |
| Adoption 3x faster than prior IT waves | **Confirmed** | "The sector is growing 3x faster than any IT wave before it." [11] |
| ~$2T CapEx vs revenue barely covering depreciation | **Confirmed, with a correction** | "Hyperscalers & neoclouds have committed to $2 trillion of cumulative CapEx" [11]. But "barely covers" is now too pessimistic: "Q4 2025: Quarterly revenues first exceed CapEx depreciation" and Q1-2026 headroom is **19%/32%** [11]. The right phrasing is *"revenue now clears the annual depreciation charge with thin headroom, and has covered only about half the cumulative bill."* |

Scope caveat to speak once: "Global ex-China · App, model & infrastructure revenue counted ·
Excludes chips, AI ad-uplift, legacy-software features and financing." [11]

### 4.4 The CapEx sustainability tension — best current argument

**The best-argued source that is neither vendor nor permabear is Exponential View itself**, and
specifically its 10 August 2026 piece "Making sense of the AI capex logjam" [12]. It is
independent (no chips, no models, no cloud to sell), it publishes its method, and its chapter
title is deliberately hedged: "The largest buildout in tech is paying back (for now)" [11].

**Two numbers a founder can hold:**

1. **$863 billion of 2026 CapEx guidance from the seven largest builders, ~$550bn of it
   AI-related — 88% more than last year** [12].
2. **Revenue currently clears the depreciation hurdle with 19% headroom for hyperscalers and
   neoclouds, 32% across all GenAI revenue** [11] — i.e. it works today, with about four-fifths
   of the revenue consumed by depreciation alone.

**The strongest counter-argument — and it comes from the same, non-bearish source:** the
depreciation base being measured today is generated by *yesterday's* spend, and the pipeline is
enormous and slowing down on its way into service. "Assets not yet in service now total $315
billion, up from $281 billion one quarter earlier"; "A dollar of capex spent by Meta now waits
some 1.7 years before going live, a year more than in FY2024"; "For every dollar it spends
today, only about a third will reach service within the year" [12]. EV states the consequence
directly: "As committed AI capex enters service, the depreciation base will rise. Revenue
growth, utilization and pricing must continue to compound or headroom will compress again" [11].

**The demand-side counter-counter-argument, for balance:** Ramp's spend data shows a ceiling
forming on willingness to pay — the top-of-market model captured "only 6% of tokens businesses
purchased from Anthropic" one month after launch despite being twice the price of the
competition, which Ramp reads as "a new upper bound for how much businesses are willing to spend
on AI" [18]. If price-per-capability compresses while the depreciation base rises, the headroom
math gets harder.

### 4.5 One production-agent outcome number

**Recommended replacement for the Intercom Fin anchor: Salesforce's own help desk.**

> "As customer zero, we are putting Agentforce to work across our own business. Salesforce's
> help agent has surpassed five million customer conversations with 64% resolved autonomously." [13]

- **Named company:** Salesforce, on `help.salesforce.com`.
- **Measured outcome:** 5,000,000+ customer conversations, 64% resolved autonomously.
- **Primary source:** Salesforce's Q2 FY2027 earnings-call transcript, quarter ended
  2026-07-31, call 2026-08-26 [13] — a public company, on the record, to investors.
- **Why it beats Intercom Fin 76% / $0.99:** the speaker is the **operator**, not the vendor
  selling you the number; the volume is stated (5M conversations, not "average across
  customers"); and it is six weeks old rather than six months.
- **Caveat to speak:** "Salesforce sells Agentforce, so it is still self-reported — but notice
  it is *lower* than the 76% a vendor quotes. That's the number to plan with."
- **Trajectory, if you want two points:** the same desk was at "four million inquiries…
  now double what human agents are handling" one quarter earlier [15], alongside
  Agentforce ARR passing **$1.5 billion, up over 240% year-on-year**, and **7.0 billion
  "Agentic Work Units" delivered to date** [14].

**On the old anchor:** Intercom's 76% is real and primary — "Our average resolution rate across
customers has increased every month and now stands at 76%" across "more than 7,000 teams" — but
it is dated **12 March 2026** and, in that very post, Intercom announced it is moving Fin's
pricing metric **from resolutions to outcomes**, which retires the "$0.99 per resolution"
framing [16]. Do not present $0.99/resolution as current pricing.

### 4.6 Enterprise adoption reality — production vs pilots

**The most credible September-2026 measure is a two-source pair, because no single instrument is
good enough.**

**Survey (stated method, small sample, big companies):** KPMG's US AI Quarterly Pulse, published
2026-06-24. Method, verbatim: the survey "captured perspectives between April 28th and May 25th
from 204 U.S.-based C-suite and business leaders representing organizations with annual revenue
of $1 billion or more" [17]. Findings, verbatim: "While agent deployment this quarter is on par
with last quarter (53% compared to 55%), the percentage of organizations orchestrating multiple
AI agents across workflows doubled from 9% to 18%" [17]. And the sober one: "only 26% report
full, real-time visibility into what their AI systems cost to operate" [17].

Read it as: **~half of billion-dollar US companies say they have deployed at least one agent;
fewer than one in five orchestrate more than one; only a quarter can see what it costs.** The
gap between "53% deployed" and "18% orchestrating" is the pilot-to-production gap, measured
inside one instrument rather than across incompatible surveys.

**Flag when speaking:** fieldwork ended **25 May 2026** — this is an anchor being updated, not a
September number, and n=204 self-reporting executives is a small, senior, self-flattering
sample. A Q3 edition was not published as of 2026-08-31.

**Behavioural cross-check (no self-report at all):** Ramp's AI Index, built on "aggregated and
anonymized card and bill pay spend from more than 70K U.S. businesses on Ramp" [19], puts
**43.5% of US businesses paying Anthropic** and 39.7% paying OpenAI in July 2026, with the
median firm spending **$11.95 per employee** against $7,400 for the top 1% [18]. Paying for AI
is not the same as running agents in production — but it is a floor nobody can inflate in a
survey response, and its shape (wide, shallow, top-heavy) is the honest picture of
"production" today.

**Surveys I deliberately did not use:** several widely-circulated 2026 figures (79% of companies
run AI agents; 78% pilot / 14% production; 67% beyond pilots) trace only to vendor content
marketing or aggregator blogs with no published method or sample. McKinsey's *State of AI*
global survey would be the strongest available instrument but its page could not be fetched
(see §7); it is therefore not cited.

---

## 5. Prior anchors superseded

| Prior anchor (verified 2026-06-10) | Status | Superseded by |
|---|---|---|
| "10% of all public commits, up from 4% in six weeks" | **Superseded — and it was never a measured point** | 17.8% of push events ≈ **6–18% of commits**, July 2026, denominator explicitly unresolved [1][2] |
| Implied exponential, doubling ~1.2 months, no ceiling | **Superseded** | Doubling **2.62 months**; sigmoid beats exponential; inflection **2026-04**; ceiling **22–30M/month** [1][2] |
| SemiAnalysis "4% of public commits, 20%+ by end of 2026" (Feb 2026) | **Stale; projection unretracted and now in tension with the data** | No SemiAnalysis update found; botcommits' bend is the live counter-evidence [1][3] |
| Anthropic $30bn run rate (VentureBeat, Apr 2026) | **Superseded** | **$65bn** at end of July 2026 [9], via $47bn in May [8] |
| Claude Code $2.5bn annualised (VentureBeat citation) | **Confirmed at source, but NOT refreshed** | Traced to Anthropic's own Series G page, 2026-02-12 [7]. No newer primary figure exists. |
| Intercom Fin: 76% resolved at $0.99/resolution | **Partly superseded** | 76% confirmed as of 2026-03-12 but Intercom is retiring resolution-based pricing [16]; recommend Salesforce **5M conversations / 64% autonomous**, 2026-08-26 [13] |
| EV "~$2T CapEx vs revenue that barely covers depreciation" | **Refined** | Quarterly revenue first exceeded depreciation in **Q4 2025**; Q1-2026 headroom **19%/32%**; cumulative still ~half-covered [11] |

---

## 6. Re-check the day before the talk (2026-09-01)

| Tracker / page | URL | What changes | Why it matters |
|---|---|---|---|
| botcommits.dev | https://botcommits.dev/ | Monthly refresh; August 2026 will become a full month | The headline commit count, MoM %, and whether the bend holds. **This is the single most likely number to move.** |
| botcommits data feed | https://botcommits.dev/data.json | `updated`, `headline.claude_last`, `headline.claude_mom_pct`, `headline.share_last_pct` | Machine-readable; grep these four keys and you have the slide |
| Ramp AI Index | https://ramp.com/data/ai-index-august-2026 (September letter lands ~2026-09-09) | Monthly adoption + spend | Demand-side corroboration of the deceleration |
| Anthropic newsroom | https://www.anthropic.com/news | Any Claude Code revenue disclosure | Would replace the six-month-old $2.5bn figure |
| Exponential View | https://www.exponentialview.co/ and https://intelligence.exponentialview.co/ | A second edition of *State of the AI Economy* | Would refresh all of S06 at once |
| KPMG AI Pulse | https://kpmg.com/us/en/media/news/q2-ai-pulse-2026.html | A Q3 2026 edition (expected September) | Would give post-June fieldwork on agents in production |
| GitHub Octoverse | https://github.blog/news-insights/octoverse/ | Octoverse 2026 (historically late October) | The only thing that can turn the 6–18% range into a point |

---

## 7. Gaps and things I could not verify

1. **No fresh Claude Code revenue figure.** Nothing newer than 2026-02-12 from Anthropic or a
   top-tier outlet. The "$8bn, May 2026" number circulating widely could not be traced to any
   primary page and is **not cited anywhere in this report**.
2. **McKinsey's *State of AI* survey could not be fetched.** Both WebFetch (two attempts,
   60s timeouts) and a direct request to
   `https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai` failed.
   It is listed as unverified in `run-result.json` and backs no claim here.
3. **CNBC returns 403 to the standard fetcher** but serves the page to a normal browser
   user-agent. The $65bn quote is real and was read from the live page; a citation gate that
   uses a plain fetcher may need the browser user-agent, or may prefer the TechCrunch or
   Bloomberg URLs listed in `sources.md` [10].
4. **Three sources are PDFs** (the EV report, and both Salesforce transcripts). A
   grep-the-quote gate must run text extraction (`pdftotext -layout`) before matching, and in
   the EV report's two-column layout the multi-line bullets wrap — quotes 5 and 6 in the S06
   table read as one sentence to a human but are split across lines in the raw extraction.
5. **Numbers wrapped in markup.** On ramp.com the percentages sit inside `<span>` tags, so
   "43.5% of U.S. businesses paid…" is contiguous in rendered text but not in raw HTML; the
   same applies to TechCrunch's "$65 billion" (inside an `<a>`). A gate that strips tags before
   matching is fine; one that greps raw HTML is not.
6. **botcommits.dev renders its headline numbers from JavaScript.** The prose quotes in the
   S05 table are in the static HTML and are greppable; the bare figures (19,804,129 etc.) are
   only in `data.json`, which is why the commit count is cited to the JSON endpoint [2].
