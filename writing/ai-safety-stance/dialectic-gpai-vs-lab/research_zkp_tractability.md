# Is ZKP-verified large-scale AI training achievable in 12 months?

**Research brief for Louis · April 2026**
Stress-testing Pierre Peigne's claim of a "first public demo at scale" under a GPAI Policy Lab grant

---

## Executive verdict

**Aspirational by 3-5x, not impossible, but only if "at scale" is defined very generously.** As of April 2026, published zero-knowledge proofs of *training* top out at ~10M parameter CNNs (Kaizen, VGG-11) with ~15-22 minute prover times *per iteration*. Published zkML proofs of *inference* have just reached LLaMA-13B (zkLLM, 15 minutes per forward pass). There is a ~3-5 order-of-magnitude gap between the state of the art and a frontier training run (10^25 FLOP, 10^11+ parameters, 10^5+ iterations). No public roadmap from any serious lab commits to closing that gap in 12 months. Pierre's claim is best read as **"we can demo a toy-to-mid-scale end-to-end pipeline that is directionally convincing to policymakers"** — which *is* achievable in 12 months and *is* genuinely useful for governance. It is not "we can cryptographically verify GPT-4-class training."

If Louis takes the grant expecting to ship rigorous ZKP verification of a frontier training run, he will be disappointed. If he takes it expecting to ship a credible proof-of-concept that moves policy conversations forward and slots into the flexHEG/verification-mechanisms agenda, it is doable.

---

## 1. Current state of ZKML (April 2026)

### Inference — near-production for ≤13B models

| System | Year | Model | Prover time | Hardware | Note |
|---|---|---|---|---|---|
| ZKML (Kang et al., EuroSys'24) | 2024 | GPT-2 (1.5B) | ~1 hour | 32 vCPU, 1TB RAM | First end-to-end LLM inference ZKP |
| zkLLM (Sun et al., CCS'24) | 2024 | LLaMA-2 13B | ~15 min / forward pass | A100, 23GB VRAM | Dedicated attention protocol (zkAttn); OOM on zkML beyond 1.5B |
| zkGPT (USENIX'25) | 2025 | GPT-2 | ~22 s | Single thread | 13× speedup over ZKML via GKR/sumcheck |
| ZKTorch (Kang, 2025) | 2025 | MLPerf edge suite | Variable | CPU/GPU | First universal ZKML compiler; covers LLMs + vision + RecSys |
| NanoZK (2026) | 2026 | LLM layers | Constant 6.9KB proof/layer | CPU | Transparent setup, selective verification |

**Bottom line on inference:** genuinely practical for models ≤13B; hours per proof is workable for audit-style verification (not real-time). Active research front: GKR-based systems, hardware acceleration (NoCap, 3 orders of magnitude speedup), and layerwise constant-size proofs.

### Training — stuck at 10M parameters

| System | Year | Model trained | Prover time / iteration | Memory |
|---|---|---|---|---|
| zkPoT (Garg et al., 2023) | 2023 | Logistic regression | 4,208 s total | 512 GB RAM |
| zkDL (2023) | 2023 | 8-layer MLP, 10M params, CIFAR-10 | <1 s / batch update | GPU (CUDA) |
| **Kaizen (Abbaszadeh et al., 2024)** | 2024 | **VGG-11, 10M params, batch 16** | **~15-22 min / iteration** | 512 GB RAM, 8× Xeon Platinum |
| SUMMER (2025) | 2025 | Mini-Char-RNN, 12M params | 70 s / iteration | Constant proof size via Merkle folding |
| Verifiable Fine-Tuning (VFT, 2025) | 2025 | LoRA adapters only | Not yet benchmarked at scale | Targets PEFT, not full training |

The **best published result for ZKP-of-training** (Kaizen, IACR ePrint 2024/162, presented at S&P) handles VGG-11 with 10 million parameters, 43× faster than generic recursive SNARKs, and still requires **15-22 minutes of prover time per training iteration**. A 1B parameter model trained for 100k iterations at that rate would require decades. This is the hard bound Pierre's demo must contend with.

Source: [Kaizen paper](https://eprint.iacr.org/2024/162.pdf); [survey arXiv 2502.18535](https://arxiv.org/html/2502.18535v2).

### Sources and key publications

- **Survey**: [Xing et al., *A Survey of ZKP-Based Verifiable ML*, Aug 2025](https://arxiv.org/html/2502.18535v2) — covers 27 systems from 2017-2025
- **Kaizen**: [Abbaszadeh et al., *ZKPs of Training for DNNs*, 2024](https://eprint.iacr.org/2024/162.pdf)
- **zkLLM**: [Sun et al., CCS 2024](https://arxiv.org/abs/2404.16109)
- **zkGPT**: [Qu et al., USENIX Security 2025](https://eprint.iacr.org/2025/1184.pdf)
- **SUMMER (RNN training)**: [eprint 2025/1688](https://eprint.iacr.org/2025/1688.pdf)
- **Verifiable Fine-Tuning**: [arXiv 2510.16830](https://arxiv.org/html/2510.16830v2)
- **EZKL benchmarks**: [EZKL blog](https://blog.ezkl.xyz/post/benchmarks/)

---

## 2. Key researchers and organizations

| Name / Org | Focus | Relevant to training verification? |
|---|---|---|
| **Daniel Kang (UIUC)** | ZKML, ZKTorch, MLPerf benchmarks | Inference only. Podcast (Zero Knowledge Podcast ep. 370) — no training claims |
| **Yupeng Zhang (UIUC)** | zkCNN, Libra, Virgo, zkLLM co-author | Strong theoretical foundations; published training work is on simple models |
| **Hongyan Zhang (Berkeley/IC)** | zkLLM lead | Inference only; says in paper training LLMs "may pose insurmountable challenges" |
| **Jason Gross (Theorem)** | Compact formal proofs via mechanistic interpretability | Orthogonal path: proving properties of trained models, not training process. NeurIPS 2024 paper on GPT-2-sized models |
| **Modulus Labs** | Productized ZKML inference | Closed-source; limited to small models; not training |
| **EZKL** | ONNX → Halo2 compiler | "Struggles beyond 1M parameters" per NanoZK paper |
| **Gensyn** | Decentralized training verification | Uses probabilistic Proof-of-Learning + refereed delegation (**not ZKP**). Verde paper: "cryptographic proofs are prohibitively expensive for large-scale ML workloads" |
| **FAR.AI** | Singapore Consensus co-publisher | Policy + research coordination, not direct ZKP research |
| **AVERI (AI Verification & Evaluation Research Institute)** | Third-party frontier AI auditing | New 501(c)(3), 2025 launch; focuses on access-based auditing, not cryptographic |
| **Seldon Lab** | "HTTPS for AI safety" — ZKP infra | SF-based accelerator; explicitly lists ZKP for AI safety as mission. Pierre Peigné is on Luma for their IASEAI 2026 side event |
| **MIRI / RAND / GovAI** | Verification mechanisms for AI treaties | Concept papers (Scher & Thiergart 2024, Wasil et al. 2024); advocate TEE+hardware over pure ZKP |
| **flexHEG** consortium | Hardware-enabled governance | Explicit 12-month TRL-raising call in 2024; targets **2027 deployment**. Sees ZKP as *complementary* to TEE, not primary |
| **Pierre Peigné (PRISM Eval + GPAI Policy Lab)** | Red-teaming, behavior elicitation, multi-agent security | **Published work is on LLM red-teaming (BET), multi-agent security (AAAI 2025), not ZKP/cryptography.** He is a *co-signer* of the Singapore Consensus, not a primary verification-mechanism researcher. He is **hosting** an IASEAI 2026 side event on verification, which is community convening, not technical delivery |

Source links: [Pierre Peigné LinkedIn post on IASEAI side event](https://www.linkedin.com/posts/pierre-peign%C3%A9-146b6316a_ai-verification-mechanisms-and-dacc-happy-activity-7424398329482104832-Exzs); [Luma event](https://luma.com/jjb3kt22); [PRISM Eval](https://www.tii.ae/seminar/ai-seminar-series-pierre-peigne); [AAAI 2025 paper](https://arxiv.org/abs/2502.19145); [Gensyn Verde paper](https://arxiv.org/html/2502.19405v1).

**Significant finding:** I could not locate any Pierre Peigné publication on cryptography, ZKP, or formal verification. His technical track record is LLM safety/red-teaming. This does not disqualify him from leading a governance-oriented verification project, but it means the claim "ZKP demo at scale in 12 months" rests on him assembling and directing a team, not executing personally.

---

## 3. Known bottlenecks (why training is much harder than inference)

1. **Commitment schemes for billion-parameter gradient updates.** Every iteration, the prover must commit to (a) the current weights, (b) the sampled batch, (c) the computed gradients, (d) the updated weights, and prove consistency. Each commitment is O(n) in the parameter count with non-trivial constants. zkLLM authors estimate that extending beyond 13B inference already requires novel cryptography; training multiplies this by the number of iterations.

2. **Non-linear operations (softmax, GeLU, LayerNorm) in finite-field arithmetic.** ZKPs operate on arithmetic circuits over finite fields. Floating-point multiplication, division, and transcendental functions require expensive lookup-argument decomposition. zkLLM's zkAttn protocol exists specifically because generic ZKP for softmax blew up. Training adds backward-pass derivatives of these same nonlinearities.

3. **Proving data provenance.** The Verifiable Fine-Tuning paper (arXiv 2510.16830) explicitly notes that pre-commitment to the data universe before training begins is necessary — otherwise the prover can retroactively claim any plausible dataset. This requires Merkle/polynomial commitments over datasets that can reach petabyte scale for frontier pre-training.

4. **Proof-of-Learning is broken.** Jia et al.'s Proof-of-Learning (2021) was cryptography-free; ["Adversarial Examples for Proof-of-Learning"](https://arxiv.org/pdf/2108.09454) demonstrated spoofing attacks in 2022. Gensyn's Verde paper explicitly rejects heuristic PoL: "fails to detect small-scale data manipulations, such as injecting backdoored data." So the "cheap" alternative to full ZKP is known-unsafe.

5. **Hardware non-determinism.** GPU matrix multiplications are not bitwise reproducible across hardware (floating-point reorder), so the verifier cannot re-execute to check. Gensyn had to build RepOps (reproducible operators) to work around this. No ZKP solves this — it must be handled at the compute-kernel layer first.

6. **Generic SNARKs are 1000× slower than training.** The Kaizen paper quantifies this explicitly: "succinct zero-knowledge proofs incur prohibitive prover costs… at least 1000× slowdown compared to the training time." Their specialized GKR-sumcheck system improves this by 43× — still ~25× slower than training. For a frontier run that takes 3 months of wall-clock time at 10^4 GPUs, the prover overhead would be decades.

**Literature's own timeline estimates:** the zkLLM authors wrote (2024): *"extending zero-knowledge proofs to training LLMs may pose insurmountable challenges."* The flexHEG consortium targets **2027** for hardware-enabled verification deployment, and treats ZKP as one tool among several (TEE, FlexHEG, confidential computing).

---

## 4. Governance / policy landscape

### Singapore Consensus on Global AI Safety Research Priorities (May 2025, arXiv 2506.20702)

Pierre Peigné is listed as a co-signer (affiliation: PRISM Eval), alongside 100+ others from 11 countries, convened at SCAI 2025 and led by Yoshua Bengio. The report uses verification as a central concept but **does not prescribe ZKP specifically**. Verification appears under the "Assessment" defence-in-depth pillar, framed as part of specification-validation-assurance-verification. The report cites hardware governance (Sastry et al., ["Computing Power and the Governance of AI"](https://arxiv.org/abs/2402.08797)) as a key reference.

Source: [Singapore Consensus PDF](https://aisafetypriorities.org/files/Singapore_Consensus_2025.pdf?v=1.2); [SCAI website](https://www.scai.gov.sg/2025/scai2025-report/); [FAR.AI hosted version](https://far.ai/research/the-singapore-consensus-on-global-ai-safety-research-priorities).

### Other policy-side actors pushing ZKP-adjacent verification

- **Oxford AI Governance Initiative (AIGI)** — [Verification for International AI Governance](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Verification_for_International_AI_Governance.pdf), July 2025. Emphasizes confidential computing + hardware attestation over pure ZKP.
- **UK AISI (AI Security Institute)** — Challenge Fund Priority Research Areas 2025 lists verification; funds work on "Proving Model Equality in Zero-Knowledge" (SPAR project by Pascal Berrang, Birmingham).
- **GPAI-OECD SAFE Project** — Technical trustworthiness and data governance; [2024 report](https://wp.oecd.ai/app/uploads/2025/09/final-GPAI-2024-SAFE-Reports-Technical-Trustworthiness-and-Data-Governance-Assurance-of-Models.pdf). References verification but frames it broadly.
- **MIRI TGT-AI RFI 2025** — [MIRI submission](https://files.nitrd.gov/90-fr-9088/MIRI-TGT-AI-RFI-2025.pdf) pushes FlexHEG as primary mechanism, not ZKP.
- **flexHEG consortium** — [Report v2 parts I/II/III](https://www.flexheg.com/), targets 2027 deployment. ZKP is explicitly optional/supplementary.
- **EU AI Act** — Compute threshold (10^25 FLOP) for GPAI models creates demand for verifiable compute accounting. No ZKP requirement.

### On the Pierre Peigné / IASEAI 2026 verification side-event

Pierre's [November 2025 LinkedIn announcement](https://www.linkedin.com/posts/pierre-peign%C3%A9-146b6316a_ai-verification-mechanisms-and-dacc-happy-activity-7424398329482104832-Exzs) frames the event's guiding questions as: *"What can we realistically verify today? What would more robust verification require?"* — a diagnostic framing, not a delivery commitment. This is consistent with a policy-lab convening role.

---

## 5. The specific "12-month demo at scale" claim

### Has anyone publicly committed to it?

**No public party has committed to a 12-month ZKP demo of frontier-scale training.** The nearest comparable commitments:

- **flexHEG SFF 2024 funding call** — [Survival and Flourishing Fund](https://survivalandflourishing.fund/2024/flexhegs-application) explicitly asked for TRL 2-4 → TRL 6-7 prototypes "within 12 months" — but for hardware-enabled guarantees, not ZKP of training. Deployment target is 2027.
- **Gensyn mainnet** — Late 2024, launched decentralized training with Verde verification (refereed delegation + RepOps, **not ZKP**). They abandoned pure ZKP as "prohibitively expensive for large-scale ML workloads."
- **Seldon Lab Act 1 cohort (2025)** — Accelerator for AI safety/assurance startups including ZKP-adjacent ones; 12-week program, pilot-scale deliverables.
- **SPAR project "Proving Model Equality in Zero-Knowledge"** (Pascal Berrang, Birmingham, 2026) — Scoped narrowly to *equality* of weights vs. committed reference, not full training verification.

### Is 12 months realistic?

If "demo at scale" means:

- **A ZKP of training for a ~10-100M parameter model** (order-of-magnitude step up from Kaizen's 10M), with aggressive engineering and 1-2 FTEs of cryptographer + ML systems engineer → **credible in 12 months**. This is what Pierre can actually deliver.
- **A ZKP of training for a 1-10B parameter model** → requires research breakthroughs on commitment scaling and nonlinear-operation proving. Not credibly done in 12 months.
- **A ZKP of a frontier (10^25 FLOP+) training run** → requires research breakthroughs across cryptography, ML systems, and hardware. 3-5x optimistic.
- **An end-to-end governance pipeline demonstration** (data provenance commitment → training proof → evaluation → policy consumer consuming the proof) on a toy model (GPT-2 scale or smaller) → **very doable in 12 months** and arguably more policy-relevant than frontier-scale demo.

---

## Honest assessment

**Verdict: (iii) aspirational by 3-5x** if "at scale" means frontier-model training. **(ii) credible stretch goal** if it means an end-to-end governance-relevant pipeline on a small-to-medium model. **(i) already near-done** is not true by any reasonable reading.

Louis should ask Pierre these three specific questions:

1. **"What is the target model size for the demo?"** If <100M params — credible. If >1B — skeptical. If Pierre hedges, that is a red flag.
2. **"What is the cryptographic primitive?"** If "ZKP" means zk-SNARK of full training → implausible. If it means a hybrid (TEE attestation + ZKP for selected components + commitment schemes for provenance) → plausible and more policy-relevant. If it means "we extend Kaizen-style proofs" → scoped.
3. **"Who on the team has published cryptography?"** If the answer is no one, the project needs to partner with Zhang/Kang/Abbaszadeh or a comparable group. Policy-lab wrapping of academic-group execution is a legitimate model, but it must be acknowledged.

A 12-month Pierre-led effort is far more likely to produce a **policy-shaped prototype and coalition** (useful for GPAI/OECD/EU AI Act discussions) than a **cryptographic breakthrough** (which would be a 3-5 year research program). For Louis, the choice is: do you want to work on the former (governance engineering with cryptographic flavor) or the latter (deep cryptography research)? Those are different careers.

---

## Sources and References

1. [Kaizen: Zero-Knowledge Proofs of Training for Deep Neural Networks (Abbaszadeh et al., 2024)](https://eprint.iacr.org/2024/162.pdf) — State of the art for zkPoT, VGG-11 10M params
2. [A Survey of ZKP-Based Verifiable ML (Xing et al., 2025)](https://arxiv.org/html/2502.18535v2) — Covers 27 systems 2017-2025
3. [zkLLM: ZKPs for Large Language Models (Sun et al., CCS 2024)](https://arxiv.org/abs/2404.16109) — LLaMA-13B inference, 15 min/forward pass
4. [zkGPT non-interactive ZKP for LLM inference (USENIX 2025)](https://eprint.iacr.org/2025/1184.pdf) — 22s GPT-2 proofs
5. [zkDL: ZKPs of Deep Learning Training (SafeAILab)](https://arxiv.org/pdf/2307.16273) + [GitHub](https://github.com/SafeAILab/zkDL) — CUDA backend
6. [SUMMER: Recursive ZKPs for Scalable RNN Training (2025)](https://eprint.iacr.org/2025/1688)
7. [Verifiable Fine-Tuning for LLMs (arXiv 2510.16830, 2025)](https://arxiv.org/html/2510.16830v2) — PEFT/LoRA focus
8. [Singapore Consensus on Global AI Safety Research Priorities (Bengio et al., May 2025)](https://aisafetypriorities.org/files/Singapore_Consensus_2025.pdf?v=1.2) — Peigné co-signer
9. [Flexible Hardware-Enabled Guarantees (flexHEG reports I/II/III, 2025)](https://www.flexheg.com/report-1.pdf) — 2027 deployment target
10. [Verification for International AI Governance (Oxford AIGI, July 2025)](https://aigi.ox.ac.uk/wp-content/uploads/2025/07/Verification_for_International_AI_Governance.pdf)
11. [Hardware-Level Governance of AI Compute (arXiv 2604.04712, 2026)](https://arxiv.org/html/2604.04712v1) — Feasibility taxonomy
12. [Gensyn Verde paper (arXiv 2502.19405, 2025)](https://arxiv.org/html/2502.19405v1) — Rejects pure ZKP for training
13. [Adversarial Examples for Proof-of-Learning (arXiv 2108.09454)](https://arxiv.org/pdf/2108.09454) — Why PoL is broken
14. [Pierre Peigné IASEAI 2026 side-event announcement (LinkedIn, Nov 2025)](https://www.linkedin.com/posts/pierre-peign%C3%A9-146b6316a_ai-verification-mechanisms-and-dacc-happy-activity-7424398329482104832-Exzs)
15. [AVERI / Frontier AI Auditing (2026)](https://www.averi.org/) — Access-based audit vision, complementary to ZKP
16. [Seldon Lab mission](https://seldonlab.com/mission) — "HTTPS for AI safety" framing
17. [EZKL benchmarks blog](https://blog.ezkl.xyz/post/benchmarks/) — EZKL vs. Orion vs. RISC Zero
18. [Compact Proofs of Model Performance via Mechanistic Interpretability (Gross et al., NeurIPS 2024)](https://proceedings.neurips.cc/paper_files/paper/2024/file/90e73f3cf1a6c84c723a2e8b7fb2b2c1-Paper-Conference.pdf) — Jason Gross work, orthogonal to ZKP of training
19. [SVIP: Verifiable Inference of Open-Source LLMs (ICLR 2025)](https://openreview.net/pdf/b3402cfe0da33c7d11b0fb1c8b63c86910fb19c5.pdf) — Statistical verification alternative to ZKP

## Additional notes

- I could not locate any peer-reviewed Pierre Peigné publication on cryptography, formal verification, or ZKP; his technical record is red-teaming (BET, PRISM Eval) and multi-agent security (AAAI 2025). This shifts the risk model: the grant depends on his ability to assemble and lead a cryptographic team, not deliver personally.
- The field is evolving fast. Between April 2024 (zkLLM at 13B inference) and April 2026, inference scale doubled and proof times dropped ~100×. Linear extrapolation is risky — nonlinearities (bottleneck shifts, hardware changes) dominate.
- **If Louis wants to sanity-check in person**: the IASEAI 2026 side-event in Paris hosted by Pierre is explicitly designed for exactly this question. Attending (or obtaining the attendee list of cryptographers) would quickly reveal whether the 12-month claim has named cryptographers backing it or is a community-convening aspiration.
- An underrated alternative framing worth raising with Pierre: the most policy-valuable deliverable in 12 months is probably **not** a ZKP of training, but a rigorously benchmarked comparison of ZKP vs. TEE vs. FlexHEG vs. refereed-delegation for AI-governance use cases, with demo code. That is tractable, original, and directly feeds the OECD/GPAI/EU AI Act conversations Pierre is already in.
