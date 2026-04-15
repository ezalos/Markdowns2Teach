# Station F deck revisions — design (2026-04-13)

## Context

The Station F decks (`slides/station-f/A-state-of-the-field.md`, `B-building-with-ai.md`) ship Wednesday April 15, 2026. After a first review pass, Louis identified ~25 specific corrections plus a new "Frontier" section drawn from `docs/sources/The Agentic AI Arms Race_ Q1 2026 Competitive Landscape.pdf`.

The brief: more depth on AI direction (inference cost, open-source gap, context window growth, METR autonomy), more depth on coding-agent components (split memory + tools + permissions slides), regenerate weak visuals as PaperBanana infographics, drop two banal slides, restructure so the 6-component anatomy comes BEFORE orchestration patterns, and add an end-of-A "what's next" section based on the PDF.

Resolved during brainstorming:
- **Frontier section** placement: end of Deck A as climax (not Deck B, not separate Deck C)
- **S22** (Claude Code leak overview): drop, salvage `subagents-use-prompt-caching` into S20 memory and `retry/resilience` as own short slide
- **Restructuring scope**: open redesign with narrative judgment (use Louis's per-slide list as source of truth for content/intent, restructure freely for flow)
- **PaperBanana**: generate all 10 in background, 7 iterations minimum (up to 15 if needed)
- **PDF citation**: cite primary sources for each claim, PDF stays as lead-gen only
- **Benchmark depth**: 4 slides — SWE-bench, Terminal-Bench, OSWorld, METR

Non-negotiable (carried from earlier audit pass): every data claim has a verifiable primary source.

## Final deck shape

### Deck A — `slides/station-f/A-state-of-the-field.md` (~40 slides, ~38 min)

```
0. INTRO                                                        3 sl
   00 title  ·  01 hook  ·  02 what-you'll-leave-with

1. STATE OF LLMs 2026 (expanded)                               12 sl
   03 Benchmarks: real progress, visible ceilings (kept)
   04 METR — task autonomy doubling every 7 months (NEW, includes METR's time-horizon plot)
   05 Inference cost dropping (NEW, Epoch AI time series)
   06 Open-source vs closed: ~6-month gap (NEW, Devstral 2 / Gemma 4)
   07 Context window growth (NEW, Opus 4.6 1M, Llama 4 10M, etc.)
   08 Training cost: from thousands to billions (kept, fixed numbers)
   09 Inference economics: B-params → GB-VRAM (NEW)
   10 Quantization tradeoffs (NEW)
   11 Qwen3-32B sweet spot for self-hosting (NEW)
   12 Reading HF model names (NEW, Qwen3-32B-Instruct-AWQ-4bit deconstructed)
   13 Synthetic data: the answer to the data wall (kept)
   14 David beats Goliath (kept)
   DROPPED: old s.04 (LLM use cases, banal) + old s.08 (pricing table, removed)

2. WHAT IS AN AGENT                                             3 sl
   15 What counts as an agent (kept)
   16 Spectrum of agency (kept)
   17 Think → Act → Observe loop (kept)

3. ANATOMY OF A CODING AGENT (moved BEFORE orchestration)       9 sl
   18 Six components overview (kept, was s.16)
   19 Component 1 — Live Repo Context (NEW split + paperbanana)
   20 Component 2 — Stable Prompt Prefix + Cache Reuse (NEW split + paperbanana)
   21 Component 3 — Tool Access (image-dominant rewrite, ~18 tools visual)
   22 5-level Permission System (NEW separate slide + paperbanana)
   23 Component 4 — Context Compaction (paperbanana replaces low-quality LS image)
   24 Component 5 — Memory part 1 (architecture + on-disk JSON + paperbanana)
   25 Component 5 — Memory part 2 (3-layer + autoDream + leverage discussion)
   26 Component 6 — Bounded Subagents + retry/resilience (salvaged from old s.22)

4. ORCHESTRATION PATTERNS                                       4 sl
   27 Golden rule: start simple (Anthropic complexity ladder, kept)
   28 Chaining + Routing (with original Anthropic illustrations, NEW concrete example)
   29 Parallelization + Orchestrator-Workers (with original illustrations, NEW examples)
   30 Evaluator-Optimizer (own slide for clarity, NEW example)

5. AGENTS IN THE WILD                                           4 sl
   31 Claude Code (kept, was s.23)
   32 OpenClaw — open-source personal agent (NEW deep-dive)
   33 MiroFish — composable agent stack (NEW deep-dive)
   34 AutoResearch — Karpathy 630-line script (NEW deep-dive)

6. FRONTIER — what's next                                       9 sl
   35 7 battlegrounds part 1 (coding · GUI · MCP · multi-agent — 2x2 grid)
   36 7 battlegrounds part 2 (enterprise · safety · OSS-vs-prop — 1x3)
   37 Decisive breakthroughs Q1 2026 (GPT-5.4 / Opus 4.6 / Gemini 3.1 / Copilot Cowork)
   38 Lab investment landscape ($122B OpenAI · $30B Azure-Anthropic · $2B Meta-Manus · etc.)
   39 Benchmark deep-dive: SWE-bench (saturation + Pro divergence + perf-vs-time)
   40 Benchmark deep-dive: Terminal-Bench / agentic coding
   41 Benchmark deep-dive: OSWorld / GUI agents (GPT-5.4 superhuman)
   42 Benchmark deep-dive: GAIA / multi-step assistants (METR autonomy already covered at A-04)
   43 Scaffolding > model thesis ("infrastructure is the new moat")

7. TAKEAWAY                                                     1 sl
   44 Closing (refined)
```

**Total Deck A: ~44 numbered slides + title = 45 sections, ~38 min**

### Deck B — `slides/station-f/B-building-with-ai.md` (~17 slides, ~25 min)

Same as current with three changes:

```
B-00 bridge (kept)
B-01 Bitter Lesson (kept)
B-02 Prompt-based dev / CV before/after (kept)
B-03 GenAI lifecycle (kept)
B-04 Baseline first (kept)
B-05 Building MVP — 3 ingredients (MOVED here, was B-06)
B-06 MVP patterns table — 5 ways to validate (MOVED here, was B-05)
B-07 Rapid agent prototyping (kept)
B-08 6 pitfalls Chip Huyen (kept)
[DROPPED: old B-09 Prompting → RAG → Fine-tuning progression]
B-09 Pricing reinvention (was B-10)
B-10 Klarna case (was B-11)
B-11 L'Oréal + Doctolib (was B-12)
B-12 5 structural trends (was B-13)
B-13 EU AI Act — 4 risk categories explainer (NEW)
B-14 EU AI Act — timeline + penalties (was B-14)
B-15 Key takeaways (was B-15)
B-16 Questions (was B-16)
```

**Total Deck B: 16 numbered slides + title + close = ~18 sections, ~25 min**

**Grand total: ~62 sections / ~60 min content** (Deck A 38 min + Deck B 22 min when image-dominant slides present in 30s). Tight; needs a rehearsal pass to tune.

## Components / work breakdown

### Component 1 — Source archives & research extracts

Three new research artifacts under `docs/station-f/`:
- `_arms-race-extract.md` — already drafted (in agent's plan file, copy verbatim)
- `_metr-research.md` — METR Time Horizon report key findings + perf-vs-time data
- `_qwen3-quantization-research.md` — Qwen3 32B sweet spot, AWQ/GGUF naming, B→GB math

### Component 2 — PaperBanana batch (10 infographics)

Generate via `uvx paperbanana generate -i <input.txt> -c "<caption>" -n <iter>`. Minimum 7 iterations, up to 15 when needed.

| # | Slide it serves | Topic | Caption seed |
|---|-----------------|-------|--------------|
| 1 | A-09 inference econ | B-params → GB-VRAM at FP16/INT8/INT4 | "Memory math for self-hosting LLMs" |
| 2 | A-18 anatomy overview | 6 components circular diagram | "The six components of a coding agent" |
| 3 | A-19 repo context | Workspace summary collection | "Live repo context: the agent's first read" |
| 4 | A-20 prompt prefix | Stable prefix + cache reuse | "Prompt caching: the cheap part stays cheap" |
| 5 | A-22 5-level perms | Hierarchical permission system | "Five permission levels Claude Code uses" |
| 6 | A-23 compaction | Clip + summarize + dedupe | "Three ways agents compress context" |
| 7 | A-24 memory pt1 | On-disk JSON working/transcript memory | "Working memory vs transcript: two storage layers" |
| 8 | A-25 memory pt2 | Three-layer memory + autoDream | "Three-layer memory and autoDream consolidation" |
| 9 | A-39 SWE-bench trajectory | Score-vs-time chart | "SWE-bench Verified saturation 2024-2026" |
| 10 | A-43 closing thesis | Infrastructure-as-moat visual | "The model is not the moat, the system is" |
| 11 | A-04 METR | Time-horizon plot (autonomy doubling every 7 months) | Redrawn version of METR's published chart, with attribution. Optional — first preference is to embed METR's published chart with proper credit; paperbanana is the fallback if licensing is unclear. |

Outputs land in `paperbanana_workspace/outputs/run_<id>/final_output.png`. After each run completes, the implementation agent inspects the final image (and intermediate iterations if needed), picks the best, and copies it to `slides/station-f/assets/paperbanana/<descriptive-name>.png`. Slides reference via that path.

### Component 3 — New slide content (Deck A NEW slides)

13 brand-new slides need content drafting:
- A-04 METR autonomy (uses METR report citation)
- A-05 Inference cost dropping (Epoch AI pricing trends data)
- A-06 OS gap (Devstral 2 SWE-bench numbers, Gemma 4 release date)
- A-07 Context window growth (Opus 4.6 1M, Llama 4 10M Series — verify each)
- A-09 B → GB inference economics (FP16/INT8/INT4 math table)
- A-10 Quantization tradeoffs (perplexity loss vs size reduction)
- A-11 Qwen3-32B sweet spot (Qwen3 HF model card data)
- A-12 HF naming (Qwen3-32B-Instruct-AWQ-4bit broken down)
- A-22 5-level permission system (LS PDF + paperbanana)
- A-26 Bounded Subagents + retry/resilience (salvaged S22 content)
- A-32 OpenClaw deep-dive (PDF + new web search)
- A-33 MiroFish deep-dive (existing archive + new web search)
- A-34 AutoResearch deep-dive (existing data + Karpathy's GitHub)
- A-35..A-43 Frontier section (9 slides, content from PDF extract)

### Component 4 — Existing slides to edit

11 existing slides need touch-ups:
- A-03 (benchmarks) — keep as-is (already strong)
- A-08 training cost — fix the numbers per audit + keep
- A-14 David vs Goliath (was A-09) — fix QwQ score per audit + keep
- A-18 6-components — keep, swap current image (Raschka figure 13) for new paperbanana #2
- A-19 + A-20 — split from old A-17, add paperbananas
- A-21 tool access — minimize text, image-dominant
- A-23 compaction — replace LS image with paperbanana
- A-24 + A-25 — split from old A-20, add second slide
- A-26 — new slide salvaging old S22 content
- A-28 + A-29 + A-30 — orchestration: add Anthropic original illustrations + concrete examples
- A-31 (Claude Code) — keep as-is

### Component 5 — Deck B small edits

- Swap B-05 ↔ B-06 ordering
- Remove old B-09 slide
- Insert new B-13 slide explaining the 4 risk categories with concrete examples per category

### Component 6 — Build & verify

- `make build-station-f` — already added in previous turn, fast
- Citation audit (will likely flag new sources; may need to extend authority-map)
- Overflow check
- Visual review via `dist/html/`

## Dependencies / sequencing

1. **Research extracts** (parallel, ~20 min): METR research, Qwen3 research, copy arms-race extract
2. **PaperBanana batch** (background, kicks off after research is in — needs 300+ word inputs): ~70 min wall time
3. **Slide editing** (sequential, ~3 hours):
   a. Deck A reorganization (move section 3 before section 4) — first
   b. Drop slides (s.04, s.08, old B-09) — quick
   c. Reorder Deck B slides — quick
   d. New A slides (Section 1 expansions, agent example deep-dives, Frontier section)
   e. New B-13 risk categories slide
   f. Swap PaperBanana images in as they become ready
4. **Citation audit + build verification** (~30 min)

Total wall time: ~5 hours, parallelizable to ~3.5h with PaperBanana running in background.

## Critical files

**Read-only inputs**:
- `slides/station-f/A-state-of-the-field.md` (current state, ~503 lines)
- `slides/station-f/B-building-with-ai.md` (current state, ~298 lines)
- `docs/sources/The Agentic AI Arms Race_ Q1 2026 Competitive Landscape.pdf`
- Existing source archives at `docs/station-f/sources/{raschka-coding-agent,latent-space-claude-code-leak,mirofish}/`
- `docs/references/slide-creation-standards.md` § 6 (citation conventions)
- `docs/references/authority-map.{md,yaml}` (publisher tiers)
- `paperbanana.md` (PaperBanana CLI usage)
- `themes/station-f.css`

**To create**:
- `docs/station-f/_arms-race-extract.md` (from agent's plan file content)
- `docs/station-f/_metr-research.md`
- `docs/station-f/_qwen3-quantization-research.md`
- `slides/station-f/assets/paperbanana/*.png` (10 images)
- `paperbanana_workspace/inputs/*.txt` (10 input briefs, 300+ words each)

**To modify**:
- `slides/station-f/A-state-of-the-field.md` (major rewrite)
- `slides/station-f/B-building-with-ai.md` (3 small edits)
- Possibly `docs/references/authority-map.{md,yaml}` (add METR, Taskade, possibly others)

## Verification

End-to-end checks before declaring done:
1. `make build-station-f` exits 0 (HTML + PPTX + PDF all generated)
2. `make check` (overflow check) shows zero warnings on `slides/station-f/*`
3. `bash scripts/check-citations.sh slides/station-f` shows OK
4. Manual read-through:
   - Every numerical claim in new slides traces to a primary source URL in the slide footer
   - Every paperbanana image is referenced (no orphan files, no broken paths)
   - Frontier section bibliography uses primary sources, not the PDF
   - Total slide count ≈ 60 (A) + 17 (B) — matches design
5. Visual review in browser (`make html` then open `dist/html/index.html`)
6. Timing rehearsal: read each slide aloud at presentation pace, target ~38 min for Deck A + ~25 min for Deck B

## Out of scope (defer or skip)

- New illustrations beyond the 10 paperbanana batch (e.g. custom diagrams for orchestration patterns) — use Anthropic's existing SVGs from their Building Effective Agents page
- Deeper L'Oréal investigation (already addressed in earlier polish pass)
- Cite-apply formal pipeline run on the new slides — too slow for Tue night; we'll do citation audit by hand based on the 70-claim baseline
- Splitting Frontier into its own deck (decided against in brainstorming)
- New theme work — `themes/station-f.css` stays as-is

## Open items requiring Louis's input (after spec approval)

Two things will only become clear during execution:
- Exact PaperBanana iteration counts per infographic (start at 7, may bump some to 15 if quality demands)
- Concrete examples for orchestration patterns (chaining/routing/parallelization/orchestrator-workers/evaluator-optimizer) — do you want startup-flavored examples (e.g. "support email triage uses chaining: classify → route → respond") or technical examples? Will default to startup-flavored unless you say otherwise.
