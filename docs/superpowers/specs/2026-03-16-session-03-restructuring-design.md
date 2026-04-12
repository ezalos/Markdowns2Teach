# Session 03 Restructuring: Split Embeddings from RAG

**Date:** 2026-03-16
**Status:** Draft
**Scope:** Restructure Session 03 from 3 decks (A-rag-embeddings, B-agents, C-methodologie) to 4 decks (A-embeddings, B-rag, C-agents, D-methodologie)

## Motivation

Louis's feedback after reviewing the current RAG & Embeddings deck:

1. Embeddings deserve their own deck — they're a foundational concept, not just a sub-section of RAG
2. The RAG deck intro is too technical too fast — needs a simple "RAG = LLM + search engine" framing before the 5-step pipeline
3. The concrete example (chatbot RH) comes too late (slide 17) — should come right after the intro
4. Search methods (TF-IDF, BM25) are missing — students see "Vector Database" and "Hybrid Search" without understanding what they're being compared to
5. Block timing is Louis's concern, not ours — just create 4 clean decks

## File Changes Summary

| Action | From | To |
|--------|------|----|
| **Create** | — | `slides/session-03/A-embeddings.md` |
| **Create** | — | `slides/session-03/B-rag.md` |
| **Rename** | `slides/session-03/B-agents.md` | `slides/session-03/C-agents.md` |
| **Rename** | `slides/session-03/C-methodologie-projet.md` | `slides/session-03/D-methodologie-projet.md` |
| **Archive** | `slides/session-03/A-rag-embeddings.md` | `slides/extra-decks/A-rag-embeddings-v1.md` |

## Design: A-embeddings.md

Extracted from current A-rag-embeddings.md slides 04–12. No content changes — pure extraction with proper deck wrapping.

### Structure

```
Title: "Embeddings — Le GPS du sens"
  Subtitle: "Session 3A — Comprendre les représentations vectorielles"

Section: "Intuition"
  01 — Intuition : les mots comme coordonnées (ex-S04)
  02 — Des vecteurs 2D aux vrais Embeddings (ex-S05)

Section: "La mécanique"
  03 — PCA : voir l'invisible (ex-S06)
  04 — Cosine Similarity : mesurer la pertinence (ex-S07)
  05 — Les clusters sémantiques (ex-S08)
  06 — Word Arithmetic : Roi − Homme + Femme ≈ Reine (ex-S09)

Section: "Applications"
  07 — Multi-Modal Embeddings (ex-S10)
  08 — Choisir son modèle d'Embedding (ex-S11)
  09 — Discussion : Embeddings et votre projet (ex-S12)
```

~13 slides total (9 content + title + 3 section dividers).

### Front matter

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
```

### ABOUTME

```markdown
<!-- ABOUTME: Embeddings — intuition, mécanique (PCA, cosine similarity, clusters, word arithmetic) et applications (multimodal, choix de modèle). -->
<!-- ABOUTME: Session 3A pour étudiants M2 IMT&E Paris 1 : comprendre les représentations vectorielles qui fondent la recherche sémantique. -->
```

## Design: B-rag.md

Restructured from current A-rag-embeddings.md. Removes embeddings section (now in A), reorders intro, adds 3 new slides.

### Structure

```
Title: "RAG — Retrieval Augmented Generation"
  Subtitle: "Session 3B — Donner de la mémoire à votre LLM"

Section: "Pourquoi le RAG ?"
  01 — Pourquoi le RAG est indispensable (ex-S01, keep)
  02 — RAG = un LLM branché sur un moteur de recherche [NEW]
  03 — Le LLM comme consultant (ex-S03, keep)
  04 — RAG en pratique : chatbot RH (ex-S17, moved up)

Section: "Le Pipeline RAG en détail"
  05 — Le RAG Pipeline en 5 étapes (ex-S02, moved here)
  06 — Chunking : découper intelligemment (ex-S13, keep)
  07 — Recherche par mots-clés : TF-IDF & BM25 [NEW]
  08 — Recherche sémantique & Hybrid Search [NEW]
  09 — Vector Databases (ex-S14, keep)
  10 — Hybrid Search : le meilleur des deux mondes (ex-S15, keep — deeper detail)
  11 — BM25 n'est pas mort : la preuve DeepMind (ex-S16, keep)
  12 — Applications du RAG (ex-S18, keep)

Section: "RAG avancé"
  13 — Reranking et Contextual Retrieval (ex-S19, keep)
  14 — Les patterns de production (ex-S20, keep)
  15 — RAG vs Fine-tuning (ex-S21, keep)
  16 — Long Context vs RAG (ex-S22, keep)

Section: "Améliorer son RAG" (Jason Liu)
  17 — RAG Maturity : 5 niveaux (ex-S23, keep)
  18 — Quick Wins : 7 améliorations (ex-S24, keep)
  19 — Les anti-patterns du RAG (ex-S25, keep)
  20 — Les 6 évaluations du RAG (ex-S26, keep)
  21 — Le RAG Flywheel (ex-S27, keep)

Section: "Synthèse"
  22 — Du Q&A au rapport structuré (ex-S28, keep)
  23 — Quand le RAG n'est pas la réponse (ex-S29, keep)
  24 — Key Takeaways (ex-S30, updated)
  25 — Pour la suite (ex-S31, updated)
```

~31 slides total (25 content + title + 5 section dividers).

### Front matter

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
```

### ABOUTME

```markdown
<!-- ABOUTME: RAG — pipeline complet (chunking, recherche TF-IDF/BM25/embeddings, vector DB, hybrid search, reranking) et amélioration continue (Jason Liu). -->
<!-- ABOUTME: Session 3B pour étudiants M2 IMT&E Paris 1 : construire et améliorer un système RAG en production. -->
```

### New slide 02: RAG = un LLM branché sur un moteur de recherche

```markdown
<!-- _class: img-right -->

# 02 — RAG = un LLM branché sur un moteur de recherche

Le RAG est une idée simple : **connecter un LLM à un moteur de recherche**.

**Deux flux** :

- **Indexation** — vous alimentez le moteur de recherche avec vos documents (FAQ, contrats, fiches produit)
- **Question** — l'utilisateur pose une question → le moteur trouve les documents pertinents → le LLM génère une réponse à partir de ces documents

> Le moteur de recherche peut être un simple **TF-IDF**, un **BM25**, des **Embeddings**, ou les trois combinés. Le choix du moteur est une décision technique — le principe reste le même.

![bg right:55% contain](assets/infographics/rag-llm-search-engine.png)
```

**Prerequisite**: infographic `rag-llm-search-engine.png` must be generated via PaperBanana before building this slide. Fallback: if the infographic is not ready, use the slide without `img-right` class and without the `![bg right]` image tag — the text stands on its own.

### New slide 07: Recherche par mots-clés : TF-IDF & BM25

```markdown
# 07 — Recherche par mots-clés : TF-IDF & BM25

Avant les Embeddings, la recherche fonctionnait par **comptage de mots** :

**TF-IDF** — Term Frequency × Inverse Document Frequency :
- Un mot fréquent dans *ce* document mais rare dans *les autres* = important
- "Assurance" dans un document juridique → peu informatif (partout)
- "Décennale" dans ce même document → très informatif (rare ailleurs)

**BM25** — l'évolution de TF-IDF :
- Gère mieux les documents longs (saturation) et les mots répétés
- Standard de la recherche textuelle depuis 30 ans — utilisé par Elasticsearch, Solr, Lucene [1]

> Rapide (~5 ms), aucun modèle à entraîner, excellent pour les **termes exacts**. Faiblesse : ne comprend pas que "voiture" et "automobile" sont le même concept.

<small>Sources : [1] [Robertson & Zaragoza — The Probabilistic Relevance Framework: BM25 and Beyond](https://dl.acm.org/doi/10.1561/1500000019)</small>
```

Note: BM25 description deliberately simplified for non-engineer audience. Technically, BM25 is a probabilistic ranking function with term-frequency saturation and document-length normalization. The simplification focuses on what matters for the students: it's better than TF-IDF at handling real documents.

### New slide 08: Recherche sémantique & Hybrid Search

```markdown
# 08 — Recherche sémantique & Hybrid Search

**Embeddings** (cf. Deck A) résolvent la faiblesse des mots-clés :
- Comparent le **sens**, pas les mots exacts
- "Voiture" et "automobile" → vecteurs proches
- Excellents pour les questions en langage naturel

**Mais les Embeddings ont aussi des limites** :
- Peuvent manquer un terme technique exact ("article L.121-3")
- Plus lents et plus coûteux que BM25

**Hybrid Search = les deux combinés** :
- BM25 pour les mots exacts + Embeddings pour le sens
- **+15–30% de rappel** vs chaque méthode seule [1]

> Il n'y a pas de débat : en production, c'est **toujours** Hybrid Search.

<small>Sources : [1] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)</small>
```

### Updates to existing slides

**Slide 24 (Key Takeaways)** — Remove embeddings-specific takeaway (now in Deck A). Adjust numbering. Add takeaway about search methods progression.

**Slide 25 (Pour la suite)** — Remove "notebook Jupyter sur les Embeddings" reference (now in Deck A's scope). Keep RAG-specific next steps.

## Design: C-agents.md (rename)

Rename `B-agents.md` → `C-agents.md`. Content changes:

- **Slide 04** (Le LLM Augmenté, line 101): Update "RAG, vu en Deck A" → "RAG, vu en Deck B"
- **Slide 04** (Le LLM Augmenté, line 105): Update "depuis le Deck A" → "depuis le Deck B"
- **Slide 25** (Pourquoi la mémoire change tout, line 543): Update "Connexion avec le Deck A" → "Connexion avec le Deck B"
- **Slide 25** (line 545): Update "le RAG (Deck A)" → "le RAG (Deck B)"
- **Slide 28** (RAG-based Memory, line 596): Update "pipeline RAG du Deck A" → "pipeline RAG du Deck B"
- **Title slide subtitle**: "Session 3B" → "Session 3C"

## Design: D-methodologie-projet.md (rename)

Rename `C-methodologie-projet.md` → `D-methodologie-projet.md`. Content changes:

- **Title slide subtitle**: "Session 3C" → "Session 3D"
- **Slide 04** (line 99): Fix stale cross-reference "cf. Deck A, Precision/Recall" → "cf. Session 2B, Precision/Recall"

## Infographics Needed

| Slide | Filename | Description |
|-------|----------|-------------|
| B-rag S02 | `rag-llm-search-engine.png` | Simple diagram: LLM + search engine, two arrows (index docs / query) |

Existing infographics (rag-pipeline-5-steps.png, etc.) stay in `assets/infographics/` and are referenced from the new B-rag.md.

## Unchanged Files

- `slides/session-03/0-infos.md` — remains unchanged (no cross-references to other decks)

## Documentation Updates

After implementation, update:

- **`CLAUDE.md`** — Update the "Active session decks" table (new file names, slide counts) AND the "Archived / extra decks" table (add `A-rag-embeddings-v1.md`). Also update the Course Structure table row for Session 3.
- **`docs/references/course-architecture.md`** — Full rewrite of the Session 3 detail table (current content references stale filenames `A-rag-agents.md` and `B-methodologie-projet.md` from a previous restructuring). Update the "État des supports" tables.
- **`docs/outline.md`** — Rewrite Session 3 section with the 4 new deck paths and accurate slide counts (current content is stale).
- **`docs/references/workflow-citation-audit.md`** — Update reference to `session-03/B-methodologie-projet.md` (line 40) → `session-03/D-methodologie-projet.md`.

## Notes on Slide Overlap

New slide 08 (Recherche sémantique & Hybrid Search) and existing slide 10 (Hybrid Search: le meilleur des deux mondes) both cover hybrid search. The differentiation:
- **Slide 08** = introductory overview — positions hybrid search in the TF-IDF → BM25 → Embeddings progression
- **Slide 10** = deeper detail — the cols layout with BM25 vs Semantic comparison, specific latency numbers, specific weaknesses

If during implementation this still feels redundant, consider reworking slide 10 to focus on implementation details (alpha parameter tuning, RRF vs weighted scoring, tool recommendations) rather than repeating the BM25-vs-Semantic comparison.
