---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Données publiques"
---
<!-- ABOUTME: L'ingénierie IA — RAG pipeline complet, embeddings, Fine-tuning, LLM generations, agents. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : choisir entre RAG, Fine-tuning et agents selon son projet. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# L'Ingénierie IA

## Session 2B — RAG, Fine-tuning & Agents

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# RAG — Retrieval Augmented Generation

## Donner de la mémoire à votre LLM

---

# 01 — Le problème que RAG résout

Un LLM généraliste ne connaît pas **vos données spécifiques** :

- Il ne connaît pas la politique de parking de votre entreprise
- Il ne connaît pas votre catalogue produit
- Il ne connaît pas vos procédures internes

**Sans RAG** : "Je n'ai pas assez d'informations pour répondre."

**Avec RAG** : "Oui, les employés peuvent se garer aux niveaux 1 et 2. Badge à l'accueil."

> Le RAG permet à un LLM de répondre sur **vos données** sans avoir besoin de le ré-entraîner. Le marché RAG atteint **$1,9 Mds** en 2025, avec **86%** des organisations qui l'adoptent [1][2].

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [K2View](https://www.k2view.com/)</small>

---

<!-- _class: compact -->

# 02 — Le RAG Pipeline en 5 étapes

Le RAG est un pipeline de bout en bout — chaque étape compte :

| Étape | Action | Outil typique |
|---|---|---|
| **1. Chunking** | Découper les docs (256-1024 tokens) | LangChain, LlamaIndex |
| **2. Embedding** | Convertir chaque chunk en vecteur | OpenAI, Jina, BGE-M3 |
| **3. Indexation** | Stocker dans une base vectorielle | Pinecone, Qdrant, pgvector |
| **4. Retrieval** | Chercher les chunks pertinents | Hybrid search (dense + sparse) |
| **5. Generation** | Répondre à partir des chunks | Claude, GPT-4o, Mistral |

![bg right:35% contain](assets/infographics/rag-pipeline_run_20260219_100700_b17371.png)

<small>Sources : [1] [Recherche interne](docs/courses/sorbonne-m2/research/rag-ecosystem/report.md) · [2] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

<!-- _class: compact -->

# 02b — RAG Pipeline : impact et bonnes pratiques

Le RAG réduit les hallucinations de **70-90%** vs un LLM seul [1].

La qualité du **Chunking** impacte plus que le choix du modèle d'embedding [2] :
- Chunks trop grands → bruit, contexte dilué
- Chunks trop petits → perte de contexte
- Sweet spot : **256-1024 tokens** selon le domaine

> Optimisez le Chunking en priorité — c'est le levier n°1 de qualité d'un pipeline RAG.

<small>Sources : [1] [Recherche interne](docs/courses/sorbonne-m2/research/rag-ecosystem/report.md) · [2] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

<!-- _class: cols -->

# 03 — Le moteur de recherche sémantique

<div class="left">

### Recherche par mots-clés (BM25)

- Compare les **mots exacts** entre la requête et les documents
- Rapide : 5-15ms, CPU uniquement
- Excellent pour les termes précis (codes produit, noms propres)
- **Faiblesse** : ne comprend pas les synonymes ou paraphrases

</div>
<div class="right">

### Recherche sémantique (Embeddings)

- Compare le **sens** des textes via des vecteurs
- Plus lent : ~45ms, nécessite GPU ou API
- Excellent pour les questions en langage naturel
- **Faiblesse** : peut manquer des termes exacts ou rares

</div>

> **Meilleure approche : Hybrid Search** (les deux combinés) → **+15-30% de rappel** [1]

<small>Sources : [1] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 04 — Embeddings : transformer les mots en coordonnées

Un **Embedding** convertit du texte en coordonnées à haute dimension — un GPS pour le sens :

- "Chat mignon" → [0.23, -0.45, 0.12, …, 0.78] (1 024 dim.)
- Textes proches en sens = coordonnées proches
- "Roi" et "Monarque" sont voisins ; "Roi" et "Réfrigérateur" éloignés

| Modèle | Éditeur | Prix/M tokens |
|---|---|---|
| **text-embedding-3-large** | OpenAI | $0,13 [1] |
| **Embed v4** | Cohere | $0,12 [2] |
| **jina-embeddings-v3** | Jina AI (Berlin) | $0,02 [3] |
| **BGE-M3** | BAAI | Gratuit (OSS) |

<small>Sources : [1] [OpenAI Pricing](https://openai.com/api/pricing/) · [2] [Cohere Pricing](https://cohere.com/pricing) · [3] [Jina AI](https://jina.ai/embeddings/)</small>

---

# 05 — La similarité vectorielle : Cosine Similarity

Comment le système sait-il quels documents sont "pertinents" pour une question ?

La **Cosine Similarity** mesure l'angle entre deux vecteurs — pas leur magnitude :

- Score de **+1** = textes de sens identique
- Score de **0** = aucun rapport
- Score de **-1** = sens opposé

> C'est la métrique au cœur de tous les moteurs de recherche sémantique et des systèmes RAG. C'est aussi un *choix business* : il définit ce que "pertinent" signifie pour votre produit.

*Astuce* : ajoutez un **Reranker** après la recherche initiale pour re-scorer les résultats — **+20-35% de précision** pour 50-500ms de latence supplémentaire [1].

<small>Sources : [1] [Données agrégées — recherche interne](docs/courses/sorbonne-m2/research/rag-ecosystem/report.md)</small>

---

<!-- _class: compact -->

# 06 — Vector Databases : stocker et chercher les vecteurs

Bases optimisées pour la recherche par similarité :

| Base | Type | Différenciateur |
|---|---|---|
| **Chroma** | OSS | "Le SQLite des vecteurs" — idéal pour démarrer |
| **Qdrant** | OSS | Rust-native, EU-based (Berlin) — RGPD friendly |
| **Pinecone** | SaaS | Zéro ops, serverless, leader managed |
| **pgvector** | Extension PG | Gratuit, 0 vendor lock-in |

<!-- Speaker notes: Pour démarrer : Chroma (prototypage) ou pgvector (si vous avez déjà PostgreSQL). Pour scaler : Qdrant (contrôle) ou Pinecone (simplicité). -->

![bg right:35% contain](assets/vecotr-database.png)

---

# 07 — RAG en pratique : l'exemple du chatbot RH

**Question utilisateur** : "Y a-t-il un parking pour les employés ?"

**Étape 1** — Le système cherche dans les documents RH → trouve le document "Facilities"

**Étape 2** — Le prompt envoyé au LLM devient :
```
Contexte : Politique parking — Tous les employés peuvent se
garer aux niveaux 1 et 2. Entrée par la rue Front [...]

Question : Y a-t-il un parking pour les employés ?
```

**Étape 3** — Le LLM répond en citant le document, avec un lien vers la source.

> Le RAG ajoute aussi de la **traçabilité** : l'utilisateur peut vérifier la source de l'information.

---

# 08 — Applications du RAG

Le RAG est partout en 2025-2026 — **86%** des organisations augmentent leurs LLMs avec du RAG [1] :

| Application | Source de données | Exemple |
|---|---|---|
| **Chat with PDFs** | Documents internes | ChatPDF, PDF.ai |
| **Support client** | Base de connaissances | Chatbots Zendesk, Intercom |
| **Recherche web augmentée** | Internet en temps réel | Perplexity, Google AI Overview |
| **Assistants spécialisés** | Documentation technique | Cursor, GitHub Copilot |
| **Analyse juridique** | Corpus légal | Harvey AI, Doctrine.fr |

> Pour un entrepreneur, le RAG est souvent **la première technologie à implémenter** après le simple Prompting.

<small>Sources : [1] [K2View](https://www.k2view.com/)</small>

---

# 09 — Le LLM comme moteur de traitement

**Changement de mental model** — Ne pensez plus au LLM comme une source d'information, mais comme un **consultant spécialisé** :

- Vous lui confiez un **dossier client** (le contexte RAG)
- Il *analyse et synthétise* l'information que vous lui fournissez
- Sa valeur = raisonnement + synthèse, pas sa mémoire brute

**Implication pour les entrepreneurs** :
- Votre avantage compétitif n'est pas le modèle (accessible à tous)
- C'est **vos données propriétaires** + la qualité de votre pipeline RAG

> "Le LLM est le consultant. Le RAG est le dossier client. Votre valeur, c'est d'avoir le meilleur dossier."

---

<!-- _class: section -->

# Fine-tuning et RAG

## Quand choisir quoi

---

<!-- _class: cols -->

# 10 — RAG vs Fine-tuning : comment choisir ?

<div class="left">

| Critère | RAG | Fine-tuning |
|---|---|---|
| **Données fraîches** | Temps réel | Statique |
| **Coût initial** | ~$70-1K/mois | $5-50/run |
| **Traçabilité** | Sources citables | Boîte noire |
| **Style/format** | Limité | Total contrôle |

</div>
<div class="right">

**En pratique** :
- **RAG** pour les données qui changent, quand la traçabilité compte
- **Fine-tuning** pour le style et les hauts volumes
- **Les deux combinés** : +10-20% d'accuracy vs séparément [1]

> Le bon choix dépend du volume, de la fraîcheur et du budget — pas de la hype.

</div>

<small>Sources : [1] [RAFT UC Berkeley](https://arxiv.org/abs/2403.10131)</small>

---

<!-- _class: section -->

# Agents IA

## Le LLM qui planifie et agit

---

<!-- _class: compact -->

# 11 — Qu'est-ce qu'un Agent ?

Un **Agent** est un LLM qui enchaîne plusieurs actions de manière autonome.

Le pattern dominant est **ReAct** (Reasoning + Acting) [1] :
- *Thought* — le modèle raisonne sur la tâche
- *Action* — il exécute (recherche, calcul…)
- *Observation* — il analyse le résultat et décide la suite

> L'agent **décide lui-même** quelles actions exécuter et dans quel ordre.

![bg right:38% contain](assets/infographics/agent-react_run_20260216_171318_224f91.png)

<small>Sources : [1] [Princeton/Google Research](https://arxiv.org/abs/2210.03629)</small>

---

<!-- _class: compact -->

# 12 — Tool Use : donner des capacités au LLM

Le **Tool Use** compense les limites intrinsèques des LLMs :

- *Calcul* → Calculatrice ("100 x 1,05^8 = ?")
- *Temps réel* → Recherche web ("Cours du Bitcoin ?")
- *Action* → API externe ("Commande un burger")
- *Données privées* → Base de données ("Mon solde ?")

Le LLM génère un **appel de fonction**, le système exécute et renvoie le résultat.

![bg right:38% contain](assets/infographics/tool-use_run_20260216_171320_c1b044.png)

---

# 13 — Les agents en 2026 : marché et écosystème

Le marché agentic AI atteint **$7 Mds** en 2025, projeté **$139-260 Mds** en 2034 [1].

| Technologie | Fournisseur | Ce que ça permet |
|---|---|---|
| **MCP** (Model Context Protocol) | Anthropic | Standard ouvert LLM → outils |
| **Computer Use** | Anthropic | L'agent contrôle souris et clavier |
| **Operator** | OpenAI | Agent qui navigue sur le web |
| **Coding Agents** | Cursor, Devin, Claude Code | Agents qui écrivent et testent du code |

> **67%** des Fortune 500 ont déployé des agents en 2025 [2]. Construire des outils compatibles MCP = être intégrable par tous les agents.

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [Gartner](https://www.gartner.com/)</small>

---

# 14 — Agents : attention aux limites

Les Agents sont prometteurs mais présentent des défis en 2026 :

- **Fiabilité** — 10 étapes à 95% de précision chacune = ~60% de précision globale
- **Coût** — un workflow d'agent peut coûter 10-100x un simple prompt
- **Sécurité** — un agent avec accès à des outils peut agir de manière imprévue
- **Taux d'échec** — Gartner prévoit **40%** des projets agents annulés d'ici 2027 [1]

> **Pour les startups** : les agents sont idéaux pour les tâches internes (analyse, recherche, reporting) où la supervision humaine est facile. Prudence pour les agents en contact direct avec les clients.

**Question pour la classe** : Quelle tâche répétitive dans votre projet de startup pourrait être déléguée à un agent IA ? Avec quel niveau de supervision humaine ?

<small>Sources : [1] [Gartner](https://www.gartner.com/)</small>

---

<!-- _class: section -->

# Synthèse

## La boîte à outils complète

---

# 15 — La boîte à outils de l'entrepreneur IA

| Besoin | Outil | Effort | Coût |
|---|---|---|---|
| Automatiser une tâche texte | **Prompting** | Minutes | Quasi nul |
| Intégrer ses propres données | **RAG** | Jours | Faible |
| Adapter le style ou le savoir | **Fine-tuning** | Semaines | Moyen |
| Connecter à des systèmes externes | **Tool Use** | Jours | Faible |
| Automatiser des workflows complets | **Agents** | Semaines | Variable |

> L'ordre de priorité pour une startup : **Prompting → RAG → Tool Use → Fine-tuning → Agents**.

---

# 16 — Key Takeaways

1. **Le RAG est le standard** — 86% des organisations l'utilisent, c'est souvent votre premier investissement après le Prompting

2. **Hybrid Search + Reranking** — combine mots-clés et sémantique pour +15-30% de rappel, le Reranking ajoute +20-35% de précision

3. **RAG vs Fine-tuning** — RAG pour données fraîches et traçables, Fine-tuning pour le style et le format. Les deux combinés : +10-20% d'accuracy

4. **Les agents sont la prochaine frontière** — $7 Mds de marché, mais 40% de taux d'échec. Commencer simple.

5. **L'ordre de priorité** — Prompting → RAG → Tool Use → Fine-tuning → Agents

---

# 17 — Pour la prochaine séance

**À explorer avant la séance 3** :

- Testez un outil de RAG gratuit : uploadez un PDF sur **ChatPDF** ou **Claude**
- Réfléchissez à votre projet startup IA : quel problème et pour qui ?
- Identifiez si vous avez besoin de Prompting seul, de RAG ou de Fine-tuning

**Prochaine séance : Cadrer et gérer un projet IA**
- CRISP-DM et AI Canvas
- Build vs Buy
- Constituer une équipe IA

> "La meilleure façon de prédire l'avenir, c'est de le construire." Les outils n'ont jamais été aussi accessibles.
