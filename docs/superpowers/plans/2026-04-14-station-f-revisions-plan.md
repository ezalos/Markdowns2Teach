# Station F Revisions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply ~25 corrections + new Frontier section to `slides/station-f/{A,B}-*.md` per the brainstorming spec, in time for Wed Apr 15 talk.

**Architecture:** Two Marp decks edited in place. New content comes from three research extracts (METR, Qwen3/quantization, agent-deep-dives) + one PDF extract (Arms Race Q1 2026). New visuals from a parallel PaperBanana batch (11 infographics). Build via existing `make build-station-f` target.

**Tech Stack:** Marp CLI (already installed), PaperBanana via `uvx`, Python validation scripts in `scripts/cite/*`, theme `themes/station-f.css`, citation-audit pipeline already exists.

**Source spec:** `docs/superpowers/specs/2026-04-13-station-f-revisions-design.md` — read this BEFORE starting any task.

**Companion files (read as needed):**
- `docs/station-f/spec.md` — current Station F spec / citation index
- `slides/station-f/A-state-of-the-field.md` — current Deck A (~503 lines)
- `slides/station-f/B-building-with-ai.md` — current Deck B (~298 lines)
- `docs/station-f/sources/raschka-coding-agent/README.md`
- `docs/station-f/sources/latent-space-claude-code-leak/README.md`
- `docs/station-f/sources/mirofish/README.md`
- `docs/sources/The Agentic AI Arms Race_ Q1 2026 Competitive Landscape.pdf`
- `/home/ezalos/.claude/projects/-home-ezalos-42-Markdowns2Teach/memory/paperbanana.md`
- `docs/references/slide-creation-standards.md`
- `docs/references/authority-map.md` + `.yaml`

**Build verification command** (run after every meaningful task):
```bash
cd /home/ezalos/42/Markdowns2Teach && \
  bash scripts/check-citations.sh slides/station-f && \
  node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md && \
  node scripts/check-overflow-visual.js slides/station-f/B-building-with-ai.md && \
  make build-station-f
```

**Don't commit** unless explicitly asked at the end (Louis's standing rule). Plan tasks describe work; commit messages are deferred until final task.

---

## Phase 1 — Research extracts (parallel-friendly, ~30 min each)

These three tasks produce the source material that downstream slide-writing tasks read. They can run in parallel — they touch different files.

### Task 1: Copy Arms Race PDF extract into the working dir

**Files:**
- Read: `/home/ezalos/.claude/plans/goofy-wandering-stallman-agent-a2c6d45ae773cae4b.md` (contains the full extract content inside a markdown code block)
- Create: `docs/station-f/_arms-race-extract.md`

**Why:** A previous subagent fully read the 7-page PDF and wrote the structured extract into its plan file (because brainstorming gates blocked direct file writes). The content is ready — we just need to relocate it.

- [ ] **Step 1: Read the agent's plan file**

```bash
cat /home/ezalos/.claude/plans/goofy-wandering-stallman-agent-a2c6d45ae773cae4b.md
```

The file contains a markdown block (between ` ```markdown ` and ` ``` `) with the extract content. Everything we need is in §1–§6 of that block.

- [ ] **Step 2: Extract the markdown block to the target file**

Open `/home/ezalos/.claude/plans/goofy-wandering-stallman-agent-a2c6d45ae773cae4b.md`, copy everything between the opening ` ```markdown ` fence and the matching closing fence (lines ~10–243 of that file), and write it verbatim to `/home/ezalos/42/Markdowns2Teach/docs/station-f/_arms-race-extract.md`.

- [ ] **Step 3: Sanity-check the extract**

```bash
wc -w /home/ezalos/42/Markdowns2Teach/docs/station-f/_arms-race-extract.md
grep -c "^##" /home/ezalos/42/Markdowns2Teach/docs/station-f/_arms-race-extract.md
```

Expected: ~1500 words, 6 H2 headings (§1 through §6 plus "## Content to write" if accidentally included — strip the wrapper if so).

---

### Task 2: METR research extract

**Files:**
- Create: `docs/station-f/_metr-research.md`

**Why:** Slide A-04 cites "METR — task autonomy doubling every 7 months" with their actual time-horizon plot. We need: METR's report URL, the exact methodology, the time-series datapoints, the chart's licensing for embed/redraw, and what counts as the "task autonomy" measurement.

- [ ] **Step 1: Web-search the canonical METR report**

Use Tavily (`mcp__tavily__tavily_search`) with the query: `"METR" "time horizon" "task length" autonomy doubling site:metr.org`

Fallback: WebSearch the same query.

Pick the canonical METR report (their original "Measuring AI Ability to Complete Long Tasks" paper or its blog post on metr.org). Note the URL.

- [ ] **Step 2: Extract page content**

Use `mcp__tavily__tavily_extract` with `extract_depth: "advanced"` on the chosen URL. If that fails, fall back to `WebFetch`. Save the raw extracted text to `/tmp/metr-page.txt` for reference.

- [ ] **Step 3: Write the research extract**

Create `docs/station-f/_metr-research.md` with this structure (filled with verbatim quotes from the page):

```markdown
# METR research extract — for Station F slide A-04

**Canonical source URL**: <verbatim URL>
**Title**: <exact title from page>
**Authors**: <names from page>
**Publication date**: <date from page, YYYY-MM-DD>
**Accessed**: 2026-04-14

## What METR measures
<verbatim quote from the page describing the "task length / time horizon" methodology>

## Headline finding (verbatim)
> <exact quote of the doubling-claim sentence>

## Time-series datapoints (verbatim)
<list every (model, year, time-horizon-minutes) tuple they publish>

## The published chart
- URL of the chart image: <if accessible>
- License / attribution requirements: <e.g. "CC BY 4.0 with attribution to METR" — verify on the page>
- Recommended in-slide treatment: <embed-with-attribution / redraw-via-paperbanana / both>

## Quotes worth slide-using
> <2-3 short pull-quotes>

## Citation footer block (ready to paste into slide)
`[1] [METR — Time Horizon](URL)`
```

- [ ] **Step 4: Verify the extract**

```bash
wc -w /home/ezalos/42/Markdowns2Teach/docs/station-f/_metr-research.md
grep -E "^>" /home/ezalos/42/Markdowns2Teach/docs/station-f/_metr-research.md | head -5
```

Expected: ≥400 words, at least 3 verbatim blockquotes.

---

### Task 3: Qwen3 + quantization + agent-examples research extract

**Files:**
- Create: `docs/station-f/_qwen3-quantization-research.md`
- Create: `docs/station-f/_agent-examples-research.md`

**Why:** Three slides need fresh research — A-09 through A-12 (B→GB / quantization / Qwen3 sweet spot / HF naming) and A-32 through A-34 (OpenClaw / MiroFish / AutoResearch deep-dives).

- [ ] **Step 1: Qwen3 family research**

Search Tavily: `"Qwen3-32B" Hugging Face benchmark MMLU "Instruct" quantization AWQ GGUF`. Pick the official Qwen team blog post AND the Qwen3-32B HuggingFace model card. Extract via `tavily_extract` (advanced).

- [ ] **Step 2: Quantization theory research**

Search: `"int8 quantization" "int4 AWQ" "GGUF" perplexity vs size LLM inference VRAM`. Pick a respected technical source (Hugging Face docs, llama.cpp docs, or a recognized practitioner blog). Extract.

- [ ] **Step 3: Write `_qwen3-quantization-research.md`**

```markdown
# Qwen3 + quantization research — for Station F slides A-09 through A-12

## A-09 — B-params → GB-VRAM math

**Formula**: GB needed ≈ (params_in_B × bytes_per_param) + KV-cache + activations.
- FP16: 2 bytes/param → 7B = 14GB, 32B = 64GB, 70B = 140GB
- INT8: 1 byte/param → 32B = 32GB
- INT4 (AWQ/GGUF Q4): 0.5 bytes/param → 32B = 16GB

Source for the formula: <URL + verbatim quote>
Source for KV-cache addendum: <URL + verbatim quote>

## A-10 — Quantization tradeoffs

| Quant | Perplexity loss vs FP16 | Use case |
|-------|-------------------------|----------|
| FP16 | 0% baseline | Training, finest serving |
| INT8 | ~1-2% | Production serving, halves VRAM |
| AWQ INT4 | ~3-5% | Self-hosting on consumer GPUs |
| GGUF Q4_K_M | ~3-6% | llama.cpp / CPU-fallback |

Source for each row: <URL + verbatim quote>

## A-11 — Qwen3-32B sweet spot

**Why 32B is the sweet spot for self-hosting**:
- Fits on a single 24GB consumer GPU with INT4 quantization (~16GB after quant)
- Performance: <verbatim Qwen3-32B benchmark numbers from the model card>
- Cost vs Qwen3-72B / Qwen3-110B: <details>

Source: <Qwen blog URL + Qwen3-32B HF model card URL + verbatim quotes>

## A-12 — Reading HF model names

Example: `Qwen/Qwen3-32B-Instruct-AWQ-4bit`
- `Qwen` — organization
- `Qwen3` — model family / generation
- `32B` — params (billions)
- `Instruct` — fine-tuning variant (Instruct = instruction-tuned, Base = pretrained-only, Reasoning = reasoning-tuned)
- `AWQ` — quantization method (AWQ / GGUF / GPTQ / bnb)
- `4bit` — bit width

Source for naming convention: <HF docs URL + verbatim quote>
```

- [ ] **Step 4: Agent examples research**

For each of OpenClaw, MiroFish, AutoResearch:
- Tavily search the latest news + official repo
- Pull: what it does (1 sentence), key technical claim, headline number (stars / users / ARR / something), distinct angle vs the others, current status (active / abandoned / acquired)
- Save to `docs/station-f/_agent-examples-research.md`

```markdown
# Agent examples research — for Station F slides A-32, A-33, A-34

## OpenClaw (slide A-32)
- **What it is**: <1 sentence>
- **Headline number**: <e.g. "315K+ GitHub stars in 4 months", verify from current data>
- **Distinct angle**: <vs Claude Code: open-source, vs MiroFish: focused on personal use>
- **Current status**: <e.g. "Founder Peter Steinberger acqui-hired by OpenAI Q1 2026 per Arms Race PDF — verify">
- **Citations**: <URL + verbatim quote each>

## MiroFish (slide A-33)
[same template]

## AutoResearch (slide A-34)
[same template — Karpathy GitHub repo + his viral writeup]
```

- [ ] **Step 5: Verify both research files**

```bash
wc -w /home/ezalos/42/Markdowns2Teach/docs/station-f/_qwen3-quantization-research.md /home/ezalos/42/Markdowns2Teach/docs/station-f/_agent-examples-research.md
```

Expected: each ≥600 words. Every numeric claim has a URL.

---

## Phase 2 — PaperBanana batch (background, ~70 min wall time)

### Task 4: Draft 11 PaperBanana inputs and kick off the batch

**Files:**
- Create: `paperbanana/inputs/01-inference-econ.txt` through `11-metr-time-horizon.txt`
- Run: `uvx paperbanana generate ...` × 11 (in background batches of 3)
- Output: `paperbanana/outputs/run_<id>/final_output.png` × 11

**Why:** 11 infographics are needed for slides across Deck A. PaperBanana takes ~5–10 min per generation at 7+ iterations. Run them in parallel batches so they're ready by the time we get to those slides.

- [ ] **Step 1: Confirm paperbanana is set up**

```bash
cd /home/ezalos/42/Markdowns2Teach
ls paperbanana/  # should exist
test -f .envrc && grep -E "GEMINI_API_KEY|GOOGLE_API_KEY" .envrc
# If GOOGLE_API_KEY isn't set: export GOOGLE_API_KEY="$GEMINI_API_KEY"
```

If the directory doesn't have an `inputs/` subdir, create it: `mkdir -p paperbanana/inputs paperbanana/outputs`.

- [ ] **Step 2: Draft input #1 — Inference economics (B → GB)**

Create `paperbanana/inputs/01-inference-econ.txt` with ~350 words describing what the diagram should show. Template:

```
Diagram: a clean educational infographic comparing the VRAM (GPU memory)
required to run large language models at different parameter counts and
quantization levels.

The X-axis shows model size in billions of parameters (7B, 13B, 32B, 70B, 110B).
The Y-axis shows VRAM required in gigabytes. Three plotted curves show the
memory requirement at FP16 (2 bytes per parameter), INT8 (1 byte per parameter),
and INT4 / AWQ (0.5 bytes per parameter).

Annotate the practical thresholds for common consumer and prosumer GPUs:
- RTX 4090 (24GB) — the upper limit for typical desktop self-hosting
- A100 40GB — typical professional single-GPU
- A100 80GB / H100 80GB — large single-GPU
- 8x H100 (640GB) — typical inference cluster

Highlight three sweet-spot points where a popular model size crosses a
specific GPU's memory ceiling: Qwen3-32B at INT4 fits a single RTX 4090
(roughly 16GB after quant), Llama 3.1 70B at INT4 fits an A100 80GB,
and Qwen3-32B at FP16 needs an A100 80GB.

Style: clean academic / NeurIPS-paper aesthetic, light background, three
distinct line colors for the three precision levels, callout boxes for
the GPU thresholds. Avoid clutter, prefer clear labels over a legend.

Title: "GPU memory required by model size and quantization"
Subtitle: "FP16 vs INT8 vs INT4 — where each model fits"
```

- [ ] **Step 3: Draft inputs #2 through #11**

Create the remaining 10 input files. Each should be ~300 words, describing a clear diagram. Use the table from the spec (`docs/superpowers/specs/2026-04-13-station-f-revisions-design.md` § "PaperBanana batch") for topic + caption seeds. For each:
- File: `paperbanana/inputs/0N-<short-name>.txt`
- ~300 words of methodological description (what the diagram shows, what to label, what visual style)

The 10 remaining briefs:
- `02-six-components.txt` — six components of a coding agent (circular diagram, six numbered nodes around the model in the center: Live Repo Context, Prompt Shape + Cache Reuse, Tools + Permissions, Context Compaction, Session Memory, Bounded Subagents)
- `03-repo-context.txt` — workspace summary collection (agent reading Git state + AGENTS.md + repo layout, single output: a "stable facts" object)
- `04-prompt-prefix.txt` — stable prefix + cache reuse (timeline of agent turns, showing prefix stays cached across turns while session-state varies)
- `05-permission-levels.txt` — 5-level permission system (hierarchical pyramid or matrix: auto-allow → notify → confirm → human-approval → blocked, with example tool actions per level)
- `06-context-compaction.txt` — three compaction strategies (clip oversized, summarize older transcript, dedupe repeated reads — illustrated as before/after of a context window)
- `07-memory-pt1.txt` — working memory vs full transcript (two on-disk JSON files: one small "what matters now", one large append-only history)
- `08-memory-pt2.txt` — three-layer memory + autoDream (MEMORY.md index → topic files → session transcripts, with autoDream as a consolidation arrow)
- `09-swe-bench-trajectory.txt` — SWE-bench Verified score-vs-time chart (X = quarter from 2024-Q1 to 2026-Q1, Y = top score, multiple model lines, saturation plateau visible)
- `10-infrastructure-moat.txt` — closing visual: a stack diagram showing model-layer at the bottom (commoditizing) and the "moat" layers above it (harness, protocol, governance, safety)
- `11-metr-time-horizon.txt` — METR time-horizon: log-scale Y axis (task length agents can complete autonomously, in minutes), X axis = year 2019 to 2026, doubling curve every 7 months. **First-preference fallback**: if METR's published chart turns out to have permissive licensing (Step 7 of Task 2), use their original chart instead and skip generating this one.

- [ ] **Step 4: Run the first batch (inputs 1-3) in background**

```bash
cd /home/ezalos/42/Markdowns2Teach
source .envrc
mkdir -p paperbanana/outputs

# Background batch 1
nohup uvx paperbanana generate -i paperbanana/inputs/01-inference-econ.txt \
  -c "GPU memory required by model size and quantization" -n 7 \
  > paperbanana/outputs/01.log 2>&1 &

nohup uvx paperbanana generate -i paperbanana/inputs/02-six-components.txt \
  -c "The six components of a coding agent" -n 7 \
  > paperbanana/outputs/02.log 2>&1 &

nohup uvx paperbanana generate -i paperbanana/inputs/03-repo-context.txt \
  -c "Live repo context: the agent's first read" -n 7 \
  > paperbanana/outputs/03.log 2>&1 &

wait
```

(`wait` blocks until all three background jobs finish — useful here if you want to gate the next batch on the first completing. Otherwise drop `wait` and start batches 2 and 3 immediately, but watch GPU/API rate-limits.)

- [ ] **Step 5: Run batches 2 and 3 the same way**

Same pattern as Step 4 for inputs 4-7, then 8-11. Each batch ~7-15 min wall time. Keep logs.

- [ ] **Step 6: After each batch completes, locate the outputs**

```bash
ls -lt paperbanana/outputs/run_*/final_output.png 2>/dev/null | head -15
```

Note the run-id directories so we can copy the right `final_output.png` to staged asset paths in Phase 3+.

- [ ] **Step 7: If a generation fails or quality is poor, re-run with more iterations**

```bash
# Bump to 15 iterations for any input that didn't produce a good output
nohup uvx paperbanana generate -i paperbanana/inputs/0X-<name>.txt \
  -c "<same caption>" -n 15 \
  > paperbanana/outputs/0X-retry.log 2>&1 &
```

---

## Phase 3 — Deck A surgery, sequential

These tasks must run in order — they reshape the same file. Each commits to source even though we won't `git commit` until the very end.

### Task 5: Drop banal slides + reorder section ordering (anatomy before orchestration)

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`

**Why:** Two slides (`s.04 What LLMs enable` and `s.08 The right model for the right task`) are dropped per spec. The agents-anatomy section (currently slides 16-21) moves to BEFORE the orchestration patterns section (currently slides 13-15). After this, all slides need renumbering.

- [ ] **Step 1: Read the current Deck A**

```bash
wc -l /home/ezalos/42/Markdowns2Teach/slides/station-f/A-state-of-the-field.md
grep -nE "^# [0-9]+ — " /home/ezalos/42/Markdowns2Teach/slides/station-f/A-state-of-the-field.md
```

Expected: ~503 lines, 25 numbered slide headings. Note the line numbers of slides 04, 08, 13-15, 16-21, 22.

- [ ] **Step 2: Delete the two dropped slides**

Remove the entire slide block (from its slide-divider `---` through the next `---`) for:
- Old slide `04 — What LLMs enable` (the `<!-- _class: img-right compact-table -->` slide with the use-case table and `assets/ng01/img-026.png`)
- Old slide `08 — The right model for the right task` (the cols-class slide with the pricing table — it was already partially neutered in earlier audit but still exists)

Use the Edit tool with the exact `---\n\n# 04 — ...` opening block as `old_string`.

- [ ] **Step 3: Move the anatomy section before orchestration**

Cut the entire anatomy block (currently old slides 16 through 21 — six components, components 1+2, tool access, compaction, memory, bounded subagents — plus the salvaged retry/resilience that we'll add later). Paste it just BEFORE the orchestration overview slide (current old slide 13, "The golden rule: start simple"). The agents-section header `<!-- _class: section --> # Agents` stays where it is (covers both anatomy and orchestration).

After this, the order inside the Agents section becomes:
1. What counts as an agent (old s.10)
2. Spectrum of agency (old s.11)
3. Think-Act-Observe loop (old s.12)
4. Six components anatomy (old s.16)
5. Components 1+2 (old s.17) — to be split
6. Component 3 tool access (old s.18) — to be image-rewritten
7. Component 4 compaction (old s.19)
8. Component 5 memory (old s.20) — to be split
9. Component 6 subagents (old s.21)
10. Golden rule + complexity ladder (old s.13)
11. Chaining + Routing (old s.14)
12. Parallelization + others (old s.15)
13. Examples (old s.23)
14. Takeaway (old s.25)

- [ ] **Step 4: Renumber every numbered slide heading sequentially**

After the moves and deletions, walk top to bottom and renumber so headings go `# 01 — ...`, `# 02 — ...`, `# 03 — ...` without gaps. Use `Edit` with `replace_all: false` on each unique heading. (Don't use `sed` — easy to corrupt the file).

After renumbering, expect the deck to now have ~21 numbered slides (was 25, dropped 2, no new slides added yet, 23 → 21 with re-merge of moved blocks).

- [ ] **Step 5: Build and verify**

```bash
cd /home/ezalos/42/Markdowns2Teach
bash scripts/check-citations.sh slides/station-f
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md
make build-station-f 2>&1 | tail -5
```

Expected: all green. Open `dist/html/station-f-A-state-of-the-field.html` in the browser and visually confirm: title slide intact, agents section flows def → anatomy → orchestration → examples, no broken images, sequential slide numbers.

---

### Task 6: Add the new Section 1 expansion slides (LLM direction batch)

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`
- Read: `docs/station-f/_metr-research.md`, `docs/station-f/_qwen3-quantization-research.md`

**Why:** Per spec, Section 1 (state of LLMs) expands from 6 slides (was 03/05/06/07/09 + a couple of intro) to 12 slides covering: benchmarks, METR autonomy, inference cost dropping, OS gap, context window growth, training cost, B→GB economics, quantization, Qwen3 sweet spot, HF naming, synthetic data, David-vs-Goliath.

This is THE biggest single content task. Do it in two sub-batches for executor sanity.

- [ ] **Step 1: Add the four "AI direction" slides between the existing Benchmarks slide and the existing Training cost slide**

Insert these four new slides in this exact order:

1. **METR — task autonomy doubling** (uses `_metr-research.md` content)
2. **Inference cost dropping** (uses Epoch AI's pricing-trends data — extract from `_arms-race-extract.md` §1 OS section + an Epoch URL search)
3. **Open-source closes the gap** (Devstral 2 SWE-bench numbers from `_arms-race-extract.md` + Gemma 4 release date)
4. **Context window growth** (Opus 4.6 1M tokens from `_arms-race-extract.md` §2 + Llama 4 / Gemini context-window verifications via Tavily)

Each new slide follows this structure:

```markdown
---

<!-- _class: img-right -->

# NN — <Title>

![bg right:55% contain](assets/<path-to-paperbanana-or-stock-image>)

- <Bullet 1 with concrete number> [1]
- <Bullet 2 with concrete number> [2]
- <Bullet 3 framing> [1]

> <One-sentence callout / takeaway>

<small>Sources : [1] [Authority](url) · [2] [Authority](url)</small>
```

For the METR slide specifically, the image is METR's published time-horizon chart (per Step 3 of Task 2's research) OR PaperBanana #11 (`paperbanana/.../11-metr-time-horizon`) as fallback. Reference whichever ends up being used.

For Inference Cost Dropping, the image is PaperBanana-able OR an Epoch AI screenshot — first preference is to embed Epoch's own published chart with attribution.

- [ ] **Step 2: Add the five "deployment economics" slides between Training cost and Synthetic data**

Insert in this order:
5. **Inference economics: B-params → GB-VRAM** — uses PaperBanana #1 (`01-inference-econ`) as the bg-right image
6. **Quantization tradeoffs** — text + small comparison table from `_qwen3-quantization-research.md`
7. **Qwen3-32B sweet spot** — citation from Qwen blog + Qwen3-32B HF model card
8. **Reading HF model names** — text-heavy slide, no image needed (use `<!-- _class: cols -->` for breakdown table on left, full example name on right)

(Synthetic data and David-vs-Goliath stay where they are after this batch.)

- [ ] **Step 3: Renumber all subsequent slides**

Walk top to bottom, renumber. After this batch, Deck A should have ~30 numbered slides.

- [ ] **Step 4: Build + verify after each sub-batch**

```bash
make build-station-f 2>&1 | tail -5
bash scripts/check-citations.sh slides/station-f
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md
```

If overflow on any new slide, switch its `<!-- _class: img-right -->` to `<!-- _class: img-right compact -->` or trim a bullet.

---

### Task 7: Anatomy section rebuild (5 → 9 slides via splits + image-dominant rewrite + paperbanana swaps + S22 salvage)

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`

**Why:** Per spec § "Anatomy of a coding agent (moved BEFORE orchestration) 9 sl". Major surgery on the components slides:
- s.16 (six-component overview) — keep, swap image to PaperBanana #2
- s.17 (Components 1+2) — split into TWO slides (s.19 Repo Context, s.20 Prompt Prefix), each with its own paperbanana
- s.18 (Tool Access) — minimize text, image-dominant rewrite
- NEW slide — 5-level Permission System (own slide + paperbanana)
- s.19 (Compaction) — replace LS image with PaperBanana #6
- s.20 (Memory) — split into TWO slides (memory-architecture + memory-leverage), each with paperbanana
- s.21 (Bounded Subagents) — keep, ADD retry/resilience content salvaged from old s.22
- s.22 (the leak in one slide) — DELETE; subagents-prompt-caching salvaged into memory part 2

- [ ] **Step 1: Update the six-components overview image**

Edit the existing slide `# NN — Anatomy of a coding agent: 6 components` to swap `assets/raschka/13-six-features-summary.png` → `assets/paperbanana/06-components.png`. Make sure the file exists at that path (copy from PaperBanana output dir before this step):

```bash
# Once PaperBanana batch 1 has produced output #2:
mkdir -p slides/station-f/assets/paperbanana
cp paperbanana/outputs/run_<id-of-#2>/final_output.png \
   slides/station-f/assets/paperbanana/06-components.png
```

- [ ] **Step 2: Split the Components 1+2 slide into two slides**

Replace the existing single cols-class slide with two image-right slides:

```markdown
---

<!-- _class: img-right -->

# NN — Component 1 — Live Repo Context

![bg right:55% contain](assets/paperbanana/repo-context.png)

- The agent collects **stable facts** about your workspace upfront [1]
- Git state, repo layout, AGENTS.md / CLAUDE.md conventions, recent test results
- "Fix the tests" is **not self-contained** — the meaning lives in the repo, not the prompt

> Founder takeaway: this is why a thin chat wrapper around GPT-5 doesn't beat Claude Code. The harness reads your project for you.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# NN+1 — Component 2 — Stable Prompt Prefix + Cache Reuse

![bg right:55% contain](assets/paperbanana/prompt-prefix.png)

- Instructions + tool list + repo summary form a **stable prompt prefix** [1]
- Reused across every turn via **prompt caching** — same bytes, ~10× cheaper, ~2× faster
- Only session state (recent transcript + newest user request) changes turn-to-turn

> The cheap-but-stable part stays cheap. The new-but-small part stays small. That's how you make 100-turn sessions affordable.

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>
```

Stage the paperbanana images first (same `cp` pattern as Step 1).

- [ ] **Step 3: Rewrite the Tool Access slide as image-dominant**

Replace the existing tool-access slide with a minimal-text image-dominant version. Use `<!-- _class: img-right -->` with `bg right:65%` (more space for image):

```markdown
---

<!-- _class: img-right -->

# NN — Component 3 — Tool Access

![bg right:65% contain](assets/latent-space/01-tools-list.png)

- Tools = the line between **chat** and **agency** [1]
- Claude Code ships with **~18 named tools** [2]
- Validated before execution — typed inputs, path checks, optional approval gate

> The harness gives the model less freedom — and that's exactly why it ships. [1]

<small>Sources : [1] [Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>
```

The image stays the Latent Space tools-list (which is the strongest visual we have for this).

- [ ] **Step 4: Add a NEW dedicated 5-Level Permission System slide right after Tool Access**

```markdown
---

<!-- _class: img-right -->

# NN — The 5-level permission system

![bg right:55% contain](assets/paperbanana/permissions.png)

- Tools aren't yes/no — they live on a **permission spectrum** [1]
- Level 1 — auto-allow (read-only operations)
- Level 2 — notify (write to working directory)
- Level 3 — confirm (write outside, network calls)
- Level 4 — human-approval (destructive operations, rm, push)
- Level 5 — blocked (dangerous patterns: rm -rf /, etc.)

> The permission system is what lets you sleep while Claude Code refactors overnight.

<small>Sources : [1] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>
```

Levels 1-5 above are inferred from the Latent Space article structure. **VERIFY** the exact level definitions from the LS archive at `docs/station-f/sources/latent-space-claude-code-leak/README.md` § "Named artifacts from the leak" before committing.

- [ ] **Step 5: Replace the Compaction slide image**

Edit the existing Compaction slide and swap `assets/latent-space/05-compaction-types.png` → `assets/paperbanana/compaction.png`. The Latent Space original is hard to read; PaperBanana #6 redraws it from the OCR'd info.

```bash
cp paperbanana/outputs/run_<id-of-#6>/final_output.png \
   slides/station-f/assets/paperbanana/compaction.png
```

- [ ] **Step 6: Split Memory into two slides**

Replace the existing single Memory slide with two:

```markdown
---

<!-- _class: img-right -->

# NN — Component 5 — Memory part 1: architecture

![bg right:55% contain](assets/paperbanana/memory-pt1.png)

- Two storage layers, both on-disk JSON [1]:
  - **Working memory** — distilled, small, "what matters now"
  - **Full transcript** — every turn, append-only, durable, resumable
- Working memory feeds into the next prompt; transcript serves audit + replay

<small>Sources : [1] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>

---

<!-- _class: img-right -->

# NN+1 — Component 5 — Memory part 2: leverage

![bg right:55% contain](assets/paperbanana/memory-pt2.png)

- Claude Code's leaked architecture: **three layers** [1]
  - `MEMORY.md` index → topic files → session transcripts
- **autoDream** consolidation mode merges, dedupes, prunes contradictions
- **Subagents share parent's prompt cache via fork pattern** — parallelism without re-paying context cost [2]
- Founder leverage: write a thoughtful `CLAUDE.md` once, get its benefit on every session

<small>Sources : [1] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak) · [2] [Raschka — bounded subagents](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>
```

This is where the salvaged "subagents-use-prompt-caching" content from old s.22 lands.

- [ ] **Step 7: Modify Bounded Subagents to add retry/resilience**

Edit the existing Component 6 (Bounded Subagents) slide. Add 1-2 bullets for retry/resilience (the other piece salvaged from old s.22):

```markdown
---

<!-- _class: img-right -->

# NN — Component 6 — Bounded Subagents + resilience

![bg right:55% contain](assets/raschka/12-bounded-subagent.png)

- Delegation parallelizes subtasks: "which file defines X?", "why is this test failing?" [1]
- Hard part isn't *spawning* subagents, it's **binding** them — enough context to work, tight enough to not explode [1]
- Techniques: read-only mode, recursion depth limits, task scoping
- The leaked architecture also reveals **explicit retry + exponential-backoff resilience** at the runtime layer [2]

> "The tricky design problem is not just how to spawn a subagent but also how to bind one :)." — Raschka [1]

<small>Sources : [1] [Raschka](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent) · [2] [Latent Space — CC source leak](https://www.latent.space/p/ainews-the-claude-code-source-leak)</small>
```

- [ ] **Step 8: Delete old slide 22 ("The leak in one slide") entirely**

Remove the whole slide block for the old "leak in one slide" slide (its content has now been absorbed into Memory part 2 and Bounded Subagents).

- [ ] **Step 9: Renumber + verify**

```bash
# After all the splits and adds, renumber sequentially.
# Then:
make build-station-f 2>&1 | tail -5
bash scripts/check-citations.sh slides/station-f
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md
```

After this task, Deck A should have ~30 → ~38 numbered slides.

---

### Task 8: Orchestration patterns rebuild (add Anthropic illustrations + concrete examples)

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`
- Possibly create: `slides/station-f/assets/anthropic/` (download Anthropic's published SVGs)

**Why:** Per Louis: "S14 + S15: missing the 2 original illustrations, and missing concrete example." The Anthropic Building Effective Agents post publishes SVG diagrams for each pattern that we should embed (with attribution).

- [ ] **Step 1: Fetch Anthropic's published pattern diagrams**

The diagrams live on https://www.anthropic.com/research/building-effective-agents. Use Tavily extract or WebFetch to enumerate the image URLs. We want diagrams for: Prompt Chaining, Routing, Parallelization (Sectioning + Voting), Orchestrator-Workers, Evaluator-Optimizer.

```bash
mkdir -p slides/station-f/assets/anthropic
# Download each SVG/PNG via curl. Example pattern:
# curl -sL <image-url> -o slides/station-f/assets/anthropic/01-chaining.png
```

If Anthropic's diagrams aren't directly downloadable (some Substack-style images are CDN-served): screenshot them manually OR fall back to PaperBanana for redraws.

- [ ] **Step 2: Rebuild the Chaining + Routing slide**

Replace the existing combined cols-class slide with two `<!-- _class: img-right -->` slides — one for Chaining, one for Routing. Each has Anthropic's diagram on the right + concrete startup-flavored example on the left:

```markdown
---

<!-- _class: img-right -->

# NN — Pattern 1: Prompt Chaining

![bg right:55% contain](assets/anthropic/01-chaining.png)

- Sequential LLM calls, each consumes the previous output [1]
- **Concrete example**: support email triage
  1. Classify the email's intent (refund / bug / complaint)
  2. Extract the key facts (order id, dates, customer mood)
  3. Draft a response in the support team's voice
  4. Gate-check before sending: does the response answer the original ask?

> Covers the majority of business workflows. Start here.

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# NN+1 — Pattern 2: Routing

![bg right:55% contain](assets/anthropic/02-routing.png)

- Classify the input, route to a specialized handler [1]
- **Concrete example**: customer-support model selection
  - Simple FAQ → cheap LLM ($0.06/M tokens)
  - Complex case → premium LLM ($15/M tokens)
  - Anything escalation-flagged → human agent
- Optimizes **cost AND quality simultaneously** — the simplest multi-model pattern that pays back

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>
```

- [ ] **Step 3: Rebuild Parallelization + Orchestrator-Workers**

Same pattern, two slides:

```markdown
---

<!-- _class: img-right -->

# NN — Pattern 3: Parallelization

![bg right:55% contain](assets/anthropic/03-parallelization.png)

- *Sectioning*: independent subtasks run in parallel (e.g. legal + financial + technical contract review)
- *Voting*: same task, multiple independent runs, majority wins
- **Concrete example**: 3 independent LLM judges score a generated marketing copy; ship if 2/3 agree
- 2–3× cost; use when **speed** or **reliability** beats raw cost

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# NN+1 — Pattern 4: Orchestrator-Workers

![bg right:55% contain](assets/anthropic/04-orch-workers.png)

- A central LLM **dynamically decomposes** the task at runtime
- Delegates each piece to a specialized worker, then synthesizes the result
- **Concrete example**: refactor a multi-file PR
  - Orchestrator reads the diff, plans the migration
  - Workers each rewrite one file (parallel)
  - Orchestrator runs the test suite, reconciles failures
- The agentic IDE pattern (Cursor, Cline, etc.)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>
```

- [ ] **Step 4: Add an own slide for Evaluator-Optimizer**

```markdown
---

<!-- _class: img-right -->

# NN — Pattern 5: Evaluator-Optimizer

![bg right:55% contain](assets/anthropic/05-eval-opt.png)

- Generator + Evaluator loop, iterating until the quality bar is met [1]
- **Concrete example**: generate a sales email
  - Generator drafts the email
  - Evaluator scores tone, CTA strength, brand-voice fit
  - Loop until score ≥ threshold OR circuit-breaker (3-5 rounds max)
- Always add a circuit breaker — otherwise you've built an infinite-cost machine

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>
```

- [ ] **Step 5: Build + verify**

```bash
make build-station-f 2>&1 | tail -5
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md
```

After this task, Deck A should be ~38 + 3 = ~41 numbered slides (we went from 3 orchestration slides to 5).

---

### Task 9: Agents-in-the-wild — split into 4 deep-dive slides

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`
- Read: `docs/station-f/_agent-examples-research.md`

**Why:** Per spec, replace the current single multi-bullet slide with 4 separate slides — Claude Code (kept), OpenClaw (deep-dive), MiroFish (deep-dive), AutoResearch (deep-dive).

- [ ] **Step 1: Keep Claude Code slide**

The existing `# NN — Agents in the wild: Claude Code` slide stays. Confirm its citation `[1] Anthropic` deep-links to the actual Claude Code page (currently anthropic.com root — upgrade to `https://www.anthropic.com/claude/claude-code` or similar).

- [ ] **Step 2: Replace the combined "OpenClaw / MiroFish / AutoResearch" slide with three slides**

Use the research from `_agent-examples-research.md`. Each slide follows this template:

```markdown
---

<!-- _class: img-right -->

# NN — Agents in the wild: <Name>

![bg right:55% contain](assets/<image-path>)

- **What it is**: <1 sentence>
- **Headline number**: <stars / users / ARR / verifiable metric>
- **Distinct angle**: <vs the others — open vs closed, focus area, license>
- **Why founders care**: <1 takeaway>

> <Optional pull-quote from the project>

<small>Sources : [1] [<Authority>](url) · [2] [<Authority>](url)</small>
```

For OpenClaw, source the founder's blog or the Latent Space article + GitHub stats (verify current numbers).

For MiroFish, source `docs/station-f/sources/mirofish/README.md` (already archived) + a fresh fetch for star count.

For AutoResearch, source Karpathy's GitHub (https://github.com/karpathy/autoresearch or his nanoGPT discussion) + his viral X post.

Image options per slide:
- OpenClaw: from Latent Space images OR a logo fetched from the GitHub repo
- MiroFish: from `docs/station-f/sources/mirofish/images/MiroFish_logo_compressed.jpeg`
- AutoResearch: a code-snippet screenshot OR a small chart of "experiments per hour"

- [ ] **Step 3: Build + verify**

```bash
make build-station-f 2>&1 | tail -5
bash scripts/check-citations.sh slides/station-f
```

After this task, Deck A should be ~41 + 2 = ~43 numbered slides (was 1 example slide, now 4).

---

### Task 10: Build the new Frontier section (9 slides)

**Files:**
- Modify: `slides/station-f/A-state-of-the-field.md`
- Read: `docs/station-f/_arms-race-extract.md`

**Why:** Per spec § Frontier. End-of-A climax: 7 battlegrounds (in 2 slides), decisive breakthroughs, lab investment, 4 benchmark deep-dives (SWE-bench, Terminal-Bench, OSWorld, GAIA), scaffolding-as-moat thesis.

For citations: per spec, use **primary sources** — for each numerical claim, search for the actual primary URL (Anthropic blog, OpenAI blog, METR report, vals.ai, Epoch AI). The Arms Race PDF stays as research input only, NEVER cited in a slide footer. If a claim has no findable primary source after one search, drop the claim.

- [ ] **Step 1: Add a section divider before the new Frontier section**

```markdown
---

<!-- _class: section -->

# Frontier — what's next
```

Place this just before the existing Takeaway slide (which is the final numbered slide).

- [ ] **Step 2: Add Frontier slide #1 — 7 battlegrounds part 1 (4 of 7)**

Use `<!-- _class: cols -->` to fit 4 battlegrounds in a 2x2 grid:

```markdown
---

<!-- _class: cols -->

# NN — 7 battlegrounds (1/2)

<div class="left">

**Coding agents** [1]
- Claude Code ARR ~$2.5B (early 2026)
- OpenAI Codex ~2M weekly users, +70% MoM

**Computer / GUI agents** [2]
- GPT-5.4 first to exceed human OSWorld baseline
- Project Mariner 83.5% on WebVoyager

</div>
<div class="right">

**MCP / protocol** [3]
- Anthropic donated MCP to AAIF (Linux Foundation) Dec 2025
- 10,000+ indexed MCP servers, integrated across ChatGPT/Cursor/Gemini/Copilot

**Multi-agent orchestration** [4]
- 1,445% surge in enterprise inquiries (Gartner)
- Microsoft Agent Framework 1.0 RC, Magentic UI, LangChain Deep Agents

</div>

<small>Sources : [1] [Anthropic Claude Code](url) · [2] [OpenAI GPT-5.4 announcement](url) · [3] [Anthropic MCP donation](url) · [4] [Gartner / MS Agent Framework](url)</small>
```

For each `(url)` placeholder, search Tavily for the primary source. If any can't be found, soften the claim or drop it.

- [ ] **Step 3: Frontier slide #2 — 7 battlegrounds part 2 (3 of 7)**

Same pattern, `<!-- _class: cols-3 -->` for the remaining three:

```markdown
---

<!-- _class: cols-3 -->

# NN — 7 battlegrounds (2/2)

<div class="left">

**Enterprise agents** [1]
- Microsoft Agent 365 GA May 1, $15/user/mo
- AWS Bedrock AgentCore GA Mar 31
- Cohere North runs on 2 GPUs (air-gapped)

</div>
<div class="center">

**Safety & alignment** [2]
- Task autonomy doubling every 7 mo (3× Moore's Law) — Bengio-led report
- Anthropic A3 (Automated Alignment Agent) open-sourced
- OpenAI acquired Promptfoo (used by 25%+ of F500)

</div>
<div class="right">

**OSS vs proprietary** [3]
- Meta acquired Manus (Singapore) for >$2B
- Devstral 2 — top open-weight at 72.2% SWE-bench Verified
- Gemma 4 (Apache 2.0) on-device agentic
- OpenClaw security scandal: 12% of skills had vulnerabilities

</div>

<small>Sources : [1] [Microsoft Agent 365 announcement](url) · [2] [International AI Safety Report 2026](url) · [3] [Meta Manus deal](url) · [Mistral Devstral 2](url)</small>
```

- [ ] **Step 4: Frontier slide #3 — Decisive breakthroughs (Q1 2026)**

```markdown
---

<!-- _class: compact -->

# NN — Decisive breakthroughs (Q1 2026)

| Lab | Product | What changed | Date |
|-----|---------|--------------|------|
| **OpenAI** | GPT-5.4 | Native desktop+browser control, 75.0% OSWorld (>72.4% human) [1] | 5 Mar 2026 |
| **Anthropic** | Claude Opus 4.6 | Native 1M-token context, 14.5h task horizon, lowest prompt-injection rate (4.7%) [2] | 5 Feb 2026 |
| **Google** | Gemini 3.1 Pro | Terminal-Bench 2.0 leader (78.4%), $2/$12 per 1M tokens [3] | 19 Feb 2026 |
| **Microsoft** | Copilot Cowork | Built on Anthropic Claude (not OpenAI) — signal of $30B Azure-Anthropic deal [4] | Mar 2026 |

> "Every 60 days, there's a new king of the hill." — Microsoft CMO Jared Spataro

<small>Sources : [1] [OpenAI GPT-5.4](url) · [2] [Anthropic Opus 4.6](url) · [3] [Google Gemini 3.1](url) · [4] [Microsoft Copilot Cowork](url)</small>
```

- [ ] **Step 5: Frontier slide #4 — Lab investment landscape**

```markdown
---

# NN — Lab investment landscape

- **OpenAI**: $122B funding round @ **$852B valuation** (closed Mar 31 2026) [1]
- **Anthropic ↔ Microsoft**: $30B Azure compute deal (reshapes MS AI stack) [2]
- **Meta → Manus**: $2B+ acquisition — buying an *execution layer*, not a model [3]
- **Cursor**: $1B ARR @ $29.3B valuation [4]
- **Claude Code**: ~$2.5B ARR (doubled since January) [5]
- Tracxn: **1,040+ active agentic AI companies, $20.8B cumulative funding** [6]

> The infrastructure layer is where the money is going.

<small>Sources : [1] [<primary>](url) · [2] [<primary>](url) · [3] [<primary>](url) · [4] [<primary>](url) · [5] [<primary>](url) · [6] [Tracxn](url)</small>
```

- [ ] **Step 6: Frontier slides #5-8 — 4 benchmark deep-dives**

Per spec: SWE-bench, Terminal-Bench, OSWorld, GAIA. Each follows this template:

```markdown
---

<!-- _class: img-right -->

# NN — Benchmark deep-dive: <Name>

![bg right:55% contain](assets/<paperbanana-or-fetched-chart>.png)

- **What it measures**: <1 sentence>
- **Concrete example task**: <verbatim example or "[describe representative task]">
- **Current SOTA (Q1 2026)**: <leader + score> [1]
- **Trajectory**: <perf-vs-time bullet — "saturated at X" / "doubled in 12 months" / etc.>
- **Founder takeaway**: <why this matters for product decisions>

<small>Sources : [1] [<Bench publisher / leaderboard>](url) · [2] [<perf-trajectory source — e.g. vals.ai>](url)</small>
```

For SWE-bench, the perf-vs-time chart is PaperBanana #9. For the others, embed primary-source charts (METR for time-horizon if used, vals.ai or papers' own charts) OR text-only if no chart available.

Specific numbers from `_arms-race-extract.md` § 4 — verify each against the primary source before pasting (the PDF itself is lead-gen, not citation).

- [ ] **Step 7: Frontier slide #9 — Scaffolding > model thesis (closer)**

```markdown
---

<!-- _class: img-right -->

# NN — Infrastructure is the new moat

![bg right:55% contain](assets/paperbanana/infrastructure-moat.png)

- Six frontier models cluster within **1.3 points on SWE-bench Verified** [1]
- Same model + different harness = **10–22 point swing** in score (Claude Opus 4.5: 45.9% → 55.4% on SWE-bench Pro) [2]
- Grok 4 self-reports 72-75%; controlled measurement: **58.6%** [2]
- Meta's $2B Manus acquisition: bought the **execution layer**, not the model
- The race shifted from intelligence to infrastructure — harness engineering, protocol integration, governance, safety

> "Better models alone won't get agents to production." — Harrison Chase, LangChain

<small>Sources : [1] [<SWE-bench leaderboard>](url) · [2] [vals.ai harness study](url)</small>
```

- [ ] **Step 8: Update the existing Takeaway slide**

The current closing slide says "the model is not the product, the system is" — keep this thesis but reference back to the new Frontier section's evidence:

```markdown
---

<!-- _class: highlight -->

# NN — Takeaway: model vs harness

- Vanilla LLMs are **converging in raw capability** (1.3-point spread on SWE-bench) [1]
- The harness is the distinguishing factor [2]
- Founder implication: **a thin wrapper over GPT-5 is not your moat.** The system around the model is.

> "The harness can often be the distinguishing factor that makes one LLM work better than another." — Raschka [2]

<small>Sources : [1] [<SWE-bench leaderboard>](url) · [2] [Raschka — Components of a Coding Agent](https://magazine.sebastianraschka.com/p/components-of-a-coding-agent)</small>
```

- [ ] **Step 9: Renumber + verify**

```bash
make build-station-f 2>&1 | tail -5
bash scripts/check-citations.sh slides/station-f
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md
```

Final Deck A slide count: ~44 numbered + title + 2 section dividers ≈ 47 sections.

---

## Phase 4 — Deck B small edits (single task)

### Task 11: Reorder + remove + add risk-categories slide

**Files:**
- Modify: `slides/station-f/B-building-with-ai.md`

- [ ] **Step 1: Swap B-05 and B-06**

Current:
- B-05 = MVP patterns table
- B-06 = Building MVP — 3 ingredients

Target:
- B-05 = Building MVP — 3 ingredients
- B-06 = MVP patterns table

Read both slide blocks and swap their numbered headings (`# 05 — ...` ↔ `# 06 — ...`) and reorder them in the file. After swap: hypothesis-first ingredients comes BEFORE the table-of-patterns.

- [ ] **Step 2: Delete the "Prompting → RAG → Fine-tuning" slide**

Remove the entire slide block for current B-09 (the progression table with `assets/infographics/tool-decision_run_*.png`). It's redundant given Deck A now has the cost / quantization / Qwen3 sweet-spot slides.

- [ ] **Step 3: Insert a new "EU AI Act — 4 risk categories" slide before the timeline slide**

Right before the existing `# 14 — EU AI Act: the one date` slide, add:

```markdown
---

<!-- _class: compact -->

# 13 — EU AI Act — the 4 risk categories

| Category | Examples | What's required |
|----------|----------|-----------------|
| **Prohibited** | Social scoring, real-time biometric surveillance, subliminal manipulation | Banned outright [1] |
| **High-risk** | Recruitment/HR scoring, credit scoring, exam grading, medical devices, critical infra | Conformity assessment + registration + human oversight + ongoing monitoring [1] |
| **Limited risk** | Chatbots, deepfakes, emotion recognition | Transparency obligations (must disclose AI involvement) [1] |
| **Minimal risk** | Spam filters, AI in video games, recommender systems | No specific obligations (default for most products) [1] |

> If your product touches **HR, credit, health, or critical infra**, you're high-risk. The next slide is your deadline.

<small>Sources : [1] [EU AI Act — official summary](https://artificialintelligenceact.eu/high-level-summary/)</small>
```

Verify the URL resolves and is up-to-date. Alternative authoritative source: `https://eur-lex.europa.eu/eli/reg/2024/1689` (already in our authority map at Tier 1).

- [ ] **Step 4: Renumber Deck B**

After insert + delete, walk top to bottom and renumber so headings go sequentially. Final Deck B should have ~16 numbered slides + title + close = ~18 sections.

- [ ] **Step 5: Build + verify**

```bash
make build-station-f 2>&1 | tail -5
bash scripts/check-citations.sh slides/station-f
node scripts/check-overflow-visual.js slides/station-f/B-building-with-ai.md
```

---

## Phase 5 — PaperBanana integration

### Task 12: Stage all PaperBanana outputs into slides/station-f/assets/paperbanana/ and verify references

**Files:**
- Read: `paperbanana/outputs/run_*/final_output.png`
- Create: `slides/station-f/assets/paperbanana/*.png`

**Why:** The slide editing tasks above referenced paths like `assets/paperbanana/06-components.png` BEFORE the actual files existed. This task reconciles: it copies the best PaperBanana output for each input into the staged path, and verifies every slide image-reference resolves.

- [ ] **Step 1: Inventory all PaperBanana runs**

```bash
cd /home/ezalos/42/Markdowns2Teach
ls -la paperbanana/outputs/run_*/final_output.png 2>/dev/null
ls -la paperbanana/outputs/*.log 2>/dev/null
```

For each input (01..11), identify which run-id produced the best output. If two runs exist for the same input (initial + retry), pick by visual quality.

- [ ] **Step 2: Stage best outputs into slides/station-f/assets/paperbanana/**

```bash
mkdir -p slides/station-f/assets/paperbanana
# Per-input copy with descriptive names matching what slides reference:
cp paperbanana/outputs/run_<id-01>/final_output.png slides/station-f/assets/paperbanana/inference-econ.png
cp paperbanana/outputs/run_<id-02>/final_output.png slides/station-f/assets/paperbanana/components-overview.png
cp paperbanana/outputs/run_<id-03>/final_output.png slides/station-f/assets/paperbanana/repo-context.png
cp paperbanana/outputs/run_<id-04>/final_output.png slides/station-f/assets/paperbanana/prompt-prefix.png
cp paperbanana/outputs/run_<id-05>/final_output.png slides/station-f/assets/paperbanana/permissions.png
cp paperbanana/outputs/run_<id-06>/final_output.png slides/station-f/assets/paperbanana/compaction.png
cp paperbanana/outputs/run_<id-07>/final_output.png slides/station-f/assets/paperbanana/memory-pt1.png
cp paperbanana/outputs/run_<id-08>/final_output.png slides/station-f/assets/paperbanana/memory-pt2.png
cp paperbanana/outputs/run_<id-09>/final_output.png slides/station-f/assets/paperbanana/swe-bench-trajectory.png
cp paperbanana/outputs/run_<id-10>/final_output.png slides/station-f/assets/paperbanana/infrastructure-moat.png
cp paperbanana/outputs/run_<id-11>/final_output.png slides/station-f/assets/paperbanana/metr-time-horizon.png
```

(File names above are the contract — they must match what the slide tasks above reference.)

- [ ] **Step 3: Verify every paperbanana reference in slides resolves**

```bash
# Find every paperbanana reference and check the file exists
grep -E "assets/paperbanana/" slides/station-f/A-state-of-the-field.md slides/station-f/B-building-with-ai.md | \
  sed -E 's|.*assets/paperbanana/([^)]+).*|slides/station-f/assets/paperbanana/\1|' | \
  while read p; do test -f "$p" && echo "OK $p" || echo "MISSING $p"; done
```

Expected: every line says OK.

- [ ] **Step 4: If any input failed quality check, retry**

Re-run paperbanana with `-n 15` for any input where the output is unusable. Re-stage. Re-verify.

- [ ] **Step 5: Build with assets staged**

```bash
make build-station-f 2>&1 | tail -5
```

The Makefile automatically copies `slides/station-f/assets/` → `dist/html/assets/`. Open `dist/html/station-f-A-state-of-the-field.html` in a browser and visually confirm every paperbanana image renders correctly.

---

## Phase 6 — Citation audit + final ship

### Task 13: Citation pass + authority-map updates

**Files:**
- Read: `slides/station-f/A-state-of-the-field.md`, `B-building-with-ai.md`
- Modify (if new authorities surface): `docs/references/authority-map.md`, `docs/references/authority-map.yaml`

- [ ] **Step 1: List every URL in the new/modified slides**

```bash
grep -oE "https?://[^ )]+" slides/station-f/A-state-of-the-field.md slides/station-f/B-building-with-ai.md | sort -u > /tmp/station-f-urls.txt
wc -l /tmp/station-f-urls.txt
cat /tmp/station-f-urls.txt
```

- [ ] **Step 2: Spot-check liveness of new URLs**

For each URL added in Phase 3-5, fire a quick HEAD request:

```bash
while read url; do
  status=$(curl -sIL -o /dev/null -w "%{http_code}" "$url" 2>/dev/null)
  echo "$status $url"
done < /tmp/station-f-urls.txt | grep -vE "^(200|301|302) "
```

Any 4xx/5xx URL: either find the corrected primary source or replace with a more durable URL. Don't ship 404s.

- [ ] **Step 3: Run tier_lookup on every new domain**

```bash
grep -oE "https?://[^/ ]+" slides/station-f/A-state-of-the-field.md slides/station-f/B-building-with-ai.md | \
  sed -E 's|https?://(www\.)?||;s|/.*||' | sort -u | \
  while read d; do
    tier=$(python3 scripts/cite/tier_lookup.py "$d")
    echo "tier=$tier $d"
  done | grep -v "^tier=[1-4] "
```

Any domain returning `tier=null` or `tier=5`/`tier=6`: review whether to add it to the global authority map (per the previous polish-pass pattern). If a credible new publisher (e.g. METR's domain `metr.org`, or vals.ai), add it via the same `Edit` pattern used in the prior `docs/references/authority-map.{md,yaml}` updates. Keep `.md` and `.yaml` in sync — verify:

```bash
python3 scripts/cite/lint_authority_map.py
```

- [ ] **Step 4: Run the citation linter**

```bash
bash scripts/check-citations.sh slides/station-f
```

Expected: `OK: All data slides have source citations.` Fix any warnings before moving on.

---

### Task 14: Final build, overflow, visual, timing rehearsal

**Files:**
- Read: everything

- [ ] **Step 1: Full build**

```bash
make build-station-f 2>&1 | tail -10
```

Expected: HTML, PPTX, and PDF all generated for both decks. No errors.

- [ ] **Step 2: Overflow check**

```bash
node scripts/check-overflow-visual.js slides/station-f/A-state-of-the-field.md 2>&1
node scripts/check-overflow-visual.js slides/station-f/B-building-with-ai.md 2>&1
```

Expected: `OK: No overflow detected` for both. Fix any overflow by moving to `<!-- _class: compact -->` or trimming a bullet.

- [ ] **Step 3: Visual review in browser**

```bash
xdg-open dist/html/station-f-A-state-of-the-field.html 2>/dev/null || \
  echo "Open dist/html/station-f-A-state-of-the-field.html in your browser"
xdg-open dist/html/station-f-B-building-with-ai.html 2>/dev/null || \
  echo "Open dist/html/station-f-B-building-with-ai.html in your browser"
```

Walk every slide. Confirm:
- All paperbanana images render
- Tables don't overflow
- Citations footers render with proper spacing
- Section dividers are visually distinct
- Title slide intact
- New Frontier section flows narratively into the takeaway

- [ ] **Step 4: Slide count sanity**

```bash
echo "Deck A:"; grep -cE "^# [0-9]+ — " slides/station-f/A-state-of-the-field.md
echo "Deck B:"; grep -cE "^# [0-9]+ — " slides/station-f/B-building-with-ai.md
```

Expected: Deck A ~44, Deck B ~16.

- [ ] **Step 5: Timing rehearsal (manual)**

Read every slide aloud at presentation pace:
- Deck A target: 38 min
- Deck B target: 22 min
- Total: 60 min content

Note any slide that takes >90s to deliver — likely too dense. Either trim or split.

- [ ] **Step 6: Final build artifact check**

```bash
ls -la dist/html/station-f-*.html dist/pptx/station-f-*.pptx dist/pdf-full/station-f-*.pdf 2>&1
```

Expected: 6 files (2 HTML, 2 PPTX, 2 PDF), all freshly mtimed.

- [ ] **Step 7: Hand off — DON'T COMMIT**

Per Louis's standing rule, don't `git commit` unless he explicitly asks. Report status with:
- Final slide counts
- Anything that needed extra iterations (paperbanana retries, URL replacements)
- Anything still flagged as `needs-rework`
- Timing rehearsal verdict

---

## Self-review notes

After writing this plan, I checked it against the spec sections:

- ✅ Frontier section placement (end of Deck A) → Tasks 10
- ✅ S22 fate (drop, salvage to memory + bounded subagents) → Task 7 Steps 6-8
- ✅ All 11 PaperBanana inputs enumerated → Task 4
- ✅ All 13 NEW slides covered (METR, inference cost, OS gap, context window, B→GB, quantization, Qwen3, HF naming, 5-perm, Bounded+resilience, OpenClaw, MiroFish, AutoResearch, Frontier ×9) → Tasks 6-10
- ✅ All 11 existing slide edits → Task 7 + Task 8 + Task 9 Step 1
- ✅ Deck B 3 edits → Task 11
- ✅ PDF extract relocation → Task 1
- ✅ Research extracts (METR, Qwen3, agent examples) → Tasks 2-3
- ✅ Build + citation audit + overflow + authority-map sync → Tasks 13-14
- ✅ Section reorder (anatomy before orchestration) → Task 5

**Open from spec ("Open items requiring Louis's input")**:
- Concrete examples for orchestration patterns: defaulted to startup-flavored (support email triage, model routing, contract review, refactor-PR, sales email) per spec note. Louis can adjust during review.
- Per-paperbanana iteration counts: starting at 7, plan permits bumping to 15 on retry per Task 4 Step 7.

**Known gaps the plan EXPLICITLY relies on the executor to fill**:
- Anthropic illustration URLs (Task 8 Step 1) — must be discovered at execution time
- METR chart license (Task 2 Step 3) — must be discovered at execution time
- Per-claim primary sources for Frontier section (Tasks 10) — must be searched at execution time

These are NOT placeholders; they're research subtasks that the executor performs. Each has a search query template + a fallback strategy specified.
