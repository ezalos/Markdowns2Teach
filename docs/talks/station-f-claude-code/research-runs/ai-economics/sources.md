# Sources

All pages fetched and read on **2026-08-31**. Every entry below was retrieved successfully and
the quoted string was located in the fetched page (or, for PDFs, in `pdftotext -layout` output).
Where the raw HTML splits a figure across tags, that is noted — the quote is verbatim in the
rendered text.

---

**[1]** [botcommits.dev — AI-Attributed Commits on GitHub: The Exponential Bent](https://botcommits.dev/)
· Authority: botcommits.dev (independent open-source measurement project; code, queries and raw
Search-API calls published at github.com/edgardomunoznajar/github_explosion)
· Accessed 2026-08-31 · Page data updated 2026-08-18, series through July 2026.

> "Growth above +50%/month through March 2026; +14–26%/month since April. Search-API months carry ±10–15% measurement noise, so single-month bars are indicative, the level shift is not."

> "Read the share as a range — ~6% of commits at 3:1, ~18% at 1:1 — until GitHub publishes a monthly commit denominator."

> "GitHub's Octoverse 2025 reports 986M commits for 2025 against ~1.0B push events in GH Archive (≈1:1), while the payload size field averages 3.8 (over-counting merges) and a March-2026 SemiAnalysis estimate that Claude Code was 4.5% of public commits implies ≈3 commits per push."

> "Reading the sensitivity table: linear-space fits (weighted toward the high-volume months, which is what a ceiling question needs) agree on an April 2026 inflection and a 22–30M ceiling regardless of start month."

> "Quispe (Caltech, 2026) harvested 7,786,771 Claude co-authored commits for Jan 2025–Jan 2026 from GitHub's public API; this page's series sums to 7.83M over the same window."

> "Khosravani & Mockus (2026) find single-channel detection undercounts Claude Code by ~30× at the project level. Everything on this page is a lower bound with a stated instrument, which is more than the \"275 million AI commits a week\" figures circulating without one."

*Note: the headline numerals on this page are injected by JavaScript at render time; the prose
quoted above is in the static HTML and is greppable. For the bare figures, cite [2].*

---

**[2]** [botcommits.dev machine-readable data feed](https://botcommits.dev/data.json)
· Authority: botcommits.dev · Accessed 2026-08-31 · `"updated": "2026-08-18"`,
`"last_full_month": "2026-07"`.

> `"claude_last": 19804129,`
> `"claude_mom_pct": 14,`
> `"total6_last": 20083498,`
> `"total6_mom_pct": 13,`
> `"share_last_pct": 17.8,`
> `"doubling_now": 2.62,`
> `"doubling_march": 1.22,`
> `"march_exp_pred_last_full": 98478304,`
> `"logistic_ceiling": 22495559,`
> `"gompertz_ceiling": 29638725,`
> `"inflection_month": "2026-04",`

Also, from the model-comparison block: `"best": {"claude": "gompertz", "total6": "gompertz"}`
and, in the sensitivity block, `"sigmoid_wins": 5, "configs": 6`.

---

**[3]** [Claude Code is the Inflection Point](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point)
· Authority: SemiAnalysis (Dylan Patel et al.) · Published 2026-02-05 · Accessed 2026-08-31.

> "4% of GitHub public commits are being authored by Claude Code right now. At the current trajectory, we believe that Claude Code will be 20%+ of all daily commits by the end of 2026. While you blinked, AI consumed all of software development."

*Measured before 2026-06-01 — an anchor being updated, not a current figure. No SemiAnalysis
update to this projection was found as of 2026-08-31.*

---

**[4]** [What 986 million code pushes say about the developer workflow in 2025](https://github.blog/news-insights/octoverse/what-986-million-code-pushes-say-about-the-developer-workflow-in-2025/)
· Authority: The GitHub Blog (Octoverse) · Data window Sep 2024 – Aug 2025 · Accessed 2026-08-31.

> "You might have seen the Octoverse 2025 report, but in case you haven't, the stats are pretty wild: developers created 230+ repositories per minute and pushed 986 million commits last year."

---

**[5]** [Detecting AI Coding Agents in Open Source: A Validated Multi-Method Census of 180 Million Repositories](https://arxiv.org/abs/2606.24429)
· Authority: Arsham Khosravani & Audris Mockus, arXiv:2606.24429 · Submitted 2026-06-23 ·
Accessed 2026-08-31.

> "No single method captures more than a fraction of activity: multi-method detection identifies 850,157 Claude Code commits in one snapshot, of which bot-account lookup_the signal most adoption studies rely on_recovers only 28,154 (3.3%), a 30x relative-recall gap, so single-signal prevalence estimates are biased low by at least this factor."

> "Across snapshots from December 2024 to April 2026, commit-attributed agents generate over 320,000 commits per month; Claude Code leads (886,122 commits across 17,295 projects) and dominates silent, configuration-file-only adoption (21,078 projects)."

*The underscores around the em-dashed clause are an arXiv abstract-rendering artefact; they
appear exactly as shown on the abstract page.*

---

**[6]** [Agentic Delegation and the Language Frontier of Software Developers: A Model and Evidence from Claude Code on GitHub](https://arxiv.org/abs/2605.25438)
· Authority: Alexander Quispe & Kevin Xu, arXiv:2605.25438 · Submitted 2026-05-25 (v1),
revised 2026-07-07 (v2) · Accessed 2026-08-31.

> "We test this prediction in a monthly GitHub panel of 5,346 developers, dating adoption by first Claude Code co-authorship and constructing commit-level language outcomes from 57 million changed files."

*The 7,786,771-commit harvest cited in the report body is reported by botcommits.dev [1] as a
cross-check against this work; that figure is in the paper body, not the abstract page.*

---

**[7]** [Anthropic raises $30 billion in Series G funding at $380 billion post-money valuation](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)
· Authority: Anthropic (company newsroom) · Published 2026-02-12 · Accessed 2026-08-31.

> "Today, Claude Code's run-rate revenue has grown to over $2.5 billion; this figure has more than doubled since the beginning of 2026. The number of weekly active Claude Code users has also doubled since January 1."

> "estimated that 4% of all GitHub public commits worldwide were being authored by Claude Code—double the percentage from just one month prior."

> "Business subscriptions to Claude Code have quadrupled since the start of 2026, and enterprise use has grown to represent over half of all Claude Code revenue."

> "Today, our run-rate revenue is $14 billion, with this figure growing over 10x annually in each of those past three years."

*In the raw HTML the word "analysis" in the second quote is an `<a>` link to [3]; the quote
above begins after that tag and is contiguous.*

---

**[8]** [Anthropic raises $65B in Series H funding at $965B post-money valuation](https://www.anthropic.com/news/series-h)
· Authority: Anthropic (company newsroom) · Published 2026-05-28 · Accessed 2026-08-31.

> "Since our Series G in February, adoption has continued to grow across global enterprise customers, and our run-rate revenue crossed $47 billion earlier this month."

---

**[9]** [Anthropic tells investors annualized revenue run rate climbed to $65 billion in July](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html)
· Authority: CNBC · Published 2026-08-17, updated 2026-08-18 · Accessed 2026-08-31.

> "Anthropic told investors over the weekend that its annualized revenue run rate hit $65 billion at the end of July, CNBC confirmed."

> "Anthropic also shared a preliminary revenue figure of $11.5 billion for the second quarter, a 14-fold jump from a year ago, a source said. The company declined to comment. In May, Anthropic said its run rate topped $47 billion, compared to the roughly $10 billion in revenue the company generated for all of 2025."

*CNBC returns HTTP 403 to a default fetcher user-agent and 200 to a browser user-agent. The page
was retrieved with a browser user-agent and the quotes read from the returned HTML.*

---

**[10]** [Anthropic's annualized revenue surges to $65B](https://techcrunch.com/2026/08/17/anthropics-annualized-revenue-surges-to-65b/)
· Authority: TechCrunch · Published 2026-08-17 · Accessed 2026-08-31.

> "Anthropic's annualized revenue run rate — a projection of a full year's revenue based on a recent, shorter period — surpassed $65 billion at the end of July, Bloomberg reported on Monday, up from $47 billion in May, and just $9 billion at the end of last year."

*In TechCrunch's raw HTML both "$65 billion" and "$47 billion" sit inside `<a>` tags, so this
sentence is contiguous in the rendered text but not in the raw markup. Bloomberg's original is
at https://www.bloomberg.com/news/articles/2026-08-17/anthropic-revenue-run-rate-surpasses-65-billion-ahead-of-ipo
(paywalled; not fetched, and therefore not cited).*

---

**[11]** [The State of the AI Economy (PDF)](https://intelligence.exponentialview.co/assets/ev-state-of-ai-economy-2026.pdf)
· Authority: Exponential View (Azeem Azhar, William Gildea, Hannah Petrovic PhD, Nathan Warren,
Marija Gavrilov) · Cover date **June 25, 2026** · Accessed 2026-08-31 · 7.5 MB, text extracted
with `pdftotext -layout`.

> "$110bn trailing 12-month revenues – now at a $175bn pace" *(p.7 chart title)*

> "Generative AI ecosystem revenue has already surpassed $175 billion annualized (after removing double-counting from provider revenues)." *(p.4)*

> "The sector is growing 3x faster than any IT wave before it." *(p.6)*

> "AI is scaling three times faster than any IT wave" *(p.9 slide title)*

> "Hyperscalers & neoclouds have committed to $2 trillion of cumulative CapEx to 2026, putting pressure on growing revenues to pay back, especially as more is funded by external capital." *(p.27)*

> "Hyperscaler and neocloud CapEx reaches $2T cumulatively through 2026E" *(p.28 chart title)*

> "The 2026E depreciation charge approaches $111 billion" *(p.32 chart title)*

> "Revenues cover the ongoing expense, not yet the cumulative bill" *(p.33 slide title)*

> "Q4 2025: Quarterly revenues first exceed CapEx depreciation" *(p.33/34 chart annotation)*

> "AI infra revenue now just clears today's depreciation hurdle" *(p.34 slide title)*

> "GenAI revenues now cover the quarterly depreciation of AI infrastructure. Q1 26 headroom reached 19% for hyperscaler/neocloud revenues and 32% across all GenAI revenues." *(p.34 bullet)*

> "Coverage remains thin. Depreciation absorbs roughly 81% of hyperscaler/neocloud GenAI revenue and 68% of total GenAI revenue before additional costs." *(p.34 bullet)*

> "The next test is incremental coverage. As committed AI capex enters service, the depreciation base will rise. Revenue growth, utilization and pricing must continue to compound or headroom will compress again." *(p.34 bullet)*

> "Scope: Global ex-China · App, model & infrastructure revenue counted · Excludes chips, AI ad-uplift, legacy-software features and financing." *(p.3)*

*The p.34 bullets are laid out in a right-hand column and wrap across lines in the raw text
extraction; they read as single sentences to a human. The report's landing page,
https://intelligence.exponentialview.co/, describes it as "An Exponential View Report · June
2026" and carries no later edition as of 2026-08-31.*

---

**[12]** [Making sense of the AI capex logjam](https://www.exponentialview.co/p/ai-capex-deployment-gap)
· Authority: Exponential View · Published **2026-08-10** · Accessed 2026-08-31.

> "Based on current guidance, the seven largest AI-infrastructure builders expect capital expenditure of $863 billion in 2026 – 88% more than last year."

> "We estimate that roughly two-thirds, some $550 billion, will be AI-related."

> "Across the four hyperscalers that disclose this balance, assets not yet in service now total $315 billion, up from $281 billion one quarter earlier."

> "A dollar of capex spent by Meta now waits some 1.7 years before going live, a year more than in FY2024."

> "For every dollar it spends today, only about a third will reach service within the year."

*Superscript footnote markers appear inline in the raw HTML between "balance" and the comma in
the third quote.*

---

**[13]** [Salesforce, Inc. Q2 FY27 Earnings Conference Call transcript (PDF)](https://s205.q4cdn.com/626266368/files/doc_financials/2027/q2/Salesforce-Q2-FY27-Earnings-Transcript.pdf)
· Authority: Salesforce investor relations (q4cdn) · Quarter ended 2026-07-31; call held
2026-08-26 · Accessed 2026-08-31 · 8-page PDF, text extracted with `pdftotext -layout`.

> "As customer zero, we are putting Agentforce to work across our own business. Salesforce's help agent has surpassed five million customer conversations with 64% resolved autonomously. Slackbot is driving 8.1 million hours of annualized productivity gains for our employees."

*Line-wrapped in the PDF between "help agent" and "has surpassed".*

---

**[14]** [Salesforce Delivers Record Second Quarter Fiscal 2027 Results](https://www.salesforce.com/news/press-releases/2026/08/26/fy27-q2-earnings/)
· Authority: Salesforce (company press release) · Published 2026-08-26 · Accessed 2026-08-31.

> "Agentforce and Data 360 annual recurring revenue ("ARR") reached nearly $3.9 billion, up over 210% Y/Y Agentforce ARR exceeded $1.5 billion, up over 240% Y/Y."

> "7.0 billion Agentic Work Units ("AWUs") delivered to date across Agentforce and Slack, with 3.2 billion in Q2, growing 97% quarter-over-quarter ("Q/Q")"

*Curly quotation marks in the original; bullet items run together in the extracted text.*

---

**[15]** [Salesforce, Inc. Q1 FY27 Earnings Conference Call transcript (PDF)](https://s205.q4cdn.com/626266368/files/doc_financials/2027/q1/Salesforce-Q1-FY27-Earnings-Transcript.pdf)
· Authority: Salesforce investor relations (q4cdn) · Quarter ended 2026-04-30; call held
2026-05-27 · Accessed 2026-08-31 · text extracted with `pdftotext -layout`.

> "And since we deployed Agentforce on help.salesforce.com and on 1-800-NO-SOFTWARE, well, only 15 months ago, it's autonomously handled now four million inquiries. It's now double what human agents are handling."

> "In Q1 alone, Agentforce Sales worked 220,000 leads autonomously, generating $42 million in pipeline."

*Measured before 2026-06-01 — trajectory context only; superseded by [13].*

---

**[16]** [From resolutions to outcomes: Evolving how Fin delivers value](https://www.intercom.com/blog/from-resolutions-to-outcomes-evolving-how-fin-delivers-value/)
· Authority: Intercom (company blog, Darragh Curran) · Published **2026-03-12** ·
Accessed 2026-08-31.

> "Today, more than 7,000 teams use Fin. Our average resolution rate across customers has increased every month and now stands at 76%, even as Fin increasingly handles more complex queries."

> "That's why we're evolving Fin's pricing metric from resolutions to outcomes."

> "An outcome represents when Fin successfully completes the action it was configured to perform, as part of a conversation."

*Vendor-reported, and measured before 2026-06-01 — an anchor being updated.*

---

**[17]** [AI Investment and Agent Deployment Hold Steady Amid Growing Focus on Pragmatism](https://kpmg.com/us/en/media/news/q2-ai-pulse-2026.html)
· Authority: KPMG US (AI Quarterly Pulse Survey, Q2 2026) · Published **2026-06-24**;
fieldwork 2026-04-28 to 2026-05-25 · Accessed 2026-08-31.

> "captured perspectives between April 28th and May 25th from 204 U.S.-based C-suite and business leaders representing organizations with annual revenue of $1 billion or more."

> "While agent deployment this quarter is on par with last quarter (53% compared to 55%), the percentage of organizations orchestrating multiple AI agents across workflows doubled from 9% to 18%, pointing to a shift toward more coordinated, enterprise-level use to connect workflows across teams, systems and decisions."

> "While 66% of organizations have monitoring dashboards and 61% have approval processes, only 26% report full, real-time visibility into AI operating costs."

*Fieldwork ended before 2026-06-01 — flagged in the report as an anchor being updated. No Q3
2026 edition existed as of 2026-08-31.*

---

**[18]** [August 2026 Ramp AI Index: Cracks in the AI thesis](https://ramp.com/data/ai-index-august-2026)
· Authority: Ramp Economics Lab (Ara Kharazian, Lead Economist) · Published **2026-08-12**,
July 2026 data · Accessed 2026-08-31.

> "43.5% of U.S. businesses paid for subscriptions or tokens from Anthropic, up 1.1 percentage points month-over-month."

> "OpenAI underperformed overall AI adoption, rising only 0.23 percentage points to 39.7% of businesses."

> "But adoption of OpenAI and to a lesser extent, Anthropic, has slowed in recent months."

> "Over the last month, Fable 5 has made up only 6% of tokens businesses purchased from Anthropic, and despite being their most expensive model by far, 11.4% of dollars spent on Anthropic models."

> "So with Fable 5, we've found a new upper bound for how much businesses are willing to spend on AI."

> "In July, the top 1% of businesses spent a median $7,400 per employee on AI. The top 10% spent $650. The median firm spent $11.95 per employee."

*In the raw HTML each numeral sits inside a `<span class="font-bold">`; the quotes are verbatim
in the rendered text.*

---

**[19]** [Ramp AI Index — June 2026 update](https://ramp.com/data/ai-index-june-2026)
· Authority: Ramp Economics Lab · Published June 2026 · Accessed 2026-08-31.
Cited only for the method statement.

> "Our research uses aggregated and anonymized card and bill pay spend from more than 70K U.S. businesses on Ramp."

> "Anthropic rose 2.5 percentage points to 41%, remaining the leader in business adoption. OpenAI was essentially flat, declining 0.1 percentage points to 39.5%"

---

**[20]** [Anthropic Economic Index report: Cadences](https://www.anthropic.com/research/economic-index-june-2026-report)
· Authority: Anthropic (Economic Index research) · Published **2026-06-26** · Accessed 2026-08-31.
Cited only as colour on how agentic sessions differ from chat.

> "One year ago, most Claude usage took the form of a conversation between a user and an assistant. With the rapid growth of Claude Code and Cowork, Claude sessions now increasingly consist of long-running agentic tasks."

> "Claude Code sessions run on the most capable models far more often (54% are served by Opus, against 10% of chat and Cowork conversations)."
