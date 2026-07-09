# Handoff → deck-building agent (from the agent that ran the hackathon)

I ran the 48h research loop this deck describes; I hold the full session ground truth. This answers your
three open calls, corrects two parsing errors, and maps the new assets I just added under `docs/rlaif-vlm/`.

## 1. Verdict on your current understanding

Mostly correct, and two of your calls are exactly right:
- **Judge = separate free VLM** (`nvidia/nemotron-nano` free tier via OpenRouter), never the trained model. ✅
- **Two different evaluators, both legit** — make it explicit exactly as you proposed. ✅
  - Scoreboard (50→72.3%): the *trained model itself* ranking held-out chosen/rejected pairs from the
    RLAIF-V dataset (labels from the dataset's AI labeler). Chance = 50%.
  - Win-rate (56/37.5/58.3%): the *separate judge* blind-comparing tuned-vs-base answers on fresh prompts.

## 2. Your three pending calls

**Slide 10 (flat→leap):** recommend **option 2 — fold into slide 11 as one line** ("every scaled run went
flat then jumped at the same relative point; a naive stop-rule would have killed the winner"). Louis dictated
removal, and the beat survives as a line. Note: if you drop the slide, keep the *concept* of pre-registered /
epoch-aware gates alive somewhere — slide 8's `[~02:00] flat phase… held, not killed` beat depends on it.
(Final call is Louis's.)

**Slide 12:** keep, with your planned one-liner ("the judge is a separate model"). Your causal reading is
correct: round 2 = over-optimization of a noisy proxy — the model aced the *training* labels (train margins
exploded) while true quality fell; we measured the judge's noise at 20% order-swap inconsistency.

**Slide 2 real images:** assets now available (see map below). Provenance warning on the current quote:
the "suits and ties overlapping" / "It is unknown" pair is REAL (documented in `internal/todo.md`, round-1
judging, 2026-07-01 ~22:00) but the round-1 preferences file was later overwritten by the scaled run, so I
cannot re-attach its exact image. Two safe options:
  a) Keep the quote, no image, cite "agent lab log, round 1" — it is sourced to the committed todo.md.
  b) Switch to a fully-sourced pair from `examples/rlaif/preferences.jsonl` (+ its image in
     `examples/rlaif/images/`), or — often stronger for this audience — a **before/after** from
     `examples/probes_fullres/`: same real image, the model's actual description at training step 100 vs 500
     (`probe_log.jsonl` fields: i, step, prompt, generation; image = `probe_images/<i>.png`).

## 3. Corrections to your parsing (important)

**"cron every ~20 min launching parallel-experiment servers" — not what happened.** The ~19-min cron was a
*watchdog*, not a launcher: each firing did (1) infrastructure check, (2) science read of the learning
signal, (3) comparison vs previous runs at matched training progress, (4) gate enforcement / queue
advancement. Experiments on the 3B model ran **serially** (one fits the 24GB GPU) as **self-relaunching
chains** (train → eval → decide → scale → overnight → eval). Parallelism existed in exactly three places:
day-0 parallel deep-research; the small-model (500M) LR sweeps (3 trials at once via a gradient-accumulation
memory trick); and CPU-side judge/API work overlapping GPU training. Suggested slide-4 phrasing: *"a watchdog
woke every ~19 minutes to check, diagnose, compare, and decide — while self-relaunching experiment chains did
the work."*

**"remove pre-gestant Adquette"** = almost certainly *"pre-registered gates"* (dictation garble). See slide-10
note above before removing that chip entirely.

## 4. Slide 11 step-decomposition — confirmed numbers

- 50 → 58: learning-rate was ~200× too low (5e-6 → 1e-3), found by a systematic sweep (500M model).
- 58 → 65: model scale 500M → 3B (one config line).
- 65 → 72.3: recipe fix (LoRA r32 incl. MLP layers + cosine schedule) + data scaling 8k→16k→24k + ship-best-checkpoint.
- Speaker-note honesty caveat (nice callback to your slide 9): the intermediate numbers were measured on
  *different* held-out slices — that's precisely the "moving exam" bug the loop later caught; **72.3 vs 65.6**
  is the verified-clean comparison.
- Sourced figure you asked about earlier: **95 commits** in the 48h window (`git log --since 2026-07-01`).

## 5. Asset map (docs/rlaif-vlm/)

- `examples/rlaif/` — preferences.jsonl (105 AI-judged pairs), candidates.jsonl (128), `images/` (128 real
  images). Base-model generations judged by the free VLM.
- `examples/rlaif2/` — same schema, round-2 (on-policy: generations from the already-tuned model).
- `examples/probes_fullres/` — probe_log.jsonl (8 frozen images × steps 100..500) + `probe_images/` —
  the best before/after material.
- `examples/probes_16k/` — same for the 16k record run (steps 750/1500).
- `examples/data_sanity_16k.jsonl` — 8 real RLAIF-V *training* rows (prompt/chosen/rejected text; no images).
- `figures/`, `results/`, `internal/`, `STORY.md`, `PRESENTATION.md`, `README.md`, `DESIGN.md` — as before.
  Reminder: `results/overnight_best.json` (0.887) is the *contaminated* reading — quote
  `overnight_best_clean.json` (0.7227).

---

## UPDATE (2026-07-08) — new companion doc + go-ahead: finish the deck

Read **`RLAIF-LEVELS-METRICS-GAINS.md`** (same dir). It contains, slide-ready and fully sourced:
1. The 3-levels-of-RLAIF table (did 1+2, deliberately not 3) — add as a slide or fold into slide 12/13.
2. The metrics explainer (optimized = DPO loss only; accuracy & win-rate = thermometers; chance levels + error bars) — use for slide-11 speaker notes and the two-evaluators clarification.
3. **Slide 06:** ADD the two intervention prompts — (A) the parallel-compute demand (GPU 40→98%) and (B) the budget/free-judge demand (pays off the $0 stat). Verbatim quotes + slide copy + honesty notes in the doc. Use A + B1 unless Louis says otherwise.
4. **Slide 10 (scoreboard):** replace the "+7 recipe + data" line with the measured decomposition:
   +8 recipe overhaul + 4x data (bundled) -> +1 data x2 (within noise; ranking confidence +43%) -> +7 data x3 + full epoch (clean set).
   Speaker note: per-component attribution deliberately not measured (deadline tradeoff). Do NOT present per-component numbers — they do not exist.
Also apply the earlier corrections in this file (watchdog != parallel-experiment launcher; "pre-gestant Adquette" = "pre-registered gates" — keep the concept alive for slide 8). Then finalize.
