---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Adapté du cours de Kevin Vu · Paris Dauphine PSL"
---
<!-- ABOUTME: Introduction to Machine Learning concepts adapted from Kevin Vu's Dauphine course. -->
<!-- ABOUTME: Covers definitions, history, classification types, and ethical debates for business students. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Cours 1 — Introduction au Machine Learning

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Objectifs & organisation

## Course Objectives & Structure

---

# 01 — Objectifs de cet enseignement

### Théorie
- Concepts fondamentaux du Machine Learning
- Compréhension des différents types d'algorithmes
- Vocabulaire technique pour dialoguer avec des équipes data

### Mise en pratique
- Identifier les cas d'usage pertinents pour un projet entrepreneurial
- Gestion globale d'un projet Machine Learning
- Développer un esprit critique face aux promesses de l'IA

> **Pour un entrepreneur** : comprendre le ML, c'est savoir évaluer un CTO, challenger un prestataire, et repérer les opportunités avant la concurrence.

---

# 02 — Organisation du cours

1. Introduction
2. Notions fondamentales
3. Algorithmes linéaires
4. Arbres de décision
5. Algorithmes mémoriels
6. Clustering
7. Réseaux de neurones
8. Reinforcement Learning
9. Graph Networks
10. Time Series
11. Cas pratiques
12. Conférences

---

# 03 — Pour aller plus loin

| Ressource | Description |
|---|---|
| **The Elements of Statistical Learning** | Ouvrage de référence, disponible gratuitement en ligne (Stanford) |
| **Machine Learning: A Probabilistic Perspective** | Ouvrage très complet, couvre des sujets avancés |
| **120 Questions ML** | Pour préparer les entretiens et vérifier ses connaissances |

> Ces ouvrages sont techniques — ils servent de référence, pas de lecture obligatoire.

---

<!-- _class: section -->

# Définitions & concepts

## Definitions & Key Concepts

---

<!-- _class: cols -->

# 04 — Machine Learning, Data Mining, Statistics

<div class="left">

### Trois termes, un même objectif ?

- **Statistics** : quantifier les données d'un échantillon, estimer le comportement d'une population
- **Machine Learning** : apprentissage à partir d'un jeu de données pour prédire ou estimer
- **Data Mining** : détection de patterns et de structures cachées dans les données

> En pratique, les frontières sont floues. Un entrepreneur n'a pas besoin de les distinguer — il doit comprendre ce que chaque approche peut **résoudre**.

</div>
<div class="right">

<!-- Image: Venn diagram ML vs Statistics vs Data Mining -->
<!-- [IMAGE MISSING: MvsSTATvsML.png] -->

![bg right:90%](assets/placeholder-venn-diagram.png)

</div>

---

<!-- _class: section -->

# Un peu de contexte historique

## A Brief History of AI

---

<!-- _class: cols -->

# 05 — 1769 : l'automate turc

<div class="left">

- **Conceptualisation** d'un automate capable de jouer aux échecs
- Premier débat : la machine peut-elle surpasser l'homme ?
- **Supercherie** : un joueur humain était caché à l'intérieur

> Dès le XVIIIe siècle, le décalage entre la promesse technologique et la réalité. Un thème toujours d'actualité dans le marketing IA.

</div>
<div class="right">

<!-- [IMAGE MISSING: auto_turc.png] -->

</div>

---

<!-- _class: cols -->

# 06 — 1936 : la machine de Turing

<div class="left">

- Formalisation abstraite du concept de calcul
- Un cadre numérique unique pour représenter différentes tâches à automatiser
- Fondation théorique de l'informatique moderne

> **Alan Turing** pose la question : « Une machine peut-elle penser ? » — le **Turing Test** reste une référence 90 ans plus tard.

</div>
<div class="right">

<!-- [IMAGE MISSING: turing.jpg] -->

</div>

---

<!-- _class: cols -->

# 07 — 1950–2020 : les réseaux de neurones

<div class="left">

- **1950s** : ambition de modéliser l'intelligence humaine, premières études en neurologie
- **1980s** : résultats révolutionnaires en reconnaissance d'images
- **1990s** : premières déceptions → **AI Winter**
- **2012+** : renaissance sous le nom **Deep Learning**
  - Puissance de calcul supérieure (GPU)
  - Données massives (Internet)
  - Modèles plus profonds → meilleures performances

> L'histoire de l'IA est cyclique : hype → déception → percée. Connaître ce cycle aide à évaluer les promesses actuelles.

</div>
<div class="right">

<!-- [IMAGE MISSING: lenet5.gif] -->

</div>

---

<!-- _class: section -->

# En pratique

## Machine Learning in Practice

---

<!-- _class: cols -->

# 08 — Une première classification

<div class="left">

### Supervised Learning
- Objectif défini à l'avance
- Nécessite un échantillon d'apprentissage étiqueté
- Ex : email → spam ? image → chat ou chien ?

### Unsupervised Learning
- Objectif générique : découvrir des structures
- Pas de labels nécessaires
- Ex : segmentation clients, détection d'anomalies

</div>
<div class="right">

### Quand utiliser quoi ?

| Critère | Supervised | Unsupervised |
|---|---|---|
| Données étiquetées ? | Oui | Non |
| Objectif précis ? | Oui | Exploratoire |
| Cas d'usage typique | Prédiction | Segmentation |

> **Question pour la classe** : Vous lancez une marketplace. Classeriez-vous la détection de faux avis comme du Supervised ou Unsupervised Learning ?

</div>

---

<!-- _class: cols -->

# 09 — Types d'input : données structurées vs non structurées

<div class="left">

### Données structurées
- Tableaux, bases de données, CSV
- Colonnes = variables, lignes = observations
- Ex : CRM, comptabilité, logs serveur

### Données non structurées
- Texte, images, audio, vidéo
- Pas de format tabulaire fixe
- Ex : emails clients, photos produit, appels SAV

</div>
<div class="right">

> **80% des données d'entreprise** sont non structurées (Gartner)

Le Machine Learning « classique » excelle sur les données structurées. La **Generative AI** ouvre les données non structurées.

| Type | ML classique | Generative AI |
|---|---|---|
| Structuré | Excellent | Limité |
| Non structuré | Difficile | Excellent |

</div>

---

<!-- _class: section -->

# Enjeux & débats

## Ethical Issues & Debates

---

# 10 — L'éthique dans l'IA

| Enjeu | Question clé | Exemple |
|---|---|---|
| **Fairness** | Les données sont-elles représentatives ? | Biais de genre dans les modèles de recrutement |
| **Vie privée** | Quelles données collecte-t-on ? | RGPD et droit à l'oubli en Europe |
| **Contrôle** | Qui est responsable des décisions ? | Le chatbot Tay de Microsoft (2016) |
| **Singularité** | La machine va-t-elle dépasser l'homme ? | Débat ouvert depuis 70 ans |

> **Pour un entrepreneur** : l'éthique n'est pas un frein — c'est un **avantage compétitif**. Les entreprises qui intègrent la responsabilité IA dès le départ évitent les crises de réputation et sont mieux positionnées face au EU AI Act.

**Question pour la classe** : Si votre startup utilise un modèle qui produit des résultats biaisés, qui est légalement responsable ? Vous ? Le fournisseur du modèle ? Les deux ?

---

<!-- _class: section -->

# Récapitulatif

## Session 1 Summary

---

# 11 — Ce qu'il faut retenir

- **Machine Learning** = apprendre à partir de données pour prédire ou classifier
- **Supervised vs. Unsupervised** : la distinction fondamentale dépend de la présence de labels
- **L'IA a une histoire cyclique** : hype → déception → percée → hype
- **Données structurées vs. non structurées** : deux mondes, deux types d'outils
- **L'éthique est intégrée**, pas optionnelle — surtout en Europe (RGPD, EU AI Act)

> **Pour la prochaine séance** : explorez ChatGPT, Claude ou Mistral Le Chat. Notez 3 tâches de votre quotidien professionnel où un LLM pourrait vous aider.
