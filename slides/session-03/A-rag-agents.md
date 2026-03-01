---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: RAG et Agents IA — pipeline RAG complet (chunking, embeddings, vector DB, hybrid search), agents (ReAct, tool use, MCP), synthèse décisionnelle. -->
<!-- ABOUTME: Session 3A pour étudiants M2 IMT&E Paris 1 : maîtriser les deux piliers de l'ingénierie IA appliquée. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# RAG & Agents IA

## Session 3A — Donner de la mémoire et des capacités à vos LLMs

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# RAG — Retrieval Augmented Generation

## Donner de la mémoire à votre LLM

---

# 01 — Pourquoi le RAG est indispensable

En Session 2, on a vu que les LLMs **hallucinent** et ont un **Knowledge Cutoff** :

- Ils inventent des réponses quand ils ne savent pas
- Ils ne connaissent rien après leur date d'entraînement
- Ils ne connaissent pas **vos données spécifiques** (catalogue, procédures, contrats)

**Sans RAG** : "Je n'ai pas assez d'informations pour répondre." (ou pire : il invente)

**Avec RAG** : "Oui, les employés peuvent se garer aux niveaux 1 et 2. Badge à l'accueil."

> Le RAG résout ces deux problèmes en **injectant vos documents dans le prompt**. Marché RAG : **$1,9 Mds** en 2025, **86%** des organisations l'adoptent [1][2].

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [K2View](https://www.k2view.com/)</small>

---

# 02 — Le RAG Pipeline en 5 étapes

Le RAG est un pipeline de bout en bout — chaque étape compte :

| Étape | Ce qu'elle fait | Outil typique |
|---|---|---|
| **1. Chunking** | Découper les documents en morceaux (256–1024 tokens) | LangChain, LlamaIndex |
| **2. Embedding** | Convertir chaque chunk en vecteur numérique | OpenAI, Jina, BGE-M3 |
| **3. Indexation** | Stocker les vecteurs dans une base vectorielle | Pinecone, Qdrant, pgvector |
| **4. Retrieval** | Chercher les chunks les plus pertinents pour la question | Hybrid Search (dense + sparse) |
| **5. Generation** | Le LLM génère sa réponse à partir des chunks récupérés | Claude, GPT-4o, Mistral |

> Le RAG réduit les hallucinations de **70–90%** par rapport à un LLM seul [1]. La qualité du Chunking impacte plus que le choix du modèle d'embedding [2].

<small>Sources : [1] [Données agrégées — recherche interne](docs/research/rag-ecosystem/report.md) · [2] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 03 — Chunking : découper intelligemment vos documents

Le Chunking transforme un document de 50 pages en morceaux exploitables par le LLM :

| Stratégie | Principe | Quand l'utiliser |
|---|---|---|
| **Fixed-size** | Découper tous les N tokens (256–512) | Prototypage rapide, données homogènes |
| **Recursive** | Découper par paragraphes, puis phrases si trop long | Standard pour la plupart des cas |
| **Semantic** | Détecter les ruptures de sens via embeddings | Documents longs et variés |
| **Overlap** | Chevauchement de 10–20% entre chunks | Toujours — évite de couper une idée en deux |

> Un mauvais Chunking = un RAG qui récupère des fragments inutiles. **C'est l'étape la plus sous-estimée** du pipeline — et celle qui impacte le plus la qualité finale [1].

**Règle pratique** : commencez par Recursive + Overlap de 15%, mesurez la qualité, puis itérez.

<small>Sources : [1] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 04 — Embeddings : transformer les mots en coordonnées

Un **Embedding** convertit du texte en coordonnées dans un espace à haute dimension — comme un GPS pour le sens :

- "Chat mignon" → [0.23, -0.45, 0.12, ..., 0.78] (1 024 dimensions)
- Les textes sémantiquement proches ont des coordonnées proches
- "Roi" et "Monarque" sont voisins ; "Roi" et "Réfrigérateur" sont éloignés

| Modèle | Éditeur | Prix/M tokens |
|---|---|---|
| **text-embedding-3-large** | OpenAI | $0,13 [1] |
| **Embed v4** | Cohere | $0,12 [2] |
| **jina-embeddings-v3** | Jina AI (Berlin) | $0,02 [3] |
| **BGE-M3** | BAAI | Gratuit (OSS) |

<small>Sources : [1] [OpenAI Pricing](https://openai.com/api/pricing/) · [2] [Cohere Pricing](https://cohere.com/pricing) · [3] [Jina AI](https://jina.ai/embeddings/)</small>

---

# 05 — Cosine Similarity : mesurer la pertinence

Comment le système sait-il quels documents sont "pertinents" pour une question ?

La **Cosine Similarity** mesure l'angle entre deux vecteurs — pas leur magnitude :

- Score de **+1** = textes de sens identique
- Score de **0** = aucun rapport
- Score de **-1** = sens opposé

> C'est la métrique au cœur de tous les moteurs de recherche sémantique et des systèmes RAG. C'est aussi un *choix business* : il définit ce que "pertinent" signifie pour votre produit.

*Astuce* : ajoutez un **Reranker** après la recherche initiale pour re-scorer les résultats — **+20–35% de précision** pour 50–500ms de latence supplémentaire [1].

<small>Sources : [1] [Données agrégées — recherche interne](docs/research/rag-ecosystem/report.md)</small>

---

# 06 — Vector Databases : stocker et chercher les vecteurs

Les vecteurs sont stockés dans des **bases vectorielles** optimisées pour la recherche par similarité :

| Base | Type | Différenciateur |
|---|---|---|
| **Chroma** | OSS (Apache 2.0) | Le plus simple — "le SQLite des vecteurs", parfait pour démarrer |
| **Qdrant** | OSS (Apache 2.0) | Rust-native, performant, EU-based (Berlin) — RGPD friendly |
| **Pinecone** | Managed (SaaS) | Zéro ops, serverless, leader du marché managed |
| **pgvector** | Extension PostgreSQL | Gratuit, 0 vendor lock-in, s'ajoute à votre base existante |

> **Pour démarrer** : Chroma (prototypage) ou pgvector (si vous avez déjà PostgreSQL). Pour scaler : Qdrant (contrôle) ou Pinecone (simplicité).

---

<!-- _class: cols -->

# 07 — Hybrid Search : le meilleur des deux mondes

<div class="left">

### Recherche par mots-clés (BM25)

- Compare les **mots exacts** entre requête et documents
- Rapide : 5–15ms, CPU uniquement
- Excellent pour les termes précis (codes produit, noms propres)
- **Faiblesse** : ne comprend pas les synonymes

</div>
<div class="right">

### Recherche sémantique (Embeddings)

- Compare le **sens** des textes via vecteurs
- Plus lent : ~45ms, nécessite GPU ou API
- Excellent pour les questions en langage naturel
- **Faiblesse** : peut manquer des termes exacts

</div>

> **La meilleure approche : les deux combinés** (Hybrid Search). Gain : **+15–30% de rappel** vs chaque méthode seule [1].

<small>Sources : [1] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 08 — RAG en pratique : chatbot RH

**Question utilisateur** : "Y a-t-il un parking pour les employés ?"

**Étape 1** — Le système cherche dans les documents RH → trouve le document "Facilities"

**Étape 2** — Le prompt envoyé au LLM devient :
```
Contexte : Politique parking — Tous les employés peuvent se
garer aux niveaux 1 et 2. Entrée par la rue Front [...]

Question : Y a-t-il un parking pour les employés ?
```

**Étape 3** — Le LLM répond en citant le document, avec un lien vers la source.

> Le RAG ajoute de la **traçabilité** : l'utilisateur peut vérifier la source. C'est un avantage décisif vs un LLM seul, surtout en contexte réglementé (finance, santé, juridique).

---

# 09 — Applications du RAG

Le RAG est partout en 2025–2026 — **86%** des organisations augmentent leurs LLMs avec du RAG [1] :

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

# 10 — Le LLM comme moteur de traitement

**Changement de mental model** — Ne pensez plus au LLM comme une source d'information, mais comme un **consultant spécialisé** :

- Vous lui confiez un **dossier client** (le contexte RAG)
- Il *analyse et synthétise* l'information que vous lui fournissez
- Sa valeur = raisonnement + synthèse, pas sa mémoire brute

**Implication pour les entrepreneurs** :
- Votre avantage compétitif n'est pas le modèle (accessible à tous)
- C'est **vos données propriétaires** + la qualité de votre pipeline RAG

> "Le LLM est le consultant. Le RAG est le dossier client. Votre valeur, c'est d'avoir le meilleur dossier."

---

<!-- _class: cols -->

# 11 — RAG vs Fine-tuning : comment choisir ?

<div class="left">

| Critère | RAG | Fine-tuning |
|---|---|---|
| **Données fraîches** | Temps réel | Statique |
| **Coût initial** | ~$70–1K/mois | $5–50/run |
| **Traçabilité** | Sources citables | Boîte noire |
| **Style/format** | Limité | Total contrôle |

</div>
<div class="right">

**En pratique** :
- **RAG** pour les données qui changent, quand la traçabilité compte
- **Fine-tuning** pour le style et les hauts volumes
- **Les deux combinés** : +10–20% d'accuracy vs séparément [1]

> Le bon choix dépend du volume, de la fraîcheur et du budget — pas de la hype.

</div>

<small>Sources : [1] [RAFT — UC Berkeley](https://arxiv.org/abs/2403.10131)</small>

---

<!-- _class: section -->

# Agents IA

## Le LLM qui planifie et agit

---

# 12 — Qu'est-ce qu'un Agent ?

Un **Agent** est un LLM qui enchaîne plusieurs actions de manière autonome pour accomplir un objectif.

La différence clé avec un chatbot :

| | Chatbot (LLM seul) | Agent |
|---|---|---|
| **Interaction** | 1 question → 1 réponse | Boucle autonome multi-étapes |
| **Outils** | Aucun | Recherche, API, code, bases de données |
| **Décision** | L'humain guide chaque étape | L'agent décide quoi faire ensuite |
| **Exemple** | "Résume ce texte" | "Trouve les 3 meilleurs fournisseurs, compare les prix, et rédige un email au moins cher" |

> L'agent **décide lui-même** quelles actions exécuter et dans quel ordre. C'est un bond par rapport au simple chat — et c'est ce qui crée le plus de valeur en 2026.

---

# 13 — La boucle ReAct : Reasoning + Acting

Le pattern dominant des agents est **ReAct** (Reasoning + Acting) [1] :

**Thought** — Le modèle raisonne sur la tâche
↓
**Action** — Il exécute une action (recherche, API, calcul)
↓
**Observation** — Il analyse le résultat
↓
**Thought** — Il décide : "J'ai assez d'info ?" → sinon, nouvelle action

**Exemple concret** :
- *Thought* : "Je dois trouver le chiffre d'affaires 2025 de Mistral AI"
- *Action* : Recherche web → "Mistral AI revenue 2025"
- *Observation* : "Résultat : Mistral a atteint $300M ARR en 2025"
- *Thought* : "J'ai la réponse, je peux la synthétiser pour l'utilisateur"

> La puissance de ReAct : le LLM **montre son raisonnement**, ce qui le rend auditable et débugable.

<small>Sources : [1] [Princeton/Google Research — ReAct](https://arxiv.org/abs/2210.03629)</small>

---

# 14 — Tool Use : donner des capacités au LLM

Les LLMs ont des limites intrinsèques. Le **Tool Use** (ou Function Calling) les compense :

| Limite du LLM | Outil | Exemple |
|---|---|---|
| Ne sait pas calculer | Calculatrice | "100 × 1,05^8 = ?" |
| Pas d'info temps réel | Recherche web | "Cours du Bitcoin ?" |
| Ne peut pas agir | API externe | "Commande un burger" |
| Pas de données privées | Base de données | "Mon solde bancaire ?" |

Le LLM génère un **appel de fonction structuré** (JSON), le système exécute, puis le LLM formule la réponse finale.

> En Session 2, on a vu le Structured Output — le Tool Use en est l'application directe : le LLM produit un JSON qui déclenche une action dans le monde réel.

---

<!-- _class: cols -->

# 15 — MCP : Model Context Protocol

<!-- TODO: expand after MCP deep research — ajouter des exemples concrets de serveurs MCP, l'écosystème de connecteurs, et des retours d'expérience de déploiement en entreprise -->

<div class="left">

### Le problème

Chaque outil = une intégration custom :
- API différente par fournisseur
- N modèles × M outils = **N×M** connecteurs
- Maintenance cauchemardesque

### La solution : MCP

Un **standard ouvert** (Anthropic, nov. 2024) qui définit comment les LLMs se connectent aux outils et aux données.

</div>
<div class="right">

### L'analogie USB-C

Avant USB-C : chaque appareil avait son câble. Après : un seul standard universel.

MCP = **USB-C pour l'IA** :
- 1 protocole → tous les outils
- Un serveur MCP expose des "tools" que tout agent peut appeler
- Adopté par Claude, Cursor, Windsurf, et un écosystème croissant [1]

</div>

> MCP transforme le marché : construire un outil compatible MCP = être **intégrable par tous les agents** du marché.

<small>Sources : [1] [Anthropic — MCP](https://www.anthropic.com/news/model-context-protocol)</small>

---

# 16 — Skills : des capacités composables

<!-- TODO: expand after Skills research — ajouter des exemples concrets de Skills packagées, la différence avec les simples tools, et comment les entreprises construisent des bibliothèques de Skills internes -->

Une **Skill** empaquète un outil + un prompt + un workflow en une capacité réutilisable :

| Concept | Ce que c'est | Exemple |
|---|---|---|
| **Tool** | Une fonction que l'agent peut appeler | `search_web(query)` |
| **Prompt** | Les instructions pour utiliser le tool | "Cherche 3 sources, vérifie la date" |
| **Skill** | Tool + Prompt + Logique métier | "Veille concurrentielle" = recherche + filtrage + résumé + alerte |

**Pourquoi ça compte** :
- Les Tools sont des briques élémentaires — les Skills sont des **processus métier**
- Une Skill est testable, versionnable, partageable entre agents
- C'est le passage du "l'agent sait utiliser Google" au "l'agent sait faire une veille marché"

> Pour une startup : construire des Skills propriétaires sur vos processus métier = votre **avantage compétitif** en IA.

---

# 17 — Méthodologie : construire un agent qui marche

<!-- TODO: expand after agent methodology research — ajouter des frameworks formels (LATS, Plan-and-Solve), des métriques de fiabilité, et des retours d'expérience d'échecs en production -->

La règle d'or : **commencer simple, ajouter de la complexité par couches** :

| Étape | Ce qu'on fait | Validation |
|---|---|---|
| **1. Single Tool** | Un agent, un outil, une tâche | L'outil s'exécute correctement à 95%+ |
| **2. Multi-tool** | Ajouter un deuxième outil | L'agent choisit le bon outil au bon moment |
| **3. Multi-step** | Tâches nécessitant 3–5 étapes | Le taux de complétion reste > 80% |
| **4. Autonomie** | L'agent gère des cas imprévus | Supervision humaine sur les cas limites |

> **Rappel critique** : 10 étapes à 95% de précision chacune = **~60% de succès global**. Chaque étape ajoutée **multiplie les risques d'échec**, pas les additionne.

**Question** : pour votre projet, quelle serait la tâche la plus simple à déléguer à un agent ?

---

# 18 — Les agents en 2026 : marché et écosystème

Le marché Agentic AI atteint **$7 Mds** en 2025, projeté **$139–260 Mds** en 2034 [1] :

| Technologie | Fournisseur | Ce que ça permet |
|---|---|---|
| **MCP** | Anthropic | Standard ouvert LLM → outils |
| **Computer Use** | Anthropic | L'agent contrôle souris et clavier |
| **Operator** | OpenAI | Agent qui navigue sur le web |
| **Coding Agents** | Cursor, Devin, Claude Code | Agents qui écrivent et testent du code |
| **Deep Research** | Gemini, Perplexity, ChatGPT | Agents de recherche multi-sources |

> **67%** des Fortune 500 ont déployé des agents en 2025 [2]. La tendance 2026 : les agents ne sont plus des démos — ils sont en production.

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [Gartner](https://www.gartner.com/)</small>

---

# 19 — Agents : attention aux limites

Les agents sont prometteurs mais présentent des défis sérieux en 2026 :

- **Fiabilité** — 10 étapes à 95% de précision chacune = ~60% de précision globale
- **Coût** — un workflow d'agent peut coûter 10–100x un simple prompt
- **Sécurité** — un agent avec accès à des outils peut agir de manière imprévue
- **Taux d'échec** — Gartner prévoit **40%** des projets agents annulés d'ici 2027 [1]

> **Pour les startups** : les agents sont idéaux pour les tâches internes (analyse, recherche, reporting) où la supervision humaine est facile. Prudence pour les agents en contact direct avec les clients.

<small>Sources : [1] [Gartner](https://www.gartner.com/)</small>

---

# 20 — Discussion : où les agents créent-ils le plus de valeur ?

Réfléchissez à votre projet d'équipe :

**Les meilleurs cas d'usage agents** (2026) :
- Tâches **répétitives et structurées** (reporting, veille, extraction)
- Flux internes avec **supervision humaine** facile
- Processus où le coût de l'erreur est **faible** (brouillon, recherche, triage)

**Les pires cas d'usage agents** (aujourd'hui) :
- Contact client direct sans filet de sécurité
- Décisions financières ou juridiques autonomes
- Processus critiques sans possibilité de rollback

> **Question pour la classe** : quelle tâche répétitive dans votre projet de startup pourrait être déléguée à un agent IA ? Avec quel niveau de supervision humaine ?

---

<!-- _class: section -->

# Synthèse

## La boîte à outils de l'ingénieur IA

---

# 21 — La boîte à outils : Prompting → RAG → Agents → Fine-tuning

| Besoin | Outil | Effort | Coût | Quand |
|---|---|---|---|---|
| Automatiser une tâche texte | **Prompting** | Minutes | Quasi nul | Toujours — c'est la base |
| Intégrer ses propres données | **RAG** | Jours | Faible | Données propriétaires, fraîcheur |
| Connecter à des systèmes | **Tool Use** | Jours | Faible | Actions dans le monde réel |
| Automatiser des workflows | **Agents** | Semaines | Variable | Tâches multi-étapes complexes |
| Adapter le style ou le savoir | **Fine-tuning** | Semaines | Moyen | Hauts volumes, format spécifique |

> L'ordre de priorité pour une startup : **Prompting → RAG → Tool Use → Agents → Fine-tuning**. La plupart des projets n'ont pas besoin d'aller au-delà du RAG.

---

# 22 — Key Takeaways

1. **Le RAG est le standard** — 86% des organisations l'utilisent ; c'est votre premier investissement après le Prompting

2. **La qualité du pipeline compte** — Chunking, Hybrid Search et Reranking impactent plus que le choix du modèle

3. **RAG vs Fine-tuning** — RAG pour données fraîches et traçables, Fine-tuning pour le style. Combinés : +10–20%

4. **Les agents = boucle ReAct** — Reasoning + Acting en autonomie, mais chaque étape multiplie les risques

5. **MCP standardise l'écosystème** — construire compatible MCP = être intégrable par tous les agents

6. **Commencer simple** — Prompting → RAG → Tool Use → Agents → Fine-tuning

---

# 23 — Pour la suite

**À explorer** :

- Testez un outil de RAG gratuit : uploadez un PDF sur **ChatPDF** ou **Claude** et posez-lui des questions
- Identifiez dans votre projet : avez-vous besoin de Prompting seul, de RAG, ou d'agents ?
- Réfléchissez à la source de données qui donnerait le plus de valeur en RAG

**Prochaine séance : Le business de l'IA**
- L'écosystème IA (qui fait quoi, la chaîne de valeur)
- Business Models & cas réels (Klarna, Mistral AI, L'Oréal)

> "Le LLM est le consultant. Le RAG est le dossier client. L'agent est l'assistant qui va chercher le dossier, l'analyse, et planifie les prochaines étapes."
