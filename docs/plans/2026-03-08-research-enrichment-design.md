# Design: Research Enrichment — 20 URLs across 7 topics

<!-- ABOUTME: Design doc for enriching existing slide decks with content from 20 external URLs. -->
<!-- ABOUTME: Covers research strategy, chart capture, content mapping, and slide integration plan. -->

## Goal

Research 20 URLs across 7 topics, extract the top 20% most important/interesting facts and charts, and create/replace slides in existing decks. All new content must be properly cited per `slide-creation-standards.md` §6.

## Approach: Two-wave parallel

### Wave 1 — Research + Capture (parallel)

Launch ~7 research subagents (one per topic cluster). Each agent:
1. Reads all URLs for its topic (via web fetch/extract)
2. Extracts key facts, numbers, quotes
3. Identifies the most impactful charts/graphs
4. Produces a structured summary

In parallel, capture all charts from pages with interactive JS graphics (primarily Epoch AI) using `scripts/capture-charts.js`.

### Wave 2 — Slide writing (per-deck)

For each target deck:
1. Review existing slides to identify weak/replaceable content
2. Map Wave 1 findings to specific slide positions (replace or insert)
3. Write slides following all conventions
4. Run `make check` after each deck

### Final — Documentation update

Update `docs/references/course-architecture.md` with new slide counts and content descriptions.

## Content Mapping

| Topic | URLs | Target Deck | Expected Slides |
|-------|------|-------------|-----------------|
| **LLM** | 3 | S2-A `A-llms.md` (40 slides) | 3-6 new/replaced |
| **Ecosystem** | 4 | S4-A `A-ecosysteme-ia.md` (18 slides) | 4-8 new |
| **Ethics** | 4 | S5-A `A-regulation-ethique.md` (23 slides) | 3-5 new |
| **Agents** | 1 | S3-A `A-rag-agents.md` (27 slides) | 2-3 new |
| **RAG** | 3 | S3-A `A-rag-agents.md` (27 slides) | 2-4 new |
| **Eval** | 2 | S2-B `B-evaluer-ia.md` (18 slides) | 2-3 new + charts |
| **Engineering** | 1 | S3-B `B-methodologie-projet.md` (27 slides) | 2-3 new |

**Total**: ~18-32 new/replaced slides, ~15-25 captured charts.

## URL Inventory

### LLM (→ S2-A)
1. https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models
2. https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data
   - Balanced by: https://vintagedata.org/blog/posts/synthetic-pretraining
3. https://epoch.ai/blog/open-models-report

### Eval (→ S2-B)
4. https://lmcouncil.ai/benchmarks
5. https://epoch.ai/benchmarks/eci

### RAG (→ S3-A)
6. https://arxiv.org/html/2508.21038v1
7. https://jxnl.co/writing/category/rag/#why-cognition-does-not-use-multi-agent-systems
8. https://jxnl.co/writing/2025/08/28/context-engineering-index/

### Engineering (→ S3-B)
9. https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html

### Ethics (→ S5-A)
10. https://www.darioamodei.com/essay/the-adolescence-of-technology
11. https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/unless-its-governance-changes-anthropic-is-untrustworthy
12. https://www.anthropic.com/news/claudes-constitution
13. https://www.anthropic.com/constitution

### Agents (→ S3-A)
14. https://arxiv.org/pdf/2601.10825

### Ecosystem (→ S4-A)
15. https://epoch.ai/blog/inference-economics-of-language-models
16. https://epoch.ai/blog/can-ai-scaling-continue-through-2030
17. https://epoch.ai/blog/what-will-ai-look-like-in-2030
18. https://epoch.ai/blog/what-do-economic-value-benchmarks-tell-us

## Deck modification strategy

- **Replace**: when existing slides have weaker sourcing or less current data
- **Add**: when the topic adds a new angle not currently covered
- **Target**: 25-30 slides per 45-min deck (some can exceed if content is strong)

## Quality gates

- All slides follow `slide-creation-standards.md` conventions
- Every data claim has `[N]` in-text + `<small>Sources</small>` footer
- `make check` passes (0 overflow) on every modified deck
- `make html` builds cleanly
- `course-architecture.md` updated with final counts
