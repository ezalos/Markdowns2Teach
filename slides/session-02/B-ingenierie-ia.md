---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Données publiques"
---
<!-- ABOUTME: L'ingénierie IA — RAG, embeddings, Fine-tuning, agents, pour comprendre les briques techniques. -->
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

> Le RAG permet à un LLM de répondre sur **vos données** sans avoir besoin de le ré-entraîner. Le marché RAG atteint **$1,85 Mds** en 2025 [1].

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/)</small>

---

<!-- _class: cols -->

# 02 — RAG : comment ça marche

<div class="left">

### Étape 1 : Retrieval
Quand l'utilisateur pose une question, le système **cherche les documents pertinents** dans votre base de connaissances.

### Étape 2 : Augmentation
Les extraits trouvés sont **injectés dans le prompt** du LLM comme contexte additionnel.

</div>
<div class="right">

### Étape 3 : Generation
Le LLM génère sa réponse en s'appuyant sur **le contexte fourni** — pas uniquement sur son entraînement initial.

> **R**etrieval **A**ugmented **G**eneration = on *augmente* la génération avec de la *recherche*.

</div>

---

# 03 — La similarité : pourquoi le RAG fonctionne

Comment le système sait-il quels documents sont "pertinents" pour une question ?

| Métrique | Principe | Cas d'usage |
|---|---|---|
| **Cosine Similarity** | Compare la **direction** de deux vecteurs, pas leur magnitude | Recherche sémantique, RAG |
| **Euclidean Distance** | Distance "en ligne droite" entre deux points | Peu de variables, valeurs comparables |
| **Manhattan Distance** | Somme des écarts absolus | Données hétérogènes, grande dimension |

- La Cosine Similarity mesure un angle entre -1 (opposés) et +1 (identiques)
- C'est la métrique au coeur des moteurs de recherche sémantique et des systèmes RAG

> Le choix de la métrique de similarité est un **choix business** : il définit ce que "pertinent" signifie pour votre produit.

---

# 04 — Embeddings : transformer les mots en vecteurs

Un **Embedding** convertit du texte en un vecteur numérique de grande dimension :

- "Chat mignon" → [0.23, -0.45, 0.12, ..., 0.78] (1 024 dimensions)
- Les textes sémantiquement proches ont des vecteurs proches

| Modèle | Éditeur | Dimensions | Prix/M tokens |
|---|---|---|---|
| **text-embedding-3-large** | OpenAI | 3 072 | $0,13 [2] |
| **Embed v4** | Cohere | 1 024 | $0,12 [3] |
| **jina-embeddings-v3** | Jina AI (Berlin) | 1 024 | $0,02 [4] |
| **BGE-M3** | BAAI | 1 024 | Gratuit (OSS) |

> La qualité du **Chunking** (découpage des documents) impacte plus que le choix du modèle d'embedding [1].

<small>Sources : [1] [Anthropic](https://www.anthropic.com/news/contextual-retrieval) · [2] [OpenAI Pricing](https://openai.com/api/pricing/) · [3] [Cohere Pricing](https://cohere.com/pricing) · [4] [Jina AI](https://jina.ai/embeddings/)</small>

---

# 05 — Vector Databases : stocker et chercher les vecteurs

Les vecteurs sont stockés dans des **bases vectorielles** optimisées pour la recherche par similarité :

| Base | Type | Différenciateur | Origine |
|---|---|---|---|
| **Pinecone** | Managed | Leader serverless, free tier | USA |
| **Qdrant** | OSS + Cloud | Rust-native, performant | Berlin |
| **Weaviate** | OSS + Cloud | Hybrid Search natif | Amsterdam |
| **pgvector** | Extension PG | Gratuit, 0 vendor lock-in | OSS |

- **pgvector** : la meilleure option pour démarrer (gratuit, pas de vendor lock-in)
- **Pinecone** : le plus rapide à déployer (managed, serverless)

> **Règle d'or** : Managed pour la vitesse. Open-source pour le contrôle et les coûts à l'échelle.

<small>Sources : [GitHub](https://github.com/) · [Pinecone](https://www.pinecone.io/) · [Qdrant](https://qdrant.tech/)</small>

---

# 06 — RAG en pratique : l'exemple du chatbot RH

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

# 07 — Applications du RAG

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

# 08 — Le LLM comme moteur de raisonnement

**Changement de mental model** — Ne pensez plus au LLM comme une source d'information, mais comme un **moteur de raisonnement** :

- Les LLMs ont des connaissances générales, mais pas tout
- En leur fournissant du **contexte pertinent** via le prompt, on leur demande de *lire et traiter* l'information
- Le LLM raisonne sur l'information fournie plutôt que de puiser dans sa mémoire

**Implication pour les entrepreneurs** :
- Votre avantage compétitif n'est pas le modèle (accessible à tous)
- C'est **vos données propriétaires** + la qualité de votre pipeline RAG

> "Le LLM est le cerveau. Le RAG est la bibliothèque. Votre valeur, c'est d'avoir la meilleure bibliothèque."

---

<!-- _class: section -->

# Fine-tuning

## Quand le RAG ne suffit plus

---

<!-- _class: cols -->

# 09 — Fine-tuning : de quoi parle-t-on ?

<div class="left">

Le **Fine-tuning** consiste à ré-entraîner un modèle existant sur vos propres données :

| | Pretraining | Fine-tuning |
|---|---|---|
| **Données** | Milliards de mots | Milliers d'exemples |
| **Objectif** | Apprendre le langage | Adapter à une tâche |
| **Coût** | Millions $ | Centaines $ |

</div>
<div class="right">

**Quand fine-tuner ?**
- Le modèle a besoin d'un **style** spécifique
- Le jargon est trop technique (médical, juridique)
- Le RAG ne capture pas le **format** attendu

> Analogie : le musicien connaît la musique mais apprend un nouveau style.

</div>

---

# 10 — L'escalade de personnalisation

L'ordre de complexité et de coût croissants est clair [1] :

| Étape | Coût | Délai | Quand l'utiliser |
|---|---|---|---|
| **Prompt Engineering** | $0 | Heures | **80% des cas** — toujours commencer ici |
| **RAG** | $70-1 000/mois | Heures-jours | Données fraîches, sources vérifiables |
| **Fine-tuning (LoRA)** | $5-50/run | Jours | Style, format, tâche spécifique |
| **Pretraining** | $1M+ | Mois | Domaine ultra-spécialisé (rare) |

> **80% des besoins** se résolvent avec du Prompt Engineering + RAG. Ne fine-tuner que si le gain justifie le coût.

<small>Sources : [1] [Meta AI](https://ai.meta.com/blog/when-to-fine-tune-llms-vs-other-techniques/)</small>

---

# 11 — LoRA : la démocratisation du Fine-tuning

**LoRA** (Low-Rank Adaptation) entraîne de petites matrices au lieu du modèle entier [1] :

- Entraîne **0,1-1%** des paramètres → **90-95%** de la qualité totale
- Un adapter LoRA pèse **10-100 Mo** (vs 14+ Go pour un modèle complet)
- **QLoRA** ajoute la quantification 4-bit → un modèle 7B tourne sur **8 Go de VRAM** [2]

| Config | VRAM requise | Coût | Hardware minimum |
|---|---|---|---|
| 7B LoRA | ~16-24 GB | $5-15 | RTX 4090 |
| 7B QLoRA | ~8-10 GB | **$0-5** | **Google Colab T4 gratuit** |

> Le rapport qualité/prix de QLoRA a **démocratisé** le Fine-tuning pour les startups.

<small>Sources : [1] [Hu et al. ICLR 2022](https://arxiv.org/abs/2106.09685) · [2] [Dettmers et al. NeurIPS 2023](https://arxiv.org/abs/2305.14314)</small>

---

# 12 — Distillation : un grand modèle entraîne un petit

Le principe de **Distillation** :
- Un **grand modèle** (100B+ paramètres) sait bien faire une tâche
- On utilise ses réponses comme données d'entraînement pour un **petit modèle** (1B paramètres)
- Le petit modèle apprend à imiter le grand sur cette tâche spécifique

**Pourquoi c'est utile** :
- **Coût divisé par 10-100x** en production
- **Latence réduite** — réponses plus rapides
- **Déploiement on-device** — mobile, laptop, edge

> Avec 500-1 000 exemples, un petit modèle fine-tuned peut égaler un grand modèle sur une tâche ciblée. DeepSeek-R1 distillé sur Qwen-7B atteint **55,5%** sur AIME 2024 [1].

<small>Sources : [1] [DeepSeek](https://arxiv.org/abs/2501.12948)</small>

---

<!-- _class: cols -->

# 13 — RAG vs Fine-tuning : comment choisir ?

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

# 14 — Qu'est-ce qu'un Agent ?

Un **Agent** est un LLM qui enchaîne plusieurs actions de manière autonome.

Le pattern dominant est **ReAct** (Reasoning + Acting) [1] :
- *Thought* — le modèle raisonne sur la tâche
- *Action* — il exécute une action (recherche, visite, calcul)
- *Observation* — il analyse le résultat et décide la suite

> L'agent **décide lui-même** quelles actions exécuter et dans quel ordre. C'est un bond par rapport au simple chat.

![bg right:50%](assets/infographics/agent-react_run_20260216_171318_224f91.png)

<small>Sources : [1] [Princeton/Google Research](https://arxiv.org/abs/2210.03629)</small>

---

# 15 — Tool Use : donner des capacités au LLM

Les LLMs ont des limites intrinsèques. Le **Tool Use** les compense :

- *Calcul* → Calculatrice ("100 x 1,05^8 = ?")
- *Temps réel* → Recherche web ("Cours du Bitcoin ?")
- *Action* → API externe ("Commande un burger")
- *Données privées* → Base de données ("Mon solde ?")

Le LLM génère un **appel de fonction**, le système exécute et renvoie le résultat, puis le LLM formule la réponse finale.

![bg right:50%](assets/infographics/tool-use_run_20260216_171320_c1b044.png)

---

# 16 — Les agents en 2026 : marché et écosystème

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

# 17 — Agents : attention aux limites

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

# 18 — La boîte à outils de l'entrepreneur IA

| Besoin | Outil | Effort | Coût |
|---|---|---|---|
| Automatiser une tâche texte | **Prompting** | Minutes | Quasi nul |
| Intégrer ses propres données | **RAG** | Jours | Faible |
| Adapter le style ou le savoir | **Fine-tuning** | Semaines | Moyen |
| Connecter à des systèmes externes | **Tool Use** | Jours | Faible |
| Automatiser des workflows complets | **Agents** | Semaines | Variable |

> L'ordre de priorité pour une startup : **Prompting → RAG → Tool Use → Fine-tuning → Agents**.

---

# 19 — Key Takeaways

1. **Le RAG est le standard** — 86% des organisations l'utilisent, c'est souvent votre premier investissement après le Prompting

2. **Embeddings + Vector DB = le pipeline** — transformer vos documents en vecteurs et les chercher par similarité

3. **Fine-tuning quand le RAG ne suffit pas** — style, format, jargon. QLoRA rend le Fine-tuning gratuit pour prototyper

4. **RAG + Fine-tuning sont complémentaires** — +10-20% d'accuracy en les combinant

5. **Les agents sont la prochaine frontière** — $7 Mds de marché, mais 40% de taux d'échec. Commencer simple.

---

# 20 — Pour la prochaine séance

**À explorer avant la séance 3** :

- Testez un outil de RAG gratuit : uploadez un PDF sur **ChatPDF** ou **Claude** et posez-lui des questions
- Réfléchissez à votre projet de startup IA : quel problème résolvez-vous et pour qui ?
- Identifiez si votre projet a besoin de Prompting seul, de RAG, ou de Fine-tuning

**Prochaine séance : Cadrer et gérer un projet IA**
- CRISP-DM et AI Canvas
- Build vs Buy
- Constituer une équipe IA

> "La meilleure façon de prédire l'avenir, c'est de le construire." Avec la Generative AI, les outils pour construire n'ont jamais été aussi accessibles.
