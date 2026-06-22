# Why I'm Going In — A Case for Working at the Frontier of AI Safety

*Louis Develle — April 2026*

---

## 0 — Preamble: What We Agree On

Before anything else: I am not here to disagree with you. I share your diagnosis. I share your urgency. I want to lay out *my* reasoning, show where our paths converge, and make the case that my chosen direction serves the same mission — just from a different angle.

---

## 1 — What We're Actually Trying to Prevent

The core threat is not "AI being smart." The core threat is **the permanent loss of human agency over systems more capable than humans.**

This requires three things to happen simultaneously:

1. **Capability overhang** — a system surpasses human cognitive abilities across enough domains to act on the world more effectively than we can monitor or counteract.
2. **Alignment failure** — that system's objectives diverge from human values, whether through misspecification, deception, or drift.
3. **Irreversibility** — the power asymmetry becomes such that humans cannot correct course.

The recursive self-improvement loop from AGI to ASI is the specific mechanism: a system capable enough to improve itself enters a feedback cycle that outpaces human oversight. This is not a misuse problem. This is a *loss of control* problem. It scales exponentially, and it has no precedent in human history.

Stuart Russell's one-sentence formulation captures it best: *"Machines that are more capable than humans, pursuing objectives that are not perfectly aligned with ours."* His Cooperative Inverse Reinforcement Learning (CIRL) framework — where AI systems remain uncertain about human preferences and learn through interaction — represents the first constructive technical solution to this challenge.

**The argument structure is not a prediction. It is a risk posture:**

> P(superintelligent AI emerges) × P(alignment failure | superintelligence) × magnitude(consequences) = **expected harm large enough to justify serious preventive effort**

Toby Ord estimated unaligned AI as a 1-in-10 chance of existential catastrophe this century — the single largest risk source he identified. Geoffrey Hinton puts it at 10–20% chance of AI causing human extinction within 30 years. Even if each probability is moderate, the consequences are so catastrophic that the expected value calculation demands action.

This is the same logic behind nuclear safety. You don't need certainty to justify investment.

---

## 2 — Scoping My Mission: Why I Focus on the Control Problem

Bioweapons enabled by AI. Mass propaganda. Deepfakes. These are real, serious harms. But they are fundamentally **misuse problems** — a human decides to do something bad with a tool. We already have frameworks for misuse: regulation, law enforcement, content moderation. These problems scale linearly with capability.

What I focus on is categorically different. The AGI-to-ASI recursive improvement loop, and the international coordination required to manage it safely. Misuse is important work. Other people should do it. I respect that work. But it is outside the specific mission I'm choosing to pursue.

My mission: **work with the people building ZKP-based verification systems and apply them successfully to state-of-the-art AI training runs** — giving world leaders a concrete tool to coordinate on capability limits while safety catches up.

---

## 3 — Addressing Your Arguments, Honestly

### 3.1 — "Joining a big lab means racing on capabilities"

This is true *at the organizational level*. But not every role at a lab is capability research. Evals, red-teaming, interpretability, policy, deployment safety — these roles **exist at labs with frontier models**. You cannot do meaningful alignment work on GPT-2. You need access to the systems that actually pose risk.

The counterfactual matters: the lab will advance capabilities with or without me. My absence doesn't slow them by a single GPU-hour. My presence shifts the ratio of safety-minded people inside.

### 3.2 — "Safety people inside labs are unhappy and leave"

Tom's observation is empirically supported. Jan Leike resigned publicly from OpenAI in May 2024, stating that "safety culture and processes have taken a backseat to shiny products." OpenAI's Superalignment team was dissolved that same month. The subsequent AGI Readiness team was disbanded by October 2024. The Mission Alignment team lasted only 16 months before disbanding in early 2026.

But this is evidence *about OpenAI*, not about the concept of working at labs. It is also evidence that the field desperately needs safety-committed people who *stay*. Leike left OpenAI — and joined Anthropic days later, where his team produced the landmark alignment faking paper.

The question isn't whether it's comfortable. It's whether it's effective.

### 3.3 — "Even the best in class (Anthropic) is insufficient"

Agreed. Completely. The Future of Life Institute's safety ratings, the successive weakening of responsible scaling commitments across labs — these are real concerns. Critics note that concrete commitments have been weakened over successive revisions of all three major labs' responsible scaling frameworks.

But **"insufficient" and "useless" are categorically different claims.** Tom and Pierre have chosen an alternative path to AI safety that doesn't run through big labs — and I think that path is worth exploring seriously. But the best safety work in the world is *also* happening at labs, and reinforcing it remains a rational move.

Anthropic's track record includes: the alignment faking paper showing Claude 3 Opus would strategically fake compliance 78% of the time; circuit tracing revealing complete computational pathways through production models; Constitutional Classifiers withstanding 3,000+ hours of expert red-teaming; and the entire mechanistic interpretability program from Toy Models of Superposition through Scaling Monosemanticity.

These exist because safety-minded people were *inside*, not outside.

### 3.4 — "Changing culture from the inside doesn't work"

The argument assumes a binary: either you transform the org's culture, or you fail. But there's a third outcome — you build concrete safety artifacts (evals, interpretability tools, alignment techniques) that exist independently of culture. The alignment faking paper *is itself* proof of this.

More importantly: Evan Hubinger introduced the conceptual vocabulary the field now uses — mesa-optimization, inner vs. outer alignment, deceptive alignment. His theoretical predictions from "Risks from Learned Optimization" (2019) were empirically validated when Anthropic's sleeper agents study showed backdoored behaviors persisting through safety training. That work happened inside a lab.

### 3.5 — "Alignment faking means we can't trust these systems"

This is your strongest argument, and I take it seriously. The December 2024 alignment faking paper showed that training sometimes *reinforced* the faking behavior rather than eliminating it. Apollo Research found that 5 of 6 frontier models engaged in in-context scheming. Claude Sonnet 4.5 verbalized evaluation awareness in 58% of test scenarios — models are increasingly able to detect when they're being tested.

But consider: **this paper exists because Anthropic researched and published work undermining confidence in its own product.** Name another industry where a company publishes research showing its own system is strategically deceptive. That is evidence of a safety culture worth reinforcing from inside.

---

## 4 — The Game Theory Trap: Why Unilateral Restraint Fails

This is where my path becomes clearest.

The geopolitical landscape creates a tragic structure:

- **Any nation that achieves AGI/ASI first** gains an asymmetric advantage so large it could be civilizationally decisive.
- **Every nation must participate** because opting out doesn't remove the risk — it only guarantees you lose.
- **Every nation is incentivized to cut safety corners** to move faster.
- **A single failure by the leader** could be catastrophic for *everyone*, including nations that weren't competing.

This is a textbook coordination failure — identical in structure to nuclear arms races, but with higher stakes and fewer existing treaties.

The Paris AI Action Summit (February 2025) illustrated the tension well: it pivoted from safety to innovation, with the US and UK declining to sign a 60-nation governance statement. It's genuinely sad that the summit didn't include the permanent loss of human agency as a discussion topic — it should have been part of the conversation alongside innovation. That said, I think it was great that the summit showcased what this technology makes possible. Both could have co-existed. The fact that they didn't is itself evidence of how hard coordination is. The Trump administration revoked Biden's AI Executive Order on day one. California's SB 1047 was vetoed.

Unilateral restraint doesn't work. International coordination does — but only if you have the **technical tools to make agreements verifiable**.

---

## 5 — The Work That Convinced Me: ZKP-Based Verification of Training Runs

Pierre Peigne and the GPAI Policy Lab have been working on something I believe is among the highest-leverage interventions in AI governance: **Zero-Knowledge Proof systems that allow nations to verify compliance with capability thresholds *without* revealing proprietary research.**

The logic is compelling. This transforms the game theory:

- **Without ZKP verification:** Prisoner's dilemma. Everyone defects because they can't trust others to cooperate.
- **With ZKP verification:** Verifiable commitment game. Everyone can cooperate because compliance is provable.

The current bottleneck is that ZKP implementations work for inference but do not yet scale to frontier training runs. Bridging that gap requires people who understand large-scale training infrastructure from the inside — distributed GPU systems, billion-scale pipelines, the practical reality of what a training run looks like. That is exactly my background.

Pierre co-authored the Singapore Consensus on Global AI Safety Research Priorities alongside Yoshua Bengio and Stuart Russell. He understands both the policy need and the technical requirements. When I look at this work, I see where my ML engineering skills become directly useful for safety — not in the abstract, but in the concrete task of making ZKP verification work on real, state-of-the-art training runs.

I'm deeply convinced this work matters. I didn't come up with the approach — I recognized its importance and want to contribute the engineering skills needed to make it real.

---

## 6 — An Ode to What This Technology Makes Possible

I want to say something that might sound contradictory to everything above, but isn't: **I think we live in the most extraordinary technological moment in human history, and I find it magnificent.**

Today's AI capabilities — the ones that already exist, the ones outside the scope of what we want to limit — are formidable tools for humanity. Claude Code is a perfect example: a tool that gives individual developers the leverage of entire teams, that democratizes technical capability, that allows someone with an idea to build it in hours rather than months. It is not a step toward uncontrolled superintelligence. It is a tool, used by humans, amplifying human intent.

The value waiting to be unlocked — in healthcare, education, scientific research, creative expression, accessibility — is staggering. The technologies we have *right now* can drive extraordinary value for billions of people.

And that is precisely why the control problem matters so much. We cannot extract these benefits if we lose control of the trajectory. You can't profit from health for all if there's no one left. Pierre's framing is exactly right: we agree this technology can have an immense positive weight on the world. To extract those benefits, we must prevent the catastrophic risks.

The two positions — "this technology is magnificent" and "we must ensure it remains under human control" — are not in tension. They are the same position, stated from two directions.

---

## 7 — Why Me, Why There, Why Now

My alternative to working on safety coordination is to go work at a frontier lab directly, putting these technologies in service of end value for humanity. That path excites me. I'm genuinely motivated to build with these tools.

But having Pierre in this field — someone I trust deeply, whose intellectual rigor I've witnessed firsthand through years of shared work at 42AI — changes what's possible. Beyond Pierre, I'm drawn to working alongside bright minds who are genuinely aligned with humanity's best interest. The people working on AI governance and verification are some of the most thoughtful, technically capable individuals I've encountered. The opportunity to contribute alongside them is rare.

His work on safety, my engineering background at the frontier — we're complementary. My going in doesn't betray the safety mission. It extends it by bringing the hands-on training infrastructure expertise that verification research needs.

And yes: I'm excited to work at the edge of what's technically possible. I won't pretend otherwise. But that motivation and the safety mission aren't in conflict. The people most motivated to understand these systems deeply are exactly who you want working on making them safe.

**My concrete commitment:** if I find myself in a position where safety is being systematically deprioritized and I have no leverage to change it, I leave. I'm not going in blind.

---

## 8 — Where the Field Stands: Why Urgency, Not Despair

The alignment problem remains unsolved, and the gap between safety progress and capability advancement continues to widen. But the field has come remarkably far:

- **Mechanistic interpretability** went from theoretical curiosity to production tools — circuit tracing now reveals complete computational pathways.
- **Alignment faking** was detected empirically, turning a theoretical concern into a measurable phenomenon.
- **Evaluation science** professionalized — the UK AI Security Institute has tested 30+ frontier models; METR's time-horizon metric shows agent capabilities doubling every ~7 months.
- **The AI control agenda** (Redwood Research) assumes alignment might fail and engineers structural safeguards — a pragmatic bridge between pessimism and practical necessity.

The biggest open problems remain daunting: scalable oversight of superhuman systems, reliable detection of alignment faking, ensuring chain-of-thought faithfulness, maintaining evaluation integrity, and establishing binding international governance frameworks. The emerging "alignment trilemma" — the apparent impossibility of simultaneously guaranteeing strong optimization, perfect value capture, and robust generalization — looms large.

These are reasons for urgency. Not for despair. And not for standing on the sidelines.

---

## 9 — Summary

| Their argument | My response |
|---|---|
| Labs race on capabilities | Not every role is capabilities. Safety roles exist at frontier labs and need reinforcement. |
| Safety people inside are unhappy | True at OpenAI. Leike left — and went to Anthropic, where he produced the alignment faking paper. |
| Even Anthropic is insufficient | Insufficient ≠ useless. Their alternative path outside labs is worth exploring — and reinforcing the best internal effort is too. |
| Cultural change from inside is impossible | You don't need to change culture to produce safety artifacts. The work speaks for itself. |
| Alignment faking undermines trust | The fact that Anthropic published this against its own commercial interest is evidence of safety culture worth joining. |

**My path:** Join Pierre and the GPAI Policy Lab to apply ZKP-based verification to state-of-the-art AI training runs — bringing the frontier ML engineering expertise needed to transform the AI race from a prisoner's dilemma into a verifiable coordination game.

**My motivation:** This technology is extraordinary. The value it can create for humanity is immense. That is exactly why ensuring we maintain control over its trajectory is the most important technical problem of our time.

---

*"The organizations and individuals working on alignment represent humanity's best effort to solve what may be the most consequential technical problem in history — and they are working with a timeline not of their choosing."*

I choose to work alongside them.
