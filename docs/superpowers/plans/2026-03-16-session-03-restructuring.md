# Session 03 Restructuring Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split Session 03's A-rag-embeddings.md into A-embeddings.md + B-rag.md, rename B/C decks to C/D, and add 3 new slides to the RAG deck.

**Architecture:** Extract embeddings slides (04–12) into standalone deck A. Restructure remaining RAG slides with reordered intro and 2 new search-method slides + 1 new overview slide. Rename existing B-agents → C-agents, C-methodologie → D-methodologie, fix cross-references.

**Tech Stack:** Marp (markdown slides), PaperBanana (infographic generation), Make (build system)

**Spec:** `docs/superpowers/specs/2026-03-16-session-03-restructuring-design.md`

---

## Chunk 1: Create New Decks

### Task 1: Archive the original file

**Files:**
- Move: `slides/session-03/A-rag-embeddings.md` → `slides/extra-decks/A-rag-embeddings-v1.md`

- [ ] **Step 1: Move the file**

```bash
git mv slides/session-03/A-rag-embeddings.md slides/extra-decks/A-rag-embeddings-v1.md
```

- [ ] **Step 2: Verify the archive**

```bash
head -10 slides/extra-decks/A-rag-embeddings-v1.md
```

Expected: the original front matter with `marp: true` and `theme: sorbonne`.

- [ ] **Step 3: Commit**

```bash
git add slides/extra-decks/A-rag-embeddings-v1.md
git commit -m "archive: move A-rag-embeddings.md to extra-decks before restructuring"
```

---

### Task 2: Create A-embeddings.md

**Files:**
- Create: `slides/session-03/A-embeddings.md`
- Source: `slides/extra-decks/A-rag-embeddings-v1.md` (lines 84–234 = slides 04–12 content)

This is a pure extraction — copy slides 04–12 from the archived original, wrap in proper deck structure (front matter, title slide, section dividers), renumber 04→01 through 12→09.

- [ ] **Step 1: Create A-embeddings.md**

Extract from the archived file:
- Front matter: new (from spec)
- ABOUTME comments: new (from spec)
- Title slide: new — "Embeddings — Le GPS du sens" / "Session 3A — Comprendre les représentations vectorielles"
- Section "Intuition": divider + slides 04–05 → renumber to 01–02
- Section "La mécanique": divider + slides 06–09 → renumber to 03–06
- Section "Applications": divider + slides 10–12 → renumber to 07–09

Content of each slide stays identical. Only changes:
- Slide number prefix: `# 04 —` becomes `# 01 —`, etc.
- No other content modifications

- [ ] **Step 2: Verify slide count**

```bash
grep -c "^# [0-9]" slides/session-03/A-embeddings.md
```

Expected: `9` (content slides 01–09)

- [ ] **Step 3: Run overflow linter**

```bash
make check 2>&1 | grep -A2 "A-embeddings"
```

Expected: no overflow warnings for this file.

- [ ] **Step 4: Commit**

```bash
git add slides/session-03/A-embeddings.md
git commit -m "feat: create A-embeddings.md — extract slides 04-12 from original RAG deck"
```

---

### Task 3: Create B-rag.md

**Files:**
- Create: `slides/session-03/B-rag.md`
- Source: `slides/extra-decks/A-rag-embeddings-v1.md`

This is the most complex task. Build the file by assembling slides from the original in the new order specified by the spec, plus 3 new slides.

- [ ] **Step 1: Create B-rag.md with all content**

Assemble in this order (source slide → new number):

**Front matter** (from spec) + **ABOUTME** (from spec)

**Title slide**: "RAG — Retrieval Augmented Generation" / "Session 3B — Donner de la mémoire à votre LLM"

**Section: "Pourquoi le RAG ?"**
- ex-S01 → new 01 "Pourquoi le RAG est indispensable" (lines 32–47 of original)
- NEW → new 02 "RAG = un LLM branché sur un moteur de recherche" (from spec, use text-only fallback until infographic exists)
- ex-S03 → new 03 "Le LLM comme consultant" (lines 68–81)
- ex-S17 → new 04 "RAG en pratique : chatbot RH" (lines 326–343)

**Section: "Le Pipeline RAG en détail"**
- ex-S02 → new 05 "Le RAG Pipeline en 5 étapes" (lines 50–65)
- ex-S13 → new 06 "Chunking : découper intelligemment" (lines 244–258)
- NEW → new 07 "Recherche par mots-clés : TF-IDF & BM25" (from spec)
- NEW → new 08 "Recherche sémantique & Hybrid Search" (from spec)
- ex-S14 → new 09 "Vector Databases" (lines 261–273)
- ex-S15 → new 10 "Hybrid Search : le meilleur des deux mondes" (lines 276–300)
- ex-S16 → new 11 "BM25 n'est pas mort : la preuve DeepMind" (lines 303–323)
- ex-S18 → new 12 "Applications du RAG" (lines 346–360)

**Section: "RAG avancé"**
- ex-S19 → new 13 (lines 372–389)
- ex-S20 → new 14 (lines 392–414)
- ex-S21 → new 15 (lines 419–441)
- ex-S22 → new 16 (lines 445–457)

**Section: "Améliorer son RAG"**
- ex-S23 → new 17 (lines 468–485)
- ex-S24 → new 18 (lines 490–507)
- ex-S25 → new 19 (lines 510–529)
- ex-S26 → new 20 (lines 534–549)
- ex-S27 → new 21 (lines 553–566)

**Section: "Synthèse"**
- ex-S28 → new 22 (lines 569–595)
- ex-S29 → new 23 (lines 599–611)
- ex-S30 → new 24 "Key Takeaways" — **MODIFY**: remove embeddings-specific takeaway, add search methods takeaway
- ex-S31 → new 25 "Pour la suite" — **MODIFY**: remove embeddings notebook reference, keep RAG-specific content

Each copied slide: update the number prefix (`# 17 —` → `# 04 —`, etc.)

New slide 02 uses text-only fallback (no `img-right` class, no `![bg right]`) until PaperBanana infographic is generated.

- [ ] **Step 2: Verify slide count**

```bash
grep -c "^# [0-9]" slides/session-03/B-rag.md
```

Expected: `25` (content slides 01–25)

- [ ] **Step 3: Verify section dividers**

```bash
grep -c "_class: section" slides/session-03/B-rag.md
```

Expected: `5`

- [ ] **Step 4: Run overflow linter**

```bash
make check 2>&1 | grep -A2 "B-rag"
```

Expected: no overflow warnings (new slides are within budget: S02=6 lines, S07=11 lines, S08=13 lines).

- [ ] **Step 5: Commit**

```bash
git add slides/session-03/B-rag.md
git commit -m "feat: create B-rag.md — restructured RAG deck with 3 new search-method slides"
```

---

## Chunk 2: Rename Existing Decks + Fix Cross-References

### Task 4: Rename B-agents.md → C-agents.md and fix cross-references

**Files:**
- Rename: `slides/session-03/B-agents.md` → `slides/session-03/C-agents.md`
- Modify: 8 changes inside the file (subtitle, ABOUTME, 6 cross-references)

- [ ] **Step 1: Rename the file**

```bash
git mv slides/session-03/B-agents.md slides/session-03/C-agents.md
```

- [ ] **Step 2: Update title slide subtitle**

Change "Session 3B" → "Session 3C" in the title slide.

- [ ] **Step 3: Update ABOUTME comment**

Line ~9: Change "Session 3B" → "Session 3C" in the ABOUTME comment.

- [ ] **Step 4: Update 6 "Deck A" → "Deck B" cross-references**

All refer to RAG content that is now in Deck B:

1. Line ~101: `(RAG, vu en Deck A)` → `(RAG, vu en Deck B)`
2. Line ~105: `depuis le Deck A` → `depuis le Deck B`
3. Line ~543: `Connexion avec le Deck A` → `Connexion avec le Deck B`
4. Line ~545: `le RAG (Deck A)` → `le RAG (Deck B)`
5. Line ~594: `le pont avec le Deck A` → `le pont avec le Deck B` (this is in the slide TITLE `# 28 —`)
6. Line ~596: `pipeline RAG du Deck A` → `pipeline RAG du Deck B`

Note: line numbers are approximate — search for the exact strings.

- [ ] **Step 5: Verify no remaining "Deck A" references**

```bash
grep -n "Deck A" slides/session-03/C-agents.md
```

Expected: 0 matches (all updated to "Deck B").

- [ ] **Step 6: Commit**

```bash
git add slides/session-03/C-agents.md
git commit -m "refactor: rename B-agents → C-agents, update Deck A → Deck B cross-refs"
```

---

### Task 5: Rename C-methodologie-projet.md → D-methodologie-projet.md and fix cross-references

**Files:**
- Rename: `slides/session-03/C-methodologie-projet.md` → `slides/session-03/D-methodologie-projet.md`
- Modify: 3 changes inside the file (subtitle, ABOUTME, cross-reference)

- [ ] **Step 1: Rename the file**

```bash
git mv slides/session-03/C-methodologie-projet.md slides/session-03/D-methodologie-projet.md
```

- [ ] **Step 2: Update title slide subtitle**

Change "Session 3C" → "Session 3D".

- [ ] **Step 3: Update ABOUTME comment**

Line ~10: Change "Block C de la Session 3" → "Block D de la Session 3" in the ABOUTME comment.

- [ ] **Step 4: Fix stale cross-reference**

Line ~99: `cf. Deck A, Precision/Recall` → `cf. Session 2B, Precision/Recall`

- [ ] **Step 5: Commit**

```bash
git add slides/session-03/D-methodologie-projet.md
git commit -m "refactor: rename C-methodologie → D-methodologie, fix stale Precision/Recall cross-ref"
```

---

## Chunk 3: Generate Infographic

### Task 6: Generate PaperBanana infographic for B-rag slide 02

**Files:**
- Create: `slides/session-03/assets/infographics/rag-llm-search-engine.png`
- Modify: `slides/session-03/B-rag.md` (add img-right class + image tag after generation)

- [ ] **Step 1: Generate the infographic**

Write input text to a temp file, then run PaperBanana:

```bash
cat > /tmp/rag-infographic-input.txt << 'EOF'
RAG (Retrieval Augmented Generation) connects a Large Language Model to a search engine. There are two main flows: Indexation, where documents like FAQs, contracts, and product sheets are fed into the search engine to build an index; and Query, where a user asks a question, the search engine finds the most relevant documents, and the LLM generates a response using those documents as context. The search engine component can use different retrieval methods: TF-IDF for simple keyword matching, BM25 for improved keyword search, dense Embeddings for semantic search, or a hybrid combination of all three.
EOF

cd /home/ezalos/42/Markdowns2Teach
uvx paperbanana generate -i /tmp/rag-infographic-input.txt -c "RAG architecture: an LLM connected to a search engine. Two flows: (1) Indexation - documents are fed into the search engine, (2) Query - user asks a question, search engine finds relevant documents, LLM generates answer from those documents. Simple, clean diagram with two clear arrows showing the two flows." -n 5
```

- [ ] **Step 2: Copy best output to assets**

```bash
cp outputs/run_<id>/final_output.png slides/session-03/assets/infographics/rag-llm-search-engine.png
```

- [ ] **Step 3: Update B-rag.md slide 02 to use the infographic**

Change slide 02 from text-only fallback to img-right layout:
- Add `<!-- _class: img-right -->` before the slide title
- Add `![bg right:55% contain](assets/infographics/rag-llm-search-engine.png)` at the end

- [ ] **Step 4: Verify Marp renders the slide**

```bash
make html 2>&1 | grep -i error
```

Expected: no errors.

- [ ] **Step 5: Commit**

```bash
git add slides/session-03/assets/infographics/rag-llm-search-engine.png slides/session-03/B-rag.md
git commit -m "feat: add RAG overview infographic for B-rag slide 02"
```

---

## Chunk 4: Update Documentation

### Task 7: Update CLAUDE.md

**Files:**
- Modify: `CLAUDE.md`

- [ ] **Step 1: Update the Course Structure table**

Find the Session 3 row in the Course Structure table. Update:

```
| 3 | Construire avec l'IA | RAG & Embeddings | Agents IA · C: Méthodologie projet IA |
```

→

```
| 3 | Construire avec l'IA | Embeddings · B: RAG | Agents IA · D: Méthodologie projet IA |
```

- [ ] **Step 2: Update the Active session decks table**

Replace the Session 3 entries:

```
| `slides/session-03/A-rag-embeddings.md` | RAG & Embeddings | 30 |
```

→

```
| `slides/session-03/A-embeddings.md` | Embeddings : Le GPS du sens | 9 |
| `slides/session-03/B-rag.md` | RAG : Retrieval Augmented Generation | 25 |
```

And rename:
```
| `slides/session-03/B-agents.md` | Agents IA ... | 49 |
| `slides/session-03/C-methodologie-projet.md` | Méthodologie projet IA | 25 |
```

→

```
| `slides/session-03/C-agents.md` | Agents IA ... | 49 |
| `slides/session-03/D-methodologie-projet.md` | Méthodologie projet IA | 25 |
```

- [ ] **Step 3: Add to Archived / extra decks table**

Add this row:

```
| `slides/extra-decks/A-rag-embeddings-v1.md` | RAG & Embeddings v1 *(split → A-embeddings + B-rag)* | 31 |
```

- [ ] **Step 4: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: update CLAUDE.md for Session 03 restructuring (4 decks)"
```

---

### Task 8: Update course-architecture.md

**Files:**
- Modify: `docs/references/course-architecture.md`

- [ ] **Step 1: Rewrite Session 3 detail table**

Find the `### Séance 3` section (currently references stale filenames `A-rag-agents.md` and `B-methodologie-projet.md`). Replace entirely with:

```markdown
### Séance 3 — Construire avec l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **Info** | Informations pratiques — logistique S4 (42 Paris), intervenants S4/S5, rappels QCM et présentations | `slides/session-03/0-infos.md` (9 slides) |
| **A** | Embeddings — intuition (GPS du sens, 2D→768d), mécanique (PCA, cosine similarity, clusters, word arithmetic), applications (multimodal, choix de modèle) | `slides/session-03/A-embeddings.md` (13 slides) |
| **B** | RAG — pourquoi (hallucinations/cutoff), pipeline (chunking, TF-IDF, BM25, embeddings, hybrid search, vector DB), avancé (reranking, contextual retrieval, production patterns), amélioration (Jason Liu: maturity levels, quick wins, anti-patterns, 6 evals, flywheel) | `slides/session-03/B-rag.md` (31 slides) |
| **C** | Agents IA — spectre d'agence, cycle Think→Act→Observe, 6 patterns Anthropic, MCP deep dive, Skills, Claude Code, OpenClaw, mémoire, production (erreurs composées), Context Engineering, AutoResearch | `slides/session-03/C-agents.md` (49 slides) |
| **D** | Méthodologie projet IA — Prompt-based dev, 4 catégories GenAI, lifecycle, CRISP-DM, LLMOps, AI Canvas, MVP patterns, 6 pièges AI Engineering, choix de stack | `slides/session-03/D-methodologie-projet.md` (25 slides) |
```

- [ ] **Step 2: Update the État des supports table**

Find the decks actifs table. Replace Session 3 entries:

```markdown
| `session-03/A-embeddings.md` | 13 | ✅ Terminé — extrait de A-rag-embeddings |
| `session-03/B-rag.md` | 31 | ✅ Terminé — restructuré avec slides TF-IDF/BM25, intro simplifiée |
| `session-03/C-agents.md` | 49 | ✅ Terminé — enrichi MCP, Skills, OpenClaw, AutoResearch |
| `session-03/D-methodologie-projet.md` | 25 | ✅ Terminé — enrichi 6 pièges AI Engineering (Chip Huyen) |
```

- [ ] **Step 3: Commit**

```bash
git add docs/references/course-architecture.md
git commit -m "docs: rewrite course-architecture.md Session 3 for 4-deck structure"
```

---

### Task 9: Update outline.md

**Files:**
- Modify: `docs/outline.md`

- [ ] **Step 1: Rewrite Session 3 section**

Find `## Session 3 — Cadrer un projet IA` (line 67). Replace the entire section up to the `---` before Session 4 with:

```markdown
## Session 3 — Construire avec l'IA

**0 — Informations pratiques** (`session-03/0-infos.md`, 9 slides)
- Session 4 logistics: 42 Paris location, transport, ID required, campus visit
- Session 4 intervenants: Maxime Jégat (Hoox, AI UGC), Tanguy Auffret (HEC, startup advisor)
- Session 5 intervenante: Juliette Lefay (Phygital Studio, tech-art entrepreneurship)
- Session 5 reminders: QCM format (20 Qs, 5 propositions, 30 min), project presentations grading

**A — Embeddings : Le GPS du sens** (`session-03/A-embeddings.md`, 13 slides)
- Intuition: mots comme coordonnées, 2D → 768 dimensions
- Mécanique: PCA, Cosine Similarity, clusters sémantiques, Word Arithmetic
- Applications: Multi-Modal Embeddings, choix de modèle, discussion

**B — RAG : Retrieval Augmented Generation** (`session-03/B-rag.md`, 31 slides)
- Pourquoi le RAG: hallucinations, knowledge cutoff, RAG = LLM + moteur de recherche, chatbot RH
- Pipeline: 5 étapes, chunking, TF-IDF & BM25, recherche sémantique, hybrid search, vector DBs
- RAG avancé: reranking, contextual retrieval, patterns de production, RAG vs fine-tuning, long context
- Améliorer son RAG (Jason Liu): 5 niveaux de maturité, quick wins, anti-patterns, 6 evals, flywheel

**C — Agents IA** (`session-03/C-agents.md`, 49 slides)
- Progressive intro: Alfred narrative, agency spectrum (5 levels), agent cycle (Think→Act→Observe), augmented LLM
- Anthropic complexity ladder: 6 patterns (Prompt Chaining → Routing → Parallelization → Orchestrator-Workers → Evaluator-Optimizer → Agents)
- MCP deep dive: M×N problem, M+N solution, Host/Client/Server, 4 capabilities, ecosystem, security risks
- Tools, Skills & products: Tool Use, SKILL.md standard, Claude Code + Knowledge Work Stack, OpenClaw (315K stars, MoltMatch incident)
- Agent memory: Buffer, Summary, RAG-based, Semantic, Episodic, Tool-based persistence
- Production: compound errors, failure modes, when NOT to use agents, Discovery-first
- Context Engineering (Jason Liu): Write/Select/Compress/Isolate, 4 response levels, Peripheral Vision, Subagents, Compaction, 3 Form Factors, Composabilité
- Karpathy AutoResearch: autonomous ML experimentation loop, "programming the program.md"

**D — Méthodologie projet IA** (`session-03/D-methodologie-projet.md`, 25 slides)
- Prompt-based development, 4 catégories GenAI, lifecycle Scope/Build/Evaluate/Deploy
- CRISP-DM 6 phases, LLMOps 9 phases, AI Canvas, ML Canvas
- MVP patterns (Wizard of Oz, Concierge, Rule-Based, Prompt Eng, API Wrapper)
- 6 pièges AI Engineering (Chip Huyen), Gmail Story
- Choix de stack: Closed vs Open Source, progression Prompting→RAG→Fine-tuning, coûts API
```

- [ ] **Step 2: Commit**

```bash
git add docs/outline.md
git commit -m "docs: rewrite outline.md Session 3 for 4-deck structure"
```

---

### Task 10: Update workflow-citation-audit.md

**Files:**
- Modify: `docs/references/workflow-citation-audit.md` (line 40)

- [ ] **Step 1: Update stale filename reference**

Line 40: change `session-03/B-methodologie-projet.md` → `session-03/D-methodologie-projet.md`

- [ ] **Step 2: Commit**

```bash
git add docs/references/workflow-citation-audit.md
git commit -m "docs: fix stale filename in citation audit backlog"
```

---

## Chunk 5: Build Verification

### Task 11: Full build verification

**Files:** None (verification only)

- [ ] **Step 1: Run full HTML build**

```bash
make html
```

Expected: clean build, no errors. All 4 new deck files compile.

- [ ] **Step 2: Run overflow linter**

```bash
make check
```

Expected: no new overflow warnings for A-embeddings.md or B-rag.md.

- [ ] **Step 3: Verify all Session 3 files exist**

```bash
ls -la slides/session-03/*.md
```

Expected: `0-infos.md`, `A-embeddings.md`, `B-rag.md`, `C-agents.md`, `D-methodologie-projet.md`

- [ ] **Step 4: Verify archive exists**

```bash
ls slides/extra-decks/A-rag-embeddings-v1.md
```

Expected: file exists.

- [ ] **Step 5: Verify no "Deck A" references remain in Session 3 decks (except A-embeddings itself)**

```bash
grep -rn "Deck A" slides/session-03/B-rag.md slides/session-03/C-agents.md slides/session-03/D-methodologie-projet.md
```

Expected: 0 matches (A-embeddings.md may reference "Deck A" — that's fine, it IS Deck A).

- [ ] **Step 6: Spot-check slide numbering**

```bash
grep "^# [0-9]" slides/session-03/A-embeddings.md | head -3
grep "^# [0-9]" slides/session-03/B-rag.md | head -3
```

Expected A-embeddings: `# 01 —`, `# 02 —`, `# 03 —`
Expected B-rag: `# 01 —`, `# 02 —`, `# 03 —`
