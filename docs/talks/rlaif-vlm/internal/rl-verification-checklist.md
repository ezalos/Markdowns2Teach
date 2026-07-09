# Verifying DPO / RL preference-training correctness

Prioritized checks to prove the training loop is bug-free (most valuable first). Those marked ✅ are
implemented in `src/verify_wiring.py` (`make verify`). Sources at the bottom.

## DPO / preference (ranked first — this is what we run)

1. ✅ **Step-0 loss == ln2 ≈ 0.6931.** At init the adapter is a no-op so policy==ref, margin=0,
   loss=−log0.5. Checks the *entire* wiring (β applied, log-ratios subtract, no sign flip). If it's not
   ~0.693, the reference or loss is miswired. `assert abs(loss0 − ln2) < 1e-2`.
2. ✅ **Reference identity: margin==0 at step 0** (dropout off). Catches the wrong-reference bug
   (base used when you meant the SFT/adapter checkpoint). With `ref_model=None`+PEFT the ref is the
   adapter-disabled policy — verify `logps(policy)==logps(ref)` before any step.
3. ✅ **Overfit 2 memorized pairs:** accuracies→1.0, margins↑ monotonically, loss→~0. DPO analogue of
   the supervised overfit test. Expect `rewards/rejected` to go **negative** more than `rewards/chosen`
   rises. Needs `lora_dropout=0` + constant LR.
4. ✅ **Params change, and ONLY trainable ones** (VLM-critical): LoRA params trainable & get grads;
   the vision tower stays **bit-identical / 0 trainable**. NB: freezing base vision weights is not
   enough — LoRA `target_modules=[q/k/v/o_proj]` also matches vision attention, so add
   `exclude_modules=".*vision.*"`. (This repo hit exactly this; `make verify` caught it.)
5. ✅ **NaN/Inf guard + grad-norm sanity.** `loss`/`grad_norm` finite every step; alarm if `grad_norm`
   ≫ rolling median. VLM `max_length` truncation of image tokens often surfaces as NaN → keep `max_length=None`.
6. **precompute_ref_log_probs consistency.** Cached ref logps == on-the-fly (within 1e-4). Incompatible
   with liger/sync_ref_model/IterableDataset.
7. **Healthy-run trajectory:** margins↑; accuracies↑→~1; `rewards/rejected`↓; both logps drift down (gap
   matters). ALARM: both `rewards/chosen`&`rewards/rejected` crater together w/ flat margin = reward
   collapse / fluency loss; accuracies stuck ~0.5 & loss flat 0.693 = nothing trains.
8. **Loss-goes-down-on-one-batch** (seconds-fast smoke). 9. **Gradient checking** (`torch.autograd.gradcheck`,
   float64 tiny model) if you customized the loss/collator. 10. **Seed determinism**: same seed → identical
   step-0 loss & first-N grad_norm (TRL ships an opt-in `pytest -m invariant` snapshot suite — mirror it).

## RLHF / PPO / GRPO (if we move past offline DPO)

11. **KL-to-reference bounded & ≥0** (Schulman k3 estimator is always ≥0). Unbounded KL + rising reward
    = reward hacking. 12. **"Reward up but samples worse"**: hold out a gold metric; gold reward rises then
    *falls* vs KL (Gao et al.) → early-stop on decline. 13. **Completion-length collapse / reward-dist
    monitoring**: `completions/mean_length` stable; `frac_reward_zero_std`↛1; `reward_std`↛0.
    14. **Per-reward-component logging** + advantages ≈ mean-0 bounded; watch premature entropy collapse.
    15. **Reward-model unit tests**: known-ordering pairs `r(good)>r(bad)`, monotonicity, invariance,
    calibration (a ~55%-accurate proxy is trivially hacked). 16. **PPO pairing/reset correctness** on probe envs.

## Add to a TRL DPO repo right now
Step-0 loss assert · reference-identity assert · frozen-vs-trainable grad assert (+ `exclude_modules`
for VLM) · param-update check · NaN/grad-spike callback · overfit-2-pairs regression test · margin-
monotonicity + collapse alarm · `assert max_length is None`. (First 5 + overfit are in `make verify`.)

## Sources
TRL DPO docs https://huggingface.co/docs/trl/dpo_trainer · GRPO docs https://huggingface.co/docs/trl/main/grpo_trainer ·
TRL issues #1340/#1365 (ref w/ PEFT), #1843 (margins not changing) · Andy Jones "Debugging RL"
https://andyljones.com/posts/rl-debugging.html · Schulman "Nuts & Bolts" http://joschu.net/docs/nuts-and-bolts.pdf ·
KL approx http://joschu.net/blog/kl-approx.html · Karpathy "Recipe" https://karpathy.github.io/2019/04/25/recipe/ ·
Lilian Weng "Reward Hacking" https://lilianweng.github.io/posts/2024-11-28-reward-hacking/ ·
Gao et al. 2022 (RM overoptimization) https://arxiv.org/abs/2210.10760 · DPO paper https://arxiv.org/abs/2305.18290
