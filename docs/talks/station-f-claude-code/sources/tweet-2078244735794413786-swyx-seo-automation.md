<!-- ABOUTME: Full capture of swyx's "SEO/AEO automation" tweet + self-thread (2026-07-17), Louis's label "SEO automation". -->
<!-- ABOUTME: Source material for the Station F / Incubateur 42 talk (2026-09-02) on Claude Code & agentic best practices. -->

# Tweet — swyx on weekly SEO/AEO agent automations ("SEO automation")

## Header

- **URL**: https://x.com/swyx/status/2078244735794413786
- **Author**: swyx (@swyx) — 186.9K followers; affiliations: @smol_ai, @dxtipshq, @cognition (Devin), @aidotengineer, @latentspacepod
- **Date**: 2026-07-17 22:25:31 UTC (head tweet)
- **Engagement** (head, as of 2026-08-31): 2,148 likes · 2,855 bookmarks · 105 replies · 48 RTs · 17 quotes · 197,689 views
- **Fetch method**: fxtwitter API (head + each thread tweet individually); thread structure discovered via Tavily extract of the x.com page (threadreaderapp had no unroll cached)
- **Thread**: YES — head + 2 self-replies, one of which quote-tweets an earlier swyx tweet with a data screenshot. All collected below.

## Full text (verbatim, thread numbered)

**1/ Head — 2026-07-17 22:25 UTC** (https://x.com/swyx/status/2078244735794413786)

> btw if you havent set your {codex | claude | gemini | devin} automations to autoresearch how to improve your seo/aeo every week you are really truly missing out on free, should-be-commoditizing-but-weirdly-untapped alpha

**2/ Self-reply — 2026-07-18 01:41 UTC** (https://x.com/swyx/status/2078293998398263587) — 26 likes, 17.2K views

> alpha only gone when we all stop asking these level of questions and start discussion about on-policy autoaeo (does claude optimizing your aeo disproportionately work on claude?) vs generalizable aeo

This reply quote-tweets a question from @thomasmustier (2026-07-17, https://x.com/thomasmustier/status/2078253254652108806):

> @swyx what's it hillclimbing? or do you mean iterate each week and then the experiment runs over that week

**3/ Self-reply — 2026-07-18 20:45 UTC** (https://x.com/swyx/status/2078581967768166591) — 12 likes, 8K views

> btw at current rate i think AEO will be fully responsible for $1m in my revenue next yr

This reply quote-tweets swyx's own earlier tweet (2026-06-28 19:48 UTC, https://x.com/swyx/status/2071319972882911687 — 103 likes, 28.6K views):

> in case anyone was wondering, 300 or so people were referred by chatgpt this year

Context of that quoted tweet: it sits inside a swyx thread about **AI Engineer World's Fair 2026 selling out** (parent: https://x.com/swyx/status/2071259119047315827, "any guesses what the AIEWF Stress Curve* looked like for this year lol", quoting @aiDotEngineer's sell-out announcement). So the "300 people referred by chatgpt" = ~300 AIEWF ticket buyers/visitors whose UTM source was chatgpt.com — the revenue behind the "$1m from AEO next year" projection is AI Engineer conference ticket sales.

Notable third-party reply in-thread: @bensenescu plugging https://github.com/every-app/open-seo ("Open source alternative to Semrush and Ahrefs" — grounds the SEO agent with real data).

## Media described

- `videos/tweet-2071319972882911687-swyx-chatgpt-referrals.png` (320x836 PNG, from the quoted Jun 28 tweet): a Google Sheets screenshot showing a "UTM Source" column filtered/sorted — every visible row reads **chatgpt.com** (~20 rows visible of the claimed ~300), next to a truncated "UTM Medium" column; Google Sheets "Summarize this data" AI banner at top. It is raw analytics-export evidence of ChatGPT-referral traffic to the AI Engineer ticketing funnel.
- Head tweet and the two self-replies have no media of their own.

## Linked content summaries

- No external links in the head tweet. The only substantive external link in the conversation is the third-party open-seo GitHub repo (open-source Semrush/Ahrefs alternative to feed SEO agents real data) — relevant as tooling, not part of swyx's claim.

## Relevance to the talk

- **Automation of R&D / recurring agent jobs**: the concrete pattern — a scheduled weekly agent automation (Codex/Claude/Gemini/Devin all have "automations"/scheduled-task features) that autoresearches how to improve your SEO/AEO. Maps directly to Claude Code scheduled routines / `/loop`-style recurring agents. Cheap, unattended, compounding.
- **Economic opportunity for founders**: swyx frames it as "free, should-be-commoditizing-but-weirdly-untapped alpha" — i.e., a window where early adopters win before it commoditizes. His own numbers: ~300 ChatGPT-referred customers in H1 2026; projects **$1M of his (conference) revenue attributable to AEO next year**. AEO (Answer Engine Optimization = being cited/recommended by ChatGPT/Claude/Gemini answers) as the new SEO — very actionable for startup founders in the audience.
- **Evals / on-policy subtlety** (reply 2 is the intellectually interesting bit): "on-policy autoaeo" — does having Claude optimize your AEO disproportionately improve how *Claude* ranks you, vs generalizable AEO across all answer engines? A sharp framing of optimizer/judge coupling — same family of problems as LLM-as-judge bias. Good discussion hook.

## Freshness & sourcing gaps

- Tweet is 2026-07-17 — fresh enough for a 2026-09-02 talk.
- The **$1M/yr AEO revenue** figure is a self-reported, forward-looking anecdote — citable only *as swyx's claim* (link the tweet), never as a market fact.
- The ~300 ChatGPT referrals: evidenced only by a partial spreadsheet screenshot; not independently verifiable.
- To put "AEO is a real channel" on a slide with a primary source, deep-research would need: Similarweb/Cloudflare Radar/Adobe Analytics data on AI-assistant referral traffic growth in 2025–2026 (Adobe published ChatGPT-referral retail-traffic growth figures; Cloudflare publishes AI crawler/referral stats), and/or a named company's disclosed AI-referral revenue. Also verify each vendor's "automations" feature by name (ChatGPT/Codex tasks, Claude Code scheduled routines, Gemini scheduled actions, Devin playbooks) against product docs before naming them on a slide.
