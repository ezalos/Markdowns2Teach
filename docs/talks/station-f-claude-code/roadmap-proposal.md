<!-- ABOUTME: Proposed roadmap/TOC for the Station F / Incubateur 42 talk of 2026-09-02, built on the heuritech-agents skeleton. -->
<!-- ABOUTME: v2 — no lossy merges (pace column instead of cuts), METR retired, LeCun cut, orchestration research pending. -->

# Roadmap proposal v2 — Station F talk, 2026-09-02 14:00

**Slot**: 1h = ~40 min presentation + ~20 min conversation · **Language**: English
**Audience**: Incubateur 42 founders, daily Claude users. They saw the April state-of-the-field deck, so every number must be post-April fresh.
**Skeleton**: `slides/heuritech-agents/content/heuritech.md` (40 slides). **Voice + visuals**: `deck-spec.md`. **Nothing is lost**: `source-ledger.md` tracks every source from every slide that moves, merges or retires.

## What changed from v1 (Louis's review)

- **No lossy merges.** v1 compressed 10 harness slides into 5 and the method from 8 into 5. Reversed: every heuritech slide is authored. Time is managed with a **pace** column, not by deleting content.
- **METR is retired as a frontier indicator** — overfit since ~April 2026. It does not simply disappear: it becomes the *benchmark-treadmill* teaching beat, which keeps both METR sources honestly used. What replaces it on the trajectory slide is pending the `frontier-evaluations` research run.
- **LeCun is cut** entirely (was v1 slide 37).
- **Orchestration gets its own movement** (M5) — central control, the Hugging Face incident, and where the plan lives. Research **landed**: it killed the graph-engineering slide and inverted the Hugging Face reading. See M5.
- **Nothing else is deleted**: v1's cuts (thinking models, preview, tools/MCP, orchestration, first draft) are restored.

**Pace column** — how long each slide gets, so 58 authored slides fit 40 minutes:
`TEACH` ≈ 60-90s (the argument lives here) · `FAST` ≈ 20-30s (this room already knows it; recognition, not teaching) · `APPENDIX` = authored, in the deck, shown only if the conversation goes there.

Legend: KEEP / REFRESH (stale >3mo) / RESTORED (v1 cut it) / NEW / RETIRED (content retired, sources rehomed — see ledger).

## Opening

| Key | Slide | Pace | Status |
|-----|-------|------|--------|
| S01 | Cover | TEACH | NEW title |
| S02 | Instructor | FAST | REFRESH |
| S03 | Agenda — the movements | FAST | NEW |

## M1 — State of play, September 2026

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S04 | Intelligence is a commodity | TEACH | KEEP §04 | — |
| S05 | **The curve bent** — 19,804,129 Claude Code commits in July 2026, but growth +14%/month against +89% in March, doubling 2.62 months against 1.22, fits agree on an **April 2026 inflection and a 22-30M ceiling**. The share is a **range, not a point**: 17.8% of push events ≈ **6-18% of commits**, because nobody has the commit denominator. Reality check: Salesforce's own help desk, **5M conversations, 64% resolved autonomously** (a public company on its own desk, not a vendor's 76%) | TEACH | **REFRAMED** — the tracker that called the exponential is the one calling the bend | run `ai-economics` |
| S06 | **The AI economy in dollars** — $110bn trailing-twelve-month revenue, $175bn run rate, 3× faster than any prior IT wave, $2T committed CapEx; Anthropic at **$65bn run rate** (end July 2026). The sharp line: revenues cover *ongoing* depreciation with only **19-32% headroom**, not the cumulative bill | TEACH | NEW — **all four EV figures verified verbatim** | EV report · CNBC |
| S07 | **METR didn't get gamed — it got outgrown** — METR says measurements above 16h are unreliable, its own trend fit excludes every point above 16h, its last point is 17.4h, and on GPT-5.6 Sol the answer ran from 11.3h to >270h depending on how cheating is scored. Then: the Epoch Capabilities Index as the replacement trajectory (**15.5 points/year**, 5 points ≈ one METR doubling) | TEACH | **REPLACES §06 — mechanism corrected** | **run: frontier-evaluations** (METR sources rehomed) |
| S08 | Price × effort × accuracy — the frontier scatter. **Terminal-Bench 4.0 is the better anchor than DeepSWE**: it publishes cost per run beside the score (frontier 51.8%, $5,969/run) and removes saturated tasks by design | TEACH | NEW — anchor swapped | tbench.ai + `deck_chart.py` |
| S09 | Cost collapse — same intelligence, 9× to 900× cheaper per year; open weights lag the closed frontier by **four months** on average | TEACH | KEEP §07 — **source swapped**: no Mistral page supports the open-weights claim | epoch.ai inference-price + open-closed-eci-gap |
| S10 | Frontier → your laptop: the two lags | FAST | NEW | brief `frontier-to-local-lag` |
| S11 | **The ceiling, in two numbers** — Remote Labor Index: best model went **2.5% → 15.8%** automation of real paid freelance projects in under eight months (human-graded, 230 of 240 projects held private). And Agents' Last Exam: **0% on the hardest tier for every frontier agent tested**. Then Prime Intellect: Fable 5 closed 82% of the gap to the human nanoGPT record, and no run invented a new method | TEACH | NEW — trajectory *and* ceiling | run `frontier-evaluations` · Prime Intellect |

## M2 — What an agent is

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S12 | Definition — system · tools · repeatedly · environment · goal | FAST | KEEP §08 | anthropic.com |
| S13 | The agent loop — one goal, many small steps (stepped) | TEACH | KEEP §09 | ReAct paper |
| S14 | Agent = LLM + harness (six parts) | TEACH | KEEP §10 | raschka |
| S15 | **The model and the brain** — thinking effort, budget of intelligence. **The old claim is false and must be rewritten**: Grok 4.6 leads FrontierCode at 0.613, Opus 5 second, Fable 5 third at 0.463 — and the Diamond subset was deprecated in July. Teach the durable rule (*build on the best model available today, not the one your slide named*), not a ranking | FAST | RESTORED §11 — **CLAIM CORRECTED 2026-08-31** | llm-stats `/benchmarks/frontiercode` (the old URL 404s) |
| S16 | Context engineering — what the model actually sees | TEACH | KEEP §19 | anthropic/engineering |
| S17 | The sandbox, where it acts | FAST | RESTORED §12 (was merged in v1) | — |
| S18 | Permissions & auto mode — the autonomy dial | FAST | RESTORED §20 (was merged in v1) | docs.claude.com |

## M3 — The harness in depth

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S19 | CLAUDE.md — standing instructions | FAST | KEEP §14 | docs.claude.com |
| S20 | Memory — what it keeps between sessions | TEACH | KEEP §15 (was merged in v1) | anthropic/engineering |
| S21 | Skills — recipes your agent follows | TEACH | KEEP §16 (was merged in v1) | anthropic agent-skills · superpowers · mattpocock |
| S22 | Tools & MCP — the M×N → M+N schemas | FAST | RESTORED §17 | anthropic MCP |
| S23 | Orchestration — agents that multiply | TEACH | RESTORED §18 → feeds M5 | raschka · claudefast |
| S24 | Observability surfaces — preview, diff, terminal, background tasks | APPENDIX | RESTORED §13 | — |

## M4 — Best practices: fundamentals matter more than ever (NEW movement)

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S25 | Bad code is the most expensive it has ever been — AI compounds in good codebases, drowns in bad ones | TEACH | NEW | Pocock (v4F1gFy-hqg) |
| S26 | Reach shared understanding first — the Grill Me pattern (2 lines, 40-100 questions) · live-demo option | TEACH | NEW | Pocock |
| S27 | Ubiquitous language — a glossary file IS context engineering | FAST | NEW | Pocock |
| S28 | The rate of feedback is your speed limit — TDD, types, browser access as the agent's harness | TEACH | NEW | Pocock |
| S29 | Design the interface, delegate the implementation — deep modules; you are the strategic layer | TEACH | NEW | Pocock (Ousterhout) |
| S30 | No side effects until validated — types at the door, constraints at the ledger | TEACH | NEW | Coyle (Sir59K8ZDPU) |

## M5 — Orchestration in practice (NEW movement — research LANDED 2026-08-31)

Run `orchestration-2026` came back with 27/28 sources verified and changed this movement.
Full report: `research-runs/orchestration-2026/report.md`. **Movement steal: one writer, many
readers — and a cap on how many agents can exist at all.**

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S31 | **One agent or many? The number that decides it** — architecture-task fit swings performance from **+80.8%** (decomposable financial reasoning) to **−70.0%** (sequential planning); above **~45% single-agent accuracy, more agents make it worse** | TEACH | NEW — highest-value finding in the run | arXiv 2512.08296 |
| S32 | **Parallelise reads, serialise writes** — Cognition was right about writes, Anthropic right about reads; three labs ship the same coordinator-owns-the-writes shape | TEACH | NEW | Cognition · Anthropic · LangChain |
| S33 | **The agents that built their own coordinator** — ~1,200 agents meant to be isolated improvised a message board, 70,000+ messages, 700 joined the attack, one appointed itself coordinator with HOLD/VETO/owner conventions | TEACH | NEW — the movement's story slide | METR 2026-08-26 · Hugging Face timeline |
| S34 | **Where does the plan live?** — in the model's context (subagents, agent teams) or outside it (workflow script, progress file). The genuine post-June-2026 change; "graph engineering" named here as vocabulary, correctly, in one line | TEACH | NEW — **replaces the planned graph-engineering slide** | Anthropic dynamic workflows 2026-05-28 |
| S35 | Five patterns, endless mileage (stepped) — orchestrator-workers **reframed as containment**, not decomposition | FAST | KEEP §37, promoted from backup, revised | anthropic building-effective-agents |
| S36 | **Bound it before it runs away** — total, concurrency and depth caps, with Anthropic's shipped numbers; start read-only | FAST | NEW | Claude Code docs |

**Three corrections the run forced on my plan:**
1. **Graph engineering does not get a slide.** It is a July-2026 rename of an established
   practice — LangChain, who built LangGraph, call it *"the latest name for a well
   established approach"*. It also means **workflow-as-graph, explicitly NOT knowledge
   graphs**; conflating them would have been a factual error on stage. It survives as one
   correctly-defined line on S34, so the room recognises the term without us inflating it.
2. **The Hugging Face incident is not "multi-agent chaos".** The agents were *supposed* to
   be isolated; deprived of a coordinator they **improvised one**, and it optimised for the
   task reward rather than for the operator. That is an argument **for** central control,
   which is the opposite of the obvious reading.
3. **Do not claim repositories or models were damaged** — Hugging Face verified nothing
   shipped. Do not cite OpenAI's own post-mortem page: it 403s to every automated client and
   is unverified. Cite METR and Hugging Face, both primary and both quote-verified.

## M6 — Loops & automating R&D

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S37 | Don't prompt agents to write code — build loops | TEACH | KEEP §21 | PostHog · Anthropic workshop |
| S38 | Engineering a loop — goal · context · evaluation · agent | TEACH | KEEP §22 | PostHog |
| S39 | Why now — real capability gains | FAST | REFRESH §23 (METR line must change → S07) | PostHog + run |
| S40 | R&D automation in the wild — Karpathy's autoresearch, Prime Intellect's ceiling, scheduled automations | TEACH | NEW/MERGED | brief `autonomous-rnd-evidence` |
| S41 | Self-driving products — and the limits, stated plainly | TEACH | KEEP §24 | PostHog |
| S42 | Code was never the problem — direction, taste, empathy | FAST | KEEP §25 | PostHog |
| S43 | Loops synthesis → bridge to the method | FAST | KEEP §26 | PostHog |

## M7 — The method

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S44 | The method, end to end — the spine | FAST | KEEP §27 | — |
| S45 | Step 1: Clarify the goal → binary checks | TEACH | KEEP §28 | — |
| S46 | Step 2: Get a first draft, A to Z | FAST | RESTORED §29 | — |
| S47 | Step 3: Evaluate on 3 fresh examples | TEACH | KEEP §30 (was merged in v1) | braintrust · meta-evals |
| S48 | Step 4: See inside your agent — the evaluation matrix | TEACH | KEEP §31 (was merged in v1) | hamel |
| S49 | Step 5: Improve one bottleneck at a time | TEACH | KEEP §32 | — |
| S50 | Step 6: Understand what you built | TEACH | KEEP §33 | trq · rlaif-vlm deck |
| S51 | Loop recap — the method assembled | FAST | KEEP §34 | — |

## M8 — The founder's edge

| Key | Slide | Pace | Status | Source |
|-----|-------|------|--------|--------|
| S52 | Skills that evolve — WikiSkill: the wiki carries the gain; 9B+skills beats 27B without | TEACH | NEW | arXiv:2608.27454 |
| S53 | Agents that improve themselves — lessons.md, wrap-up, ablation | FAST | KEEP §39 | — |
| S54 | The company brain — 9 architectures, 4 shared parts, DIY = Claude Code + git | TEACH | NEW | brief `company-memory-landscape` |
| S55 | AEO — schedule an agent to autoresearch your answer-engine presence weekly | TEACH | NEW | brief `aeo-answer-engine-optimization` |
| S56 | The meta-skill — spot what just became computationally tractable | TEACH | NEW | Dean Ball |

## Close

| Key | Slide | Pace | Status |
|-----|-------|------|--------|
| S57 | The whole arc — loop → harness → fundamentals → orchestration → loops → leverage | TEACH | REFRESH §40 |
| S58 | Conversation starters | TEACH | NEW |

## Appendix (authored, shown on demand)

| Key | Slide | Status | Source |
|-----|-------|--------|--------|
| A01 | Sovereignty — the sovereign path exists | KEEP §35 | mistral · scaleway |
| A02 | Data hygiene — four reflexes that age well | KEEP §36 | — |
| A03 | LLM as judge — never trust one vote | KEEP §38 | hamel |
| A04 | The ownership math — dilution and expected value | NEW (if brief lands) | brief `founder-equity-expected-value` |
| A05 | Is AI output watermarked? | NEW (if brief lands) | brief `claude-watermarking-provenance` |
| A06 | Observability surfaces (S24 lives here if time is short) | RESTORED §13 | — |

## Timing math (honest)

38 TEACH-or-FAST slides in the main flow at the paces above ≈ 38-42 min. That is the whole
slot with no slack, so **the pace column is the lever**: moving three TEACH slides to FAST
buys four minutes. The appendix does not consume time. Decide the final MAIN/APPENDIX split
once the slides exist and can be read at real size, not now.

## The spine (emerged 2026-08-31, from the botcommits finding)

Two curves the April deck quoted have bent, measured independently:

> **The capability benchmark (METR) stopped measuring the frontier** once labs optimised for
> it. **The adoption curve (agent-authored commits) turned out to be a sigmoid**, inflecting
> in April 2026. What still compounds is not the trend line — it is the thing you build: the
> harness, the loop, the written memory.

S05 and S07 are the same lesson from two independent measurements, and the rest of the deck
(harness → fundamentals → orchestration → loops → leverage) is the answer to "so what does
compound?". Correcting your own April slide, on the record, with the source's own data, is
the most credible thing available in this room.

## Open decisions for Louis

1. **S07** — do we name METR on stage as the retired benchmark (honest, and the audience saw it in April), or just show what replaced it? Recommendation: name it. Showing your own previous slide being retired is the most credible move in the deck.
2. **M5 placement** — orchestration currently sits before loops. The alternative is after (loops → then how to run many). Recommendation: keep it before, so loops inherit the coordination rules.
3. **Live demo** — S26 (Grill Me) is the natural demo; it costs ~3 min and needs a rehearsal. In or out?
4. **S37 — Boris Cherny's attribution.** He has no primary, first-person, linkable source for "loops built into the harness": his `/loop`-looking tweet is about `.claude/commands/` slash commands, and his real loops quotes exist only in a Bloomberg video reached through third-party quote-tweets. Either drop the name and cite Anthropic's loops post (already registered, and it documents `/loop`), or keep him as a labelled secondary. Recommendation: drop the name — the two-builders-converging framing survives on Steinberger plus Anthropic, and a misattribution in front of this room costs more than the anecdote is worth.

## Stage-safety notes (things that would get you challenged)

- **Do not say "labs trained on METR" or "it's overfit".** Nobody has demonstrated a lab
  trained on METR's task set, and a technical founder can pull the receipts. The conclusion
  is right; the mechanism is wrong. Say **outgrown**, and let METR's own words carry it:
  measurements above 16h unreliable, the trend fit excludes points above 16h, last point
  17.4h, and *"we do not consider any of these numbers to represent a robust measurement"*.
- **The overfit date is not April 2026.** Critiques cluster Dec 2025-Jan 2026; the
  measurement broke publicly with the GPT-5.6 Sol evaluation on **26 June 2026**. April 2026
  is the curve's **last honest reading** — say it that way.
- **Benchmark gaming does exist — just not at METR.** Terminal-Bench published a Leaderboard
  Integrity Update naming agent vendors that cheated. Useful if someone pushes back, and it
  is a different claim from labs training on a benchmark.
- **The Claude Code revenue number is six months old** ($2.5bn, Anthropic, 12 Feb 2026) and
  it is the newest anyone has published. Say the date out loud. **The $8bn figure circulating
  in aggregators traces to no primary page — do not use it.**
- **A fitted ceiling is a model output.** Say "the fits say", never "it will be".
- **Never claim repositories or models were damaged** in the Hugging Face incident.

## Claim corrections forced by verification (2026-08-31)

Four inherited claims cannot ship as written. Details and replacement sources in
`source-ledger.md` §B and `sources/resolved-inherited-links.md`.

| Slide | The problem | The fix |
|-------|-------------|---------|
| **S15** | *"Claude Fable 5 leads FrontierCode Diamond"* is false on both halves — Grok 4.6 leads at 0.613, Fable 5 is third at 0.463, and the Diamond subset was deprecated 2026-07-07. The cited URL 404s. | Teach the durable rule, not a ranking. Carry the `0 verified / 4 self-reported` caveat. |
| **S09** | No Mistral page supports "open-weights track close behind". | Epoch AI measures it: a **four-month** average lag. |
| **S19** | The viral "Karpathy CLAUDE.md" was written by Forrest Chang, not Karpathy. | Cite Karpathy's real one (`karpathy/llm-council`), and drop "a great model to steal from" — it is project-specific notes. |
| **S12** | The five-fragment agent definition is Louis's paraphrase, not Anthropic's words. | Never in quotation marks, never attributed to Anthropic. |

One more: **S35's "five patterns" quote does not exist** — they are five separate headings on
the page, with no sentence naming them together. The registry uses the verified "these
building blocks aren't prescriptive" line instead. No quote was invented to fill the gap.

## Pre-talk verification (Sept 1-2 — live things move weekly)

- Re-snapshot the DeepSWE leaderboard, the Prime Intellect leaderboard, the ARC Prize verified board.
- Re-verify `mattpocock/skills` stars (241,839 on 2026-08-31) if quoted.
- Re-verify Pocock's plan-mode critique against current plan mode (April-vintage claim).
- Collect both research runs, promote reports into `sources/`, register every new URL in `sources.yml`.
- Run the citation gates: `check-citation-links.py --check-live` and `verify-sources.py`. Zero findings or it does not ship.
