# How are multi-agent systems actually orchestrated in 2026 — graph engineering, central control, and what the Hugging Face incident changed?

## Decision this feeds

The same 2026-09-02 talk to founders at the Incubateur 42 / Station F has a movement on
building agents that work (the method: clarify, draft, evaluate, observe, improve,
understand) and one on loops. Its orchestration material is currently a June-2026
snapshot: Anthropic's five canonical patterns (prompt chaining, routing, parallelization,
orchestrator-workers, evaluator-optimizer) plus "subagents in parallel, then merge". The
speaker has since heard two things he wants reviewed before he teaches from that
material: **"graph engineering"** as an evolution of context engineering, and **"central
control"** — one main agent coordinating others — which he associates with **an incident
at Hugging Face**. The decision this feeds: **what the orchestration slides should say in
September 2026**, including whether the five-pattern framing still holds, and which
failure mode founders should design against from day one.

## Must answer

- **Identify the Hugging Face incident.** Find what actually happened (date, what broke, what was published, by whom) — specifically any incident involving multiple agents operating without a single coordinating authority, or an agent system damaging a repository, dataset, model hub or CI. Report the primary write-up (post-mortem, engineering blog, maintainer statement, issue thread). If no such incident is verifiable, say so plainly rather than assembling a plausible story from fragments — the speaker heard this second-hand and needs it confirmed or killed.
- **Central control as a pattern**: what "one main agent coordinates the others" means concretely in 2026 practice — a single writer, a lock or lease on shared state, a supervisor owning merges, a scheduler. What failures it prevents (concurrent writes, conflicting edits, duplicated work, runaway spawning) and what it costs (throughput, single point of failure, context pressure on the coordinator). Who advocates it, with primary sources.
- **Graph engineering**: what the term denotes in 2026. Credible candidates: (a) representing an agent's knowledge/context as a graph rather than flat files or vector chunks (knowledge graphs, GraphRAG, temporal graphs like Graphiti), and (b) representing the agent workflow itself as an explicit graph of nodes and edges (LangGraph-style state machines, DAG pipelines). Establish which meaning practitioners use, whether both are in play, who popularised it, and what measured evidence exists that it beats the simpler alternative it replaces.
- **What the evidence says about multi-agent vs single-agent.** Anthropic published on multi-agent research systems; Cognition published a widely-read argument against multi-agent architectures ("don't build multi-agents"). Establish the current state of that argument with primary sources on both sides, plus any 2026 measurement (benchmarks, production write-ups) that settles or sharpens it. This is the single most useful item for the audience.
- **Do Anthropic's five patterns still hold** as the teaching frame in September 2026 — prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer? Have they been revised, extended or superseded by the labs' newer guidance (Anthropic, OpenAI, Google) or by the frameworks people actually ship on?
- **The coordination failure modes, with names and evidence**: context rot in long runs, error compounding across agent hops, concurrent edits to shared state, spawn storms, coordinator context exhaustion. For each: one citable source and, where it exists, the mitigation practitioners report works.
- **What a small team should actually do**: a founder-legible rule set — when a single agent with good context beats orchestration, when to add a coordinator, what to make append-only or single-writer, how to bound spawning. Grounded in cited practice, not opinion.

## Source bar

tier: Primary practitioner and lab sources first — Anthropic/OpenAI/Google engineering
and research posts, agent-framework documentation and design docs (LangGraph, OpenAI
Agents SDK, AAIF/MCP), first-party post-mortems and maintainer statements, arXiv papers
with real evaluation. Named senior practitioners' write-ups count when they describe
systems they built. Secondary syntheses and content-marketing posts may be used for
framing only, and must be labelled as such. Vendor claims about their own framework must
be marked self-reported.

recency: State of play as of September 2026. Foundational material (the five patterns,
the multi-agent debate's opening arguments) may be older but must carry its date and be
checked for whether it was superseded. Anything about the Hugging Face incident must be
sourced to a dated primary account.

## Deliverable

A Markdown report with:
- A 5-line executive answer: what changed in orchestration since June 2026, and the one
  rule founders should leave with.
- A verified account of the Hugging Face incident, or an explicit statement that it could
  not be verified, with what WAS found.
- The multi-agent-vs-single-agent state of the argument, both sides quoted, with a verdict
  on what the evidence supports.
- A definition of graph engineering that a non-specialist founder can hold, with the
  measured evidence for it and against it.
- A table of coordination failure modes: name · what happens · citable source · mitigation.
- For every number or named claim that could go on a slide: exact clickable URL AND a
  verbatim quote containing it (a citation registry greps these character-by-character).
- A short "what to teach" section: what to keep, revise or cut from the five-pattern frame.

## Out of scope

- Tutorials or code for any specific framework.
- Agent security and prompt-injection defence as a topic in itself (except where a
  coordination failure mode is a security failure).
- Model selection, pricing, or benchmark scores.
- Anything about Hugging Face other than the incident and its lessons.
