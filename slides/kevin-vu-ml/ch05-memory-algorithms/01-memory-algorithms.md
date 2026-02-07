---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Adapté du cours de Kevin Vu · Paris Dauphine PSL"
---
<!-- ABOUTME: Memory-based algorithms covering KNN, similarity measures, recommendation systems, Gaussian processes, and SVM. -->
<!-- ABOUTME: Business-focused presentation for non-engineers emphasizing recommendation systems as the key entrepreneurial topic. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Cours 5 — Algorithmes mémoriels

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Algorithmes mémoriels

## Memory-Based Algorithms

---

<!-- _class: cols -->

# 01 — Qu'est-ce qu'un algorithme mémoriel ?

<div class="left">

### Instance-Based Learning vs Model-Based Learning

- **Model-Based** : l'algorithme apprend des règles explicites pendant l'entraînement, puis les applique
- **Instance-Based** : l'algorithme **mémorise** les données et compare chaque nouveau cas aux exemples connus
- Pas de formule paramétrique : la prédiction est **locale**, basée sur les voisins les plus proches

> **Analogie business** : un Model-Based, c'est un process documenté. Un Instance-Based, c'est un expert senior qui dit « ça me rappelle un cas similaire ».

</div>
<div class="right">

*#TODO ADD IMAGE — schéma comparant instance-based learning (stockage de points) vs model-based learning (courbe apprise)*

</div>

---

# 02 — Avantages et inconvénients

| | Instance-Based | Model-Based |
|---|---|---|
| **Mise à jour** | Immédiate : on ajoute des données | Nécessite un ré-entraînement |
| **Interprétabilité** | Fournit des comparables concrets | Dépend du modèle |
| **Modularité** | Très flexible sur la métrique de similarité | Fixée à l'entraînement |
| **Performance** | Lent à grande échelle (calcul à chaque requête) | Rapide en inférence |
| **Généralisation** | Risque d'Overfitting sur le bruit | Meilleure généralisation |

> **Pour un entrepreneur** : les algorithmes mémoriels brillent quand vous avez besoin de résultats explicables (« voici 3 cas similaires ») ou quand vos données changent souvent.

---

<!-- _class: section -->

# Mesurer la similarité

## Similarity Measures

---

# 03 — La similarité, question centrale

Comment mesurer la proximité entre deux éléments ?

- **Fleurs** : comparer la taille des pétales, la couleur, la forme
- **Adresses** : comparer les coordonnées géographiques
- **Clients** : comparer leurs historiques d'achat
- **Films** : comparer les notes données par les utilisateurs
- **Mots** : comparer leur sens dans un espace vectoriel

> Le choix de la **métrique de similarité** détermine la qualité de tout algorithme mémoriel. C'est un choix stratégique, pas technique.

**Question pour la classe** : Si vous lancez une app de mode, comment mesureriez-vous la « similarité » entre deux vêtements ? Quels critères choisir ?

---

<!-- _class: cols -->

# 04 — Distance euclidienne vs Manhattan Distance

<div class="left">

### Euclidean Distance
- Distance « en ligne droite » entre deux points
- Efficace en faible dimension (2D, 3D)
- Formule : racine carrée de la somme des carrés des écarts

### Manhattan Distance
- Distance « en suivant les rues » (en grille)
- Plus robuste en grande dimension
- Formule : somme des valeurs absolues des écarts

</div>
<div class="right">

*#TODO ADD IMAGE — schéma comparant distance euclidienne (ligne droite) et Manhattan (chemin en grille) entre deux points*

> **Règle pratique** : quand vous avez beaucoup de variables (features), la Manhattan Distance est souvent plus fiable que l'euclidienne.

</div>

---

<!-- _class: cols -->

# 05 — Cosine Similarity

<div class="left">

### Mesurer l'angle, pas la distance

- Compare la **direction** de deux vecteurs, pas leur magnitude
- Valeur entre -1 (opposés) et +1 (identiques)
- Fondamental pour la comparaison de textes et de préférences

### Cas d'usage concrets
- **NLP** : comparer des mots ou documents (Word2Vec, Embeddings)
- **Recommendation** : comparer les profils d'achat de deux clients
- **Search** : classer les résultats par pertinence

</div>
<div class="right">

*#TODO ADD IMAGE — schéma montrant deux vecteurs et l'angle entre eux pour illustrer la Cosine Similarity*

> **Pourquoi c'est important** : la Cosine Similarity est la métrique utilisée par les moteurs de recherche sémantique et les systèmes de recommandation modernes (y compris les RAG des LLM).

</div>

---

# 06 — Quelle similarité choisir ?

| Métrique | Quand l'utiliser | Exemple business |
|---|---|---|
| **Euclidean** | Peu de variables, valeurs comparables | Comparer des biens immobiliers (surface, prix) |
| **Manhattan** | Beaucoup de variables, données hétérogènes | Scoring de leads dans un CRM |
| **Cosine Similarity** | Texte, préférences, vecteurs de grande dimension | Recommendation de produits, recherche sémantique |
| **Haversine** | Données géographiques (latitude/longitude) | Trouver les restaurants les plus proches |

> Le choix de la métrique est un **choix business** : il définit ce que « similaire » signifie pour votre produit.

---

<!-- _class: section -->

# KNN — K-Nearest Neighbors

## L'algorithme le plus intuitif

---

<!-- _class: cols -->

# 07 — Comment fonctionne KNN ?

<div class="left">

### Principe
1. Recevoir un nouveau point à classifier
2. Calculer la distance avec **tous** les points existants
3. Sélectionner les **K** voisins les plus proches
4. Vote majoritaire (classification) ou moyenne (régression)

### Le paramètre K
- **K petit** (ex. 1-3) : très sensible au bruit
- **K grand** (ex. 50+) : lisse trop, perd les détails
- Trouver le bon K = trouver le bon compromis

</div>
<div class="right">

*#TODO ADD IMAGE — visualisation KNN avec un point inconnu entouré de ses K plus proches voisins de différentes classes*

</div>

---

# 08 — KNN en pratique

| Avantage | Inconvénient |
|---|---|
| Extrêmement simple à implémenter | Lent sur de gros datasets (calcul exhaustif) |
| Aucun entraînement nécessaire | Nécessite de stocker toutes les données |
| Fonctionne pour classification et régression | Sensible aux variables non normalisées |
| Résultats interprétables (« voici vos voisins ») | Mauvais en grande dimension (curse of dimensionality) |

> **Cas réel** : de nombreux systèmes de détection de fraude utilisent KNN comme première couche — si une transaction ressemble à des transactions frauduleuses connues, elle est signalée.

**Question pour la classe** : Vous gérez une marketplace de freelances. Comment utiliseriez-vous KNN pour recommander des profils à un recruteur ?

---

<!-- _class: section -->

# Recommendation Systems

## Le coeur business des algorithmes mémoriels

---

# 09 — Les systèmes de recommandation, partout

Les Recommendation Systems sont l'application la plus visible du ML pour le grand public :

| Entreprise | Ce qui est recommandé | Impact business |
|---|---|---|
| **Netflix** | Films et séries | 80% du contenu visionné vient des recommandations |
| **Amazon** | Produits | 35% du chiffre d'affaires attribué aux recommandations |
| **Spotify** | Playlists (Discover Weekly) | Facteur clé de rétention utilisateur |
| **YouTube** | Vidéos suivantes | 70% du temps de visionnage est guidé par l'algorithme |

> **Pour un entrepreneur** : un bon système de recommandation transforme un catalogue passif en expérience personnalisée. C'est souvent le **moat** technologique d'une plateforme.

---

# 10 — Collaborative Filtering : l'approche mémorielle

### Principe fondamental
> « Les utilisateurs qui ont aimé les mêmes choses que vous aimeront probablement les mêmes nouvelles choses. »

**Deux variantes :**
- **User-Based** : trouver des utilisateurs similaires, recommander ce qu'ils ont aimé
- **Item-Based** : trouver des produits similaires à ceux déjà appréciés

### Fonctionnement concret
1. Construire une **matrice utilisateurs x produits** (notes ou achats)
2. Calculer la similarité entre lignes (users) ou colonnes (items)
3. Prédire les cases vides de la matrice

---

<!-- _class: cols -->

# 11 — User-Based vs Item-Based Filtering

<div class="left">

### User-Based
- Cherche des utilisateurs au profil similaire
- « Les gens comme vous ont aussi acheté... »
- Fonctionne bien avec peu de produits et beaucoup d'utilisateurs

### Item-Based
- Cherche des produits souvent appréciés ensemble
- « Les clients qui ont acheté X ont aussi acheté Y »
- Plus stable quand les goûts utilisateurs évoluent

</div>
<div class="right">

*#TODO ADD IMAGE — schéma d'une matrice utilisateurs-produits avec des notes, montrant les deux approches de filtrage*

> **Amazon** a popularisé l'Item-Based Filtering parce que les relations entre produits sont plus stables que les préférences volatiles des utilisateurs.

</div>

---

# 12 — Matrix Factorization : l'approche Model-Based

### Au-dela du Collaborative Filtering pur

- Décomposer la matrice utilisateurs-produits en **deux matrices plus petites**
- Chaque utilisateur et chaque produit sont représentés par un vecteur de **facteurs latents**
- Les facteurs capturent des dimensions cachées (ex : un film est « action + sombre + européen »)

| Approche | Type | Avantage | Inconvénient |
|---|---|---|---|
| **Collaborative Filtering** | Instance-Based | Simple, interprétable | Passage à l'échelle difficile |
| **Matrix Factorization** | Model-Based | Performant à grande échelle | Moins interprétable |

> **Netflix Prize** (2009) : l'équipe gagnante a utilisé un ensemble de méthodes dont la Matrix Factorization. Le prix : 1 million de dollars.

---

# 13 — Le probleme du Cold-Start

### Quand le système n'a pas assez de données

| Scénario | Probleme | Solutions courantes |
|---|---|---|
| **Nouvel utilisateur** | Aucun historique de préférences | Questionnaire initial, données démographiques |
| **Nouveau produit** | Aucune note, aucun achat | Content-Based Filtering (décrire le produit), mise en avant éditoriale |
| **Nouvelle plateforme** | Peu d'utilisateurs ET peu de produits | Données externes, partenariats, curation manuelle |

> **Spotify** résout le Cold-Start avec l'analyse audio : même sans écoutes, l'algorithme peut comparer le son d'un nouveau titre avec des titres populaires.

**Question pour la classe** : Vous lancez une plateforme de mise en relation B2B. Comment gérez-vous le Cold-Start quand vous avez 50 entreprises inscrites ?

---

<!-- _class: cols -->

# 14 — Content-Based vs Collaborative Filtering

<div class="left">

### Content-Based Filtering
- Recommande en analysant les **caractéristiques** du produit
- Ne dépend pas des autres utilisateurs
- Ex : recommander un film « action + Nolan » parce que vous avez aimé Inception

### Collaborative Filtering
- Recommande en analysant les **comportements** des utilisateurs
- Ne dépend pas des caractéristiques du produit
- Ex : recommander un documentaire parce que des profils similaires l'ont aimé

</div>
<div class="right">

### En pratique : les systemes hybrides

La plupart des plateformes combinent les deux approches :

| Phase | Approche |
|---|---|
| Lancement (Cold-Start) | Content-Based |
| Croissance | Collaborative Filtering |
| Maturité | Hybride + Deep Learning |

> **Netflix** utilise un systeme hybride combinant Content-Based, Collaborative Filtering et Deep Learning.

</div>

---

<!-- _class: section -->

# Gaussian Process & SVM

## Deux algorithmes pour la culture technique

---

<!-- _class: cols -->

# 15 — Gaussian Process

<div class="left">

### Principe
- Algorithme mémoriel de type « Lazy Evaluation »
- Très utilisé en **analyse géospatiale** (2D)
- Aussi connu sous le nom de **Krigeage**
- Prédit une valeur en un point en se basant sur les valeurs observées aux points voisins

### Cas d'usage
- Cartographie de la pollution atmosphérique
- Estimation de prix immobilier par zone
- Optimisation de paramètres (Bayesian Optimization)

</div>
<div class="right">

*#TODO ADD IMAGE — visualisation d'un Gaussian Process montrant une courbe de prédiction avec intervalle de confiance*

> **Pour un entrepreneur** : le Gaussian Process est la base de la **Bayesian Optimization**, utilisée par les plateformes d'A/B testing automatisé.

</div>

---

# 16 — SVM (Support Vector Machine)

### Un algorithme historique

- **Principe** : trouver l'hyperplan qui sépare le mieux deux classes, en maximisant la marge
- Utilise un **kernel trick** pour gérer les données non linéairement séparables
- Très populaire dans les années 2000, avant l'essor du Deep Learning

| Avantage | Inconvénient |
|---|---|
| Performant en grande dimension | Lent sur de très gros datasets |
| Bonne généralisation avec peu de données | Choix du kernel complexe |
| Solide base théorique | Largement supplanté par les réseaux de neurones |

> **En pratique** : SVM est rarement le premier choix en 2026. On le croise encore dans des niches (bioinformatique, détection d'anomalies sur petits datasets).

---

<!-- _class: section -->

# Récapitulatif

## Session 5 Summary

---

# 17 — Ce qu'il faut retenir

- **Instance-Based Learning** = mémoriser les données et comparer localement, sans modèle explicite
- **La similarité est un choix business** : Euclidean, Manhattan, Cosine Similarity selon le contexte
- **KNN** : simple, interprétable, mais ne passe pas à l'échelle
- **Recommendation Systems** : Collaborative Filtering + Content-Based + Matrix Factorization
- **Cold-Start** : le probleme numero 1 de toute nouvelle plateforme de recommandation
- **Gaussian Process et SVM** : utiles dans des niches, mais rarement le premier choix aujourd'hui

> **Pour la prochaine séance** : identifiez 3 recommandations que vous avez recues cette semaine (Netflix, Amazon, Spotify, LinkedIn...). Essayez de deviner si elles sont Content-Based ou Collaborative Filtering.
