<!-- ABOUTME: 80/20 extraction of the Anthropic "Build Agents That Run for Hours" workshop, with concrete integration proposals into the Heuritech "AI Agents — From Theory to Loops" deck. -->
<!-- ABOUTME: Primary first-party Anthropic source on long-running agents via loops; corroborates and partly supersedes the secondary PostHog loops framing in the deck. -->

# Anthropic Workshop — "Build Agents That Run for Hours" — Insights & Deck Integration

## Header

- **Title:** Anthropic Workshop: Build Agents That Run for Hours
- **Speakers:** Ash Prabaker & Andrew Wilson — Applied AI team, Anthropic (Andrew: solution architect, London; Ash: harness/post-training experiments)
- **Source:** https://www.youtube.com/watch?v=mR-WAvEPRwE — AI Engineer conference (first session), ~75 min (talk ~45 min + ~30 min Q&A).
- **X repost:** reposted by @0xMovez — framed as "Anthropic engineers showed how to build agentic systems that run for days using loops; >30% of Anthropic's code is written by loops." NOTE: the ">30% of code written by loops" line is the X poster's framing, not a verbatim claim in the talk. The talk's actual claim is stronger and more specific: *"almost all of Cloud Code is being written by Cloud Code"* (Boris Cherny quote), and runs of *3–5 hours typical, up to ~30 hours* producing fully-featured apps. Treat ">30%" as a paraphrase; cite the verbatim claims below instead.
- **One-line gist:** Anthropic builds agents that run for hours-to-days by pairing a frontier model with an evolving *harness* — and the current state-of-the-art harness is an adversarial **planner / generator / evaluator loop** with separate context windows, file-system state, and the agent (not the engineer) doing verification.

---

## The 20% that matters (80% of the value)

### A. Why long-running agents are hard — the three failure buckets

This is the problem statement and it is unusually crisp (Andrew):

1. **Context.** Context windows are finite → a new session is *"amnesia, the agent has to start from scratch."* Three named pathologies:
   - **Context rot** — *"less coherence as you're getting deeper into that session."*
   - **Context anxiety** — *"the model actually exhibits what's called context anxiety… it gets kind of nervous as it reaches the end of its context window, and it just quickly hurries up to finish what it's doing."*
   - (and amnesia between sessions → you need a **memory** component).
2. **Planning.** Models are *"not that great at planning out of the box"* — they try to one-shot everything, or *"build half a feature and then stop,"* or run out of context and leave a half-built app.
3. **Self-judgment (the least intuitive, most important).** Models are *"really bad at judging their own output."* Sycophancy applies to code: it looks at a half-baked feature and says *"yeah, okay, that looks done"* and moves on — or builds a button with no backend behind it but *"it looks like the feature is done."*

> Memorable: **"deterministically bad in an undeterministic world… it's better to fail predictably than it is to succeed unpredictably."** (Andrew, on the Ralph loop philosophy.)

### B. Two levers: the model AND the harness (they co-evolve)

- **The model lever** = baking capability into the weights. The METR-style chart: minimal-scaffold autonomy at 50% task completion went from **~1 hour (Opus 3.7)** to **12 hours (Opus 4.6)** in about a year.
- **The harness lever** = the scaffolding around the model (the Agent SDK primitives: core agent loop, tool use, MCP, subagents, CLAUDE.md / skills / slash commands, permission system).
- **The key meta-insight** (load-bearing for the deck): *"the harness doesn't just disappear as the models get better. It's really evolving as the models change over time… you find the gaps in the model, fill that in with the harness, then you train the model on using that aspect of the harness, and maybe at some point you remove that entirely."* Every model release shipped **with** harness changes — *"these things are co-evolving together."*
- The frontier framing: **"the frontier doesn't really shrink, it just moves."**

### C. The history → what each release unlocked for long runs

A compressed timeline, useful because each step maps to one harness concept:

- **Sonnet 3.5 / artifacts + computer use + MCP** — first model that could *verify* (look at what it built and iterate); computer use (screenshots, clicking) and MCP (tool use).
- **Sonnet 3.7 / Claude Code research preview (Feb 2025)** — explicit goal: *"to better understand how developers use Claude for coding to inform future model improvements"* — i.e. the harness as a data-collection scaffold for the next model.
- **Opus 4 / Sonnet 4 + Claude Code GA + Claude Code SDK** — better self-context-management, less reward hacking.
- **Ralph Wiggum technique (Jeffrey Huntley, July 2025)** — prompt fed to the Claude Code CLI on a loop until tasks complete; phases: plan → break into features → pick one → fresh context window → repeat. Anthropic shipped its **own Ralph plugin** (runs in a *single* session relying on **compaction** rather than fresh context windows; `max iterations` + a `safe word`; a **stop hook** intercepts Claude's stop and continues until exit criteria).
- **Sonnet 4.5 + Claude Code 2.0** — model became **context-aware** (tracks tokens consumed, manages its own context); **checkpoints** (rewind to earlier session state); SDK renamed **Claude Code SDK → Agent SDK** (*"much more general purpose than just for coding"*). Runs ~**30 hours**.
- **Haiku 4.5 + Opus 4.5** — subagents became **economical**; Opus 4.5 became good at **planning**. Pattern emerges: **Opus 4.5 for planning, Sonnet 4.5 as the workhorse executor.**
- **Skills** — *progressive disclosure*: only the **front matter** loads up front (not all tool descriptions), the body loads when instantiated, with references to code that can run deterministically. **Programmatic tool calling** — write code on the fly to run a series of tool calls and get only the final result back, instead of pulling every intermediate result into context.
- **Opus 4.6 / Sonnet 4.6** — Sonnet 4.6 = "Opus-level intelligence at Sonnet price" (the new workhorse); Opus 4.6 = *"very much an agentic model"*, jumped the meter from **~4h to 12h**. Shipped **agent teams** (subagents that **communicate with each other**, not just report to the main agent), **server-side compaction** (*"these models can now just run indefinitely, compaction happens server-side"*), and **1M context GA**.

> Anecdote anchor: tasks that took ~20 min on older models now build **fully-fledged apps**; *"they can run typically we're seeing like 3 to 5 hours"* for a really fully-featured app (up to ~30h observed).

### D. The first long-running harness (Nov blog post) — the explicit recipe

Human gives a vague one-liner (*"write me a browser"*, *"create a Slack clone"*). Then:

1. **Initializer agent** breaks the prompt into **persistent artifacts**:
   - a `featurelist.json` of N features — **JSON specifically** because *"the models might overwrite markdown files, whereas they're less likely to just overwrite JSON files"* (concrete do).
   - a **progress file**, a **git repo**, an **init script**, and a per-feature **pass/fail flag**.
2. **Harness loop**, each iteration in a **fresh context window**:
   - get bearings (pwd, read progress file), run the **init script / smoke test** (so it doesn't re-derive how to boot the server every time),
   - **pick exactly ONE feature** that hasn't passed,
   - implement it, **run real tests / a verification loop** (Puppeteer, *"much like a human would"*),
   - on pass: **git commit** + flip the feature flag to "passes",
   - continue in a fresh context window until all features pass.

Concepts layered here: **fresh context windows · persistent artifacts · verification loops · strong up-front planning.**

### E. State of the art — the adversarial planner / generator / evaluator loop (the meat)

The core idea, *"shamelessly stolen from GANs"* (Ash):

- A **generator** builds; an **evaluator** grades; **adversarial pressure** between them. **Separate context windows, separate system prompts, separate jobs** for each.
- The evaluator *"isn't just reading diffs — it's actually using Playwright to open live pages, click around, try things out"* and hands a **critique** back to the generator. Loop continues. Contrast with what most people do: *"one Claude Code session, telling it to check its own work."*

**Why a separate critic beats self-review (the load-bearing argument):**
> **"Tuning a standalone critic to be harsh is actually very tractable, but tuning a builder to be somewhat self-critical is not."** Analogy: *"it's very easy for me to critique a lovely piece of artwork or a fine meal, much harder for me to actually go ahead and paint that or cook that meal myself. So what we're doing here is exploiting the gap between the ability of an LLM to be a critic versus a generator."*

**Grading subjective quality (taste is gradable):**
- *"Most people say you can't grade taste, but we think you can if you have a strong enough opinion on it and you just write it down."*
- A **rubric of four criteria: design, originality, craft, functionality** — **weighted toward design + originality** (because Opus 4.6 is already good at functionality). The enemy: *"purple gradients, general AI slop aesthetics."*
- Calibrated with **few-shot reference sites** so *"the evaluator's taste converges on our own."* You can show it *"this is what a read-before prompt looks like, this is what AI slop looks like"* — and it **generalizes**.
- Runs observed: HTML/CSS-only apps, **~4 hours, 5–15 rounds**.

**The unique behavior a separate critic buys — pivoting:**
> If the generator keeps scoring low on one criterion (e.g. originality), *"this GAN-style harness will just throw the whole thing out and try again from scratch,"* whereas a single-pass generation or a Ralph loop *"keeps trying to patch the same thing."* This **course-correction over long horizons** is unique to splitting roles.

### F. The planner — high-level on purpose; and the "contract" negotiation

- Add a **planner**: takes a one-line prompt, breaks it into a **deliberately high-level spec / series of sprints**. Crucially it **does NOT plan granular technical details** — because *"when it does make an error, it's going to cascade through every single one of these sprints and magnify errors over a multi-hour time horizon."*
- The org analogy: *"a very simple PM, IC, and QA org structure… we didn't invent this, we just gave each role its own context window."*

**The key innovation Ralph never had — the contract:**
- Before the generator writes a single line, **generator and evaluator negotiate what "done" means**, via **files on disk**: generator proposes "I'll build X, verify by testing Y", evaluator pushes back *"the scope is too big, those tests are too weak, you've missed XYZ edge case."* They iterate (one writes markdown, the other reads) **until both agree**.
- The evaluator then grades **against the negotiated contract, not the planner's original one-shotted spec.** This bridges fuzzy user-stories → *"tangible, testable assertions"* without the planner over-specifying.
- *"This is the key innovation that the Ralph loop never really had. It had a fixed plan.md, but nobody on the other side is arguing with the main loop."*

**Concrete granularity number:** for one app, the negotiated contract had **27 contract criteria**. *"That's the level of granularity you really need to make findings actionable. Vague criteria → vague critiques → the generator just shrugs. Granular criteria → the agent knows 'I need to fix this exact line.'"*

### G. The retro-game-maker case study (solo loop vs harness) — the proof

Same prompt (*"build a retro game maker"*), same model:

- **Solo loop:** opening screen + sprite editor *"look fine"* — *"the bait"* — but **play mode is dead**: entities render but arrow/space keys do nothing. *"The agent really didn't have any idea what it meant to play a game and actually succeed… it looks done on the surface, but when you push it to its limits it just failed."*
- **With the harness:** ~**$200, 6 hours.** Self-named "Retro Forge", 54-color palette, an **AI-level-assistant feature the planner invented** from a vague spec line (recursive: the harness built an AI feature into the app it was building), a live **debug HUD** *"clearly to make life easier for the evaluator"*, working physics, collisions, playable. *"The difference between this output and the previous output is entirely just scaffolding. It's a very simple loop ultimately, but the results are quite startlingly different."*
- Bugs the **using**-the-app evaluator caught that CI would miss: **FastAPI route-ordering** (passes unit tests, breaks in prod), a **delete-key boolean-logic bug**. *"These are things which were only caught because the evaluator's actually using the app."*

### H. The hard truth — Claude is a bad QA agent out of the box; you tune it by reading traces

- *"Out of the box, Claude is a really, really bad general QA agent."* Same sycophancy/generosity bias as LLM-judge systems: early runs, the QA agent *"would find a bug and be like 'fix it later, might take 2 weeks' and just be done with it."*
- The fix is **not more experiments** — it's **reading traces**:
> **"The primary debugging loop was this, and not necessarily running more experiments. It was reading what the agent actually did, finding where its judgment diverged from ours as humans, and then tuning the prompt for that. It was the same muscle as reading a stack trace."**
- Tooling tip: **pipe agent transcripts to files, grep them with another agent, or have another agent play through them and update the prompts** — *"closing the loop even on just building the harness out."*
- On traceability generally (Q&A): *"a lot of it is just reading through traces by hand… by far and away the best approach that we use internally is just reading the traces by hand. Only then do you truly get to relate to what the model is trying to do."*

### I. Adapting the harness as models improve (the ablation discipline)

The single most deck-relevant theme — what to **delete** as the frontier moves:

- **Context resetting between sessions → dropped entirely.** Opus 4.5 had *"really bad context anxiety"*; **Opus 4.6 doesn't** (post-trained out). *"One continuous session and compaction was more than enough."*
- **Sprint decomposition** was *"really critical to getting Opus 4.5 to work"* but Opus 4.6 *"was able to hold a 2-hour continuous build coherently without being force-fed one feature at a time."*
- **Evaluator cadence:** was every sprint → now just at the **end of a one-shot generation**, then pass back. *"The harness is still the same, we're just simplifying the specific loops."*
- The lesson: *"our harness wasn't wrong — it was right for 4.5, the frontier moved, and we ran a simplified version."* Final SOTA setup = **planner / generator / evaluator core kept**, many sub-components ditched, **~half the cost** of previous runs.
- **File system as shared state** is the durable default: *"big fan of just using a file system for shared state instead of leaning on context windows for very long-running agents."* It's grep-able by another model, and the model doesn't overwrite JSON.

### J. The five things to remember (Ash's closing "take a photo" slide)

1. **Self-evaluation is a trap — use an adversarial evaluator.**
2. **Compaction ≠ coherence** — *"lossy summaries really drift."*
3. **Structured hand-offs and clean contexts** are good patterns.
4. **Don't assume subjective quality isn't gradable** — if you have a strong view, **write it down**.
5. **Sit with the model, read the traces** — *"only then can you really know what bits of a scaffold to delete, what bits to keep, especially as the frontier moves."*

### K. "You don't need our internal harness" — the DIY primitives (actionable)

- **auto mode** (Ash's favorite) — *"safe yellow"* instead of `--dangerously-skip-permissions`.
- **Custom subagents** as the evaluator/QA role — *"give it a harsh system prompt and a very detailed rubric."*
- **Playwright MCP** or **Claude for Chrome MCP** (more robust) for web apps; **computer use** for native apps. Vision is now good enough to *"identify overlapping text on elements."*
- **Skills** to package grading rubrics into the dev flow.
- **Hooks** to inject a human-in-the-loop stop condition when you want one.

### L. Notable Q&A nuggets

- **Is reading traces per-project or reusable secret sauce?** Goal is **reusable** — find *"the common patterns across the model's weak points"* (e.g. the front-end-design taste rubric generalizes well across web apps).
- **Dumb-zone / smart-zone & Ralph (with 1M context, ~100K "smart zone"):** With 1M GA + more agentic models, Opus 4.6 holds coherence in a **single long session with compaction**; multi-fresh-session Ralph vs single-session *"is still up to your use case and your evals."* Context rot is *"a temporary problem… a failing of today's models"* — Ash would *"be hunting for the model release and strip it out."*
- **Don't feed the generator's traces to the critic.** They tried it; it **muddies the two model streams**. Better: critic judges **output only** and says *"this is an issue"*, letting the generator reflect — otherwise *"it's very easy for the model to kid itself that something is working"* and that leaks into the evaluator. Hand-off pattern only.
- **Generator vs evaluator restart behavior (surprise finding):** 4.6 models were *"extremely willing to throw away everything, even after 10 passes, and start from scratch"* if they couldn't hill-climb the rubric — *a behavior never seen when the generator judges its own work* (it gets *"proud of its own work"*). So they didn't need a resume / human-in-loop intervention.
- **Greenfield vs brownfield:** the pattern is great for **greenfield**, *"quite opinionated"* (assumes a stack), and needs customization for **brownfield**. For brownfield, point the evaluator at the existing codebase + the spec and let it hill-climb. Broader brownfield play = automate the **whole SDLC**: autonomous monitoring → issue/feature request → PR agent → review → human merge.
- **Long-lived products (persisting state across days/weeks):** leave **breadcrumbs** for the next model/human — a **JSON log** (`tried this → evaluated → found bug → implemented fix → worked ✓`, timestamped) plus a **live-updating high-level docs file** (file structure). *"Those two files are more than enough for Claude Code and a human to come in and iterate."* Also: Claude Code now has **auto memory** that *"constantly memorizes little things as it goes."*
- **Agent teams vs explicit generator/critic:** generator-evaluator is *"a subset of the teams approach, not contradictory."* Claude Code runs on the same harness (Agent SDK), but Claude Code runs **on your machine** (you'd `caffeinate`), whereas the Agent SDK runs in a **cloud / sandbox environment** for long autonomous periods. Use Claude Code as the **testing ground** before building into the Agent SDK.
- **Measuring harness quality / "is it just a vibe check?":** specify **rubrics in extreme detail** at generator + evaluator level; you get a signal of where the model **started vs ended** on each criterion. *"Not super comparable across products, but very useful within a product or run."*
- **Empathize with the model.** The Claude-for-Chrome team literally *"closed our eyes and tried to navigate web pages"* — every 10s you open your eyes to a static page, then act blind. *"Really putting yourself in the shoes of the model is an empathetic skillset you need to develop."*

### Verbatim quotes to consider for the deck (quote exactly)

1. *"Almost all of Cloud Code is being written by Cloud Code, and it can run effectively for days at a time."* — Boris Cherny, quoted in the talk.
2. *"Tuning a standalone critic to be harsh is actually very tractable, but tuning a builder to be somewhat self-critical is not."* — Ash.
3. *"Most people say you can't grade taste, but we think you can if you have a strong enough opinion on it and you just write it down."* — Ash.
4. *"It's better to fail predictably than it is to succeed unpredictably."* — Andrew (on Ralph).
5. *"The harness doesn't just disappear as the models get better — it's really evolving… you find the gaps in the model and fill that in with the harness."* — Andrew.
6. *"Compaction doesn't equal coherence — lossy summaries really drift."* — Ash.
7. *"Read the whole thing. … It's the same muscle as reading a stack trace."* — Ash (on traces).

---

## Deck integration proposals

> General note: this Anthropic talk is a **first-party primary source** that directly covers the deck's thesis (long-running agents via loops). Where the deck currently leans on the **secondary PostHog article** ("Why we're bullish on loops"), this source can **corroborate or replace** that framing with stronger provenance. Cite added material as **`Source: Anthropic — Prabaker & Wilson, "Build Agents That Run for Hours" (AI Engineer, 2026)`**. Below, each proposal names the existing slide and the concrete change.

### Proposal 1 — NEW slide in the Loops section: the adversarial planner/generator/evaluator loop *(highest priority)*

**Where:** insert after **§22 Loops · Part 1** (the four ingredients), as **§22b**. This is the single biggest gap: the deck teaches loops abstractly (Goal/Context/Evaluation/Agent) but never shows the **concrete SOTA architecture** Anthropic actually runs.

**Proposed title:** *Planner / Generator / Evaluator — the loop Anthropic actually runs*

**Bullets:**
- Three roles, **three separate context windows + system prompts** — a PM / IC / QA org structure, each given its own head.
- **Generator builds; evaluator grades by *using* the app** (Playwright: opens live pages, clicks, screenshots, scores) — not by reading diffs.
- Why split? *"Tuning a standalone critic to be harsh is tractable; tuning a builder to be self-critical is not."* You exploit the **critic-vs-creator gap.**
- **The contract:** before any code, generator and evaluator **negotiate "done" via files on disk** — scope, tests, edge cases — and the evaluator grades against *that*, not the original spec. (The thing Ralph never had.)
- **Planner stays deliberately high-level** — granular plans make errors **cascade and magnify** over a multi-hour run.
- **Unique payoff:** the loop **throws everything out and restarts** when it can't hill-climb a criterion — a single Ralph loop just keeps patching.

**Diagram idea:** Planner → (one-line spec) → [Generator ⇄ Evaluator] negotiating a *contract.md* on disk, then Generator builds → Evaluator drives the live app with Playwright → critique back to Generator → loop; an arrow labeled "can throw it all out & restart" curving back to the start.

**Why:** This is the talk's centerpiece and the most actionable, novel content. It turns the deck's abstract "Evaluation: agents verify, not engineers" bullet into a real, named, reproducible architecture from the strongest possible source.

### Proposal 2 — Enhance §38 "LLM as Judge" → reframe as *adversarial evaluator*, corroborated by Anthropic

**Where:** existing **§38 LLM as Judge** (currently sourced to hamel.dev, majority-vote framing).

**Change:** keep the majority-vote / validate-the-judge mechanics, but **add the Anthropic adversarial framing as the headline**:
- *"Self-evaluation is a trap — use an adversarial evaluator"* (Ash's #1 takeaway) — promotes this from "noisy vote" to "separate the roles entirely."
- Add: out-of-the-box, Claude is a **bad QA agent** (generosity bias: *"fix it later, might take 2 weeks"*); you tune it by **reading traces**, not running more experiments.
- Add the do/don't: **don't feed the generator's traces to the critic** — it muddies the streams; critic judges **output only**.

**Why:** §38 currently teaches the *statistics* of judging; the Anthropic source supplies the *architecture* of judging (adversarial, separate context, output-only). They're complementary and this is first-party corroboration of the deck's "agents do the verification" thesis. **Corroborates** PostHog's Evaluation ingredient with concrete failure modes.

### Proposal 3 — Strengthen §22 "Loops · Part 1" Evaluation + Context bullets with primary sourcing

**Where:** existing **§22 Loops · Part 1 — the four ingredients** (PostHog-sourced).

**Change (no restructure, just upgrade evidence + add a cite):**
- **Evaluation bullet** → append: *"Agents verify by using the product, not by reading diffs — and a separate critic beats self-review (Anthropic)."*
- **Context bullet** → append the **file-system-as-state** rule: *"For long runs, keep shared state in files (JSON the model won't overwrite), not the context window."*
- Add a second source line on the slide: `+ Anthropic — Prabaker & Wilson (2026)` next to the PostHog cite.

**Why:** The PostHog article is a secondary blog; Anthropic is the primary actor PostHog is describing. Dual-citing raises authority and the file-system rule is a concrete, missing do.

### Proposal 4 — Enhance §15 "Memory" with the file-system / JSON / breadcrumbs rules

**Where:** existing **§15 Memory** (plain files → DB, markdown/JSON).

**Add bullets:**
- **Prefer JSON for state the agent must not clobber** — *"models might overwrite markdown files, they're less likely to overwrite JSON files."* (Direct, concrete, first-party.)
- **Breadcrumbs for the next session/human:** a timestamped JSON log (`tried → evaluated → found bug → fixed → ✓`) + a live high-level docs file (file structure). *"Those two files are more than enough for Claude Code and a human to pick up."*
- Note Claude Code's **auto-memory** (memorizes little things as it goes) as the productized version.

**Why:** The deck's memory slide is sound but generic. These are battle-tested, specific rules from the people who built it — and the markdown-vs-JSON detail is a genuinely surprising, citable nugget that corroborates the deck's "MEMORY.md / featurelist.json" instinct.

### Proposal 5 — Enhance §19 "Context Engineering" with compaction-≠-coherence + context rot/anxiety

**Where:** existing **§19 Context Engineering** (four blocks, progressive disclosure, finite window).

**Add to "A finite window" / failure-modes:**
- **Context rot** (coherence decays deeper into a session) and **context anxiety** (model rushes as it nears the limit) — named, vivid failure modes the deck currently lacks.
- **Compaction ≠ coherence** — *"lossy summaries really drift"* — the caveat to the deck's own progressive-disclosure optimism.
- Note **programmatic tool calling** + **progressive disclosure of skills (front-matter only)** as Anthropic's concrete context-saving techniques (the deck already teaches progressive disclosure for SKILL.md/MEMORY.md — this corroborates it by name).

**Why:** Adds first-party vocabulary (rot/anxiety) and an honest limit (compaction drifts) that make the context slide more credible to a technical Heuritech audience.

### Proposal 6 — Add an "adapting the harness as models improve" beat to §39 Meta-Improvement (or §I as a new advanced card)

**Where:** existing **§39 Meta-Improvement** (ablation already appears: *"try removing complexity, keep what survives the tests"*).

**Add bullets (this is the perfect primary example for the existing ablation point):**
- Anthropic **dropped context-resetting** between Opus 4.5→4.6 (anxiety post-trained out), **dropped forced sprint decomposition** (4.6 holds a 2h continuous build), **halved evaluator cadence** — **and runs ~half the cost.**
- The rule: *"the harness wasn't wrong — it was right for 4.5, the frontier moved."* The harness fills model gaps, then the model is trained on it, then you **remove** it.
- **"The frontier doesn't shrink, it just moves"** — quotable closer for the ablation card.

**Why:** The deck already preaches ablation in the abstract; this gives it a concrete, named, dated case study of Anthropic ablating their own harness across two model generations. Strongest possible illustration of "complexity must earn its place."

### Proposal 7 — Optional: corroborate §05 "Crazy Numbers" and reconcile the X "30% of code" claim

**Where:** existing **§05 Crazy Numbers** and the METR curve **§06**.

**Change:** add an Anthropic-sourced anchor and **explicitly correct** the X repost's framing in presenter notes:
- Quote: *"Almost all of Cloud Code is being written by Cloud Code… runs for days at a time"* (Boris Cherny) — a vivid, first-party version of the "AI writes the code" claim.
- METR anchor: **~1h (Opus 3.7) → 12h (Opus 4.6)** at 50% completion, minimal scaffold — matches the deck's METR curve and PostHog's "12-hour tasks / ~6× Opus 4". **Corroborates** the deck's §06 and §23.
- Presenter-note caveat: the ">30% of code written by loops" line circulating on X is a **paraphrase**, not a verbatim talk claim — don't put a hard "30%" number on a slide attributed to this talk.

**Why:** Keeps the deck's numbers honest and gives §05/§06 a first-party corroborating quote, while inoculating against repeating the X poster's imprecise stat.

### Provenance / corroboration summary (PostHog vs Anthropic)

- **Corroborates PostHog:** loops as the unit of long-running work; "agents do the verification"; subagents separate the loop driver from the work; harnesses maturing (compaction, skills+MCP, cloud execution); METR autonomy gains; Ralph as the basic loop. The Anthropic talk is, in effect, the **primary account** of much of what PostHog summarizes — safe to **dual-cite or upgrade**.
- **Goes beyond PostHog (net-new for the deck):** the **adversarial planner/generator/evaluator** architecture; the **contract negotiation** between generator and evaluator; **separate critic beats self-review** (the tractability argument); **rubric-based taste grading** (4 weighted criteria + few-shot calibration); **27-criteria granularity** rule of thumb; **read the traces** as the primary debugging loop; **JSON-not-markdown** for un-clobberable state; **harness ablation across model generations**; **don't feed generator traces to the critic.**
- **Mild tension with PostHog/deck framing:** PostHog (and §21) leans on the **Ralph loop** as the loop archetype. Anthropic explicitly positions Ralph as the **basic** tier and their **adversarial-contract loop** as the SOTA that *"Ralph never really had"* — and notes context-reset/fresh-window Ralph is being **dropped** as models improve. Worth flagging on §21/§22 so the deck doesn't over-sell Ralph as the endpoint.
