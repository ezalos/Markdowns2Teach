<!-- ABOUTME: 80/20 insight extraction from Phil Hetzel (Braintrust) "maturity phases of running evals" talk. -->
<!-- ABOUTME: Plus concrete proposals to fold the eval-maturity framework into the Heuritech "From Theory to Loops" deck. -->

# Insights — "The maturity phases of running evals" (Phil Hetzel, Braintrust)

- **Title:** The maturity phases of running evals
- **Speaker:** Phil Hetzel — Head of Solutions Engineering, Braintrust (prior: 12 yrs consulting, KPMG + Slalom, led Slalom's global Databricks unit)
- **Source:** https://www.youtube.com/watch?v=FB-MLPhL9Ms (AI Engineer conference)
- **Duration:** ~18 min
- **Gist:** Evals are not unit tests — they are a maturity continuum. You climb from documented vibe checks → automated LLM/code scoring fed by production traces → whole-trace + tool/state evaluation → advanced auto-discovery, and the whole point is a *flywheel*: capture production, find what broke, replay it offline as an eval, ship the fix.

---

## The 20% that matters (80% of the value)

### Why evals exist (the framing)
- Evals are **wholly in service to agent quality** — making sure the agent does what you expect "when confronted with real usage and real users."
- They play **defense** (reputational risk of an unkind/unhelpful agent; systems risk of an agent that costs too much money; compliance/legal risk if it "goes off the rails") **and offense** (knowing, with each tweak, *whether* and *how much* the agent improved).

### Core primitives (the mental model under everything)
- **Evals are NOT unit tests.** Unit tests are exhaustive; evals are not. Start **high-level, from the failure modes** of the agent (you or a subject-matter expert name them), and build evals around those specifically. You cannot enumerate everything that could go wrong — it's infinite, and you'd "spend all of your time writing tests and none of your time shipping."
- **Eval results don't need to be perfect — directional is fine.** LLM-as-judge won't score 100% every time; that's OK "as long as you're trending in the right directions."
- **An eval = three parts:** (1) a **Task** — the agent/prompt under test; (2) a **Dataset** — example inputs that initiate the task; (3) **Scoring functions** — that judge the utility/quality of the output.

### The maturity phases (in order — "more of a continuum than discrete")
You traverse these as your agent gets more complex: more complexity → more failure vectors → more failure modes to cover.

1. **Just getting started — vibe checks (documented).**
   - Starting with vibes is "not wrong" — "certainly better than nothing." You can't help but start here.
   - The one upgrade: **document while you vibe-check.** Run ~10 example inputs through the agent, and have a human — ideally a subject-matter expert who knows what a quality response looks like — give each output two things: a **thumbs up / thumbs down** AND, **more importantly, a written justification** for that call.
   - Why the justification matters: you are **extracting domain-specific knowledge out of the annotator's head** so you can later scale it via LLM-as-judge.
   - Tooling note: **don't hand experts a generic annotation UI** — make the annotation view very specific to their domain; it encourages good evaluation.

2. **Measuring to manage — scale the human judgment.**
   - Feed the thumbs-down + justifications through Cursor / Claude Code / Codex to **derive the actual failure modes**.
   - Once you know the failure modes, **automate the judgment** so you're not dependent on a few experts:
     - **LLM-as-judge** for subjective criteria — but "just because you put a robe and a cloak on an LLM, that doesn't make it inherently more trustworthy." **You must evaluate the judge too.**
     - **Deterministic / code scorers** for objective failure modes — e.g. **fail the eval if too many tool calls, or too many tokens.** You don't *have* to use an LLM judge.
   - The dataset shifts: **start pulling production (or at least UAT) traces into the eval dataset.** "Don't think about evals as running tests. Think about evals like *re-running production*" — because you ultimately want confidence in production.
   - **The flywheel (the single most important idea):** capture agent traces in production → understand what went wrong (human or automated) → bring those examples back to an **offline experimentation environment** → re-run production through an eval → use it to guide which direction to improve. That's evals playing offense.

3. **Accounting for complexity — tools, traces, and external state.**
   - Two kinds of tool calls: **context-gathering** (read data, inject into the LLM) vs **CRUD** (create/read/update/delete on a DB or external system). Both carry a lot of quality lift and a lot of new failure surface.
   - You stop evaluating just the **final output** and start **evaluating the entire trace** — every step the agent took — sometimes targeting evals at **individual tool / MCP calls.**
   - **The hard, not-fully-solved problems with CRUD agents offline:** (1) it's hard to **represent the external-system state** as it was at the time the eval input was created; (2) you don't want to run CRUD against production and **overwrite production data**.
   - Emerging techniques he names:
     - Use **mock-level APIs** to approximate a real production environment.
     - **Agent traces can be arbitrarily large** (unlike app tracing), so **cram system state into the trace itself** and inject it into the task — instead of standing up a whole test infrastructure, encapsulate state in the trace.
     - **Point-in-time / timestamp queries:** if a system supports it (e.g. a versioned vector DB), query it *as of* the moment the input was captured, to faithfully represent original state.

4. **Advanced eval techniques (the "what's next").**
   - **Topic modeling at scale** over production to **auto-discover failure modes** (not hand-named anymore).
   - **Evals via CLI automation** — Claude Code + the eval provider's CLI to run evals in an automated way.

### Concrete heuristics / numbers / rules of thumb
- Vibe-check sample size: **~10 example inputs** to loop through at the start.
- Two annotations per example: **thumbs up/down + a written justification** (the justification is the load-bearing part).
- Deterministic fail conditions worth coding: **too many tool calls**, **too many tokens**.
- **Always validate the judge** against a human-labeled ground-truth set — and because LLM-judge outputs are **discrete**, building that ground-truth set is easy.
- On the deterministic-vs-LLM-judge debate (audience Q): **embrace LLM-as-judge for subjective things** (subjectivity "is why we love agents so much") **but eval the judge heavily** so it aligns with what a human would decide — "you would eval the eval as an eval."

### Common mistakes he calls out
- Treating evals like **exhaustive unit tests** (infinite, kills shipping velocity).
- Demanding **perfect** eval scores instead of accepting directional signal.
- **Trusting an LLM judge blindly** without validating it against human labels.
- Vibe-checking **without documenting** the thumbs + justification (you lose the domain knowledge you need to scale).
- Handing experts a **generic annotation UI** instead of a domain-specific one.
- Running **CRUD evals against production** / not representing external state, so offline runs are unfaithful.

### Verbatim quotes
- "Don't think about evals as running tests. Think about evals like re-running production."
- "Just because you put a robe and a cloak on an LLM, that doesn't make it inherently more trustworthy."
- "Evals are not unit tests… You would spend all of your time writing tests and none of your time shipping, which is not productive."
- "You would eval the eval as an eval."

---

## Deck integration proposals

The Heuritech deck already has the *engineering* view of evaluation (Step 3 Evaluate, Step 4 Observability matrix, Step 5 Improve, the LLM-as-judge card, and "Evaluation" as one of the four loop ingredients). What it is **missing** is a **maturity/progression view** — the idea that evals are a continuum you climb as the agent gets more complex, and the **flywheel** that connects production back to offline evals. Phil Hetzel's talk slots in cleanly as the "how eval practice matures" layer on top of the deck's "how to build one eval" layer.

### Proposal 1 — NEW slide: "Evals mature in four phases" (place right after Step 4 Observability, slide 31)
*Why here:* the Observability matrix (slide 31) is the deck's strongest eval artifact but it's presented as a single static technique. Hetzel's continuum reframes that matrix as **phase 1–2 of a longer journey**, which a technical Heuritech audience (who will run CRUD/tool agents) needs to hear. It directly extends the Observability slide forward in time.

- **Eyebrow / Title:** "Eval maturity · Evals are a continuum, not a checkbox"
- Bullets:
  - **Evals are not unit tests** — start from named failure modes, not exhaustive coverage. Exhaustive = infinite = you never ship.
  - **Phase 1 — Documented vibe checks:** ~10 inputs, a human (ideally an SME) gives thumbs up/down **plus a written justification.** The justification is the asset — it's domain knowledge you'll scale later.
  - **Phase 2 — Measuring to manage:** turn justifications into failure modes; automate scoring with **LLM-as-judge** (subjective) + **code scorers** (objective: too many tool calls / too many tokens).
  - **Phase 3 — Accounting for complexity:** evaluate the **whole trace**, target evals at individual **tool / MCP calls**, mock external systems, snapshot state for offline CRUD evals.
  - **Phase 4 — Advanced:** topic-modeling production to **auto-discover failure modes**; evals run from the CLI.
  - Takeaway: *results don't need to be perfect — directional is enough.*
- **Diagram idea:** a rising staircase, four steps, x-axis "agent complexity", y-axis "eval rigor": Vibes → Automated scoring → Whole-trace/state → Auto-discovery. Annotate step 1 with "thumbs + justification", step 3 with "mock APIs · point-in-time state".
- **Source on slide:** "Source: Phil Hetzel, Braintrust — 'The maturity phases of running evals' (AI Engineer)."

### Proposal 2 — NEW slide OR enhance Loops · Part 1 (slide 22): "The eval flywheel — re-run production, don't run tests"
*Why here:* slide 22's **Evaluation** loop ingredient says "agents do the verification, not engineers" — but it doesn't say *where the eval data comes from*. Hetzel's flywheel is exactly the missing piece: the loop's self-verification is fed by **captured production traces replayed offline.** This makes the "Evaluation" ingredient concrete and ties the deck's Loops section to the Observability/method section.

- **Eyebrow / Title:** "The eval flywheel · evals = re-running production"
- Bullets:
  - **Capture** agent traces in production (or UAT).
  - **Diagnose** what went wrong — human annotation or automated tooling.
  - **Replay offline** — pull those traces into the eval dataset and re-run them as evals.
  - **Improve** — the scores tell you which direction to push the agent; ship the fix.
  - Key line: *"Don't think about evals as running tests. Think about evals like re-running production."* — Phil Hetzel, Braintrust
  - This is what makes the loop's **Evaluation** ingredient run unattended: production feeds the verification.
- **Diagram idea:** a circular flywheel — Production traces → Diagnose (human/auto) → Offline eval replay → Improve → back to Production. Overlay it on the existing four-ingredient loop so "Evaluation" visibly pulls from production.
- **Source on slide:** Phil Hetzel, Braintrust.

### Proposal 3 — ENHANCE the LLM-as-Judge slide (slide 38) with "validate the judge"
*Why here:* slide 38 already nails judge *noise* (sample 3–5, majority vote, Haiku, ≥80% agreement against your labels — already aligned with Hetzel). His one extra, quotable reinforcement is worth adding as a one-liner: a judge isn't trustworthy by default. This is a low-cost, high-credibility add (external practitioner corroborating the deck's existing rule).

- Add one bullet + the quote to the existing slide:
  - "**A judge is not trustworthy by default** — *'putting a robe and a cloak on an LLM doesn't make it more trustworthy'* (Phil Hetzel, Braintrust). Always eval the judge against human labels — and because judge outputs are **discrete**, building that ground-truth set is cheap."
- *Why it strengthens:* the deck's ≥80%-agreement rule currently cites hamel.dev only; a second independent practitioner (Braintrust) saying "eval the eval as an eval" hardens it and gives a memorable line for the stage.

### Proposal 4 — ENHANCE Step 4 Observability (slide 31): forward-pointer to whole-trace evaluation
*Why here:* the Observability matrix evaluates **final outputs** (criteria × examples). Hetzel's phase-3 insight is that once agents do **tool/CRUD work**, you must evaluate the **whole trace**, sometimes per tool/MCP call. Adding a single forward-pointing bullet keeps the slide honest about its scope and sets up the new maturity slide (Proposal 1).

- Add one bullet:
  - "This matrix scores **outputs.** Once your agent calls tools and external systems, you also score the **whole trace** — even individual tool / MCP calls — and you must reproduce external **state** offline (mock APIs, point-in-time queries). *(see eval-maturity, Phase 3)*"
- *Why it strengthens:* the Heuritech audience builds real tool-using agents; the current slide silently assumes a single-shot output. This closes that gap and threads into Proposal 1.

### Recommended sequencing
Insert **Proposal 1** as a new slide after 31 (Observability) and **Proposal 2** as a new slide inside the Loops section after 22 (or fold into 22 if slide budget is tight). Apply **Proposals 3 and 4** as in-place one-line enhancements. Cite "Phil Hetzel / Braintrust" on every added or enhanced slide.
