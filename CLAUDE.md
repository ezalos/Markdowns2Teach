# Markdowns2Teach — Project Conventions

## Purpose

Slide decks for the **"Deep Tech & Machine Learning" (UE3)** course, M2 IMT&E at Paris 1 Panthéon-Sorbonne (5 sessions x 3h, Mon 17h30–20h30, ~28 inscrits, 15–20 présents, 7 équipes de 4).

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

| Session | Title | Deck A | Deck B |
|---------|-------|--------|--------|
| 1 | Comprendre l'IA en 2026 | L'IA Générative : ce qu'elle sait faire | Les LLMs |
| 2 | Construire avec l'IA | Du Prompt au Produit | L'Ingénierie IA |
| 3 | Cadrer un projet IA | Évaluer une solution IA | Méthodologie projet IA |
| 4 | Le business de l'IA | L'écosystème IA | Business Models & Cas Réels |
| 5 | Éthique, gouvernance & clôture | Régulation & IA responsable | B: Présentations finales (live) · C: QCM & clôture |

Each 3h session follows: **Deck A** (45 min) → break → **Deck B** (45 min) → break → **Block C** (practice/QCM/speaker, 45 min).

## Directory Structure

```
Markdowns2Teach/
├── CLAUDE.md                        # This file
├── .marprc.yml                      # Marp CLI config
├── .gitignore
├── Makefile                         # build/preview/clean/check/sync
├── themes/
│   └── sorbonne.css                 # Custom Marp theme
├── slides/
│   ├── session-XX/                  # One dir per session (01–05)
│   │   ├── A-slug.md                # Deck A (first half of session)
│   │   ├── B-slug.md                # Deck B (second half, optional)
│   │   └── assets/                  # Images (subdirs by source prefix)
│   │       ├── ng01/                # Andrew Ng W1 images
│   │       ├── ng02/                # Andrew Ng W2 images
│   │       ├── ng03/                # Andrew Ng W3 images
│   │       └── infographics/        # PaperBanana-generated diagrams
│   └── extra-decks/                 # Optional/extracted decks (not in main sessions)
│       ├── architectures.md         # CNN, RNN, GAN, Transformer deep dive
│       ├── D-biais-ethique.md       # Bias & ethics intro (teaser for Session 5)
│       └── assets/                  # Assets for extra decks
├── scripts/
│   ├── extract-images.sh            # PDF image extraction
│   ├── check-overflow.sh            # Slide overflow linter
│   └── generate-index.sh            # HTML index page generator
├── docs/
│   ├── outline.md                   # Active session map
│   ├── todos.md                     # Active task tracker
│   ├── notes/                       # Informal notes and drafts
│   │   ├── Meeting Notes - Kevin Vu M2 Sorbonne.md
│   │   ├── Outline - 2026 M2 - ML & DeepTech.md
│   │   └── prompt_continue_deep_research.md
│   ├── references/                  # Formalized course references
│   │   ├── course-identity.md       # Course identity and student profile
│   │   ├── course-architecture.md   # Session calendar and topics
│   │   ├── slide-creation-standards.md  # Single source of truth for all slide-building rules
│   │   ├── workflow-new-slides.md   # Workflows: create slides from scratch or from research
│   │   ├── workflow-citation-audit.md   # Citation audit backlog and remediation process
│   │   └── student-group-project.md # Student classification project brief
│   ├── plans/                       # One-shot roadmaps
│   │   ├── andrew-ng-conversion-roadmap.md
│   │   ├── 2026_02_07-convert_references.md
│   │   └── NotebookLM.prompt.txt
│   ├── archive/slides-v1/           # Pre-restructuring slide archive
│   ├── qcm/                         # Quiz materials
│   ├── research/                    # Research pipeline outputs
│   └── sources/                     # Source materials (gitignored except READMEs)
│       ├── courses/                 # Course PDFs and HTML
│       │   ├── AndrewNg/            # W1.pdf, W2.pdf, W3.pdf
│       │   └── KevinVu/             # cours_*.html, cours_*.pdf
│       └── books/                   # Reference books
└── dist/                            # Generated output (gitignored)
    ├── html/                        # Flat HTML output + assets/
    └── pptx/                        # Flat PPTX output
```

**Naming conventions:**
- Session directories: `session-XX/` (XX = 01–05)
- Deck files: `A-slug.md`, `B-slug.md` — letter prefix provides ordering within session
- Session 5 has only deck A (Block B is live presentations, Block C is QCM + closing)
- Assets: `assets/` per session, with source-prefix subdirs (`ng01/`, `ng02/`, `ng03/`)
- English names for files/dirs
- Original topic-based decks archived at `docs/archive/slides-v1/`

## Marp Slide Standards

### Front matter template

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session N · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0"
---
```

The header includes the session number. The footer lists source attributions:

| Case | Footer |
|------|--------|
| Multi-source (research + Andrew Ng) | `"Sources multiples · DeepLearning.AI CC BY-SA 2.0"` |
| Primarily Andrew Ng | `"Adapté de Generative AI for Everyone par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"` |
| Original research only | `"Recherche [Topic] 2024–2026 · Données publiques"` |

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
- Cols slides: 15 linter lines = 1 title + 4 div tags + **~9 lines of actual content** split across 2 columns + 1 source line
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
make html       # Build HTML only → dist/html/
make pptx       # Build PPTX only → dist/pptx/
make preview    # Launch Marp preview server
make sync       # Sync dist/pptx/ to GDrive via rclone
make clean      # Remove dist/
```

## Attribution

- **Andrew Ng / DeepLearning.AI**: CC BY-SA 2.0 — cite DeepLearning.AI as source
  - Footer: `Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0`
- **Kevin Vu / Dauphine**: archived materials, attribution TBD
- **Research decks**: original content based on cited sources (URLs in slide `<small>` tags)
  - Footer: `Recherche [Topic] 2024–2026 · Données publiques`
- **Multi-source decks**: use `Sources multiples · DeepLearning.AI CC BY-SA 2.0` when combining Andrew Ng + research content

## Slide Decks

| Path | Title | Slides |
|------|-------|--------|
| `slides/session-01/A-genai-fondamentaux.md` | L'IA Générative : ce qu'elle sait faire | 37 |
| `slides/session-01/B-llms.md` | Les LLMs : comprendre et utiliser | 20 |
| `slides/session-01/C-premier-projet-ia.md` | Votre premier projet IA | 25 |
| `slides/session-02/A-prompt-au-produit.md` | Du Prompt au Produit | 18 |
| `slides/session-02/B-ingenierie-ia.md` | L'Ingénierie IA | 17 |
| `slides/session-03/A-evaluer-solution-ia.md` | Évaluer une solution IA | 18 |
| `slides/session-03/B-methodologie-projet.md` | Méthodologie projet IA | 17 |
| `slides/session-04/A-ecosysteme-ia.md` | L'écosystème IA | 18 |
| `slides/session-04/B-business-models.md` | Business Models & Cas Réels | 17 |
| `slides/session-05/A-regulation-ethique.md` | Régulation & IA responsable | 23 |
| `slides/extra-decks/architectures.md` | Tour des architectures (CNN, RNN, GAN, Transformer) | 4 |
| `slides/extra-decks/D-biais-ethique.md` | Biais et éthique : introduction | 3 |
| `slides/session-02/B-au-dela-des-llms.md` | L'IA au-delà des LLMs *(archive, ex-S01-B)* | 23 |

## Source Materials

| Path | Contents |
|------|----------|
| `docs/sources/courses/AndrewNg/W1.pdf` | Andrew Ng "Generative AI for Everyone" W1 (88p) |
| `docs/sources/courses/AndrewNg/W2.pdf` | Andrew Ng "Generative AI for Everyone" W2 (57p) |
| `docs/sources/courses/AndrewNg/W3.pdf` | Andrew Ng "Generative AI for Everyone" W3 (49p) |
| `docs/sources/courses/KevinVu/cours_*.html` | Kevin Vu WebSlides course decks (7 sessions) |
| `docs/sources/courses/KevinVu/cours_*.pdf` | Kevin Vu course PDFs |
| `docs/archive/slides-v1/` | Pre-restructuring slide archive (15 topic directories) |
| `docs/research/` | Research pipeline outputs (13 topics, reports + raw data) |
| `docs/notes/Outline - 2026 M2 - ML & DeepTech.md` | Course plan, themes, and session structure |
| `docs/notes/Meeting Notes - Kevin Vu M2 Sorbonne.md` | Notes from meeting with previous teacher |
| `docs/references/` | Formalized course references (identity, architecture, standards, workflows) |
