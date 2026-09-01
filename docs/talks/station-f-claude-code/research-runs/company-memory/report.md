# The real state of company-memory systems for agents — September 2026

**Run date:** 2026-09-01 · **Feeds:** S52 "The company brain", Station F founders' talk 2026-09-02
**Sources:** 33, all fetched and quoted (see `sources.md`). Repository and funding figures carry a retrieval date.

---

## Headline for the slide

Four things are true at once, and the honest version of the slide says all four:

1. **The category is not new.** Its founding paper, MemGPT, was submitted 12 October 2023 [1]. Zep was founded in 2023 and went through Y Combinator's Winter 2024 batch [2]. The "less than six months old" marketing framing is false by roughly three years.
2. **Written memory does not beat long context everywhere — it beats it past a corpus threshold.** At ~26k tokens, mem0's own paper shows a plain full-context baseline winning outright [3]. At ~115k tokens, memory systems win by 11 to 24 points [4][5][6]. At 1M–10M tokens, independent academic work shows long context failing on its own [7].
3. **Plain files are a real contender, measured.** Letta's own research found an agent that just puts the conversation in a file and greps it scores **74.0%** on LoCoMo — above every specialised memory product in mem0's table, and above the full-context baseline [8][3].
4. **The benchmarks the vendors quote are broken enough to matter.** An audit of LoCoMo found 6.4% of the answer key wrong and the LLM judge accepting 62.81% of deliberately wrong answers [9].

---

## 1. Named systems

Every "one defensible number" below is either a first-party primary announcement or a repository count I retrieved myself. Self-reported benchmark claims are marked and never used as the headline number.

| System | What it stores & retrieves | Architecture in one sentence | One defensible number (date) | Source | Verbatim quote | Self-reported? |
|---|---|---|---|---|---|---|
| **mem0** | Salient facts extracted from conversation turns, as natural-language memories; graph variant (Mem0ᵍ) also stores entities and relations | An LLM extraction-and-consolidation pipeline that turns dialogue into a compact fact store, retrieved by semantic search at query time [3] | **64,506 GitHub stars** (retrieved 2026-09-01) | [10] | `"stargazers_count": 64506` | No — measured by me |
| **mem0** (funding) | — | — | **$24M** seed + Series A, announced **2025-10-28** | [11] | "today announced $24M in funding: a Seed led by Kindred Ventures and Series A led by Basis Set Ventures" | No — company announcement |
| **Letta** (MemGPT lineage) | Core memory blocks held in context, plus recall (full history) and archival (vector) tiers; agent edits its own memory via tool calls | An OS-inspired virtual-memory manager that pages information between the context window and external tiers, with the model itself issuing the page-in/page-out calls [1][12] | **24,527 GitHub stars** (retrieved 2026-09-01) | [13] | `"stargazers_count": 24527` | No — measured by me |
| **Letta** (funding) | — | — | **$10M** seed, announced **2024-09-24** | [14] | "emerged from stealth today with a $10 million seed round led by Felicis with participation from Sunflower Capital and Essence VC" | No — company announcement |
| **Zep / Graphiti** | Episodic nodes (raw messages), extracted entities and facts on bi-temporally validated edges, and community summaries | A temporally-aware knowledge-graph engine that ingests conversation and business data and keeps a record of when each fact was true [6] | **30,485 GitHub stars** on `getzep/graphiti` (retrieved 2026-09-01) | [15] | `"stargazers_count": 30485` | No — measured by me |
| **Cloudflare Agent Memory** | Facts, events, instructions and tasks extracted from agent conversations, deduplicated and version-chained on supersession | A managed ingestion-plus-retrieval service with a deliberately narrow tool surface (recall / remember / forget / list), fusing five retrieval channels with Reciprocal Rank Fusion [16] | Private beta announced **2026-04-17** | [16] | "Today we're announcing the private beta of Agent Memory, a managed service that extracts information from agent conversations and makes it available when it's needed" | No — first-party engineering post |
| **Anthropic** (the platform layer) | Files under a `/memories` path the model creates, reads, updates and deletes; plus Skills as versioned folders of instructions and scripts | A file-based memory tool whose storage the application owns, paired with structured note-taking as an explicit context-engineering technique [17][18][19] | Memory tool shipped in public beta with **Sonnet 4.5**; "Dreaming" — scheduled curation of past agent sessions — shipped **2026-05-12** | [18][20] | "Dreaming. A scheduled process that reviews past agent sessions, surfaces patterns, and curates memory, so agents improve between runs." | No — first-party announcement |

### Their own claimed benchmarks — all self-published, with methodology

| Claim | System | Setup | Caveat |
|---|---|---|---|
| **J = 68.44%** on LoCoMo (Mem0ᵍ), vs 65.99% for Zep and 72.90% for full context [3] | mem0 | LoCoMo, ~26k tokens/conversation, LLM-as-judge (J) | **Self-published.** Zep says mem0 mis-implemented Zep and that a correct run puts Zep at **75.14% ± 0.17** [21] — a direct, unresolved vendor dispute |
| **+18.5% accuracy, −90% latency** vs full-context baseline on LongMemEval [6] | Zep | LongMemEval-S, ~115k tokens/question; full-context gpt-4o 60.2% → Zep 71.2% at 1.6k context tokens [4] | **Self-published.** Experiments run Dec 2024–Jan 2025 from a consumer laptop in Boston against AWS us-west-2 [4] |
| **84.23% (gpt-4o) / 94.87% (gpt-5-mini)** on LongMemEval [5] | Mastra (Observational Memory) | Same benchmark; two background agents maintain a dense observation log replacing raw history | **Self-published.** Independently quoted with its 60.20% full-context baseline by the LoCoMo auditors [9] |
| **74.0%** on LoCoMo using only a filesystem [8] | Letta | gpt-4o-mini, LoCoMo transcript dropped into a file; agent given `grep`, `search_files`, `open`, `close` | **Self-published**, but the finding cuts *against* selling a memory product |

---

## 2. Does written memory beat long context?

**Verdict: yes, but only past a corpus size — and the crossover sits between roughly 26k and 115k tokens. Below it, long context wins on accuracy and memory wins only on cost and latency. The strongest evidence for memory is independent and academic; the strongest evidence at the crossover is vendor-run.**

### The evidence, in order of corpus size

**At ~26k tokens, long context wins outright.** mem0's own paper reports its best variant at 68.44% against a full-context baseline at 72.90% [3]. The paper says so plainly: "Despite these improvements, a full-context method that ingests a chunk of roughly 26,000 tokens still achieves the highest J score (approximately 73%)" [3]. What memory buys at this scale is not accuracy — it is 1,764 memory tokens instead of 26,031, and a p95 total latency of 1.44s instead of 17.1s [3]. That is a 92% latency reduction for a ~4.5-point accuracy loss. **This is the single most useful number on the slide, because it is the vendor conceding the point.**

**At ~115k tokens, memory wins by a wide margin.** Zep reports full-context gpt-4o at 60.2% and Zep at 71.2% on LongMemEval-S, using 1.6k context tokens instead of 115k: "Using gpt-4o-mini, Zep achieved a 15.2% accuracy improvement over the baseline, while gpt-4o showed an 18.5% improvement" [4]. Mastra reports 84.23% with the same model against the same 60.20% baseline [5][9]. The benchmark's own authors found "commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions" [22].

**At 1M–10M tokens, long context fails on its own terms.** BEAM (ICLR 2026, Tavakoli et al., independent of every vendor above) built 100 coherent conversations up to 10M tokens with 2,000 validated questions and concluded: "even LLMs with 1M token context windows (with and without retrieval-augmentation) struggle as dialogues lengthen" [7]. Their memory framework LIGHT gained "an average improvement of 3.5%-12.69% over the strongest baselines" [7]. LOCA-bench (Feb 2026) reaches the same place from the agent side: "While agent performance generally degrades as the environment states grow more complex, advanced context management techniques can substantially improve the overall success rate" [23].

### Where the evidence is thin — say this out loud

- **The crossover point is measured only by interested parties.** The 26k result is mem0's, the 115k results are Zep's and Mastra's. No neutral party has run the same memory systems across a token-size sweep. The shape of the curve is well supported; the exact crossover is not.
- **LoCoMo is not sound enough to carry a slide number.** The audit found "99 score-corrupting errors in 1,540 questions (6.4%)", computed a theoretical ceiling of ~93.6% for a perfect system, and found the gpt-4o-mini judge accepted 62.81% of intentionally wrong but topically adjacent answers [9]. Vague answers that name the right topic and get every detail wrong pass roughly two-thirds of the time — which is precisely the failure mode of weak retrieval.
- **LongMemEval-S may be measuring the wrong thing.** The same auditors argue "each question's corpus fits entirely in modern context windows, making it more of a context window test than a memory test" [9]. LongMemEval-V2 (May 2026) responds by moving to web-agent trajectories "containing up to 500 trajectories and 115M tokens" [24] — but I found no cross-system leaderboard on it yet.
- **Nobody has benchmarked a *company* memory.** Every benchmark named here is a user-assistant chat history or a single agent's trajectory. A shared corpus of a whole team's sessions — many authors, conflicting facts, access boundaries — has no public benchmark at all. This is the largest documented gap in this report, and it is exactly what the team in the room is building.

---

## 3. The academic bridge: WikiSkill

**The numbers check out against the paper.** WikiSkill (arXiv 2608.27454, submitted 27 August 2026, Google Research and Virginia Tech) states: "evolved skills can compensate for substantial model scale: Qwen-3.5-9B with WikiSkill outperforms Qwen-3.6-27B without skills (47.4% vs. 39.4%)" [25]. Two corrections to how it is usually retold:

- **The models are Qwen, not Google's.** The paper is from Google Research, but the 9B-beats-27B result is on Alibaba's Qwen family. Saying "Google's 9B model" on a slide would be wrong.
- **The gain grows with scale, it does not substitute for it.** "WikiSkill improves average performance by 12.3%, 17.5%, and 23.9% for 4B, 9B, and 27B models, respectively, with gains increasing with model scale" [25]. Skills are not a small-model rescue; the big model benefits more. The 9B-beats-27B line is a crossover, not a reversal of scaling.
- **Setup:** five benchmarks — LiveMath, SealQA, SpreadsheetBench, OfficeQA, ALFWorld — across five models from the Qwen, Gemma and Gemini families [25]. The 47.4 / 39.4 figures are averages across those five.

**Does the written knowledge carry the gain?** The paper's own ablation says yes: "our ablation studies confirm that persistent knowledge accumulation in the wiki is critical for effective skill evolution" [26]. Their analysis adds that "The Wiki Layer preserves recurring errors, rejected proposals, and evolution history, which provide the Skill Proposer with accumulated context for subsequent updates" [25].

**Independent replication: none exists.** The paper is five days old as of this run. What does exist is *convergent* independent work, which is worth more on a slide than a claim of replication:

- **ACE (Agentic Context Engineering)**, arXiv 2510.04618, 6 October 2025, Stanford and SambaNova — "treats contexts as evolving playbooks that accumulate, refine, and organize strategies", reporting "+10.6% on agents and +8.6% on finance" and, notably, matching "the top-ranked production-level agent on the overall average… despite using a smaller open-source model" [27]. That is the same shape of finding — written, accumulated context lets a smaller model punch above its weight — from a different lab, eleven months earlier.
- ACE also names the failure mode WikiSkill's wiki layer is designed against: "context collapse, where iterative rewriting erodes details over time" [27].

**Honest framing for the slide:** two independent groups, a year apart, found that accumulated *written* knowledge lets a smaller model beat a bigger one. Neither has been replicated by a third party. Say "converging evidence", not "established".

---

## 4. The do-it-yourself pattern: plain files plus version control

This is the best-evidenced part of the whole picture, and it is the pattern the speaker teaches.

**Anthropic publishes it as a named technique.** "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times. This strategy provides persistent memory with minimal overhead." [17] They report an agent that "maintains precise tallies across thousands of game steps, and after context resets, the agent reads its own notes and continues multi-hour training sequences" — coherence "that would be impossible when keeping all the information in the LLM's context window alone" [17].

**The platform ships it as files you own.** The memory tool's storage is the application's: "The `/memories` path is a prefix that your handler maps onto real storage, such as a per-user directory or keys in a database. Memory lives entirely in your application." [19] Agent Skills extend the same idea to procedural knowledge: "Skills are folders that include instructions, scripts, and resources that Claude can load when needed" [18] — folders, therefore diffable, reviewable and version-controllable by construction.

**And there is one measurement.** Letta, August 2025: "Letta agents running on gpt-4o-mini achieve 74.0% accuracy on LoCoMo by simply storing conversation histories in files, rather than using specialized memory or retrieval tools" [8]. Same benchmark, same weak model class, above mem0's 68.44% graph variant and above the 72.90% full-context baseline [3]. Their explanation is the interesting part: "Agents today are extremely effective at using filesystem tools, largely due to post-training optimization for agentic coding tasks. In general, simpler tools are more likely to be in the training data of an agent and therefore more likely to be used effectively." [8]

**The counter-position, from a production vendor.** Cloudflare, April 2026: "Tighter ingestion and retrieval pipelines are superior to giving agents raw filesystem access. In addition to improved cost and performance, they provide a better foundation for complex reasoning tasks required in production, like temporal logic, supersession, and instruction following." [16] Their objection is specifically that raw filesystem access makes the agent "burn tokens on storage and retrieval strategy instead of the actual task" [16].

**The gap:** Letta's is the only head-to-head measurement of the files pattern against dedicated memory products that I could find, it is vendor-run, and it is on the benchmark the auditors say is broken [9]. No one has measured plain-files-plus-git against a memory product on a multi-author company corpus. Say that.

---

## 5. Market signal: 2026 in agent-memory infrastructure

Primary announcements only. This list is not exhaustive — it is what I could verify from first-party pages or the announcing company.

| Date | Event | Amount | Detail | Source |
|---|---|---|---|---|
| 2024-09-24 | Letta emerges from stealth | $10M seed | Led by Felicis; angels include Jeff Dean, Clem Delangue | [14] |
| 2025-10-28 | mem0 announces funding | $24M (seed + Series A) | Kindred Ventures + Basis Set Ventures; "Thousands of teams, from startups to Fortune 500 companies, now use Mem0 in production" | [11] |
| 2026-02-19 | Cognee seed | $7.5M | Led by Pebblebed (Pamela Vagata, Keith Adams), with 42CAP and Vermilion Ventures | [28] |
| 2026-03-19 | Interloom seed | $16.5M | Led by DN Capital; named enterprise users Zurich Insurance and Fiege; explicitly "enterprise memory" for how work is done | [29] |
| 2026-04-17 | Cloudflare launches Agent Memory (private beta) | — | Hyperscale infra vendor entering the category with an opinionated managed service | [16] |
| 2026-05-12 | Anthropic ships "Dreaming" to Claude Managed Agents | — | Scheduled curation of past agent sessions into a shared memory store — the platform absorbing the company-memory pattern | [20] |

**Testing the "category is less than six months old" claim: it is false.**
- MemGPT, the founding paper, was submitted **12 October 2023** — nearly three years before this talk [1].
- Zep AI: "Founded: 2023 · Batch: Winter 2024" [2].
- Letta was funded in **September 2024** [14]; mem0's paper is from **April 2025** [3].

What *is* genuinely fast-moving is the release cadence, and Cloudflare says so as a first-party observer: "Agentic memory is one of the fastest-moving spaces in AI infrastructure, with new open-source libraries, managed services, and research prototypes launching on a near-weekly basis" [16]. That is the defensible version of the claim. "Six months old" is not.

---

## 6. Failure modes

| Failure mode | What the evidence says | Source | Documented mitigation |
|---|---|---|---|
| **Memory poisoning** | MINJA injects malicious records into an agent's memory bank "by only interacting with the agent via queries and output observations" — no privileged access, "any user" can do it [30]. Follow-up work confirms it "achieves over 95% injection success rate and 70% attack success rate under idealized conditions" [31] | [30][31] | Partial. Realistic conditions blunt it: "realistic conditions with pre-existing legitimate memories dramatically reduce attack effectiveness" [31]. Proposed defences are I/O moderation with composite trust scoring, and memory sanitization with temporal decay — but they require "careful trust threshold calibration" to avoid rejecting legitimate memories [31] |
| **Stale facts outliving their truth** | Measured, and memory can make it *worse*: on LongMemEval's knowledge-update category with gpt-4o-mini, the full-context baseline scored 76.9% and Zep 74.4% — the one category where the memory system lost [4]. Knowledge update is one of LongMemEval's five named core abilities precisely because assistants fail it [22] | [4][22] | Temporal graph edges: Graphiti is built to synthesise conversational and business data "while maintaining historical relationships" [6]. Cloudflare version-chains on a normalized topic key: "when a new memory has the same key as an existing one, the old memory is superseded rather than deleted… a version chain with a forward pointer" [16] |
| **Retrieval precision collapse** | In a bounded-vocabulary corpus — exactly what a single team's sessions are — dense embedding retrieval falls apart: "Cosine similarity over dense embeddings achieves mean precision of 0.12… passing 72/72 cases versus 8/72 for cosine similarity on the same corpus" for alias-weighted BM25 [32]. Under multi-turn topic drift "the vector backend produces drift scores of 0.43–0.50 on noise-critical turns where BM25 maintains 0" [32]. Agent-side, LOCA-bench confirms "agent performance generally degrades as the environment states grow more complex" [23] | [32][23] | Hybrid and fused retrieval. Cloudflare runs five channels in parallel — full-text with Porter stemming, exact fact-key lookup, raw message search, HyDE and direct vectors — merged with Reciprocal Rank Fusion, "because no single retrieval method works best for all queries" [16]. **Caveat:** [32] is a preprint by the author of the tool it evaluates, N = 72 cases |
| **Privacy exposure from a shared session corpus** | MEXTRA: "we systematically investigate the vulnerability of LLM agents to our proposed Memory EXTRaction Attack (MEXTRA) under a black-box setting… Experiments on two representative agents demonstrate the effectiveness of MEXTRA" [33] (ACL 2025). Agents "enhance decision-making by storing private user-agent interactions in the memory module for demonstrations, introducing new privacy risks" [33] | [33] | Weak. The paper's own conclusion is a call for work not yet done: "Our findings highlight the urgent need for effective memory safeguards in LLM agent design and deployment" [33]. Scope isolation is the proposed structural answer — "the right beliefs surface, and only within the boundaries the user has authorized" [32] — but it is a preprint, not a shipped standard. **This is the sharpest unsolved problem for a team pooling everyone's sessions.** |

---

## 7. Build versus buy for a five-person team

**Build.** At five people, your corpus is one team's files, and the only measurement of the plain-files pattern against dedicated memory products has files winning — 74.0% on LoCoMo with nothing but `grep` and `search_files` [8] — while Anthropic ships the pattern as a first-class technique with storage you own [17][19] and folders you can version-control [18].

**Buy when one of three thresholds trips, not before:** the corpus outgrows a context window and retrieval starts returning the semantically-near-but-wrong (dense retrieval hits 0.12 precision in bounded-vocabulary corpora [32]); facts start superseding each other faster than a human curates them (the one benchmark category where memory systems lose today [4]); or the corpus crosses an access boundary, at which point you need scope isolation you did not build, because memory extraction attacks work black-box [33].

---

## Documented gaps

- **No benchmark exists for company memory.** Every evaluation here is single-user chat or single-agent trajectory. Multi-author corpora with conflicting facts and access boundaries are unmeasured.
- **No independent replication of WikiSkill.** The paper is five days old. ACE [27] is convergent, not confirmatory.
- **No neutral crossover measurement.** The token size at which written memory overtakes long context is bracketed by vendor-run experiments (26k [3] vs 115k [4][5]) and never measured by a disinterested party.
- **No measurement of plain files versus a memory product on a team corpus.** Letta's result [8] is single-conversation, vendor-run, and on an audited-as-flawed benchmark [9].
- **Zep's funding could not be verified from a primary source.** Only aggregator profiles were available; no number is cited for it here.
- **Named production users could not be verified from primaries for mem0, Letta, Zep or Cloudflare.** mem0's announcement says only "Thousands of teams, from startups to Fortune 500 companies, now use Mem0 in production" without naming one [11]; the others name none. Interloom is the sole exception, naming Zurich Insurance and Fiege [29]. Do not put a customer logo on the slide for the other four.
