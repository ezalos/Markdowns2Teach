---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: ""
---

<!-- ABOUTME: Introduction au cours — présentation de l'enseignant, plan du cours, modalités d'évaluation. -->
<!-- ABOUTME: Deck d'ouverture de la Session 1, avant les decks thématiques A et B. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->

# Deep Tech & Machine Learning (UE3)

## M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

# 01 — Qui suis-je ?

**Louis — ML Research Engineer**

- *ML Research Engineer* chez Heuritech (4+ ans en ML de production)
- *AI Curriculum Architect* pour 42 Network (20 000+ étudiants)
- Ancien *Président* de l'AI Lab de 42
- *Co-fondateur* d'ICONO SAS (startup IA & Computer Vision)

*Ce que je fais au quotidien* :
- Computer Vision à l'échelle : embeddings, classification, VLMs
- Pipelines ML distribués traitant des millions de frames vidéo par jour
- De la recherche à la production : prototypage → déploiement

> Mon objectif : vous donner l'intuition de ce que le ML peut (et ne peut pas) faire en pratique.

---

# 02 — Ce cours en un mot

*Bridging the gap* entre la Deep Tech et la décision business.

| Ce que ce cours est | Ce que ce cours n'est pas |
|---|---|
| Vous donner de **bons fondamentaux en IA** | Un cours de Data Science |
| Apprendre à **choisir et utiliser** les systèmes IA pour entreprendre | Apprendre à coder des modèles |
| Cadrer et piloter un projet IA | Un catalogue d'outils |
| Développer un regard critique | Une formation ChatGPT |

**5 sessions × 3h** · Du 23 février au 30 mars 2026 · Lundi 17h30–20h30

> Vous êtes des *décideurs*, pas des exécutants techniques. On va vous donner les clés pour décider intelligemment.

---

# 03 — Plan du cours

| Session | Thème | Vous saurez… |
|---|---|---|
| **1** | Les types d'IA | Ce que l'IA sait et ne sait pas faire |
| **2** | Les LLMs | Comment fonctionne un LLM et comment l'utiliser |
| **3** | Évaluer l'IA | Évaluer, choisir et piloter une solution IA |
| **4** | RAG & Agents | Comment construire des systèmes IA complexes |
| **5** | Le business de l'IA | Qui gagne de l'argent, comment, et pourquoi |

> Chaque session inclut un **atelier pratique** (projet de groupe).

---

# 04 — Format des sessions

Chaque session de 3h suit le même rythme :

| Bloc | Durée | Format |
|---|---|---|
| **Deck A** | 45 min | Cours + discussion |
| *Pause* | 15 min | |
| **Deck B** | 45 min | Cours + discussion |
| *Pause* | 15 min | |
| **Bloc C** | 45 min | Pratique ou intervenant |

**Bloc C** par session :
- **S1–S3** : Ateliers n8n + HuggingFace (projet de groupe)
- **S4** : Intervenants externes (Mistral AI, startup IA)
- **S5** : Présentations finales + QCM

> Les questions sont bienvenues *à tout moment*. N'attendez pas la fin.

---

# 05 — Évaluation

| Composante | Poids | Format |
|---|---|---|
| **QCM final** | 30% | 20 questions, 30 min, en Session 5 |
| **Projet de groupe** | 50% | Par équipes de 4, présentation en Session 5 |
| **Participation** | 20% | Engagement en cours et en ateliers |

> Détails complets du projet et des critères dans le **Bloc C** de cette session.

---

# 06 — QCM — Comment ça marche

- Un **QCM unique** en Session 5, couvrant l'ensemble du cours
- Questions à choix multiples sur les 5 sessions
- *Objectif* : vérifier la compréhension, pas piéger

*Format* :
- **20 questions** à choix multiples
- Durée : **30 minutes**
- Supports de cours autorisés : aucun

---

# 07 — Projet de groupe

**Équipes** : 7 groupes de 4 étudiants

**Sujet** : Construire un système de **classification IA** avec HuggingFace + n8n

**3 livrables** : workflow n8n (JSON) + jeu de test (20+ cas) + présentation (5 min en S5)

*Critères d'évaluation* :
- Choix du modèle et justification (25%)
- Qualité de l'évaluation (25%)
- Honnêteté de l'analyse (20%)
- Déploiement fonctionnel (15%)
- Présentation (15%)

> Tous les détails dans le **Bloc C** — après la pause !

---

# 08 — Règles du jeu

*Ce que j'attends de vous* :
- **Poser des questions** — il n'y a pas de question bête
- **Participer aux discussions** — votre expérience est précieuse
- **Être ponctuel** — on commence à 17h30 précises

*Ce que vous pouvez attendre de moi* :
- Des cas concrets et récents (2024–2026)
- De l'honnêteté sur ce que l'IA sait et ne sait pas faire
- De la disponibilité pour vos questions, en cours et par email

**Contact** : develle.louis@gmail.com

> *On y va ?*

---

<!-- _class: section -->

# Passons au contenu

## Session 1A — L'IA Générative : ce qu'elle sait faire

