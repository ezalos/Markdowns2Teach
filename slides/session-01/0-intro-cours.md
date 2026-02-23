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

| Thème | Vous saurez… |
|---|---|
| Les types d'IA | Ce que l'IA sait et ne sait pas faire |
| Les LLMs | Comment fonctionne un LLM et comment l'utiliser |
| Du prompt au produit | Comment on passe d'un prompt à un produit |
| Évaluer l'IA | Évaluer, choisir et piloter une solution IA |
| RAG & Agents | Comment construire des systèmes IA complexes |
| Le business de l'IA | Qui gagne de l'argent, comment, et pourquoi |
| Éthique & gouvernance | Les règles du jeu et vos présentations finales |


---

# 04 — Dates des sessions

| Session | Date | Horaire | Lieu |
|---|---|---|---|
| **1** | Lundi 23 février | 17h30–20h30 | Paris 1 — 14 rue Cujas |
| **2** | Lundi 9 mars | 17h30–20h30 | Paris 1 — 14 rue Cujas |
| **3** | Lundi 16 mars | 17h30–20h30 | Paris 1 — 14 rue Cujas |
| **4** | Lundi 23 mars | **18h00–21h00** | **École 42 — 96 Bd Bessières** |
| **5** | Lundi 30 mars | 17h30–20h30 | Paris 1 — 14 rue Cujas |

**⚠️ Session 4** : pour accueillir un intervenant en fauteuil roulant, le cours a lieu à l'**École 42** (96 Bd Bessières, 75017). Depuis le 14 rue Cujas : **~30 min** (RER B + métro 14, ou métro 4 + 14). Le cours démarre **30 min plus tard** (18h) pour que tout le monde ait le temps d'arriver.

---

# 05 — Format des sessions

Chaque session de 3h suit le même rythme :

| Bloc | Durée |
|---|---|
| **Deck A** — Cours + discussion | 45 min |
| *Pause* | 15 min |
| **Deck B** — Cours + discussion | 45 min |
| *Pause* | 15 min |
| **Bloc C** — Pratique ou intervenant | 45 min |

> Les questions sont bienvenues *à tout moment*. N'attendez pas la fin.

---

# 06 — Évaluation

| Composante | Poids | Format |
|---|---|---|
| **QCM final** | 40% | 20 questions, 30 min, en Session 5 |
| **Projet de groupe** | 40% | Par équipes de 4, présentation en Session 5 |
| **Participation** | 20% | Engagement en cours et en ateliers |

> Détails complets du projet et des critères dans le **Bloc C** de cette session.

---

# 07 — QCM — Comment ça marche

- Un **QCM** en Session 5, couvrant l'ensemble du cours
- Questions à choix multiples sur les 5 sessions
- *Objectif* : vérifier la compréhension, pas piéger

*Format* :
- **20 questions** à choix multiples
- Durée : **30 minutes**
- Supports de cours autorisés : aucun

---

# 08 — Projet de groupe

**7 équipes de 4** · Présentations en Session 5 (4 min par groupe)

**Sujet** : Construire un système de **classification IA** avec HuggingFace ou un LLM, automatisé via n8n

**Livrables** : workflow n8n fonctionnel + interface accessible en ligne + dataset de test (20+ cas) + évaluation de 2+ modèles comparés

*L'essentiel* : la démo marche en live, le dataset est solide, et vous avez un regard critique sur les résultats.

> Tous les détails dans le **Bloc C** — après la pause !

---

# 09 — Règles du jeu

*Ce que j'attends de vous* :
- **Poser des questions** — il n'y a pas de question bête
- **Participer aux discussions** — votre expérience est précieuse
- **Être ponctuel** — on commence à 17h30 précises

*Ce que vous pouvez attendre de moi* :
- Des cas concrets et récents (2023–2026)
- De l'honnêteté sur ce que l'IA sait et ne sait pas faire
- De la disponibilité pour vos questions, en cours et par email

**Contact** : develle.louis@gmail.com

> *On y va ?*

---

<!-- _class: section -->

# Passons au contenu

## Session 1A — L'IA Générative : ce qu'elle sait faire

