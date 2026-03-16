---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: Embeddings — intuition, mécanique (PCA, cosine similarity, clusters, word arithmetic) et applications (multimodal, choix de modèle). -->
<!-- ABOUTME: Session 3A pour étudiants M2 IMT&E Paris 1 : comprendre les représentations vectorielles qui fondent la recherche sémantique. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Embeddings — Le GPS du sens

## Session 3A — Comprendre les représentations vectorielles

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Intuition

## Coordonnées dans l'espace du sens

---

<!-- _class: img-right -->

# 01 — Intuition : les mots comme coordonnées

- Un **Embedding** transforme du texte en **coordonnées** dans un espace mathématique
- Analogie : un **GPS pour le sens** — textes proches en sens = coordonnées proches
- "Chat mignon" et "Chaton adorable" → coordonnées voisines
- "Chat mignon" et "Réfrigérateur" → coordonnées éloignées
- C'est ainsi que le RAG "sait" quels documents sont pertinents

> L'embedding encode le **sens**, pas les mots exacts. C'est la brique fondamentale de toute recherche sémantique.

![bg right:55% contain](assets/infographics/embeddings-2d-vectors.png)

---

<!-- _class: img-right -->

# 02 — Des vecteurs 2D aux vrais Embeddings

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

<!-- _class: section -->

# La mécanique

## Mesurer, visualiser, calculer

---

<!-- _class: img-right -->

# 03 — PCA : voir l'invisible

- **Problème** : on ne peut pas visualiser 768 dimensions
- **PCA** compresse les dimensions en préservant la structure la plus importante
- Analogie : photographier un bâtiment 3D → on perd la profondeur mais on garde la forme
- Le notebook projette 768 dimensions sur 2D avec PCA

> C'est ainsi que sont produites toutes les "visualisations de clusters" dans les publications IA.

![bg right:55% contain](assets/infographics/pca-projection.png)

---

<!-- _class: img-right -->

# 04 — Cosine Similarity : mesurer la pertinence

- Comment le système sait quels documents sont "pertinents" ?
- La **Cosine Similarity** mesure l'**angle** entre deux vecteurs
- Score **+1** = sens identique · **0** = aucun rapport · **−1** = sens opposé
- C'est la métrique au cœur de tout moteur de recherche sémantique

> C'est aussi un *choix business* : la Cosine Similarity définit ce que "pertinent" signifie pour votre produit.

![bg right:55% contain](assets/infographics/cosine-similarity-angles.png)

---

<!-- _class: img-right -->

# 05 — Les clusters sémantiques

- Quand on embed beaucoup de mots, ils forment **naturellement** des clusters par sens
- Animaux ensemble, couleurs ensemble, professions ensemble
- Ce n'est pas programmé — ça **émerge** des données d'entraînement
- Le modèle a appris une "carte du savoir humain"

> Dans votre RAG : les documents sur des sujets similaires se regroupent dans la base vectorielle. La qualité de ces clusters = la qualité de votre retrieval.

![bg right:55% contain](assets/infographics/semantic-clusters.png)

---

<!-- _class: img-right -->

# 06 — Word Arithmetic : Roi − Homme + Femme ≈ Reine

- La propriété la plus surprenante : on peut **faire des maths avec le sens**
- King − Man + Woman ≈ Queen
- Paris − France + Japan ≈ Tokyo
- Les embeddings encodent des **relations**, pas juste de la similarité [1]

> Le notebook vous permet de tester ces analogies. Essayez vos propres combinaisons.

![bg right:55% contain](assets/infographics/word-arithmetic-parallelogram.png)

<small>Sources : [1] [Mikolov et al. — Word2Vec, 2013](https://arxiv.org/abs/1301.3781)</small>

---

<!-- _class: section -->

# Applications

## Du modèle au produit

---

<!-- _class: img-right -->

# 07 — Multi-Modal Embeddings : texte + images

- Les modèles modernes (CLIP, SigLIP) embeddent texte **ET** images dans le même espace
- "A photo of a cat" (texte) est proche d'une vraie photo de chat (image)
- Applications : Google Images, recherche produit, modération de contenu [1]

> Le notebook montre comment texte et images se retrouvent dans le même espace vectoriel. C'est la base du Multimodal RAG.

![bg right:55% contain](assets/infographics/multimodal-embedding-space.png)

<small>Sources : [1] [OpenAI — CLIP](https://openai.com/research/clip)</small>

---

<!-- _class: compact-table -->

# 08 — Choisir son modèle d'Embedding

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

# 09 — Discussion : Embeddings et votre projet

> Votre startup construit un chatbot de support pour une compagnie d'assurance française. Il doit embedder des documents de police et des questions clients.

**Questions pour la classe** :

- Quel modèle d'embedding choisiriez-vous et pourquoi ? (multilingue ? coût ? résidence des données EU ?)
- Si "assurance vie" et "life insurance" doivent matcher, qu'est-ce que ça exige du modèle ?
- Combien de dimensions sont nécessaires pour votre cas d'usage ?
