# Markdowns2Teach — Project Conventions

## Purpose

Slide decks for the **"Deep Tech & Machine Learning" (UE3)** course, M2 IMT&E at Paris 1 Panthéon-Sorbonne (5 sessions x 3h, Mon 17h30–20h30, ~28 inscrits, 15–20 présents, 7 équipes de 4).

Target audience: business school students (mostly non-engineers), entrepreneurially-minded, heavy LLM users, curious about the latest AI products. Some have coded a bit but get lost in deep technical detail.

The repo has since grown beyond this one course: it is now the home for **all of Louis's
teaching and online writing** — standalone talks (`slides/<event>/`) and articles/essays
(`writing/`) alongside the Sorbonne course (`slides/sorbonne-m2-2026/`). The pedagogical
principles below are Sorbonne-specific; the slide/writing standards and tooling are reusable
across everything.

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
| 1 | Comprendre l'IA en 2026 | L'IA Générative : ce qu'elle sait faire | *(pas de Deck B — Bloc C : premier projet IA)* |
| 2 | Les LLMs : de la théorie à la pratique | Les LLMs : comprendre et utiliser | Évaluer l'IA |
| 3 | Construire avec l'IA | Embeddings · B: RAG | Agents IA |
| 4 | Le business de l'IA | Méthodologie projet IA · B: L'écosystème IA | Business Models & Cas Réels |
| 5 | Éthique, gouvernance & clôture | Régulation & IA responsable | B: Présentations finales (live) · C: QCM & clôture |

Each 3h session follows: **Deck A** (45 min) → break → **Deck B** (45 min) → break → **Block C** (practice/QCM/speaker, 45 min).

## Directory Structure

The repo began as the Sorbonne M2 course and now also hosts **standalone talks** and
**online writing**. Top-level split: `slides/` (decks), `writing/` (articles/essays),
`workshops/` (hands-on infra), `docs/` (course docs + per-talk docs + reusable references).

```
Markdowns2Teach/
├── CLAUDE.md                        # This file
├── .marprc.yml                      # Marp CLI config
├── Makefile                         # build/preview/clean/check/sync/index/guide
├── themes/                          # sorbonne.css, sorbonne-fullpage.css, station-f.css
├── slides/
│   ├── index.manifest.yml           # Source of truth for index grouping/dates/order
│   ├── sorbonne-m2-2026/            # The Sorbonne M2 course
│   │   ├── session-01 … session-05/ # A-/B-/C- decks + assets/ (ng01/ ng02/ ng03/ infographics/)
│   │   ├── evaluation/              # Evaluation reference decks
│   │   └── extra-decks/             # Archived/older session decks
│   ├── station-f/                  # Talk — Building With AI (EN), 2 decks (2026-04-15)
│   ├── pruna/                      # Talk — SDXL optimization, interview (2026-05-28)
│   ├── gustave-eiffel-agents/      # Talk — Building AI Agents (2026-06-01)
│   └── capgemini-ai-agents/        # Talk — AI Agents Tech Lab (frontend-slides HTML, 2026-06-18)
│       ├── content/                # Portable Markdown (latest.md + 2026-06-10-original.md)
│       └── capgemini-ai-agents.html # Generated self-contained deck (committed, linked from index)
├── writing/                        # Online writing
│   ├── medium/                     # Article projects (e.g. tf-to-pytorch-migration/)
│   └── ai-safety-stance/           # Essay + grant + dialectic run
├── workshops/
│   └── sorbonne-m2-n8n/            # n8n hands-on workshop infra (Sorbonne course)
├── scripts/                        # generate-index.py, check-overflow-visual.js, cite/, ...
├── docs/
│   ├── courses/sorbonne-m2/        # Course-specific docs:
│   │   ├── course-identity.md  course-architecture.md  student-group-project.md
│   │   ├── n8n-student-guide.md  outline.md  todos.md  student-sheets/
│   │   ├── notes/  qcm/  research/  plans/  sources/   # sources/ gitignored except READMEs
│   ├── talks/                      # Per-talk specs/sources:
│   │   ├── station-f/  gustave-eiffel-agents/  capgemini-ai-agents/
│   ├── references/                 # Generic reusable standards (slides AND writing):
│   │   ├── slide-creation-standards.md  workflow-new-slides.md
│   │   ├── writing-standards.md  workflow-new-article.md  great-medium-article.md
│   │   ├── authority-map.md/.yaml  cite-skill-backlog.md  overflow-remediation-playbook.md
│   │   └── workflow-citation-audit.md
│   ├── superpowers/                # Plans + specs
│   └── archive/slides-v1/          # Pre-restructuring slide archive
└── dist/                           # Generated output (gitignored): html/ pptx/ pdf-full/
```

**Naming conventions:**
- Course decks: `slides/sorbonne-m2-2026/session-XX/` (XX = 01–05), files `A-slug.md`, `B-slug.md`, `C-slug.md` (letter prefix orders within a session). Session 5 has only deck A.
- Standalone talks: one top-level dir per event under `slides/` (group multiple decks only when they belong to the same event, e.g. `station-f/`). Add each to `slides/index.manifest.yml` with its date.
- Assets: `assets/` per deck dir, source-prefix subdirs (`ng01/`, `ng02/`, `ng03/`, `infographics/`).
- Build output mirrors source layout: `slides/<rel>.md` → `dist/{html,pptx,pdf-full}/<rel>.{html,pptx,pdf}`. Each deck's `assets/` is symlinked into its output dir so relative refs resolve.
- English names for files/dirs. Original topic-based decks archived at `docs/archive/slides-v1/`.
- **No spaces in slide or asset filenames.** Make's prereq parser splits on whitespace, so a file like `foo bar.png` becomes two prereqs and breaks the build. Use kebab-case (`foo-bar.png`) or snake_case (`foo_bar.png`).

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
- Image-heavy slides use `<!-- _class: img-right -->` with `![bg right:55% contain]` (compressed 20px text, large image)

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
  - **Exception — standalone talks** (e.g. `slides/station-f/`): English body, same technical-term convention. Audiences are international. Per-talk source-of-truth lives under `docs/talks/<event>/` (e.g. `docs/talks/station-f/spec.md`).
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
- `img-right` slides (`bg right:55%`): budget **~6–8 bullets + sources** (image is main content, text = annotations)
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
make build      # Incremental: HTML → PDF → PPTX (only rebuilds what changed)
make html       # HTML only → dist/html/<deck>/ (+ prebuilt HTML, regenerates index)
make pdf-full   # Full-content PDFs → dist/pdf-full/<deck>/
make pptx       # PPTX → dist/pptx/<deck>/
make preview    # Launch Marp preview server
make index      # Regenerate dist/html/index.html from slides/index.manifest.yml
make sync       # Sync dist/pptx/ to GDrive via rclone (not configured currently)
make guide      # Build the n8n student guide DOCX
make clean      # Remove dist/
make build-<NAME>  # Build one slides/<NAME>/ dir only (e.g. make build-station-f)
```

**Two build systems:**
- **Marp** (default) — Markdown decks under `slides/<deck>/` → `dist/{html,pptx,pdf-full}/<deck>/`,
  preserving the source layout. Per-file pattern rules → builds are incremental: only files whose
  `.md`, `assets/`, theme CSS, or `.marprc.yml` changed get rebuilt.
- **frontend-slides** (the `/frontend-slides` skill) — for polished standalone HTML decks
  generated from portable Markdown content (e.g. `slides/capgemini-ai-agents/`). The committed
  `.html` is copied into `dist/html/<deck>/` by `make html` and linked from the index via a
  `prebuilt_html` entry in `slides/index.manifest.yml`. See that deck's README to regenerate.

**The index** (`dist/html/index.html`) is generated by `scripts/generate-index.py` from
`slides/index.manifest.yml` — the single source of truth for which decks appear, their group
labels, dates, and order (talks sorted newest-first; the Sorbonne course grouped together).
Adding a new talk = a new deck dir + one manifest entry with a `date`.

## Citation Audit Skill

The `/cite` skill family is **globally installed** (symlinked into `~/.claude/skills/cite*`
from Louis's dotfiles) and works in **any repo** — it is no longer project-specific. Use the
`/cite <file>` orchestrator, or the three phase-skills `/cite-diagnose`, `/cite-remediate`,
`/cite-correct`. The skills carry their own bundled validators and authority-map under
`~/.claude/skills/cite/`. Per-run state lives at `docs/citation-audit/<slug>/` (gitignored).

**Repo-local pieces (build-only mirror, NOT used by the skill):** `scripts/cite/` is a local
copy of the validators used solely by the Makefile — `make check` / `make lint-authority-map`:
- `scripts/cite/lint_authority_map.py` — authority-map .md/.yaml sync check (wired into `make check`)
- `scripts/cite/validate_claim.py`, `tier_lookup.py`, `target_scope.py` — same contracts
- 23 unit tests at `scripts/cite/tests/`, run with `pytest scripts/cite/tests/`

**Authority map:** `docs/references/authority-map.{md,yaml}` is this repo's roster, and doubles
as the optional **per-project overlay** the global skill accepts (passed as an extra `--map`).
The global skill's own `~/.claude/skills/cite/memory/authority-map.yaml` is **shared mutable
state across all repos** — `/cite-correct`'s auto-promote writes accumulated learnings there.
- `docs/references/cite-skill-backlog.md` — self-improvement tracker

Design specs (historical): `docs/superpowers/specs/2026-04-12-cite-skill-design.md` (v1),
`docs/superpowers/specs/2026-04-13-cite-skill-v2-design.md` (v2 — validators + least-privilege).

## Attribution

- **Andrew Ng / DeepLearning.AI**: CC BY-SA 2.0 — cite DeepLearning.AI as source
  - Footer: `Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0`
- **Kevin Vu / Dauphine**: archived materials, attribution TBD
- **Research decks**: original content based on cited sources (URLs in slide `<small>` tags)
  - Footer: `Recherche [Topic] 2024–2026 · Données publiques`
- **Multi-source decks**: use `Sources multiples · DeepLearning.AI CC BY-SA 2.0` when combining Andrew Ng + research content

## Slide Decks

### Active session decks

| Path | Title | Slides |
|------|-------|--------|
| `slides/sorbonne-m2-2026/session-01/A-genai-fondamentaux.md` | L'IA Générative : ce qu'elle sait faire | 37 |
| `slides/sorbonne-m2-2026/session-01/C-premier-projet-ia.md` | Votre premier projet IA | 25 |
| `slides/sorbonne-m2-2026/session-02/A-llms.md` | Les LLMs : comprendre et utiliser | 45 |
| `slides/sorbonne-m2-2026/session-02/B-evaluer-ia.md` | Évaluer l'IA | 21 |
| `slides/sorbonne-m2-2026/session-02/C-n8n-openrouter.md` | Classification par LLM avec OpenRouter | 16 |
| `slides/sorbonne-m2-2026/session-03/A-embeddings.md` | Embeddings : Le GPS du sens | 9 |
| `slides/sorbonne-m2-2026/session-03/B-rag.md` | RAG : Retrieval Augmented Generation | 25 |
| `slides/sorbonne-m2-2026/session-03/C-agents.md` | Agents IA : du workflow à l'autonomie | 44 |
| `slides/sorbonne-m2-2026/session-04/A-methodologie-projet.md` | Méthodologie projet IA | 17 |
| `slides/sorbonne-m2-2026/session-04/B-ecosysteme-ia.md` | L'écosystème IA | 22 |
| `slides/sorbonne-m2-2026/session-04/C-business-models.md` | Business Models & Cas Réels | 14 |
| `slides/sorbonne-m2-2026/session-05/A-regulation-ethique.md` | Régulation & IA responsable | 27 |

### Standalone talks (English — scoped exception)

One dir per event under `slides/`; each has a `date` in `slides/index.manifest.yml`
and per-talk docs under `docs/talks/<event>/`.

| Path | Title | Date | Build |
|------|-------|------|-------|
| `slides/capgemini-ai-agents/` | AI Agents & Claude Code — Tech Lab | 2026-06-18 | frontend-slides (HTML) |
| `slides/gustave-eiffel-agents/agents.md` | Building AI Agents | 2026-06-01 | Marp |
| `slides/pruna/sdxl_pruna_slides.md` | Optimizing SDXL Inference | 2026-05-28 | Marp |
| `slides/station-f/A-state-of-the-field.md` | Building With AI — State of the Field (25) | 2026-04-15 | Marp |
| `slides/station-f/B-building-with-ai.md` | Building With AI — Part B (15) | 2026-04-15 | Marp |

- Station F source of truth: `docs/talks/station-f/spec.md`; source archives `docs/talks/station-f/sources/` (Raschka, Latent Space, MiroFish).
- Capgemini: portable content in `slides/capgemini-ai-agents/content/` (genericized; branding removed); provenance in `docs/talks/capgemini-ai-agents/context.md`; regenerate the HTML via the frontend-slides skill (see the deck README).

### Evaluation reference decks

| Path | Title | Slides |
|------|-------|--------|
| `slides/sorbonne-m2-2026/evaluation/A-eval-regression.md` | Évaluation : Regression | 27 |
| `slides/sorbonne-m2-2026/evaluation/B-eval-classification.md` | Évaluation : Classification | 30 |
| `slides/sorbonne-m2-2026/evaluation/C-eval-computer-vision.md` | Évaluation : Computer Vision | 31 |
| `slides/sorbonne-m2-2026/evaluation/D-eval-llm.md` | Évaluation : LLMs | 45 |

### Archived / extra decks

| Path | Title | Slides |
|------|-------|--------|
| `slides/sorbonne-m2-2026/extra-decks/architectures.md` | Tour des architectures (CNN, RNN, GAN, Transformer) | 4 |
| `slides/sorbonne-m2-2026/extra-decks/D-biais-ethique.md` | Biais et éthique : introduction | 3 |
| `slides/sorbonne-m2-2026/extra-decks/A-prompt-au-produit.md` | Du Prompt au Produit *(ex-S2-A, absorbed → S3-B)* | 18 |
| `slides/sorbonne-m2-2026/extra-decks/B-ingenierie-ia.md` | L'Ingénierie IA *(ex-S2-B, absorbed → S3-A)* | 17 |
| `slides/sorbonne-m2-2026/extra-decks/B-au-dela-des-llms.md` | L'IA au-delà des LLMs *(ex-S1-B, prompting → S2-A)* | 23 |
| `slides/sorbonne-m2-2026/extra-decks/A-evaluer-solution-ia.md` | Évaluer une solution IA *(ex-S3-A, replaced by S2-B)* | 18 |
| `slides/sorbonne-m2-2026/extra-decks/B-methodologie-projet-v1.md` | Méthodologie projet IA v1 *(ex-S3-B, restructured)* | 17 |
| `slides/sorbonne-m2-2026/extra-decks/A-rag-agents-v1.md` | RAG & Agents IA v1 *(ex-S3-A, split → A-rag-embeddings + B-agents)* | 34 |
| `slides/sorbonne-m2-2026/extra-decks/C-demo-agents-v1.md` | Agents en action *(ex-S3-C, absorbed → B-agents)* | 11 |
| `slides/sorbonne-m2-2026/extra-decks/A-rag-embeddings-v1.md` | RAG & Embeddings v1 *(split → A-embeddings + B-rag)* | 31 |
| `slides/sorbonne-m2-2026/extra-decks/B-context-engineering-deep.md` | Context Engineering approfondi *(overflow from C-agents)* | 5 |
| `slides/sorbonne-m2-2026/extra-decks/D-methodologie-projet-v1.md` | Méthodologie projet IA v1 *(ex-S3-D, restructured → S4-A)* | 25 |

## Writing

Online articles and essays live under `writing/`. The standards mirror the slide system:
- `docs/references/writing-standards.md` — single source of truth for article rules (distilled from `docs/references/great-medium-article.md`, the deep research-backed reference).
- `docs/references/workflow-new-article.md` — from-scratch / from-research article workflow (mirrors `workflow-new-slides.md`).
- `writing/medium/<slug>/` — one dir per article project (README + `outline.md`; draft prose later).
- `writing/ai-safety-stance/` — personal essay + Coefficient Giving grant + dialectic run.

## Source Materials

| Path | Contents |
|------|----------|
| `docs/courses/sorbonne-m2/sources/courses/AndrewNg/W1.pdf` | Andrew Ng "Generative AI for Everyone" W1 (88p) |
| `docs/courses/sorbonne-m2/sources/courses/AndrewNg/W2.pdf` | Andrew Ng "Generative AI for Everyone" W2 (57p) |
| `docs/courses/sorbonne-m2/sources/courses/AndrewNg/W3.pdf` | Andrew Ng "Generative AI for Everyone" W3 (49p) |
| `docs/courses/sorbonne-m2/sources/courses/KevinVu/cours_*.html` | Kevin Vu WebSlides course decks (7 sessions) |
| `docs/courses/sorbonne-m2/sources/courses/KevinVu/cours_*.pdf` | Kevin Vu course PDFs |
| `docs/archive/slides-v1/` | Pre-restructuring slide archive (15 topic directories) |
| `docs/courses/sorbonne-m2/research/` | Research pipeline outputs (13 topics, reports + raw data) |
| `docs/courses/sorbonne-m2/notes/Outline - 2026 M2 - ML & DeepTech.md` | Course plan, themes, and session structure |
| `docs/courses/sorbonne-m2/notes/Meeting Notes - Kevin Vu M2 Sorbonne.md` | Notes from meeting with previous teacher |
| `docs/courses/sorbonne-m2/` | Course-specific docs (identity, architecture, qcm, research, sources, notes, student project) |
| `docs/references/` | Reusable standards (slide + writing creation, workflows, citation/authority map) |
