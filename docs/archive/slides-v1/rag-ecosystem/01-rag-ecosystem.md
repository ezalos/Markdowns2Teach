---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Écosystème RAG 2024–2026 · Sources publiques"
---

<!-- ABOUTME: Écosystème RAG — taxonomie, outils, patterns avancés, évaluation, sécurité et décisions Build vs Buy. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : choisir son stack RAG, estimer les coûts, anticiper les risques. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# L'Écosystème RAG

## Choisir, construire et déployer votre pipeline

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Le marché RAG en chiffres

- Le marché RAG atteint **$1,85 Mds** en 2025 → **$67 Mds** en 2034 (CAGR ~49%) [1]
- **86%** des organisations augmentent leurs LLMs avec du RAG [2]
- **60%** des applications LLM en production utilisent du RAG [2]
- RAG réduit les hallucinations de **70-90%** vs un LLM seul [1]
- RAG est **1 250x moins cher** que le long contexte ($0,00008 vs $0,10 par requête) [3]
- Budget production typique : **$5-25K/mois** selon la complexité

> Le RAG n'est plus une option — c'est le standard de facto pour les apps LLM en entreprise.

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [K2View](https://www.k2view.com/) · [3] [Meilisearch](https://www.meilisearch.com/)</small>

---

# 02 — La taxonomie RAG : Naive → Advanced → Modular

| Niveau | Pipeline | Coût/mois | Cas d'usage |
|--------|----------|-----------|-------------|
| **Naive** | Retrieve + Generate | $500-2K | FAQ interne, chatbot simple |
| **Advanced** | Hybrid Search + Reranking | $2-8K | Support client, knowledge base |
| **Modular** | Routing + Agentic + Graphs | $5-20K+ | Juridique, compliance, multi-source |

- **80% des use cases** sont couverts par l'Advanced RAG [1]
- RAG vs Fine-tuning : RAG pour des données dynamiques, Fine-tuning pour le style/domaine [2]
- Les deux se combinent : **+11% d'accuracy** ensemble vs séparément [2]

> Rappel session précédente : le RAG en 3 étapes (retrieve → augment → generate).
> Aujourd'hui on passe aux outils concrets et aux choix d'architecture.

<small>Sources : [1] [MarketsandMarkets](https://www.marketsandmarkets.com/) · [2] [arXiv 2401.08406](https://arxiv.org/abs/2401.08406)</small>

---

<!-- _class: section -->

# Le stack RAG

## Chaque couche, une décision Build vs Buy

---

# 03 — Vue d'ensemble du stack RAG

| Couche | Rôle | Players clés | Signal |
|--------|------|-------------|--------|
| **Document Processing** | Ingérer PDF, HTML, images | Unstructured, Docling, LlamaParse | Build (OSS mature) |
| **Embedding** | Vectoriser le texte | OpenAI, Cohere Embed, Jina | Buy (API, $0,02-0,13/M tokens) |
| **Vector Database** | Stocker & chercher les vecteurs | Pinecone, Qdrant, pgvector | Choix critique (lock-in) |
| **Orchestration** | Chaîner les étapes du pipeline | LangChain, LlamaIndex, Haystack | Build (différenciation) |
| **Managed RAG** | Pipeline clé-en-main | AWS Bedrock KB, Azure AI Search | Buy (vitesse de déploiement) |

- Règle d'or : **Buy l'infra, Build l'orchestration**
- L'orchestration est votre avantage compétitif — l'infra est commoditisée

---

# 04 — Document Processing : le premier kilomètre

| Outil | Différenciateur | Licence | Prix |
|-------|----------------|---------|------|
| **Unstructured.io** | 30+ formats, 71 connecteurs | Apache 2.0 + SaaS | $2,66/h compute |
| **Docling** (IBM Zurich) | 97,9% accuracy tables, 52K ★ | MIT | Gratuit |
| **LlamaParse** | GenAI-native, mode agentic | Propriétaire | $0,003-0,09/page |
| **MinerU** | #1 PDF open-source, 54K ★ | AGPL-3.0 | Gratuit |
| **Crawl4AI / Firecrawl** | Web scraping pour RAG, 80K ★ | Apache / AGPL | Free → $83/mois |

- "**Data quality > model quality**" — 60-70% de votre temps ici [1]
- Docling et MinerU : deux projets européens open-source de classe mondiale

<small>Sources : [1] [Unstructured.io](https://unstructured.io/) · [GitHub](https://github.com/DS4SD/docling) · [GitHub](https://github.com/opendatalab/MinerU)</small>

---

# 05 — Embedding Models : le cœur du RAG

| Modèle | Éditeur | MTEB | Dimensions | Prix/M tokens |
|--------|---------|------|------------|---------------|
| **text-embedding-3-large** | OpenAI | 64,6 | 3 072 | $0,13 |
| **Embed v4** | Cohere | 65,2 | 1 024 | $0,12 |
| **jina-embeddings-v3** | Jina AI (Berlin) | 65,5 | 1 024 | $0,02 |
| **Voyage AI** | Voyage | ~65 | 1 024 | $0,12 |
| **BGE-M3** | BAAI | ~63 | 1 024 | Gratuit (OSS) |
| **Qwen3-Embedding** | Alibaba | ~64 | Variable | Gratuit (OSS) |

- La qualité du **chunking** impacte plus que le choix de l'embedding [1]
- Jina v3 : **#1 multilingual** pour les modèles <1B paramètres [2]

<small>Sources : [1] [Anthropic](https://www.anthropic.com/news/contextual-retrieval) · [2] [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)</small>

---

# 06 — Vector Databases : le guide de choix

| Base | Type | Différenciateur | Stars | Origine |
|------|------|----------------|-------|---------|
| **Pinecone** | Managed | Leader serverless, free tier 100K | — | 🇺🇸 USA |
| **Qdrant** | OSS + Cloud | Rust, performant, EU-hosted | 22K | 🇩🇪 Berlin |
| **Weaviate** | OSS + Cloud | Hybrid search natif | 14K | 🇳🇱 Amsterdam |
| **Milvus** | OSS + Cloud | Échelle massive (milliards) | 42K | 🇺🇸 USA |
| **pgvector** | Extension PG | Gratuit, 0 vendor lock-in | 13K | OSS |
| **Chroma** | OSS | Prototypage rapide | 16K | 🇺🇸 USA |
| **Elasticsearch** | OSS + Cloud | Incumbent, hybrid BM25+dense | 73K | 🇳🇱 Amsterdam |

<small>Sources : [GitHub](https://github.com/) · [Pinecone](https://www.pinecone.io/) · [Qdrant](https://qdrant.tech/)</small>

---

<!-- _class: cols -->

# 07 — Spotlight : Pinecone vs pgvector

<div class="left">

**Pinecone** — Managed leader, serverless, free tier 100K vecteurs, $750M valorisation [1]

</div>

<div class="right">

**pgvector** — Extension PostgreSQL gratuite, zéro vendor lock-in, suffisant <5M vecteurs

</div>

> Managed pour la vitesse. Open-source pour le contrôle et les coûts à l'échelle.

<small>Sources : [1] [Pinecone](https://www.pinecone.io/) · [pgvector](https://github.com/pgvector/pgvector)</small>

---

# 08 — RAG Frameworks : l'orchestration

| Framework | Stars | Focus | Origine |
|-----------|-------|-------|---------|
| **LangChain** | 120K | Écosystème complet, LangGraph agents | 🇺🇸 USA |
| **LlamaIndex** | 46K | Data-focused, LlamaParse intégré | 🇺🇸 USA |
| **Haystack** (deepset) | 20K | Production-grade, modulaire | 🇩🇪 Berlin |
| **DSPy** | 22K | Prompt optimization automatique | 🇺🇸 Stanford |
| **Dify** | 129K | No-code RAG builder | 🇨🇳 Chine |
| **RAGFlow** | 73K | Open-source, RAPTOR intégré | 🇨🇳 Chine |

- **35% du Fortune 500** utilise les services LangChain [1]
- Haystack : l'option européenne production-ready

<small>Sources : [1] [LangChain](https://www.langchain.com/) · [GitHub](https://github.com/)</small>

---

# 09 — RAG-as-a-Service : les offres cloud

| Service | Éditeur | Point fort | Prix indicatif |
|---------|---------|-----------|---------------|
| **Bedrock KB** | AWS | 8 vector stores, 100K+ clients | Pay-per-use |
| **Azure AI Search** | Microsoft | 40+ régions, 85% Fortune 500 | $75-1 960/mois |
| **Vertex AI RAG** | Google | Gemini 2M tokens, Spanner | $0,90/node/h |
| **File/Web Search** | OpenAI | Intégré aux Assistants API | $2,50/1K queries |
| **Sonar API** | Perplexity | Web search RAG, 780M queries/mois | $1-15/M tokens |
| **Vectara** | Vectara | 100+ langues, HHEM hallucination | $100-500K/an |
| **Command R+** | Cohere | GDPR-native, 85% déploiements privés | $2,50/M tokens |

<small>Sources : [AWS](https://aws.amazon.com/bedrock/) · [Azure](https://azure.microsoft.com/) · [Cohere](https://cohere.com/pricing)</small>

---

<!-- _class: cols -->

# 10 — Spotlight : Cohere RAG — le champion GDPR

<div class="left">

### Stack intégré

- Embed v4 (#1 MTEB) + Rerank + Generate
- **Citations intégrées** nativement
- 23 langues, **+23% qualité** avec Rerank [1]

</div>

<div class="right">

### Souveraineté des données

- **85%** du revenu = déploiements privés
- VPC / on-prem natif, GDPR, SOC 2
- Clients : Oracle, McKinsey, RBC [2]

</div>

> La souveraineté des données est un avantage concurrentiel en Europe.

<small>Sources : [1] [Cohere](https://cohere.com/) · [2] [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: section -->

# Les patterns avancés

## Quand le Naive RAG ne suffit plus

---

# 11 — Hybrid Search & Reranking

- **Hybrid Search** = Dense (embeddings) + Sparse (BM25) → standard en production [1]
- Le **Reranking** ajoute **+20-30%** de qualité sur les résultats [2]

| Reranker | Éditeur | Point fort |
|----------|---------|-----------|
| **Cohere Rerank 3.5** | Cohere | +23% NDCG, 100+ langues |
| **Jina Reranker** | Jina AI (Berlin) | Léger, $0,02/M tokens |
| **ColBERT** | Stanford | Late interaction, open-source |
| **Cross-encoder** | Sentence Transformers | Précis mais lent |

- Pipeline production recommandé : Hybrid Search → Reranking → LLM [1]
- Anthropic Contextual Retrieval : **-67% d'échecs** avec reranking [3]

<small>Sources : [1] [Weaviate](https://weaviate.io/) · [2] [Cohere](https://cohere.com/) · [3] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 12 — Chunking & Query Transformation

| Stratégie | Principe | Quand l'utiliser |
|-----------|----------|-----------------|
| **Fixed-size** | Découpage à N tokens | Prototypage rapide |
| **Recursive** | Split par structure (§, phrases) | Texte structuré |
| **Semantic** | Regroupement par similarité | Documents longs, hétérogènes |
| **RAPTOR** | Résumés hiérarchiques récursifs | Questions multi-niveaux (+20% accuracy) [1] |
| **Late Chunking** | Embedding complet → découpage après | Coréférences, Jina AI (Berlin) [2] |
| **Contextual** | LLM ajoute du contexte par chunk | Haute qualité (-49% d'échecs) [3] |

- **Le chunking est le facteur #1 de qualité RAG** — plus impactant que le modèle
- Query Transformation : HyDE, multi-query, routing adaptatif

<small>Sources : [1] [ICLR 2024](https://iclr.cc/) · [2] [Jina AI](https://jina.ai/news/late-chunking/) · [3] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

<!-- _class: cols -->

# 13 — Spotlight : ColPali — le RAG visuel made in Paris

<div class="left">

**ILLUIN Technology**, Paris — Vision Language Model encode la page comme image, **aucun OCR** [1]

</div>

<div class="right">

ViDoRe NDCG@5 = **81,3**, 2M+ downloads, NVIDIA adopte le paradigme, 85+ clients [2]

</div>

> La France produit de la recherche RAG de pointe. €25M levés.

<small>Sources : [1] [arXiv 2407.01449](https://arxiv.org/abs/2407.01449) · [2] [NVIDIA](https://developer.nvidia.com/blog/)</small>

---

# 14 — GraphRAG, Self-RAG & Agentic RAG

| Pattern | Principe | Gain | Latence |
|---------|----------|------|---------|
| **GraphRAG** (Microsoft) | Knowledge Graphs + communautés | Requêtes thématiques globales | 2-5s |
| **Self-RAG** (ICLR 2024) | LLM auto-évalue la pertinence | **+55,8%** accuracy (PopQA) [1] | 1-3s |
| **CRAG** | Correctif : discard + web search | **+36,6%** (PubHealth) [2] | 2-4s |
| **Agentic RAG** | LLM décide quand/où retriever | Flexible, multi-source | 3-10s |
| **LightRAG** (HKU) | GraphRAG léger, **6 000x** moins de tokens [3] | 67% win rate vs Naive | <1s |

- **80% des cas n'ont pas besoin d'Agentic RAG** aujourd'hui
- CAG (Cache-Augmented) : **40x plus rapide** que RAG si <200K tokens [4]

<small>Sources : [1] [ICLR 2024](https://openreview.net/) · [2] [arXiv CRAG](https://arxiv.org/) · [3] [GitHub LightRAG](https://github.com/HKUDS/LightRAG) · [4] [arXiv 2412.15605](https://arxiv.org/abs/2412.15605)</small>

---

# 15 — Multimodal RAG : au-delà du texte

| Approche | Principe | Outil phare |
|----------|----------|-------------|
| **Extract-then-embed** | OCR + extraction → embedding texte | Docling (IBM Zurich), MinerU |
| **Vision Embeddings** | Encoder l'image de la page directement | ColPali (Paris), CLIP |
| **VLM Captioning** | LLM multimodal décrit les visuels | GPT-4o, Gemini 2.0 |

- **25-40%** d'amélioration sur les documents visuellement riches [1]
- Use cases : factures, rapports avec graphiques, catalogues produits, manuels techniques
- **40-60%** de l'information dans les docs business est non-textuelle [2]

> Si vos documents contiennent des tableaux, graphiques ou images, le RAG texte-only ne suffit pas.

<small>Sources : [1] [arXiv 2502.08826](https://arxiv.org/abs/2502.08826) · [2] [Morphik](https://www.morphik.ai/)</small>

---

# 16 — Choisir le bon pattern

| Scénario | Pattern recommandé | Coût/mois |
|----------|-------------------|-----------|
| FAQ interne, 1 source | **Naive RAG** | $500-2K |
| Support client multi-sources | **Advanced** (Hybrid + Rerank) | $2-8K |
| Juridique, contrats multi-docs | **GraphRAG** | $5-15K |
| Catalogue images / factures | **Multimodal RAG** | $3-10K |
| Compliance temps réel, multi-outils | **Agentic RAG** | $10-20K+ |

- Commencez **toujours** par Naive → mesurez → upgradez si nécessaire
- La complexité a un coût : chaque couche ajoute latence et maintenance

> **Question pour la classe** : Votre startup traite 10K factures/mois avec des tableaux.
> Quel pattern choisissez-vous ? Pourquoi ?

---

<!-- _class: section -->

# Évaluer et sécuriser

## Le maillon faible du RAG

---

# 17 — RAGAS & DeepEval : mesurer la qualité

**4 métriques clés** (RAGAS, standard open-source, 12K ★) [1] :

| Métrique | Mesure | Sans ground truth |
|----------|--------|:-----------------:|
| **Faithfulness** | Réponse fidèle au contexte récupéré | ✅ |
| **Answer Relevancy** | Réponse pertinente à la question | ✅ |
| **Context Precision** | Contexte récupéré pertinent | ✅ |
| **Context Recall** | Contexte récupéré complet | ❌ |

- **DeepEval** (YC W24) : **50+ métriques**, CI/CD natif, 12,8K ★ [2]
- Observabilité : **LangSmith** (leader, $39/seat/mois) vs **Arize Phoenix** (OSS, gratuit) [3]

> Règle d'or : intégrez l'évaluation **au jour 1**, pas après le déploiement.

<small>Sources : [1] [RAGAS](https://github.com/explodinggradients/ragas) · [2] [DeepEval](https://github.com/confident-ai/deepeval) · [3] [LangSmith](https://www.langchain.com/langsmith)</small>

---

# 18 — Sécurité RAG : les risques à connaître

| Risque | Menace | Impact |
|--------|--------|--------|
| **Knowledge Base Poisoning** | 5 documents empoisonnés → **97% de succès** [1] | Réponses manipulées |
| **Indirect Prompt Injection** | Injection via documents récupérés → **80% de succès** [2] | Exfiltration de données |
| **Permission Bypass** | Fuite d'embeddings sans contrôle d'accès | Données confidentielles exposées |

- **90%** des organisations déploient des LLMs, seulement **5%** sont confiantes en leur sécurité [3]
- L'EU AI Act pousse la demande de déploiement on-prem / souverain

**Mitigations** : GRADA (graph reranking, -80% attaques), NeMo Guardrails (NVIDIA), Lakera Guard (99,7% détection)

<small>Sources : [1] [USENIX Security 2025](https://arxiv.org/abs/2402.07867) · [2] [IEEE S&P 2026](https://www.ieee.org/) · [3] [OWASP LLM Top 10](https://genai.owasp.org/)</small>

---

# 19 — Construire votre stack RAG

**Scénario** : Legaltech, 5 personnes, budget 200K€, 10K documents juridiques.

| Option | Stack | Coût/mois | Délai MVP |
|--------|-------|-----------|-----------|
| **A — Full OSS** | pgvector + Mistral + LlamaIndex | ~3K€ | 3-4 mois |
| **B — Hybride** | Pinecone + Claude + LlamaIndex | ~8K€ | 1-2 mois |
| **C — Managed** | AWS Bedrock KB | ~5K€ | 2-4 semaines |

- Option A : contrôle total, mais maintenance lourde et expertise requise
- Option B : bon équilibre coût/vitesse, vendor lock-in modéré
- Option C : le plus rapide, mais flexibilité limitée et coûts croissants à l'échelle

> **Question pour la classe** : Quelle option choisissez-vous ? Quel facteur pèse le plus :
> vitesse de mise en marché, coût à 3 ans, ou souveraineté des données ?

---

<!-- _class: section -->

# Synthèse

## Ce qu'il faut retenir

---

# 20 — L'écosystème européen du RAG

L'Europe dispose d'un écosystème RAG **complet et compétitif** :

| Entreprise | Ville | Contribution |
|-----------|-------|-------------|
| **ColPali / ILLUIN** | Paris 🇫🇷 | Vision RAG, benchmark ViDoRe |
| **Docling / IBM Research** | Zurich 🇨🇭 | Document Processing, 52K ★ |
| **Jina AI** | Berlin 🇩🇪 | Embeddings #1 multilingual, Late Chunking |
| **Qdrant** | Berlin 🇩🇪 | Vector DB Rust-native |
| **Weaviate** | Amsterdam 🇳🇱 | Vector DB hybrid search |
| **Haystack / deepset** | Berlin 🇩🇪 | Framework production-grade |
| **Cohere** | Toronto 🇨🇦 | GDPR-native, 85% déploiements privés |

> "L'Europe a les briques pour construire un stack RAG souverain."

<small>Sources : [GitHub](https://github.com/) · [Jina AI](https://jina.ai/) · [Qdrant](https://qdrant.tech/) · [Weaviate](https://weaviate.io/)</small>

---

# 21 — Les 5 décisions clés pour l'entrepreneur

1. **Advanced RAG, pas Naive** — hybrid search + reranking couvre 80% des cas
2. **60-70% du temps sur la data quality** — chunking, cleaning, document processing
3. **Buy l'infra, Build l'orchestration** — l'orchestration est votre moat
4. **Évaluation RAGAS au jour 1** — pas après le déploiement
5. **GDPR-ready si marché européen** — Cohere, Qdrant, Weaviate, déploiement on-prem

| Phase | Budget indicatif |
|-------|-----------------|
| **MVP / POC** | < 2K€/mois |
| **Production** | 5-15K€/mois |
| **Enterprise** | 20K€+/mois |

<small>Sources : [MarketsandMarkets](https://www.marketsandmarkets.com/) · [Cohere](https://cohere.com/) · [RAGAS](https://docs.ragas.io/)</small>

---

# 22 — 5 faits à retenir

- **$1,85 Mds → $67 Mds** : le marché RAG croît à ~49% CAGR [1]
- **80% des use cases** = Advanced RAG (hybrid + reranking) suffit [2]
- **Data quality > model quality** : le chunking impacte plus que le modèle [3]
- **L'écosystème européen est complet** : ColPali, Docling, Jina, Qdrant, Weaviate, Haystack
- **5 documents empoisonnés suffisent** à compromettre un RAG (97% succès) [4]

> La prochaine fois que quelqu'un vous dit "il suffit de brancher un LLM sur vos données",
> vous saurez que le diable est dans le pipeline.

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [MarketsandMarkets](https://www.marketsandmarkets.com/) · [3] [Anthropic](https://www.anthropic.com/news/contextual-retrieval) · [4] [USENIX Security 2025](https://arxiv.org/abs/2402.07867)</small>
