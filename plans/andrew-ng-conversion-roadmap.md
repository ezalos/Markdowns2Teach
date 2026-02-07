# Andrew Ng "Generative AI for Everyone" — Conversion Roadmap

<!-- ABOUTME: Consolidated plan for converting Andrew Ng's course PDFs into 3 Marp slide decks. -->
<!-- ABOUTME: Targets 30-50 slides per deck, mapped to Sorbonne session structure. -->

## Overview

The 194 PDF pages compress to ~95–125 Marp slides, organized into **3 consolidated decks** (one per original Ng week). Each deck targets **30–50 slides** to avoid excessive PPTX switching during class.

| Deck | Source | Pages | Est. Slides | Target Session(s) |
|------|--------|-------|-------------|--------------------|
| 1 — Comprendre la Generative AI | W1.pdf | 88 | 42–50 | Sessions 1–2 |
| 2 — Construire avec la Generative AI | W2.pdf | 57 | 38–47 | Sessions 2–3 |
| 3 — L'IA dans l'entreprise et la société | W3.pdf | 49 | 33–44 | Sessions 3–5 |
| **Total** | | **194** | **113–141** | |

### Directory Structure

```
slides/andrew-ng-genai/
├── deck-01-comprendre-genai/
│   ├── 01-comprendre-genai.md          # Single consolidated deck
│   └── assets/                          # Extracted images from W1
├── deck-02-construire-genai/
│   ├── 01-construire-genai.md
│   └── assets/                          # Extracted images from W2
└── deck-03-ia-business-societe/
    ├── 01-ia-business-societe.md
    └── assets/                          # Extracted images from W3
```

> **Note:** The existing POC at `ch01-intro-genai/01-what-is-genai.md` (5 slides) will be absorbed into Deck 1. The `ch01-intro-genai/` directory and its 99 extracted images move to `deck-01-comprendre-genai/assets/`.

---

## Conversion Principles

### Content Compression
- Andrew Ng uses **progressive reveal** (same slide built across 2–4 pages). Collapse into single Marp slides with the final state.
- Target ratio: ~2 PDF pages → 1 Marp slide (194p → ~120 slides).
- Drop "optional" section markers where content is still relevant — integrate instead of segregating.

### Language & Framing
- French body text, **English technical terms used directly** (no translations).
- Business-framed for M2 Entrepreneurship students: emphasize startup/business angles.
- Add **engagement questions** (1–2 per major section) to drive class discussion.

### Stats & Examples Updates for 2026
- Update economic impact figures if newer McKinsey/Goldman Sachs data is available.
- Replace tool screenshots (ChatGPT Nov 2022 era) with 2025–2026 equivalents where relevant.
- Add French/European context: Mistral AI, EU AI Act, GDPR implications.
- Add 2024–2026 case studies: Klarna AI assistant, L'Oréal beauty AI, Mistral Le Chat.

### Slide Numbering
- Flat per-file numbering: `# 01 — Title Here`
- Title slides and section dividers are NOT numbered.
- Numbering restarts in each `.md` file.

### Attribution
- Footer: `Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0`
- Required on every adapted slide deck.

---

## Image Strategy

### Extraction
- W1 images already extracted → `ch01-intro-genai/assets/` (99 images). Move to `deck-01-comprendre-genai/assets/`.
- Run `scripts/extract-images.sh` on W2 and W3 when converting those decks.
- Filter: discard images <200px wide (logos, masks, decorative).

### Usage in Slides
- **Diagrams/charts** (tables, flow diagrams, scaling curves): `![bg left:50%](assets/img-XXX.png)` or `![bg right:50%]`.
- **Screenshots** (ChatGPT, Bard, etc.): replace with 2025–2026 equivalents where possible.
- **Progressive-reveal sequences** (diffusion model steps): pick the final composite image or the 2 most illustrative frames.
- **Full-page diagrams** (lifecycle, RAG pipeline): `![bg contain](assets/img-XXX.png)`.

---

## Deck 1 — Comprendre la Generative AI

**File:** `slides/andrew-ng-genai/deck-01-comprendre-genai/01-comprendre-genai.md`
**Source:** W1.pdf (88 pages) · **Target: 42–50 slides**
**Sessions:** 1–2

This deck covers everything a business student needs to understand what GenAI is, what it can do, and how to use it effectively. It flows from "what is AI?" through concrete applications to practical prompting skills.

### Section A: What is Generative AI? (W1 p3–29, ~15–17 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Rise of GenAI | p3–5 | 2 | Stats ($2.6–4.4T McKinsey), definition, chatbot screenshots |
| GenAI modalities | p6–10 | 2 | Developer tool, AI already pervasive, image/audio/video generation |
| Course overview | p11–13 | 1 | What you'll learn (3 pillars) |
| AI landscape | p13–17 | 3 | AI categories bubble diagram, supervised learning, scaling curves |
| How LLMs work | p18–19 | 2 | Next-word prediction, iterative generation |
| LLMs as thought partner | p20–25 | 3 | Writing partner, web search vs. LLM comparison |
| AI as general purpose tech | p26–29 | 2 | Electricity analogy, Writing/Reading/Chatting taxonomy |

**Key diagrams:** AI categories bubble (p14), supervised learning table (p16), scaling curves (p17), next-word prediction (p18–19), web search vs. LLM (p23), task taxonomy (p28).

### Section B: GenAI Applications (W1 p30–55, ~17–20 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Writing applications | p30–37 | 5 | Brainstorming, press releases (generic→improved), translation (Hindi→pirate) |
| Reading applications | p38–48 | 7 | Proofreading, summarization, email routing, prompt anatomy, reputation monitoring |
| Chatting applications | p49–55 | 5 | Customer service bot, specialized chatbots, deployment maturity spectrum |

**Key diagrams:** Call center pipeline (p41, p43), annotated prompt anatomy (p47), reputation dashboard (p48), chatbot deployment spectrum (p53).

**Teaching notes:**
- Press release example (generic→improved) is excellent for showing context importance.
- Translation examples (formal Hindi→spoken Hindi→pirate) demonstrate register awareness.
- Deployment advice (internal→human-in-loop→direct) is directly relevant for entrepreneurs.

### Section C: Capabilities, Limits & Prompting (W1 p56–88, ~13–16 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| What LLMs can/cannot do | p56–62 | 3 | "Fresh college grad" heuristic, knowledge cutoffs |
| Hallucinations & limits | p63–71 | 4 | Fake court cases, context length, structured vs. unstructured data, bias |
| Tips for prompting | p72–78 | 4 | Be specific, chain-of-thought, iterate, prompt cycle |
| Image generation | p79–88 | 2–3 | Diffusion models (trim to key visuals only — apple noise, watermelon denoising) |

**Key diagrams:** Hallucination example (p64), structured vs. unstructured (p69), chain-of-thought table (p76), prompt iteration cycle (p78), diffusion sequence (p81, p85).

**Teaching notes:**
- "Fresh college grad" heuristic = the single most memorable mental model for evaluating LLM capabilities.
- Hallucination courtroom example sets realistic expectations.
- Image generation section: trim heavily — focus on the visual "magic", not the math. 2–3 slides max.
- Prompting tips pair naturally with a live prompting exercise.

---

## Deck 2 — Construire avec la Generative AI

**File:** `slides/andrew-ng-genai/deck-02-construire-genai/01-construire-genai.md`
**Source:** W2.pdf (57 pages) · **Target: 38–47 slides**
**Sessions:** 2–3

This deck transitions from "using GenAI" to "building with GenAI". It covers the project lifecycle, costs, key technologies (RAG, fine-tuning), and model selection — everything an entrepreneur needs to scope and evaluate an AI project.

### Section A: From Using to Building (W2 p2–10, ~6–7 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Software application categories | p2–4 | 2 | Writing/Reading/Chatting in apps, FAQ bot, sentiment classification |
| Supervised vs. prompt-based dev | p5–8 | 3 | LSTM code vs. 3-line prompt, workflow comparison (7 months → hours) |
| Jupyter notebook intro | p9–10 | 1 | Optional hands-on setup |

**Key diagrams:** Three-column app examples (p3), workflow comparison timeline (p8).

**Teaching note:** The 7 months → hours/days comparison is the single most powerful business argument for GenAI adoption. Lead with it.

### Section B: GenAI Project Lifecycle (W2 p11–23, ~9–12 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Four-stage lifecycle | p11–15 | 4 | Scope→Build→Evaluate→Deploy, feedback loops, evaluation catches errors |
| Tools to improve performance | p16–19 | 3 | Prompting→RAG→Fine-tune→Pretrain (progressive pyramid) |
| BettaBurgers walkthrough | p20–23 | 3 | Concrete lifecycle example: chatbot errors→fixes→deploy→monitor |

**Key diagrams:** Full lifecycle with feedback loops (p15), iterative prompting cycle (p16), four tools pyramid (p19).

### Section C: Costs, RAG & Fine-Tuning (W2 p24–49, ~18–22 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Cost intuition | p24–26 | 3 | Token pricing table, what is a token, $0.08/hour-of-content calculation |
| RAG explained | p27–34 | 6 | General vs. RAG chatbot, 3-step process, applications, LLM as reasoning engine |
| Fine-tuning | p35–44 | 5 | Pretraining vs. fine-tuning, 3 reasons (style, knowledge, small models), distillation |
| Pretraining & model selection | p45–49 | 4 | BloombergGPT, model sizes (1B/10B/100B+), open vs. closed source |

**Key diagrams:** Token pricing + visualization (p25), 3-step RAG process (p29–30), RAG applications (p31–33), pretraining vs. fine-tuning (p36), model size table (p48), open vs. closed source (p49).

**Teaching notes:**
- Update token pricing to 2025–2026 rates (GPT-4o, Claude 3.5, Mistral).
- The "LLM as reasoning engine" concept (p34) is key for entrepreneurs evaluating AI products.
- Add Mistral and Llama to the open-source discussion. Add Hugging Face as the ecosystem hub.
- BloombergGPT = good "when to pretrain" case study.

### Section D: Advanced Topics (W2 p50–57, ~5–8 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Instruction tuning & RLHF | p50–54 | 2–3 | How models learn to follow instructions, helpful/honest/harmless |
| Tool use & agents | p55–57 | 3–5 | Tool calls (ORDER, CALCULATOR), multi-step agent workflows |

**Teaching notes:**
- RLHF: keep conceptual. The reward model scoring table is intuitive enough for non-engineers.
- Tool use & agents: despite being "optional" in Ng's course, this is **HIGH priority for 2026**. Expand with current examples: MCP, Claude computer use, GPT Actions, Devin-style coding agents.

---

## Deck 3 — L'IA dans l'entreprise et la société

**File:** `slides/andrew-ng-genai/deck-03-ia-business-societe/01-ia-business-societe.md`
**Source:** W3.pdf (49 pages) · **Target: 33–44 slides**
**Sessions:** 3–5

This deck is the most strategically important for entrepreneurs. It covers how to analyze jobs for AI potential, build teams, understand sector impacts, and navigate ethical/regulatory concerns. Supplement thin sections with EU AI Act and French/European case studies.

### Section A: Daily LLM Usage (W3 p2–7, ~3–4 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Use case examples | p2–7 | 3–4 | Writing assistant, marketer brainstorming, recruiter summarizing, programmer coding |

**Teaching note:** Warm-up section. Pair with "show us your ChatGPT/Claude history" class activity.

### Section B: Task Analysis Framework (W3 p8–22, ~14–18 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| "AI automates tasks, not jobs" | p8–11 | 3 | Customer service task breakdown, augmentation vs. automation |
| Technical feasibility vs. business value | p12–13 | 2 | Two-axis evaluation framework, O*NET as resource |
| Job analysis examples | p14–17 | 3 | Programmer, lawyer, landscaper — contrasting AI potential profiles |
| New workflows & opportunities | p18–22 | 4 | Surgeon time reallocation, legal review, marketing automation, customer task analysis |

**Key diagrams:** Customer service task table (p9), augmentation vs. automation (p10), feasibility vs. value framework (p12), workflow before/after charts (p19–21).

**Teaching notes:**
- This is the **most strategically important section** for entrepreneurs — understanding which tasks to target.
- The marketing automation example (p21) shows how GenAI creates entirely new workflows — powerful for entrepreneurial thinking.
- The landscaper example (p17, mostly "Low") is a great contrast — not all jobs are equally impacted.

### Section C: Teams & Sector Analysis (W3 p23–30, ~6–8 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Building GenAI teams | p23–27 | 3 | Key roles, small team configs, "prompt engineer" not a dedicated role |
| Automation potential by sector | p27–30 | 3–4 | Higher-paid jobs = more exposure, McKinsey functional/industry analysis |

**Key diagrams:** AI exposure vs. wage scatter plot (p28), McKinsey functional impact chart (p29), industry sector bar chart (p30).

**Teaching notes:**
- Team building is directly relevant for students building startups. Emphasize: "prompt engineer" is a skill, not a role.
- Counterintuitive finding: higher-paid jobs face MORE exposure. Great discussion trigger.
- Add French/European company examples to the sector analysis.

### Section D: AI Concerns & Responsible AI (W3 p31–49, ~10–14 slides)

| Topic | Source Pages | Est. Slides | Key Content |
|---|---|---|---|
| Bias & toxicity | p31–33 | 2 | Gender bias example, RLHF as mitigation |
| Job displacement | p34–37 | 3 | Radiologist debate, O*NET task lists, Langlotz quote |
| Existential risk | p38–39 | 2 | Real AI harms (car crashes, flash crash, sentencing), balanced perspective |
| AGI | p41–42 | 1 | Definition, what it could do |
| Responsible AI framework | p43–45 | 3 | Five dimensions: fairness, transparency, privacy, security, ethical use |
| Course summary | p46–49 | 1 | Three-pillar recap |

**Key quotes:** "AI won't replace radiologists. But radiologists that use AI will replace radiologists that don't." (Curtis Langlotz)

**Teaching notes:**
- Expand responsible AI section with **EU AI Act** content (risk tiers, prohibited practices, transparency obligations).
- Add GDPR angle for data privacy — directly relevant to French/European students.
- Add 2024–2026 examples: Klarna replacing 700 agents, EU fining companies for AI violations.
- AGI section is very brief — can fold into the concerns discussion rather than standalone.

### Expansion Opportunities (to reach 40+ slides)

If this deck runs under 35 slides from Andrew Ng content alone, supplement with:
- **EU AI Act deep-dive** (risk tiers, compliance timeline): +3–5 slides
- **French AI ecosystem** (Mistral AI, Hugging Face, French Tech): +2–3 slides
- **GDPR & AI** (data minimization, right to explanation, CNIL guidance): +2–3 slides
- **Case studies** (Klarna, L'Oréal, BNP Paribas AI adoption): +2–3 slides

---

## Session Mapping

How the consolidated decks map to the 5 Sorbonne sessions:

| Session | Theme | Andrew Ng Deck | Deck Sections Used | Supplementary |
|---|---|---|---|---|
| 1 | Fundamentals & AI landscape | **Deck 1** (first half) | Sections A–B | Kevin Vu intro, live demo |
| 2 | Prompt engineering & tools | **Deck 1** (second half) + **Deck 2** (start) | Deck 1 Section C + Deck 2 Section A | Teachable Machine, Voiceflow |
| 3 | Framing & managing AI projects | **Deck 2** (remainder) | Sections B–D | CRISP-DM, AI Canvas, Build vs Buy |
| 4 | AI business models & strategy | **Deck 3** (first half) | Sections A–C | Business model patterns, unit economics |
| 5 | Ethics, governance & presentations | **Deck 3** (second half) | Section D + expansions | EU AI Act, student project pitches |

> **Presentation flow:** In sessions where only part of a deck is used, the presenter can stop at a section break and resume next session. Marp HTML allows jumping to any slide by number, and PPTX supports bookmarks.

---

## Next Steps

1. Rename `ch01-intro-genai/` → `deck-01-comprendre-genai/`, move assets
2. Extract images from W2 and W3 PDFs using `scripts/extract-images.sh`
3. Convert Deck 1 first (builds on existing POC content, expands to full 42–50 slides)
4. Convert Deck 2, then Deck 3
5. Update stats and examples for 2025–2026 context during conversion
6. Add engagement questions and hands-on activity prompts
7. Run `make check` after each deck to catch overflow
