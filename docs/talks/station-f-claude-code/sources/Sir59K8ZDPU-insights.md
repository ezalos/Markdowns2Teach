<!-- ABOUTME: 80/20 insight extraction from Frank Coyle's AI Engineer talk "Why Agentic Systems Need Ontologies". -->
<!-- ABOUTME: Feeds the Station F / Incubateur 42 talk (2026-09-02) on Claude Code & agentic best practices. -->

# Insights — "Why Agentic Systems Need Ontologies" (Frank Coyle)

- **Title:** Why Agentic Systems Need Ontologies — Frank Coyle, UC Berkeley
- **Speaker:** Frank Coyle — educator at UC Berkeley, ~30–35 years in computer science, expert-systems practitioner in the 1980s, early career in neuroscience; sites: frank-coyle.ai, codesupreme.ai
- **Channel:** AI Engineer (AI Engineer World's Fair 2026 talk — "5,000 people are here" [00:41])
- **Published:** 2026-07-23
- **URL:** https://www.youtube.com/watch?v=Sir59K8ZDPU
- **Duration:** 21:18 · ~322K views (as of 2026-08-31)
- **Local sources:** `videos/Sir59K8ZDPU.transcript.txt` (+ `.en-orig.vtt`, `.info.json`) — note: auto-captions mangle "W.V.O. Quine" and "OWL, the Web Ontology Language"
- **Gist:** Most agent failures (double refunds, payouts to the wrong party, invented statuses) are symptoms of one missing layer: a formal ontology sitting *outside* the model as logical guardrails. LLMs are probabilistic by nature — hallucination is the feature, not the bug — so the fix is neurosymbolic: keep probabilistic reasoning inside the loop, put logic outside it. Concretely: wrap a Claude tool-use loop with a validator — Pydantic checks types at the door, an ontology (typed entities, relationships, constraints in boring old RDFS/OWL) checks results at the ledger — and only then let the agent act. The catches that are painful to write in English become a few lines of logic.

---

## Structured summary

*(Timestamps below follow the video's own chapter markers, cross-checked against the transcript.)*

- **[00:12–02:18] Intro and an educator's philosophy.** CS degrees are no longer a guaranteed job "thanks to AI" — but 5,000 people at this conference say agents are the way to leverage the new universe. His teaching philosophy, from Sister Corita Kent (popularized by John Cage): "Nothing is a mistake. There is no win. There's no fail. There's only make" [01:23] — learn by making, not reading. Side advice: write by hand, engage the senses.
- **[02:21–04:04] Two lineages: agents and ontologies.** Agents descend from early AI — McCarthy, Selfridge, Minsky's *Society of Mind*, the 1956 Dartmouth coining of "artificial intelligence"; an agent = something that perceives, decides, acts [03:01–03:07]. Ontologies descend from Aristotle's categories of being, through Quine, to **Gruber (1993): an ontology is "a formal specification of a shared conceptualization"** [03:51] — "that's what we want to give to our agents: our conceptualization of our domains" [03:57–04:04].
- **[04:04–05:20] Neurosymbolic AI: guardrails around a probabilistic model.** The convergence of probabilistic LLMs with formal representations (rule-based systems, knowledge graphs). Neurosymbolic AI = a way to keep the LLM on guardrails, "because LLMs are by nature probabilistic" [04:56]. "People worry about hallucinations, but that's the feature… We hallucinate in a way. We imagine things that may not exist, and then we turn them into reality" [05:02–05:15].
- **[05:23–06:14] What an ontology actually is.** Not complicated: entities, their relationships, and properties — think "a graph data structure" [09:47]. Graph databases arose because relational tables are rigid (new attribute = new column = restructure); in a graph you just attach a node/property/edge.
- **[06:14–07:55] Building one, and the expert-systems era.** Top-down: domain experts enumerate entities (purchase orders, customers, support reps), properties, relationships — exactly what the 1980s expert-systems wave did. That wave (companies, millions spent, the Japanese national project, kids learning Japanese) **couldn't scale → AI winter** [07:17–07:21]. Neural networks existed since the '60s but also couldn't scale — until Nvidia's game GPUs came along [07:25–07:46]. Bottom-up alternative: mine real interactions (customer reactions) and grow the graph incrementally.
- **[07:55–09:12] Reuse existing taxonomies.** 15–20 years of prior art: **schema.org** (terms + relationships), **FOAF** (social networks), **Dublin Core** (bibliographic metadata), **DBpedia** (Wikipedia's knowledge extracted as a graph). "Don't reinvent the wheel… this stuff has been out there underlying a lot of what we already do" [08:27, 09:02]. *(His claim that Wikipedia search runs on DBpedia is backwards — see sourcing table.)*
- **[09:12–12:12] RDFS and OWL: inference and constraints.** These sit *beside* the graph and let you infer and constrain. RDFS **domain/range**: if `teaches` has domain Teacher and range Student, then "Bob teaches Scooter" ⇒ Bob is a teacher (and a person), Scooter is a student [10:05–10:39]. OWL **transitive properties**: ancestor(Sue,Mary) ∧ ancestor(Mary,Ann) ⇒ ancestor(Sue,Ann) [10:52–11:04]. OWL **functional properties** ("only one"): hasFather is functional, so "Bob is Jim's father" + "BB is Jim's father" ⇒ Bob and BB denote the same individual — a constraint that catches identity errors [11:23–12:01].
- **[12:12–14:22] Agents, loops, and how they break.** Böhm & Jacopini (1966): sequence + conditionals + loops = Turing complete — it settled the Fortran-vs-COBOL wars [12:42–13:10]. "Now we're seeing this in agentic AI. Agents now have loops. Loops give us the last piece" — a technology capable of computing anything computable [13:20–13:37]. But loops break: **infinite loops; drift as agents talk to each other; and cost — "token counts crank up as the loops continue"** [13:40–14:08]. "In a way we are revisiting… the world of expert systems — the symbolic part" [14:11–14:20].
- **[14:22–17:47] A Claude tool-use loop with an ontology validator.** He walks a raw Python `while True` loop against the Claude API: model + messages + a tool. The key insight for the room: **"LLMs can't do anything. All they can do is give us the next word with a high probability… I can't execute this tool… I'm the LLM. I'm just locked in this box"** [15:14–16:02] — the LLM only *proposes* the tool call with parameters; your code executes it on `stop_reason == "tool_use"` [16:08–16:31]. His addition (in red on the slide): **after the tool runs, pass the result to a validator that operates over the domain ontology** — if the result is reasonable, proceed; if not, bounce it back to the LLM or get a human in the loop [16:41–17:38]. "The idea is to surround the input with checks" [17:38–17:42].
- **[17:47–18:52] Pydantic at the door, ontology at the ledger.** Pydantic adds typing to Python — check the *types* of tool parameters with Pydantic, then check the *results* against the ontology [18:12–18:20]. "**Pydantic at the door, ontology at the ledger**" [18:23] — "and by the way, your agents should try to have no side effects… they're not changing things in the database yet. You want to run them through the ontology first" [18:28–18:42].
- **[18:52–20:30] The errors an ontology catches that English cannot.** Concrete failure classes, each mapped to an OWL construct: **a second refund on the same order** (functional property — refundable once) — "ontologies could catch it, whereas it's very tricky to do that in English" [19:17–19:22]; **a payout sent to the support desk instead of the buyer** (disjoint classes — customer and support rep are different things) [19:22–19:33]; **a made-up value like "probably shipped"** (enumerated value constraint: "paid, shipped, or refunded, nothing else") [19:34–19:50]. Bottom line: "you can have a reasoner built on an ontology to keep the LLM on track, have guardrails to keep it honest" [20:05–20:17].
- **[20:30–21:00] Close.** Back to "there's only make"; contact + codesupreme.ai (named for Coltrane's *A Love Supreme*).

## Verbatim key quotes (slide-ready)

- [01:23] "Nothing is a mistake. There is no win. There's no fail. There's only make." *(Corita Kent, via John Cage — attribute accordingly)*
- [03:51] "A formal specification of a shared conceptualization." *(Gruber's 1993 ontology definition — real, citable paper)*
- [05:02] "People worry about hallucinations, but that's the feature… We imagine things that may not exist, and then we turn them into reality."
- [13:40] "The danger of loops is that they can break… Loops can drift as agents start talking to each other… And loops can cost you money. Token counts crank up as the loops continue."
- [15:14] "LLMs can't do anything. All they can do is give us the next word with a high probability."
- [15:58] "I can't do it. I'm the LLM. I'm just locked in this box."
- [18:23] "Pydantic at the door, ontology at the ledger."
- [18:28] "Your agents should try to have no side effects… You want to run them through the ontology first."
- [19:44] "The status: paid, shipped, or refunded — nothing else."
- [20:05] "You can have a reasoner built on an ontology to keep the LLM on track — guardrails to keep it honest."

## Numbers & claims — sourcing quality

| Claim | Where | Sourcing |
|---|---|---|
| Gruber's definition of ontology (1993) | [03:39] | Well-sourced — T. Gruber, "A translation approach to portable ontology specifications", *Knowledge Acquisition* 5(2), 1993 |
| "Artificial intelligence" coined 1956 (Dartmouth) | [02:52] | Well-sourced, standard history |
| Böhm–Jacopini structured program theorem, 1966 (sequence + selection + iteration = Turing complete) | [12:42] | Well-sourced — Böhm & Jacopini, *CACM* 1966. His gloss ("no real difference in programming languages") is a simplification of the theorem |
| Japanese "future world project in the late '80s" | [07:02] | Imprecise — the Fifth Generation Computer Systems project (MITI) launched **1982**; don't reuse his name or date |
| Expert systems couldn't scale → AI winter; neural nets ('60s) unscalable until Nvidia GPUs | [07:17–07:46] | Broadly correct but heavily simplified narrative — fine as color, not as a history slide |
| "Wikipedia is based on an ontology called DBpedia… when you search Wikipedia it's looking things up in its giant graph database" | [08:54–09:01] | **Inaccurate as stated** — DBpedia is *extracted from* Wikipedia, not underneath it, and Wikipedia search is not DBpedia-backed (Wikidata is the Wikimedia graph project). Do NOT repeat on a slide |
| schema.org / FOAF / Dublin Core as reusable taxonomies, 15–20 years old | [08:14–08:49] | Well-sourced — all real, long-standing standards |
| "5,000 people are here" | [00:41] | Offhand crowd estimate — verify against AI Engineer World's Fair 2026 organizer numbers before citing attendance |
| Ontology validators catch double-refund / wrong-payee / invalid-status errors that prompts can't reliably stop | [19:09–19:57] | Speaker's design argument with worked examples — **no benchmark or measured error-rate data anywhere in the talk**; needs external neurosymbolic/guardrails literature if quantified on a slide |
| Loops → token costs crank up | [14:02] | Qualitative speaker assertion — true directionally; pair with real token-economics numbers from elsewhere if used |

## Relevance to the talk (Station F / Incubateur 42, 2026-09-02)

- **The anatomy of an agent, taught in 3 minutes.** His line-by-line Claude tool-use loop ("the LLM is locked in a box, it only proposes tool calls; your code executes on `stop_reason == tool_use`") is the single clearest founder-level explanation of what an agent *is* — ideal for the audience segment that uses Claude Code daily but has never seen the loop underneath.
- **Deterministic guardrails = the missing half of evals.** "A paragraph of instructions cannot reliably stop a double refund" — but three lines of logic can. This is the deterministic-validation complement to LLM-as-judge (pairs directly with the Hetzel/Braintrust eval-maturity material in `docs/talks/heuritech-agents/sources/FB-MLPhL9Ms-insights.md`: code scorers for objective failure modes, judges for subjective ones).
- **Maps 1:1 onto Claude Code primitives.** "Pydantic at the door" = tool input schemas / typed tool definitions; "ontology at the ledger" + "validator after the tool runs" = **Claude Code hooks (PreToolUse/PostToolUse) and the permission system**; "agents should have no side effects until validated" = sandboxing, dry-runs, plan-then-approve. Translating his raw-API pattern into Claude Code features is a strong original slide for this audience.
- **Context engineering convergence with Matt Pocock (v4F1gFy-hqg).** Both talks land on *give the model a formal shared conceptualization of the domain* — Pocock as a ubiquitous-language markdown glossary (soft, in-context), Coyle as typed entities + constraints (hard, outside the model). Soft context shapes generation; hard constraints veto it. That two-layer framing is itself a slide.
- **Founder-legible failure taxonomy.** Double refund, payout to the support desk, "probably shipped" — concrete, monetary, instantly understood by startup founders; excellent demo/story material for "why your agent needs guardrails before it touches production".
- **Agent orchestration risk framing.** "Loops can drift as agents start talking to each other" — a compact statement of the multi-agent failure mode; and "loops cost you money — token counts crank up" ties the guardrails story to AI economics.
- **Historical arc as a narrative device.** Expert systems (symbolic, couldn't scale) → neural nets (probabilistic, scaled) → neurosymbolic agents (both) gives a talk a satisfying "we're revisiting the '80s, but with the missing half" arc.

## Staleness / gaps (today: 2026-08-31)

- **Published 2026-07-23 — ~5 weeks old.** Well inside the 3-month freshness bar.
- **The content is deliberately timeless** (1956, 1966, 1993, W3C standards) — near-zero decay risk, but also **zero 2026 data**: no benchmarks, adoption numbers, or cost figures. Anything quantitative on a guardrails slide must come from other sources (e.g., published neurosymbolic/constrained-validation results, guardrails-library evals).
- **Known inaccuracies to keep off slides:** the Wikipedia/DBpedia claim (backwards); the Japanese Fifth Generation project name/date; "OWL = web object language" (it's the Web Ontology Language).
- **The demo is raw Anthropic Messages API, not Claude Code.** For this audience the pattern needs translating into hooks/permissions/tool schemas (see Relevance) — a framing task, not a staleness problem.
- **No evidence the ontology layer was run in production** — the talk is an architecture argument with worked examples, not a case study. If the talk needs a "this works at scale" claim, source a real deployment (e.g., enterprise knowledge-graph + agent case studies) separately.
