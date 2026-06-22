# Technical Writing Standards

<!-- ABOUTME: Single source of truth for all rules on writing technical articles / blog posts (Medium and beyond). -->
<!-- ABOUTME: Covers titles, hooks, narrative, formatting, depth, visuals, reproducibility, engagement, series, platform. -->

Distilled, actionable rules for writing great ML/technical articles. This is the writing analogue of `slide-creation-standards.md`. Deep rationale, data, and worked examples live in the full reference: [great-medium-article.md](great-medium-article.md).

---

## 1. Titles & Headlines

The title decides ~40% of the article's success before anyone reads a word. A poorly formatted title is also ineligible for Medium curation.

### Rules

- **Write 5–10 variations** before choosing. Never ship your first instinct.
- **Keep the main title 50–60 characters** to avoid feed/search truncation.
- **Front-load keywords**: "PyTorch Training Optimization: 7 Techniques…" beats "7 Techniques for Optimizing Your PyTorch Training…".
- **Use a strong subtitle** as a second hook (up to ~120 chars). Expand the promise; never repeat the title.
- **Choose a preview image that signals technical depth** — architecture diagrams, training curves, annotated code beat stock photos.

### Formulas that work

| Formula | Example |
|---------|---------|
| Number + Outcome | "7 PyTorch Optimizations That Cut Training Time by 8x" |
| How-To + Specific result | "How to Systematically Tune Any Deep Learning Model" |
| Problem + Fix | "Why Your PyTorch Model Trains Slower Than TF — And How to Fix It" |
| Counterintuitive claim | "The Hyperparameter You Tune Most Is Probably the Wrong One" |
| X Mistakes | "5 Mistakes ML Engineers Make When Migrating to PyTorch" |
| Story + Scale | "We Migrated 50K Lines from TF to PyTorch. Here's What Broke" |
| Comparison | "Grid Search vs Quasi-Random: What 200 Experiments Taught Us" |

Numbers add ~36% clicks; `[brackets]` on numbered titles add another ~38% (e.g. "5 Techniques [With Code]").

### Power words / red flags

- **Use sparingly**: *systematic, battle-tested, reproducible, step-by-step, practical, production-ready, from scratch, under the hood, deep dive, lessons learned.*
- **Avoid** (ML readers are allergic to hype): *ultimate, revolutionary, game-changing, hack, secret, insane, mind-blowing.*

Full cheat sheet: [great-medium-article.md](great-medium-article.md) Appendix B.

---

## 2. The Opening Hook

### The 15-second rule

Readers decide within ~15 seconds whether to keep reading. The opening is a **sales pitch, not a summary**. Read it out loud before shipping.

### Hook techniques (combine 2–3)

1. **Problem-focused** — name the reader's pain ("You've run 47 sweeps and accuracy hasn't budged…"). Most reliable for ML.
2. **Compelling statistic** — quantify a problem they feel.
3. **Curiosity gap** — withhold the key fact ("one step most engineers skip…").
4. **Scenario / drop into action** — "It's 2am. The run you launched 18 hours ago just diverged."
5. **Unexpected insight** — "Adam in PyTorch and TensorFlow are not the same optimizer."
6. **Engaging question** — invite the reader to think.
7. **Active / bold statement** — establish authority and scope.

### Never open with

- "In this article, we will explore…" (passive, generic)
- A textbook definition your audience already knows
- A long personal intro or credentials dump — earn authority through the content
- A disclaimer ("I'm not an expert but…")

---

## 3. Narrative Architecture

Three frameworks **layer on top of each other** — do not pick one.

```
ARTICLE-LEVEL: Story Spine (setup → problem → escalation → resolution)
  └── SECTION-LEVEL: Gradual Discovery cycles
        └── WITHIN SECTIONS: Progressive Disclosure (concept → detail)
```

### Story Spine (whole article)

Context → recurring problem → the one day it broke → consequences → escalation → resolution → new reality + what readers can do. Cast yourself as the character (see §7).

### Progressive Disclosure (within a section)

Reveal in layers: concept (what/why) → how it works → implementation detail → edge cases. Don't front-load every detail; introduce simply, let it breathe, then deepen. Readers who want the overview can stop; readers who want depth keep going.

### Gradual Discovery (the repeating unit)

```
Problem to Solve → Method Introduced → Concrete Example → Pitfalls & Limits → (Next Problem)
```

Each cycle is **self-contained** (value even if the reader stops) and the pitfalls section creates tension that pulls into the next cycle. This is the default section shape for technical articles.

---

## 4. Structure & Formatting

Readers **scan before they read** (F-pattern: headings, first sentences, bold text). Formatting is the roadmap that makes scanning productive.

### Rules

- **Paragraphs**: 2–3 sentences max. One idea per paragraph. White space is a feature.
- **Headings**: H2 = major sections (each answers one searchable question), H3 = sub-topics, H4 = sparingly.
- **Lists**: bullets for unordered, numbered for sequential/ranked steps.
- **Tables**: for comparisons and parameter summaries — ML readers love them.
- **Bold**: the 2–3 words that carry the meaning, not whole sentences. These are scan anchors.
- **Code blocks**: fenced + language tag, 10–30 focused lines. Longer code → show the critical section, link the rest.

### MECE

Organize H2 sections **Mutually Exclusive, Collectively Exhaustive**: no overlap, full coverage. Max **3–4 major points per section** before splitting into sub-sections.

### Medium specifics

- Use Medium's **T dropdown** for heading hierarchy (Title / Subtitle / Section), not manual bold.
- Title Case for H2, Sentence case for H3 and below — be consistent.
- `backtick` for inline code, parameter names, file paths.
- Medium has no native syntax highlighting — use GitHub Gists for complex code.
- `---` separator lines between major sections; pull quotes for key takeaways (readers highlight these).

---

## 5. Depth, Clarity & Credibility

### The long-form paradox

Articles of 3,000–10,000 words get the most shares — there's less competition in deep content. **Long ≠ padded.** Every paragraph earns its place; length comes from genuine depth, not throat-clearing.

### Jargon calibration

Audience = ML engineers. **Do not define fundamentals** (learning rate, Adam, SGD) — that's the #1 sign of a junior writer.

- **Do define** non-obvious, methodology-specific terms on first use (e.g. "scientific" vs "nuisance" parameters, "Halton sequences").
- **Do clarify** when you use a term in a non-standard way.
- **Use consistent terminology** — pick "sweep" or "search" and keep it throughout.

### No hand-waving

Every claim is backed by, in order of strength:

1. **Your own experimental data** (best — proves you did the work)
2. **Published papers / benchmarks** (credibility by association)
3. **First-principles reasoning** (acceptable — shows understanding)

**Never** write "It's well-known that…", "Experts agree…", or "Research shows…" without a specific citation or your own data.

### Active voice & directness

| Weak | Strong |
|------|--------|
| "It was observed that LR impacts convergence" | "We found the LR schedule directly impacts convergence" |
| "The model can be trained with mixed precision" | "Train with mixed precision — it halves memory with negligible accuracy loss" |
| "Consideration should be given to…" | "Consider…" |

### Acknowledge limitations

Stating what you don't know **increases** credibility. Flag where more work is needed rather than feigning universality. Sophisticated readers trust transparency.

---

## 6. Visual Strategy

### Chart-type guidance

| Visual | Use for |
|--------|---------|
| Architecture diagram | System overview, data flow |
| Flowchart | Decision processes, methodology steps |
| Table | Precise numerical comparisons, param → metric maps |
| Line chart | Trends over time/iterations (training/convergence curves) |
| Bar chart | Comparing discrete categories (model A/B/C, speedup per technique) |
| Heat map | Multi-dimensional parameter interactions |
| Code snippet | Implementation details, key diffs |
| Before/After | Impact demonstration (TF vs PyTorch, before/after optimization) |

**Never use pie charts** — ML audiences find them imprecise.

### The 75–100 word rule

Aim for a visual break point every **75–100 words** (~2x more shares than text-only). This counts code blocks, tables, diagrams, pull quotes, and callouts — not just images. A 4,000-word article ≈ 40–50 break points.

### Presenting experimental results

**Do:**
- Show **error bars / variance** across runs — point estimates are suspicious.
- Report **wall-clock time AND accuracy together** — speed without quality is meaningless.
- Specify **hardware** (GPU model, count, VRAM) — results aren't reproducible otherwise.
- Use **progressive results tables**: baseline → +technique A → +technique B → combined.
- Show **training curves**, not just final numbers — the trajectory reveals more.

**Don't:**
- Present untuned baselines as fair comparisons.
- Dump raw training logs (summarize).
- Show numbers without context on why they matter.

### Color & labels

- Color **encodes information**, never decorates. Keep coding consistent (e.g. always blue = PyTorch, orange = TF).
- Readable on light **and** dark backgrounds (Medium has dark mode).
- **Label every axis** — unlabeled axes are a cardinal sin.

---

## 7. Storytelling

Humans retain stories ~22x better than isolated facts. Wrap technical insight in narrative — without writing a novel.

### Author as character

You faced a real challenge → made mistakes → iterated → got measurable results → share what you learned. This reads as authentic; ML engineers can tell theory from real work.

### Context → Story → Results (per section)

1. **Context** — why it matters, the problem faced
2. **Story** — what you tried, what failed, what worked (include the messy middle)
3. **Results** — what you achieved, with data

**The messy middle is the most valuable part.** Readers buy your failure stories, not your success stories — that's where transferable knowledge lives.

### Second person

Use "you" to make the reader the protagonist: "When you compare curves, your instinct will be to adjust the LR. Resist it — the problem is in the optimizer defaults."

### Humor

Dry wit and self-deprecation build rapport ("…I briefly considered a career in carpentry"). It should punctuate the technical flow, never interrupt it. No "LOL training is so hard 😂".

---

## 8. Reproducibility & Code

Reproducible content is rare (~6% of conference presenters share code; >70% of researchers fail to reproduce others' work) and therefore highly valued.

### Reproducibility checklist (inline or linked)

| Element | Where |
|---------|-------|
| All hyperparameter values | Table in results |
| Hardware specs (GPU model/count/VRAM, CPU, RAM) | Footnote or dedicated section |
| Software versions (PyTorch, CUDA, key libs) | Top / prerequisites |
| Working, tested code | Inline snippets + linked repo |
| Random seeds | Code or config |
| Dataset details (size, splits, preprocessing) | Method section |
| Training / wall-clock time | Results table |
| Statistical reporting (variance across runs) | Results |

### Code quality

- **Working code only.** No pseudocode, no "left as an exercise." Readers will copy-paste-run; broken code destroys credibility instantly.
- **Short, focused snippets** (10–30 lines). Link the full implementation.
- **Annotate tensor dimensions** — the #1 confusion point.
- **Show the diff**, not the whole file. Before/after teaches more than the final version.

### Template for presenting code

```
[Brief: what this does and why]
[Code block — 10–30 lines, the key change]
[1–2 sentences on the non-obvious parts]
[Metrics: what this change achieved]
```

---

## 9. Engagement & CTAs

### Drive shares

- **Awe** is the #1 sharing emotion; "aha moment" content (new mental model) gets the most engagement.
- Aha moments come from: revealing hidden mechanisms, connecting disparate concepts, or quantifying intuition.

### CTAs at three points (mid-content CTAs convert ~121% higher than end-only)

- **Beginning (soft)**: set the value promise ("By the end you'll have a systematic framework — no more guessing").
- **Mid-content (contextual)**: "Try this on your own model before reading on."
- **End (direct)**: ask a **specific, answerable** question, not "what do you think?".

### Highlightable sentences

Deliberately craft 3–5 standalone, insight-dense lines readers will highlight (highlights are weighted by the algorithm). They must make sense without surrounding context, e.g. "A systematic methodology beats intuition not because intuition is wrong, but because it doesn't scale."

### Comments

Ask specific questions; respond within the first 48 hours — active discussion signals quality to the algorithm.

---

## 10. Two-Part Series Strategy

### Core rule: standalone value per part

**Each part must be valuable on its own** — readers may hit Part 2 first via search. Part 1 is a complete article that *also* sets up Part 2, never a teaser.

### Linking

- Navigation links at **both top and bottom** of each part.
- **Keyword-rich anchor text**, never "click here" or "Part 2".
- Part 1 bottom: "Continue to Part 2: [Title] →". Part 2 top: one-line recap of what Part 1 established + back-link.

### Transition

End Part 1 with **constructive tension** (a question Part 2 answers), not a cliffhanger: "We matched TF performance. But matching isn't the point — Part 2 covers how we surpassed it."

### Timing & cross-referencing

- Publish Part 2 within **1–2 weeks**; if longer, recap in the intro.
- Promote both when Part 2 launches (Part 1 gets a second traffic wave).
- Consistent formatting, visual style, and tone across both parts.

---

## 11. Platform & Algorithm Notes (Medium)

The algorithm rewards: **read time** (~265 wpm), **read ratio** (% who finish), **claps**, **highlights**, **responses**, **followers gained**.

### Practical

- **Tags**: 3–5, mixing broad (`Machine Learning`, `Deep Learning`) and specific (`PyTorch`, `Hyperparameter Tuning`, `MLOps`).
- **Meta description**: under 160 chars; complement the title, don't repeat it.
- **Read-time sweet spot**: 8–15 min (~2,000–4,000 words). Under 3 min reads shallow; over 20 min risks drop-off unless exceptional.
- **Publish timing**: Tue is highest-engagement; mornings (8–10am) in the target timezone; Mon–Wed for ML readers.

### Distribution (shares drop ~96% after 3 days)

1. **Day 0**: publish; share on X and LinkedIn with a real hook (a thread/insight, not just the title).
2. **Day 0–2**: reply to every comment; post in r/MachineLearning, r/pytorch, Hacker News, ML Discords.
3. **Day 7**: reshare with different framing per platform.
4. **Ongoing**: link from future articles; update with new results.

One influencer share ≈ +32% total shares. Identify 3–5 ML-community people and share directly with a personalized note.

---

## 12. Common Pitfalls

| Pitfall | Fix |
|---------|-----|
| Weak/descriptive headline | Use a §1 formula; put a concrete result in the title |
| Generic opening ("In this article…") | Use a §2 hook; read it out loud |
| No narrative (reads like a manual) | Tell the story of how you built it; show the failures |
| Jargon overload | Define methodology-specific terms; skip the fundamentals |
| Hand-waving claims | Back with own data, citation, or first principles |
| Wall of text | Visual break every 75–100 words; 2–3 sentence paragraphs |
| Broken code snippets | Test every block; include imports; annotate tensor dims |
| Point-estimate results | Show variance, hardware, wall-clock time, curves |
| Missing CTAs | Soft (start) + contextual (mid) + specific question (end) |
| Series part feels like "just setup" | Make each part standalone-valuable |
| Ignoring distribution | Follow §11; great articles get 0 views without promotion |
| Endless research | Time-box; ship even if imperfect |

---

## 13. Pre-Publish Checklist

The authoritative checklist is [great-medium-article.md](great-medium-article.md) Appendix C. Quick version:

- [ ] Title <60 chars, proven formula; subtitle expands without repeating
- [ ] Opening hook works in 15 seconds (read aloud)
- [ ] Every section follows Gradual Discovery (problem → method → example → pitfall)
- [ ] No undefined methodology jargon; fundamentals not over-explained
- [ ] All claims backed by data, citation, or first-principles
- [ ] Limitations acknowledged; standalone value confirmed
- [ ] Paragraphs 2–3 sentences; scannable H2/H3; bold on key terms
- [ ] Code blocks tagged; tables used for comparisons
- [ ] Visual every 75–100 words
- [ ] Figures labeled; consistent color; variance + hardware + curves shown
- [ ] Every code snippet tested; tensor dims annotated; repo linked
- [ ] Hyperparameters, versions, seeds documented
- [ ] CTAs at start / mid / end; 3–5 highlightable sentences
- [ ] Series: nav links top AND bottom
- [ ] Medium: T-dropdown headings, 3–5 tags, preview image, meta <160 chars
- [ ] Distribution plan ready (X, LinkedIn, Reddit, 3–5 people, day-7 reshare)
