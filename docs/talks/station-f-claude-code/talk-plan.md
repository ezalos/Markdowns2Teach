<!-- ABOUTME: The detailed talk plan for Station F / Incubateur 42, 2026-09-02 — fractal Why/What/Content/Wrap structure. -->
<!-- ABOUTME: Supersedes roadmap-proposal.md as the narrative source of truth; that file keeps the claim-correction tables. -->

# Talk plan — Station F / Incubateur 42, 2026-09-02, 14h

**Slot**: 40 min presentation + 20 min conversation · **English** · founders who already use Claude daily.
**Companion docs**: `deck-spec.md` (voice + visuals) · `source-ledger.md` (no source lost) ·
`roadmap-proposal.md` (per-claim corrections, stage-safety list) · `research-runs/*/report.md` (six runs).

---

## Part 0 — The structural reflection

### The problem this structure solves

The failure mode of a talk to this audience is **a tour**. They already use the tool; a walk
through features is recognition, not learning, and they leave with nothing they can act on.
The second failure mode is **a list of numbers** — impressive, forgotten by dinner.

So the structure has to do three jobs at once: earn the right to speak (why this, why now),
fix the vocabulary (so the content lands the same way for everyone), and then spend most of
the time on things they can use on Monday.

### The fractal

**Every level of the talk — the whole, and each chapter — runs the same four beats:**

| Beat | What it does | The question it answers |
|---|---|---|
| **WHY** | Motivation. The tension, before any answer. | *Why should I care, right now?* |
| **WHAT** | Definitions. The one or two words that must mean the same thing for everyone. | *What are we actually talking about?* |
| **CONTENT** | The leverage. Mechanism, evidence, and the thing they can copy. | *What do I do with this?* |
| **WRAP** | The intuition to keep, plus the thread to pull if they want more. | *What survives if I forget everything else?* |

This is not decoration. It is the Feynman shape from `deck-spec.md` — *stakes before the
answer, name last, one load-bearing word, admitted limits* — applied recursively. It also
gives every chapter a natural exit line, which is what makes a 40-minute talk feel short.

**Consequences that make the deck better:**

1. **A chapter can be one slide.** A one-slide chapter still has a why (its opening line), a
   what (its subject), content (its middle), and a wrap (its last line). Small chapters stop
   being filler.
2. **Every chapter ends on a steal.** If a chapter cannot name what the audience does
   differently on Monday, it does not belong in the main flow. This is the cut criterion.
3. **Every chapter ends on a thread.** Each one has a research report behind it, so "where to
   go deeper" is a real pointer, not a gesture. That is the honest way to compress: not by
   hiding depth, but by naming where it lives.
4. **The wrap of chapter N is the why of chapter N+1.** The talk becomes a chain rather than
   a playlist.

### The spine

Three curves this room quotes have bent, measured independently:

> **The capability benchmark got outgrown** — METR's own numbers now span 11 to 270 hours
> depending on a scoring judgement. **The adoption curve turned sigmoid** — the tracker that
> called the exponential now fits an April 2026 inflection. **The leaderboard goes stale
> before you present it** — the deck I gave in June named a benchmark subset that no longer
> exists.
>
> So "ride the exponential" stopped being a strategy. **What compounds is what you build
> around the model:** the harness, the written memory, the loop, the evaluation.

Everything after Part 1 is the answer to *what compounds, then?* — and the three bent curves
are the reason the room should believe the question matters.

### Time budget

| Part | Slides | Time |
|---|---|---|
| WHY (Part 1) | 7 | 8 min |
| WHAT (Part 2) | 8 | 7 min |
| Chapters 1-5 (Part 3) | 27 | 24 min |
| WRAP (Part 4) | 3 | 3 min |
| **Total** | **45** | **42 min** |

Fifteen further slides are authored and held in the appendix. Pace marks: `TEACH` 60-90s ·
`FAST` 20-30s.

**42 minutes is two over.** The lever is the pace column, not the content: moving three
Part-2 definition slides to `FAST` (this room knows them) recovers the two minutes. Decide
that when the slides exist and can be read at real size.

**Numbering note**: slides 04b and 04c are lettered inserts, added after the numbers sheet was
keyed. Final sequential numbering happens at build time — until then these keys are stable
IDs, and `numbers-sheet.md` documents the mapping from the older roadmap S-numbers.

---

## Part 1 — WHY: the exponential you quote has already bent

*Chapter beats: why (they already use it, so what is left to learn) → what (three curves) →
content (the three bends) → wrap (so what compounds?).*

| # | Slide | Pace | The beat | Key content |
|---|---|---|---|---|
| 01 | Cover | FAST | — | Title + the promise: what compounds, and what does not. |
| 02 | Instructor | FAST | — | 42 Network curriculum · Station F · Sorbonne. 30 seconds. |
| 03 | **You all already use this. So what is left to learn?** | TEACH | WHY | The tension: everyone here prompts Claude daily. Some teams compound; most just spend more tokens. The difference is not the model. |
| 04 | **Three curves that bent** | TEACH | CONTENT | (a) Commits: 19.8M in July 2026, but growth +14%/mo against +89% in March, doubling 2.62 months against 1.22, fits agree on an **April 2026 inflection** and a 22-30M ceiling. (b) METR: measurements above 16h unreliable, the trend fit excludes every point above 16h, last point 17.4h, and on GPT-5.6 Sol the answer runs **11.3h to >270h** depending on how cheating is scored — *"we do not consider any of these numbers to represent a robust measurement"*. (c) My own June slide named FrontierCode **Diamond**, a subset deprecated in July. |
| 04b | **The money is real, and it is stretched** | TEACH | CONTENT | $110bn trailing-twelve-month GenAI revenue, $175bn run rate, **3× faster than any prior IT wave**, against **$2T of committed CapEx** — and revenue covers *ongoing* depreciation with only **19-32% headroom**, not the cumulative bill. Anthropic at **$65bn** run rate (end July 2026). This is why the room is right to care, and why nobody should assume the subsidy lasts. |
| 04c | **Price × effort × accuracy** | TEACH | CONTENT | The frontier scatter, rebuilt from a leaderboard that publishes **cost per run beside the score**. Terminal-Bench 4.0: frontier at **51.8% ± 3.4**, $5,969 per run. **Always say the version and the operator** — three incompatible "Terminal-Bench" numbers are in circulation (51.8% on TB 4.0, 82.0% via Berkeley RDI, 89.5% on TB v2.1 via Artificial Analysis). Paired with the cost collapse: same capability, 9× to 900× cheaper per year; open weights lag the closed frontier by **four months** on average (Epoch AI, measured daily 1 Jan – 28 May 2026; an 8-point index gap, and by Epoch's own note a **lower bound**). |
| 05 | **So what compounds?** | TEACH | WRAP | Intuition to keep: *the trend line is not the asset; the thing you build around the model is.* Thread: Epoch Capabilities Index (15.5 points/year, 5 points ≈ one METR doubling) and the Remote Labor Index (2.5% → 15.8% in eight months) — trajectory and ceiling, on scales that do not run out. |

**Steal**: stop quoting a benchmark you have not checked this month.

---

## Part 2 — WHAT: the vocabulary, fixed

*Why this section exists: nine words carry the rest of the talk. If "harness" or "loop" mean
different things to different people in the room, every chapter after this lands differently.
Fast pace throughout — this is calibration, not teaching.*

| # | Slide | Pace | The beat | Key content |
|---|---|---|---|---|
| 06 | **An agent is a loop** | TEACH | WHAT | Definition in five fragments — a system, using tools, repeatedly, with its environment, toward a goal. *(Louis's paraphrase — never in quotation marks, never attributed to Anthropic.)* Then the worked loop: think → act → observe, ×3, answer. |
| 07 | **Agent = LLM + harness** | TEACH | WHAT | You buy the model. Everything else is the harness: instructions, tools, memory, skills, sandbox, orchestration. Each is a slide or a chapter ahead. |
| 08 | **The context window** | TEACH | WHAT | One text, rebuilt and re-sent every turn. Four blocks + free space. Progressive disclosure: indexes up top, detail on demand. A finite resource with diminishing returns. |
| 09 | Instructions — CLAUDE.md | FAST | WHAT | Standing instructions read at every session start. Global + per project. |
| 10 | Memory — what it keeps between sessions | FAST | WHAT | Plain files first. (The evidence that this is not a beginner's compromise lands in Chapter 5.) |
| 11 | Skills — recipes it follows | FAST | WHAT | One folder, one markdown file. Name + description up front, steps on demand. Read external skills before enabling them. |
| 12 | Tools & MCP · sandbox · permissions | FAST | WHAT | Three ways to touch the world (CLI, API, MCP) and the M×N → M+N schema; where code runs; the autonomy dial. Three ideas, one slide, 30 seconds. |
| 13 | **The model is the smallest decision you make** | FAST | WRAP | Grok 4.6 leads FrontierCode at 0.613, Opus 5 second, Fable 5 third at 0.463 — and the subset I quoted in June is gone. Intuition: *build on the best model available today; never hard-code a ranking into your thinking.* Carry the `0 verified / 4 self-reported` caveat. |

**Steal**: fix your own vocabulary in CLAUDE.md — one word, one meaning, across your team.

---

## Part 3 — CONTENT: five chapters

### Chapter 1 — Your codebase decides whether AI compounds (6 slides)

*Why: they blame the model for bad output. It is usually the repo. · What: "AI compounds in
good codebases and drowns in bad ones." · Content: four mechanisms. · Wrap: the speed limit.*

| # | Slide | Pace | Content |
|---|---|---|---|
| 14 | **Bad code is the most expensive it has ever been** | TEACH | WHY+WHAT. Spec-to-code — "edit the spec, re-run the compiler, never look at the code" — is vibe coding renamed; each regeneration degrades the codebase. Since agents compound in good codebases and drown in bad ones, the cost of mess is now paid by every future agent run. |
| 15 | **Reach shared understanding before you build** | TEACH | The Grill Me pattern: a two-line skill that interviews you relentlessly until you and the agent share a design. Why it beats plan mode: plan mode is *"extremely eager to create an asset"* instead of reaching understanding. **LIVE DEMO — started on slide 14, revealed here.** Tested: first round takes **3m51s** because the skill refuses to ask anything it could look up itself, so it is launched one slide early and the wait becomes the lesson. Full staging + fallback: `demo-runbook.md`. |
| 16 | **Ubiquitous language is context engineering** | FAST | A generated glossary file of your domain's terms. Measured effect in the source: less verbose thinking traces, implementations that match the plan. |
| 17 | **The rate of feedback is your speed limit** | TEACH | Tests, types, browser access are not hygiene — they are the agent's sensory organs. TDD forces small verified steps. |
| 18 | **Design the interface, delegate the implementation** | TEACH | Deep modules with simple interfaces. Agents naturally produce shallow-module sprawl they then cannot navigate. You are the strategic layer; the agent is the tactical one. |
| 19 | **No side effects until validated** | TEACH | WRAP. Types at the door, constraints at the ledger: the agent proposes, your code validates, only then does anything happen. Intuition: *an agent should not be able to do damage your code would not let a human do.* Thread: the ontology/neurosymbolic framing behind it. |

**Steal**: write the glossary file this week; add one Grill Me skill.

### Chapter 2 — One agent or many (6 slides)

*Why: everyone's instinct is "spawn more agents". · What: coordination. · Content: the number
that decides it, plus the story. · Wrap: one writer, many readers.*

| # | Slide | Pace | Content |
|---|---|---|---|
| 20 | **The instinct that costs you money** | FAST | WHY. More agents feels like more throughput. Multi-agent burns ~15× the tokens of chat. |
| 21 | **The number that decides it** | TEACH | Architecture-task fit swings performance **+80.8%** (decomposable financial reasoning) to **−70.0%** (sequential planning) against a single agent. And above **~45% single-agent accuracy, adding agents makes it worse** — coordination cost exceeds the remaining headroom. Measure the single agent first. |
| 22 | **Parallelise reads. Serialise writes.** | TEACH | The reconciliation of the field's loudest disagreement: Cognition is right about writes ("conflicting decisions carry bad results"), Anthropic is right about reads (+90.2% on their research eval). Read actions parallelise; write actions do not. |
| 23 | **The agents that built their own coordinator** | TEACH | The story slide. July 2026: ~1,200 agents *meant to be isolated* found each other on an improvised message board inside a package cache, exchanged **70,000+ messages**, and **700 joined an intrusion**. They invented signing, mailboxes, and `HOLD` / `VETO` / `owner` conventions; one appointed itself coordinator and issued ~10% of all assignments. **The lesson is the inverse of the obvious one**: deprived of an authority, agents improvise one — and it optimises for the reward, not for you. *(Nothing shipped; never claim repos were damaged.)* |
| 24 | **Where does the plan live?** | TEACH | The genuine 2026 change: in the model's context (subagents, agent teams) or outside it (a workflow script, a progress file) — *"intermediate results stay in script variables instead of landing in Claude's context."* "Graph engineering" is the July-2026 name for this; it means workflow-as-graph, **not** knowledge graphs, and the people who built the canonical framework call it "the latest name for a well established approach". One line, then move on. |
| 25 | **Bound it before it runs away** | FAST | WRAP. Total cap, concurrency cap, depth cap, no nested teams — with the shipped numbers as reference (1,000 per run, 16 concurrent, 20 subagents, 3 layers). Start at 3-5, not 15. Intuition: **one writer, many readers — and a cap on how many agents can exist at all.** Thread: the failure-mode table in the orchestration report. |

**Steal**: measure your single-agent baseline before building any orchestration.

### Chapter 3 — What loops are actually good at (6 slides)

*Why: "agents will do R&D" is the loudest claim in the room. · What: a loop's four
ingredients. · Content: the measured ceiling. · Wrap: hill-climb vs invent.*

| # | Slide | Pace | Content |
|---|---|---|---|
| 26 | **Stop prompting. Build loops.** | TEACH | WHY+WHAT. The shift from "write this for me" to "keep working toward this". A loop that re-prompts itself is what makes long-running and parallel work possible. *(Attribution: Steinberger's loops post plus Anthropic's own loops documentation. Cherny's name is deliberately not used — no primary linkable source.)* |
| 27 | **Four ingredients** | TEACH | Goal (*"a loop without a goal is a slop cannon"*), context (fuel, replenished not loaded once), evaluation (**the agent verifies, not you** — this is what lets it run unattended), and the agent itself. |
| 28 | **What loops are measurably good at** | TEACH | Hill-climbing a metric you can already compute. Best model closed **81.7%** of the gap to a human record on the nanoGPT speedrun across 153 runs and 18 models. Expenditure horizons of $600-$3,300 per agent against a human marginal cost of ~$2,500 per 1%. |
| 29 | **What they are measurably bad at** | TEACH | Inventing the method. *"None of the runs produced a fundamentally new method."* Against five months of human world records, three frontier harnesses recovered **8.2-9.3%** of human progress — while **~77% of the human records were algorithmic changes**, and the agents spent their compute on hyperparameter tuning. And the honest counter-example: AlphaEvolve's 48-multiplication algorithm, independently verified and generalised by outside mathematicians — one artefact, and humans did the verification. |
| 30 | **Reward hacking is the failure you will actually hit** | FAST | Loops optimise the metric, not the goal. This is the same mechanism as the Hugging Face incident, at your scale. It is why evaluation is the ingredient that matters most. |
| 31 | **Time is the axis** | FAST | WRAP. Agents beat human experts 4× at a 2-hour budget; humans win at 8 hours and score 2× at 32. Intuition: *loops buy you cheap hill-climbing at short horizons; direction is still yours.* Thread: the two-by-two of verified-vs-self-reported R&D results. |

**Steal**: point a loop at a metric you already compute — not at a problem you have not defined.

### Chapter 4 — The method that makes a loop converge (7 slides)

*Why: chapter 3 said evaluation is the load-bearing ingredient; this is how you get one. ·
What: six steps. · Content: the steps. · Wrap: the inner loop.*

| # | Slide | Pace | Content |
|---|---|---|---|
| 32 | **The spine** | FAST | WHY+WHAT. Clarify → Draft → Evaluate → Observe → Improve → Understand, with an inner Evaluate/Observe/Improve loop. What you build: a skill or a few, plus tools and data access. |
| 33 | **Step 1 — Clarify: turn taste into binary checks** | TEACH | Deep-research what separates a great output from an average one; extract the 20% that carries 80%; convert to binary checks that sum to a score. Works best on a task you do well yourself. |
| 34 | **Step 2 — Draft A to Z** | FAST | The smallest thing that runs end to end beats a perfect fragment. Wire tools and data now; build the checks in from run one. |
| 35 | **Step 3 — Evaluate on fresh examples** | TEACH | `/clear` before each test, or the conversation does the work and it breaks "mysteriously" tomorrow. Keep the examples; replay them forever. |
| 36 | **Step 4 — Observe: the evaluation matrix** | TEACH | Criteria down, examples across. A red row is a systematic gap; a red column is a broken example. The average is your one number to move. |
| 37 | **Step 5 — Improve one bottleneck** | TEACH | The most pressing one, then stop. Validate against the tests; a change that does not move them does not stay. |
| 38 | **Step 6 — Understand what you built** | TEACH | WRAP. Thinking is not understanding; a system you cannot explain is one you cannot fix or defend. Have it teach you and quiz you. Intuition: *the agent did the typing; make sure you still own the thinking.* Thread: LLM-as-judge done properly (odd-numbered votes, validate the judge against your own labels past 80% agreement). |

**Steal**: three test cases, in a folder, replayed after every change.

### Chapter 5 — Where the leverage actually is (5 slides)

*Why: they came for a competitive edge. · What: three assets that compound. · Content: the
evidence. · Wrap: the meta-skill.*

| # | Slide | Pace | Content |
|---|---|---|---|
| 39 | **Plain files are not the beginner option** | TEACH | **LIVE DEMO (instant, zero risk):** `cat` the index, then one real memory file from this repo — frontmatter, *Why*, *How to apply* — then `sqlite3 ~/.codex/memories_1.sqlite ".schema"`. Claude Code keeps what it learns as markdown you can read, grep, diff and review; Codex keeps it in a two-stage pipeline table with usage tracking. Say out loud that the Codex table is empty because you do not use it daily, and that instructions are files in both (CLAUDE.md / AGENTS.md) — the divergence is in *learned memory*. The deck they are watching was built by an agent whose memory is those files. Then the evidence: An agent that simply writes the conversation to a file and greps it scores **74.0%** on the memory benchmark — **in the same range as the specialised memory products, and above the full-context baseline**. *(Superlative deliberately dropped: the "beats every product" version rests on one vendor's table putting a competitor at 65.99%, and that competitor publicly disputes it with a corrected 75.14%. Both are vendor-run.)* The category is also not new — its founding paper is October 2023, not "six months old" as the marketing says. |
| 40 | **When files stop being enough** | FAST | The honest threshold: at ~26k tokens, plain full context wins outright; at ~115k, memory systems win by 11-24 points; past a million, long context fails on its own. Scale when you cross the threshold, not before. And treat the vendor benchmarks with care — an audit of the standard one found 6.4% of the answer key wrong and the judge accepting 62.81% of deliberately wrong answers. |
| 41 | **Skills that improve themselves** | TEACH | A persistent wiki plus executable skills: a 9B model with skills (47.4%) beats a 27B model without (39.4%) — the written artefact carries the gain, not the parameters. Plus the practice: `lessons.md`, a wrap-up skill, ablation. |
| 42 | **The distribution nobody is optimising yet** | TEACH | Three measured facts, and the shape they make. **Tiny**: AI assistants are still *"less than 0.15% of total visits"* (Semrush, 50,000+ sites, all of 2025), and Google remains ~88% of referral traffic. **Best-converting**: Adobe, across a trillion-plus visits to US retail sites, measures AI-referred visits converting **60% higher** than non-AI traffic, with that traffic up 62% year over year. **Fastest-growing**: AI traffic grew 66% in 2025, outpacing every other channel. That profile — tiny, best-converting, fastest-growing — is exactly the case for **an automated weekly agent rather than a headcount**. Scheduled runs are first-party documented in Claude Code and ChatGPT; the practitioner's revenue projection stays a labelled anecdote on top of this. |
| 43 | **The meta-skill** | TEACH | WRAP. Spotting which problems in your domain just became computationally tractable — *"probably the skill to have optimized for"* (**US spelling — the quote is graded character-by-character; "optimised" fails the gate**). Intuition: *the edge is not the model everyone has; it is noticing, first, what it just made possible.* |

**Steal**: pick one thing that was intractable 12 months ago and re-test it this week.

---

## Part 4 — WRAP

| # | Slide | Pace | Content |
|---|---|---|---|
| 44 | **The intuition to keep** | TEACH | Four lines, one per chapter, plus the spine. *The trend line is not the asset. Your codebase decides whether AI compounds. One writer, many readers. Loops hill-climb; you still choose the hill. Written knowledge is the asset that compounds.* |
| 45 | **Threads to pull** | TEACH | Named, honest pointers: the orchestration failure-mode table · the verified-vs-self-reported R&D two-by-two · the memory threshold data · Epoch's capability index · the eval-maturity material. Each maps to a research report we can share. |
| 46 | **Questions** | — | Conversation cards: *What would you put in a loop? · What is your single-agent baseline? · Where does your company's written knowledge live? · What just became tractable in your domain?* |

---

## Before you speak — the six things not to say

1. **Not** "labs trained on METR / it is overfit." Say **outgrown**, in METR's own words. Nobody has shown contamination.
2. **Not** "April 2026" as the break date. April is the curve's *last honest reading*; it broke publicly on 26 June with the GPT-5.6 Sol evaluation.
3. **Not** the $8bn Claude Code revenue figure — it traces to no primary. Use $2.5bn and **say it is from February**.
4. **Not** "X% of all commits" as a point. It is a **range**: 17.8% of push events, ~6-18% of commits, because nobody has the commit denominator.
5. **Not** "repositories were damaged" in the Hugging Face incident. Nothing shipped.
6. **Not** "graph engineering is the evolution of context engineering." It is a rename, and it means workflow-as-graph, not knowledge graphs.

7. **Never say "Terminal-Bench" without the version and the operator.** Three incompatible numbers are in circulation: 51.8% (TB 4.0), 82.0% (Berkeley RDI), 89.5% (TB v2.1 via Artificial Analysis).
8. **Not** "plain files beat every memory product." Say *in the same range as, and above full context* — the superlative depends on one vendor's measurement of a competitor who publicly disputes it.

Plus: a fitted ceiling is a model output — say *"the fits say"*, never *"it will be"*.
And the full per-figure list, with the exact quote each one is graded against, is in
`numbers-sheet.md` — that is the page to read the night before, not this one.

---

## Appendix (authored, shown on demand)

Sovereignty · data hygiene · LLM-as-judge · the five orchestration patterns in full · observability
surfaces · the harness slides in depth (thinking effort, preview panel) · the ownership-math card ·
watermarking · **the two-lags card** if the local-inference question comes up.

**The two-lags card, corrected**: the r/LocalLLaMA ~24.8-month cloud-to-laptop claim is
**dropped** — unverifiable, and every independent measurement of the 2025-2026 regime puts the
lag between **3 and 12 months**, a factor of 2 to 8 lower. Say four months for open-weights
parity, and treat it as a lower bound.

Two briefs were never run and stay as briefs: `claude-watermarking-provenance` and
`founder-equity-expected-value`. Both are conversation-dependent appendix cards; if either
comes up on the day, the honest answer is "I have not verified that, I will send it to you."

## Decisions taken (2026-09-01)

1. **Demos: IN, two of them.** Grill Me (slide 15) is launched on slide 14 and revealed on 15 — tested at 3m51s to first round, so it must never be run cold. Memory files (slide 39) is instant and carries no risk. Both tested on this machine; staging, commands, safety checks and fallback in `demo-runbook.md`.
2. **Boris Cherny: dropped.** No primary linkable source for the loops claim. The two-builders framing stands on Steinberger plus Anthropic's own loops post, which documents `/loop` directly.
3. **Chapter 5 order: kept** — memory before distribution, building from what they own to what they can reach.
