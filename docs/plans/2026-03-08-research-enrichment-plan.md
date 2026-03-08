# Research Enrichment Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Research 20 URLs across 7 topics, capture charts, and enrich 6 existing slide decks with the top 20% most impactful facts and visuals.

**Architecture:** Two-wave parallel approach. Wave 1 fetches all content and captures all charts in parallel. Wave 2 writes/modifies slides per deck, replacing weak slides or inserting new ones. Final pass updates course-architecture.md.

**Tech Stack:** Marp slides (Markdown), `scripts/capture-charts.js` (Puppeteer chart capture), `make check` (overflow linter), tavily/web-fetch for URL research.

**Key references:**
- `docs/references/slide-creation-standards.md` — all slide conventions
- `docs/references/workflow-new-slides.md` — slide creation workflow
- `CLAUDE.md` — project conventions

---

## Wave 1: Research + Chart Capture (parallel)

All 7 tasks in this wave are independent and should run in parallel.

---

### Task 1: Research — LLM (3 URLs → S2-A)

**URLs:**
1. https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models
2. https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
3. https://vintagedata.org/blog/posts/synthetic-pretraining (counter-argument to #2)
4. https://epoch.ai/blog/open-models-report

**Existing coverage in S2-A (40 slides):**
- Training costs: slides 13-14 cover BERT→GPT-4 costs + efficiency gains. Could be enriched with Epoch AI's detailed cost breakdowns and charts.
- Data limits: **NO COVERAGE** — significant gap. Only indirect mention of data volumes in slide 09.
- Open-source lag: slides 19-20, 27 cover open-weights access and "David vs Goliath". Could be enriched with Epoch's quantitative lag analysis.

**Step 1: Fetch and extract key facts from all 4 URLs**

Use web fetch/tavily extract on each URL. For each, extract:
- Key statistics with exact numbers
- Main thesis/argument
- Charts described (title, what they show)
- Quotable conclusions

**Step 2: Write structured summary**

Save to `/tmp/research-llm.md` with sections:
```
## Training Costs
- [fact] [number] [source URL]
...
## Data Limits
- [fact] [number] [source URL]
- [counter-argument from vintagedata]
...
## Open-Source Lag
- [fact] [number] [source URL]
...
## Charts to capture
- [page URL] → [chart description] → [suggested filename]
```

---

### Task 2: Research — Ecosystem (4 URLs → S4-A)

**URLs:**
1. https://epoch.ai/blog/inference-economics-of-language-models
2. https://epoch.ai/blog/can-ai-scaling-continue-through-2030
3. https://epoch.ai/blog/what-will-ai-look-like-in-2030
4. https://epoch.ai/blog/what-do-economic-value-benchmarks-tell-us

**Existing coverage in S4-A (18 slides):**
- Inference economics: slide 03 mentions "÷280 en 2 ans", slide 09 has pricing. Light coverage — Epoch's deep analysis would add substance.
- Scaling to 2030: **NO COVERAGE** — deck only goes to 2026-2027.
- AI in 2030: **NO COVERAGE** — no forward-looking content.
- Economic benchmarks: slide 01 has adoption stats, slide 03 has ROI (95% pilots = zero ROI). Could be enriched.

**Step 1: Fetch and extract from all 4 URLs**
**Step 2: Write structured summary to `/tmp/research-ecosystem.md`**

Sections: Inference Economics, Scaling Through 2030, AI in 2030, Economic Value Benchmarks, Charts to capture.

---

### Task 3: Research — Ethics (4 URLs → S5-A)

**URLs:**
1. https://www.darioamodei.com/essay/the-adolescence-of-technology
2. https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/unless-its-governance-changes-anthropic-is-untrustworthy
3. https://www.anthropic.com/news/claudes-constitution
4. https://www.anthropic.com/constitution

**Existing coverage in S5-A (23 slides):**
- Dario Amodei: **ZERO** mentions
- Anthropic: ONE mention (slide 17, Responsible Scaling Policy line)
- AI constitutions: **ZERO** mentions
- Good insertion points: after slide 17 (Responsible AI frameworks) or after slide 18 (Discussion auto-regulation vs loi dure)

**Step 1: Fetch and extract from all 4 URLs**

For Amodei essay: extract key arguments, memorable quotes, the "adolescence" metaphor.
For LessWrong critique: extract the core criticism points (balanced view — present both sides).
For Anthropic constitution: extract the principles, how it works, what makes it novel.

**Step 2: Write structured summary to `/tmp/research-ethics.md`**

Sections: Amodei's Vision, Anthropic Criticism (balanced), Claude's Constitution, Charts/diagrams to capture.

---

### Task 4: Research — Agents (1 URL → S3-A)

**URL:**
1. https://arxiv.org/pdf/2601.10825

**Existing coverage in S3-A (30 slides):**
- Agents section: slides 14-27 cover ReAct, Tool Use, MCP, Skills, failure modes, ecosystem
- This arxiv paper likely adds academic framework/taxonomy

**Step 1: Fetch and extract from the arxiv paper**

Note: This is a PDF. Use web fetch on the HTML version if available, or extract key sections.
Focus on: taxonomy of agent architectures, key findings, failure mode analysis, benchmarks.

**Step 2: Write structured summary to `/tmp/research-agents.md`**

---

### Task 5: Research — RAG (3 URLs → S3-A)

**URLs:**
1. https://arxiv.org/html/2508.21038v1 (BM25 DeepMind)
2. https://jxnl.co/writing/category/rag/#why-cognition-does-not-use-multi-agent-systems
3. https://jxnl.co/writing/2025/08/28/context-engineering-index/

**Existing coverage in S3-A:**
- RAG section: slides 01-13 cover pipeline, chunking, embeddings, vector DBs, hybrid search, reranking
- Slide 07 already covers "Hybrid Search" — BM25 paper could strengthen this
- Context engineering: **NOT COVERED** — could be a valuable addition

**Step 1: Fetch and extract from all 3 URLs**
**Step 2: Write structured summary to `/tmp/research-rag.md`**

---

### Task 6: Research — Eval (2 URLs → S2-B)

**URLs:**
1. https://lmcouncil.ai/benchmarks
2. https://epoch.ai/benchmarks/eci

**Existing coverage in S2-B (18 slides):**
- LLM benchmarks: slides 10-11 cover MMLU/GSM8K/HumanEval + Chatbot Arena
- These new resources could enrich with more comprehensive benchmark landscape

**Step 1: Fetch and extract from both URLs**

For LM Council: extract benchmark categories, scoring methodology, key rankings.
For Epoch ECI: extract the Economic Competence Index methodology, key findings.

**Step 2: Write structured summary to `/tmp/research-eval.md`**

---

### Task 7: Research — Engineering (1 URL → S3-B)

**URL:**
1. https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html

**Existing coverage in S3-B (27 slides):**
- Scattered pitfalls: slides 06 (common errors), 09 (red flags), 12 (Google Rule of ML #1)
- No dedicated "engineering pitfalls" section

**Step 1: Fetch and extract key pitfalls**

Focus on: numbered pitfalls, memorable examples, data claims.

**Step 2: Write structured summary to `/tmp/research-engineering.md`**

---

### Task 8: Chart Capture — Epoch AI pages (parallel with research)

**Pages with likely interactive charts:**
1. https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models → `slides/session-02/assets/epoch/`
2. https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data → `slides/session-02/assets/epoch/`
3. https://epoch.ai/blog/open-models-report → `slides/session-02/assets/epoch/`
4. https://epoch.ai/blog/inference-economics-of-language-models → `slides/session-04/assets/epoch/`
5. https://epoch.ai/blog/can-ai-scaling-continue-through-2030 → `slides/session-04/assets/epoch/`
6. https://epoch.ai/blog/what-will-ai-look-like-in-2030 → `slides/session-04/assets/epoch/`
7. https://epoch.ai/blog/what-do-economic-value-benchmarks-tell-us → `slides/session-04/assets/epoch/`
8. https://epoch.ai/benchmarks/eci → `slides/session-02/assets/epoch/`

**Step 1: List charts on each page**

For each URL, run:
```bash
node scripts/capture-charts.js <url> --list
```

**Step 2: Capture all charts**

For each URL with detected charts:
```bash
# S2-A related (LLM topic)
node scripts/capture-charts.js <url> \
  -o slides/session-02/assets/epoch \
  -p <descriptive-prefix>

# S4-A related (Ecosystem topic)
node scripts/capture-charts.js <url> \
  -o slides/session-04/assets/epoch \
  -p <descriptive-prefix>

# S2-B related (Eval topic)
node scripts/capture-charts.js <url> \
  -o slides/session-02/assets/epoch \
  -p <descriptive-prefix>
```

**Step 3: Inventory captured files**

```bash
find slides/session-*/assets/epoch/ -name "*.png" -type f | sort
```

Save list to `/tmp/captured-charts.md` with: filename, source URL, what the chart shows.

---

### Task 9: Chart Capture — Non-Epoch pages

**Pages that may have downloadable images/charts:**
- https://lmcouncil.ai/benchmarks — may have benchmark comparison charts
- https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html — may have diagrams

**Step 1: Check for charts**
```bash
node scripts/capture-charts.js <url> --list
```

**Step 2: If charts found, capture to appropriate asset dirs**
- LM Council → `slides/session-02/assets/lmcouncil/`
- Chip Huyen → `slides/session-03/assets/huyenchip/`

---

## Wave 2: Slide Writing (per-deck)

After Wave 1 completes, use the research summaries and captured charts to write slides. Each task below is one deck modification.

**Before starting any deck:** Read the full existing deck + the relevant research summary from `/tmp/research-*.md` + the chart inventory from `/tmp/captured-charts.md`.

**For all slides:** Follow `docs/references/slide-creation-standards.md` strictly — citations, budget, language, format.

---

### Task 10: Write slides — S2-A LLMs (`slides/session-02/A-llms.md`)

**Read first:**
- Full content of `slides/session-02/A-llms.md`
- `/tmp/research-llm.md`
- `/tmp/captured-charts.md` (filter for session-02)

**Modifications:**

**A) Enrich slides 13-14 (Training costs):**
- Replace or enrich with Epoch AI's detailed cost breakdown data
- Add chart: training cost over time (from captured epoch charts)
- Ensure all new numbers have `[N]` citations + `<small>Sources</small>`

**B) NEW slides: Data limits / running out of data (insert after slide 14, in pipeline section):**
- Slide: "Les données d'entraînement : une ressource limitée ?" — present Epoch's analysis on data scarcity
- Slide: "Synthetic Data : la solution ?" — present the counter-argument from vintagedata.org
- Both sides must be presented (Louis explicitly asked for balance)
- Include chart if available from captured Epoch charts

**C) Enrich slides about open-source (19-20 or 27):**
- Add quantitative data from Epoch's open-models-report on the lag between open and closed
- Include chart showing the gap evolution over time
- Strengthen with specific numbers (months of lag, benchmark gaps)

**After writing:** Renumber all slides if insertions changed the sequence.

**Step 1: Read full deck**
**Step 2: Draft new/modified slides in isolation**
**Step 3: Insert into deck at correct positions**
**Step 4: Renumber all slides sequentially**
**Step 5: Run `make check` — fix any overflows**
**Step 6: Verify citations are complete**

---

### Task 11: Write slides — S4-A Ecosystem (`slides/session-04/A-ecosysteme-ia.md`)

**Read first:**
- Full content of `slides/session-04/A-ecosysteme-ia.md`
- `/tmp/research-ecosystem.md`
- `/tmp/captured-charts.md` (filter for session-04)

**Modifications:**

**A) Enrich slide 03 (Bulle ou boom) with inference economics data:**
- Add Epoch's analysis on inference cost trends and economics
- Possibly split into 2 slides if the content is rich enough

**B) NEW section: "L'IA en 2030" (insert before or after current section 5 "Applications & Synthèse"):**
- Slide: "Scaling compute : peut-on continuer jusqu'en 2030 ?" — Epoch's scaling analysis
- Slide: "À quoi ressemblera l'IA en 2030 ?" — Epoch's predictions
- Slide: "Valeur économique : que mesurent les benchmarks ?" — economic value analysis
- Include charts from captured Epoch images

**C) Possible discussion slide:** "En 2030, l'IA sera... — faites vos prédictions"

**Steps:** Same as Task 10 (read → draft → insert → renumber → check → verify).

---

### Task 12: Write slides — S5-A Ethics (`slides/session-05/A-regulation-ethique.md`)

**Read first:**
- Full content of `slides/session-05/A-regulation-ethique.md`
- `/tmp/research-ethics.md`

**Modifications:**

**A) NEW slides after slide 17-18 (Responsible AI section):**
- Slide: "Claude's Constitution : l'IA guidée par des principes" — Anthropic's constitution approach, how it works, key principles
- Slide: "Dario Amodei : l'adolescence de la technologie" — key arguments from the essay, the metaphor, what it means for governance
- Slide: "Les critiques : Anthropic tient-elle ses promesses ?" — balanced presentation of LessWrong criticism + Anthropic's position. Present BOTH sides fairly.

**B) Possible discussion enhancement for slide 18:**
- Could add a reference to Anthropic's self-regulation as a concrete example

**Steps:** Same pattern.

---

### Task 13: Write slides — S3-A RAG & Agents (`slides/session-03/A-rag-agents.md`)

**Read first:**
- Full content of `slides/session-03/A-rag-agents.md`
- `/tmp/research-rag.md`
- `/tmp/research-agents.md`

**Modifications:**

**A) Enrich slide 07 (Hybrid Search) with BM25 DeepMind findings:**
- Add the key insight from the paper about BM25's surprising resilience
- Cite the arxiv paper

**B) NEW slide(s): Context Engineering (insert after slide 13, before Agents section):**
- Slide: "Context Engineering : au-delà du RAG" — jxnl's framework for thinking about context
- Possibly: "Pourquoi Cognition n'utilise pas le multi-agent" — practical insight

**C) Enrich Agents section with arxiv survey findings:**
- Add taxonomy or framework from the paper to existing agent slides
- Strengthen failure modes (slide 24) with academic data if available

**Steps:** Same pattern.

---

### Task 14: Write slides — S2-B Eval (`slides/session-02/B-evaluer-ia.md`)

**Read first:**
- Full content of `slides/session-02/B-evaluer-ia.md`
- `/tmp/research-eval.md`
- `/tmp/captured-charts.md` (filter for epoch/lmcouncil)

**Modifications:**

**A) Enrich slides 10-11 (Benchmarks + Chatbot Arena):**
- Add LM Council as a resource/reference
- Add Epoch's Economic Competence Index as a new type of benchmark
- Possibly NEW slide: "ECI : mesurer la valeur économique de l'IA" with chart

**B) Add benchmark landscape chart if captured from LM Council or Epoch**

**Steps:** Same pattern.

---

### Task 15: Write slides — S3-B Méthodologie (`slides/session-03/B-methodologie-projet.md`)

**Read first:**
- Full content of `slides/session-03/B-methodologie-projet.md`
- `/tmp/research-engineering.md`

**Modifications:**

**A) NEW slides: AI Engineering Pitfalls (insert near slides 06/09 where pitfalls are mentioned):**
- Slide: "Les pièges de l'AI Engineering" — Chip Huyen's top pitfalls, business-framed
- Possibly a second slide with concrete examples
- Cite huyenchip.com

**Steps:** Same pattern.

---

## Wave 3: Final verification + documentation

---

### Task 16: Run overflow check on all modified decks

**Step 1: Run make check**
```bash
make check
```

**Step 2: Fix any overflows** using techniques from `slide-creation-standards.md` §2:
- Add `compact` class
- Split long slides
- Trim bullets

**Step 3: Run make html**
```bash
make html
```
Verify clean build.

---

### Task 17: Update course-architecture.md

**File:** `docs/references/course-architecture.md`

**Step 1: Read current file**
**Step 2: Update slide counts** for all 6 modified decks
**Step 3: Update content descriptions** in the "Détail par séance" section to reflect new topics added
**Step 4: Update "État des supports"** table with new slide counts

---

### Task 18: Commit all changes

**Step 1: Review all changes**
```bash
git status
git diff --stat
```

**Step 2: Commit**
```bash
git add slides/session-02/A-llms.md \
       slides/session-02/B-evaluer-ia.md \
       slides/session-02/assets/epoch/ \
       slides/session-03/A-rag-agents.md \
       slides/session-03/B-methodologie-projet.md \
       slides/session-03/assets/ \
       slides/session-04/A-ecosysteme-ia.md \
       slides/session-04/assets/epoch/ \
       slides/session-05/A-regulation-ethique.md \
       docs/references/course-architecture.md \
       docs/plans/2026-03-08-research-enrichment-design.md \
       docs/plans/2026-03-08-research-enrichment-plan.md

git commit -m "Enrich 6 decks with research from 20 external sources

Add slides on training costs, data limits, open-source lag (S2-A),
inference economics, AI scaling to 2030 (S4-A), Claude's constitution,
Dario Amodei essay (S5-A), BM25/context engineering (S3-A),
AI engineering pitfalls (S3-B), and ECI benchmarks (S2-B).
Capture Epoch AI charts. Update course-architecture.md.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```
