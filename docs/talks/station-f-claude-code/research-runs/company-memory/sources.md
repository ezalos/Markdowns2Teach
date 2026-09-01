# Sources — company-memory systems for agents (September 2026)

All 33 sources below were fetched during this run and quoted verbatim from the page.
Accessed date is the date I retrieved and read the page.

---

**[1]** [MemGPT: Towards LLMs as Operating Systems — arXiv:2310.08560](https://arxiv.org/abs/2310.08560)
Authority: arXiv (Packer, Wooders, Lin, Fang, Patil, Stoica, Gonzalez — UC Berkeley) · Accessed: 2026-09-01
> "Submitted on 12 Oct 2023"
> "we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory."

**[2]** [Zep AI — Y Combinator company profile](https://www.ycombinator.com/companies/zep-ai)
Authority: Y Combinator · Accessed: 2026-09-01
> "Zep AI Founded: 2023 Batch: Winter 2024 Team Size: 5 Status: Active Location: San Francisco"

**[3]** [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory — arXiv:2504.19413 (HTML)](https://arxiv.org/html/2504.19413v1)
Authority: arXiv (Chhikara, Khant, Aryan, Singh, Yadav — Mem0) · Accessed: 2026-09-01
> "Despite these improvements, a full-context method that ingests a chunk of roughly 26,000 tokens still achieves the highest J score (approximately 73%). However, as shown in Figure 4(b) , it also incurs a very high total p95 latency—around 17 seconds—since the model must read the entire conversation on every query. By contrast, Mem0 and Mem0 g \\texttt{Mem0}^{\\tiny g} significantly reduce token usage and thus achieve lower p95 latencies of around 1.44 seconds (a 92% reduction) and 2.6 seconds (a 85% reduction), respectively over full-context approach."
> (Table 2, Overall J / avg memory tokens: Full-context 26031 / 72.90%; Zep 3911 / 65.99%; Mem0 1764 / 66.88%; Mem0ᵍ 3616 / 68.44%)

**[4]** [Zep: A Temporal Knowledge Graph Architecture for Agent Memory — arXiv:2501.13956 (HTML)](https://arxiv.org/html/2501.13956v1)
Authority: arXiv (Rasmussen, Paliychuk, Beauvais, Ryan, Chalef — Zep AI) · Accessed: 2026-09-01
> "Zep demonstrates substantial improvements in both accuracy and latency compared to the baseline across both model variants. Using gpt-4o-mini, Zep achieved a 15.2% accuracy improvement over the baseline, while gpt-4o showed an 18.5% improvement."
> "We conducted all experiments between December 2024 and January 2025. We performed testing using a consumer laptop from a residential location in Boston, MA, connecting to Zep's service hosted in AWS us-west-2."
> (Table 2: Full-context gpt-4o 60.2% / 28.9 s / 115k tokens; Zep gpt-4o 71.2% / 2.58 s / 1.6k tokens. Table 3, knowledge-update, gpt-4o-mini: Full-context 76.9%, Zep 74.4%)

**[5]** [Observational Memory: 95% on LongMemEval — Mastra Research](https://mastra.ai/research/observational-memory)
Authority: Mastra (Tyler Barnes), published 2026-02-09 · Accessed: 2026-09-01
> "Observational Memory (OM), a new memory system developed by Mastra, achieves SOTA on LongMemEval with an 84.23% gpt-4o score — outperforming the oracle (a configuration given only the conversations containing the answer). With gpt-5-mini , it scores 94.87% — the highest score ever recorded on this benchmark, by any system, with any model."

**[6]** [Zep: A Temporal Knowledge Graph Architecture for Agent Memory — arXiv:2501.13956 (abstract)](https://arxiv.org/abs/2501.13956)
Authority: arXiv · Submitted 20 Jan 2025 · Accessed: 2026-09-01
> "Zep addresses this fundamental limitation through its core component Graphiti -- a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships."
> "In this evaluation, Zep achieves substantial results with accuracy improvements of up to 18.5% while simultaneously reducing response latency by 90% compared to baseline implementations."

**[7]** [Beyond a Million Tokens: Benchmarking and Enhancing Long-Term Memory in LLMs — arXiv:2510.27246](https://arxiv.org/abs/2510.27246)
Authority: arXiv (Tavakoli et al.; ICLR 2026) · Submitted 31 Oct 2025 · Accessed: 2026-09-01
> "we construct BEAM, a new benchmark comprising 100 conversations and 2,000 validated questions."
> "Our experiments on BEAM reveal that even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen. In contrast, LIGHT consistently improves performance across various models, achieving an average improvement of 3.5%-12.69% over the strongest baselines, depending on the backbone LLM."

**[8]** [Benchmarking AI Agent Memory: Is a Filesystem All You Need? — Letta Research Blog](https://www.letta.com/blog/benchmarking-ai-agent-memory/)
Authority: Letta, published 2025-08-12 · Accessed: 2026-09-01
> "Letta agents running on gpt-4o-mini achieve 74.0% accuracy on LoCoMo by simply storing conversation histories in files, rather than using specialized memory or retrieval tools."
> "This simple agent achieves 74.0% on LoCoMo with GPT-4o mini and minimal prompt tuning, significantly above Mem0's reported 68.5% score for their top-performing graph variant."
> "Agents today are extremely effective at using filesystem tools, largely due to post-training optimization for agentic coding tasks. In general, simpler tools are more likely to be in the training data of an agent and therefore more likely to be used effectively."

**[9]** [We audited LoCoMo: 6.4% of the answer key is wrong and the judge accepts up to 63% of intentionally wrong answers — Penfield Labs](https://penfieldlabs.substack.com/p/we-audited-locomo-64-of-the-answer)
Authority: Penfield Labs (non-peer-reviewed, artifacts at github.com/dial481/locomo-audit), published 2026-04-08 · Accessed: 2026-09-01
> "We conducted a systematic audit of the ground truth and identified 99 score-corrupting errors in 1,540 questions (6.4%). Error categories include hallucinated facts in the answer key, incorrect temporal reasoning, and speaker attribution errors."
> "The theoretical maximum score for a perfect system is approximately 93.6%."
> "We generated intentionally wrong but topically adjacent answers for all 1,540 questions and scored them using the same judge configuration and prompts used in published evaluations. The judge accepted 62.81% of them."
> "LongMemEval-S is often raised as an alternative, but each question's corpus fits entirely in modern context windows, making it more of a context window test than a memory test."
> "Mastra's research illustrates this: their full-context baseline scored 60.20% with gpt-4o (128K context window, near the 115K threshold). Their observational memory system scored 84.23% with the same model"

**[10]** [mem0ai/mem0 — GitHub repository metadata (REST API)](https://api.github.com/repos/mem0ai/mem0)
Authority: GitHub · Retrieved: 2026-09-01T12:20:17Z
> `"full_name": "mem0ai/mem0"` … `"stargazers_count": 64506` … `"forks_count": 7557` … `"pushed_at": "2026-08-31T21:04:52Z"`
> `"description": "The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists."`

**[11]** [Mem0 Raises $24M Series A to Build Memory Layer for AI Agents — PR Newswire](https://www.prnewswire.com/news-releases/mem0-raises-24m-series-a-to-build-memory-layer-for-ai-agents-302597157.html)
Authority: Mem0 via PR Newswire, dated 2025-10-28 · Accessed: 2026-09-01
> "SAN FRANCISCO , Oct. 28, 2025 /PRNewswire/ -- Mem0, a memory infrastructure platform for AI agents, today announced $24M in funding: a Seed led by Kindred Ventures and Series A led by Basis Set Ventures, with participation from Peak XV Partners, GitHub Fund, and Y Combinator."
> "Since launching, they've reached 41,000 GitHub stars and 14 million downloads, with API calls growing from 35 million in Q1 to 186 million in Q3 2025. Thousands of teams, from startups to Fortune 500 companies, now use Mem0 in production."

**[12]** [Memory Blocks: The Key to Agentic Context Management — Letta Blog](https://www.letta.com/blog/memory-blocks/)
Authority: Letta, published 2025-05-14 · Accessed: 2026-09-01
> "The idea of an agent that could manage its own memory (including its own context window) originated in the MemGPT paper . MemGPT demonstrated the idea of self-editing memory in a simple chat use-case with two in-context memory blocks"

**[13]** [letta-ai/letta — GitHub repository metadata (REST API)](https://api.github.com/repos/letta-ai/letta)
Authority: GitHub · Retrieved: 2026-09-01T12:20:17Z
> `"full_name": "letta-ai/letta"` … `"stargazers_count": 24527` … `"forks_count": 2606` … `"pushed_at": "2026-08-23T19:05:43Z"`
> `"description": "Platform for stateful agents: AI with advanced memory that can learn and self-improve over time."`

**[14]** [Berkeley AI Research Lab Spinout Letta Raises $10M Seed Financing Led by Felicis to Build AI with Memory — PR Newswire](https://www.prnewswire.com/news-releases/berkeley-ai-research-lab-spinout-letta-raises-10m-seed-financing-led-by-felicis-to-build-ai-with-memory-302257004.html)
Authority: Letta via PR Newswire, dated 2024-09-24 · Accessed: 2026-09-01
> "SAN FRANCISCO , Sept. 24, 2024 /PRNewswire/ -- Letta , a new generative AI startup spun out of UC Berkeley's AI research lab, emerged from stealth today with a $10 million seed round led by Felicis with participation from Sunflower Capital and Essence VC. Notable angels include Jeff Dean (Chief Scientist at Google DeepMind), Clem Delangue (CEO of HuggingFace)"

**[15]** [getzep/graphiti — GitHub repository metadata (REST API)](https://api.github.com/repos/getzep/graphiti)
Authority: GitHub · Retrieved: 2026-09-01T12:20:17Z
> `"full_name": "getzep/graphiti"` … `"stargazers_count": 30485` … `"forks_count": 3094` … `"pushed_at": "2026-09-01T03:05:06Z"`
> `"description": "Build Real-Time Knowledge Graphs for AI Agents"`

**[16]** [Agents that remember: introducing Agent Memory — Cloudflare Blog](https://blog.cloudflare.com/introducing-agent-memory/)
Authority: Cloudflare (first-party engineering post), published 2026-04-17 · Accessed: 2026-09-01
> "Today we're announcing the private beta of Agent Memory , a managed service that extracts information from agent conversations and makes it available when it's needed, without filling up the context window."
> "Agentic memory is one of the fastest-moving spaces in AI infrastructure, with new open-source libraries, managed services, and research prototypes launching on a near-weekly basis."
> "Tighter ingestion and retrieval pipelines are superior to giving agents raw filesystem access. In addition to improved cost and performance, they provide a better foundation for complex reasoning tasks required in production, like temporal logic, supersession, and instruction following."
> "Ingestion extracts facts, events, instructions, and tasks from the message history, deduplicates them against existing memories, and stores them as memories for future retrieval."
> "when a new memory has the same key as an existing one, the old memory is superseded rather than deleted. This creates a version chain with a forward pointer from the old memory to the new memory."
> "During development, we discovered that no single retrieval method works best for all queries, so we run several methods in parallel and fuse the results."
> "results from all five retrieval channels are merged using Reciprocal Rank Fusion (RRF)"

**[17]** [Effective context engineering for AI agents — Anthropic Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
Authority: Anthropic, dated 2025-09-29 · Accessed: 2026-09-01
> "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times. This strategy provides persistent memory with minimal overhead."
> "The agent maintains precise tallies across thousands of game steps, and after context resets, the agent reads its own notes and continues multi-hour training sequences. This coherence across summarization steps enables long-horizon strategies that would be impossible when keeping all the information in the LLM's context window alone."
> "As part of our Sonnet 4.5 launch , we released a memory tool in public beta on the Claude Developer Platform that makes it easier to store and consult information outside the context window through a file-based system."

**[18]** [Introducing Agent Skills — Anthropic](https://claude.com/blog/skills)
Authority: Anthropic, dated 2025-10-16 (updated 2025-12-18) · Accessed: 2026-09-01
> "Skills are folders that include instructions, scripts, and resources that Claude can load when needed. Claude will only access a skill when it's relevant to the task at hand."
> "Portable : Skills use the same format everywhere. Build once, use across Claude apps, Claude Code, and API."

**[19]** [Memory tool — Claude Docs](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
Authority: Anthropic (first-party documentation) · Accessed: 2026-09-01
> "The /memories path is a prefix that your handler maps onto real storage, such as a per-user directory or keys in a database. Memory lives entirely in your application."

**[20]** [Code w/ Claude SF 2026: Building on the AI exponential — Anthropic](https://claude.com/blog/code-w-claude-sf-2026-sf)
Authority: Anthropic, dated 2026-05-12 · Accessed: 2026-09-01
> "Dreaming. A scheduled process that reviews past agent sessions, surfaces patterns, and curates memory, so agents improve between runs. Recurring mistakes, shared workflows, and team preferences get pulled into a more useful memory store."

**[21]** [Is Mem0 Really SOTA in Agent Memory? — Zep Blog](https://blog.getzep.com/lies-damn-lies-statistics-is-mem0-really-sota-in-agent-memory/)
Authority: Zep AI (competitor rebuttal — self-interested) · Accessed: 2026-09-01
> "We've updated the article to reflect Zep's corrected result is 75.14% +/- 0.17, with Zep outperforming Mem0 by 10%."
> "Tellingly, Mem0's own results show their system being outperformed by a simple full-context baseline (feeding the entire conversation to the LLM), which achieved a J score of ~73%, compared to Mem0's best score of ~68%. If simply providing all the text yields better results than the specialized memory system, the benchmark isn't adequately stressing memory capabilities representative of real-world agent interactions."

**[22]** [LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory — arXiv:2410.10813](https://arxiv.org/abs/2410.10813)
Authority: arXiv (Wu, Wang, Yu, Zhang, Chang, Yu; ICLR 2025) · Submitted 14 Oct 2024, v2 4 Mar 2025 · Accessed: 2026-09-01
> "We introduce LongMemEval, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, LongMemEval presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions."

**[23]** [LOCA-bench: Benchmarking Language Agents Under Controllable and Extreme Context Growth — arXiv:2602.07962](https://arxiv.org/abs/2602.07962)
Authority: arXiv · Submitted 8 Feb 2026 · Accessed: 2026-09-01
> "While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate."

**[24]** [LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues — arXiv:2605.12493](https://arxiv.org/abs/2605.12493)
Authority: arXiv · Submitted 12 May 2026 · Accessed: 2026-09-01
> "LME-V2 contains 451 manually curated questions covering five core memory abilities for web agents: static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness. Questions are paired with history trajectories containing up to 500 trajectories and 115M tokens."

**[25]** [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution — arXiv:2608.27454 (HTML)](https://arxiv.org/html/2608.27454)
Authority: arXiv (Tang, Rashtchian, Ferng, Tomkins, Juan, Vu — Google Research / Virginia Tech) · Submitted 27 Aug 2026 · Accessed: 2026-09-01
> "Within the Qwen family, WikiSkill improves average performance by 12.3%, 17.5%, and 23.9% for 4B, 9B, and 27B models, respectively, with gains increasing with model scale . At the same time, evolved skills can compensate for substantial model scale: Qwen-3.5-9B with WikiSkill outperforms Qwen-3.6-27B without skills (47.4% vs. 39.4%)."
> "across five benchmarks spanning diverse domains: mathematical reasoning ( LiveMathematicianBench (LiveMath) ( He et al., 2026 ) ), web search ( SealQA ( Pham et al., 2026 ) ), spreadsheet manipulation ( SpreadsheetBench (Ma et al., 2024) ), long-context document question answering OfficeQA"
> "The Wiki Layer preserves recurring errors, rejected proposals, and evolution history, which provide the Skill Proposer with accumulated context for subsequent updates."

**[26]** [WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution — arXiv:2608.27454 (abstract)](https://arxiv.org/abs/2608.27454)
Authority: arXiv · Submitted 27 Aug 2026 · Accessed: 2026-09-01
> "[Submitted on 27 Aug 2026]"
> "Finally, our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution."
> "We find that skill evolution complements model scaling: larger models generally benefit more from evolved skills, while smaller models with skills can outperform substantially larger models without them."

**[27]** [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models — arXiv:2510.04618](https://arxiv.org/abs/2510.04618)
Authority: arXiv (Zhang, Hu, Upasani, … Zou, Olukotun — Stanford / SambaNova) · Submitted 6 Oct 2025 · Accessed: 2026-09-01
> "Prior approaches improve usability but often suffer from brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time. We introduce ACE (Agentic Context Engineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation."
> "consistently outperforming strong baselines: +10.6% on agents and +8.6% on finance"
> "On the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split, despite using a smaller open-source model."

**[28]** [Cognee Raises $7.5M Seed to Build Memory for AI Agents — Cognee Blog](https://www.cognee.ai/blog/cognee-news/cognee-raises-seven-million-five-hundred-thousand-dollars-seed)
Authority: Cognee (company announcement), dated 2026-02-19 · Accessed: 2026-09-01
> "Cognee News Feb 19, 2026"
> "Today, I am proud to announce that Cognee has raised a $7.5 million seed round led by Pebblebed , with participation from 42CAP and Vermilion Ventures , and angel investors from Google DeepMind , n8n , and Snowplow ."

**[29]** [Interloom Raises $16.5M to Give AI Agents "Enterprise Memory" — Interloom Blog](https://interloom.com/en/blog/seed-announcement/)
Authority: Interloom (company announcement), published 2026-03-23 · Accessed: 2026-09-01
> "Munich / Berlin / London – March 19th, 2026 – Interloom, the enterprise operations platform that captures expert knowledge and transforms it into permanent memory for AI agents, today announced a $16.5 million seed round . The investment was led by DN Capital , with participation from Bek Ventures and existing investor Air Street Capital ."
> "Interloom is already solving this for leading enterprises including Zurich Insurance and Fiege , processing millions of cases to bridge this "context gap.""

**[30]** [Memory Injection Attacks on LLM Agents via Query-Only Interaction — arXiv:2503.03704](https://arxiv.org/abs/2503.03704)
Authority: arXiv (NeurIPS 2025) · Submitted 5 Mar 2025 · Accessed: 2026-09-01
> "we propose a novel Memory INJection Attack, MINJA, without assuming that the attacker can directly modify the memory bank of the agent. The attacker injects malicious records into the memory bank by only interacting with the agent via queries and output observations."
> "With minimal requirements for execution, MINJA enables any user to influence agent memory, highlighting the risk."

**[31]** [Memory Poisoning Attack and Defense on Memory Based LLM-Agents — arXiv:2601.05504](https://arxiv.org/abs/2601.05504)
Authority: arXiv · Submitted 9 Jan 2026 · Accessed: 2026-09-01
> "Recent work demonstrated that the MINJA (Memory Injection Attack) achieves over 95 % injection success rate and 70 % attack success rate under idealized conditions."
> "Our experiments on GPT-4o-mini, Gemini-2.0-Flash and Llama-3.1-8B-Instruct models using MIMIC-III clinical data reveal that realistic conditions with pre-existing legitimate memories dramatically reduce attack effectiveness. We then propose and evaluate two novel defense mechanisms: (1) Input/Output Moderation using composite trust scoring across multiple orthogonal signals, and (2) Memory Sanitization with trust-aware retrieval employing temporal decay and pattern-based filtering."

**[32]** [Beyond Similarity Search: Tenure and the Case for Structured Belief State in LLM Memory — arXiv:2605.11325 (HTML)](https://arxiv.org/html/2605.11325v1)
Authority: arXiv (Jeffrey Flynt, independent researcher — author of the tool evaluated; N = 72 cases) · Submitted 11 May 2026 · Accessed: 2026-09-01
> "Similarity search fails for named entity resolution within bounded vocabulary contexts because beliefs about a shared technical domain are semantically proximate by construction. A single user is the simplest bounded vocabulary context; engineering teams converge on the same property through shared codebases and terminology."
> "A controlled evaluation on 72 retrieval cases demonstrates the gap. Cosine similarity over dense embeddings achieves mean precision of 0.12. Alias-weighted BM25 maintains mean precision of 1.0, passing 72/72 cases versus 8/72 for cosine similarity on the same corpus."
> "Under multi-turn topic drift this worsens: the vector backend produces drift scores of 0.43–0.50 on noise-critical turns where BM25 maintains 0."
> "Hard scope isolation provides a structural guarantee: the right beliefs surface, and only within the boundaries the user has authorized."

**[33]** [Unveiling Privacy Risks in LLM Agent Memory — arXiv:2502.13172](https://arxiv.org/abs/2502.13172)
Authority: arXiv (ACL 2025) · Submitted 17 Feb 2025 · Accessed: 2026-09-01
> "They enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks for LLM agents. In this work, we systematically investigate the vulnerability of LLM agents to our proposed Memory EXTRaction Attack (MEXTRA) under a black-box setting."
> "Experiments on two representative agents demonstrate the effectiveness of MEXTRA."
> "Our findings highlight the urgent need for effective memory safeguards in LLM agent design and deployment."
