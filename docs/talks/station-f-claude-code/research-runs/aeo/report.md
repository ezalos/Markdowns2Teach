# How real is AI-assistant referral traffic in 2026, and what actually moves it?

Research run for **S53 "AEO"** — Station F founders' talk, 2026-09-02.
Completed 2026-09-01. Status: **complete**, with one documented gap (see §6 and §9).

---

## The two numbers that carry the slide

**Headline traffic figure.** AI assistants are a rounding error in raw referral volume and a
steep curve in growth. Semrush measured channel-level traffic across more than 50,000
websites and 17 industries for all of 2025 [4] and found: *"AI traffic grew 66% in 2025 and
outpaced every other channel, but it still makes up less than 0.15% of total visits"* [5]. At
the infrastructure layer one year later, Cloudflare's 2026 bot report puts the same fact from
the other side: *"Google remains the dominant gateway to online discovery, accounting for
approximately 88% of referral traffic"* [1].

**Headline conversion figure.** The visitors who do arrive convert better. Adobe Analytics,
across more than a trillion visits to U.S. retail sites, reports that *"AI-based retail site
visits convert at a rate 60% higher than non-AI traffic"* (July 2026 data) [9], with
AI-referral traffic to those sites up 62% year over year in the same month [10].

**The slide's actual claim, in one line:** *tiny channel, best-converting channel, growing
faster than anything else — which is exactly the profile of a channel worth an automated
weekly agent rather than a headcount.*

---

## 1. The traffic curve

| Measurement | Source type | Period | Finding |
|---|---|---|---|
| Semrush Traffic & Market, 50,000+ sites, 17 industries [4] | Analytics vendor, clickstream panel | Jan–Dec 2025 | AI traffic **+66%**, still **<0.15% of total visits** [5] |
| Cloudflare, network-level [1] | Internet infrastructure | June 2026 | Google still ≈**88% of referral traffic** [1] |
| Similarweb worldwide panel [6] | Analytics vendor | Jun 2025 – May 2026 | Visits *to* the assistants **+70% YoY to 9.5bn/month** [6] |
| Adobe Analytics, >1tn U.S. retail visits [11] | Retail-scale analytics | Q1 2026 vs Q1 2025 | AI-sourced retail traffic **+393%** [11] |
| Adobe Analytics [10] | Retail-scale analytics | July 2026 vs July 2025 | AI-referral retail traffic **+62%** [10] |

Two things to read off this. First, **the growth rate is decelerating as the base grows** —
+393% in Q1 2026 against +62% in July 2026 [11][10], which is what a channel looks like when it
stops being a novelty. Second, **the assistants' own audience is growing much faster than the
traffic they send out**: 9.5 billion monthly visits to the assistants [6] converting into a
sub-1% share of the web's referrals [5][1]. The gap is the product design — assistants answer
in place rather than sending you away.

Cloudflare quantified that gap directly with the crawl-to-refer ratio. In its June 2025
baseline, *"Anthropic's AI platform Claude made nearly 71,000 HTML page requests for every
HTML page referral"* [7]. By June 2026, 52% of all crawler requests Cloudflare sees are for AI
training [2], and *"for every hour spent online searching for information, only 15 minutes is
spent on the open web"* [3].

**Caveat that matters for every ratio above**, and Cloudflare states it themselves: *"As such,
because the referral counts only include traffic from the Web-based tools from these
providers, these calculations may overstate the respective ratios, but it is unclear by how
much"* [8]. Native mobile apps do not send referrers. See §7.

---

## 2. Conversion quality

The primary is Adobe Analytics, on the largest published sample.

- July 2026: *"AI-based retail site visits convert at a rate 60% higher than non-AI traffic"* [9].
- March 2026: *"AI traffic converted 42% better than living, breathing customers in March 2026"* [11] — and, critically, twelve months earlier the sign was reversed: *"In March 2025, AI traffic converted 38% worse than regular people"* [12].
- Sample and method: Adobe's insight is based on analysis of online transactions covering *"over 1 trillion visits to U.S. retail sites"* [11]. It is **U.S. retail e-commerce**, measured in Adobe Analytics on client sites — not a cross-industry benchmark.

The independent corroboration is a single-company B2B SaaS case, and should be labelled as
such: Ahrefs, reporting on its own site, wrote *"That's crazy right? 12.1% of signups from
0.5% of the traffic"* [13] (30-day window, June 2025). That is a ~23x conversion differential,
but it is one company, one product, one high-consideration purchase — a ceiling, not a
benchmark.

**The honest reading:** the direction is consistent across two very different datasets and the
sign flipped inside twelve months [12]. The magnitude (42%, 54%, 60%, 23x) is not stable
enough to quote as a constant. Quote the direction and the flip; quote one magnitude with its
date attached.

---

## 3. What actually works, with evidence

| Practice | Rating | Evidence |
|---|---|---|
| **`llms.txt`** | **Folklore** | Ahrefs checked every domain in its analytics that got traffic in May 2026: *"Of the ~38,000 domains with a valid file, 97% saw no requests for it whatsoever in May"* [14], and *"Zero requests came from AI bots for llms.txt files that don't exist. They never go looking"* [15]. Google's John Mueller: *"FWIW no AI system currently uses llms.txt."* [16]. Google's own docs: *"You don't need to create new machine readable files, AI text files, or markup to appear in these features."* [17] |
| **Schema.org / JSON-LD structured data** | **Folklore for AI citations** (still fine for classic search) | Ahrefs ran a matched difference-in-differences test — *"We tracked 1,885 web pages that added JSON-LD schema between August 2025 and March 2026, matched them against 4,000 control pages"* [20] — and concluded *"Adding schema produced no major uplift in citations on any platform."* [19]. Google states there is no special schema.org structured data needed for AI features [17]. Vendor study; Ahrefs sells AI-visibility tooling. |
| **Being crawlable by the right bot (`OAI-SearchBot`, `PerplexityBot`)** | **Evidence-backed** (vendor-documented gate) | OpenAI: *"OAI-SearchBot is used to surface websites in search results in ChatGPT's search features."* [26] and *"Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links."* [27]. Perplexity documents `PerplexityBot` as *"designed to surface and link websites in search results on Perplexity."* [28]. This is a necessary condition, not a growth lever. |
| **Third-party mentions of your brand across the web** | **Evidence-backed as correlation, not causation** | Ahrefs: *"we've analyzed 75,000 brands to see which search factors are most likely to influence brand mentions in AI Overviews"* [23], finding *"Web mentions (0.664) correlate much more strongly than backlinks (0.218)."* [24]. Correlational only, and the authors say so. Vendor study. |
| **Community and UGC presence (Reddit, YouTube, LinkedIn)** | **Evidence-backed as a citation surface** | Peec AI analysed 30 million cited sources: *"Reddit was the most-cited source across ChatGPT, Google AI Mode, Gemini, Perplexity, and AI Overviews."* [25] Vendor study, existence claim only — it shows where citations land, not that posting there causes citations. |
| **Documentation as a citation/consumption surface** | **Plausible but unmeasured** | Agents do hit docs, but invisibly: a study of *"nine AI coding agents"* and six AI assistant services [40] found agents collapse browsing into one or two requests, *"making traditional engagement metrics - session depth, time-on-page, click path, and bounce rate - unreliable indicators of actual documentation consumption."* [40] No published measurement of docs → citation lift. |
| **Ranking #1 in Google as a proxy for being cited** | **Diverging — no longer a reliable proxy** | Ahrefs: *"This time around, we analyzed 863K keyword SERPs, and a grand total of 4M AI Overview URLs—over double our last analysis."* [22], finding only *"38% of pages cited in AI Overviews also rank in the top 10"* [21] — down from ~76% seven months earlier. |
| **Adding statistics, quotes and citations to your own pages** | **Plausible-but-thinly-measured** | The original Princeton GEO paper reports up to ~40% visibility gains from these edits, but it is a 2023 preprint benchmarked against 2023-era generative engines and predates ChatGPT Search, AI Mode and every 2026 product change. **Not carried in this report's citations** — see §9. |

**The pattern.** Every *on-page technical* lever that has actually been tested under control
came back null [19][14][17]. Every *off-page presence* signal that has been measured came back
strongly correlated [24][25]. Whatever the causal story, the actionable read for a founder is:
this is a "be talked about in the places assistants read" problem, not a "add a file to your
webroot" problem.

---

## 4. How assistants choose what to cite

**What the vendors document is thinner than the market assumes.**

- **Anthropic.** The docs say *"The web search tool gives Claude direct access to real-time web content, allowing it to answer questions with up-to-date information beyond its knowledge cutoff."* [29] and, on mechanism, only *"The API runs the searches and provides Claude with the results."* [30] — the retrieval and ranking behind that sentence is not documented.
- **OpenAI.** Documents three distinct user agents with distinct jobs, and one binary control: opt out of `OAI-SearchBot` and you are not shown in ChatGPT search answers [26][27]. Nothing about ranking.
- **Perplexity.** Documents `PerplexityBot` as the surfacing crawler [28]. Nothing about ranking.
- **Google.** The most explicit, and it is a *negation*: *"There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary."* [18]

So: **no major assistant vendor documents its citation-selection function.** Everything sold as
"AEO methodology" is inference from observed output, not from vendor specification. Say that
on the slide.

**The independent picture** is heavy concentration on a few user-generated-content domains
[25], and a growing divergence from Google's own ranking: cited-in-AI-Overviews and
ranks-top-10-on-Google overlapped 38% in the March 2026 measurement, against ~76% seven months
before [21][22].

---

## 5. The self-preference question

The founder's open question — *does content optimised with one model get disproportionately
recommended by that same model?* — has **no direct published answer**. What exists is the
adjacent and arguably more useful finding.

**Peer-reviewed, and directly on point for recommendation:** a PNAS study tested *"GPT-3.5,
GPT-4 and a selection of recent open-weight models in binary choice scenarios"* [32] choosing
between human-written and LLM-written descriptions of the same items, including consumer
products. The result: *"Our results show a consistent tendency for LLM-based AIs to prefer
LLM-presented options."* [31] Human raters did not share the preference at anything like the
same rate. This is **AI-authored vs. human-authored**, not **model-X-authored vs.
model-Y-authored** — but it is the finding that matters commercially: writing your product page
with an LLM at all plausibly advantages you with LLM recommenders.

**Supporting evidence on same-model favouritism:**
- Self-preference in judging is established: *"One such bias is self-preference, where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality"* [34], with the strength of the bias tracking the model's ability to recognise its own text [34].
- And it extends beyond text quality into brand-level association: across *"72 experiments and ~41,000 queries, we discovered massive self-preferences in eight widely used LLMs"* [33] — models pairing positive attributes with their own companies over competitors [33].

**Verdict for the slide:** *LLMs demonstrably prefer LLM-written content over human-written
content when recommending [31]. Whether Claude specifically prefers Claude-written content over
GPT-written content is not published; the same-model effect is documented for judging [34] and
for brand association [33], not for content recommendation.* Do not overclaim past that line.

---

## 6. The automation pattern

**First-party documentation of scheduled agent runs — fully answered.**

Anthropic ships this as a product feature. *"A routine is a Claude Code automation you
configure once — including a prompt, repo, and connectors — and then run on a schedule, from an
API call, or in response to an event"* [35], and *"Routines run on Claude Code's web
infrastructure, so nothing depends on your laptop being open"* [36]. The cost model is
subscription-bundled, not metered: *"Pro users can run up to 5 routines per day, Max users can
run up to 15 routines per day, and Team and Enterprise users can run up to 25 routines per
day"* [37]. A weekly AEO research loop consumes **1 of ~35 monthly Pro routine-runs** — the
slide's "for roughly nothing" is accurate on the published limits [37].

OpenAI ships the consumer equivalent: ChatGPT can *"Schedule recurring tasks to run in the
background"* [38].

**Documented examples of a weekly AEO research loop, with outputs and costs — NOT FOUND.** No
first-party case study, vendor write-up or independent study documenting a scheduled agent
running answer-engine research on a weekly cadence, with what it produced and what it cost, was
located. The *capability* is first-party documented [35][36][37][38]; the *worked example* is
not. This is the honest state of the evidence and the slide should not imply otherwise.

---

## 7. Attribution: how a small team actually measures this

The measurement problem is real, mechanical, and has a known workaround.

**Why the traffic disappears.** Links opened from assistant mobile apps and links carrying
`rel="noreferrer"` suppress the header analytics depends on: under the `no-referrer` policy,
*"The `Referer` header will be omitted: sent requests do not include any referrer
information."* [39] With no referrer, GA4 files the session under Direct. Cloudflare hits the
same wall at network scale and says so: their referral counts *"only include traffic from the
Web-based tools from these providers"* [8]. The industry knows it is blind here — Semrush found
*"45% of marketing leaders cannot accurately measure their brand visibility within
AI-generated answers"* [41].

**The practical method, in order of reliability:**

1. **Server logs, not the JS tag.** Logs capture user-agent and IP on every request regardless of referrer or consent banner. This is the only layer that sees agent fetches at all — and note that agents collapse browsing into one or two requests [40], so classic engagement metrics are meaningless for them; count requests, not sessions.
2. **UTM the links you control.** ChatGPT Search appends `utm_source=chatgpt.com` to outbound citation links, so a GA4 channel group matching `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com` captures the desktop-web slice. This is observed behaviour, not a vendor-documented guarantee — treat it as a floor.
3. **Treat the Direct delta as the signal.** Since mobile-app referrals land in Direct, the honest metric for a small team is not "AI referral sessions" but the *ratio* of measured AI referrals to a Direct baseline, tracked over time. Movement is interpretable; absolute levels are not.
4. **Ask.** A one-field "how did you hear about us?" on signup is, for a small team, the highest-signal instrument available, and it is the only one that survives referrer stripping entirely.

**Rule of thumb to say out loud:** any AI-referral number from GA4 is a **lower bound**. The
correct posture is directional, not absolute.

---

## 8. Placing the founder's $1M projection

The tweet contributes two things, and they should be labelled differently on the slide.

**The anecdote (usable).** ~300 customers referred by a chat assistant is a concrete, plausible
data point, and it sits comfortably inside the measured picture: a channel that is <0.15% of
visits [5] but converts 60% better than baseline [9] is exactly the kind of channel where a
small absolute visitor count produces a visible customer count. Nothing about the anecdote
contradicts the infrastructure data. Show it as *one founder's reported experience*.

**The projection (not usable as evidence).** "$1M of revenue next year from AEO" is a
self-reported forward projection by a party with an interest in the claim. It is not a
measurement, it has no stated method, and no published dataset supports extrapolating any
company's AEO revenue a year out. Every measured series here either decelerates (+393% Q1 2026
→ +62% July 2026 [11][10]) or has already reversed sign once inside twelve months (−38% → +42%
conversion [12][11]). **Put the projection on the slide as a labelled anecdote in a founder's
own words, on top of the Adobe conversion figure [9] and the Semrush share figure [5], and let
the measured numbers carry the argument.** The projection is what makes the room lean in; the
measured data is what makes the advice defensible.

**What the slide can honestly assert:**
- AI referrals are still under a fifth of a percent of web traffic [5], while Google remains ~88% of referrals [1].
- The visitors who do arrive convert materially better than non-AI traffic, on a trillion-visit retail sample [9].
- The technical AEO tactics people sell are measurably null [19][14]; the off-page presence signals are the ones that correlate [24][25].
- Being cited by an assistant has come loose from ranking on Google [21].
- A weekly agent to watch this costs one routine-run out of a bundled daily allowance [37].

---

## 9. Conflicts, gaps and things to not say

**Conflicting numbers, stated openly.** Adobe's conversion premium is reported as 42% (March
2026) [11], 54% (May 2026, per Semrush citing Adobe), and 60% (July 2026) [9]. These are
different months of the same series, not contradictions — but quoting "AI converts X% better"
without a date is wrong. Use 60%, July 2026 [9].

Crawl-to-refer ratios vary wildly by source and window — Cloudflare's own June 2025 figure for
Anthropic was ~71,000:1 [7], while third-party readings of Cloudflare Radar in 2026 report
figures an order of magnitude lower. The ratios are directionally robust and numerically
unstable; do not put a specific ratio on a slide.

**Sources I could not fetch, and therefore did not cite.** Adobe's own pages
(`business.adobe.com` blog posts and the Q2/Q3 2026 ADI PDFs) timed out repeatedly from this
network; the Adobe figures here come from TechCrunch and Digital Commerce 360 quoting Adobe
directly [11][12][9][10]. `dl.acm.org` (the ACM Web Science 2026 paper *Self-Promotion in LLM
Recommendations*, which reportedly finds providers ranking their own products ~0.2 positions
above benchmark-justified) returned 403 — **that finding is deliberately absent from §5**.
`pnas.org` returned 403; the PubMed Central mirror of the same article was used [31][32].
Cloudflare Radar's live AI Insights dashboard is not fetchable, so 2026 per-platform
crawl-to-refer figures rest on Cloudflare's blog posts rather than the live dashboard.

**The one gap.** No documented worked example of a weekly scheduled AEO agent loop — outputs
and costs — exists in the public record (§6). Say "here is the pattern and here is what it
costs to run" [35][37], not "here is what it returned for someone else."
