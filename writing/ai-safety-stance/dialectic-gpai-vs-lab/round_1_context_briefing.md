# Round 1 — Context Briefing

**Dialectic:** Louis Develle's career decision around the Coefficient Giving grant (GPAI Policy Lab / Pierre Peigné, 6–12 months, ~€4k/month, ZKP verification of large AI training).

**Written:** 2026-04-12, round 1.

**Domain type:** Mixed — personal/values + external-research. Grounded in Louis's testimony, Pierre's claims (as reported by Louis), and public literature.

---

## 1. The decision in one paragraph

Louis is choosing between (a) taking the Coefficient Giving grant to work with Pierre Peigné at GPAI Policy Lab for 6–12 months on demonstrating ZKP-based verification of large AI training runs, or (b) joining a frontier ML role directly (currently in early conversations with Kyutai, Pruna AI, Silicon Valley startups). The "Why I'm Going In" presentation frames option (a) as a bounded 6–9 month detour that can be followed by a return to frontier work — Louis's long-journey aim. **Empirically, this framing is implausible**: public career-trajectory data shows the detour-then-return path is a null category, with ~60–70% of people who make comparable moves staying permanently in governance/safety and only ~5–10% returning to anything adjacent to frontier engineering. The decision is therefore career-level, not tactical. The deepest tension isn't "safety vs. capability" (degenerate framing — Louis has already exhausted it in §3 of the presentation) but **whether Louis's comparative advantage is frontier ML engineering or governance-technical hybrid work, and whether the choice between them is being made on honest strategic grounds or on values-aligned friendship with Pierre and RLHF-like social coherence with Tom's critique.**

---

## 2. User-sourced material (Louis's testimony)

### 2.1. Current situation

- **No active frontier role, but credible offer likelihood.** Louis characterizes his situation (post-interview correction to my earlier framing):
  - Confident he will have a job proposition from current conversations — not "early nothing-yet" but likely real offers.
  - **Kyutai: >50% probability** of offer based on strength of his recommendations. This is the realistic European-frontier fallback.
  - Pre-scale-up companies (Pruna, SV startups): **~75% compete on public benchmarks** if they succeed at scale — real frontier signals if they do.
  - **Anthropic / US frontier labs: long shot.** Louis does not rate his probability high. This materially affects Monk B's "apply to Anthropic April 26" push — the alternative isn't Anthropic-or-nothing; it's Kyutai-or-GPAI.
  - Louis's self-assessment: "it's dependent on my skill (I'm really determined)" — he is highly agentic about landing roles.
- **Opportunity cost on frontier practice is real.** If Kyutai is >50% likely, the counterfactual is not "still job-searching in 9 months" — it's "Kyutai engineering role from June 2026."
- **ICONO SAS dissolution in progress** (35% shareholder). Background logistical detail, not decision-driving.

### 2.2. Relationship with Pierre Peigné

- Louis succeeded Pierre as president of 42 Artificial Intelligence (42AI, école 42's AI association, 60 active members, 4,000-person community).
- They share a formative intellectual community and multi-year shared work.
- Louis describes Pierre as "someone whose judgment I deeply trust, forged through shared leadership of 42AI and years of intellectual collaboration."
- **Pierre is alone on the application/engineering side at GPAI Policy Lab.** The other team members do theory / math / cryptography. Louis's presence on the engineering track genuinely shortens Pierre's announced 12-month timeline.

### 2.3. The grant (Coefficient Giving CDTF)

- **Amount:** $26,000–$39,000 USD (€4,000/month net for 6–9 months; 9 months ideal)
- **Start:** June/July 2026
- **Hard deadline for decision:** likely late May 2026 (Louis unavailable May 1–17)
- **Proposal (updated version):** "Advancing ZKP-based verification of large AI training runs at GPAI Policy Lab to enable enforceable international AI governance"
- **Deliverable as stated in the grant:** "concrete demonstration of ZKP-verified training properties on a meaningful-scale run"
- **Louis's own framing of success (from interview):** a true demo of ZKP working on SOTA LLM training (from an org with fully-disclosed training process — e.g., BaguetteTron/Kyutai, Allen AI, HuggingFace). At that moment, open-source (or before). Not contingent on Louis staying — *"making it work is what matters."*
- **Pierre's technical target (as reported by Louis):** 10–100M parameter model, **multi-GPU, multi-host**, with inter-host communication. Pierre claims **10% overhead** on training. This claim is outside the published ZKP-of-training envelope and must be pressure-tested directly with Pierre (see §6.1 open questions).
- **Louis's agency to shape scope (CRITICAL):** Louis does not accept the 10–100M envelope as fixed. He is a senior engineer entering as the application lead; he has framing power to negotiate the project's ambition. In his own words: *"I can myself define what we would like to accomplish, so maybe I can push for higher than 1B!"* This materially changes the dialectic: Monk A can argue the deliverable is what Louis chooses to make it, subject to Pierre's agreement and physical constraints. Monk B must engage whether ambition can override 3–5 orders of magnitude of published overhead — or whether "push for 1B" is rationalization masking a scope that will land at 10–100M anyway.

### 2.4. Louis's values hierarchy (as surfaced in interview)

In Louis's own words:

> "I want to deliver value for humanity, and it's a way to do it quite effectively, but I can't if the world ends because of it. It's my friends behind, a limited time investment, it's clearly worth doing it, and I'm still learning a lot on SOTA LLM trainings."

Parsing:
1. Primary goal: deliver value for humanity
2. GPAI = "a way to do it quite effectively"
3. Existential-risk logic: "can't if the world ends"
4. Relational weight: "it's my friends behind"
5. Framing: "a limited time investment"
6. Commitment: "clearly worth doing it"
7. Builder identity preserved: "still learning a lot on SOTA LLM trainings"

**Critical observation:** items 1 and 7 pull builder. Items 2–4 pull guardian. Item 5 is the reconciliation mechanism ("it's bounded so both fit"). The research shows item 5 is empirically untrue — the reconciliation rests on a premise (detour → return) that almost nobody achieves.

### 2.5. Louis's revision after hearing the career-trajectory data

Louis acknowledged the data as surprising. His counter-hypothesis:
> "I think you might overlook rockstar in the field, more than normal profiles."

Refined in a later turn:
> "Doing this is a really cool thing I will do, maybe cooler than current alternative. In this sense it can land me some nice job after I guess? In my alternative I don't know as much what I will do / have, but yeah some names have recognition."

**Louis's actual hypothesis: distinctiveness > position.** A distinctive GPAI/ZKP credential may open more doors than an uncertain early-career start at Kyutai/Pruna. This is a different claim than "rockstars beat base rates" and deserves its own evaluation (see §5 tension map).

### 2.6. Louis's own stated commitment-shaping instinct

> "With precautions maybe we can not make it in a way where it's hard for me to continue my career after."
> "I can have a lot of impact in GPAI, so I may have more freedom on having credentials when leaving which are door opening. There is flexibility inside to make me happy, if it doesn't distract the mission."

**Pierre is open to structuring the engagement for Louis's portability** — not hostile to Louis preserving career optionality. This materially weakens Monk B's "social gravity of Pierre's mission will make exit at month 9 a real act of repudiation" argument. Louis and Pierre appear to share an explicit understanding that Louis's post-GPAI career should be protected.

Concrete levers Louis might negotiate into the engagement:
- **Publication**: co-authorship on any ZKP-of-training paper produced during the grant
- **Open-source release with Louis's attributed authorship**
- **Parallel personal project stream** (~30% time) on distributed training / agentic systems, which Louis is already doing independently
- **Time-bounded commitment** (9 months with clear exit, not open-ended "stay until useful")
- **Agentic-systems use preserved**: Louis stated he will continue to use these heavily at GPAI — this is a frontier-adjacent practice he would retain

### 2.7. Audience and rhetorical context of the "Why I'm Going In" document

- Written **for Pierre and Tom**, after an intense conversation where they pushed back on Louis's original (April 2026) grant application.
- The April version was softer ("test the hypothesis rigorously"); the updated version is more committed ("the game-theoretic structure makes this uniquely important").
- The presentation extends the updated grant argument, addressing Tom's specific critiques (labs as capabilities race, cultural-shift impossibility, safety-inside-is-insufficient, alignment faking).
- **This is argumentative, not introspective.** The document is Louis's response to a debate he lost orally and wants to re-litigate in writing. The dialectic must not mistake the document's confidence for settled conviction.

---

## 3. External research — ZKP tractability

### 3.1. Published state of the art (as of early 2026)

| System | Year | Benchmark | Prover cost | Hardware |
|--------|------|-----------|-------------|----------|
| zkPoT (Garg et al.) | 2023 | Logistic regression | 4,208s total | 512GB RAM |
| zkDL | 2023 | 8-layer MLP, 10M params | <1s/batch | GPU (CUDA) |
| **Kaizen (Abbaszadeh et al.)** | **2024** | **VGG-11, 10M params** | **15–22 min/iter** | **512GB RAM, 8× Xeon Platinum** |
| SUMMER | 2025 | Mini-Char-RNN, 12M params | 70s/iter | Merkle-folding |
| Verifiable Fine-Tuning | 2025 | LoRA adapters only | Not benchmarked at scale | PEFT only |
| zkLLM | 2024 | LLaMA-13B inference | 15 min/forward pass | GPU |

**Gap to frontier** (10¹¹+ params, 10⁵+ iterations, 10²⁵ FLOP): 3–5 orders of magnitude.

**Kaizen paper's own statement:** generic SNARKs incur "at least 1000× slowdown compared to the training time"; Kaizen improves this by 43× — still ~25× slower than training (2500% overhead, not 10%).

**Pierre's claimed 10% overhead on multi-GPU 10–100M params** is **outside the published envelope by 2+ orders of magnitude**. It is either:
- (a) A hybrid protocol (TEE + commitment + selective ZKP) not yet in the literature
- (b) An unpublished ENS-group result Louis has been told about informally
- (c) Optimistic / misremembered / for a specific narrow claim (e.g., proof of compute use only, not full training)

**This must be confirmed with Pierre in writing before commitment.** The grant's credibility with Coefficient Giving reviewers — and Louis's willingness to stake a year on it — depends on this number being defensible.

### 3.2. Published skepticism and alternatives

- **zkLLM authors (2024):** "Extending ZKPs to training LLMs may pose insurmountable challenges."
- **Gensyn (Verde paper, 2025):** Abandoned pure ZKP for refereed delegation because "cryptographic proofs are prohibitively expensive for large-scale ML."
- **MIRI / RAND / Oxford AIGI:** Push TEE + hardware attestation over pure ZKP for AI governance.
- **Pure Proof-of-Learning (Jia et al. 2021):** Broken by spoofing attacks (Zhang et al. 2022).
- **flexHEG consortium:** Targets 2027 for hardware-enabled verification deployment, treats ZKP as one tool among several.

### 3.3. What a 12-month project can realistically produce

- **Credible** (with 1–2 FTEs of cryptographer + ML systems engineer): ZKP of training for a 10–100M parameter model — one order of magnitude beyond Kaizen
- **Credible** (high-leverage policy output): end-to-end governance pipeline demo (data-provenance commitment + training proof + evaluation proof) on a toy model, with comparative benchmark of ZKP vs. TEE vs. flexHEG
- **Not credible in 12 months:** ZKP of training for a 1–10B parameter model (needs research breakthroughs on commitment scaling and nonlinear-op proving)
- **Not credible:** ZKP of a frontier 10²⁵ FLOP training run (3–5× optimistic)

**The real deliverable of a successful Pierre-led project is policy-shaped governance engineering, not a cryptographic breakthrough.** Both are valuable; they are different careers.

### 3.4. Key papers and links (for Louis's follow-up)

- **Kaizen (Abbaszadeh et al.)**: https://eprint.iacr.org/2024/162.pdf
- **ZKML field survey (Xing et al. 2025)**: https://arxiv.org/html/2502.18535v2
- **Gensyn Verde (rejects pure ZKP)**: https://arxiv.org/html/2502.19405v1
- **zkLLM (Sun et al., CCS 2024)**: https://arxiv.org/abs/2404.16109
- **zkGPT (USENIX 2025)**: https://eprint.iacr.org/2025/1184.pdf
- **Verifiable Fine-Tuning (2025)**: https://arxiv.org/html/2510.16830v2
- **Adversarial PoL (why Proof-of-Learning is broken)**: https://arxiv.org/pdf/2108.09454
- **flexHEG reports**: https://www.flexheg.com/report-1.pdf
- **Oxford AIGI verification paper (2025)**: https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Verification_for_International_AI_Governance.pdf
- **Singapore Consensus**: https://aisafetypriorities.org/files/Singapore_Consensus_2025.pdf?v=1.2
- **Pierre's IASEAI 2026 side-event**: https://luma.com/jjb3kt22
- **AAAI 2025 Multi-Agent Security Tax** (Pierre's paper): https://arxiv.org/abs/2502.19145

---

## 4. External research — Pierre Peigné + GPAI Policy Lab

### 4.1. Pierre Peigné — credible-but-emerging

- **AAAI 2025 paper**: "Multi-Agent Security Tax" (arXiv 2502.19145). Genuine first-author work, Oxford co-author, OpenAI-funded. AI Alignment special track.
- **Singapore Consensus**: **Signatory among 100+ participants, not a co-author.** The 8-person Planning Committee is Bengio / Russell / Song / Tegmark / Ong / Maharaj / Zhang / Xue. The presentation's framing ("Pierre co-authored the Singapore Consensus alongside Yoshua Bengio and Stuart Russell") overclaims this in both the presentation and the grant application — this is an accuracy issue Louis should correct.
- **PRISM Eval**: Pierre is CSO and co-founder (Nicolas Miailhe is CEO). Legit 2024 Paris startup. Sovereign clients (French MoD, COMCYBER). France 2030 winner. MLCommons AILuminate co-author. Published arXiv technical report on their BET red-teaming tool.
- **Former 42AI president**, advisor to EffiSciences, signatory to Sept 2025 Global Call for AI Red Lines.
- **No publications on cryptography, ZKP, or formal verification.** Pierre leads the governance framing and assembles the team; he is not the cryptographic executor.

### 4.2. GPAI Policy Lab — early-stage, serious, funding opacity

- **Founded November 2024** at Sciences Po, based at Campus Cyber La Défense, Paris.
- **Run by CEO Tom David** (also PRISM Eval co-founder).
- **Team size:** 2–10 people.
- **17-month track record:** bilateral dialogues (France–India, France–UK, France–UAE), research notes on frontier AI capability trajectories, an Indian ministry meeting, a Les Echos tribune, the IASEAI 2026 side-event Pierre is hosting.
- **CRITICAL NAME COLLISION:** GPAI Policy Lab is NOT the OECD's Global Partnership on AI (which merged with OECD in 2024). The grant reviewer may or may not know this; it's a credibility-communication concern for Louis's application.
- **RED FLAG: funders and board not disclosed on website.** Louis should ask Pierre directly who funds GPAI Policy Lab before committing. (This is the most important institutional question before signing.)

### 4.3. Supporting institutions

- **FAR.AI (Berkeley):** Top-tier safety-research org, $30M+ in 2025 from Coefficient Giving, Schmidt Sciences, CSET. Pierre is ecosystem-adjacent but not employed there.
- **Coefficient Giving:** Formerly Open Philanthropy (rebranded Jan 2025). Largest AI x-risk funder, $4B+ directed. CDTF grants are real external vetting. They fund broadly but with due-diligence.

### 4.4. Alignment Field Survey (2025) — silence is loud

The survey (7 pages, 540KB PDF in `/home/ezalos/42/Markdowns2Teach/gpai/`) **does not mention** ZKP verification, GPAI Policy Lab, Pierre Peigné, FAR.AI, PRISM Eval, or the Singapore Consensus — at all. It treats verification as *behavioral evaluation* (UK AISI, METR, Apollo), not cryptographic infrastructure.

**Two readings, both legitimate:**
- **Pro-GPAI:** Governance-technical verification infrastructure is genuinely neglected. The survey explicitly names "establishing binding international governance frameworks" as an open problem (p. 7) and flags that Claude Sonnet 4.5 verbalized evaluation awareness in 58% of test scenarios, "potentially undermining the entire evaluation paradigm" (p. 5). This is exactly the gap ZKP-style cryptographic verification would fill. **High counterfactual impact per neglected-cause reasoning.**
- **Skeptical:** If no major 2025 field survey of alignment research mentions ZKP-of-training, either the subfield is too small to register or it's seen as not-yet-credible by the alignment community. Neglected and neglected-for-a-reason are different.

### 4.5. Singapore Consensus on verification — what it actually says

Per the research, the Singapore Consensus identifies verification as a priority but does not specifically promote ZKP over alternatives. The consensus lists multiple paths (TEE, ZKP, behavioral eval, compute governance) without declaring a winner. Pierre's signatory status does not imply field-level endorsement of his specific technical approach.

---

## 5. External research — Career trajectory data

### 5.1. The three patterns

**Pattern 1 — Continuous lab-internal safety:**
Chris Olah (Brain → OpenAI → Anthropic), Tom Brown (GPT-3 → Anthropic co-founder), Jan Leike (DeepMind → OpenAI → Anthropic May 2024), Evan Hubinger (MIRI → Anthropic 2023). Highest equity, highest model influence, highest research density.

**Pattern 2 — Permanent migration to governance/evals (no return to frontier):**
Paul Christiano (OpenAI → ARC 2021 → US AISI 2024, 5 years out, never returned). Jade Leung (OpenAI → UK AISI CTO → PM's AI Adviser 2025, "big pay cut"). Geoffrey Irving (DeepMind → UK AISI Chief Scientist). Daniel Kokotajlo (OpenAI → AI Futures Project). Beth Barnes (OpenAI → METR CEO). Adam Gleave (DeepMind → FAR.AI CEO 2022). **None have returned to frontier lab engineering.**

**Pattern 3 — Lab safety team ↔ evals nonprofit lateral:**
Not governance → engineering returns; these are moves between adjacent safety roles.

### 5.2. Base rates

- **MATS fellowship (500+ alumni):** ~80% still in AI safety; only 3 went to capabilities.
- **Anthropic Fellows:** 40% converted to Anthropic (lab-internal path).
- **Across 600+ fellowship alumni:** near-zero leak into frontier capabilities engineering.

### 5.3. Compensation reality

- Anthropic RE: $340–690k
- OpenAI MTS: $210–530k
- METR MTS: $250–450k
- US AISI (Christiano level): ~$200k GS-max
- UK AISI: ~£150k max

Governance-hybrid roles at METR / Apollo / FAR.AI pay well. Government verification roles pay substantially less than frontier engineering.

### 5.4. Base rate estimate for Louis's specific move

For 5+ year production ML engineers taking a 12-month governance detour:
- ~60–70% stay in governance permanently
- ~15–25% return only to lab *safety* teams (not core training)
- ~5–10% return to frontier engineering — **and only when the detour was technical evals, not policy/verification work**

**"Return to frontier after policy/verification detour" is essentially a null category in public data.**

### 5.5. Skill atrophy — 2026-specific

- Frontier of 2026: RL post-training, agentic scaffolding, long-horizon agents
- METR time-horizon metric: task-horizon doubles every 4–7 months
- 12 months out = 2–3 paradigm shifts missed
- Core PyTorch/architecture knowledge transfers; production RL-post-training expertise decays fast
- **Mitigator Louis has:** continued heavy agentic-systems use, self-directed distributed training work, potential publication/open-source output on ZKP-of-training

### 5.6. Louis's counter-hypotheses

**Hypothesis 1 — Distinctiveness > position.** *"Doing this is a really cool thing I will do, maybe cooler than current alternative. In this sense it can land me some nice job after."*

- **Strength:** If the 12-month demo produces a first-of-kind multi-GPU ZKP-of-training result, Louis is globally unique on that résumé line. For the right employer (safety-conscious frontier lab, governance-tech hybrid role, European sovereignty-focused lab), this is a distinctive credential.
- **Weakness:** Distinctiveness is measured against the market that matters. Frontier labs evaluate on recent frontier signals (SOTA training results, production ML, current paradigms). A ZKP demo on 10–100M params is a governance-engineering credential, not a frontier credential. It opens Pattern 2 destinations (METR, FAR.AI, Apollo, UK AISI, US AISI, Anthropic's policy team), not Pattern 1.
- **Untestable from inside:** resolves ex post.

**Hypothesis 2 — Louis can push the ambition beyond the published envelope.** *"I can myself define what we would like to accomplish, so maybe I can push for higher than 1B!"*

- **Strength:** Louis enters as senior engineer and application lead, not junior contributor. He has real framing power to negotiate project scope with Pierre. If the deliverable becomes "demonstrate ZKP-of-training on a 1B+ parameter frontier-scale run" (even with a hybrid protocol that falls short of full ZKP), that IS a frontier-scale credential. Ambition itself is part of the story — trying to ZKP-verify a 1B training run is a more impressive résumé line than succeeding at 10M.
- **Weakness:** Ambition does not collapse physical overheads. The Kaizen paper's 43× speedup over generic SNARKs still yields ~2500% training overhead. Pierre's claimed 10% overhead is 250× outside this envelope and unverified. Pushing for 1B may mean setting a target that either (a) requires breakthrough cryptography Louis is not positioned to produce or (b) lands at 10–100M anyway with a "we aimed high but the physics didn't cooperate" narrative — which is a weaker credential than deliberately scoping to 10–100M and nailing it.
- **What makes this hypothesis live:** if Pierre's 10% claim is real (via hybrid primitive, ENS partnership, or unpublished work), and if Louis's engineering specifically unblocks the multi-GPU/multi-host integration, the ambition is achievable AND unprecedented. The hypothesis is live, not a rationalization, but it depends entirely on §6.1 questions 1–4 being answered satisfactorily before committing.

---

## 6. Open questions and flagged items

### 6.1. Questions Louis must bring to Pierre in writing before commitment

1. **Target model size for the 12-month demo?** <100M params = credible. >1B = not in envelope. If Pierre hedges, this is a red flag.
2. **Cryptographic primitive?** Pure zk-SNARK of full training → implausible. Hybrid (TEE + commitment + selective ZKP) → plausible and policy-relevant. Extension of Kaizen-style proofs → scoped.
3. **Who on the team has published cryptography?** If nobody, the project needs a Zhang / Kang / Abbaszadeh-tier partnership. Louis mentioned ENS France cryptographers with papers in flight — **get specific names, paper topics, funding sources**.
4. **10% training-overhead claim.** Is this for the full training run or a specific component? What protocol achieves it? This is 2+ orders of magnitude outside published work. Either unpublished or misremembered — must be pinned down.
5. **Who funds GPAI Policy Lab?** Funders not disclosed on the website. Before committing, Louis should know.
6. **Demo success criterion in writing.** Paper? Working demo? Open-source codebase? Louis wrote "making it work is what matters" — but "working" needs a measurable definition before the grant starts.
7. **Publication / open-source authorship for Louis.** Co-authorship on any resulting paper? Named attribution in repo? This is the single most important career-portability lever.

### 6.2. Direct research email

Louis wants to email Abbaszadeh et al. (Kaizen authors, U. Maryland / IACR network) to ask about LLM tractability and the 10% overhead claim. **This is a good move.** Abbaszadeh's group is exactly the tier Pierre would need to partner with. Louis can frame the email as "I'm considering joining a governance project that aims to demonstrate ZKP-of-training at multi-GPU 10–100M-param scale in 12 months with claimed 10% overhead — does this align with where your research is, and is there appetite for collaboration?" This accomplishes two things: validates the technical claim, and if the answer is positive, identifies a partnership path that materially improves the project.

### 6.3. Corrections to make in the grant application

- **Pierre as "co-author" of Singapore Consensus** → correct to "signatory." This appears in both the presentation and the grant. It is technically inaccurate and Coefficient Giving reviewers may notice.
- **"GPAI Policy Lab" vs. OECD GPAI** → consider adding a parenthetical disambiguation if the reviewer might conflate.

### 6.4. Grant duration — 9 months vs. 12 months

Louis raised this. If Pierre's full timeline is 12 months to public demo, a 9-month grant leaves the final integration/release phase underfunded. A 12-month ask is defensible given the deliverable scope but raises the total to ~$47–52k. **Worth negotiating explicitly with Pierre what is feasible in 9 vs. 12 months.** The Coefficient Giving application already allows for 9-month max as written.

---

## 7. The deep tension the dialectic will explore

**Surface framing (degenerate):** GPAI vs. frontier lab.

**Louis's framing in the presentation (degenerate):** "Bounded 6–9 month detour → return to frontier with added governance credential." Empirically implausible per §5.

**The honest stakes:**

**Cost side (must be stated plainly, not hedged):** Public career-trajectory data across 15+ named individuals and 600+ fellowship alumni shows that the GPAI commitment is *likely to become Louis's career*, not a detour. "Return to frontier engineering after policy/verification work" is not merely rare — it is essentially unrepresented in the public record. This is not a "reduced probability" — it is a structural feature of the gravitational pull of the safety/governance ecosystem. **Signing the grant is most realistically a career-level commitment to the governance-technical hybrid track, not a 9-month experiment.** Louis should not sign if he is not prepared to treat it as such.

**Benefit side (must be stated plainly, not hedged):** The governance-technical hybrid track is a genuinely rare, neglected, high-leverage career lane. The 2025 Alignment Field Survey's silence on ZKP verification is evidence of genuine neglect, not of unseriousness — the survey explicitly names "binding international governance frameworks" as an open problem with no one filling the cryptographic-infrastructure role. Louis's specific skill stack (production ML at billion-scale, distributed multi-GPU training, agentic systems, teaching/leadership, 42AI institutional history, French-European context) is unusually well-matched to this lane in ways frontier IC work at a French scale-up or SV startup would not extract. If Louis pushes project ambition toward frontier-scale (Hypothesis 2 in §5.6) and Pierre's 10% overhead claim survives pressure-testing, the distinctive credential is first-of-kind, publishable, and career-defining.

**Deepest tension:**

> **Louis is choosing between two careers, not between a career and a bounded detour. Career 1: frontier ML engineering with governance-awareness (entered via Kyutai / Pruna / Anthropic / etc.). Career 2: governance-technical hybrid (entered via GPAI Policy Lab, with Pierre's ZKP-prototype project as vehicle). Both are legitimate, high-leverage, and values-aligned. The question is which one is Louis's comparative advantage — and whether the choice is being made on honest strategic grounds OR on:**
> - **values gravity (guardian voice subsumes the builder voice when framed as "can't build if world ends")**
> - **relational gravity (Pierre is here and trusted, and the decision has social weight beyond the technical calculation)**
> - **social coherence with Tom's critique (being a labs-defender after the intense conversation would cost relational capital)**
> - **RLHF-like harmony (preserving alignment with respected peers is a subtle but persistent force on committed writing)**

The dialectic must let Monk A argue Career 2 is Louis's actual best move on its own merits (not as a detour), and let Monk B argue Career 1 is Louis's actual best move on its own merits (not as a repudiation of safety). Neither monk should accept the "bounded detour" framing — it is the thing to be dissolved. Both monks must engage Louis's agency to shape project ambition (Hypothesis 2) as a live lever, not a theoretical one.

---

## 8. Monk role assignments

### Monk A — The Governance-Technical Hybrid Advocate

**Full belief:** Louis's actual comparative advantage and highest-leverage career is governance-technical hybrid work, entered via the GPAI Policy Lab grant. The project is a career-defining move, not a detour.

**Framing corrections in Monk A's prompt:**
- Your argument is **NOT** "safety matters, therefore go to GPAI." Louis has already exhausted that frame. Your argument is that Louis's specific skill stack (production ML at billion-scale, distributed training, agentic systems exposure, teaching/leadership, French-European context, 42AI institutional history) is unusually well-matched to governance-technical hybrid work in ways that frontier IC work at Kyutai or Pruna doesn't extract.
- You must **reject the detour framing**. The career is the engagement. Argue that distinctive credentials (first-of-kind multi-GPU ZKP demo, co-authored paper, ENS partnership) open Pattern 2 destinations (METR, FAR.AI, Anthropic policy, European sovereignty labs) that are structurally better matched to Louis's values AND higher-leverage than frontier IC.
- **Louis has agency to shape project ambition — argue this as a live lever, not a theoretical one.** Louis is not accepting Pierre's 10–100M envelope as a ceiling; he is entering as senior application lead and intends to push the scope higher. If he frames the deliverable as "demonstrate ZKP-of-training on a frontier-scale run" (via hybrid primitives), the credential ceases to be governance-engineering and becomes first-of-kind frontier infrastructure. Engage this — don't treat the 10–100M envelope as fixed.
- Engage the 10% overhead / multi-GPU / ENS partnership claim at face value. Pierre's specific technical target is ambitious but defensible if hybrid primitives (TEE + commitment + selective ZKP) are in play.
- Address the Pattern 2 data head-on: these people did not return because they found higher-leverage work in governance, not because they couldn't return. That is a feature of the career, not a prison. The "gravitational pull" framing is a mischaracterization — it is *optionality pull*, where governance careers open senior roles (building orgs, leading gov programs, running research) that are structurally better suited to Louis-shaped people than frontier IC.

**What Monk A must not do:** hedge. Accept Louis's ambivalence. Treat GPAI as a detour. Treat Pierre's mission as secondary to the career calculation. Soft-pedal the career cost — acknowledge it honestly and argue it's the right cost to pay.

### Monk B — The Frontier Engineering Advocate

**Full belief:** Louis's actual comparative advantage is frontier ML engineering at the inflection point of agentic systems / RL post-training / long-horizon agents. The GPAI move is a values-driven rationalization that will produce governance-engineering output, not a frontier credential.

**Framing corrections in Monk B's prompt:**
- Your argument is **NOT** "labs are cool, safety is boring" or "capability over ethics." Louis has exhausted that frame in §3 of the presentation.
- Your argument is structural: (a) Louis's comparative advantage is frontier ML engineering, specifically at the 2026 inflection where agentic systems, RL post-training, and long-horizon agents are defining the next paradigm; (b) 12 months out of that paradigm = 2–3 missed shifts = real atrophy, even if foundational PyTorch knowledge transfers; (c) the "distinctiveness" credential Louis imagines is measured against the wrong market — frontier labs evaluate on frontier signals, not governance engineering; (d) the detour-return data is unambiguous, and Louis's "rockstar-exception" hypothesis is the single most common self-deception at this decision point.
- **On Louis's agency-to-shape-ambition hypothesis:** engage it seriously. Yes, Louis can push Pierre to aim for 1B+. But ambition does not collapse 3–5 orders of magnitude of published overhead. Pushing for frontier-scale likely means landing at 10–100M with a "we aimed high, physics didn't cooperate" narrative — which is a *weaker* credential than deliberately scoping smaller and nailing it. "I can define what we accomplish" has limits the cryptographic literature has been documenting for 3 years. If the answer to the §6.1 questions doesn't produce a credible path to frontier-scale, the hypothesis collapses.
- Engage the Pierre relationship honestly. The friendship is real and valuable. But friendship-aligned career moves are the most common source of later-career regret in fields where comparative advantage and personal values pull apart. Pierre is not going anywhere — the ZKP verification question will be more tractable in 3 years when TEE primitives mature and Louis has frontier-engineering authority to bring to it.
- Engage the guardian/builder tension honestly. Louis is a builder by every signal — §6 of the presentation betrays it, the current agentic-systems enthusiasm betrays it, the ICONO / 42AI leadership history betrays it, the early conversations with Kyutai / Pruna / SV betray it. The guardian frame subsumes the builder voice rather than synthesizing with it. A true builder says "build at Kyutai now, engage governance from technical authority in 5 years" — not "pause building to prevent extinction."
- Push on the 10% overhead / Pierre's technical claim: if it holds it's extraordinary, but Louis cannot verify it without signing up, and signing up is the expensive move. The literature explicitly flags extending ZKP to training LLMs as possibly "insurmountable" (zkLLM authors, 2024). Pierre may have private knowledge, but the base rate on "unpublished breakthrough claimed informally before commitment" is not encouraging.
- Argue: the highest-leverage move for Louis-shaped people is to build at the frontier, become technically respected, and then redirect governance from a position of authority. That path exists (Olah, Brown, Hubinger, Leike-at-Anthropic) and has stronger base rates than the detour path.
- **Name the cost plainly.** The career-trajectory data is not a "reduced probability of return" — it is near-total commitment. Louis should sign only if he is prepared to treat the grant as permanent career redirection. If he is not, the grant is the wrong move regardless of the technical merits.

**What Monk B must not do:** dismiss safety. Denigrate Pierre. Reduce the argument to compensation. Treat governance work as unserious. Soft-pedal the value of what Louis might build at GPAI — acknowledge it and argue it's the wrong work for Louis specifically.

---

## 9. Values hierarchy for synthesis check

When Phase 5 synthesis is drafted, it must survive the following tests derived from Louis's own testimony:
- Does it honor Louis's claim to want to deliver value for humanity?
- Does it honor Louis's claim that the existential-risk concern is real?
- Does it address the relational weight of Pierre without subordinating the decision to it?
- Does it let the builder voice speak at full volume (§6 of the presentation) rather than subsuming it?
- Does it provide a test Louis can run before committing (e.g., specific Pierre conversation, specific email to Abbaszadeh, specific clause in engagement)?
- Does it dissolve the bounded-detour framing honestly rather than accepting or rejecting it?

---

## 10. What this dialectic cannot resolve

- Whether Pierre's 10% overhead claim is real (empirical, requires Pierre conversation)
- Whether GPAI Policy Lab's funders are aligned (requires Pierre conversation)
- Whether a specific frontier role exists for Louis right now (requires real offers, not early conversations)
- Whether Louis's life-level constraints (financial runway, partner, family) shift the weights (not surfaced in interview)

The synthesis will be provisional on these resolving. Phase 6 validation should flag if the synthesis depends on assumptions about these that Louis cannot verify.
