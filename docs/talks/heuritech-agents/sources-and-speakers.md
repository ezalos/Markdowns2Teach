<!-- ABOUTME: Sources + speaker-credibility map for the Heuritech talk "AI Agents — From Theory to Loops". -->
<!-- ABOUTME: Link registry, speaker/author map, and web-researched track-record + credibility tiers for every key source. -->

# Sources & Speaker Credibility — "AI Agents: From Theory to Loops" (Heuritech)

> Companion to `slides/heuritech-agents/content/heuritech.md`. Built by grounding against the deck
> and the two fetched insight files in `docs/talks/heuritech-agents/sources/`, then web-researching
> every speaker, author and data claim. Research date: 2026-06-25. Cite-as-you-go links are inline.

---

## 1. Source link registry

> Every link the owner provided or the deck cites, grouped. Nothing dropped — unaired premieres and the
> X reposts are kept even though they are not (currently) cited in `heuritech.md`.

### A. Videos (all 6 provided)

| URL | What it is | Who made it | Used in deck? |
|-----|-----------|-------------|---------------|
| https://www.youtube.com/watch?v=mR-WAvEPRwE | Anthropic workshop **"Build Agents That Run for Hours (Without Losing the Plot)"** — AI Engineer conference, ~75 min | **Ash Prabaker & Andrew Wilson**, Applied AI team, Anthropic | **Fetched & central.** First-party primary source behind the whole **Loops** section (§21–26) and the planner/generator/evaluator + adversarial-evaluator material that corroborates §22, §38. Quoted: Boris Cherny "almost all of Claude Code is written by Claude Code". |
| https://www.youtube.com/watch?v=FB-MLPhL9Ms | **"The maturity phases of running evals"** — AI Engineer conference, ~18 min | **Phil Hetzel**, Head of Solutions Engineering, Braintrust | **Fetched.** Backs the eval-maturity / "eval the judge" framing; reinforces §30 Evaluate, §31 Observability, §38 LLM-as-Judge. The "robe and a cloak on an LLM" line. |
| https://x.com/0xMovez/status/2069075857629409378 | **X repost** of the Anthropic workshop (mR-WAvEPRwE) | **@0xMovez ("Movez")** — third-party reposter, not affiliated with Anthropic | Provenance only. Frames the talk as ">30% of Anthropic's code is written by loops" — a **paraphrase, NOT a verbatim talk claim** (the insight file flags this). Do not put a hard "30%" on a slide attributed to the talk. |
| https://www.youtube.com/watch?v=ZD9-4fW2HhM | **FETCHED** → **"Build Systems, Not Code"** — AI Engineer conference, ~20 min | **Angie Jones**, VP Developer Experience, Agentic AI Foundation (AAIF) | **Fetched** (insights at `docs/talks/heuritech-agents/sources/ZD9-4fW2HhM-insights.md`). Not cited in deck, but **strongly corroborates the deck's thesis**: "designing agents is software engineering — the primitives changed, the disciplines didn't" (nine SWE disciplines mapped onto agents; "build systems/loops, not one-off prompts"). Speaker/title now confirmed (her own X + AAIF). |
| https://www.youtube.com/watch?v=ZRM_TfEZcIo | UNAIRED premiere → identified: **"Turn 10,994 Notes Into Memory"** (AI Engineer World's Fair memory talk) | **Paul Iusztin** (Decoding AI) & **Louis-François Bouchard** (Towards AI) | **Not cited in deck.** Memory/context-engineering talk (Obsidian vault → file-based research wiki for agents). Relevant to §15 Memory if ever expanded. Title confirmed in spirit by web search (their "10,000 notes → AI research OS" talk). |
| https://www.youtube.com/watch?v=vljxQZfJ9wY | **FETCHED** → **"Production Evals For Agentic AI Systems"** — AI Engineer conference, ~8 min | **Nishant Gupta**, Tech Lead, Meta Superintelligence Labs | **Fetched** (insights at `docs/talks/heuritech-agents/sources/vljxQZfJ9wY-insights.md`). Not cited in deck, but adjacent to the Braintrust eval-maturity material: reframes eval as always-on production *infrastructure* with an SRE mindset (reliability, not accuracy, as North Star); production telemetry > scenario evals > benchmarks. Speaker/affiliation now **corroborated by a second source** (StartupHub.ai, Sessionize). |

Note on the premieres: **ZD9 (Angie Jones) and vljx (Nishant Gupta) have now aired and been fetched** — insight files exist and speaker/title/affiliation are corroborated by second sources (see §3). The third, **ZRM "Turn 10,994 Notes Into Memory" (Iusztin & Bouchard), remains a PENDING premiere** (not aired/fetched; identified, corroborated in spirit by web search). None of the three are **load-bearing** for the deck (the deck cites only mR-WAvEPRwE, FB-MLPhL9Ms and PostHog), but ZD9 and vljx are now solid corroborating material for the harness/method and eval sections respectively.

### B. Articles / written

| URL | What it is | Author | Used in deck? |
|-----|-----------|--------|---------------|
| https://newsletter.posthog.com/p/why-were-bullish-on-loops | **"Why we're bullish on loops"** (PostHog *Product for Engineers* newsletter, ~17 Jun 2026) | **Ian Vanagas**, technical content marketer / Editorial Lead, PostHog | **Primary written source for the entire Loops section** (§21–26): the four ingredients, "a loop without a goal is a slop cannon", "self-driving products", "code was never the problem". Cited in-deck on every loops slide. |
| https://posthog.com/newsletter/loops | PostHog companion piece **"WTF is loop engineering"** | PostHog (Ian Vanagas) | Secondary/companion to the above; same thesis, more intro-level. |
| https://x.com/posthog/status/2069472232712389112 | **X post** linking the PostHog loops article | PostHog (org account) | Provenance / discovery link only. |

### C. Data / case-study sources the deck cites — canonical primary links

| Claim in deck | Best primary URL | Notes |
|---------------|------------------|-------|
| **METR time-horizon** — task length at 50% success doubles ~every 7 months, ~3× Moore's Law (§06, §23) | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ (foundational) + https://metr.org/blog/2026-1-29-time-horizon-1-1/ ("Time Horizon 1.1", the figure the deck's PNG is from) | The deck also cites arXiv 2503.14499 (the paper). Caveat: recent METR data shows doubling has *accelerated* to ~4.3 months — the "every 7 months" line is the 2019–2025 historical trend. |
| **Epoch AI** — inference price for fixed capability falls ~9×–900×/yr (§07) | https://epoch.ai/data-insights/llm-inference-price-trends | Epoch's own data insight: "LLM inference prices have fallen rapidly but unequally across tasks"; 10×–1,000×/yr depending on performance level. Matches the deck's "9× to 900×". |
| **Stripe codebase migration in a day** (vs ~2 months by hand) (§23) | https://x.com/LightningAI/status/2064461309878419648 (the widely-circulated claim) — context: Claude Fable 5 launch, 9 Jun 2026 | 50M-line Ruby migration in a day. **Not an Anthropic-published case study with a methodology**; it is a launch-day testimonial relayed via third parties. Treat the "1 day vs 2 months" as a vendor-launch claim, not an audited benchmark. |
| **Lovable one-shots apps** (§23) | https://lovable.dev/ (product) | Generic capability claim (full-stack app from one prompt). No single canonical "one-shot" study; widely demonstrated but with the well-known "70%→100%" completion caveat. |
| **Karpathy "autoresearcher" loop** — fixed a 3-yr-old bug, +11% perf (§22) | https://github.com/karpathy/autoresearch (repo) + https://posthog.com/blog/karpathy-autoresearch-query-engine-bug (the bug/+11% writeup) | Karpathy's own repo is the primary artifact. The "3-year-old bug + 11%" is documented; note the "+11% Time-to-GPT-2" came from his **nanochat** run (2.02h→1.80h), and the "3-year-old query-engine bug" is a separate **PostHog** application of the same loop — the deck merges two stories. |
| **Peter Steinberger "OpenClaw" + loops posts** (§21) | https://x.com/steipete/status/2063697162748260627 ("you should be designing loops that prompt your agents", ~6.5M views) + https://github.com/steipete (OpenClaw) | The viral post that, with Cherny, anchors the deck's "two builders converging on loops" framing. |
| **Boris Cherny + Claude Code `/loop`** (§21, §23) | https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens (interview) + https://x.com/bcherny/status/2007179832300581177 (his setup) | Cherny is "Creator & Head of Claude Code". `/loop` / automations are productized Claude Code features; the cleanest first-party docs anchor is docs.claude.com (deck already cites it for §14/§20). |

---

## 2. Speaker / author map

| Talk / source | Delivered / authored by | Role + org at the time |
|---------------|-------------------------|------------------------|
| Anthropic workshop "Build Agents That Run for Hours" (mR-WAvEPRwE) | **Ash Prabaker** & **Andrew Wilson** | Both **Applied AI team, Anthropic.** Ash: Member of Technical Staff, Applied AI + RL (harness / post-training experiments). Andrew: Solutions Architect, Applied AI, based in London (digital-native & industries customers). |
| Quoted inside that talk: "almost all of Claude Code is written by Claude Code" | **Boris Cherny** | **Creator & Head of Claude Code, Anthropic** (ex-Meta Principal Engineer; author of *Programming TypeScript*). |
| "The maturity phases of running evals" (FB-MLPhL9Ms) | **Phil Hetzel** | **Head of Solutions Engineering, Braintrust** (eval/observability platform). Prior: 12 yrs consulting — KPMG, then led Slalom's global Databricks unit. |
| "Why we're bullish on loops" (PostHog) | **Ian Vanagas** | **Technical content marketer / Editorial Lead, PostHog** (runs the *Product for Engineers* newsletter). Writer + software developer by background, not a frontier-model practitioner. |
| Loops thesis cited in §21 | **Peter Steinberger** | Creator of **OpenClaw** (180k+ GitHub stars), founder/ex-CEO **PSPDFKit**; **joined OpenAI as engineer, Feb 2026.** |
| "autoresearcher" loop (§22) | **Andrej Karpathy** | Independent / **Eureka Labs** founder; **ex-OpenAI founding member, ex-Senior Director of AI at Tesla.** Author of `nanochat` / `autoresearch`. |
| METR time-horizon data (§06, §23) | **METR** (Model Evaluation & Threat Research) | Independent nonprofit AI-evaluation org. |
| Epoch AI cost-collapse data (§07) | **Epoch AI** | Independent AI-research / data org tracking compute, cost and capability trends. |
| "Build Systems, Not Code" (ZD9) — *fetched* | **Angie Jones** | **VP Developer Experience, Agentic AI Foundation (AAIF)**; ex-Block (Head of DevRel, TBD), ex-Applitools (founded Test Automation University), ex-Twitter, ex-IBM; Java Champion, 26+ US/China patents. *(Not cited in deck.)* |
| Premiere "Turn 10,994 Notes Into Memory" (ZRM) — *pending* | **Paul Iusztin** & **Louis-François Bouchard** | Founder, Decoding AI / *LLM Engineer's Handbook* author; and Towards AI. *(Not cited in deck; premiere not yet aired.)* |
| "Production Evals For Agentic AI Systems" (vljx) — *fetched* | **Nishant Gupta** | **Tech Lead / Staff Software Engineer, Meta Superintelligence Labs (MSL)** — agentic & training/inference infrastructure, eval/auditing of AI decision systems. *(Not cited in deck.)* |

---

## 3. Track record & credibility

> Tiers: **Very High** (frontier first-party practitioner on exactly this topic) · **High** (named expert / strong primary work) · **Solid** (credible specialist, some COI) · **Moderate** (secondary synthesis / promotional). COI = conflict of interest.

### Ash Prabaker — Anthropic, Applied AI
- **Role/affiliation:** Member of Technical Staff, Applied AI + RL, Anthropic. Works on the harness and post-training experiments for long-running agents.
- **Track record:** Co-delivered the definitive first-party talk on long-running agents; describes building and *ablating* Anthropic's own planner/generator/evaluator harness across model generations — the exact architecture the deck teaches. ([daily.dev](https://daily.dev/posts/build-agents-that-run-for-hours-without-losing-the-plot-ash-prabaker-andrew-wilson-anthropic-n3dvnyjtj), [theorg.com](https://theorg.com/org/anthropic/org-chart/ash-prabaker))
- **Domain authority on *this* topic:** Maximal — he builds the thing the deck is about.
- **Credibility: Very High.** *Caveat:* employed by Anthropic → his examples are Claude-centric; the "almost all of Claude Code written by Claude Code" framing is first-party promotional even if technically true.

### Andrew Wilson — Anthropic, Applied AI
- **Role/affiliation:** Solutions Architect, Applied AI, Anthropic (London); prior roles at Seldon and Curvestone. ([LinkedIn](https://uk.linkedin.com/in/anddwilson))
- **Track record:** Co-author of the same workshop; framed the three failure buckets (context rot, context anxiety, self-judgment) the deck draws on.
- **Domain authority:** High — first-party deployment experience across Anthropic customers, though more "field SA" than core research.
- **Credibility: Very High** (same first-party caveat as Ash; solutions-architect lens = deployment-flavored, not lab-research-flavored).

### Boris Cherny — Anthropic, Claude Code
- **Role/affiliation:** Creator & Head of Claude Code, Anthropic. Ex-Meta Principal Engineer; author *Programming TypeScript*. ([Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), [Fortune](https://fortune.com/2026/06/08/anthropics-boris-cherny-creator-of-claude-code-says-there-are-days-he-manages-tens-of-thousands-of-ai-agents-at-once/))
- **Track record:** Built the product that holds >half the AI-coding market and hit ~$1B run-rate; ships 20–30 PRs/day via parallel Claude instances; popularized "I don't prompt Claude anymore."
- **Domain authority on loops:** Maximal — the person who productized `/loop` and parallel agents.
- **Credibility: Very High.** *Caveat:* strongest possible vendor COI — every claim promotes Claude Code; the "80–90% of Claude Code written by Claude Code" figure is self-reported and unauditable externally.

### Phil Hetzel — Braintrust
- **Role/affiliation:** Head of Solutions Engineering, Braintrust (eval + observability vendor). Prior: 12 yrs consulting (KPMG; led Slalom's global Databricks unit). ([StartupHub interview](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/agent-vs-traditional-observability-braintrust-s-phil-hetzel-explains), [LinkedIn](https://www.linkedin.com/in/philliphetzel/))
- **Track record:** Speaks frequently and coherently on eval maturity/observability; his "evals are not unit tests / re-run production / eval the judge" framing is well-regarded and aligns with independent sources (hamel.dev) the deck already cites.
- **Domain authority on evals:** High — but it is *vendor* authority (SE leader, not a researcher); his expertise is real and practitioner-grade, just commercially motivated.
- **Credibility: Solid–High.** *Caveat:* Braintrust sells the eval platform his talk argues you need — clear product COI. The conceptual content (maturity phases, validate-the-judge) is vendor-neutral and corroborated, so it survives the COI well.

### Ian Vanagas — PostHog
- **Role/affiliation:** Technical content marketer / Editorial Lead, PostHog; runs the *Product for Engineers* newsletter. Writer + software developer, **not** a frontier-model builder. ([LinkedIn](https://ca.linkedin.com/in/ianvanagas), [About page](https://newsletter.posthog.com/about))
- **Track record:** Strong, popular technical-marketing writing; "Why we're bullish on loops" is a clear, well-sourced **synthesis** of what practitioners (Steinberger, Cherny, Karpathy, METR) said — not original first-party work.
- **Domain authority on loops:** Moderate (as an author) — he is relaying and framing others' work, well, for a product-engineering audience.
- **Credibility: Moderate (Solid as synthesis).** *Caveat 1:* it is **content marketing** — the article's payoff is "PostHog builds self-driving-product features." *Caveat 2:* secondary source. The deck leans on it heavily for the Loops section; the fetched Anthropic talk is the **primary account of most of what PostHog summarizes**, so prefer dual-citing or upgrading to Anthropic where possible (the insight file recommends exactly this).

### Peter Steinberger — OpenClaw / ex-PSPDFKit / now OpenAI
- **Role/affiliation:** Creator of OpenClaw (180k+ stars); founder/ex-CEO PSPDFKit (PDF SDK on 1B+ devices); joined OpenAI Feb 2026. ([Wikipedia](https://en.wikipedia.org/wiki/Peter_Steinberger_(programmer)), [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-creator-of-clawd-i-ship-code))
- **Track record:** Genuine first-party loop practitioner; the "design loops that prompt your agents" post (~6.5M views) helped name "loop engineering."
- **Domain authority on loops:** High — first-party builder, lives the workflow daily.
- **Credibility: High.** *Caveat:* deliberately provocative/maximalist ("I ship code I don't read") — great signal, but his takes are opinion-leader hot-takes, not measured studies; also now at OpenAI, a vendor.

### Andrej Karpathy — ex-OpenAI / ex-Tesla
- **Role/affiliation:** Eureka Labs founder; OpenAI founding member; ex-Senior Director of AI, Tesla. ([autoresearch repo](https://github.com/karpathy/autoresearch))
- **Track record:** Among the most authoritative individuals in applied deep learning; `nanochat`/`autoresearch` are real, runnable artifacts. The "+11% Time-to-GPT-2" and the missing QK-Norm scalar are documented in his own work.
- **Domain authority on autonomous-loop research:** Very High.
- **Credibility: Very High.** *Caveat for the deck:* it conflates two stories — the **+11% nanochat** result (his repo) and the **3-year-old query-engine bug** (PostHog applying his loop). Keep them attributed separately to stay precise.

### Angie Jones — Agentic AI Foundation (talk: "Build Systems, Not Code", fetched)
- **Role/affiliation:** VP of Developer Experience, Agentic AI Foundation (AAIF, a Linux Foundation project for open agent standards — MCP, goose, AGENTS.md). Career arc through hands-on software engineering and developer experience: IBM software engineer (9 yrs, Master Inventor), Twitter Senior Automation Engineer, Applitools (founded Test Automation University), then Head of Developer Relations at Block (TBD). Java Champion; 26+ patented inventions; long-running international keynote speaker. ([angiejones.tech](https://angiejones.tech), [AAIF blog](https://aaif.io/blog/building-the-foundation-for-agentic-ai), [Wikipedia](https://en.wikipedia.org/wiki/Angie_Jones), [LinkedIn](https://www.linkedin.com/in/angiejones))
- **Track record:** Two decades building/shipping and teaching test automation and developer tooling; led MCP-at-scale adoption at Block; now sets developer-experience direction for agentic standards at AAIF. The talk distills classic SWE disciplines (systems thinking, decomposition, separation of concerns, contracts, idempotency, threat modeling) onto agent design via a single running example — exactly the deck's "build systems/loops, not one-off prompts" thesis.
- **Domain authority on *this* topic:** High — strong on the deck's central claim (building agentic systems *is* software engineering / dev-experience & testing leadership). Her authority is engineering-discipline and DX, not frontier-model research.
- **Credibility: High.** *Rationale:* deep, verifiable SWE/DX track record speaking directly to "design the system before the agent." *Caveat/COI:* AAIF is a standards body she represents, so the talk gently advances open-agent standards (MCP/goose/AGENTS.md) — mild advocacy COI, but the engineering content is vendor-neutral and corroborates the deck independently.

### Nishant Gupta — Meta Superintelligence Labs (talk: "Production Evals For Agentic AI Systems", fetched)
- **Role/affiliation:** Tech Lead / Staff Software Engineer & Researcher, Meta Superintelligence Labs (MSL) — large-scale distributed systems and agentic infrastructure, including evaluation/auditing of AI-driven decision systems and reliability/safety in production. ([StartupHub.ai](https://www.startuphub.ai/ai-news/ai-research/2026/meta-s-nishant-gupta-on-evaluating-agentic-ai-systems), [Sessionize profile](https://sessionize.com/nishantgupta))
- **Track record:** Builds the production infrastructure his talk is about — monitoring, scheduling, feedback loops, and eval/auditing for agents in high-stakes environments at Meta scale. The talk's frame (eval as always-on production *infrastructure* run with an SRE mindset; reliability — not accuracy — as the North Star; production telemetry > scenario evals > benchmarks) is first-party practitioner experience, and it dovetails with the deck's Evaluate/Observability slides (§30–31, §38) and complements Braintrust's eval-maturity material.
- **Domain authority on *this* topic:** High — genuine production-evals/ML-infrastructure practitioner at a frontier lab, on precisely the topic he presents.
- **Credibility: High.** *Rationale:* first-party builder of production-eval infrastructure at MSL, corroborated by a second source; content is methodological and vendor-neutral (no product being sold). *Caveat:* examples are Meta-internal and not externally auditable; single ~8-min talk, so it's a sharp frame rather than a deep study.

### Org-credibility notes
- **Anthropic — Very High, first-party / vendor.** The builder of Claude/Claude Code; the workshop is the single best primary source for the deck's loops thesis. COI: every number flatters Claude; self-reported internal stats (% of code written by Claude) are unauditable. Use the verbatim quotes, avoid the X "30%" paraphrase.
- **Braintrust — Solid, specialist vendor.** Credible, focused eval/observability expertise; the conceptual content is vendor-neutral. COI: sells the product its talks motivate.
- **PostHog — Moderate, content-marketing engine.** Excellent technical writing and a real product-analytics company, but the loops article is **synthesis-for-marketing**, not primary research. Best treated as a readable framing layer over primary sources.
- **METR — High, independent.** Nonprofit AI-evaluation org; the time-horizon benchmark is the field's reference for autonomy trends. Caveat: it is a benchmark with stated limitations, and the headline doubling rate has shifted (7 mo → ~4.3 mo), so quote it as a trend, not a constant.
- **Epoch AI — High, independent.** Well-regarded data org on compute/cost trends; the inference-price-decline insight is theirs and methodologically transparent. Caveat: the "9×–900×" range is performance-band-dependent — fine as stated, misleading if flattened to one number.

---

## Bottom line

This is a **strong, well-balanced source set, anchored by genuine first-party practitioners.** The load-bearing source is the **Anthropic workshop (Prabaker & Wilson, with Cherny quoted)** — the people who actually build long-running-agent harnesses — backed by two independent data authorities (**METR**, **Epoch AI**) and a high-authority individual (**Karpathy**). The weakest link by provenance is the **PostHog "loops" article**: a credible but **secondary content-marketing synthesis** that the deck currently leans on hardest for its Loops section — it should be **dual-cited or upgraded to the Anthropic primary** wherever the claims overlap. **Braintrust (Hetzel)** is a solid specialist but a vendor selling the eval tooling it advocates, so use its *concepts* (eval maturity, validate-the-judge) rather than treating it as neutral. Two things to handle with caution: the **@0xMovez ">30% of code written by loops"** line (a paraphrase, not a talk claim — don't slide it) and the **Stripe "1 day vs 2 months" migration** (a vendor launch-day testimonial, not an audited study). Two more conference-stage practitioners have since aired and been fetched, and both reinforce the set without the deck having to cite them: **Angie Jones (Agentic AI Foundation, "Build Systems, Not Code")** independently restates the deck's core thesis from a software-engineering/dev-experience seat (High), and **Nishant Gupta (Meta Superintelligence Labs, "Production Evals For Agentic AI Systems")** adds a frontier-lab, SRE-flavored production-evals frame that complements Braintrust on the eval side (High). Both sit just below the first-party Anthropic/Karpathy tier and above the PostHog synthesis: real practitioners on exactly their topic, with only mild advocacy (Jones → open standards) or non-auditable internal examples (Gupta → Meta) as caveats. Most authoritative: Karpathy, Anthropic's Cherny/Prabaker/Wilson. Least authoritative (by provenance, not quality of writing): the PostHog secondary synthesis and the still-pending ZRM memory premiere, none of which the deck actually cites.
