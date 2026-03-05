# Overflow Remediation Playbook

<!-- ABOUTME: Decision guide and technique catalog for fixing overflowing Marp slides. -->
<!-- ABOUTME: Includes decision tree, 8 techniques with before/after examples, and content writing guidelines. -->

---

## 1. Decision Tree

```
Overflow < 30px (< 1 line)?
  → Technique A: Tighten wording (shorter bullets, remove filler)

Overflow 30-80px (1-2 lines)?
  → Technique B: Add `compact` class
  → Technique C: Move blockquote to speaker notes

Overflow 80-200px (2-5 lines)?
  → Technique D: Switch to cols layout (split content into two columns)
  → Technique E: Add `compact-table` for table-heavy slides
  → Technique F: Reduce image from bg right:50% to bg right:35-40%

Overflow > 200px (5+ lines)?
  → Technique G: Split into 2 slides (same section, "XXa" and "XXb")
  → Technique H: Extract table to its own slide
```

Multiple techniques can be combined. When in doubt, start with the lightest fix and escalate.

---

## 2. Technique Catalog

### Technique A — Tighten wording

**When to use**: Overflow < 30px. Long sentences in bullets that wrap to 2+ lines.

**Rule**: Max 15 words per bullet. Use fragments, not sentences.

**Validated on**: S2A slide 13 "Le coût d'entraînement" — **21px → 0px**

Before:
```markdown
- Ces chiffres = **compute du run final uniquement**. Le coût total (salaires R&D, expériences ratées, infra) peut être **2–10x** plus élevé [1]
- DeepSeek-V3 atteint le niveau GPT-4o pour **14x moins cher** — mais sur des H800 à $2/h [2]
```

After:
```markdown
- Chiffres = **compute du run final** — coût total (R&D, infra) : **2–10x** plus élevé [1]
- DeepSeek-V3 ≈ GPT-4o pour **14x moins cher** (H800 à $2/h) [2]
```

---

### Technique B — `compact` class

**When to use**: Overflow 30-200px. Content is well-organized but needs more vertical space.

**Effect**: Reduces font 25px→21px, line-height 1.5→1.4, blockquote font 21px→18px.

**Validated on**: S2A slide 06 "Context Window : croissance exponentielle" — **201px → 0px**

Fix applied: Added `<!-- _class: compact -->` + reduced image from `bg right:50%` to `bg right:40%` + slightly tightened text.

Before:
```markdown
---

# 06 — Context Window : une croissance exponentielle

![bg right:50% contain](assets/context-window-growth.png)

(table + paragraph + blockquote)
```

After:
```markdown
---

<!-- _class: compact -->

# 06 — Context Window : une croissance exponentielle

![bg right:40% contain](assets/context-window-growth.png)

(same table + tightened paragraph + shortened blockquote)
```

**Note**: For overflows > 100px, `compact` alone may not suffice — combine with image reduction (Technique F) or blockquote removal (Technique C).

---

### Technique C — Move blockquote to speaker notes

**When to use**: Overflow 30-100px. Slide has bullets + blockquote + sources, and the blockquote is a pedagogical aside (not core content).

**Effect**: Saves ~60-80px per blockquote removed. Move the insight to a Marp comment for speaker reference.

**Validated on**: S2A slide 05 "Context Window : mémoire de conversation" — **95px → 0px**

Before:
```markdown
# 05 — Context Window : la mémoire de conversation

![bg right:45% contain](assets/context-window.svg)

La **Context Window** est la mémoire de travail du LLM — tout ce qu'il peut "voir" pour générer sa réponse.

- Input + Output partagent la même fenêtre (ex : 200K tokens pour Claude)
- Le contexte *s'accumule* à chaque tour — rien n'est supprimé silencieusement
- Les **Thinking Tokens** comptent pendant la génération, puis sont retirés [1]

> La Context Window limite la longueur des conversations et la taille des documents analysables. Les APIs facturent **par Token** (input + output).
```

After:
```markdown
# 05 — Context Window : la mémoire de conversation

![bg right:40% contain](assets/context-window.svg)

La **Context Window** = mémoire de travail du LLM, tout ce qu'il "voit" pour répondre.

- Input + Output partagent la même fenêtre (200K tokens pour Claude)
- Le contexte *s'accumule* à chaque tour — rien n'est supprimé
- Les **Thinking Tokens** comptent pendant la génération, puis sont retirés [1]
- Facturation **par Token** (input + output)

<!--
Speaker notes:
La Context Window limite la longueur des conversations et la taille des documents analysables.
-->
```

The blockquote's key info ("facturent par Token") was promoted to a bullet; the rest moved to speaker notes.

---

### Technique D — Switch to cols layout

**When to use**: Overflow 80-350px. Slide has a table + image + text that compete for vertical space. Content is logically splittable into two groups.

**Effect**: Moves from vertical stacking to side-by-side layout, roughly doubling available vertical space.

**Validated on**: S1A slide 31 "Object Detection & Segmentation" — **344px → 0px**

Before:
```markdown
# 31 — Object Detection & Segmentation

Des tâches de vision qui vont au-delà de la simple Classification :

| Tâche | Ce qu'elle fait | Exemple |
|---|---|---|
| **Image Classification** | Une étiquette par image | "C'est un chat" |
| **Object Detection** | Localise chaque objet (bounding box) | "Chat à (x,y), chien à (x,y)" |
| ... | ... | ... |

*Outils clés* : YOLO (détection temps réel) [1], Segment Anything (Meta) [2]

> Ces tâches sont au cœur de la conduite autonome...

![bg right:45% contain](assets/tasks_cv.webp)
```

After:
```markdown
<!-- _class: cols compact compact-table -->

# 31 — Object Detection & Segmentation

<div class="left">

| Tâche | Ce qu'elle fait |
|---|---|
| **Classification** | Une étiquette par image |
| **Object Detection** | Localise chaque objet (box) |
| **Semantic Seg.** | Colore chaque pixel par catégorie |
| **Instance Seg.** | Sépare chaque objet individuel |

*Outils* : YOLO [1], Segment Anything [2]

</div>
<div class="right">

![w:450](assets/tasks_cv.webp)

> Au cœur de la conduite autonome, du contrôle qualité et de l'imagerie médicale.

</div>
```

Key changes: `bg right:45%` → inline `![w:450]` inside right column; 3-column table → 2-column (removed "Exemple" column); combined `cols compact compact-table` classes.

---

### Technique E — `compact-table` class

**When to use**: Overflow 80-200px on a slide with a table of 4+ rows or 4+ columns.

**Effect**: Reduces table font 21px→17px, cell padding 8-10px→4px.

**Validated on**: S2A slide 09 "Vue d'ensemble du pipeline" — **168px → 0px**

Fix applied: Added `<!-- _class: compact compact-table -->` + shortened table header labels + tightened blockquote.

Before:
```markdown
| Étape | Ce qu'il apprend | Volume de données | Résultat |
```

After:
```markdown
<!-- _class: compact compact-table -->

| Étape | Ce qu'il apprend | Données | Résultat |
```

Column header "Volume de données" → "Données" and cell values tightened (e.g. "~25K–1M exemples" → "~25K–1M ex.").

---

### Technique F — Reduce image width

**When to use**: Overflow 80-250px. Slide uses `bg right:45-50%` with text + table or 4+ bullets.

**Effect**: `bg right:50%` → `bg right:35%` gives ~15% more width for text, reducing line wrapping significantly.

**Validated on**: S2A slide 08 "MoE : l'architecture qui change tout" — **227px → 0px**

Fix applied: `bg right:45%` → `bg right:35%` + added `compact` class.

Before:
```markdown
# 08 — Mixture of Experts (MoE) : l'architecture qui change tout

![bg right:45% contain](assets/infographics/dense-vs-moe.png)
```

After:
```markdown
<!-- _class: compact -->

# 08 — Mixture of Experts (MoE) : l'architecture qui change tout

![bg right:35% contain](assets/infographics/dense-vs-moe.png)
```

**Tip**: For severe overflows (>200px), combine image reduction with `compact` class.

---

### Technique G — Split slide

**When to use**: Overflow > 200px. Slide contains two distinct sub-topics or a definition + detailed reference data.

**Effect**: Distributes content across 2 slides with related numbering (e.g. "04" and "04b").

**Validated on**: S2A slide 04 "Tokens : le vocabulaire des LLMs" — **286px → 0px + 0px**

Before (one overflowing slide):
```markdown
# 04 — Tokens : le vocabulaire des LLMs

(definition paragraph + link + rule + 3-row table + blockquote + sources)
```

After (two slides):
```markdown
# 04 — Tokens : le vocabulaire des LLMs

(definition paragraph + rule + link + blockquote)

---

# 04b — Tokens : taille du vocabulaire

(table + 2 analysis bullets + sources)
```

**Naming**: Use "XXb" suffix for the continuation slide, or find a natural subtitle ("définition" / "exemples", "concept" / "référence").

---

### Technique H — Extract table to its own slide

**When to use**: Overflow > 200px. Slide has explanatory bullets/text + a reference table. The table is useful but standalone.

**Effect**: Table moves to a dedicated slide; original slide keeps the narrative.

**Validated on**: S1A slide 33 "HuggingFace Tasks" — **310px → 0px + 0px**

Before:
```markdown
# 33 — HuggingFace Tasks : votre vocabulaire de recherche

(description + 2 bg images + link + 4-row table + blockquote)
```

After:
```markdown
# 33 — HuggingFace Tasks : votre vocabulaire de recherche

(description + 2 bg images + link + blockquote)

---

<!-- _class: compact-table -->

# 33b — HuggingFace Tasks (référence)

(table only)
```

---

## 3. Class Composition Cheat Sheet

Marp supports multiple classes: `<!-- _class: compact cols -->`.

| Combination | Effect | Use when |
|---|---|---|
| `compact` | Smaller font (21px), tighter spacing | 1-3 extra lines needed |
| `compact-table` | Dense table (17px font, 4px padding) | Table has 5+ rows or 4+ cols |
| `compact compact-table` | Both effects | Dense text + dense table |
| `cols compact` | Two columns + smaller font | Dense two-column layout |
| `cols compact compact-table` | All three | Cols with dense table in one side |
| `cols-60-40` | Asymmetric 60/40 split | One column has more content |
| `cols-3` | Three equal columns | Three-way comparison |
| `highlight` | Orange accent, warm background | Key takeaway slides |
| `dark` | Dark gradient background | Summary or key stat slides |

---

## 4. Content Writing Guidelines

Key rules derived from cognitive load theory and assertion-evidence slide design:

1. **Max 4-6 visual elements per slide** (Cowan's working memory limit) — an element is a bullet, a table, a blockquote, an image, or a source line
2. **Max 15 words per bullet** — use fragments, not sentences
3. **Assertion headline**: The slide title states the key takeaway, not just the topic
   - ✅ "Context windows double every year"
   - ❌ "Context Window: growth"
4. **Image carries structure, text adds interpretation** — don't duplicate in text what the infographic shows
5. **One table per slide**, max 5 rows × 4 columns (unless `compact-table`)
6. **Blockquote = optional** — if the slide overflows, remove the blockquote first (Technique C)
7. **Sources line is mandatory** for data slides but counts as 1 visual element
8. **`bg right` images**: budget text for the remaining width
   - `bg right:50%` → ~8-9 lines of text
   - `bg right:40%` → ~11-12 lines of text
   - `bg right:35%` → ~12-13 lines of text

---

## 5. Validation Results Summary

| Technique | Test slide | Before | After | Method |
|---|---|---|---|---|
| A: Tighten wording | S2A "Coût d'entraînement" | 21px | 0px | Shortened 2 bullets |
| B: `compact` | S2A "Context Window growth" | 201px | 0px | compact + bg 50%→40% |
| C: Move blockquote | S2A "Context Window" | 95px | 0px | Blockquote→bullet + speaker notes, bg 45%→40% |
| D: cols layout | S1A "Object Detection" | 344px | 0px | cols compact compact-table, bg→inline img |
| E: `compact-table` | S2A "Vue d'ensemble pipeline" | 168px | 0px | compact compact-table + tighter headers |
| F: Reduce image | S2A "MoE" | 227px | 0px | compact + bg 45%→35% |
| G: Split slide | S2A "Tokens" | 286px | 0px+0px | Split into 04 + 04b |
| H: Extract table | S1A "HuggingFace Tasks" | 310px | 0px+0px | Table → separate 33b slide |

All 8 techniques validated with `node scripts/check-overflow-visual.js`.
