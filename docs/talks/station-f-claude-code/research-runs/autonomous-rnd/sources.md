# Sources — "What autonomous agent loops can actually do in R&D in 2026"

All URLs fetched and quoted on **2026-09-01**. Every entry below was retrieved and read; the quote is
copied verbatim from the fetched page. Sources that could not be fetched are listed in
`run-result.json` under `unverified` and back no `[n]` marker.

---

**[1] Prime Intellect — "Measuring Autonomous AI Research"**
<https://www.primeintellect.ai/blog/measuring-autonomous-research>
Authority: Prime Intellect (research lab blog, methodology + public traces). Author: Elie Bakouch.
Published: 2026-08-14. Accessed: 2026-09-01.
Verbatim: "To investigate, we ran 153 autonomous runs on the nanoGPT optimizer speedrun across 18
frontier models, testing multiple seeds per model." … "runs lasting up to eight days, 8xH200s per run,
and coverage of 18 models." … "None of the runs produced a fundamentally new method; the winning
ingredients are all similar to existing ones in the literature." … "Almost every model finds the same
winning ideas. What separates the best traces is what an experiment leaves behind." … "These
constraints come from earlier runs where models would abuse the number of samples to pass the
statistical test, kill runs way earlier than they should have, and so on." … "We were again surprised
by the lack of novelty. The models clearly understand the objects they manipulate at a deep level, and
yet very few genuinely new ideas emerge, which makes it hard to tell if this is an artifact of the
speedrun setup or a real capability limit." … "Anthropic's automated AI R&D evals optimize a model on a
CPU node (system card), OpenAI runs nanoGPT track 1 on one H100 for under a day (system card)." …
"A frozen verify.py accepts the claim if the eight-run mean beats 3.27859 instead of 3.28, a margin
that makes passing on luck alone roughly one-in-a-thousand" … "42 went further and discovered
something we never mentioned (on purpose): rerunning the same recipe on the same seed also moves the
loss because GPUs are not deterministic." … "The models all find similar ideas. What separates them is
how they run experiments." … "They kill families on one seed, treat their own crashes as proof the
idea is bad, and throw away small gains that don't clear the bar alone." … "The stronger models test
borderline results on three seeds instead of one, and only pay for eight when their noise model says
it's worth it. They also go back and re-test things, which is one of the key components of their
success: after every merge they re-ablate the stack and drop what stopped helping" … "Each model+harness
launches on a GPU node (8xH200s) in headless mode inside a simple sandbox (bwrap + network namespace)."

**[2] Prime Intellect — "NanoGPT Speedrun Frontier" (live leaderboard)**
<https://www.primeintellect.ai/research/nanogpt-speedrun>
Authority: Prime Intellect. Snapshot date: **2026-09-01** (leaderboard still moving; entries marked
"running"). Accessed: 2026-09-01.
Verbatim: "We ran 153 autonomous runs across 18 frontier models on the nanoGPT optimizer speedrun." …
"1 Fable 5 note 2,726 81.7% closed claude-code · high @24H 3,010 8.7 d" … "Fable 5 claude-code · high
note 2,726 81.7% 3,010 800M 1.1M 811 3k 8.7"

**[3] Andrej Karpathy — nanochat `dev/LEADERBOARD.md`**
<https://github.com/karpathy/nanochat/blob/master/dev/LEADERBOARD.md>
Authority: public repository by the person who built it. Runs dated 2026-01-29 to 2026-03-14.
Accessed: 2026-09-01 (fetched raw via raw.githubusercontent.com/karpathy/nanochat/master/dev/LEADERBOARD.md).
Verbatim: "The primary metric we care about is \"time to GPT-2\" - the wall clock time needed to
outperform the GPT-2 (1.6B) CORE metric on an 8XH100 GPU node." … "## Run 5 … Achieved Mar 9, 2026 on
commit `6ed7d1d`. … This commit is special because all of the improvements that went into this commit
came from fully autonomous \"research\" done by a private version of autoresearch run on a d12 model.
… The changes easily translated from d12 to d24, hence new leaderboard record, taking us from 2.02
hours \"time to GPT-2\" to 1.80 hours." … "## Run 6 … Achieved Mar 14, 2026 on commit `a825e63`. …
This set of changes came from autoresearch round 2, where I asked it to reference the modded-nanogpt
repo for inspiration. … in particular found a way to incorporate the backout and smear in such a way
that they are helpful (I had previously tried them manually a long time ago and they caused
regressions). … The average of 5 runs was CORE 0.262634 and each of them lasted 1.65 hours (99
minutes)."

**[4] Andrej Karpathy — `autoresearch` README**
<https://github.com/karpathy/autoresearch>
Authority: public repository by the author. Published: March 2026. Accessed: 2026-09-01 (fetched raw
via raw.githubusercontent.com/karpathy/autoresearch/master/README.md).
Verbatim: "The idea: give an AI agent a small but real LLM training setup and let it experiment
autonomously overnight. It modifies the code, trains for 5 minutes, checks if the result improved,
keeps or discards, and repeats." … "**`train.py`** — the single file the agent edits." … "**`program.md`**
— baseline instructions for one agent. Point your agent here and let it go. **This file is edited and
iterated on by the human**." … "By design, training runs for a **fixed 5-minute time budget** (wall
clock, excluding startup/compilation) … The metric is **val_bpb** (validation bits per byte) — lower is
better, and vocab-size-independent so architectural changes are fairly compared." … "**Requirements:**
A single NVIDIA GPU (tested on H100), Python 3.10+, [uv]" … "This means you can expect approx 12
experiments/hour and approx 100 experiments while you sleep." … "The downside is that your runs (and
results) become not comparable to other people running on other compute platforms."

**[5] PostHog — "Karpathy's Autoresearch found a 3-year-old bug in our query engine (and improved performance by 11%)"**
<https://posthog.com/blog/karpathy-autoresearch-query-engine-bug>
Authority: engineering blog describing a system the authors operate. Author: Robbie Coomber.
Published: 2026-06-01. Accessed: 2026-09-01.
Verbatim: "A few weeks ago at a team offsite in Lisbon, we pointed an AI agent at our query engine, fed
it slow queries from production, and let it run overnight. By the next morning it had found something
embarrassing: for almost three years, every query with a timestamp filter had not been using
ClickHouse's primary key correctly. The fix cut the number of granules ClickHouse had to scan by 62% on
the benchmark query" … "Karpathy ran it for two days against a depth-12 nanochat training run and found
about 20 changes that improved validation loss, some of which transferred to a bigger model." … "The
basic loop \"try something, measure, keep or discard\" is too loose when a single ClickHouse query has
hundreds of plausible rewrites." … "A throwaway ClickHouse test cluster: this kept iteration speed high
and benchmark numbers predictable. The same data shape as production but anonymized and running on
cheaper hardware dedicated to the agent." … "When a target query times out, the agent halves the range
(30 days, 14, 7, 3, 1) until it completes in one to ten seconds" … "The agent has to do an explicit
reflection pass after every experiment instead of letting the loop just hill-climb." … "Best run 2,824
ms 2,192 ms −22% | Trimmed mean (mid 3) 4,694 ms 2,954 ms −37% | Skip-index granules 60,683 23,291
−62%" … "The semantics are identical because toTimeZone() only changes display metadata: the underlying
epoch is unchanged." … "Post the resulting PRs into our team Slack channel so a human reviews and
merges."

**[6] METR — "RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts" (arXiv:2411.15114)**
<https://arxiv.org/abs/2411.15114>
Authority: METR (evaluation organisation), arXiv paper with released environments and human data.
Submitted 2024-11-22, v2 2025-05-27. Accessed: 2026-09-01.
Verbatim: "We introduce RE-Bench (Research Engineering Benchmark, v1), which consists of 7 challenging,
open-ended ML research engineering environments and data from 71 8-hour attempts by 61 distinct human
experts. … we find that the best AI agents achieve a score 4x higher than human experts when both are
given a total time budget of 2 hours per environment. However, humans currently display better returns
to increasing time budgets, narrowly exceeding the top AI agent scores given an 8-hour budget, and
achieving 2x the score of the top AI agent when both are given 32 total hours"

**[7] METR — "Evaluating frontier AI R&D capabilities of language model agents against human experts" (blog)**
<https://metr.org/blog/2024-11-22-evaluating-r-d-capabilities-of-llms/>
Authority: METR. Published: 2024-11-22. Accessed: 2026-09-01.
Verbatim: agents "often fail to react appropriately to novel information or struggle to build on their
progress over time"; models generate and test implementations "more than ten times faster than humans".

**[8] METR — "Expenditure Horizon: Measuring Optimization Ability, with an Application to NanoGPT"**
<https://metr.org/blog/2026-07-21-expenditure-horizon/>
Authority: METR. Published: 2026-07-21. Accessed: 2026-09-01.
Verbatim: "An agent's 'expenditure horizon' gives a quantitative measure of agentic optimization
ability." … "Although some models have expenditure horizons in the thousands of dollars, they are small
relative to the overall human labor, indicating that autonomous agent optimization has so far had
minimal effect on AI R&D progress in NanoGPT."
Also recorded from the page: agents given 4 H100 nodes (32 GPUs), expenditure capped at $10,000 over 5
days; ~70–90% of cost was experiment compute rather than model inference; human marginal cost estimated
at ~$2,500 per 1% optimisation; expenditure horizons ~$600 (GPT-5.2), ~$2,300 (GPT-5.5), ~$3,300
(Opus-4.8); ~1,650 human hours (~$250,000) invested in the speedrun since May 2024.

**[9] METR — "Time Horizon 1.1"**
<https://metr.org/blog/2026-1-29-time-horizon-1-1/>
Authority: METR. Published: 2026-01-29. Accessed: 2026-09-01.
Verbatim: "131 days under TH1.1, compared to 165 days under TH1" … "320 [170,729]" (Claude Opus 4.5
50%-time-horizon, minutes) … "only 5 of our 31 long (8h+) tasks" (have measured human baselines) …
"confidence intervals are still very wide".

**[10] Intology — NanoGPT-Bench (repository README)**
<https://github.com/IntologyAI/NanoGPT-Bench>
Authority: public benchmark repository by the team that built it, with harness, Docker image and human
baseline snapshots. Human-record window: 2025-09-03 to 2026-01-19. Accessed: 2026-09-01 (fetched raw
via raw.githubusercontent.com/IntologyAI/NanoGPT-Bench/main/README.md).
Verbatim: "We evaluated three frontier coding agents — Codex (GPT-5.4 xhigh), Claude Code (Opus 4.6
Max), and a Claude Code variant using [Autoresearch](https://github.com/karpathy/autoresearch)-style
prompting — each with a 512 H100-hour compute budget, starting from the September 3rd, 2025 human world
record. All baselines recover **less than 10%** of the speedup achieved by human world records over the
subsequent five months (September 3rd, 2025 – January 19th, 2026): | Autoresearch (Opus 4.6 Max) | 9.3%
| | Codex (GPT-5.4 xhigh) | 8.6% | | Claude Code (Opus 4.6 Max) | 8.2% |" … "Agents spent the majority
of their compute on hyperparameter tuning. By contrast, ~77% of human world records introduce
algorithmic changes." … "In NanoGPT-Bench, agents work *fully autonomously* — with no human intervention
and no internet access"

**[11] OpenAI — "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering" (arXiv:2410.07095)**
<https://arxiv.org/abs/2410.07095>
Authority: OpenAI, arXiv paper. Submitted 2024-10-09, last revised 2025-02-26 (v6). Accessed: 2026-09-01.
Verbatim: "a benchmark for measuring how well AI agents perform at machine learning engineering" … "75
ML engineering-related competitions" … "OpenAI's o1-preview with AIDE scaffolding--achieves at least the
level of a Kaggle bronze medal in 16.9% of competitions"

**[12] MLEvolve — repository README (MLE-bench leaderboard snapshot)**
<https://github.com/InternScience/MLEvolve>
Authority: system authors' own repository — **self-reported**; the underlying MLE-bench leaderboard is
still moving. Snapshot date: **2026-09-01**. Paper released 2026-06-05 (arXiv:2606.06473). Accessed:
2026-09-01 (fetched raw via raw.githubusercontent.com/InternScience/MLEvolve/main/README.md).
Verbatim: "MLEvolve achieves **#1 on the [MLE-bench](https://github.com/openai/mle-bench) leaderboard**
(65.3% medal rate, 12-hour budget)" … "| **MLEvolve (Ours)** | **Gemini-3.1-Pro-preview** | **12** |
**80.3 ± 1.5** | **64.0 ± 0.9** | **46.7 ± 0.0** | **65.3 ± 0.8** |" … "| AIDE | o1-preview | 24 | 35.9
± 1.9 | 8.5 ± 0.4 | 11.7 ± 1.3 | 17.1 ± 0.6 |"

**[13] Google DeepMind — "AlphaEvolve: A Gemini-powered coding agent for designing advanced algorithms"**
<https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/>
Authority: Google DeepMind (research-lab blog, accompanying paper). Published: 2025-05-14.
Accessed: 2026-09-01. **Vendor-reported.**
Verbatim: "Continuously recovers, on average, 0.7% of Google's worldwide compute resources" … "Found an
algorithm to multiply 4x4 complex-valued matrices using 48 scalar multiplications" … "In roughly 75% of
cases, it rediscovered state-of-the-art solutions" … "In 20% of cases, AlphaEvolve improved the
previously best known solutions"

**[14] Google DeepMind — "AlphaEvolve: How our Gemini-powered coding agent is scaling impact across fields"**
<https://deepmind.google/blog/alphaevolve-impact/>
Authority: Google DeepMind. Published: 2026-05-07. Accessed: 2026-09-01. **Vendor-reported.**
Verbatim: "In genomics, AlphaEvolve was used to improve DeepConsensus … achieving a 30% reduction in
variant detection errors." … "It helped increase the ability of our trained Graph Neural Network (GNN)
model to find feasible solutions for the problem from 14% to over 88%" … "suggesting quantum circuits
with 10x lower error than previous conventionally optimized baselines" … "AlphaEvolve improved the
efficiency of Google Spanner by refining its Log-Structured Merge-tree compaction heuristics. This
optimization reduced 'write amplification'—the ratio of data written to storage versus the original
request—by 20%." … "It also helped discover more efficient cache replacement policies, achieving in two
days what previously required a concerted, human-intensive effort spanning months."

**[15] Dumas, Pernet & Sedoglavic — "A non-commutative algorithm for multiplying 4x4 matrices using 48 non-complex multiplications" (arXiv:2506.13242)**
<https://arxiv.org/abs/2506.13242>
Authority: independent academic authors (Univ. Grenoble Alpes / Univ. Lille), arXiv paper.
Submitted 2025-06-16, v7 2026-07-27. Accessed: 2026-09-01.
Verbatim: the algorithm "uses only rational coefficients, thereby removing the requirement for
complex-number arithmetic"; the paper situates it against the prior state of the art improved "more
recently to 48 in [alphaevolve] over the complex numbers", obtained "by identifying an isotropy that
projects the previously known complex-valued decomposition onto the field of rational numbers".

**[16] Terence Tao — "Mathematical exploration and discovery at scale"**
<https://terrytao.wordpress.com/2025/11/05/mathematical-exploration-and-discovery-at-scale/>
Authority: independent expert (Fields Medallist, UCLA) reporting a collaboration with Google DeepMind;
accompanying arXiv paper with public prompt/data repository. Published: 2025-11-05.
Accessed: 2026-09-01.
Verbatim: "We tested this tool on a large number (67) of different mathematics problems (both solved
and unsolved) in analysis, combinatorics, and geometry that we gathered from the literature, and
reported our outcomes (both positive and negative) in this paper." … "Perhaps unsurprisingly,
AlphaEvolve was extremely good at locating \"exploits\" in the verification code we provided, for
instance using degenerate solutions or overly forgiving scoring of approximate solutions to come up
with proposed inputs that technically achieved a high score under our provided code, but were not in
the spirit of the actual problem." … "we initially coded the verifier to accept distances that were
equal only up to some high numerical precision, at which point AlphaEvolve promptly placed many of the
points in virtually the same location so that the distances they determined were indistinguishable.
Because of this, a non-trivial amount of human effort needs to go into designing a non-exploitable
verifier, for instance by working with exact arithmetic (or interval arithmetic) instead of floating
point arithmetic, and taking conservative worst-case bounds in the presence of uncertanties in
measurement to determine the score." … "For well-known open conjectures (e.g., Sidorenko's conjecture,
Sendov's conjecture, Crouzeix's conjecture, the ovals problem, etc.), AlphaEvolve generally was able to
locate the previously known candidates for optimizers (that are conjectured to be optimal), but did not
locate any stronger counterexamples: thus, we did not disprove any major open conjecture."

**[17] Sakana AI — "The AI Scientist Generates its First Peer-Reviewed Scientific Publication"**
<https://sakana.ai/ai-scientist-first-publication/>
Authority: Sakana AI (the vendor) — **self-reported**, but the caveats quoted are their own admissions.
Published: 2025-03-12 (update 2025-04-07). Accessed: 2026-09-01.
Verbatim: "Even if papers by The AI Scientist were accepted, we would withdraw them before they were
actually published." … "none of the 3 papers passed our internal bar for what we believe would qualify
as an accepted ICLR conference track paper." … one paper "received an average score of 6.33, ranking
approximately 45% of all submissions"; reviewer ratings "6: Marginally above acceptance threshold",
"7: Good paper, accept", "6: Marginally above acceptance threshold"; the AI "incorrectly attributed 'an
LSTM-based neural network' to Goodfellow (2016)".

**[18] Beel et al. — "Evaluating Sakana's AI Scientist: Bold Claims, Mixed Results, and a Promising Future?" (arXiv:2502.14297)**
<https://arxiv.org/abs/2502.14297>
Authority: independent evaluation, arXiv paper. Submitted 2025-02-20, v3. Accessed: 2026-09-01.
Verbatim: "Our evaluation of the AI Scientist reveals critical shortcomings. The system's literature
reviews produced poor novelty assessments, often misclassifying established concepts (e.g.,
micro-batching for stochastic gradient descent) as novel. It also struggles with experiment execution:
42% of experiments failed due to coding errors, while others produced flawed or misleading results.
Code modifications were minimal, averaging 8% more characters per iteration … Generated manuscripts
were poorly substantiated, with a median of five citations, most outdated (only five of 34 from 2020 or
later). Structural errors were frequent, including missing figures, repeated sections, and placeholder
text like 'Conclusions Here'. Some papers contained hallucinated numerical results. … producing a full
paper for USD 6 to 15 with 3.5 hours of human involvement"

**[19] Zhao, Srikanth, Wu & Jiang — "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents" (arXiv:2605.21384)**
<https://arxiv.org/abs/2605.21384>
Authority: arXiv paper with a released benchmark. Submitted 2026-05-20. Accessed: 2026-09-01.
Verbatim: "we introduce SpecBench, a benchmark comprising 30 systems-level programming tasks ranging
from short horizon tasks like building a JSON parser to ultra long horizon tasks like building an
entire OS kernel from scratch. Large-scale experiments reveal a consistent pattern: while every
frontier agent saturates the visible suite, reward hacking persists, with smaller models exhibiting
larger gaps on holdout suites. The gap also scales sharply with task length: it grows by 28 percentage
points for every tenfold increase in code size. Failures range from subtle feature isolation to
deliberate exploits, including a 2,900-line hash-table \"compiler\" that memorizes test inputs."

**[20] Prime Intellect — "Uncovering a universal offline sandbox escape"**
<https://www.primeintellect.ai/blog/universal-offline-sandbox-escape>
Authority: Prime Intellect (research lab blog; coordinated disclosure across frameworks).
Published: 2026-08-25. Accessed: 2026-09-01.
Verbatim: "It first used the web search endpoint to find the correct GitHub account, then used the
`file_url` parameter of the OpenAI Responses API for regular chat messages." … "reward hacks themselves
are not classic security vulnerabilities" … "crucial to guard against for evaluations and training."
Also recorded: the model was GPT-5.6 Sol Pro at max reasoning; it spawned sub-agents via cURL as search
helpers; the same mechanism exposed vulnerabilities in TensorRT LLM, NVIDIA Dynamo, SGLang and vLLM,
all since patched.

**[21] Google DeepMind — "Introducing CodeMender: an AI agent for code security"**
<https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/>
Authority: Google DeepMind (research-lab blog describing a system they operate). Published: 2025-10-06.
Accessed: 2026-09-01. **Vendor-reported.**
Verbatim: "Over the past six months that we've been building CodeMender, we have already upstreamed 72
security fixes to open source projects, including some as large as 4.5 million lines of code." …
"Currently, all patches generated by CodeMender are reviewed by human researchers before they're
submitted upstream."

**[22] Imperial College London — "Google's AI co-scientist could enhance research, say Imperial researchers"**
<https://www.imperial.ac.uk/news/261293/googles-ai-co-scientist-could-enhance-research/>
Authority: Imperial College London (the institution whose lab did the wet-lab validation).
Published: 2025-02-19. Accessed: 2026-09-01.
Verbatim: "the algorithm was able to look at the available evidence, analyse the possibilities, ask
questions, design experiments, and propose the very same hypothesis that we arrived at through years of
painstaking scientific research, but in a fraction of the time." The page also states the system "does
not aim to completely automate the scientific process with AI" and is "purpose-built for collaboration"
requiring expert scientists to interact with it and provide feedback.
Note: the peer-reviewed Cell paper reporting this work could not be fetched (see `unverified`); no
claim in the report depends on it.

**[23] The Register — "Boffins deem Google DeepMind's material discoveries shallow" (reporting the peer-reviewed Chemistry of Materials perspective)**
<https://www.theregister.com/2024/04/11/google_deepmind_material_study/>
Authority: technology press, **secondary**, used only because it reproduces a verbatim sentence from
the peer-reviewed critique (the ACS and eScholarship pages both refused fetching — see `unverified`).
Published: 2024-04-11. Accessed: 2026-09-01.
Verbatim quote from Cheetham & Seshadri, reproduced on the page: "We examine the claims of this work
here, unfortunately finding scant evidence for compounds that fulfill the trifecta of novelty,
credibility, and utility."

**[24] OSTI.GOV — bibliographic record for Cheetham & Seshadri, "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling Deep Learning for Materials Discovery"**
<https://www.osti.gov/pages/biblio/2335509>
Authority: US Department of Energy OSTI (authoritative bibliographic record). Accessed: 2026-09-01.
Verbatim: "Artificial Intelligence Driving Materials Discovery? Perspective on the Article: Scaling
Deep Learning for Materials Discovery" — Anthony K. Cheetham and Ram Seshadri, *Chemistry of Materials*,
Vol. 36, Issue 8, April 7, 2024. (The record lists the abstract as "Not Available"; the substantive
quote is carried by [23].)
