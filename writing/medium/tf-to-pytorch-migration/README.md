# TF→PyTorch Migration — Article Project

<!-- ABOUTME: Project README for a two-part Medium series on migrating ~50K lines of DL code TF→PyTorch + systematic tuning. -->
<!-- ABOUTME: Tracks the two-part plan, status, and links to standards, workflow, and the section-by-section outline. -->

**Status: draft (scaffold — outline only, no prose written yet)**

A two-part Medium series for ML engineers, drawn from a real project: migrating ~50,000 lines of deep-learning code from TensorFlow to PyTorch, then building a systematic hyperparameter-tuning methodology to not just match but beat the TF baseline.

## The two-part plan

| | Part 1 | Part 2 |
|---|--------|--------|
| **Topic** | TF→PyTorch migration | Systematic tuning methodology |
| **Reader journey** | "This is harder than I thought" → "There's a systematic way" | "Guessing isn't enough" → "Here's a rigorous framework" |
| **Emotional arc** | Empathy → competence | Curiosity → mastery |
| **Standalone value** | How to migrate and verify correctness | How to systematically tune any DL model |
| **Target length** | ~3,000–4,000 words (10–15 min) | ~4,000–5,000 words (15–20 min) |

**The narrative thread:** the migration reveals that "same configuration" ≠ "same behavior", which forces a principled approach to finding the right configuration in the new framework. That insight bridges Part 1 into Part 2.

## Files

- `outline.md` — section-by-section outline for both parts (titles, hooks, flow, visuals, pitfalls map)
- *(later)* `part-1.md`, `part-2.md` — the drafted articles

## References

- Rules: [`../../../docs/references/writing-standards.md`](../../../docs/references/writing-standards.md)
- Workflow: [`../../../docs/references/workflow-new-article.md`](../../../docs/references/workflow-new-article.md) — use **Part B (from research)**, since the project material already exists
- Deep reference + this series' blueprint: [`../../../docs/references/great-medium-article.md`](../../../docs/references/great-medium-article.md) (Part II)

## Next steps

1. Gather raw material: migration repo diffs, verification test files, tuning experiment results.
2. Confirm the single takeaway per part (workflow Phase 1.1).
3. Draft Part 1 from `outline.md` following the workflow Part B.
4. Produce visuals (Phase 5), run the pre-publish checklist (Appendix C), publish.
