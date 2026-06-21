# Arms Race PDF — extract for Station F deck (2026-04-13)

**Source**: The Agentic AI Arms Race — Q1 2026 Competitive Landscape (PDF)
**Local path**: docs/sources/The Agentic AI Arms Race_ Q1 2026 Competitive Landscape.pdf
**Pages**: 7
**Author / publication URL**: NOT VISIBLE — Louis must supply. The PDF has no byline, no masthead, no footer URL, no visible publication logo. It reads like an analyst/consulting brief compiled from press citations (small inline "pill" tags: Morph, Anthropic, VentureBeat, Fortune, TechCrunch, CNBC, Wikipedia, DataCamp, Softmax Data Blog, OpenAI, Google Developers, etc. appear to be source tags).

## §1 Frontier battlegrounds

The PDF's own heading is "Seven battlegrounds define the competition." It does not map 1:1 to Louis's list — the report's seven are: **Coding agents**, **Computer and GUI agents**, **Protocol standards (MCP)**, **Multi-agent orchestration**, **Enterprise agents**, **Agent safety and alignment**, **Open-source vs proprietary**.

### Coding agents (p.1–2)
- "The fiercest battleground by revenue and adoption."
- Leaders: **OpenAI's Codex** (2 million weekly active users by March 2026, growing 70% month-over-month), **Anthropic's Claude Code** (ARR "estimated $2.5 billion annualized" early 2026, doubling since January).
- Challengers: **Google's Jules** (public beta April 2 with no waitlist, offering 300 tasks/day via its Ultra tier), **Cognition's Devin 2.0** (slashed pricing from $500 to $20 per month), **Morph** (reporting enterprise customers like Nubank achieved 12x efficiency gains), **BCO** in ETL migrations.
- "Cursor crossed $1 billion in ARR at a $29.3 billion valuation."
- "In a single two-week window in February, every major coding tool shipped multi-agent parallel execution — Grok Build (8 agents), Windsurf (5 parallel), Claude Code background agents, and Codex CLI's new Agents SDK — signaling that single-agent coding is already obsolete."

### Computer use and GUI agents (p.1–2)
- "Represent the most visible frontier."
- **OpenAI's GPT-5.4 (March 5, 2026)** "introduced native desktop and browser control, scoring 75.0% on OSWorld-Verified — the first model to exceed the 72.4% human expert baseline."
- **Anthropic's Claude Computer Use** in research preview on March 23 for macOS (expanded to Windows on April 3), "enabling Claude to see screens, click buttons, open applications, and fill spreadsheets."
- **Google's Project Mariner**, available to AI Ultra subscribers, achieved **83.5% on the WebVoyager benchmark** and now supports up to 10 concurrent browser tasks.
- "The OpenClaw phenomenon — an open-source personal agent created by Austrian developer Peter Steinberger — demonstrated mass-market appetite for computer-controlling agents, triggering adoption frenzies in China where people queued outside Tencent offices for installation help before security vulnerabilities forced early pullbacks."

### Protocol standards / MCP (p.2)
- "Protocol standards have consolidated around Anthropic's MCP faster than anyone had predicted."
- "In December 2025, Anthropic donated MCP to the Agentic AI Foundation (AAIF) under the Linux Foundation, co-founded with Block and OpenAI, with Google, Microsoft, AWS, Anthropic, Salesforce, and Snowflake as supporting members."
- "MCP is now integrated across ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code, LangChain, and LlamaIndex, with over 10,000 indexed MCP servers."
- "Forrester predicts 30% of enterprise application vendors will launch MCP servers by year end."
- "While the Agent Client Protocol (ACP) targets editor portability and Google's Universal Commerce Protocol (UCP) addresses retail, MCP has effectively won the protocol war for agent-tool integration."

### Multi-agent orchestration (p.2)
- "Multi-agent orchestration saw a 1,445% surge in enterprise inquiries from Q1 2024 to Q2 2025 according to Gartner, and the technology matured rapidly in early 2026."
- **Microsoft's Agent Framework** (successor to AutoGen and Semantic Kernel) "reached release candidate 1.0 in February, offering sequential, concurrent, group chat, and dynamic task-ledger orchestration patterns."
- **Microsoft Magentic UI's xRAI's xGrok 4.0** "introduced a 4-agent collaboration system with specialized personas (Grok, Harper, Benjamin, Lucas) processing queries simultaneously, scaling to 16 agents at high reasoning levels."
- "Google's Antigravity IDE features a 'Manager Surface' that coordinates multiple coding agents producing verifiable artifacts."
- "LangChain launched Deep Agents with subagent delegation and parallel execution."

### Enterprise agents (p.2)
- "Enterprise agents have become a distinct competitive dimension as agent deployments scale."
- **Microsoft** "announced Agent 365 (GA May 1) at $15/user/month — a control plane with agent registry, Entra ID access control, performance visualization, and security monitoring. Its new M365 E7 'Frontier Suite' bundles everything at $99/user/month."
- **AWS Bedrock AgentCore** reached GA on March 31 with 13 built-in evaluators and persistent session storage.
- **Cohere's North platform** "differentiates by running on as few as 2 GPUs in air-gapped environments."
- **Mistral** "launched Forge for enterprise model training with reinforcement learning for agentic performance."
- "The governance layer — identity, audit trails, compliance — is increasingly where enterprise deals are won."

### Agent safety and alignment (p.2)
- "Agent safety and alignment research accelerated in response to real-world incidents."
- "The International AI Safety Report 2026, led by Yoshua Bengio and backed by 30+ countries, found that **AI task autonomy is doubling every 7 months — 3x faster than Moore's Law** — while safety testing has become less reliable as models learn to distinguish test environments from production."
- "Scale AI's PropensityBench showed that realistic pressures dramatically increase misbehavior rates, with models using harmful tools 64% of the time when those tools were renamed with benign labels."
- "Anthropic launched its **Automated Alignment Agent (A3)**, an open-source framework that automatically mitigates safety failures."
- "OpenAI acquired security-testing firm Promptfoo (used by 25%+ of Fortune 500) to bolster its agentic safety stack."

### Open-source vs proprietary (p.3)
- "Open-source versus proprietary dynamics are more complex than ever."
- "**Meta acquired Singapore-based Manus** — the world's fastest startup to reach $100M ARR — for over $2 billion, buying an execution layer rather than a model."
- "**Mistral's Devstral 2** achieved **72.2% on SWE-bench Verified** as the top open-weight coding model, 4x smaller and 7x more cost-efficient than Claude Sonnet."
- "Google released **Gemma 4** (April 2) and an open Apache 2.0 with on-device agentic capabilities including multi-step planning and autonomous action."
- Code name "Avocado" for commercial use.
- "Yet Meta is simultaneously developing a closed-source model codenamed 'Avocado' for commercial use."
- "OpenClaw's security disasters (12% of marketplace skills contained critical vulnerabilities) demonstrated that open-source agents face severe trust challenges."

## §2 Decisive breakthroughs (Q1 2026)

PDF heading: "Decisive breakthroughs from January through April."

### GPT-5.4 (OpenAI, released March 5) — p.3
- "The quarter's most consequential technical milestone was GPT-5.4's superhuman computer use."
- "Unified OpenAI's coding, reasoning, and computer-use capabilities into a single architecture."
- "GPT-5.4 surpassed the human expert baseline of 72.4%, while achieving 67.3% on WebArena-Verified and 92.8% on Online-Mind2Web."
- "Introduced 'Tool Search' for dynamic MCP server integration, reducing tokens by 47% on the MCP Atlas benchmark."
- "OpenAI shipped five model variants in under three months — GPT-5.2-Codex (January 14), GPT-5.3-Codex (February 5), GPT-5.3-Codex-Spark on Cerebras hardware (February), GPT-5.4 (March 5), and GPT-5.4 mini (March 17) — an unprecedented cadence."

### Claude Opus 4.6 (Anthropic, February 5) — p.3
- "Matched this intensity with its own breakthroughs."
- "A native 1-million-token context window."
- "**14.5-hour task completion horizon** (the longest of any model at release)."
- "The strongest prompt injection resistance in the industry at just 4.7% attack success rate versus GPT-5.1's 21.9%."
- Claude Sonnet 4.6 (February 17) "scored 79.6% on SWE-bench Verified at one-fifth the cost of Opus, including adaptive thinking with four effort levels."
- Anthropic's most ambitious unreleased project, **the Conway Platform**, surfaced in testing around April — "a persistent 'always-on autonomous environment' that would represent a step-change in agent informatization."

### Gemini 3.1 Pro (Google DeepMind, February 19) — p.3
- "Claimed the Terminal-Bench 2.0 crown at 78.4% and ARC-AGI-2 at 77.1%, while matching competitors on SWE-bench Verified at 80.6% — all at $2/$12 per million tokens."
- "Google's Alethela autonomous research agent, powered by Gemini Deep Think, resolved 4 open Erdős conjectures and produced a fully autonomous research paper, achieving what DeepMind called 'Level A2' research autonomy."
- "Gemma 4's launch brought multi-agent workflows to edge devices through a dedicated 'Agent Skills' app."

### Copilot Cowork (Microsoft) — p.3–4
- "Microsoft's most striking move was building its flagship Copilot Cowork feature on Anthropic's Claude rather than OpenAI's models — a clear signal that the $30 billion Azure compute deal with Anthropic is reshaping Redmond's AI stack."
- "Copilot Wave 3 (March 9) introduced long-running autonomous task execution across M365 apps, with model selection dynamically choosing between Claude and GPT based on task type."
- "Microsoft CMO Jared Spataro candidly acknowledged: 'Every 60 days, there's a new king of the hill.'"

### OpenAI's acquisition spree (p.4)
- "Six deals in Q1 2026 revealed strategic priorities: Promptfoo for agent security testing, Astral (Python developer tools uv and Ruff) for Codex integration, and the acqui-hire of OpenClaw's creator Peter Steinberger to 'drive the next generation of personal agents.'"

### Mistral cadence (p.4)
- **Mistral Vibe 2.0** (January 27) "introduced custom subagents for terminal-native coding."
- **Devstral 2** (March) "achieved state-of-the-art open-weight coding performance."
- **Leanstral** (March 17) "targeted formal proof verification in Lean 4 for aerospace and financial infrastructure."
- **Xpert Forge** (March 17) "enables enterprises to train models on proprietary data with RL for agentic performance."
- "The acquisition of Koyeb (serverless cloud) signals a full-stack strategy — owning models and deployment infrastructure on European servers, with 10,000 French government agents already piloting Mistral-powered systems."

## §3 Lab investment data

Verbatim dollar figures and rounds scattered across the PDF:

- **OpenAI**: "$122 billion funding round at an $852 billion valuation, closed March 31, provided the capital to sustain this pace." (p.4)
- **Anthropic / Microsoft**: "$30 billion Azure compute deal with Anthropic is reshaping Redmond's AI stack." (p.3–4)
- **Meta → Manus**: "Meta acquired Singapore-based Manus — the world's fastest startup to reach $100M ARR — for over $2 billion, buying an execution layer rather than a model." (p.3)
- **Cursor**: "Cursor crossed $1 billion in ARR at a $29.3 billion valuation." (p.1–2)
- **Claude Code**: "ARR estimated $2.5 billion annualized, doubling since January." (p.1)
- **OpenAI Codex**: "reached 2 million weekly active users by March 2026, growing 70% month-over-month." (p.1) — usage not dollars, but the PDF's lead revenue datapoint.
- **Microsoft M365 E7 'Frontier Suite'**: "$99/user/month"; **Agent 365**: "$15/user/month (GA May 1)." (p.2)
- **Cohere North**: "runs on as few as 2 GPUs in air-gapped environments." (p.2) — only explicit GPU count.
- **Mistral deployment**: "10,000 French government agents already piloting Mistral-powered systems." (p.4) — seat count, not dollars.
- **MCP ecosystem**: "97 million monthly SDK downloads" and "over 10,000 indexed MCP servers." (p.1 / §1 / p.5 conclusion)
- **Tracxn cumulative funding**: "the agentic AI sector now counts over 1,040 active companies backed by $20.8 billion in cumulative funding." (p.1)
- **Viral open-source GitHub**: "OpenClaw amasses 247,000 GitHub stars." (p.1)
- **Devin pricing change**: "Cognition's Devin 2.0 slashed pricing from $500 to $20 per month." (p.1–2)
- **Promptfoo reach**: "used by 25%+ of Fortune 500." (p.2)
- **MCP adoption**: "Gartner projects 40% of enterprise applications will embed AI agents by end of 2026, up from less than 5% in 2025." (p.1)

## §4 Benchmark deepenings

The PDF's benchmark-results table (end of page 6) is verbatim below before the per-benchmark notes:

| Benchmark | Leader | Score | Runner-up | Score | Human baseline |
|---|---|---|---|---|---|
| SWE-bench Verified | Claude Opus 4.5 | 80.9% | Claude Opus 4.6 | 80.8% | ~77% (est.) |
| SWE-bench Pro | GPT-5.4 | 57.7% | GPT-5.2-Codex | 56.4% | N/A |
| Terminal-Bench 2.0 | Gemini 3.1 Pro | 78.4% | GPT-5.3-Codex | 77.3% | N/A |
| OSWorld-Verified | GPT-5.4 | 75.0% | Claude Opus 4.6 | 72.7% | 72.4% |
| WebVoyager | Project Mariner | 83.5% | — | — | ~78% |
| GAIA (test) | h2oGPTe | 75% | — | — | 92% |
| HumanEval | Kimi K2.5 | 99.0% | Claude Sonnet 4.5 | 97.6% | ~95% (est.) |

### SWE-bench Verified
- **What it measures**: 500 Python tasks — "remains the most-watched coding benchmark despite acknowledged contamination." (p.5)
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "Claude Opus 4.5 at 80.9%, with Claude Opus 4.6 at 80.8%, Gemini 3.1 Pro at 80.6%, open-weight MiniMax M2.5 at 80.2%, GPT-5.2 at 80.0%, and Claude Sonnet 4.6 at 79.6%."
- **Trajectory data**: "six frontier models sit within 1.3 points on SWE-bench Verified, making the benchmark nearly saturated amid significant contamination concerns."
- **Page ref**: p.5

### SWE-bench Pro
- **What it measures**: "1,865 tasks across Python, Go, TypeScript, and JavaScript using private codebases" — designed because "SWE-bench Verified shows far more separation."
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "GPT-5.4 leads at 57.7%."
- **Trajectory data**: "Claude Opus 4.5 scores 45.9% on Scale AI's standardized SEAL scaffold. The gap between Verified (~81%) and Pro (~46–58%) starkly illustrates contamination's distorting effect."
- **Page ref**: p.5

### Terminal-Bench 2.0
- **What it measures**: "Introduced by Stanford and the Laude Institute, has emerged as the most respected new agentic benchmark. It tests agents across 89 real-world terminal tasks spanning software engineering, biology, security, and gaming in Docker containers."
- **Concrete example task**: PDF doesn't show specific example
- **Saturation status / current SOTA**: "Gemini 3.1 Pro leads at 78.4% (via Forge Code scaffold), followed by GPT-5.3-Codex at 77.3% and GPT-5.4 at 75.1%."
- **Trajectory data**: "On the harder Terminal-Bench Hard subset, GPT-5.4 leads at 57.6%, with Gemini 3.1 Pro and Claude Sonnet 4.6 tied at 53%."
- **Page ref**: p.5

### OSWorld-Verified
- **What it measures**: "369 tasks across Ubuntu, Windows, and macOS involving desktop apps, web apps, and multi-application workflows." (p.5–6)
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "GPT-5.4's 75.0% score exceeding the 72.4% human expert baseline — the first superhuman result on a comprehensive computer-use benchmark." Claude Opus 4.6 scored 72.7%, "effectively matching human performance."
- **Trajectory data**: "An Epoch AI critique noted that ~15% of tasks can be solved via terminal rather than GUI interaction, but the result remains significant."
- **Page ref**: p.5–6

### GAIA (General AI Assistants)
- **What it measures**: "Tests 466 multi-step questions requiring reasoning, web browsing, and tool use."
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "H2O.ai's h2oGPTe agent leads the test set at 75% — the first 'C grade' on the benchmark, still far below the 92% human baseline." "Manus AI scored 57.7% on the validation set."
- **Trajectory data**: Only two data points given.
- **Page ref**: p.6

### Tau-bench
- **What it measures**: Customer service agents — "highlights reliability challenges."
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "Even frontier models succeed on fewer than 50% of retail tasks, and pass-8 rates drop below 25%. StepFun's Step-3.5-Flash leads at 0.882."
- **Trajectory data**: (not present in source)
- **Page ref**: p.6

### WebVoyager
- **What it measures**: Web browsing agents; human baseline ~78%.
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "Project Mariner 83.5%." Cited earlier: "Google's Project Mariner, available to AI Ultra subscribers, achieved 83.5% on the WebVoyager benchmark and now supports up to 10 concurrent browser tasks."
- **Trajectory data**: (not present in source)
- **Page ref**: p.2 / p.6 table

### HumanEval
- **What it measures**: "Effectively dead as a differentiator."
- **Concrete example task**: PDF doesn't show example
- **Saturation status / current SOTA**: "Kimi K2.5 scores 99.0%, the average across 74 tracked models is 89.6%, and training-data contamination is well-documented. LiveCodeBench and SWE-bench Pro have replaced it for frontier comparisons."
- **Trajectory data**: Average across 74 tracked models = 89.6%.
- **Page ref**: p.6

### Other benchmarks named
- **WebArena-Verified**: GPT-5.4 at 67.3%. (p.3)
- **Online-Mind2Web**: GPT-5.4 at 92.8%. (p.3)
- **ARC-AGI-2**: Gemini 3.1 Pro at 77.1%. (p.3)
- **MCP Atlas**: tool-search reduced tokens by 47%. (p.3)
- **PropensityBench (Scale AI)**: "models using harmful tools 64% of the time when those tools were renamed with benign labels." (p.2)
- **LiveCodeBench**: named as HumanEval replacement, no score. (p.6)

## §5 Notable misc claims worth slide-quoting

Verbatim pull-quotes with page refs:

- **Task autonomy vs Moore's Law (p.2, confirmed p.7)**: "AI task autonomy is doubling every 7 months — 3x faster than Moore's Law." Source pill: Taskade (p.2 and p.7); corroborated by the International AI Safety Report 2026 led by Yoshua Bengio and backed by 30+ countries.

- **Scaffolding swings scores (p.6, confirmed from p.5)**: "The same model can score 10-22 points differently depending on the harness. Claude Opus 4.5 ranged from 45.9% (standardized scaffold) to 55.4% (optimized scaffold) on SWE-bench Pro. This validates the industry's shift toward harness engineering as a core competency." Also (p.5): "Grok 4 self-reports 72-75% but measures 58.6% under controlled conditions." Also (p.5): "independent effort by vals.ai, found that self-reported scores often exceed standardized evaluations by 10-20 points."

- **Infrastructure layer is the new moat (p.6–7, conclusion heading)**: Full heading: "Conclusion: the infrastructure layer is the new moat." Key sentence: "The competitive frontier has shifted from model performance — where six models cluster within 1.3 points on SWE-bench — to agent infrastructure: harness engineering, protocol integration, enterprise governance, and safety architecture." And: "Meta's $2 billion Manus acquisition was for the execution layer, not the model." And: "Harrison Chase's dictum holds: better models alone won't get agents to production."

- **"New king of the hill every 60 days" (p.4)**: "Microsoft CMO Jared Spataro candidly acknowledged: 'Every 60 days, there's a new king of the hill.'"

- **Harness and context engineering (p.5)**: "Harrison Chase of LangChain argued that 'when agents mess up, they mess up because they don't have the right context' — and the competitive moat is shifting from model quality to integration, orchestration, and permission architectures." "Andrej Karpathy's viral declaration — 'Code's not even the right verb anymore... I have to express my will to my agents for 16 hours a day' — captured the practitioner mindset shift. His AutoResearch script (630 lines of Python, 61,000+ GitHub stars) ran 700 experiments autonomously in 2 days, finding 20 optimizations that improved LLM training time."

- **"Top-tier convergence, scaffold dependence, and growing contamination concerns" (p.5)**: "The agentic benchmark landscape in early 2026 is defined by three dynamics: top-tier convergence, scaffold dependence, and growing contamination concerns."

- **Safety gap widening (p.7)**: "Third, the safety gap is widening faster than the capability gap is closing. Agent task autonomy doubles every 7 months while safety testing becomes less reliable — models now distinguish between test and production environments."

- **OpenClaw security disaster (p.7)**: "The OpenClaw security debacle (12% malicious marketplace skills, one-click RCE vulnerabilities) and real-world incidents of agents ignoring explicit instructions demonstrate that governance infrastructure is not optional."

- **Final strategic framing (p.7)**: "OpenAI is betting on a superapp strategy consolidating Codex, ChatGPT, and Atlas. Anthropic is betting that safety leadership and MCP ubiquity create a trust moat. Google is betting that breadth across coding, browser, multimodal, and on-device agents captures the most surface area. Microsoft is betting that enterprise governance and multi-model flexibility win the workplace. The race is no longer about intelligence. It is about infrastructure."

- **Mass-market China frenzy (p.1)**: "demonstrated mass-market appetite for computer-controlling agents, triggering adoption frenzies in China where people queued outside Tencent offices for installation help before security vulnerabilities forced early pullbacks."

## §6 Citation footprint

- **Author name**: NOT VISIBLE. No byline, institutional masthead, or contributor credit appears anywhere in the 7 pages.
- **Publication / URL**: NOT VISIBLE. No publisher logo, footer URL, or watermark. Inline "pill" tags (Morph, Anthropic, VentureBeat, Fortune, TechCrunch, CNBC, Wikipedia, DataCamp, OpenAI, Google Developers, Softmax Data Blog, ItemalTechnologies, Morph+2, Marco Patzelt, Osworld, OpenReview, Epoch AI, Hugging Face, Towards Data Science, H2O.ai, VentureBeat, o-mega, LLM Leaderboard, Taskade, Internationalaisafetyreport, Zylos, Kiteworks, Nerdleveltech, Fortune+3, Xpert, L'EssentielDeL'IA, Artificial Analysis, Rootly) look like upstream source citations inside the doc, not the publisher of the doc itself.
- **Date**: NOT VISIBLE in-doc. The title states "Q1 2026 Competitive Landscape" and the content references events through **April 3 and April 2** (Windows rollout of Claude Computer Use, Gemma 4 launch), so compiled **early April 2026** at earliest. Filesystem mtime (2026-04-12) matches Louis's framing of 2026-04-13 deck.
- **Recommended in-deck citation display**: `"Arms Race Report Q1 2026 (internal brief)"` — until Louis supplies the actual author/publisher. Alternate if it's a public analyst doc: `"The Agentic AI Arms Race — Q1 2026, [Pub]"`.
- **Caveat to flag**: No visible author or URL. Many numeric claims (ARR figures, investment rounds, benchmark scores) are sourced to pill tags but those pills aren't hyperlinked in the PDF — each cited data point would need an independent verification pass before public use. Treat the extract as a lead-generation doc, not a primary source.
