---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: RAG et Embeddings — pipeline RAG complet (chunking, embeddings, vector DB, hybrid search, reranking) avec deep dive progressif sur les embeddings. -->
<!-- ABOUTME: Session 3A pour étudiants M2 IMT&E Paris 1 : comprendre le RAG et la mécanique des embeddings qui le rend possible. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# RAG — Retrieval Augmented Generation

## Session 3A — Donner de la mémoire à votre LLM

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Pourquoi le RAG ?

## Quand le LLM ne sait pas

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

<!-- _class: img-right -->

# 02 — Le RAG Pipeline en 5 étapes

- **1. Chunking** — découper les documents en morceaux (256–1024 tokens)
- **2. Embedding** — convertir chaque chunk en vecteur numérique
- **3. Indexation** — stocker les vecteurs dans une base vectorielle
- **4. Retrieval** — chercher les chunks pertinents pour la question
- **5. Generation** — le LLM génère sa réponse à partir du contexte

> Le RAG réduit les hallucinations de **70–90%** vs un LLM seul [1].

![bg right:55% contain](assets/infographics/rag-pipeline-5-steps.png)

<small>Sources : [1] [Anthropic](https://www.anthropic.com/news/contextual-retrieval)</small>

---

# 03 — Le LLM comme consultant

**Changement de mental model** — le LLM n'est pas une base de données, c'est un **consultant spécialisé** :

- Vous lui confiez un **dossier client** (le contexte RAG)
- Il *analyse et synthétise* l'information que vous lui fournissez
- Sa valeur = raisonnement + synthèse, pas sa mémoire brute

**Implication pour les entrepreneurs** :
- Votre avantage compétitif n'est pas le modèle (accessible à tous)
- C'est **vos données propriétaires** + la qualité de votre pipeline RAG

> "Le LLM est le consultant. Le RAG est le dossier client. Votre valeur, c'est d'avoir le meilleur dossier."

---

<!-- _class: section -->

# Embeddings

## Le GPS du sens

---

<!-- _class: img-right -->

# 04 — Intuition : les mots comme coordonnées

- Un **Embedding** transforme du texte en **coordonnées** dans un espace mathématique
- Analogie : un **GPS pour le sens** — textes proches en sens = coordonnées proches
- "Chat mignon" et "Chaton adorable" → coordonnées voisines
- "Chat mignon" et "Réfrigérateur" → coordonnées éloignées
- C'est ainsi que le RAG "sait" quels documents sont pertinents

> L'embedding encode le **sens**, pas les mots exacts. C'est la brique fondamentale de toute recherche sémantique.

![bg right:55% contain](assets/infographics/embeddings-2d-vectors.png)

---

<!-- _class: img-right -->

# 05 — Des vecteurs 2D aux vrais Embeddings

- En 2D : facile à dessiner, chaque mot = une flèche depuis l'origine
- En réalité : les modèles utilisent **768 à 3 072 dimensions**
- Plus de dimensions = plus de nuances capturées (ton, domaine, contexte)

| Modèle | Dimensions |
|---|---|
| MiniLM | 384 |
| BGE-M3 | 1 024 |
| OpenAI large | 3 072 |

> La math est la même quelle que soit la dimension. Le notebook vous permet de manipuler ces vecteurs.

![bg right:55% contain](assets/infographics/embeddings-2d-to-768d.png)

---

<!-- _class: img-right -->

# 06 — PCA : voir l'invisible

- **Problème** : on ne peut pas visualiser 768 dimensions
- **PCA** compresse les dimensions en préservant la structure la plus importante
- Analogie : photographier un bâtiment 3D → on perd la profondeur mais on garde la forme
- Le notebook projette 768 dimensions sur 2D avec PCA

> C'est ainsi que sont produites toutes les "visualisations de clusters" dans les publications IA.

![bg right:55% contain](assets/infographics/pca-projection.png)

---

<!-- _class: img-right -->

# 07 — Cosine Similarity : mesurer la pertinence

- Comment le système sait quels documents sont "pertinents" ?
- La **Cosine Similarity** mesure l'**angle** entre deux vecteurs
- Score **+1** = sens identique · **0** = aucun rapport · **−1** = sens opposé
- C'est la métrique au cœur de tout moteur de recherche sémantique

> C'est aussi un *choix business* : la Cosine Similarity définit ce que "pertinent" signifie pour votre produit.

![bg right:55% contain](assets/infographics/cosine-similarity-angles.png)

---

<!-- _class: img-right -->

# 08 — Les clusters sémantiques

- Quand on embed beaucoup de mots, ils forment **naturellement** des clusters par sens
- Animaux ensemble, couleurs ensemble, professions ensemble
- Ce n'est pas programmé — ça **émerge** des données d'entraînement
- Le modèle a appris une "carte du savoir humain"

> Dans votre RAG : les documents sur des sujets similaires se regroupent dans la base vectorielle. La qualité de ces clusters = la qualité de votre retrieval.

![bg right:55% contain](assets/infographics/semantic-clusters.png)

---

<!-- _class: img-right -->

# 09 — Word Arithmetic : Roi − Homme + Femme ≈ Reine

- La propriété la plus surprenante : on peut **faire des maths avec le sens**
- King − Man + Woman ≈ Queen
- Paris − France + Japan ≈ Tokyo
- Les embeddings encodent des **relations**, pas juste de la similarité [1]

> Le notebook vous permet de tester ces analogies. Essayez vos propres combinaisons.

![bg right:55% contain](assets/infographics/word-arithmetic-parallelogram.png)

<small>Sources : [1] [Mikolov et al. — Word2Vec, 2013](https://arxiv.org/abs/1301.3781)</small>

---

<!-- _class: img-right -->

# 10 — Multi-Modal Embeddings : texte + images

- Les modèles modernes (CLIP, SigLIP) embeddent texte **ET** images dans le même espace
- "A photo of a cat" (texte) est proche d'une vraie photo de chat (image)
- Applications : Google Images, recherche produit, modération de contenu [1]

> Le notebook montre comment texte et images se retrouvent dans le même espace vectoriel. C'est la base du Multimodal RAG.

![bg right:55% contain](assets/infographics/multimodal-embedding-space.png)

<small>Sources : [1] [OpenAI — CLIP](https://openai.com/research/clip)</small>

---

<!-- _class: compact-table -->

# 11 — Choisir son modèle d'Embedding

| Modèle | Éditeur | Dim. | Prix/M tokens | Multilingue | Note |
|---|---|---|---|---|---|
| **text-embedding-3-large** | OpenAI | 3 072 | $0,13 | Oui | Leader marché [1] |
| **Embed v4** | Cohere | 1 024 | $0,12 | Oui | Enterprise [2] |
| **jina-embeddings-v3** | Jina AI (Berlin) | 1 024 | $0,02 | Oui | EU-based, RGPD [3] |
| **BGE-M3** | BAAI | 1 024 | Gratuit (OSS) | Oui | Meilleur OSS |
| **Gemini Embedding** | Google | 3 072 | Gratuit (preview) | Oui | Leader MTEB 2025 [4] |

> Pour une startup française : Jina (Berlin, RGPD) ou BGE-M3 (gratuit) pour démarrer. OpenAI ou Gemini pour la performance.

<small>Sources : [1] [OpenAI](https://openai.com/api/pricing/) · [2] [Cohere](https://cohere.com/pricing) · [3] [Jina AI](https://jina.ai/embeddings/) · [4] [Google](https://developers.googleblog.com/)</small>

---

# 12 — Discussion : Embeddings et votre projet

> Votre startup construit un chatbot de support pour une compagnie d'assurance française. Il doit embedder des documents de police et des questions clients.

**Questions pour la classe** :

- Quel modèle d'embedding choisiriez-vous et pourquoi ? (multilingue ? coût ? résidence des données EU ?)
- Si "assurance vie" et "life insurance" doivent matcher, qu'est-ce que ça exige du modèle ?
- Combien de dimensions sont nécessaires pour votre cas d'usage ?

---

<!-- _class: section -->

# Le Pipeline RAG en détail

## De vos documents à la réponse

---

# 13 — Chunking : découper intelligemment vos documents

Le Chunking transforme un document de 50 pages en morceaux exploitables par le LLM :

| Stratégie | Principe | Quand l'utiliser |
|---|---|---|
| **Fixed-size** | Découper tous les N tokens (256–512) | Prototypage rapide, données homogènes |
| **Recursive** | Découper par paragraphes, puis phrases si trop long | Standard pour la plupart des cas |
| **Semantic** | Détecter les ruptures de sens via embeddings | Documents longs et variés |
| **Overlap** | Chevauchement de 10–20% entre chunks | Toujours — évite de couper une idée en deux |

> Un mauvais Chunking = un RAG inutile. **Astuce** : reformulez vos chunks en paires Q&A — si les utilisateurs posent des questions, les chunks doivent y ressembler [1][2].

<small>Sources : [1] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) · [2] [Jason Liu — Low-Hanging Fruit](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)</small>

---

# 14 — Vector Databases : stocker et chercher les vecteurs

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

# 15 — Hybrid Search : le meilleur des deux mondes

<div class="left">

**Mots-clés (BM25)** :
- Compare les **mots exacts** entre requête et documents
- Rapide (5–15ms), excellent pour les termes précis
- **Faiblesse** : ne comprend pas les synonymes

</div>
<div class="right">

**Sémantique (Embeddings)** :
- Compare le **sens** des textes via vecteurs
- Excellent pour les questions en langage naturel
- **Faiblesse** : peut manquer des termes exacts

</div>

> **Les deux combinés** (Hybrid Search) = **+15–30% de rappel** vs chaque méthode seule [1].

<small>Sources : [1] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)</small>

---

<!-- _class: compact -->

# 16 — BM25 n'est pas mort : la preuve par DeepMind

Google DeepMind a prouvé mathématiquement que les Dense Embeddings ont une **limite structurelle** [1] :

| Méthode | Recall@2 (LIMIT) |
|---|---|
| **BM25** (sparse) | **97,8%** |
| ColBERT (multi-vector) | 83,5% |
| E5-Mistral 7B (4 096 dim.) | 29,5% |
| Gemini Embed (3 072 dim.) | 1,6% |

- Le gap **97,8% vs 29,5%** n'est pas un problème d'entraînement — c'est une **impossibilité mathématique** liée à la compression en vecteurs denses
- Plus d'entraînement ou plus de dimensions ne comblera pas le fossé
- Confirmé en pratique : l'agent Augment a atteint le **top du SWE-Bench** avec grep seul, sans embeddings [2]

> Le Hybrid Search n'est pas "nice to have" — c'est une **nécessité architecturale** prouvée.

<small>Sources : [1] [Google DeepMind — ICLR 2026](https://arxiv.org/html/2508.21038v1) · [2] [Augment — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-grep-beat-embeddings-in-our-swe-bench-agent-lessons-from-augment/)</small>

---

# 17 — RAG en pratique : chatbot RH

**Question utilisateur** : "Y a-t-il un parking pour les employés ?"

**Étape 1** — Le système cherche dans les documents RH → trouve le document "Facilities"

**Étape 2** — Le prompt envoyé au LLM devient :
```
Contexte : Politique parking — Tous les employés peuvent se
garer aux niveaux 1 et 2. Entrée par la rue Front [...]

Question : Y a-t-il un parking pour les employés ?
```

**Étape 3** — Le LLM répond en citant le document, avec un lien vers la source.

> Le RAG ajoute de la **traçabilité** : l'utilisateur peut vérifier la source. Avantage décisif en contexte réglementé.

---

# 18 — Applications du RAG

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

<!-- _class: section -->

# RAG avancé

## Passer en production

---

<!-- _class: compact -->

# 19 — RAG avancé : Reranking et Contextual Retrieval

Le RAG basique récupère les top-K par similarité. En production, deux techniques changent la donne :

**Reranking** — Un Cross-Encoder re-score les résultats après la recherche initiale :
- Gain : **+20–35% de précision** pour 50–500ms de latence [1]
- Outils : Cohere Rerank, Jina Reranker, BGE-Reranker (OSS)

**Contextual Retrieval** (Anthropic) — Résumé de contexte ajouté à chaque chunk avant embedding :
- Le LLM génère "Ce chunk parle de la politique parking" → embedé avec le chunk
- Résultat : **67% de réduction** des échecs de retrieval vs RAG naïf [2]

> Techniques complémentaires, déployables en quelques heures. Meilleur ratio effort/qualité après le pipeline de base.

<small>Sources : [1] [Données agrégées — recherche interne](docs/courses/sorbonne-m2/research/rag-ecosystem/report.md) · [2] [Anthropic — Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)</small>

---

<!-- _class: cols -->

# 20 — RAG : les patterns de production

<div class="left">

- **Agentic RAG** — l'agent **choisit** son outil (grep, embeddings, web) et itère [2]
- **Self-RAG** — le LLM juge si sa réponse a besoin de plus de contexte
- **Corrective RAG** — vérifie les documents avant génération

</div>
<div class="right">

- Chunking adapté au type de contenu
- Hybrid Search (BM25 + dense) + Reranker
- Évaluation sur dataset réel (Ragas, TruLens)
- Monitoring des taux de retrieval

</div>

> Les meilleurs systèmes combinent Hybrid Search + Reranking + boucle agentique → **>90% de pertinence** [1].

<small>Sources : [1] [Données agrégées — recherche interne](docs/courses/sorbonne-m2/research/rag-ecosystem/report.md) · [2] [Sourcegraph/Amp — via jxnl.co](https://jxnl.co/writing/2025/09/11/rethinking-rag-architecture-for-the-age-of-agents/)</small>

---

<!-- _class: cols -->

# 21 — RAG vs Fine-tuning : comment choisir ?

<div class="left">

| Critère | RAG | Fine-tuning |
|---|---|---|
| **Données fraîches** | Temps réel | Statique |
| **Coût initial** | ~$70–1K/mois | $5–50/run |
| **Traçabilité** | Sources citables | Boîte noire |

</div>
<div class="right">

- **RAG** pour les données qui changent, quand la traçabilité compte
- **Fine-tuning** pour le style et les hauts volumes
- **Les deux combinés** : +10–20% d'accuracy [1]

> Le bon choix dépend du volume, de la fraîcheur et du budget — pas de la hype.

</div>

<small>Sources : [1] [RAFT — UC Berkeley](https://arxiv.org/abs/2403.10131)</small>

---

# 22 — Long Context vs RAG : le faux débat

Les LLMs ont maintenant des fenêtres de contexte de **1M+ tokens** — le RAG est-il mort ?

- **Non** : le RAG est **8–82x moins cher** que le Context Stuffing pour les mêmes résultats [1]
- Le RAG fournit de la **traçabilité** (citation des sources), pas le Long Context
- Pour des bases < 200K tokens (~500 pages) : skip le RAG, utilisez le Prompt Caching [2]
- Pour tout le reste : le RAG reste le standard

> Le Long Context est un outil complémentaire, pas un remplacement. Le RAG gagne sur le coût et la traçabilité.

<small>Sources : [1] [Li et al. — Long Context vs RAG](https://arxiv.org/abs/2407.16833) · [2] [Anthropic — Prompt Caching](https://www.anthropic.com/news/prompt-caching)</small>

---

<!-- _class: section -->

# Améliorer son RAG

## Les leçons du terrain (Jason Liu)

---

<!-- _class: compact-table -->

# 23 — RAG Maturity : 5 niveaux

La plupart des équipes sautent au niveau 4 et se demandent pourquoi rien ne fonctionne [1] :

| Niveau | Focus | Ce que vous faites |
|---|---|---|
| **1 — Basics** | Pipeline fonctionnel | Chunking, embedding, retrieval, génération |
| **2 — Structured** | Query Understanding | Le LLM reformule la question, un reranker améliore les résultats |
| **3 — Observability** | Logger et monitorer | Cosine scores, reranker scores, segmentation par type de query |
| **4 — Evaluations** | Mesurer systématiquement | Synthetic data → precision/recall, LLM-as-judge |
| **5 — Understanding** | Comprendre les limites | Clusters de topics vs clusters de capacités |

> **Maîtrisez chaque niveau avant de monter.** La plupart des problèmes viennent du niveau 3 (observability), pas du niveau 4 (evals) [1].

<small>Sources : [1] [Jason Liu — Levels of RAG](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/)</small>

---

<!-- _class: compact-table -->

# 24 — Quick Wins : 7 améliorations à fort impact

Optimisations rapides qui n'exigent pas de refonte architecturale [1] :

| Quick Win | Pourquoi ça marche |
|---|---|
| **Baseline synthétique** | Générer des questions à partir de vos chunks → mesurer precision/recall |
| **Date filters** | "Le plus récent" est une date, pas un concept sémantique — filtrez |
| **Feedback précis** | "Avons-nous répondu ?" et non "Aimez-vous la réponse ?" |
| **Logger les scores** | Cosine + reranker score par requête → identifier les faiblesses |
| **Hybrid Search** | BM25 + dense embeddings — toujours |
| **Chunks → questions** | Reformuler les chunks en paires Q&A avant embedding |
| **Metadata dans chunks** | Ajouter auteur, date, chemin, tags au texte du chunk |

> "On ne peut pas améliorer ce qu'on ne mesure pas." — Commencez par la baseline synthétique [1].

<small>Sources : [1] [Jason Liu — Low-Hanging Fruit](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)</small>

---

<!-- _class: compact -->

# 25 — Les anti-patterns du RAG : échecs réels

Des systèmes RAG en production qui ont échoué — avec des chiffres [1] :

| Anti-pattern | Impact réel |
|---|---|
| **Encoding silencieux** | Chatbot médical : **21% du corpus perdu** (Latin-1 vs UTF-8) — aucune erreur |
| **Chunking excessif** | Fiches produit en 200 caractères → **13% d'hallucination** |
| **Complexité prématurée** | **>90%** des systèmes complexes performent **pire** qu'une baseline évaluée |
| **Requêtes hors-sujet** | Outil de comparaison produit qui répond "Écris un poème sur les licornes" |

**Vérification anti-hallucination en 3 étapes** :
1. Forcer des **citations inline** pour chaque affirmation
2. Vérifier que les documents cités **existent** dans les résultats
3. Valider sémantiquement que les citations **supportent** les affirmations

<small>Sources : [1] [Jason Liu & Skylar Payne — RAG Anti-Patterns](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/)</small>

---

<!-- _class: compact-table -->

# 26 — Les 6 évaluations du RAG

Tout système RAG a 3 variables : **Question (Q)**, **Contexte (C)**, **Réponse (A)**. Il n'existe que 6 évals possibles [1] :

| Eval | Notation | Ce qu'elle mesure |
|---|---|---|
| **Context Relevance** | C\|Q | Les chunks récupérés répondent-ils à la question ? |
| **Faithfulness** | A\|C | La réponse se limite-t-elle au contexte ? (hallucination) |
| **Answer Relevance** | A\|Q | La réponse répond-elle directement à la question ? |
| **Context Coverage** | C\|A | Le contexte contient-il tout ce que la réponse affirme ? |
| **Answerability** | Q\|C | La question est-elle répondable avec ce contexte ? |
| **Self-Containment** | Q\|A | La réponse est-elle autonome et complète ? |

> **Priorité selon le domaine** : médical → Faithfulness. Support client → Answer Relevance. Documentation → Answerability [1].

<small>Sources : [1] [Jason Liu — The Only 6 RAG Evals](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/)</small>

---

# 27 — Le RAG Flywheel : amélioration continue

Un RAG n'est **jamais terminé** — c'est une boucle d'amélioration continue [1] :

**Implémentation → Synthetic Data → Évaluation → Données réelles → Classification → Amélioration → Monitoring → Feedback → Itération**

**Leading vs Lagging Metrics** — l'insight clé :
- **Lagging** (résultat) : satisfaction globale — comme se peser
- **Leading** (action) : expériences/semaine, precision/recall — comme compter ses séances

> "C'est comme la perte de poids. Se peser ne fait pas maigrir. Compter ses entraînements prédit le résultat et donne des actions concrètes." [1]

<small>Sources : [1] [Jason Liu — The RAG Flywheel](https://jxnl.co/writing/2024/08/19/rag-flywheel/)</small>

---

<!-- _class: cols -->

# 28 — Le futur : du Q&A au rapport structuré

<div class="left">

**RAG Q&A** (aujourd'hui) :
- 1 question → 1 réponse
- Valeur = temps économisé
- ROI : "on remplace 8 analystes à $50/h"
- Échelle linéaire

</div>
<div class="right">

**RAG Report** (demain) :
- Données → rapport structuré (SOP)
- Valeur = meilleures décisions
- ROI : "rapport $20K → budget $5M"
- Templates réutilisables à l'échelle

</div>

> **Le template est la propriété intellectuelle.** Le RAG n'est que le moteur — la valeur est dans le format de sortie qui guide les décisions [1].

<small>Sources : [1] [Jason Liu — Future of RAG](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/)</small>

---

# 29 — Quand le RAG n'est pas la réponse

Le RAG est puissant, mais ce n'est **pas toujours le bon outil** :

| Situation | Pourquoi pas le RAG | Alternative |
|---|---|---|
| **Données structurées** (code, SQL) | La structure logique bat la similarité sémantique | grep, SQL, navigation de fichiers [1] |
| **Petits corpus** (< 500 pages) | Long Context + Prompt Caching est plus simple | Context Stuffing + cache [2] |
| **Workflow agentique** | L'agent explore par lui-même (read, search, iterate) | Outils de navigation directe [3] |

> **La Bitter Lesson** (Sutton) : à mesure que les modèles progressent, les couches d'infrastructure complexes deviennent superflues. Ce qui nécessite le RAG aujourd'hui sera peut-être résolu par un simple grep demain [3].

<small>Sources : [1] [Augment — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-grep-beat-embeddings-in-our-swe-bench-agent-lessons-from-augment/) · [2] [Anthropic — Prompt Caching](https://www.anthropic.com/news/prompt-caching) · [3] [Cline — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-i-stopped-using-rag-for-coding-agents-and-you-should-too/)</small>

---

<!-- _class: section -->

# Synthèse

## Ce qu'il faut retenir

---

# 30 — Key Takeaways

1. **Le RAG est le standard** — **86%** d'adoption, premier investissement après le Prompting

2. **Hybrid Search = non négociable** — BM25 + Dense, prouvé par DeepMind (97,8% vs 29,5%)

3. **Votre avantage = vos données + votre pipeline** — le modèle est accessible à tous

4. **5 niveaux de maturité** — observability avant evaluations, mesurer avant d'optimiser

5. **Le RAG Flywheel** — amélioration continue, Leading Metrics > Lagging Metrics

6. **Du Q&A au rapport** — le futur du RAG est la génération structurée, pas le chatbot

---

# 31 — Pour la suite

**Hands-on** :
- Le notebook Jupyter sur les Embeddings (2D, PCA, Cosine Similarity, Word Arithmetic, Multi-Modal)
- Testez un outil de RAG gratuit : uploadez un PDF sur **ChatPDF** ou **Claude**

**Pour votre projet** :
- Identifiez la source de données qui donnerait le plus de valeur en RAG
- Avez-vous besoin de Prompting seul, de RAG, ou d'agents ?

**Prochaine séance : Le business de l'IA**
- L'écosystème IA (qui fait quoi, la chaîne de valeur)
- Business Models & cas réels (Klarna, Mistral AI, L'Oréal)
