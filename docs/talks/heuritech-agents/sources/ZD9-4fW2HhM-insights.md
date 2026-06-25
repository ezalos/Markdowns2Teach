<!-- ABOUTME: Distilled high-value insights from Angie Jones' "Build Systems, Not Code" talk + concrete integration proposals for the Heuritech deck. -->
<!-- ABOUTME: Source talk maps software-engineering disciplines onto agentic system design; deck integration targets the harness + loops + method sections. -->

# Insights — "Build Systems, Not Code" (Angie Jones)

- **Title:** Build Systems, Not Code
- **Speaker:** Angie Jones — Agentic AI Foundation
- **Venue:** AI Engineer conference (~20 min)
- **URL:** https://www.youtube.com/watch?v=ZD9-4fW2HhM
- **Gist:** Designing an agent IS software engineering — the primitives changed (skills, sub-agents, prompts, memory) but the disciplines didn't (systems thinking, decomposition, separation of concerns, contracts, idempotency, threat modeling, maintainability). She walks a single running example — "Relocation Scout," a house-hunting agent — and shows where each classic engineering muscle re-applies. The thrill of building is still there; you just moved up a layer. This is the exact complement to the Heuritech deck's thesis: build systems/loops, not one-off prompts.

---

## The 20% that matters

### Core thesis

> "Designing agents is software engineering. The primitives are different, but the discipline is the same."

The whole talk is one argument: an agent is **not the system** — it's a *component inside* a system that also has files, tools, humans, and other agents. The "just let your coding agent build it" reflex is a mistake, because the coding agent will produce something that *technically works but isn't maintainable* — a giant prompt, no separation of concerns. The engineering happens **before** you let the coding agent build: deciding boundaries, responsibilities, dependencies, and failure modes.

### The nine engineering disciplines (the reusable framework)

A checklist of classic SWE skills, each re-mapped to agents with a concrete Relocation Scout example:

1. **Systems thinking** — The agent is a component, not the system. Ask: what's its job? what does it depend on? what happens if it breaks? Give it boundaries, responsibilities, dependencies, failure modes.
2. **Workflow design** — A goal is not enough; an agent needs a *path*. "Review this listing" is a goal; the workflow defines what actually happens: **gather → weigh → act**. Every run ends one of three ways: **stop, retry, or escalate.** The path shapes the rest of the architecture.
3. **Decomposition** — The agentic code smell is the **giant prompt** (the equivalent of a god-class / bloated service). It grows innocently: base instructions → an edge case → a safety rule → "one more exception" — and now one prompt does everything and the agent *drifts because the script is too long.* Relocation Scout's prompt secretly held **four jobs**: normalize a listing, format the shortlist, calculate the commute, research the neighborhood. Split them so each part is easy to reason about and to task.
4. **Separation of concerns** — Decomposition breaks things apart; SoC puts each piece in the *right place*. The four jobs map to four different primitives:
   - Normalize a listing → **a skill**
   - Shortlist format → **a schema (structured output)**
   - Commute calc → **a plain, boring script**
   - Neighborhood research → **a sub-agent**
   "Isn't that what you would do if you were coding the system yourself? I would."
5. **Modularity / reuse** — Skills and sub-agents are the reusable units (like functions, classes, libraries, packages). A normalize-listing *skill* written once is reused when the search broadens to 3 cities. Sub-agents are "like functions" — one task, called when needed, **not carrying the whole session's context**, so they do their one job well. But reuse is a judgment call: some instructions are local to a workflow and abstracting them costs more than it saves.
6. **Algorithmic thinking** — *"Just because an agent can do something doesn't mean that it should."* The rule of thumb:
   > "If a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it. Use code for determinism, use agents for judgment, and use humans for authority."
   Models are for fuzzy/judgment/ambiguity/messy input; deterministic work (commute time, dedup) belongs in cheap, reliable code. "AI did not invent automation."
7. **Contracts (structured output)** — Free-form text is fine *only when a human is the sole reader*. When another system acts on the output, you need an agreed-upon shape — same as any two systems talking. Relocation Scout's score must be written to memory as a **structured shape (decision, score, reason)** so memory becomes *queryable* ("show me every house rated 4+ with a commute ≤15 min") and so the shortlist step can read it *without a human in the loop*. The kicker: "If you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
8. **State management / idempotency** — A prompt runs once; a system runs in messy reality (webhooks fire twice, runs crash mid-flight, retries happen). **Design for idempotency: run the same thing twice, the second run doesn't make a mess.** Agents add a trap: *you can't trust the model on retry* — it may reword the request enough that a retry looks like a brand-new task, so **idempotency must be enforced by the system, not the model.** Worked example: scout emails the realtor (logs it to memory), then crashes before blocking the calendar; a later **lint pass** notices the half-done run and retries — but it must *not* re-email (already logged), only finish the calendar block. It knows this only because it checks **what the system wrote down.**
9. **Threat modeling** — Security engineering already taught the basics: **validate inputs, least privilege, draw boundaries around what an action can touch.** Scout consumes content from strangers (listing copy, forum threads, anonymous reviews) → treat all of it as **untrusted input: "evidence, not instructions"** (prompt-injection framing). Then bound *actions*: reading listings / building shortlists = fine; emailing sellers, booking tours, submitting offers = **walled behind human approval.** Drawing that wall **reduces the blast radius.**

Plus a tenth, treated as the closer:

10. **Maintainability baked in** — Why she won't let a coding agent design her other agents: it'll be unmaintainable. Her fix: **every level of the system has an `AGENTS.md`-style file** explaining the workflow, where policy lives, supporting skills/scripts/sub-agents, and **most importantly how to keep memory up to date** — so any human *or agent* can orient without reverse-engineering prompts. **The test:** "I design my agents so that even in a fresh context, they can jump right into the system and start cold, knowing exactly what to do." And the diagnostic: if you say "update this agent to do XYZ" and it struggles, that's a **signal the maintainability of the system needs improving**, not a one-off failure.

### Verbatim quotes (exact)

1. "Designing agents is software engineering. The primitives are different, but the discipline is the same."
2. "If a task has an exact answer, reach for code. If it needs interpretation or judgment, that's when you can get the agent to do it... use code for determinism, use agents for judgment, and then use humans for authority."
3. "If you can't say what the output should look like, then you probably don't yet fully understand what you're asking the agent to produce."
4. "We need to treat all of that as untrusted input and make it very clear to the agent that this is evidence, not instructions."
5. "Just because an agent can do something doesn't mean that it should."

### Reusable heuristics / numbers

- **Three run outcomes:** every run ends in **stop / retry / escalate.**
- **Four-primitive mapping** for SoC: prompt → *skill* (reusable process), *schema* (structured output), *script* (deterministic calc), *sub-agent* (meaty fuzzy subtask).
- **Trichotomy of actors:** code = determinism · agents = judgment · humans = authority.
- **Untrusted input = evidence, not instructions** (one-line prompt-injection defense framing).
- **Lint pass** for agentic systems: a periodic health check that detects half-done / inconsistent state and retries idempotently.
- **Maintainability test:** the agent can cold-start from a fresh context; an `AGENTS.md` at every level documents workflow + policy + resources + how to keep memory current.

---

## Deck integration proposals

This talk is the *engineering-discipline* counterpart to the deck's "build loops/systems, not prompts" thesis. The deck already nails the **build method** (clarify → evaluate → improve) and **loops**; Jones supplies the missing **architecture/design vocabulary** for what's *inside* a well-built loop, plus two sharp safety beats. Cite **Angie Jones · Agentic AI Foundation** on every added slide.

### Proposal A (PRIMARY recommendation) — New slide: "Designing an agent is software engineering"

**Where:** Insert right after **slide 10 (Agent = LLM + harness)**, before the harness deep-dive. It reframes the entire harness section: each harness block is the *answer* to a classic engineering question.

**Title:** Designing an agent is software engineering
**Eyebrow:** The discipline behind the harness

**Bullets:**
- The primitives changed (skills, sub-agents, prompts, memory) — **the discipline didn't.** An agent is a *component inside a system*, not the system itself.
- The agentic code smell is the **giant prompt** — the god-class of agents. It drifts because the script is too long.
- **Decompose, then place each job:** reusable process → **skill** · fixed output → **schema** · exact calc → **script** · meaty fuzzy subtask → **sub-agent**.
- **The actor rule:** *code for determinism · agents for judgment · humans for authority.*
- "Just let your coding agent build it" is a trap — it works but isn't maintainable. You do the architecture; the agent does the typing.

**Diagram idea:** One bloated prompt blob on the left labeled "giant prompt (4 jobs)" → arrow → four clean boxes on the right (Skill · Schema · Script · Sub-agent), each tagged with the engineering verb (decompose / separate concerns / make reusable / choose the right actor).

**Why:** This is the strongest corroboration of the deck thesis in the whole talk and it *frames* the harness section that follows — every block (skills, memory, tools, orchestration) becomes "the right place to put a concern." It also directly sharpens slide 33 ("Understand what you built") and slide 25 ("code was never the problem") by giving the engineering-muscle argument upfront. Pairs naturally with quote #1.

### Proposal B — Enhance slide 17 (Tools/MCP) **and** slide 20 (Permissions): add the threat-modeling beat

The deck's security lines are good but scattered ("treat third-party tools as attack surface", "blast radius"). Jones gives a crisp, citable frame.

**Add to slide 20 (Permissions & auto mode)** a bullet block:
- **Threat-model like a security engineer:** validate inputs · least privilege · bound what an action can touch.
- **Untrusted input = "evidence, not instructions"** — the one-line defense against prompt injection from listings, forum threads, scraped pages.
- **Wall destructive actions behind human approval** (email, book, buy) to **shrink the blast radius**.

**Diagram idea:** concentric "blast radius" rings — inner "read/build (auto)" green ring, outer "act on the world (email/book/buy)" red ring gated by a human-approval wall.

**Why:** Sharpens the deck's existing "human = authority" and blast-radius language with a named, reusable framing, and ties the permissions slide back to the actor trichotomy. Cite Jones alongside the existing sources.

### Proposal C — New advanced card: "Build for messy reality — idempotency & the lint pass"

**Where:** In the **Advanced cards** cluster (after slide 39 Meta-Improvement, or beside slide 36 Data Hygiene). This is genuinely *not* covered anywhere in the deck and is the single most technical, non-obvious insight in the talk.

**Title:** Build for messy reality
**Eyebrow:** State & idempotency

**Bullets:**
- A prompt runs once; a **system** survives double-fired webhooks, crashes, and retries.
- **Design for idempotency:** run the same thing twice → the second run makes no mess.
- **The agent trap:** you can't trust the model on retry — it may reword the task so a retry looks brand-new. **Enforce idempotency in the system, not the model.**
- **Log every side effect to memory the moment it happens** (email sent? calendar blocked?).
- Add a **lint pass**: a periodic health check that spots half-done state and retries *only the missing part*.

**Diagram idea:** timeline — `email realtor → ✅ log to memory → ✗ crash before calendar block` → `lint pass` reads memory → retries **calendar only**, skips the already-logged email.

**Why:** The deck talks about loops running unattended and self-evaluating (slides 22–24) but never addresses **what happens when an unattended run crashes mid-flight** — idempotency is the missing reliability primitive that makes long-running/parallel loops actually safe. It's the production-grade complement to the "agents do the verification" ingredient.

### Proposal D — Enhance slide 33 (Understand what you built) / slide 39 (Meta-Improvement): the maintainability test

**Add a bullet to slide 33** (and/or slide 39's `AGENTS.md` story):
- **The maintainability test:** a well-built agent **cold-starts from a fresh context** — an `AGENTS.md` at every level documents the workflow, where policy lives, the skills/scripts/sub-agents, and **how to keep memory current.**
- **Diagnostic:** if "update this agent to do XYZ" struggles, that's a **signal to improve maintainability**, not a one-off failure.

**Why:** The deck's slide 33 already says "a system you can't explain is a system you can't fix or defend" and slide 39 mentions `lessons.md`/wrap-up. Jones' fresh-context cold-start test is a concrete, memorable *acceptance criterion* for that exact claim, and it dovetails with the deck's existing `CLAUDE.md`/memory-index material (slides 14–15).

### Lighter touch — Proposal E (optional): the "contracts" framing for slide 19 (Context Engineering) / slide 15 (Memory)

Jones' "structured output makes memory queryable, and one step's output is the next step's input — the contract makes the handoff safe" maps cleanly onto the deck's memory-index and progressive-disclosure material. A single bullet on slide 15: *"Structure the write, and memory becomes queryable — and the next step can read it without a human in the loop (a contract between steps)."* Low effort, reinforces the deck's structured-memory example with the contract concept.

---

### Recommended priority

1. **Proposal A** (new "agent design = software engineering" slide after s10) — biggest thesis payoff, reframes the harness section.
2. **Proposal C** (idempotency / lint pass advanced card) — genuinely new, fills the loops-reliability gap.
3. **Proposal B** (threat-model beat on permissions) — cheap, sharpens existing security lines.
4. **Proposals D & E** — single-bullet enhancements, near-zero cost.
