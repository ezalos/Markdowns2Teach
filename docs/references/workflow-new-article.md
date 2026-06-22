# Workflow: write an article

<!-- ABOUTME: Phased workflow for producing a technical article / blog post — from scratch or from research. -->
<!-- ABOUTME: Covers scope, research/outline, draft, revise, visuals, pre-publish checklist, publish. References writing-standards.md. -->

## Which workflow to use?

| Situation | Workflow |
|-----------|----------|
| Write a single article on a topic you have direct experience with | **Part A** — From scratch |
| Turn a finished research/project log (notes, experiment data, repo) into an article | **Part B** — From research |
| Plan a multi-part series | Run Part A/B per part, then apply the **two-part strategy** (`writing-standards.md` §10) |

All writing conventions (titles, hooks, formatting, citations, reproducibility) live in **`writing-standards.md`**. This workflow references it without repeating the rules. The deep reference with data and worked examples is [great-medium-article.md](great-medium-article.md).

---

# Part A: From scratch — one article

## Phase 1: Scope (~15 min)

### 1.1 Define the takeaway

Answer in one sentence: **what will the reader be able to DO after this article?**

Examples:
- "Verify a TF→PyTorch migration is correct before trusting it"
- "Design a hyperparameter experiment that yields unbiased conclusions"

### 1.2 Pick the angle and audience

- Audience = ML engineers (default). Calibrate jargon accordingly (`writing-standards.md` §5).
- Pick the title formula family early (§1) — it shapes the article's promise.

### 1.3 Estimate length and read time

| Article type | Words | Read time |
|--------------|-------|-----------|
| Focused how-to / single technique | 1,500–2,500 | 6–10 min |
| Deep methodology / case study | 3,000–5,000 | 12–20 min |
| Series part | 3,000–5,000 each | 12–20 min each |

Target the 8–15 min sweet spot (`writing-standards.md` §11).

---

## Phase 2: Research & outline (~30–60 min)

### 2.1 Gather supporting material

| Need | Source |
|------|--------|
| Your own experimental data | Project logs, experiment tracker, repo — **strongest evidence** |
| Published benchmarks / papers | arXiv, official docs, HuggingFace |
| Framework / library behavior | Context7 (`resolve-library-id` → `query-docs`), official docs |
| External facts / stats | Tavily Search; verify the page with Tavily Extract |

Prefer **your own data** over citations over first-principles (`writing-standards.md` §5). Every numeric or factual claim needs a backing.

### 2.2 Build the outline

Write a section-by-section outline before drafting. Apply the narrative stack (`writing-standards.md` §3):

- **Article level**: Story Spine — context → problem → escalation → resolution → reader takeaway.
- **Section level**: one Gradual Discovery cycle per H2 — `problem → method → concrete example → pitfall`.
- **Within sections**: Progressive Disclosure — concept first, detail later.

For each section, note: the problem it opens with, the method/insight, the concrete example, the pitfall, and **the planned visual** (chart type per `writing-standards.md` §6).

### 2.3 Scope checkpoint

Before drafting, verify:

- [ ] One-sentence takeaway written (§1.1)
- [ ] Title formula chosen; 5–10 variations drafted (`writing-standards.md` §1)
- [ ] Every section maps to a Gradual Discovery cycle
- [ ] Every data claim has identified backing (own data / citation / first principles)
- [ ] At least one planned visual per ~75–100 words of dense content
- [ ] No orphan claim (number with no source)

---

## Phase 3: Draft

Apply `writing-standards.md` throughout. Drafting order that works:

1. **Hook first** (§2) — write the opening, read it aloud, confirm the 15-second test.
2. **Skeleton** — drop in all H2/H3 headings from the outline.
3. **Fill each cycle** — problem → method → example → pitfall, in Context → Story → Results form (§7). Include the messy middle.
4. **Code as you go** (§8) — paste real, tested snippets; annotate tensor dims; show diffs, not whole files.
5. **CTAs** (§9) — soft (start), contextual (mid), specific question (end).

Drafting reminders (all detailed in `writing-standards.md`):
- Paragraphs 2–3 sentences; bold the load-bearing 2–3 words (§4)
- Don't define fundamentals; do define methodology-specific terms on first use (§5)
- Leave `[VISUAL: …]` placeholders where charts go — produce them in Phase 5
- Mark unverified claims with `<!-- TODO: source needed -->`

---

## Phase 4: Revise (~30 min)

Self-edit passes, one concern per pass:

1. **Cut the padding** — every paragraph earns its place (`writing-standards.md` §5). Length from depth, not throat-clearing.
2. **Scan test** — read only headings + bold + first sentences. Does the article make sense? Fix the F-pattern (§4).
3. **Claim audit** — every number/fact backed; no "research shows" without a citation (§5).
4. **Highlightables** — ensure 3–5 standalone insight sentences exist (§9).
5. **Active voice & directness** — replace weak constructions (§5 table).
6. **Limitations** — explicitly acknowledge what the method doesn't cover (§5).

---

## Phase 5: Visuals

Produce every `[VISUAL: …]` placeholder from Phase 2/3. Apply `writing-standards.md` §6.

- **Pick the chart type** by intent (trend → line, categories → bar, interactions → heat map, comparison → table). Never pie charts.
- **Results visuals**: show variance/error bars, wall-clock time + accuracy together, hardware specs, progressive cumulative tables, training curves (not just endpoints).
- **Consistency**: same color = same thing across all figures; label every axis; readable on light + dark.
- **Reusable diagrams** (pipeline, workflow, parameter-space): the project's PaperBanana flow in `workflow-new-slides.md` Phase 5 can generate these — same CLI, just an article-appropriate caption.
- **Code screenshots / Gists**: for complex code Medium can't highlight natively, use a GitHub Gist (§4).

Target a visual break point every 75–100 words (counts code blocks, tables, pull quotes — not just images).

---

## Phase 6: Pre-publish checklist

The authoritative list is [great-medium-article.md](great-medium-article.md) Appendix C, mirrored as the quick version in `writing-standards.md` §13. Run it in full before publishing. Critical gates:

- [ ] Hook passes the read-aloud 15-second test
- [ ] Every code snippet has been **run** and works (with imports)
- [ ] Hyperparameters, software versions, seeds, hardware documented; repo linked
- [ ] Results show variance + wall-clock time + curves
- [ ] Title <60 chars + subtitle; 3–5 tags; preview image set
- [ ] Standalone value confirmed (no dependency on unwritten content)

---

## Phase 7: Publish & distribute

Apply `writing-standards.md` §11.

1. **Day 0**: publish on Medium (T-dropdown headings, tags, preview image, meta <160 chars). Share on X + LinkedIn with a real hook, not just the link.
2. **Day 0–2**: reply to every comment; post in r/MachineLearning, r/pytorch, Hacker News, relevant Discords.
3. **Day 7**: reshare with platform-specific framing.
4. **Ongoing**: link from future articles; update with new results.
5. **Influencers**: share directly with 3–5 ML-community people, with a personalized note.

---

# Part B: From research — turn a project log into an article

When the raw material already exists (experiment logs, a migration repo, tuning results), the work is selection and narrative, not discovery.

## 1. Pre-flight

- [ ] Skim the raw material — experiment data, repo history, notes
- [ ] Identify the **single takeaway** the data supports (Phase 1.1)
- [ ] Inventory the strongest evidence (best results tables, before/after diffs, training curves)
- [ ] Spot the **failures and dead ends** — these are the most valuable narrative (`writing-standards.md` §7)
- [ ] Decide single article vs series (if two distinct takeaways, lean series — §10)

## 2. Outline from the material

- Map the project's actual chronology onto the **Story Spine**: what you were doing → what broke → what you tried → what worked.
- Each major problem/solution pair becomes one **Gradual Discovery** H2.
- For results-heavy projects, plan a **progressive cumulative table** early (baseline → +A → +B → final).
- Use **subagents** to read large logs/repos and extract structured summaries — never load big files into the main context.

## 3. Extraction patterns

| Raw material | Article element |
|--------------|-----------------|
| Experiment results table | Progressive results table (`writing-standards.md` §6) |
| Before/after code in repo diff | Side-by-side code comparison (§8) |
| Failed approaches in your notes | The "messy middle" story per section (§7) |
| Config files / hyperparameters | Reproducibility table (§8) |
| Training logs | Summarized training curves — never raw logs (§6) |

## 4. Draft, revise, visuals, publish

Follow Part A Phases 3–7. The only difference is that evidence is already in hand — spend the saved time on narrative and on verifying every snippet still runs.

---

# Appendix: Quick reference card

```
┌─────────────────────────────────────────────────────────┐
│  SCOPE                                                   │
│  1. Takeaway: reader will be able to DO what?           │
│  2. Title formula + 5-10 variations                     │
│  3. Length: how-to 1.5-2.5k / deep 3-5k words           │
├─────────────────────────────────────────────────────────┤
│  RESEARCH & OUTLINE                                      │
│  Evidence: own data > citations > first principles       │
│  Narrative stack: Story Spine / Gradual Discovery /     │
│                   Progressive Disclosure                 │
│  Plan a visual per section                               │
├─────────────────────────────────────────────────────────┤
│  DRAFT                                                   │
│  Hook first (15s test) → skeleton → fill cycles →      │
│  tested code → CTAs (start/mid/end)                      │
├─────────────────────────────────────────────────────────┤
│  REVISE                                                  │
│  Cut padding · scan test · claim audit ·                │
│  highlightables · active voice · limitations            │
├─────────────────────────────────────────────────────────┤
│  VISUALS                                                 │
│  Chart by intent · variance+hardware+curves ·           │
│  consistent color · label axes · no pie charts          │
├─────────────────────────────────────────────────────────┤
│  PUBLISH                                                 │
│  Checklist (Appendix C) → publish → distribute          │
│  Day 0 / Day 0-2 / Day 7 / ongoing                      │
└─────────────────────────────────────────────────────────┘
```
