# RLAIF on a tiny VLM

A 2-day hackathon: train a small vision-language model with **RLAIF** on a single RTX-3090, with
first-class observability — then close the loop for real. Full write-up in **[`report/PRESENTATION.md`](report/PRESENTATION.md)**.

## What we did (Phase 0 → 4b of `DESIGN.md`)

| | Result |
|---|---|
| **Harness** | one command each: `deploy / monitor / fetch / verify / sweep / validate / rlaif` on the remote `smic` box, live Trackio dashboard, reproducible report figures |
| **Verify** | `make verify` — 7 DPO wiring assertions (step-0 loss = ln2, overfit-to-0, LoRA-only grads). Caught LoRA silently adapting the "frozen" vision tower |
| **LR tuning** | the baseline LR was ~200× too low; **1e-3** is the stable optimum; held-out acc 0.50 → 0.58 (500M) |
| **Fix the recipe (day 2)** | LoRA r=32+MLP, lr 1e-4 cosine, more data: own-slice arc **0.58 → 0.643 (8k) → 0.701 (16k) → 0.709 (24k)**; clean fixed-slice head-to-head: **24k model 0.723** vs 16k 0.656 |
| **Epoch-band finding** | all three scaled runs inflect upward at **epoch ≈ 0.6-0.75** after a flat phase — epoch-aware early-stop gates (not step-matched) were essential |
| **Closed-loop RLAIF** | our model generates → **free** VLM judge → fresh prefs → DPO, at **$0**: 56% (round 1) → 37.5% (iterating = reward-hacks the noisy judge) → **58.3%** (3-vote de-noised labels). Judge noise measured at 20%; 108 clean on-policy prefs ≈ 3k noisy dataset pairs |
| **Measurement bugs caught by our own instruments** | eval-slice confound (train_size moved the eval set), judge order-swap noise (20%), fixed-slice contamination (24k trained through the pinned slice — flagged at 0.887, rescored clean) |

**Bottom line:** the machinery is built and *verified*, the final model (`qwen3b-overnight-24k/checkpoint-2500`)
is a real, honestly-measured improvement (**0.72** clean held-out preference accuracy vs ~0.5 chance), and
every weak result comes with a measured cause rather than a shrug.

## Run it

```bash
make verify          # prove the DPO training loop is bug-free (fast)
make deploy          # SmolVLM-500M DPO baseline on smic, full observability
make monitor         # live Trackio dashboard (also public at http://smic.<domain>:22041)
make sweep           # parallel LR sweep, then `make sweep-report`
make scale           # switch to Qwen2.5-VL-3B (one config)
make rlaif           # closed-loop RLAIF: generate -> free-VLM judge -> DPO retrain -> win-rate
make fetch           # pull results back locally
```

## Layout

- `DESIGN.md` — the guiding design doc (phased plan).
- `report/PRESENTATION.md` + `report/figures/` — the slide deck.
- `configs/` — one YAML per experiment. `data/build_dataset.py` — RLAIF-V -> TRL adapter.
- `src/` — `train_dpo.py` (entrypoint), `callbacks.py` (dual-write observability),
  `verify_wiring.py` (regression guard), `rlaif_{generate,judge,eval}.py` (the closed loop),
  `sweep_report.py` / `report.py` (analysis + figures).
- `scripts/` — the harness (deploy/monitor/fetch + orchestration).
- `docs/superpowers/` — specs + implementation plans. `tasks/` — lessons + RL-verification checklist.
