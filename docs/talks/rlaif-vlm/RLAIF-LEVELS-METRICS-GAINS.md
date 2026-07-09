# RLAIF levels · metrics · gain attribution
*Companion doc for the deck — the three questions Louis asked, with every number sourced to `results/` or `internal/todo.md`.*

---

## 1. The three levels of RLAIF — what we did and didn't

| level | what it means | did we? |
|---|---|---|
| **1. Offline RLAIF** | Train on an existing preference dataset whose labels were produced *by an AI* (not humans). The feedback is AI-made, but it's about *other models'* answers, and the "RL" is done by DPO — a direct training objective mathematically equivalent to the RL goal, with no live loop. | ✅ **Yes — this produced the headline model** (0.723). All the scaled runs (8k/16k/24k on RLAIF-V) are this level. |
| **2. Closed-loop RLAIF** | No dataset: **our own model writes answers**, a separate AI judge compares them, we retrain on the judge's verdicts, and can iterate. The feedback is about *the policy's own behavior* — this is the level that really earns the name. | ✅ **Yes — three rounds** ($0, free judge): 56% win-rate → 37.5% (iterating over-optimizes the noisy judge) → 58.3% (3-vote de-noised labels). Modest gains, big lessons: judge quality is the ceiling. |
| **3. Online RL** | True reinforcement learning (PPO/GRPO): the model generates *during training*, an explicit reward scores every rollout live, policy gradients update the model continuously. | ❌ **No — deliberately.** It needs fast rollout infrastructure (vLLM) and, critically, a much less noisy reward: we *measured* our judge flipping 20% of its verdicts under an answer-order swap, and level-2 round-2 empirically showed what optimizing against that noise does (37.5%). Doing level 3 with this judge would reward-hack from step one. It's the documented next step, not an oversight. |

One-liner for the deck: *"We did levels 1 and 2 of 3 — and level 2's failure mode is exactly the measured reason we didn't attempt level 3."*

---

## 2. The metrics — what they mean, and what we actually optimized

**What the training optimizes (the loss).** DPO loss = −log σ(β·(margin)), where the *margin* is how much more the model prefers the chosen answer over the rejected one, relative to its own starting point (the frozen reference). Training pushes margins up on training pairs. Key calibration facts: the loss starts at exactly **ln 2 ≈ 0.693** when the model hasn't moved (that's the fingerprint the overfit test checks), and a *training* loss near 0 means memorization, > 1 means divergence.

**What we monitored and selected checkpoints on (the scoreboard metric): held-out preference accuracy.**
Take pairs the model **never trained on**; for each, check whether the model now ranks the faithful answer above the hallucinated one (margin > 0). Report the fraction ranked correctly.
- **Chance = 50%** (a model that learned nothing ranks like a coin flip).
- Error bar at n=256: about **±3 points** — differences smaller than that are noise.
- This is *measured, never optimized directly* — the model never sees these pairs. That's what makes it evidence of generalization rather than memorization.
- Its known pitfall (which bit us twice): the number is only comparable across models **if they're graded on the same held-out set** ("the moving exam"), and only meaningful **if that set is outside everyone's training data** ("the contaminated exam", the 0.887 → 0.723 story).

**The external metric (closed loop): judge win-rate.** A separate free VLM blind-compares tuned-vs-base answers on fresh prompts (randomized order). 50% = indistinguishable; ±7 points of noise at n=48. This measures *behavior*, not ranking — but inherits the judge's own 20% noise.

**So: what were we optimizing for?** The DPO loss on training pairs — nothing else. Accuracy and win-rate are *thermometers*, not targets. The one place a thermometer became a target is exactly where things broke: closed-loop round 2 effectively optimized toward the judge's (noisy) opinions, and true quality fell. That's the cleanest illustration in the whole project of why you keep optimization targets and evaluation metrics separate.

---

## 3. Slide 06 — the two missing intervention prompts (real quotes)

**A. The parallel-compute demand** (2026-07-01, verbatim): *"It would be interesting to bump the number of xp we run in parallel to better use our compute."*
→ Result: the agent found that a batch-8 trial needs ~19 GB but micro-batch 2 × gradient-accumulation 4 gives the *identical* gradient at ~6 GB — so **3 experiments ran concurrently** on the small model; GPU utilization went **40% → 98%**.
Slide-ready copy: **"Use the whole GPU — run experiments in parallel."** → a memory trick (same math, ⅓ the footprint) put 3 trials on one card; utilization 40→98%.
*(Honest speaker note: this was the small-model phase; the 3B runs don't fit two-at-once — the agent learned that limit by OOM-ing and wrote it into its rules.)*

**B. Candidates for the second blank — all real, pick one:**
1. **The budget constraint** (verbatim: *"OR key has limited budget, be careful"* / *"If run out of credit use some free model — look for which ones have the modality vision activated"*) → the agent found a free-tier vision judge, added hard call-caps and idempotent caching → **the entire AI-feedback loop cost $0.00**. *(Strong for this audience — it explains the $0 on the cost slide.)*
2. **The relative-comparison demand** (verbatim: *"how does it compare to previous runs at similar stages? This should always be a relative comparison as well"*) → every status report gained a baseline table comparing runs at matched training progress — which later powered the "flat phase → held, not killed" call at 2am.
3. **The validate-at-length demand** (verbatim: *"we should validate this run with a longer running one"*) → caught a learning rate that looked fine in short sweeps but diverged over longer runs — "short sweeps hide late-onset divergence."

Recommendation: **A + B1** (parallel + budget) — they're the most concrete for non-data-scientists and B1 pays off the "$0" stat. B2 fits better as a speaker note under the existing "reports must interpret the science" gate.

---

## 4. Slide 10 (scoreboard) — decomposing "+7 recipe + data 8k→16k→24k"

The honest answer first: **the recipe components can't be fully separated** — under deadline, r32+MLP, cosine schedule, lr 1e-4 and the 2k→8k data jump shipped *together* in one run (a deliberate speed-over-attribution tradeoff; the original plan's "one axis at a time" rule was consciously broken on day 2). What *is* measured, on shared test sets:

| step | what changed | measured gain | source & caveat |
|---|---|---|---|
| old recipe → phase3 | **recipe overhaul (LoRA r32+MLP + cosine + lr 1e-4) AND data ×4 (2k→8k), bundled** | **+7.8 pts** (0.531 → 0.609) | same test set @20000; > 2σ — real. Per-component split *not measured*. |
| 8k → 16k | data ×2 (also steps ×1.5) | **+0.8 pts** (0.609 → 0.617) — *within the ±3 noise band* — but the preference **margin grew +43%** (0.32 → 0.46) and the own-curve best went 0.643 → 0.701 | same test set @20000. Accuracy ~flat, confidence up: the model ranks the same pairs right but far more decisively. |
| 16k → 24k | data ×1.5 AND a full epoch (steps ×2), bundled | **+6.7 pts** (0.656 → 0.723) | clean set @25000 (the only set valid for the 24k model); > 2σ — real. Data-vs-steps split *not measured*. |

Suggested slide phrasing (accurate without over-claiming):
> **+8** recipe overhaul + 4× data (bundled) · **+1** data ×2 (ranking flat, confidence +43%) · **+7** data ×3 + full epoch
> *speaker note: components inside each step shipped together — attributing them individually would have cost runs we spent on scale instead.*

And if someone asks "why isn't data monotone?" — the earlier steps were also graded on an easier/different mix before the shared-test-set discipline existed; the two > 2σ deltas above are the ones measured under it.
