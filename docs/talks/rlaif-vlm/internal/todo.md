# FINAL DAY plan — 2026-07-02 (DEADLINE EXTENDED: ends 2026-07-03 10:00)

## Extended-budget schedule
- now-19:50: qwen3b-final-16k (gates at 500/750/1000/1250; kill rules below).
- ~20:00-22:30 evening evals: desc-hal (base/phase3/16k) + consensus retrain + winrate + eval_pref fixed-slice suite.
- FINAL: clean head-to-head @25000: **24k ckpt-2500 = 0.7227** (+0.62 margin) vs 16k ckpt-1000 = 0.6562. 24k = final model.
- desc-hal v2 (fixed grouping): coverage 0.323->0.364 (+4pt), absent-mentions at floor both (1-2/174).
- CONTAMINATION CAUGHT: overnight@20000 = 0.887 is memorization (24k train includes rows 20000-20256).
  Own-slice 0.709 valid. Clean head-to-head 16k vs 24k running @25000 (tmux morning2).
- OVERNIGHT (real clock): evening chain armed in tmux 'evening' (waits for 16k ~18:20 -> desc-hal x2 -> consensus retrain+winrate -> eval_pref suite -> launches qwen3b-overnight-24k 24k/3000 full epoch ~21:30, training ~23:30->07:20).
- 08:00-10:00: eval_pref + desc-hal on overnight best checkpoint, final figures, deck polish, done by 10:00.

Louis's directive: the models must actually WORK (passable results), not just run. Free to launch xps,
tweak, test. Keep writing findings + plots to the report.

## Diagnosis (why results were weak)
1. 3B undertrained: 2k pairs / 400 steps / LoRA r=16 attention-only = ~1.5 passes over a tiny slice.
2. NO external hallucination eval existed (HalProxyStub logs generation LENGTH). No "it works" proof.
3. RLAIF capped by free-judge noise (56% r1 / 37.5% r2).

## Live readings (phase3, slice 8000-8511)
- step 250: acc 0.580, eval_loss 0.732 | step 500: acc 0.582, el 0.670 | **step 750: acc 0.639, el 0.646 — broke upward**.
  Best-run-yet at matched freshness (old recipes needed epoch>1 + repeats to reach 0.61-0.65; phase3 at epoch 0.75, fresh data, still climbing).
- Read: margins grow on already-correct pairs; ranking acc likely plateaus ~0.6 on noisy AI labels across ALL configs.
  POPE (behavioral) is the real decision metric for the 16k launch.

## Reference baselines @ matched stage (for relative science reads; match on EPOCH not step)
| run | step | epoch | loss | acc | margin | logp_c |
|---|---|---|---|---|---|---|
| fullres-old (3k,r16,3e-4) | 250 | 0.67 | 0.676 | 0.625 | 0.31 | -105 |
| phase3 (8k,r32+MLP,1e-4cos) | ~630 | 0.63 | 0.57 | 0.75 | 0.75 | -110 |
| night-lr-1e-4 (2k,r16) | 250 | 1.00 | 0.563 | 0.717 | 0.45 | -97 |
| fullres-old | 500 | 1.07 | 0.859(!) | 0.825* | 1.87* | -142(!) |
(*=inflated by repeated data; (!)=over-optimization signature under constant 3e-4)
-> phase3 recipe leads on every train metric at equal freshness; eval comparison pending fixed-slice rescore.

## EARLY-STOP GATES for qwen3b-final-16k (enforce at every watchdog firing; GPU-hours > completeness)
- Checkpoints+evals every 250 steps -> final model = BEST checkpoint by eval acc, not last.
- KILL if: eval@500 <= 0.582 (phase3's @500; identical recipe + more data must not be worse), OR
  eval flat/down across two consecutive gates after 750 (< +0.5pt cumulative), OR any divergence sign
  (train loss > 1, grad spikes, logps/chosen < -250).
- CONTINGENCY: if POPE(phase3) reads NEGATIVE (tuned < base), tighten the 16k gate-500 bar to
  'clearly above 0.60' — no point scaling a recipe that doesn't transfer to behavior; pivot to rpo_alpha.
- On kill: keep best checkpoint, fetch it, jump immediately to the improvement queue
  (consensus retrain -> winrate; eval_pref suite; rpo_alpha run if >=3h GPU left).

## 16k live gates (evals DON'T print to pane this run — read checkpoint-*/trainer_state.json)
- gate-250: acc 0.574, el 0.700, margin +0.18 (epoch .125 — matches phase3@250 at HALF the epoch; on pace).
- gate-500 PASSED: **0.631** (el 0.656, margin +0.33) at epoch 0.25.
- gate-750: 0.623 (el 0.630 falling, margin +0.53 climbing) — flat-phase, epoch .375; phase3 was also flat in this epoch band before its .6-.75 upturn.
- GATE AMENDMENT (pre-registered 16:40, BEFORE gate-1000 exists): original rule was step-matched, contradicting our epoch-matched discipline.
  New rule: gate-1000 (epoch .5) kills only on divergence or acc<0.60 (real regression); flat-but-healthy continues.
  gate-1250 (epoch .625, the upturn window): kill if no new high >0.636. Rationale: phase3's own trajectory shows the
  inflection at epoch .6-.75; killing at epoch .5 would preempt the region the run exists to reach.
- **GATE-1000: acc 0.7012** (el 0.589, margin +0.67) — upturn landed in predicted window; BEST RESULT of project.
- gate-1250: 0.693 (noise-level dip, margin +0.685 climbing) — holding ~0.70 plateau. Run ends ~18:40 -> evening chain.

## Evening chain results (live)
- desc-hal FLOOR EFFECT (honest finding): base already ~0 hallucination on single-object 128-tok descriptions
  (phase3: 0.008->0.0; 16k: 0.008->0.008). Instrument limitation, not a training failure; full-CHAIR out of scope.
- consensus retrain: 36 steps, margin 5.8; held-out-16 acc 0.44 (n tiny).
- **CONSENSUS WIN-RATE: 28/48 = 58.3%** (vs 56% single-vote r1, 37.5% r2). De-noising labels lifts modestly ->
  judge noise confirmed as bottleneck; ceiling is the judge itself. RLAIF arc: 56 -> 37.5 (iterate) -> 58.3 (de-noise).
- **FIXED-SLICE TABLE (@20000, n=256)**: 16k-ckpt1000 0.617 (+0.46 margin) > phase3 0.609 (+0.32) > consensus-RLAIF 0.570 (+0.20, from just 108 on-policy prefs!) > old recipe 0.531 (+0.26).
  Recipe fix = real +8pt (>2sigma); own-slice numbers ran hot (0.70 had slice tailwind); label quality competes with quantity.
- round1 fixed-slice 0.590 — both on-policy RLAIF adapters (~100 prefs) land 0.57-0.59, near phase3 (0.61) with 80x less data.
- OVERNIGHT qwen3b-overnight-24k LAUNCHED ~21:35; gates: 0.568/0.602/0.631/0.6445/0.639/0.633 then **0.676@1750
  — upturn landed in phase3 epoch band (0.58)**; then 0.658@2000, **0.6934@2250 (new overnight best, el 0.598)** — then **0.709@2500 = NEW PROJECT RECORD** (el 0.596, margin +0.71), still climbing; gates 2750/3000 next.

## Today's queue
- [x] `qwen3b-phase3-8k` DONE: eval acc 0.580->0.582->0.639->**0.643@1000** (climbed to the end, epoch 1.0,
  fresh data, zero over-optimization). Best eval-side run (its slice). ~13:25.
- [~] POPE(phase3) running ~14:30->15:15 (was blocked 45min by tmux-client pgrep ghost-match — fixed+committed).
- [~] 16k auto-chain armed (tmux 'chain'): launches configs/final_qwen3b.yaml when POPE exits; gates active.
- [x] Built `src/eval_pope.py` — POPE benchmark, paired base-vs-adapter (acc/F1/yes-rate/McNemar) + tests.
- [x] Consensus judge DONE: of 99 pairs judged 3x with A/B order swaps, **20% had no stable majority** -> direct
  measurement of free-judge noise. 108 consensus-filtered prefs ready (vs 105 single-vote).
- [x] POPE(phase3) DONE: base 0.8667 -> tuned 0.8683; adversarial EQUAL 0.835; paired disagreements 7/600 (4v3).
  FINDING: binary object-QA is behaviorally unmoved — base already aligned (0.867) + RLAIF-V trains long-form
  faithfulness, not yes/no. METRIC MISMATCH -> built eval_hal_desc.py (description-level, CHAIR-style on POPE labels).
- [ ] POPE on the old fullres adapter too (was the old recipe helping at all?).
- [ ] Consensus retrain + eval if time.
- [ ] Plots + report updates THROUGHOUT (deck slide: "Day 2 — making it actually work").

# ---- previous night plan (done) ----
Goal (Louis, /goal): run experiments, keep smic's GPU busy, improve, log results + plots, iterate.
North star = DESIGN.md. We are on **Phase 4b: closed-loop RLAIF**.

## GPU queue (keep it busy the whole time)
- [~] RUNNING: overnight `night-fullres-3e4` (full-res 3B, 800 steps) — let it finish.
- [ ] RLAIF loop on Qwen-3B (generate → judge(free VLM) → retrain → win-rate eval).
- [ ] Redo the OOM'd 3B exps at concurrency **2** (LR 1e-3/3e-3, data 5k/10k) to complete the sweep.
- [ ] RLAIF round 2 (iterate) / stretch experiments to fill remaining compute.

## Build (CPU, while GPU busy)
- [ ] RLAIF components (TDD pure parts first):
  - [ ] `src/rlaif_judge.py` — OpenRouter free VLM judge (parser, randomize, budget guards, cost log).
  - [ ] `src/rlaif_generate.py` — Qwen-3B K=2 sampled candidates.
  - [ ] `data/build_dataset.py::load_local_preferences` + train_dpo local-dataset path.
  - [ ] `src/rlaif_eval.py` — judge win-rate (RLAIF'd vs base).
  - [ ] `scripts/rlaif_loop.sh` + `make rlaif`; inject OPENROUTER_API_KEY to smic.
- [ ] Unit tests for parser / preference builder / local loader / cost cap.

## Log + plots (continuous)
- [ ] Fetch overnight; plot 3B LR comparison + fullres curves/probes; update `report/PRESENTATION.md`.
- [ ] RLAIF: preferences stats, win-rate plot, base-vs-RLAIF probe table.
- [ ] Keep `tasks/lessons.md` updated with gotchas.

## Guardrails
- Judge = FREE OpenRouter vision model (`nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`) → $0 cost.
  Never touch the paid budget unattended.
- 3B concurrency = 2 max (a trial is ~11GB; 3 OOMs — lesson from the overnight batch).
- Every experiment: own run dir + Trackio + committed results. Never `git add -A`.

## Results log (append as we go)
- 3B DPO (400 steps, 2k, trimmed res): eval acc **0.652** (lr 1e-4), **0.617** (lr 3e-4) — vs 500M 0.578, chance 0.5.
- **RLAIF round 1 DONE (22:20):** Qwen-3B -> 64 gens -> free VLM judge -> **57 prefs ($0)** -> DPO -> **eval acc 0.625**.
  Judge picks sensibly (less-hallucinated/cautious). The honest closed-loop RLAIF works end-to-end.
- **RLAIF WIN-RATE (honest): 27/48 = 56% (+/-7%)** on the SCALED round (128 gens -> 105 prefs -> DPO, 48-prompt eval).
  Above chance but within noise. (The first 24-prompt read of 71% was small-sample optimism.) Loop PROVEN; effect modest at 1 round.
- **RLAIF round 2 (on-policy iteration): 18/48 = 37.5%** vs base -> ITERATION HURT (over-optimized the noisy free judge).
  Honest finding: the loop works, but judge quality is the bottleneck. Round 1 helps modestly, round 2 degrades.
- Full-res 3B headline DONE: train margin 2.68, acc 0.875, loss 0.69->0.30 (strongest DPO signal); gen-len 68->106. Figure in deck.

## SESSION SUMMARY (for Louis) — full RL/RLAIF arc, all committed; deck = report/PRESENTATION.md (14 slides)

| Phase | Result |
|---|---|
| Harness | one-command deploy/monitor/fetch/verify/sweep/report on smic + Trackio (public board :22041) |
| Verify | `make verify` (7 assertions) — caught LoRA leaking into the "frozen" vision tower |
| 500M DPO + LR tuning | LR was 200x too low; **1e-3** best; held-out acc 0.50->0.58; divergence trap caught |
| **3B DPO (Phase 2)** | held-out preference acc **0.65** — the real delta from scaling the model |
| **Closed-loop RLAIF (Phase 4b)** | Qwen-3B -> free VLM judge -> fresh prefs -> DPO. **Loop works, $0 cost.** |
| RLAIF win-rate (round 1) | **56%** vs base (48-prompt eval; above chance, within noise) |
| **RLAIF iteration (round 2)** | **37.5%** vs base — iterating a weak judge OVER-OPTIMIZES (reward hacking). Judge is the bottleneck. |

Honest bottom line: the machinery (harness, DPO, closed-loop RLAIF) all works and is verified; effect size
is limited by model scale and, for RLAIF, the free judge's noise. Next levers: stronger judge (paid/ensemble),
KL-reg + early-stop on a gold metric, more rounds with a good judge.
