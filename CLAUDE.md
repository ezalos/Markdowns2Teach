# Markdowns2Teach — Project Conventions

## Purpose

Slide decks for the **"Deep Tech & Machine Learning"** course, M2 Entrepreneuriat at Sorbonne (5 sessions x 3h, Mon 17h30–20h30, ~15–20 students).

Target audience: business school students (mostly non-engineers), entrepreneurially-minded, heavy LLM users, curious about the latest AI products. Some have coded a bit but get lost in deep technical detail.

## Pedagogical Principles

- **70% hands-on / 30% theory** — practice from session 1
- **Business-first** — start from business problems, not algorithms
- **Non-technical friendly** — accessible vocabulary, decision-making focus
- **French/European context** — Mistral AI, EU AI Act, GDPR as priorities
- **Real cases 2024–2026** — Klarna, Mistral AI, L'Oréal, etc.
- **Avoid ChatGPT-reproducible content** — students already prompt; add structured vision, verified sources, entrepreneurial perspective
- **Ethics integrated** — from session 1, not an afterthought

## Course Structure (5 sessions)

1. **Fundamentals & AI landscape** — AI categories, ecosystem actors, first hands-on
2. **Prompt engineering & no-code tools** — advanced prompts, Teachable Machine, Voiceflow
3. **Framing & managing AI projects** — CRISP-DM, AI Canvas, Build vs Buy
4. **AI business models & strategy** — business model patterns, scaling, unit economics
5. **Ethics, governance & final presentations** — EU AI Act, bias, final project pitches

## Directory Structure

```
Markdowns2Teach/
├── CLAUDE.md                        # This file
├── .marprc.yml                      # Marp CLI config
├── .gitignore
├── Makefile                         # build/preview/clean/check
├── themes/
│   └── sorbonne.css                 # Custom Marp theme
├── slides/
│   └── <source-slug>/
│       └── chXX-descriptive-slug/
│           ├── XX-topic-name.md     # Slide deck
│           └── assets/              # Images for this chapter
├── scripts/
│   ├── extract-images.sh            # PDF image extraction
│   └── check-overflow.sh            # Slide overflow linter
├── references/                      # Source PDFs and HTML (not generated)
│   ├── AndrewNg/                    # W1.pdf, W2.pdf, W3.pdf
│   └── KevinVu/                     # cours_*.html, cours_*.pdf
├── docs/                            # Course planning documents
├── plans/                           # Conversion roadmaps and specs
└── dist/                            # Generated output (gitignored)
```

**Naming conventions:**
- Directories: `chXX-descriptive-slug/` (2-digit prefix for ordering)
- Files: `XX-topic-name.md`
- English names for files/dirs

## Marp Slide Standards

### Front matter template

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Source attribution · License"
---
```

### File header comments

Every `.md` slide file must start (after front matter) with two ABOUTME comments:

```markdown
<!-- ABOUTME: Brief description of what this slide deck covers. -->
<!-- ABOUTME: Audience and content approach. -->
```

### Slide separators

- Use `---` on its own line to separate slides
- First slide should use `<!-- _class: title -->` with `<!-- _paginate: skip -->`
- Section dividers use `<!-- _class: section -->`
- Two-column layouts use `<!-- _class: cols -->` with `<div class="left">` / `<div class="right">`

### Slide numbering

- Content slides use flat per-file numbering: `# 01 — Title Here` (2-digit number, em dash)
- Title slides and section dividers are **NOT** numbered
- Numbering restarts in each `.md` file
- Makes it easy to reference slides: "move slide 03 after 05"

### Content guidelines

- **Language**: French body text, **English technical terms used directly** (no French translation)
  - Technical terms stay English: "Supervised Learning", "Deep Learning", "Prompt Engineering"
  - Do NOT write: "Apprentissage supervisé *(Supervised Learning)*"
  - Instead write: "Le Supervised Learning est la technique la plus déployée..."
- **Bullet points**: concise ideas, no long paragraphs
- **Business-framed**: frame concepts for entrepreneurs, not researchers
- **Engagement questions**: include 1–2 discussion questions per major section
- **Tables**: use for comparisons (input/output examples, tool comparisons)
- **Blockquotes**: use `>` for callouts, practical tips, and key takeaways

### Citations & sourcing

Every data claim must be sourced. Use the following format on all research-backed slides:

- **In-text markers**: superscript-style `[1]`, `[2]` next to each data claim
- **Slide footer**: `<small>Sources : [1] [Authority](url) · [2] [Authority](url)</small>` at the bottom of the slide
- Authority shorthand as display text (e.g., "Stanford HAI", "Gartner"), full URL as href
- Separator between citations: ` · ` (middle dot)
- The sources line costs ~1 content line — budget **~13 effective content lines** per slide (threshold remains 15)
- Cols slides: budget **~8-9 lines** of actual content per column + 1 source line
- Discussion slides and section dividers may omit citations if no data claims are made
- **Source priority**: when sources conflict, prefer the most recent data from the most reputable source (company IR > Bloomberg/CNBC > TechCrunch > Crunchbase)
- If a source contradicts the number in the slide, update the slide number to match the best source
- Example:
  ```markdown
  - Le marché atteint **$2 527 Mds** en 2026 [1]
  - L'adoption passe de 55% à **88%** en deux ans [2]

  <small>Sources : [1] [Gartner](https://www.gartner.com/...) · [2] [McKinsey](https://www.mckinsey.com/...)</small>
  ```

## Build Commands

```bash
make help       # Show available targets
make build      # Build HTML + PPTX to dist/
make html       # Build HTML only
make pptx       # Build PPTX only
make preview    # Launch Marp preview server
make clean      # Remove dist/
```

## Attribution

- Andrew Ng / DeepLearning.AI materials: **CC BY-SA 2.0** — educational use, must cite DeepLearning.AI as source
- Footer on adapted slides: `Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0`
- Kevin Vu / Dauphine archived materials: attribution TBD

## Source Materials

| Path | Contents |
|------|----------|
| `references/AndrewNg/W1.pdf` | Andrew Ng "Generative AI for Everyone" W1 (88p) |
| `references/AndrewNg/W2.pdf` | Andrew Ng "Generative AI for Everyone" W2 (57p) |
| `references/AndrewNg/W3.pdf` | Andrew Ng "Generative AI for Everyone" W3 (49p) |
| `references/KevinVu/cours_*.html` | Kevin Vu WebSlides course decks (7 sessions) |
| `references/KevinVu/cours_*.pdf` | Kevin Vu course PDFs |
| `docs/2026 M2 - ML & DeepTech.md` | Course plan, themes, and session structure |
| `docs/Kevin Vu M2 Sorbonne *.md` | Notes from meeting with previous teacher |
| `docs/NotebookLM.prompt.txt` | Audience context and pedagogical goals |
