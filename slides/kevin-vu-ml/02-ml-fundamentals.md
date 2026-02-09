---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Adapté du cours de Kevin Vu · Paris Dauphine PSL"
---
<!-- ABOUTME: Fundamental ML concepts: iterative process, classification/regression KPIs, optimization, and data preparation. -->
<!-- ABOUTME: Business-framed for non-engineer M2 students — focuses on evaluating AI product performance. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Cours 2 — Notions Fondamentales

M2 Entrepreneuriat · Sorbonne · 2026

---

# Sommaire

1. Le processus ML — un cycle itératif
2. Classification — KPIs
3. Régression — KPIs
4. Fonctions de perte & Optimisation
5. Data Preparation
6. Curse of Dimensionality

> **Fil conducteur** : comment savoir si votre produit IA fonctionne vraiment ? Les métriques sont le langage commun entre technique et business.

---

<!-- _class: section -->

# Le processus ML

## The ML Process — An Iterative Cycle

---

<!-- _class: cols -->

# 01 — Le Machine Learning est un processus itératif

<div class="left">

### Les trois étapes du cycle

1. **Data Preparation** — nettoyer et structurer les données
2. **Algorithme prédictif** — entraîner un modèle sur ces données
3. **Revue de performance** — mesurer les résultats avec des KPIs

Le cycle recommence après la revue : on ajuste les données, change l'algorithme ou ses paramètres, puis on réévalue.

> **Pour un entrepreneur** : un projet ML n'est jamais "fini" au premier essai. Budgetez des itérations, pas un livrable unique.

</div>
<div class="right">

*#TODO ADD IMAGE — schéma cyclique montrant les 3 étapes : Data Preparation, Algorithme, Revue de performance avec des flèches de retour*

</div>

---

# 02 — Pourquoi les métriques comptent pour le business

- Un modèle ML produit des prédictions — mais sont-elles **assez bonnes** ?
- Les KPIs permettent de :
  - **Communiquer** la performance aux investisseurs et clients
  - **Comparer** différentes solutions (build vs. buy)
  - **Fixer des seuils** d'acceptabilité avant mise en production
- **Unsupervised Learning** : les KPIs mesurent la qualité de l'algorithme (rarement liés au produit final)
- **Supervised Learning** : KPIs standardisés selon le type de problème

> **Question pour la classe** : vous achetez un outil de détection de fraude. Le vendeur annonce "95% de précision". Est-ce suffisant pour prendre une décision ?

---

<!-- _class: section -->

# Classification — KPIs

## Evaluating Binary & Multiclass Classifiers

---

<!-- _class: cols -->

# 03 — La Confusion Matrix : le tableau de bord de votre IA

<div class="left">

### Cas binaire (oui / non)

Un modèle de Classification binaire peut se tromper de **deux manières** :

|  | Prédit Positif | Prédit Négatif |
|---|---|---|
| **Réel Positif** | True Positive (TP) | False Negative (FN) |
| **Réel Négatif** | False Positive (FP) | True Negative (TN) |

**Exemples business** : conversion client, détection de fraude, rétention, diagnostic médical.

</div>
<div class="right">

*#TODO ADD IMAGE — confusion matrix 2x2 avec TP, FP, FN, TN colorés*

> **Question pour la classe** : vous développez un chatbot qui filtre les demandes urgentes des clients. Quelle erreur est la plus grave : ignorer une urgence (FN) ou traiter un message normal comme urgent (FP) ?

</div>

---

# 04 — Precision, Recall, F1-Score

### Les KPIs clés en Classification

| Métrique | Formule | Question business |
|---|---|---|
| **Accuracy** | (TP + TN) / Total | Quel % de prédictions sont correctes ? |
| **Precision** | TP / (TP + FP) | Parmi mes alertes, combien sont vraies ? |
| **Recall** (Sensitivity) | TP / (TP + FN) | Parmi les vrais cas, combien ai-je détectés ? |
| **F1-Score** | 2 × (Precision × Recall) / (Precision + Recall) | Compromis entre Precision et Recall |

> **Règle d'or** : l'Accuracy seule est trompeuse. Si 99% de vos transactions sont légitimes, un modèle qui dit toujours "légitime" a 99% d'Accuracy mais 0% de Recall sur la fraude.

---

# 05 — Erreur de Type I vs. Erreur de Type II

### Deux façons de se tromper

- **Type I (False Positive)** — fausse alerte
  - Ex : bloquer une transaction légitime, envoyer un email en spam par erreur
  - Coût : frustration client, perte de revenu
- **Type II (False Negative)** — cas manqué
  - Ex : laisser passer une fraude, ne pas détecter une maladie
  - Coût : perte financière, risque vital

*#TODO ADD IMAGE — illustration humoristique Type I vs Type II (ex: alarme incendie)*

> **Pour un entrepreneur** : le choix entre minimiser les FP ou les FN est une **décision business**, pas technique. C'est vous qui définissez ce qui coûte le plus cher.

---

<!-- _class: cols -->

# 06 — Le Decision Threshold

<div class="left">

### Comment un modèle "décide" ?

- Un modèle de Classification ne prédit pas directement "oui" ou "non"
- Il calcule une **probabilité** (entre 0 et 1)
- Le **Decision Threshold** (seuil) transforme cette probabilité en décision
  - Seuil = 0.5 → standard
  - Seuil = 0.3 → plus sensible (plus de Recall, moins de Precision)
  - Seuil = 0.8 → plus strict (plus de Precision, moins de Recall)

</div>
<div class="right">

*#TODO ADD IMAGE — distribution des scores avec un seuil de décision déplaçable, montrant les zones TP/FP/FN/TN*

> **Exemple** : votre startup de crédit en ligne. Un seuil bas approuve plus de clients (+ revenu) mais augmente le risque de défaut. Un seuil haut est prudent mais rejette des bons clients.

</div>

---

<!-- _class: cols -->

# 07 — La ROC Curve et l'AUC

<div class="left">

### Évaluer et comparer des modèles

- La **ROC Curve** trace le Recall (True Positive Rate) en fonction du False Positive Rate pour chaque seuil possible
- L'**AUC** (Area Under the Curve) résume la performance en un seul chiffre (de 0 à 1)
  - AUC = 0.5 → modèle aléatoire (inutile)
  - AUC = 0.8 → bon modèle
  - AUC = 1.0 → modèle parfait (suspect en pratique)

</div>
<div class="right">

*#TODO ADD IMAGE — courbe ROC avec diagonale (modèle aléatoire) et une courbe au-dessus (bon modèle), zone AUC colorée*

> **Pour un entrepreneur** : l'AUC permet de comparer deux prestataires d'IA sur un même jeu de données. C'est votre outil de benchmark.

</div>

---

# 08 — ROC / AUC — Quizz

### Testez votre compréhension

*#TODO ADD IMAGE — deux courbes ROC qui se croisent, modèle A et modèle B*

**Questions** :
- Quel modèle choisiriez-vous si vous voulez minimiser les fausses alertes ?
- Quel est l'AUC d'un modèle qui prédit toujours la même classe ?
- Si les deux courbes se croisent, comment décider ? (indice : cela dépend du seuil de décision que vous visez)

> **Réponse AUC constant** : un modèle qui prédit toujours la même classe a un AUC de **0.5** — il ne fait pas mieux que le hasard.

---

<!-- _class: cols -->

# 09 — Extension multiclasse

<div class="left">

### Au-delà du binaire

- Quand il y a plus de 2 classes (ex : catégoriser des tickets support en "technique", "facturation", "commercial")
- La Confusion Matrix devient **N × N**
- On calcule Precision et Recall **par classe**, puis on agrège :
  - **Macro-average** : moyenne simple (chaque classe compte pareil)
  - **Weighted average** : pondéré par le nombre d'exemples

</div>
<div class="right">

*#TODO ADD IMAGE — confusion matrix 3x3 ou 4x4 multiclasse avec couleurs*

> **Pour un entrepreneur** : si une classe rare est critique pour votre business (ex : détection de pannes), vérifiez les métriques **par classe**, pas seulement la moyenne globale.

</div>

---

<!-- _class: section -->

# Régression — KPIs

## Measuring Continuous Predictions

---

<!-- _class: cols -->

# 10 — Métriques de Régression

<div class="left">

### Quand la prédiction est un nombre

- **Régression** = prédire une valeur continue (prix, durée, quantité)
- On mesure l'**écart** entre la prédiction et la réalité

| Métrique | Ce qu'elle mesure |
|---|---|
| **MAE** (Mean Absolute Error) | Erreur moyenne en valeur absolue |
| **RMSE** (Root Mean Square Error) | Erreur moyenne, pénalise les gros écarts |
| **MAPE** (Mean Absolute % Error) | Erreur en %, facile à communiquer |
| **R²** (Coefficient de détermination) | % de variance expliquée par le modèle |

</div>
<div class="right">

*#TODO ADD IMAGE — graphique de régression avec points réels et droite de prédiction, écarts visualisés*

> **Exemple business** : votre outil prédit le chiffre d'affaires mensuel d'un restaurant. Une MAPE de 10% signifie que vos prédictions se trompent en moyenne de 10%. Est-ce acceptable pour votre client ?

</div>

---

# 11 — Intervalles de confiance

### Ne pas se fier à un seul chiffre

- Une prédiction ponctuelle ne suffit pas — il faut aussi mesurer l'**incertitude**
- L'**intervalle de confiance** donne une fourchette : "le prix sera entre 180k et 220k avec 95% de certitude"
- Plus l'intervalle est large, moins le modèle est sûr de lui

*#TODO ADD IMAGE — graphique de prédiction avec bandes de confiance (intervalle qui s'élargit)*

> **Pour un entrepreneur** : quand vous présentez des prédictions à un investisseur ou un client, montrez toujours l'intervalle de confiance. Un chiffre seul est une fausse promesse.

**Question pour la classe** : votre startup prédit les délais de livraison. Vaut-il mieux annoncer "3 jours" (souvent faux) ou "2 à 5 jours" (toujours vrai) ?

---

<!-- _class: section -->

# Fonctions de perte & Optimisation

## Loss Functions & Gradient Descent

---

# 12 — Comment un modèle apprend : la Loss Function

- Chaque modèle ML a une **Loss Function** (fonction de perte) qui mesure ses erreurs
- L'objectif de l'entraînement : **minimiser cette fonction**
- Exemples de Loss Functions :
  - **Classification** : Cross-Entropy Loss, Log Loss
  - **Régression** : Mean Squared Error (MSE), Mean Absolute Error (MAE)

> La Loss Function est le "GPS" du modèle : elle lui dit à quel point il est loin de la bonne réponse et dans quelle direction corriger.

---

<!-- _class: cols -->

# 13 — Gradient Descent : l'algorithme d'optimisation

<div class="left">

### Le principe

- Imaginez descendre une montagne dans le brouillard
- À chaque pas, vous allez dans la direction de la pente la plus forte
- C'est exactement ce que fait le **Gradient Descent** :
  1. Calculer l'erreur actuelle
  2. Calculer la direction de la pente (le **gradient**)
  3. Faire un pas dans cette direction
  4. Répéter jusqu'à atteindre un minimum

</div>
<div class="right">

*#TODO ADD IMAGE — surface 3D avec un point qui descend vers le minimum, flèches de gradient*

> **Paramètre clé** : le **Learning Rate** contrôle la taille du pas. Trop grand → on saute par-dessus le minimum. Trop petit → l'entraînement prend une éternité.

</div>

---

<!-- _class: cols -->

# 14 — Standardisation des données

<div class="left">

### Pourquoi normaliser les inputs ?

- Les variables ont des échelles très différentes (âge : 0–100, revenu : 0–1M)
- Sans standardisation, le Gradient Descent converge mal :
  - La surface d'erreur est **allongée** → zigzags
  - Avec standardisation → surface **circulaire** → convergence directe
- **Standardisation** : centrer (moyenne = 0) et réduire (écart-type = 1)

</div>
<div class="right">

*#TODO ADD IMAGE — comparaison de contours d'erreur : ellipsoïdes allongés (sans normalisation) vs cercles (avec normalisation)*

> **Pour un entrepreneur** : la Data Preparation (dont la standardisation) consomme souvent **60 à 80% du temps** d'un projet ML. Prévoyez-le dans vos budgets et plannings.

</div>

---

<!-- _class: section -->

# Data Preparation

## Preparing Data for Machine Learning

---

# 15 — Les étapes clés de la Data Preparation

### Le travail invisible qui fait la différence

1. **Collecte** — identifier et rassembler les sources de données
2. **Nettoyage** — traiter les valeurs manquantes, doublons, erreurs
3. **Feature Engineering** — créer de nouvelles variables pertinentes
4. **Encoding** — convertir les variables catégorielles en nombres
5. **Standardisation / Normalisation** — mettre les variables à la même échelle
6. **Train / Test Split** — séparer les données d'entraînement et de test

> **Règle d'or** : "Garbage in, garbage out." Le meilleur algorithme du monde ne peut rien faire avec des données de mauvaise qualité.

---

# 16 — Train / Test Split : éviter l'illusion de performance

- On ne peut pas évaluer un modèle sur les données qu'il a déjà vues
- **Train set** (~70-80%) : pour entraîner le modèle
- **Test set** (~20-30%) : pour évaluer la performance réelle
- Variante avancée : **Cross-Validation** (découper en K parties, tourner)

> **Analogie** : évaluer un étudiant sur les questions qu'il a déjà révisées ne teste pas sa compréhension. Le test set, c'est l'examen final avec des questions inédites.

**Question pour la classe** : un prestataire vous montre des résultats impressionnants mais refuse de tester sur vos propres données. Que faut-il en penser ?

---

<!-- _class: section -->

# Problématiques

## Common Pitfalls in Machine Learning

---

<!-- _class: cols -->

# 17 — Overfitting vs. Underfitting

<div class="left">

### Le piège le plus courant

- **Overfitting** : le modèle apprend par coeur les données d'entraînement
  - Excellente performance sur le Train set
  - Mauvaise performance sur le Test set
  - Comme un étudiant qui mémorise les réponses sans comprendre
- **Underfitting** : le modèle est trop simple
  - Mauvaise performance partout
  - Le modèle ne capture pas les patterns

</div>
<div class="right">

### Comment détecter ?

| Situation | Train | Test |
|---|---|---|
| Underfitting | Mauvais | Mauvais |
| Bon modèle | Bon | Bon |
| Overfitting | Excellent | Mauvais |

> **Pour un entrepreneur** : si un prestataire annonce 99.9% de performance, demandez **toujours** les résultats sur le Test set. L'Overfitting est la source n°1 de déceptions en production.

</div>

---

<!-- _class: cols -->

# 18 — Curse of Dimensionality

<div class="left">

### Plus de données, plus de problèmes ?

- Plus on a de **variables** (dimensions), plus il faut de données pour que le modèle fonctionne
- Avec peu de données et beaucoup de variables :
  - L'espace est trop vaste → les points sont tous "loin" les uns des autres
  - Le modèle ne peut pas trouver de patterns fiables
  - Risque accru d'Overfitting

</div>
<div class="right">

*#TODO ADD IMAGE — visualisation de la curse of dimensionality : données denses en 1D, éparses en 2D, très éparses en 3D*

> **Pour un entrepreneur** : collecter 200 variables sur vos clients ne sert à rien si vous n'avez que 500 observations. Mieux vaut 10 variables bien choisies que 200 variables bruitées.

**Question pour la classe** : votre équipe data vous propose d'ajouter 50 nouvelles features au modèle. Quelles questions posez-vous avant de valider ?

</div>

---

<!-- _class: section -->

# Récapitulatif

## Session 2 Summary

---

# 19 — Ce qu'il faut retenir

- **Le ML est itératif** : Data Preparation → Modèle → Évaluation → Itération
- **Confusion Matrix** : le tableau de bord pour comprendre les erreurs de Classification
- **Precision vs. Recall** : un choix business, pas seulement technique
- **ROC / AUC** : l'outil pour comparer des modèles et des prestataires
- **Métriques de Régression** (MAE, RMSE, MAPE) : communiquer l'erreur en termes compréhensibles
- **Gradient Descent** : le moteur d'apprentissage de la plupart des algorithmes
- **Data Preparation** : 60-80% du travail réel d'un projet ML
- **Overfitting** : la question à poser systématiquement à tout prestataire IA

> **Pour la prochaine séance** : trouvez un cas concret dans votre projet entrepreneurial où vous auriez besoin de prédire quelque chose. Identifiez s'il s'agit de Classification ou de Régression.
