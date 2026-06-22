# Outline — TF→PyTorch Migration Series

<!-- ABOUTME: Section-by-section scaffold for both parts of the TF→PyTorch series (titles, hooks, flow, visuals, pitfalls). -->
<!-- ABOUTME: Outline only — no article prose. Drawn from great-medium-article.md Part II. Draft with workflow-new-article.md. -->

Scaffold only — fill the prose during drafting. Each section uses the **Gradual Discovery** cycle: `problem → method → concrete example → pitfall`. See `../../../docs/references/writing-standards.md` §3.

---

# Part 1 — TF→PyTorch Migration

## Title options (pick one, draft 5–10 variants)

1. "We Migrated 50K Lines of Deep Learning from TensorFlow to PyTorch. Here's What Broke (And How We Fixed It)"
2. "The Hidden Differences Between TensorFlow and PyTorch That No One Warns You About"
3. "From TF to PyTorch: A Systematic Migration Methodology for Production ML Systems"

**Subtitle (working):** "A battle-tested methodology from migrating 50K lines of TF to PyTorch."

## Hook options

- **Recommended (Bold statement + Unexpected insight):**
  > "We migrated 50,000 lines of deep learning code from TensorFlow to PyTorch. Within a week, every model performed worse — not because our code was wrong, but because the two frameworks fundamentally disagree on how convolutions, optimizers, and even image resizing should work. This article is about the systematic methodology we built to find and fix every one of these differences."
- Alternatives: Problem-focused, Scenario ("It's 2am, the run just diverged…"). See `writing-standards.md` §2.

## Section flow

### Section 1 — Why Migrate? *(problem → method intro)*
- The growing gap: PyTorch's research dominance, HuggingFace ecosystem, paper implementations.
- What TF couldn't do: DINOv3, multi-GPU, mixed precision, latest architectures.
- Frame as a **forced move, not a preference** — builds empathy.

### Section 2 — Why It's Harder Than You Think *(deeper problem → method detail)*
- Scale: ~50K LOC of DL, ~15K LOC TF-specific.
- No unit tests in the original → can't regression-test the migration.
- The fundamental differences:
  - Conv padding: TF `SAME` vs PyTorch explicit padding
  - Adam: epsilon placement differs
  - Data format: NCHW vs NHWC
  - Image resizing: different interpolation implementations
  - Pretrained weight formats differ
- Even loading + resizing an image gives different tensors → work with raw tensors directly.
- **Pitfall:** direct translation is a trap. "Same code" ≠ "same behavior".

### Section 3 — The Verification Ladder *(method → concrete example)*
1. **Dummy model equivalence** — minimal model (dense only, no conv strides), identical weights both frameworks; compare inputs, per-layer outputs, loss, gradients (small relative tolerance for backend matmul diffs).
2. **Overfit the dummy** — can't memorize 2 batches of random data ⇒ something is fundamentally broken.
3. **Overfit the real model** — same test with Xception/DINOv3 on 2 batches ⇒ model + training loop correct.
4. **Validate on production data** — real datasets, compare metrics to TF baseline.
- Include the actual test-file structure + code snippet per step.

### Section 4 — Lessons Learned *(pitfalls → transition to Part 2)*
- Test as early as possible; build minimal dummy versions first.
- Lost knowledge in the codebase (undocumented decisions) — only testable with/without.
- "Matching" TF isn't enough — the optimal PyTorch config is different.
- **Transition:** "We matched TF performance. But that was just the starting point. The real gains came from a systematic tuning methodology — Part 2."

## Planned visuals (Part 1)
- Architecture diagram: training pipeline before/after migration.
- Side-by-side code: TF vs PyTorch for a key op (conv, optimizer setup).
- Table: framework differences inventory (operation · TF behavior · PyTorch behavior · impact).
- Training curves: TF baseline vs naive PyTorch port vs verified PyTorch.
- Flowchart: the verification ladder.

---

# Part 2 — Systematic Tuning Methodology

## Title options

1. "A Systematic Methodology for Tuning Deep Learning Models (Based on the Google Research Tuning Playbook)"
2. "Stop Guessing: How We Systematically Tuned PyTorch Training to Beat Our TensorFlow Baseline"
3. "The 5-Phase Experiment Workflow That Turned Hyperparameter Tuning From Art Into Science"

## Hook options

- **Recommended (Problem-focused + Curiosity gap):**
  > "Most hyperparameter tuning looks like this: change the learning rate, run for 6 hours, check the result, repeat. After migrating to PyTorch, we had hundreds of knobs to tune and no systematic way to turn them. So we built one — a 5-phase methodology based on the Google Research Tuning Playbook that turned guesswork into science. The first thing it taught us: the parameter you think matters most probably doesn't."

## Section flow (Gradual Discovery cycles)

### Cycle 1 — The Problem With Ad-Hoc Tuning
- *Problem:* after migration, "same hyperparameters" gives different results; need PyTorch-optimal config.
- *Method:* Google Research Tuning Playbook — separate **scientific** parameters (what you study) from **nuisance** parameters (what you must control). *(Define both terms on first use.)*
- *Example:* "Does TrivialAugment help? Comparing fairly requires tuning its sub-parameters (magnitude bins, probability) per augmentation. Without separation, you compare tuned-A vs untuned-B."
- *Pitfall:* conflating scientific and nuisance parameters → biased conclusions.

### Cycle 2 — Designing Rigorous Experiments
- *Problem:* how to efficiently explore the search space?
- *Method:* **quasi-random sampling (Halton sequences)** over grid/random — better coverage, fewer trials. *(Define Halton.)*
- *Example:* label-smoothing study — scientific = `label_smoothing` (0.0–0.2, uniform); nuisance = `dropout` (0.1–0.3), `image_size` ([224, 256]); 15 configs via Halton.
- *Pitfall:* grid search wastes compute on correlated dimensions; random is better but not optimal; quasi-random is the sweet spot.

### Cycle 3 — The 5-Phase Experiment Workflow
- *Problem:* well-designed experiments still fail in practice — wrong YAML, unlogged params, GPU crashes.
- *Method:* **Design → Generate → Verify → Document → Launch.**
  1. Collaborative design (research question, parameter selection, ranges from literature)
  2. YAML generation (Halton sequences, TEST config for validation)
  3. Pre-launch verification (hparam logging check, git state, server availability, TEST yaml run)
  4. Documentation (hypothesis **before** results — prevents post-hoc rationalization)
  5. Full deployment + monitoring
- *Pitfall:* skipping the TEST yaml phase → config errors discovered after 30 × 6-hour runs.

### Cycle 4 — Reading Results and Iterating
- *Problem:* 30 results — how to actually interpret them?
- *Method:* systematic analysis — best per scientific-parameter value, interaction effects, convergence analysis.
- *Example:* "Label smoothing 0.1 won in 83% of configs — but only with dropout < 0.2. Invisible in a one-at-a-time search."
- *Pitfall:* conclusions from single runs without considering variance across nuisance parameters.

### Cycle 5 — The Compound Effect
- *Problem:* individual improvements are modest — how do they stack?
- *Method:* cumulative optimization — apply discoveries sequentially, re-verify each step.
- *Example:* progressive results table: baseline → +correct optimizer → +tuned augmentation → +regularization → final (total TF→PyTorch gain).
- *Pitfall:* assuming optimizations are independent — interactions can make the sum less (or more) than the parts.

### Closing — Making It Your Own
- Methodology is framework-agnostic (JAX, TF, PyTorch).
- Open-source the experiment-generation tools if possible.
- Key line: "A systematic methodology beats intuition not because intuition is wrong, but because it doesn't scale."
- CTA: "What's your tuning methodology? Comment with the most surprising hyperparameter interaction you've discovered."

## Planned visuals (Part 2)
- Flowchart: the 5-phase workflow (core visual, reference repeatedly).
- Table: scientific vs nuisance parameter examples across experiment types.
- Diagram: Halton vs grid vs random sampling (2D parameter space).
- Results table: real experiment, progressive improvement.
- Training curves: best configs across experiments.
- Heat map: parameter interaction effects (if data available).

---

# Pitfalls map (whole series)

From `great-medium-article.md` §15 — risk level per pitfall for this specific content:

| Pitfall | Risk | Counter |
|---------|------|---------|
| Jargon overload | HIGH | Define `nuisance`/`scientific` params, `Halton sequences` on first use; skip explaining SGD |
| Weak headline | HIGH | Use §1 formulas; put a concrete result in the title |
| No narrative | HIGH | Tell the development story; the failures are the value |
| Ignoring distribution | HIGH | Follow `writing-standards.md` §11 (Reddit, X, LinkedIn, tag people) |
| No visuals | MEDIUM | Training curves, workflow diagrams, parameter-space viz; visual / 100–150 words |
| Missing CTAs | MEDIUM | Specific question per part, not "what do you think?" |
| Poor code quality | MEDIUM | Test every snippet; include imports; annotate tensor dims |
| Inconsistent series quality | MEDIUM | Make Part 1 standalone-valuable (the verification ladder stands alone) |
| Padding without depth | LOW | Keep Part 1 tighter/more focused than Part 2 |
| Unverifiable claims | LOW | Show actual numbers, not "significant improvement" |

---

# Cross-part wiring (see `writing-standards.md` §10)

- Each part standalone-valuable; readers may hit Part 2 first.
- Nav links top **and** bottom; keyword-rich anchor text.
- Part 1 ends on constructive tension (the transition above), not a cliffhanger.
- Publish Part 2 within 1–2 weeks of Part 1.
