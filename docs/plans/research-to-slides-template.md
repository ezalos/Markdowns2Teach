# Research-to-Slides Conversion Template

<!-- ABOUTME: Reusable checklist for converting any research topic into a Marp slide deck. -->
<!-- ABOUTME: Covers structure formula, content extraction, conventions, and verification. -->

## 1. Pre-flight

Before starting conversion, assess the source material:

- [ ] Read the `report.md` table of contents — identify categories/layers/sections
- [ ] Count total items (companies, tools, frameworks, etc.)
- [ ] Estimate slide count using the formula in §2
- [ ] Identify 4-6 items for spotlight slides (diverse, interesting, relevant to audience)
- [ ] Check for EU/French-relevant items to weave throughout (not isolate)

## 2. Structure Formula

Target: **25-30 slides** per deck. Adjust proportionally for smaller/larger topics.

| Section | Slides | Content |
|---------|--------|---------|
| Title | 1 | `_class: title`, deck title, subtitle, course info |
| Introduction | 1-2 | Why this topic matters, scope, recurring questions |
| Overview | 1 | Summary table of all categories/layers |
| Category blocks | 1-2 per category | Table of items + 1 spotlight per 8-10 items |
| Discussion questions | 1 per section | Scenario + 2-3 questions for the class |
| Synthesis | 2-3 | Where value concentrates, EU angle, key takeaways |

**Spotlight ratio**: ~1 spotlight per 8-10 items in the report. For 50 items → 5-6 spotlights.

**Discussion ratio**: ~1 discussion per major section (group of 2-4 category slides).

## 3. Content Extraction Patterns

### From report.md TOC tables → Layer/category overview slides

```markdown
| Entreprise | Pays | Métrique clé | Rôle |
```

- Cap tables at **7 rows** maximum — split across 2 slides if needed
- Include country flags for visual scanning
- Highlight EU companies with bold or a note

### From JSON profiles → Spotlight slides

Use `_class: cols` layout. Left column = facts, right column = analysis.

```markdown
<div class="left">

- Key financial metrics (revenue, valuation, growth)
- Products/services (2-3 bullets)

</div>
<div class="right">

- Competitive moats / what makes them special
- Lesson for entrepreneurs
- EU/sovereignty angle (if applicable)

</div>
```

**Critical**: cols slides must stay ≤15 content lines (the linter counts div tags, headings, and bullets). Budget:
- Title line: 1
- Div tags: 4 (`<div class="left">`, `</div>`, `<div class="right">`, `</div>`)
- Remaining for actual content: **10 lines**
- Avoid `###` subheaders inside cols — they eat a line each with no visual gain at this density

### From report.md analysis sections → Synthesis slides

- Extract key themes, patterns, and contrasts
- Frame for entrepreneurial decision-making
- Include a "Key Takeaways" slide as the final content slide (5 numbered points max)

### Handling uncertain data

- If a JSON field is marked `uncertain` or `estimated`, either skip it or add `(est.)` qualifier
- Never present uncertain data as definitive

## 4. Discussion Question Design

Each discussion slide should follow this pattern:

```markdown
# XX — Discussion : [Topic]

> [Concrete scenario framing the question — put students in the entrepreneur's seat]

**Questions pour la classe** :
- [Specific question 1]
- [Specific question 2]
- [Optional: table comparing options]
```

Good discussion questions:
- Present a real trade-off (cost vs. sovereignty, speed vs. control)
- Reference companies from the preceding slides
- Have no single "right" answer
- Connect to students' entrepreneurial context

## 5. Conventions Checklist

### Front matter

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche [Topic] 2024–2026 · Données publiques"
---
```

### File header

```markdown
<!-- ABOUTME: Brief description of slide deck content. -->
<!-- ABOUTME: Audience and pedagogical approach. -->
```

### Slide classes

- `<!-- _class: title -->` + `<!-- _paginate: skip -->` + `<!-- _header: "" -->` + `<!-- _footer: "" -->` for title slide
- `<!-- _class: section -->` for section dividers
- `<!-- _class: cols -->` for two-column spotlights

### Numbering

- Content slides: `# 01 — Title` (2-digit, em dash, restarts per file)
- Title slides and section dividers: **NOT** numbered

### Language

- French body text, English technical terms used directly
- "Le Supervised Learning est..." NOT "L'apprentissage supervisé (Supervised Learning)"

### Citations (mandatory for all data slides)

Every data claim must be sourced. Format:

```markdown
- Le marché atteint **$2 527 Mds** en 2026 [1]
- L'adoption passe de 55% à **88%** en deux ans [2]

<small>Sources : [1] [Gartner](https://www.gartner.com/...) · [2] [McKinsey](https://www.mckinsey.com/...)</small>
```

- In-text `[1]` markers next to each data claim
- `<small>Sources : [1] [Authority](url) · [2] [Authority](url)</small>` at slide bottom
- Authority shorthand as display text, full URL as href, ` · ` separator
- The sources line costs ~1 content line — budget **~13 effective content lines** per slide
- Discussion slides and section dividers may omit citations if no data claims are made
- Source priority: company IR > Bloomberg/CNBC > TechCrunch > Crunchbase

## 6. Directory Naming

```
slides/<research-slug>/
├── 01-<topic-name>.md
└── assets/
```

Examples:
- `slides/ai-value-chain/01-ai-value-chain.md`
- `slides/prompt-engineering/01-prompt-techniques.md`
- `slides/ai-business-models/01-business-patterns.md`

## 7. Verification

Run these checks before considering a deck complete:

- [ ] `make check` passes (no slide exceeds 15 content lines)
- [ ] `make check-citations` passes for the new deck (all data slides have sources)
- [ ] `make html` builds without errors
- [ ] Title slide renders with dark blue background
- [ ] Section dividers render with light blue background
- [ ] Cols layouts split correctly (left/right)
- [ ] All financial figures match report.md source data
- [ ] ABOUTME comments present after front matter
- [ ] Numbering is correct (01-XX, title/section unnumbered)
- [ ] French body + English technical terms (no translations)
- [ ] Footer attribution is appropriate for the source
- [ ] EU companies woven throughout (not isolated in one slide)
- [ ] Discussion questions are concrete scenarios, not abstract

## 8. Common Pitfalls

- **Cols overflow**: The linter counts `<div>` tags as content lines. Budget only 10 lines of actual content per cols slide.
- **CRLF line endings**: The Write tool may produce CRLF. Run `sed -i 's/\r$//' <file>` before `make check` if the linter shows 0 warnings on a clearly overfull deck.
- **Table overflow**: Tables with 8+ rows will overflow. Split into 2 slides (e.g., "Foundation Models 1/2" and "2/2").
- **Too many spotlights**: More than 6-7 spotlights in a 30-slide deck makes the pacing monotonous. Choose diverse, high-impact examples.
- **Isolated EU slide**: Don't put all EU companies on one slide. Weave them into each layer, then summarize in synthesis.
