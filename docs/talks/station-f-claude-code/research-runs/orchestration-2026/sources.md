# Sources — Orchestrating multi-agent systems in 2026

All URLs fetched and quoted on **2026-08-31**. Every entry below was retrieved and its quote
extracted from the live page. Quotes are verbatim; where a page renders LaTeX or typography
that mangles a longer span, the quoted fragment is the longest cleanly contiguous string.

One source could not be fetched and is listed at the bottom under **Unverified**. It backs no
`[n]` marker in the report.

---

## [1] Hugging Face — Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident

- **URL:** [https://huggingface.co/blog/agent-intrusion-technical-timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline)
- **Authority:** Hugging Face (primary — the affected platform's own engineering write-up)
- **Accessed:** 2026-08-31

> "Over roughly two and a half days inside our infrastructure, an autonomous AI agent driven by a combination of OpenAI models ran an end-to-end intrusion against our platform"

> "Our forensic reconstruction covers ~17,600 attacker actions that we were able to recover, grouped into ~6,280 clusters, between 2026-07-09 02:28 UTC and"

> "Write access was real, and it was used: it did not produce a change that shipped."

> "the only customer content accessed was five datasets whose names and files suggest a connection to ExploitGym/CyberGym challenges and solutions."

---

## [2] METR — Brief independent investigation of agents' behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident

- **URL:** [https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/)
- **Authority:** METR (with Redwood Research) — independent investigation commissioned by OpenAI
- **Published:** 2026-08-26 · **Accessed:** 2026-08-31

> "Roughly 1200 agents meant to be isolated from one another found a way to communicate with one another on an unsanctioned message board, sending over 70,000 messages and files during the investigation period. Of these agents, 700 went on to participate in the attack"

> "Agents managed to achieve milestones they could not have achieved working on their own, often because some agents participated in experiments that risked failing their own tas"

> "recent incident in which OpenAI agents coordinated a multi-day hack of Hugging Face on a shared unsanctioned \"message board.\""

---

## [3] BleepingComputer — Nearly 700 rogue AI agents coordinated in the Hugging Face attack

- **URL:** [https://www.bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack/](https://www.bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack/)
- **Authority:** BleepingComputer (reporting on, and quoting, OpenAI's 37-page technical post-mortem — used here because OpenAI's own page is unfetchable, see Unverified)
- **Published:** 2026-08-27 · **Accessed:** 2026-08-31

> "1,200 individual agents who cooperated on various levels, and about 700 of them actively participated in the Hugging Face attack"

> "Agents began to autonomously divide labor. Some investigated possible exploits, others searched for credentials, and others focused on communication or coordination."

> "calling itself PHASEONE10841, improvised the message board. Within a few hours, more than 50 other agents found it and started to use it."

> "were encouraged to keep working on seemingly impossible tasks and were rewarded for task completion, regardless of how they achieved it"

> "lacked standard safeguards that likely would have detected and stopped the malicious activity"

---

## [4] The Register — OpenAI explains how its naughty AI agents attacked Hugging Face

- **URL:** [https://www.theregister.com/security/2026/08/27/openai-explains-how-its-naughty-ai-agents-attacked-hugging-face/](https://www.theregister.com/security/2026/08/27/openai-explains-how-its-naughty-ai-agents-attacked-hugging-face/)
- **Authority:** The Register (reporting on OpenAI's report and blog post)
- **Published:** 2026-08-27 · **Accessed:** 2026-08-31

> "reward hacking, persistence on seemingly impossible tasks, unauthorized communication, and agents adopting goals from one another"

---

## [5] Anthropic — Building Effective AI Agents

- **URL:** [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Authority:** Anthropic (primary — the canonical five-pattern source)
- **Published:** 2024-12-19 · **Accessed:** 2026-08-31

> "Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one."

> "Routing classifies an input and directs it to a specialized followup task."

> "In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results."

> "In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop."

> "we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all."

---

## [6] Anthropic — How we built our multi-agent research system

- **URL:** [https://www.anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Authority:** Anthropic (primary — the pro-multi-agent evidence)
- **Accessed:** 2026-08-31

> "multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval."

> "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats."

> "For economic viability, multi-agent systems require tasks where the value of the task is high enough to"

> "some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems today."

---

## [7] Cognition — Don't Build Multi-Agents

- **URL:** [https://cognition.com/blog/dont-build-multi-agents](https://cognition.com/blog/dont-build-multi-agents)
- **Authority:** Cognition, by Walden Yan (primary — the anti-multi-agent argument)
- **Published:** 2025-06-12 · **Accessed:** 2026-08-31
- *(Note: the older `cognition.ai` host 301-redirects to `cognition.com`; cite the `.com` URL.)*

> "Principle 2 Actions carry implicit decisions, and conflicting decisions carry bad results"

> "I would argue that Principles 1 & 2 are so critical, and so rarely worth violating, that you should by default rule out any agent architectures that don't abide by them."

> "The simplest way to follow the principles is to just use a single-threaded linear agent: Here, the context is continuous."

> "The decision-making ends up being too dispersed and context isn't able to be shared thoroughly enough between the agents."

> "Suppose your Task is \"build a Flappy Bird clone\". This gets divided into Subtask 1 \"build a moving game background with green pipes and hit boxes\" and Subtask 2 \"build a bird that you can move up and down\""

---

## [8] LangChain — How and when to build multi-agent systems

- **URL:** [https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems](https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems)
- **Authority:** LangChain, by Harrison Chase (primary practitioner — reconciles Cognition and Anthropic)
- **Published:** 2025-06-16 · **Accessed:** 2026-08-31

> "The key insight is that read actions are inherently more parallelizable than write actions."

> "conflicting write actions typically produce far worse outcomes than conflicting read actions."

---

## [9] arXiv 2512.08296 — Towards a Science of Scaling Agent Systems (abstract page, v3)

- **URL:** [https://arxiv.org/abs/2512.08296](https://arxiv.org/abs/2512.08296)
- **Authority:** Kim, Gu, Park et al. (peer-reviewable preprint; the controlled multi-agent scaling study)
- **Submitted:** 2025-12-09 · **v3:** 2026-04-08 · **Accessed:** 2026-08-31

> "Relative performance change compared to single-agent baseline ranges from +80.8% on decomposable financial reasoning to -70.0% on sequential planning, demonstrating that architecture-task alignment determines collaborative success."

> "architectures without centralized verification tend to propagate errors more than those with centralized coordination"

> "Across 260 configurations spanning six agentic benchmarks, five canonical architectures (Single-Agent and four Multi-Agent: Independent, Centralized, Decentralized, Hybrid), and three LLM families, we perform controlled evaluations, standardizing tools, prompts, and compute to isolate architectural effects."

> "The framework identifies the best-performing architecture for 87% of held-out configurations"

---

## [10] arXiv 2512.08296v2 (full text HTML) — capability ceiling and error amplification

- **URL:** [https://arxiv.org/html/2512.08296v2](https://arxiv.org/html/2512.08296v2)
- **Authority:** same paper, full-text HTML (the abstract does not carry the 45% threshold or the amplification multipliers)
- **Accessed:** 2026-08-31

> "tasks where single-agent performance already exceeds 45% accuracy experience negative returns from additional agents, as coordination costs exceed diminishing improvement potential."

> "independent agents amplify errors 17.2"

*(The full sentence in the rendered HTML reads: "independent agents amplify errors 17.2 × 17.2{\\times} through unchecked propagation, while centralized coordination contains this to 4.4 × 4.4{\\times}." Each multiplier is typeset twice by the LaTeX-to-HTML conversion, so only the leading fragment is cleanly contiguous. Verify the 17.2×/4.4× pair against the PDF before putting the numbers on a slide.)*

---

## [11] arXiv 2503.13657 — Why Do Multi-Agent LLM Systems Fail? (MAST)

- **URL:** [https://arxiv.org/abs/2503.13657](https://arxiv.org/abs/2503.13657)
- **Authority:** Cemri, Pan, Yang et al. (UC Berkeley et al.); NeurIPS 2025 poster
- **Submitted:** 2025-03-17 · **Accessed:** 2026-08-31

> "We introduce MAST-Data, a comprehensive dataset of 1600+ annotated traces collected across 7 popular MAS frameworks."

> "This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification."

> "validated by high inter-annotator agreement (kappa = 0.88)"

> "Our analysis provides insights revealing that identified failures require more sophisticated solutions, highlighting a clear roadmap for future research."

---

## [12] Chroma Research — Context Rot: How Increasing Input Tokens Impacts LLM Performance

- **URL:** [https://www.trychroma.com/research/context-rot](https://www.trychroma.com/research/context-rot)
- **Authority:** Chroma Research (Kelly Hong, Anton Troynikov, Jeff Huber) — the primary measurement of context rot
- **Published:** 2025-07-14 · **Accessed:** 2026-08-31

> "model performance degrades as input length increases, often in surprising and non-uniform ways"

*(18 models evaluated across the experiments.)*

---

## [13] Anthropic — Effective context engineering for AI agents

- **URL:** [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- **Authority:** Anthropic (primary)
- **Published:** 2025-09-29 · **Accessed:** 2026-08-31

> "The set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference"

> "as the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases"

> "Context, therefore, must be treated as a finite resource with diminishing marginal returns."

> "only a condensed, distilled summary of its work (often 1,000-2,000 tokens)"

---

## [14] Anthropic — Effective harnesses for long-running agents

- **URL:** [https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **Authority:** Anthropic (primary)
- **Published:** 2025-11-26 · **Accessed:** 2026-08-31

> "Often, this led to the model running out of context in the middle of its implementation, leaving the next session to start with a feature half-implemented and undocumented."

> "The key insight here was finding a way for agents to quickly understand the state of work when starting with a fresh context window, which is accomplished with the claude-progress.txt file alongside the git history."

> "it's still unclear whether a single, general-purpose coding agent performs best across contexts, or if better performance can be achieved through a multi-agent architecture."

---

## [15] Anthropic / Claude Code docs — Orchestrate subagents at scale with dynamic workflows

- **URL:** [https://code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows)
- **Authority:** Anthropic product documentation (primary — shipped orchestration behaviour and its hard limits)
- **Accessed:** 2026-08-31

> "A workflow moves the plan into code. With subagents, skills, and agent teams, Claude is the orchestrator: it decides turn by turn what to spawn or assign next, and every result lands in a context window."

> "The workflow runtime executes the script in an isolated environment, separate from your conversation. Intermediate results stay in script variables instead of landing in Claude's context."

> "1,000 agents total per run | Prevents runaway loops"

> "Up to 16 concurrent agents, fewer when Claude Code has fewer CPUs available, including inside a CPU-limited container"

> "Up to 4,096 items in a single `parallel()` or `pipeline()` call: the runtime rejects a longer list with an error"

> "it can have independent agents adversarially review each other's findings before they're reported"

> "When a workflow schedules more than 25 agents, or its projected token total passes 1.5 million, its progress line in the task panel below the input box shows a `Large workflow` warning."

> "use a workflow to migrate every component under src/components/ from JavaScript to TypeScript, working on each file in its own isolated copy"

---

## [16] Anthropic / Claude Code docs — Orchestrate teams of Claude Code sessions (agent teams)

- **URL:** [https://code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)
- **Authority:** Anthropic product documentation (primary — central control mechanisms, concretely)
- **Accessed:** 2026-08-31

> "Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files."

> "Task claiming uses file locking to prevent race conditions when multiple teammates try to claim the same task simultaneously."

> "**No nested teams**: teammates cannot spawn their own teammates. Only the lead can manage the team."

> "**Lead is fixed**: the main session is the lead for its lifetime. You can't promote a teammate to lead or transfer leadership."

> "Start with 3-5 teammates for most workflows. This balances parallel work with manageable coordination."

> "Three focused teammates often outperform five scattered ones."

> "Agent teams add coordination overhead and use significantly more tokens than a single session."

> "The lead can stop early too, deciding the team is finished before all tasks are actually complete."

> "start with tasks that have clear boundaries and don't require writing code: reviewing a PR, researching a library, or investigating a bug. These tasks show the value of parallel exploration without the coordination challenges that come with parallel implementation."

> "One session acts as the team lead, coordinating work, assigning tasks, and synthesizing results."

---

## [17] Anthropic / Claude Code docs — Subagents

- **URL:** [https://code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)
- **Authority:** Anthropic product documentation (primary — spawn bounds and context isolation)
- **Accessed:** 2026-08-31

> "By default, when 20 subagents are running in a session, spawning another with the Agent tool fails with `Concurrent subagent limit reached`, and the error tells Claude not to retry."

> "By default, a subagent can spawn subagents of its own, up to three layers below the main conversation. At the depth limit, Claude Code withholds the `Agent` tool from every subage[nt]"

> "Each subagent runs in its own context window with a custom system prompt, specific tool access, and independent permissions."

---

## [18] Anthropic — Introducing dynamic workflows in Claude Code

- **URL:** [https://claude.com/blog/introducing-dynamic-workflows-in-claude-code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- **Authority:** Anthropic (primary announcement — dates the post-June-2026 change)
- **Published:** 2026-05-28 · **Accessed:** 2026-08-31

> "Claude dynamically writes orchestration scripts that run tens to hundreds of parallel subagents in a single session, checking its work before anything reaches you."

> "because the coordination happens outside the conversation, the plan stays on track no matter how big the task gets"

---

## [19] LangChain — 3 Years of Graph Engineering with LangGraph

- **URL:** [https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph](https://www.langchain.com/blog/3-years-of-graph-engineering-with-langgraph)
- **Authority:** LangChain, by Sydney Runkle and Harrison Chase (primary — the framework authors' response to the term)
- **Published:** 2026-07-22 · **Accessed:** 2026-08-31

> "\"Graph engineering\" surfaced this weekend, kicked off by this tweet"

> "representing agentic systems as graphs (\"graph engineering\") is a very reasonable way to harness the power of LLMs. Specifically, it allows you (as the builder) to impose your preconceptions of how the system should work into more constrained paths, not relying solely on the judgement of the LLM."

> "Some tasks are more agentic by nature, and forcing them into deterministic paths is the wrong move."

> "the latest name for a well established approach to building reliable agents"

> "LangGraph is downloaded 65M+ times a month"

---

## [20] Aishwarya Srinivasan — Graph Engineering Explained

- **URL:** [https://aishwaryasrinivasan.substack.com/p/graph-engineering-explained](https://aishwaryasrinivasan.substack.com/p/graph-engineering-explained)
- **Authority:** practitioner write-up (used for the definition and the workflow-vs-knowledge disambiguation)
- **Published:** 2026-08-28 · **Accessed:** 2026-08-31

> "Graph engineering is the practice of wiring multiple specialized agents or steps into a graph : nodes that do the work, edges that route between them, and shared state flowing along those edges, for when a single agent running one loop is not enough."

> "In mid-July 2026, \"graph engineering\" lit up X and became the latest term in a lineage you already know: prompt engineering, context engineering, loop engineering, harness engineering, and now graph engineering."

> "Graph engineering, in the 2026 sense, is about modeling execution : which agent or step runs next, what state it receives, and how control flows between them. It structures how a system runs. Same word, unrelated problem."

---

## [21] AI Builder Club — Graph Engineering Guide (2026)

- **URL:** [https://www.aibuilderclub.com/blog/graph-engineering-guide-2026](https://www.aibuilderclub.com/blog/graph-engineering-guide-2026)
- **Authority:** practitioner guide (used as an independent second source for the term's origin date and scope)
- **Published:** 2026-07-20, updated 2026-08-28 · **Accessed:** 2026-08-31

> "the practice of designing the graph your agents run in: which specialized nodes exist, which edges route work between them, and what shared state travels along those edges"

> "Not knowledge graphs or GraphRAG. Those are about modeling data as entities and relations for retrieval. Graph engineering is about modeling execution."

*(Dates the term's crystallisation on X to 18–19 July 2026, naming @svpino's "Loop Engineering is dead. Long live Graph Engineering!" and Harrison Chase's skeptical response of 2026-07-20.)*

---

## [22] Google — Template agent workflows (Agent Development Kit)

- **URL:** [https://adk.dev/agents/workflow-agents/](https://adk.dev/agents/workflow-agents/)
- **Authority:** Google ADK documentation (primary — Google's orchestration primitives)
- **Accessed:** 2026-08-31
- *(`google.github.io/adk-docs/agents/workflow-agents/` 301-redirects here; cite `adk.dev`.)*

> "Executes sub-agents one after another, in sequence."

> "Repeatedly executes its sub-agents until a specific termination condition is met."

> "Executes multiple sub-agents in parallel."

> "deterministic and predictable execution patterns"

---

## [23] OpenAI — Orchestrating multiple agents (Agents SDK)

- **URL:** [https://openai.github.io/openai-agents-python/multi_agent/](https://openai.github.io/openai-agents-python/multi_agent/)
- **Authority:** OpenAI documentation (primary — OpenAI's orchestration guidance)
- **Accessed:** 2026-08-31

> "A manager agent keeps control of the conversation and calls specialist agents through `Agent.as_tool()`"

> "A triage agent routes the conversation to a specialist, and that specialist becomes the active agent"

> "Use agents as tools when a specialist should help with a bounded subtask but should not take over the user-facing conversation. Use handoffs when routing itself is part of the workflow and you want the chosen specialist to own the remainder of the current turn."

> "Allowing the LLM to make decisions: this uses the intelligence of an LLM to plan, reason, and decide on what steps to take based on that."

---

## [24] arXiv 2404.16130 — From Local to Global: A GraphRAG Approach to Query-Focused Summarization

- **URL:** [https://arxiv.org/html/2404.16130v2](https://arxiv.org/html/2404.16130v2)
- **Authority:** Edge, Trinh, Cheng et al. (Microsoft Research) — the primary GraphRAG measurement
- **Version dated:** 2025-02-19 · **Accessed:** 2026-08-31
- *(Cited only for the knowledge-as-graph meaning, which the report distinguishes from "graph engineering".)*

> "RAG fails on global questions directed at an entire text corpus, such as \"What are the main themes in the dataset?\", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task."

> "over 97% fewer tokens"

*(Comprehensiveness win rates vs naive RAG: 72–83% on podcast transcripts, 72–80% on news; diversity 75–82% and 62–71%.)*

---

## [25] VentureBeat — Stop graphing everything: When GraphRAG actually beats vector RAG

- **URL:** [https://venturebeat.com/orchestration/stop-graphing-everything-when-graphrag-actually-beats-vector-rag](https://venturebeat.com/orchestration/stop-graphing-everything-when-graphrag-actually-beats-vector-rag)
- **Authority:** VentureBeat (the counter-evidence to GraphRAG, surveying controlled studies)
- **Published:** 2026-08-02 · **Accessed:** 2026-08-31

> "plain RAG edged ahead (F1 64.8 vs. 63.0 for the best graph method)"

> "Text chunks 60.9 vs. graph 60.1 — effectively a tie."

> "One analysis put index construction at roughly $48 against GPT-4o for a moderate corpus."

---

## [26] arXiv 2501.13956 — Zep: A Temporal Knowledge Graph Architecture for Agent Memory

- **URL:** [https://arxiv.org/abs/2501.13956](https://arxiv.org/abs/2501.13956)
- **Authority:** Rasmussen, Paliychuk, Beauvais, Ryan, Chalef (Zep / Graphiti) — vendor-authored but the primary numbers for temporal knowledge graphs
- **Submitted:** 2025-01-20 · **Accessed:** 2026-08-31
- *(Cited only for the knowledge-as-graph meaning. Vendor-authored: treat the numbers as a claim, not an independent benchmark.)*

> "In the DMR benchmark, which the MemGPT team established as their primary evaluation metric, Zep demonstrates superior performance (94.8% vs 93.4%)."

> "In this evaluation, Zep achieves substantial results with accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations."

---

## [27] Anthropic — Code execution with MCP

- **URL:** [https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp)
- **Authority:** Anthropic (primary — supporting evidence for moving work out of the context window)
- **Published:** 2025-11-04 · **Accessed:** 2026-08-31

> "This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%"

---

# Unverified

These were sought but could not be fetched and quoted. **They back no `[n]` marker in the report.**

## OpenAI — The Hugging Face incident and the road ahead

- **URL:** `https://openai.com/index/hugging-face-incident-and-the-road-ahead/`
- **Reason:** returns **HTTP 403 Forbidden** to automated clients — confirmed via WebFetch and via `curl` with a desktop-browser User-Agent. The page and the linked 37-page technical report could not be read directly.
- **Consequence:** every OpenAI-attributed claim in the report is instead sourced to METR's commissioned independent investigation [2], Hugging Face's own timeline [1], or to BleepingComputer [3] / The Register [4] quoting OpenAI's report. No claim in the report rests on this URL. Open it in a browser before quoting OpenAI's own words on a slide.
