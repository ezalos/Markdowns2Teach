<!-- ABOUTME: The no-source-left-behind ledger for the Station F talk — every inherited and new source, and where it lands. -->
<!-- ABOUTME: A source may only leave this deck with a written reason on its row. Checked before every build and before ship. -->

# Source ledger — Station F talk, 2026-09-02

**The rule**: a slide may move, merge, split or retire. **Its sources may not silently
disappear.** Every source below has a destination slide key (from `roadmap-proposal.md`)
or an explicit written reason for retirement. Rows with `??` are unresolved and block the
build.

**How to use it**: when you move content between slides, update the destination column in
the same edit. Before shipping, every row must have a destination or a reason, and every
URL in the deck must appear in `slides/station-f-claude-code/sources.yml`.

## A. Inherited from `slides/heuritech-agents/sources.yml` (23 entries)

The heuritech registry is the parent. Every entry is accounted for.

| # | Registry id | Authority | Heuritech slides | → Destination | Note |
|---|-------------|-----------|------------------|---------------|------|
| 1 | `metr-time-horizon-1-1` | METR | 6, 23 | **S07** | Re-purposed: METR is now the *retired* indicator on the benchmark-treadmill slide. Source kept, claim inverted — pending `frontier-evaluations` run. |
| 2 | `metr-long-tasks-paper` | arXiv 2503.14499 | 6 | **S07** | Same. The paper anchors "what the curve measured" before the treadmill argument. |
| 3 | `epoch-inference-price-trends` | Epoch AI | 7 | **S09** | Unchanged claim (9×-900×/yr). Re-verify the figure is current. |
| 4 | `semianalysis-claude-code-inflection` | SemiAnalysis | 5 | **S05** | Refresh number via `ai-economics-refresh`. |
| 5 | `kinlan-github-commits` | Paul Kinlan | 5 | **S05** | Same. |
| 6 | `botcommits-tracker` | botcommits.dev | 5 | **S05** | **QUOTE DEAD (2026-08-31)** — the page injects numbers client-side, so no figure is greppable. Re-registered as `botcommits-the-bend` with a static prose quote. **The claim also inverted**: the curve is now a sigmoid. See `sources/botcommits-2026-08-the-bend.md`. |
| 7 | `venturebeat-agent-acceleration` | VentureBeat | 5 | **S05** | Refresh; may be superseded by a newer revenue figure. |
| 8 | `fin-benchmarks` | Intercom Fin | 5 | **S05** | Vendor-reported — caveat travels with it. |
| 9 | `raschka-coding-agent` | Sebastian Raschka | 8, 19 | **S14 + S23** | Two claims, two destinations (harness decomposition; subagents). |
| 10 | `anthropic-advanced-tool-use` | Anthropic | 18 | **S22** | Restored slide (v1 had cut it). |
| 11 | `claude-getting-started-with-loops` | Anthropic | 21, 23 | **S37 + S39** | — |
| 12 | `react-paper` | arXiv 2210.03629 | 10 | **S13** | — |
| 13 | `anthropic-agent-skills` | Anthropic | 17 | **S21** | Pairs with the new WikiSkill evidence on S52. |
| 14 | `claudefast-subagent-patterns` | claudefa.st | 19 | **S23 + S31** | Also feeds the new multi-agent evidence slide. |
| 15 | `posthog-bullish-on-loops` | PostHog (Ian Vanagas) | 21-26 | **S37-S43** | Secondary synthesis — dual-cite with the Anthropic workshop where they overlap. |
| 16 | `anthropic-agents-run-for-hours` | Anthropic (Prabaker & Wilson) | 21, 22 | **S37 + S38** | The primary behind most of PostHog. Prefer it. |
| 17 | `obra-superpowers` | GitHub | 17 | **S21** | — |
| 18 | `mattpocock-skills` | GitHub | 17 | **S21 + S26** | **QUOTE DEAD (2026-08-31)** — the repo description changed from "Straight from my .claude directory" to **".agents directory"** (a signal in itself: the AGENTS.md convention). New quote needed. Stars **242,767** on 2026-08-31, last push 2026-08-24. Doubly load-bearing: the Grill Me skill lives here. |
| 19 | `trq-make-me-understand` | X (@trq212) | 17 | **S50** | — |
| 20 | `rlaif-vlm-deck` | own deck (self-published) | 17 | **S50** | `verify: link-only` (auth-gated own deployment) — carry the reason across. |
| 21 | `braintrust-eval-maturity` | Braintrust (Hetzel) | 19, 20, 21 | **S47 + S48** | — |
| 22 | `meta-production-evals` | Meta MSL (Gupta) | 19 | **S47** | — |
| 23 | `hamel-evals` | Hamel Husain | 20 | **S48 + A03** | — |

**Retired from the heuritech deck: none.** Every parent source has a destination.

## B. Sources referenced in `heuritech.md` prose but NOT in its registry

These were text-only mentions in the parent deck. Under this repo's non-negotiable they
must become real registry entries with exact URLs and verbatim quotes, or be dropped.

**RESOLVED 2026-08-31** — all 12 chased to a live exact URL with a grep-verified verbatim
quote; ready-to-paste YAML in `sources/resolved-inherited-links.md`. **Four of them change
what the deck may say** and block the build until the slide text changes with them.

| Mention | → Destination | Status |
|---------|---------------|--------|
| `agentskills.io` | S21 | **REGISTER** — not thin marketing: it is the official Agent Skills spec site, and a *better* source than the Anthropic post for "one folder, one markdown file". Register both; they carry different halves. |
| `snyk.io` | S21 | **REGISTER** — `skill-md-shell-access` article: *"treat third-party skills as trusted code. Read them before enabling."* |
| `llm-stats.com/frontiercode` | S15 | **BLOCKER.** The URL is a hard 404 (real path `/benchmarks/frontiercode`) **and the claim is false**: on 2026-08-31 Grok 4.6 leads at 0.613, Opus 5 0.534, **Fable 5 third at 0.463** — and Cognition **deprecated the Diamond subset** in FrontierCode 1.1 (2026-07-07), so the deck names a benchmark that no longer exists. llm-stats flags it `0 verified / 4 self-reported`. **S15 must be rewritten.** |
| `docs.claude.com` ×2 (CLAUDE.md; permissions) | S19 + S18 | **REGISTER at `code.claude.com`** — `docs.claude.com` is in the linter's `REDIRECT_HOSTS` and is rejected offline. Confirmed two genuinely different pages; `/iam` is now "Authentication" and permissions moved to its own page, so the parent deck pointed at the wrong document. |
| `anthropic.com` (agent definition) | S12 | **REGISTER with a caveat** — the deck's five-fragment definition is **Louis's paraphrase, not an Anthropic quote**. Fine on a slide; must never appear in quotation marks or be attributed to Anthropic. Anthropic's own labelled definition is "LLMs autonomously using tools in a loop". |
| `anthropic.com/news` (MCP) | S22 | **REGISTER** — exact announcement page verified. |
| `building-effective-agents` | S35 | **REGISTER at the canonical `/engineering/` URL** (the `/research/` path 301s). **No contiguous sentence on that page names the five patterns** — they are five separate H3 headings. No quote was invented; the entry uses the verified "these building blocks aren't prescriptive" line, which supports what S35 actually asserts. |
| `mistral.ai` ("open-weights track close behind") | S09 (+ S10) | **BLOCKER — the page does not exist.** Mistral's only relevant string is a product line. **Replaced with Epoch AI**, which measures exactly this: open models *"lagged frontier closed models by an average of four months"* (`epoch.ai/data-insights/open-closed-eci-gap`). Better source, same claim — and it feeds S10's two-lags slide directly. |
| `help.mistral.ai` + `scaleway.com` | A01 | **REGISTER BOTH** — exact EU sovereign-inference pages verified. |
| Karpathy `autoresearch` + nanochat +11% | S40 | Two separate stories — keep attributed separately. |
| Stripe migration "1 day vs 2 months" | S39 | Vendor launch-day testimonial. Ship with the caveat stated, or cut. |
| Steinberger loops post | S37 | **REGISTER** — exact post verified. |
| Cherny `/loop` | S37 | **BLOCKER — misattribution risk.** He has no primary first-person linkable source for "loops built into the harness"; his `/loop`-looking tweet is about `.claude/commands/` slash commands, and his real loops quotes exist only in a Bloomberg video surfaced via third-party quote-tweets. **Louis's call**: drop the name and cite Anthropic's loops post (already registered, and it documents `/loop`), or keep the name as a labelled secondary. |
| Karpathy published CLAUDE.md | S19 | **BLOCKER — wrong author.** The viral "Karpathy CLAUDE.md" was written by **Forrest Chang**, distilling Karpathy's X observations. Karpathy's real one lives in `karpathy/llm-council` and is project-specific notes, so *"a great model to steal from"* oversells it. Do not present the viral repo as his. |

## C. New sources collected for this talk (`./sources/`, 13 files)

| Source file | Carries | → Destination | Registry status |
|-------------|---------|---------------|-----------------|
| `v4F1gFy-hqg-insights.md` (Pocock) | 5 distinct claims + the Grill Me skill | **S25, S26, S27, S28, S29** | One YouTube entry + `mattpocock/skills` (already row A18). Timestamped quotes available. |
| `Sir59K8ZDPU-insights.md` (Coyle) | validate-before-side-effects; the agent-loop explainer; failure modes | **S30** (+ S13 alternate framing) | Needs YouTube registry entry + quote. |
| `tweet-…-state-of-ai-economy.md` (Azhar) | $110bn / $175bn / 3× / $2T CapEx | **S06** | Cite the **report page**, not the tweet. Tweet = discovery only. |
| `tweet-…-kimi-k3-vs-fable5-deepswe.md` | price × accuracy pairs; the real chart is the live leaderboard | **S08** | Cite `deepswe.datacurve.ai` + Together blog. Tweet numbers superseded — do not slide them. |
| `tweet-…-schema-arc-agi-3.md` | 98.98% RHAE self-reported; verified frontier 0.51% → 7.78% | **S11** | Cite arcprize.org for the verified numbers; the self-report only as a labelled self-report. |
| `tweet-…-nanogpt-prime-intellect.md` | 153 runs / 18 models; 82% of the gap; no new method | **S11 + S40** | Cite the Prime Intellect blog + leaderboard, not the tweet. |
| `tweet-…-fable-local-in-two-years.md` | ~24.8-month lag community chart | **RETIRED** | **Reason: measured false.** The `local-lag` run puts the real lag at 3-12 months, a factor of 2 to 8 lower, and the permalink was never recoverable. Replaced by Epoch AI's four-month open-weights figure. File kept; research not lost, only unused. |
| `tweet-…-dair-wikiskill.md` | WikiSkill: +12.3/17.5/23.9%; 9B+skills 47.4% > 27B 39.4% | **S52** | Cite arXiv:2608.27454 directly. Preprint caveat travels. |
| `tweet-…-femke-company-brain.md` | 9 systems, 4 shared parts | **S54** | Vendor marketing — per-system primaries needed (brief). Slite survey numbers do not ship uncorroborated. |
| `tweet-…-swyx-seo-automation.md` | scheduled AEO automations; $1M projection | **S55** | $1M = labelled practitioner anecdote. Measured data from the brief carries the slide. |
| `tweet-…-meta-skill-tractability.md` (Dean Ball) | the meta-skill aphorism | **S56** | Opinion, quotable, attributed. Note his OpenAI affiliation. |
| `tweet-…-founder-ownership-percent.md` (levelsio) | dilution + expected-value math | **A04** | Only if `founder-equity-expected-value` finds the Carta primaries. |
| `tweet-…-lecun-world-models.md` | LeCun $1.03B / world models | **RETIRED** | **Reason: Louis cut it (2026-08-31).** File kept in `sources/` — the research is not lost, only unused. |

## D. Pending research → destination

| Run / brief | → Destination | State |
|-------------|---------------|-------|
| run `frontier-evaluations` | **S07, S08, S11** | **LANDED** — 48/50 verified. Replaces METR with the Epoch Capabilities Index + Remote Labor Index; corrects the overfit *mechanism*. 3 unverified (2 JS-rendered leaderboards, 1 satirical forum post) — none backs a marker. |
| run `orchestration-2026` | **S31-S36** | **LANDED 2026-08-31** — 27/28 sources verified. Report + `sources.md` committed in the run dir; 28 new sources to register, listed there. **1 UNVERIFIED**: `openai.com/index/hugging-face-incident-and-the-road-ahead/` returns 403 to every automated client — it backs no marker and must NOT be cited until opened in a browser. |
| run `ai-economics` | **S05, S06** | **LANDED** — 20/22 verified. 2 unverified (McKinsey timeout, Bloomberg paywall); both routed through CNBC/KPMG instead. |
| run `autonomous-rnd` | S40, S11 | **RUNNING** (launched 2026-09-01) |
| run `company-memory` | S54 | **RUNNING** (launched 2026-09-01) |
| run `aeo` | slide 42 | **LANDED 2026-09-01** — 41/41 verified. One documented gap: no case study of a scheduled weekly AEO agent exists, so that pattern stays an anecdote. |
| run `local-lag` | slide 04c + appendix | **LANDED 2026-09-01** — **57/57 verified**. Verdict: drop the r/LocalLLaMA 24.8-month claim; the measured lag is 3-12 months, four months for open-weights parity. |
| brief `agent-benchmarks-sept-2026` | S08 | **folded into** run `frontier-evaluations` — kept as the leaderboard-snapshot checklist |
| brief `claude-watermarking-provenance` | A05 | queued, conversation-dependent |
| brief `founder-equity-expected-value` | A04 | queued, conversation-dependent |

## E. Assets to carry

| Asset | From | → Destination |
|-------|------|---------------|
| `metr-time-horizon.png` | heuritech assets | S07 — now shown as the retired curve |
| `epoch-inference.png` | heuritech assets | S09 |
| `orch-*.png` (5 Anthropic pattern figures) | heuritech assets | S35 |
| `claude-code-screenshot.png` | heuritech assets | S24 / A06 |
| `claudecode-mascot.svg` | heuritech assets | S05 |
| DeepSWE scatter | **to build** (`deck_chart.py`) | S08 |
| Prime Intellect leaderboard figure | `sources/videos/` (downloaded) | S11 — check licence before reuse; prefer rebuilding |
