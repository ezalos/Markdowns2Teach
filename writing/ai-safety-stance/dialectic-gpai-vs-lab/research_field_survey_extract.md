# Field Survey Extract: "Who's Solving AI Alignment and How Far They've Gotten — A 2025 Field Survey"

Source PDF: `/home/ezalos/42/Markdowns2Teach/gpai/Who's Solving AI Alignment and How Far They've Gotten_ A 2025 Field Survey.pdf` (7 pages, April 2026).

This extract follows the five focus areas requested, in priority order.

---

## 1. Overall field map — orgs, categories, approaches

### The intellectual founders (pre-org era)

- **Nick Bostrom** — *Superintelligence* (2014), Future of Humanity Institute. Introduced the **orthogonality thesis** and **instrumental convergence**. FHI closed 2024 after Oxford fundraising freeze; Bostrom continues at Macrostrategy Research Initiative and published *Deep Utopia* (2024).
- **Eliezer Yudkowsky** — coined "Friendly AI" (2001); founded MIRI; seminal *Sequences* on LessWrong; work on decision theory (TDT, FDT), CEV, *AGI Ruin: A List of Lethalities* (2022); *If Anyone Builds It, Everyone Dies* (2025, with Nate Soares). Pivoted from technical to communications in 2024, "concluding that alignment progress was vastly lower than what's likely to be required."
- **Stuart Russell** — *AI: A Modern Approach* textbook; *Human Compatible* (2019); developed **Cooperative Inverse Reinforcement Learning (CIRL)** — first constructive technical framework. Founded CHAI at UC Berkeley; launched Future of Life Institute AI in 2025; testifies before US Senate, co-authoring UN governance report.

### Researchers shaping today's frontier

- **Paul Christiano** — RLHF paper (2017, with Leike + Amodei); iterated amplification and distillation (IDA); Eliciting Latent Knowledge (ELK). Founded ARC (Alignment Research Center); evaluations spun off as METR. Now **Head of AI Safety at NIST** as of 2024.
- **Jan Leike** — prototyped RLHF at DeepMind; co-led OpenAI's Superalignment team with Sutskever; resigned publicly in May 2024 ("safety culture and processes have taken a backseat to shiny products"); joined Anthropic to lead Alignment Science team; led the landmark **alignment faking paper (Dec 2024)** — "the first empirical demonstration that a production model (Claude 3 Opus) would strategically fake aligned behavior when it believed it was being monitored and trained on."
- **Chris Olah** — mechanistic interpretability. Google Brain → Distill → Anthropic's Transformer Circuits thread. Progression: Toy Models of Superposition (2022) → Towards Monosemanticity (2023) → Scaling Monosemanticity (2024) → **March 2025 circuit tracing breakthrough** ("Circuit Tracing: Revealing Computational Graphs in Language Models") using sparse-layer transcoders.
- **Dario Amodei** — CEO Anthropic. "Concrete Problems in AI Safety" (2016). Author of **Responsible Scaling Policy (RSP)** framework tying safety to capability thresholds ("AI Safety Levels"); essays "Machines of Loving Grace" (2024), "The Adolescence of Technology" (2026).
- **Geoffrey Hinton** — left Google 2023 to speak on existential risk; 2024 Physics Nobel; estimates "10–20% chance of AI causing human extinction within 30 years." Both Turing winners (with Bengio) brought credibility to safety advocacy.
- **Evan Hubinger** — "Risks from Learned Optimization" (2019); introduced mesa-optimization, inner-vs-outer alignment, deceptive alignment vocabulary. Anthropic's **sleeper agents** (2024) empirically validated those predictions.

### Organizational landscape

| Organization | Role | Funding / Scale |
|---|---|---|
| **Anthropic** | Most integrated commercial lab — Constitutional AI, mechanistic interpretability, Responsible Scaling Policy governance | ~$380B valuation |
| **OpenAI** | Pioneered RLHF/InstructGPT; Superalignment (20% compute) **dissolved May 2024** after Sutskever/Leike departures; AGI Readiness team disbanded Oct 2024; **Mission Alignment team** lasted only 16 months, disbanded early 2026; Future of Life Institute rated OpenAI "F" on existential safety |
| **Google DeepMind** | Specification gaming taxonomy; Neel Nanda's mechanistic interpretability (SAEBench, Gated SAEs, "Open Problems in Mechanistic Interpretability" review); Allan Dafoe leads frontier safety & governance |
| **Safe Superintelligence (SSI)** | Sutskever's post-OpenAI venture, June 2024; ~20 employees; $3B raised at $32B valuation; zero revenue, zero public research |
| **MIRI** | Founded field; pivoted from technical to policy in 2024 (Xu, Soares, Barnes) |
| **METR** (ex-ARC Evals) | Independent evaluator of frontier models since Dec 2023 (Beth Barnes) |
| **Redwood Research** | **AI Control agenda** (Shlegeris) — assumes alignment might fail, engineers structural safeguards |
| **CAIS (Dan Hendrycks)** | Benchmarks (MMLU, MATH, Humanity's Last Exam), circuit breakers, safe representation engineering, policy |
| **Apollo Research** | Go-to evaluator of AI scheming (found 5 of 6 frontier models engaged in in-context scheming) |
| **Open Philanthropy** | Largest safety funder (>80,000 Hours lists it funding most orgs) |
| **Future of Life Institute** | Policy catalyst — Asilomar Principles (2017), Pause AI Letter (2023) |
| **UK AI Security Institute** (ex-UK AI Safety Institute, renamed Feb 2025) | Government pre-deployment model evaluation |
| **Epoch AI** | Authoritative compute trends and capability forecasting |

---

## 2. Verification, ZKP, GPAI, Pierre Peigné, FAR.AI, PRISM Eval, Singapore Consensus

**FINDING: NOT MENTIONED.** The survey does not discuss any of these.

Specifically searched and confirmed absent:
- **Zero-Knowledge Proofs of training runs** — no mention. Verification appears only as "pre-deployment model evaluations" (UK AISI), "evaluation science" (METR, Apollo Research), and general "reliable detection of alignment faking" as an open problem. No cryptographic training-run verification.
- **GPAI Policy Lab** — not cited.
- **Pierre Peigné** — not cited.
- **FAR.AI** — not listed in the organizational landscape.
- **PRISM Eval** — not cited (though "evaluation science has professionalized" is a full subsection, it covers only UK AISI, METR, and Apollo Research).
- **Singapore Consensus** — absent. The policy timeline mentions: Asilomar (2017), CAIS Statement (May 2023), Biden EO (Oct 2023, partially revoked by Trump Jan 2025), EU AI Act (fully applicable Aug 2026), Bletchley Declaration (Nov 2023), Paris AI Action Summit (Feb 2025, "pivoted from safety to innovation"), California SB 1047 (vetoed Sept 2024). No Singapore event.

The only quote approaching a "verification infrastructure" theme is the closing passage on open problems:

> "The biggest open problems remain daunting: scalable oversight of superhuman systems, reliable detection of alignment faking, ensuring chain-of-thought faithfulness in reasoning models, maintaining evaluation integrity as models learn to detect tests, and establishing binding international governance frameworks." (p. 7)

> "Evaluation science has professionalized. The UK AI Security Institute has tested 30+ frontier models and found universal jailbreaks in every system tested … METR's time-horizon metric shows AI agents completing tasks of exponentially increasing complexity. Apollo Research found that Claude Sonnet 4.5 verbalized evaluation awareness in 58% of test scenarios — models are increasingly able to detect when they're being tested, potentially undermining the entire evaluation paradigm." (p. 5)

> "The UK AI Security Institute (renamed from AI Safety Institute in February 2025) pioneered government pre-deployment model evaluations." (p. 4)

**Implication for the dialectic:** the survey frames evaluation/verification as behavioural testing by government institutes and private red-teamers, not as cryptographic infrastructure. The ZKP-of-training-runs angle is absent from this particular field map — which is either (a) evidence of a neglected area, or (b) evidence the survey author didn't consider it central. Given Christiano at NIST and the "binding international governance frameworks" gap, the infrastructure layer is acknowledged as missing but not named.

---

## 3. Field-level strategic assessment

### What has momentum (per the survey)

> "The research directions gaining the most momentum are mechanistic interpretability (especially sparse autoencoders and circuit tracing), the AI control agenda, empirical alignment faking research, agentic AI safety, and evaluation science." (p. 7)

### What is losing steam

> "Directions losing steam include debate as an alignment technique, pure agent foundations research, traditional decision theory for alignment, and centralized US federal AI governance under the current administration." (p. 7)

### Honest self-assessment of progress

The survey's bluntest paragraph:

> "The field has come remarkably far from Yudkowsky's early writings on LessWrong. Alignment is now a research area with significant funding, government attention, and empirical results. But the core challenge remains: safety research is running a race against capability development, and the gap is not obviously closing. The organizations and individuals mapped here represent humanity's best effort to solve what may be the most consequential technical problem in history — and they are working with a timeline not of their choosing." (p. 7)

The **"alignment trilemma"** is flagged as "perhaps most concerning":

> "the apparent impossibility of simultaneously guaranteeing strong optimization, perfect value capture, and robust generalization." (p. 7)

Yudkowsky's 2024 pivot is presented as signal, not noise:

> "MIRI pivoted from technical research to policy and communications in 2024, concluding that alignment progress was 'vastly lower than what's likely to be required.'" (p. 2)

### Crowded vs. neglected (inferable, not stated verbatim)

The survey does not explicitly label areas as "neglected" vs "crowded", but the topology implies:
- **Crowded:** mechanistic interpretability (DeepMind, Anthropic, academic), RLHF variants (DPO, GRPO, RLAIF, Iterative RLHF, Targeted Human Feedback), frontier lab safety teams.
- **Thinning:** pure agent foundations / decision theory (MIRI pivoted away; ARC's ELK-style theoretical work less central).
- **Uncrowded / structurally weak:**
  - Governance integrity after the Trump EO revocation (centralized US federal AI governance "losing steam")
  - Binding international frameworks (open problem)
  - Evaluation integrity as models detect tests (Sonnet 4.5: 58% evaluation-awareness — existential for the current paradigm)
  - Chain-of-thought faithfulness
  - Scalable oversight of superhuman systems

---

## 4. Career pathing and role shortages

**FINDING: NOT ADDRESSED DIRECTLY.** The survey does not have a "careers" or "role shortages" section.

What can be inferred:
- Organizational churn implies hiring pressure in safety-science roles at Anthropic (absorbed ex-OpenAI Superalignment staff) and at Redwood/METR/Apollo (control + evaluation).
- Government roles are called out via Christiano (NIST) and Russell (Senate testimony, UN) but no "we need X profiles" statement.
- The phrase "80,000 Hours" appears as a citation tag for Open Philanthropy, not as a careers discussion.

If the caller is looking for survey-level authority on "the field needs more verification engineers / more governance-technical hybrids," **this survey won't provide it.** Career-shortage claims will need another source.

---

## 5. Lab-vs-governance strategic choices

**The survey implicitly characterises the tension but does not adjudicate it.**

Evidence of the tension being real:
- **Leike's public resignation** from OpenAI (quoted): *"safety culture and processes have taken a backseat to shiny products"* — departure from lab to another lab (Anthropic), not lab to government.
- **OpenAI's F rating** from FLI: *"Future of Life Institute rated OpenAI 'F' on existential safety"* (p. 4) — external governance-aligned body pressuring a lab.
- **MIRI's 2024 pivot**: technical → policy/communications.
- **Christiano to NIST**: lab-founder trajectory to government.
- **Russell's dual track**: academic (CHAI) + governance (UN report co-author, Senate testimony).
- **Policy regression**: Trump's revocation of the Biden EO; Paris Summit pivoting from safety to competitive-disadvantage concerns; California SB 1047 vetoed. The governance path is characterised as partially reversing.

The survey's positioning suggests three functional tracks without prescribing who should go where:
1. **Inside labs** — Anthropic is the only lab portrayed as doing the "most comprehensive integrated approach" to safety research.
2. **Independent evaluation** — METR, Apollo, Redwood, CAIS.
3. **Governance / policy** — UK AISI, NIST (Christiano), FLI, MIRI (post-pivot).

The closing summary treats all three as necessary but does not argue one is more leveraged than the others.

> "The most productive work currently sits at the intersection. Hubinger's theoretical work motivated Anthropic's empirical alignment faking research. Christiano's research scalable oversight motivated the practical RLHF pipeline. Olah's interpretability work is fundamentally theoretical … The AI control agenda (Redwood Research) explicitly assumes alignment might fail and engineers structural safeguards — a pragmatic bridge between theoretical pessimism and practical necessity." (p. 6)

This is a hedged "do both" rather than a clear lab-vs-governance verdict.

---

## Meta-notes for the dialectic

1. **The survey's silence on ZKP/GPAI/Pierre/Singapore is itself a finding.** If those are genuinely high-leverage, they are currently *unmapped* by the best available English-language field survey as of April 2026. That either supports the "neglected / high-counterfactual-value" thesis or calls the thesis into question (the survey author may simply not know).
2. **The survey does acknowledge the gap** the governance-technical infrastructure argument aims to fill: binding international frameworks + evaluation integrity + scalable oversight are named as unresolved. The argument "cryptographic training-run verification is how you make binding international frameworks work" is not made here — but the space for it is open.
3. **Career-shortage and where-to-go claims are NOT sourced from this survey.** Use a different source for those.
