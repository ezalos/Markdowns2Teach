# Teaching an AI to stop making things up — with another AI as the teacher

*The story of a 2-day hackathon: RLAIF on a vision-language model, one GPU, an autonomous research loop,
and $0 of API budget. Written for a non-data-scientist audience. (The technical companion is
[`PRESENTATION.md`](PRESENTATION.md); every number here is traceable to a committed experiment.)*

---

## 1. The problem: AI that confidently invents things

Vision-language models (VLMs) — AIs that look at an image and talk about it — have a famous flaw:
**hallucination**. Ask one to describe a photo and it may mention a dog that isn't there, or "people in
suits" in an empty street. It doesn't lie hesitantly; it lies fluently. For any real application, this is
the #1 trust problem.

**Our goal:** take a small open-source VLM (3 billion parameters — small enough to train on one gaming-class
GPU) and make it measurably more *faithful to the image*.

## 2. The ambitious part: no humans in the labeling loop

The classic recipe for aligning models (RLHF) needs **humans** to grade thousands of model answers —
expensive and slow. The ambitious alternative is **RLAIF: Reinforcement Learning from AI Feedback** —
replace the human graders with *another AI*.

There are two levels of difficulty here, and we did both:

- **Offline RLAIF (the ladder's first rung).** Use an existing dataset (RLAIF-V: 83,000 examples, each an
  *image + question + two candidate answers*, where an AI labeling pipeline marked which answer is more
  faithful). Train our model to prefer the faithful answers, using DPO — a technique that gets the effect
  of reinforcement learning through a direct, stable training objective.
- **Closed-loop RLAIF (the rung that earns the name).** No dataset at all: **our own model writes the
  answers**, a *judge AI* (a free vision model) compares them, and we retrain on the judge's verdicts.
  The model improves by studying critiques of its own work. This is the loop everyone wants — and it's
  where the interesting failure modes live (see §6).

Why it's complex: the feedback signal is only as good as the AI judge; the training can silently learn the
judge's *quirks* instead of the truth; and nothing tells you it went wrong unless you build the
measurement tools yourself. All of this on a single RTX-3090 in 48 hours, with the judge on a free API tier.

## 3. What "did it work" means — the scoreboard

Our main scoreboard is **held-out preference accuracy**: show the trained model *pairs it never saw* —
one faithful answer, one hallucinated — and check whether it now ranks the faithful one higher.

- A model that learned nothing scores **50%** — a coin flip.
- Our starting recipes scored **53-58%** — barely above the coin.
- The final model scores **72.3%** on a verified-clean test set.

In parallel, the closed loop is scored by **win-rate**: a judge AI blind-compares the tuned model's answers
against the original model's answers on fresh images (in shuffled order, so it can't cheat by position).
50% = no difference.

## 4. The autoresearch loop — how the work actually happened

This project was as much about *how* to run AI research autonomously as about the model. The workflow had
a human (Louis) setting direction and quality bars, and an AI agent (Claude) executing research
around the clock. The arc:

**Kickoff — research before code.** The agent ran parallel deep-research on the training stack, the
dataset's format traps, and the observability tooling *before writing a line*, producing a phased design
doc with a "definition of done" per phase.

**Foundation — baseline + eval + report, wired from day 0.** First deliverable was not a model but a
*harness*: one-command remote training, live dashboards, every experiment writing its own metrics and
figures, and a report generator. Rule: no experiment without a measurement.

**The human quality gates.** At several points Louis stopped the loop and demanded sanity checks — and
each one paid off:
- *"Prove the training is bug-free"* → the **overfit test**: force the model to memorize just 2 examples.
  The training loss must start at exactly ln 2 = 0.693 (a mathematical fingerprint that the setup is
  wired right) and fall to ~0. It did — and the check *also* caught a real bug (part of the model that
  was supposed to be frozen was silently training).
- *"Your status updates must interpret the science, not just say the servers are up"* → every automated
  check-in thereafter included a learning-signal diagnosis, with comparisons to previous runs at the
  same stage.
- *"With a tight compute deadline, kill unproductive runs early"* → every run got **pre-registered
  kill-rules** (written down *before* seeing the results) and shipped its *best* checkpoint, not its last.

**Full autonomy — the goal/loop machinery.** For the final 20 hours the agent ran unattended: a watchdog
fired every ~19 minutes (infrastructure check + science read + comparison to baselines), targeted wake-ups
were timed to each experiment's decision points, crashed processes were diagnosed and relaunched, and a
chain of experiments (train → evaluate → decide → scale up → overnight run → morning evaluation) executed
itself end-to-end, committing results and updating the report as it went.

**Self-correction — the part worth showcasing.** The autonomous loop caught **three measurement bugs in
its own work**, each of which would have produced a false result:
1. *The moving exam* — different experiments were being graded on different test questions (the
   "eval-slice confound"); fixed by pinning one shared test set.
2. *The unreliable judge* — asking the judge the same question with answers in swapped order flipped its
   verdict **20% of the time**; measured, then mitigated with a 3-vote majority protocol.
3. *The contaminated exam* — the overnight model scored an impossibly-good 0.887 on the shared test set…
   because that test set had ended up inside its (larger) training data. Caught within minutes *because
   the number was too good*, and re-graded on a guaranteed-untouched set.

An unexpected scientific bonus: all three scaled training runs stayed flat and then *jumped* in performance
at the same relative point of training (~60-75% through the dataset). Naive early stopping would have
killed the best runs right before their jump; the pre-registered, epoch-aware rules kept them alive.

## 5. The results

| What | Number | In plain terms |
|---|---|---|
| Starting point | 53-58% | Barely better than a coin flip at telling faithful from hallucinated |
| After the day-2 recipe fix (better adapter, schedule, 8k examples) | 64% | Real learning, verified honest |
| Scaling data 16k → 24k overnight | 70-71% on their own tests | Each scale-up helped |
| **Final model, verified-clean test** | **72.3%** (vs 65.6% for the runner-up) | The overnight model wins a fair head-to-head |
| Closed loop, round 1 | 56% win-rate | The self-improvement loop works, modestly |
| Closed loop, round 2 (iterating) | 37.5% — *worse than base* | Over-optimizing a noisy judge backfires (a known theoretical failure, demonstrated live) |
| Closed loop with de-noised labels (3-vote judge) | 58.3% | Cleaning the feedback helps; the judge's quality is the ceiling |
| Cost of all AI feedback | **$0** | Free-tier judge, budget-guarded by design |

One more result hiding in that table: **108 carefully de-noised preferences from the model's own outputs
taught it about as much as 3,000 noisy dataset examples** — feedback *quality* competes with quantity.

## 6. What we learned (the honest version)

1. **The method works end-to-end on tiny hardware.** A 3B model went from coin-flip to 72% at
   discriminating faithful answers, trained on one GPU with AI-only feedback.
2. **In closed-loop RLAIF, the judge is the bottleneck.** A noisy free judge caps the gain (56-58%), and
   *iterating* against it actively harms the model — we measured the noise (20%), demonstrated the failure,
   and showed the mitigation (majority voting). Upgrade path: a stronger judge, then true online RL.
3. **Autonomous research needs its own immune system.** The most valuable agent behaviors were not
   training tricks but *self-auditing*: pinned test sets, pre-registered kill-rules, suspicion of
   too-good numbers. Every wrong number in this project was caught by an instrument the loop built itself.
4. **Human checkpoints multiplied the autonomy.** The handful of human interventions — demand the overfit
   proof, demand science in the status reports, demand early-stopping discipline — are what made 20 hours
   of unsupervised execution trustworthy.

## 7. Glossary (for the slides)

- **VLM** — an AI that takes images + text in, and writes text out.
- **Hallucination** — the model describing things that aren't in the image.
- **RLAIF** — aligning a model using *AI* graders instead of human graders.
- **DPO** — the training method: show pairs (better/worse answer), directly shift the model toward the
  better ones; mathematically equivalent in objective to the RL approach, but simpler and more stable.
- **Judge** — a separate AI that compares two answers to the same image and picks the more faithful one.
- **Held-out / clean** — test examples the model never trained on ("clean" = verified untouched by *any*
  of our trainings).
- **Slice** — a contiguous chunk of the dataset used as a training or test set.
- **Preference accuracy** — % of unseen answer-pairs the model ranks correctly (coin flip = 50%).
- **Win-rate** — % of fresh prompts where the judge prefers the tuned model over the original.
- **Checkpoint** — a saved snapshot of the model during training; we always ship the *best* one, not the last.
- **Kill-rule / gate** — a pre-written condition ("if the score at step X is below Y, stop the run") that
  prevents wasting compute — decided *before* seeing the data, so we can't fool ourselves.
