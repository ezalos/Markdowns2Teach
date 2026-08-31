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

| Mention | Heuritech slide | → Destination | Action needed |
|---------|-----------------|---------------|---------------|
| `agentskills.io` | 16 | S21 | Needs exact page + quote, or drop in favour of `anthropic-agent-skills`. |
| `snyk.io` (skill-security reflex) | 16 | S21 | Needs the exact article URL + quote. |
| `llm-stats.com/frontiercode` | 11 | S15 | Live leaderboard — re-snapshot; model names in the claim are stale. |
| `docs.claude.com` (CLAUDE.md, permissions/iam) | 14, 20 | S19 + S18 | Needs the exact doc pages (two different ones), not the domain. |
| `anthropic.com` (definition of an agent) | 9 | S12 | Exact page + quote. |
| `anthropic.com/news` (MCP announcement) | 18 | S22 | Exact page + quote. |
| `anthropic.com/research/building-effective-agents` | 37 | S35 | Exact page + quote (this one is already precise). |
| `mistral.ai`, `help.mistral.ai`, `scaleway.com` | 7, 35 | S09 + A01 | Exact pages + quotes. |
| Karpathy `autoresearch` repo + nanochat +11% | 22 | S40 | Two separate stories — keep attributed separately (see heuritech `sources-and-speakers.md`). |
| Stripe migration "1 day vs 2 months" | 23 | S39 | Vendor launch-day testimonial. Ship only with that caveat stated, or cut. |
| Steinberger loops post · Cherny `/loop` | 21 | S37 | Exact post URLs. |
| Karpathy published CLAUDE.md | 14 | S19 | Exact URL. |

## C. New sources collected for this talk (`./sources/`, 13 files)

| Source file | Carries | → Destination | Registry status |
|-------------|---------|---------------|-----------------|
| `v4F1gFy-hqg-insights.md` (Pocock) | 5 distinct claims + the Grill Me skill | **S25, S26, S27, S28, S29** | One YouTube entry + `mattpocock/skills` (already row A18). Timestamped quotes available. |
| `Sir59K8ZDPU-insights.md` (Coyle) | validate-before-side-effects; the agent-loop explainer; failure modes | **S30** (+ S13 alternate framing) | Needs YouTube registry entry + quote. |
| `tweet-…-state-of-ai-economy.md` (Azhar) | $110bn / $175bn / 3× / $2T CapEx | **S06** | Cite the **report page**, not the tweet. Tweet = discovery only. |
| `tweet-…-kimi-k3-vs-fable5-deepswe.md` | price × accuracy pairs; the real chart is the live leaderboard | **S08** | Cite `deepswe.datacurve.ai` + Together blog. Tweet numbers superseded — do not slide them. |
| `tweet-…-schema-arc-agi-3.md` | 98.98% RHAE self-reported; verified frontier 0.51% → 7.78% | **S11** | Cite arcprize.org for the verified numbers; the self-report only as a labelled self-report. |
| `tweet-…-nanogpt-prime-intellect.md` | 153 runs / 18 models; 82% of the gap; no new method | **S11 + S40** | Cite the Prime Intellect blog + leaderboard, not the tweet. |
| `tweet-…-fable-local-in-two-years.md` | ~24.8-month lag community chart | **S10** | **Blocked**: permalink unrecoverable. Replace with Epoch AI per brief, or the slide ships without it. |
| `tweet-…-dair-wikiskill.md` | WikiSkill: +12.3/17.5/23.9%; 9B+skills 47.4% > 27B 39.4% | **S52** | Cite arXiv:2608.27454 directly. Preprint caveat travels. |
| `tweet-…-femke-company-brain.md` | 9 systems, 4 shared parts | **S54** | Vendor marketing — per-system primaries needed (brief). Slite survey numbers do not ship uncorroborated. |
| `tweet-…-swyx-seo-automation.md` | scheduled AEO automations; $1M projection | **S55** | $1M = labelled practitioner anecdote. Measured data from the brief carries the slide. |
| `tweet-…-meta-skill-tractability.md` (Dean Ball) | the meta-skill aphorism | **S56** | Opinion, quotable, attributed. Note his OpenAI affiliation. |
| `tweet-…-founder-ownership-percent.md` (levelsio) | dilution + expected-value math | **A04** | Only if `founder-equity-expected-value` finds the Carta primaries. |
| `tweet-…-lecun-world-models.md` | LeCun $1.03B / world models | **RETIRED** | **Reason: Louis cut it (2026-08-31).** File kept in `sources/` — the research is not lost, only unused. |

## D. Pending research → destination

| Run / brief | → Destination | State |
|-------------|---------------|-------|
| run `frontier-evaluations` | **S07** (+ S08, S39 corrections) | LAUNCHED 2026-08-31, opus/high |
| run `orchestration-2026` | **S31-S36** | **LANDED 2026-08-31** — 27/28 sources verified. Report + `sources.md` committed in the run dir; 28 new sources to register, listed there. **1 UNVERIFIED**: `openai.com/index/hugging-face-incident-and-the-road-ahead/` returns 403 to every automated client — it backs no marker and must NOT be cited until opened in a browser. |
| brief `ai-economics-refresh` | S05, S06 | queued (cap = 2 runs) |
| brief `autonomous-rnd-evidence` | S40, S11 | queued |
| brief `company-memory-landscape` | S54 | queued |
| brief `aeo-answer-engine-optimization` | S55 | queued |
| brief `frontier-to-local-lag` | S10 | queued |
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
