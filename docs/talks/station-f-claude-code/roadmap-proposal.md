<!-- ABOUTME: Proposed roadmap/TOC for the Station F / Incubateur 42 talk of 2026-09-02, built on the heuritech-agents skeleton. -->
<!-- ABOUTME: Status: PROPOSAL — awaiting Louis's agreement before any slide is built. Sources collected in ./sources/. -->

# Roadmap proposal — Station F talk, 2026-09-02 14:00

**Slot**: 1h = ~40 min presentation + ~20 min conversation · **Language**: English · **Target**: ~39 slides + backup cards
**Audience**: Incubateur 42 founders, daily Claude users (Chloé: "la plupart utilisent bien sûr Claude") — they saw the April state-of-the-field + building-with-AI decks, so every number must be post-April fresh.
**Skeleton**: `slides/heuritech-agents/content/heuritech.md` (40 slides, 5 movements). Legend: KEEP / REFRESH (stale >3mo) / NEW (source in `./sources/`) / MERGED.

**Working title**: *Agentic Best Practices — Harness, Loops, Leverage* (alt: *Building With Agents in 2026*)

## Opening (3)
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 01 | Cover | NEW title | — |
| 02 | Instructor | REFRESH (SF move?) | — |
| 03 | Agenda — five movements | NEW | — |

## M1 — State of play, September 2026 (7) — the "what changed since April" payoff
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 04 | Intelligence is a commodity | KEEP | heuritech §04 |
| 05 | Crazy numbers (commit share, revenue, Fin) | REFRESH — all figures Jun-10-vintage | brief `ai-economics-refresh` |
| 06 | The AI economy in dollars — $110bn revenue, $175bn run rate, 3× faster than prior IT waves; the $2T CapEx tension (honest-broker beat) | NEW | tweet-…-state-of-ai-economy (Azhar 15-tweet thread + report) |
| 07 | METR curve | REFRESH — doubling now ~4.3 mo | brief `agent-benchmarks-sept-2026` |
| 08 | The price × effort × accuracy frontier — rebuilt scatter from the LIVE DeepSWE leaderboard (Kimi K3 ≈ Fable 5 at 35% price; Opus 5 at 74% since Aug 20) | NEW — the graph Louis wants early | tweet-…-kimi-k3-vs-fable5-deepswe + deck_chart.py |
| 09 | Frontier → your laptop — the two lags (open-weights parity vs consumer hardware) | NEW — r/LocalLLaMA chart NOT shippable as-is | tweet-…-fable-local-in-two-years + brief `frontier-to-local-lag` |
| 10 | Agents doing AI research — Prime Intellect: Fable 5 closed 82% of the gap to the human nanoGPT record… and no run invented a new method; ARC-AGI-3 harness story ([schema], self-reported caveat) | NEW | tweet-…-nanogpt-prime-intellect · tweet-…-schema-arc-agi-3 |

## M2 — The mental model, compressed (5) — they use it daily; compress heuritech's 10 harness slides
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 11 | Agent = a loop (definition + think/act/observe in one) | MERGED heuritech §08+09 | |
| 12 | Agent = LLM + harness (six parts) | KEEP §10 | |
| 13 | Context engineering — what the model actually sees | KEEP §19 (the big mental model) | |
| 14 | Skills & memory — progressive disclosure | MERGED §15+16 (sets up 33-34) | |
| 15 | Permissions, sandbox & auto mode — the autonomy dial | MERGED §12+20 (bridge to loops) | |

## M3 — Best practices: fundamentals matter more than ever (6) — NEW movement (Pocock + Coyle)
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 16 | Bad code is the most expensive it's ever been — AI compounds in good codebases, drowns in bad ones | NEW | v4F1gFy-hqg (Pocock) |
| 17 | Reach shared understanding first — the Grill Me pattern (2-line skill, 40-100 questions; why plan mode is "eager to create an asset") · live-demo option: Louis has the plugin installed | NEW | v4F1gFy-hqg |
| 18 | Ubiquitous language — a glossary file IS context engineering (calmer thinking traces) | NEW | v4F1gFy-hqg |
| 19 | The rate of feedback is your speed limit — TDD, types, browser access = the agent's verification harness | NEW | v4F1gFy-hqg |
| 20 | Design the interface, delegate the implementation — deep modules; "AI is the tactical sergeant, you're the strategic layer" | NEW | v4F1gFy-hqg |
| 21 | No side effects until validated — "Pydantic at the door, ontology at the ledger" → mapped onto Claude Code hooks/permissions/tool schemas | NEW | Sir59K8ZDPU (Coyle) |

## M4 — Loops & automating R&D (6)
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 22 | Don't prompt agents — build loops (thesis) | KEEP §21 | PostHog + Anthropic workshop |
| 23 | Four ingredients: goal · context · evaluation · agent | KEEP §22 | |
| 24 | Why now — capability gains | REFRESH §23 (METR figure, Stripe caveat) | |
| 25 | R&D automation in the wild — Karpathy autoresearch (+11%, 3-yr bug, attributed separately) + Prime Intellect's honest ceiling + scheduled automations (swyx's weekly AEO loop as teaser for 35) | NEW/MERGED | brief `autonomous-rnd-evidence` |
| 26 | Self-driving products — and the limits, stated plainly | KEEP §24 (+§25 folded) | |
| 27 | Loops synthesis → bridge to method | KEEP §26, short | |

## M5 — The method (5) — compressed from 8
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 28 | Method overview — the spine | KEEP §27 | |
| 29 | Clarify → binary checks (Pareto) | KEEP §28 | |
| 30 | Evaluate fresh + observability matrix (red row = bottleneck) | MERGED §30+31 | |
| 31 | Improve one bottleneck at a time | KEEP §32 | |
| 32 | Understand what you built (pairs with slide 20's "strategic layer") | KEEP §33 | |

## M6 — The founder's edge (5) — NEW closing movement: economic opportunities
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 33 | Skills that evolve — WikiSkill: the wiki carries the gain; 9B+skills (47.4%) beats 27B without (39.4%); + lessons.md / wrap-up / ablation (meta-improvement folded in) | NEW + §39 | tweet-…-dair-wikiskill (arXiv:2608.27454) |
| 34 | Company brain — the memory opportunity: 9 architectures, 4 shared parts, DIY = Claude Code + git; category <6 months old (Wemory-relevant → conversation fuel) | NEW | tweet-…-femke-company-brain + brief `company-memory-landscape` |
| 35 | AEO — untapped alpha: schedule an agent to autoresearch your AEO weekly (swyx's $1M framed as anecdote over measured referral data) | NEW | tweet-…-swyx-seo-automation + brief `aeo-answer-engine-optimization` |
| 36 | The meta-skill — spot what just became computationally tractable ("meta-genius for a year or two") — the movement's thesis | NEW | tweet-…-meta-skill-tractability (Dean Ball) |
| 37 | The bear case — LeCun raises $1.03B against the LLM path (world models); why the room should hold both views | NEW | tweet-…-lecun-world-models (cite TechCrunch/Brown/ETH primaries, never the re-upload) |

## Close (2)
| # | Slide | Status | Source |
|---|-------|--------|--------|
| 38 | The whole arc — loop → harness → fundamentals → loops → leverage | REFRESH §40 | |
| 39 | Conversation starters — 3-4 cards: What would you loop? · Does on-policy AEO work? · The ownership math (levelsio, if brief pans out) · Is AI output watermarked? (if brief pans out) | NEW | briefs `founder-equity-expected-value`, `claude-watermarking-provenance` |

## Backup / appendix cards (shown only if conversation goes there)
Sovereignty (§35) · Data hygiene (§36) · Orchestration patterns (§37) · LLM-as-judge (§38) — all KEEP from heuritech, demoted from main flow.

## Cut from heuritech
§11 Thinking models, §13 Preview, §17 Tools/MCP schemas, §18 Orchestration, §29 First draft — audience already lives these daily; MCP/tools get one line on slide 12.

## Pre-talk verification tasks (Sept 1-2 — live things move weekly)
- Re-snapshot DeepSWE leaderboard (moved Aug 20; may move again).
- Re-check Prime Intellect leaderboard (elie: more model results "next week").
- Check ARC Prize VERIFIED leaderboard vs [schema]'s self-report.
- Re-verify mattpocock/skills star count (241,839 on 2026-08-31) if quoted.
- Re-verify Pocock's plan-mode critique still holds against current plan mode (April-vintage claim).
- Run the citation gates (`check-citation-links.py --check-live`, `verify-sources.py`) — non-negotiable before ship.
