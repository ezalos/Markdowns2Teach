# Architecture du cours

<!-- ABOUTME: Calendrier, structure par séance, intervenants et état d'avancement des supports. -->
<!-- ABOUTME: Document de référence pour la planification et la coordination du cours. -->

## Calendrier

| Séance | Date | Titre |
|--------|------|-------|
| 1 | Lundi 23 février 2026 | Comprendre l'IA en 2026 |
| 2 | Lundi 9 mars 2026 | Construire avec l'IA |
| 3 | Lundi 16 mars 2026 | Cadrer un projet IA |
| 4 | Lundi 23 mars 2026 | Le business de l'IA |
| 5 | Lundi 30 mars 2026 | Éthique, gouvernance & clôture |

## Format de chaque séance (3h)

| Bloc | Durée | Contenu |
|------|-------|---------|
| **Deck A** | 45 min | Premier thème — présentation + échanges |
| *Pause* | 15 min | |
| **Deck B** | 45 min | Second thème — présentation + échanges |
| *Pause* | 15 min | |
| **Bloc C** | 45 min | Pratique, QCM, ou intervenant externe |
| *Buffer* | 15 min | Marge |

## Détail par séance

### Séance 1 — Comprendre l'IA en 2026

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | L'IA Générative : ce qu'elle sait faire — GenAI intro, capabilities, taxonomie IA (techniques, paradigmes, tâches), vocabulaire HuggingFace, timelines ML/DL/GenAI | `slides/session-01/A-genai-fondamentaux.md` (37 slides) |
| **B** | Les LLMs : comprendre et utiliser — Impact, fonctionnement (next-word prediction), glossaire (Tokens, Context Window, MoE), pipeline d'entraînement (Pretraining, Instruct, Thinking, Fine-tuning), accès (Web, API, Open-weights, licences), taille et performance | `slides/session-02/A-llms.md` (30 slides) — moved to Session 2A |
| **C** | Votre premier projet IA — Toolbox (JSON, API, Webhooks, HuggingFace, n8n), démo live Sentiment Analysis en 3 nodes, lancement projet de groupe | `slides/session-01/C-premier-projet-ia.md` (23 slides) |

### Séance 2 — Construire avec l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Du Prompt au Produit — 4 catégories d'apps IA (Writing/Reading/Chatting/Coding), lifecycle, coûts des APIs | `slides/session-02/A-prompt-au-produit.md` (18 slides) |
| **B** | L'Ingénierie IA — RAG pipeline (5 étapes), hybrid search, RAG vs Fine-tuning, Agentic AI (ReAct, Tool Use, MCP) | `slides/session-02/B-ingenierie-ia.md` (17 slides) |
| **C** | N8N #2 — workflow avec modèle open-source HuggingFace | *(design TBD)* |

### Séance 3 — Cadrer un projet IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Évaluer une solution IA — Métriques (matrice de confusion, précision/rappel), architecture, benchmarks, Build vs Buy, no-code landscape | `slides/session-03/A-evaluer-solution-ia.md` (18 slides) |
| **B** | Méthodologie projet IA — CRISP-DM, LLMOps, AI Canvas, Open Source vs API, cas d'études (Klarna, L'Oréal, Schneider, Doctolib, Alan) | `slides/session-03/B-methodologie-projet.md` (17 slides) |
| **C** | *(TBD — travail projet ou exercice)* | |

### Séance 4 — Le business de l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | L'écosystème IA — Chaîne de valeur 9 couches, acteurs clés (NVIDIA, cloud, labs), marché et investissements, positionnement FR/EU, Mistral AI | `slides/session-04/A-ecosysteme-ia.md` (18 slides) |
| **B** | Business Models & Cas Réels — 7 patterns business, déflation des coûts, moats, data flywheel, cas réels, 5 tendances structurelles | `slides/session-04/B-business-models.md` (17 slides) |
| **C** | Intervenants externes (~1h total) | Voir section ci-dessous |

### Séance 5 — Éthique, gouvernance & clôture

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Régulation & IA responsable — EU AI Act (4 niveaux de risque, calendrier, coûts), RGPD, biais, copyright, impact environnemental, emploi, IA responsable, veille techno | `slides/session-05/A-regulation-ethique.md` (23 slides) |
| **B** | Présentations finales — 7 équipes × 5 min + feedback (~40 min) | *(live)* |
| **C** | QCM final & clôture | |

## Intervenants externes (Séance 4, Bloc C)

| Intervenant | Sujet | Durée | Détail |
|-------------|-------|-------|--------|
| **Tanguy Auffret** | Business de l'IA & Mistral | ~1h | Parcours business, positionnement Mistral, décisions stratégiques |
| **Maxime Jegat** | Entrepreneuriat IA — Hoox | ~30 min + Q&A | Parcours fondateur, décisions build vs buy, retour d'expérience concret |

## État des supports

### Decks

| Fichier | Slides | Statut |
|---------|--------|--------|
| `session-01/A-genai-fondamentaux.md` | 37 | ✅ Terminé |
| `session-02/A-llms.md` | 30 | ✅ Terminé |
| `session-01/C-premier-projet-ia.md` | 23 | ✅ Terminé |
| `session-02/A-prompt-au-produit.md` | 18 | ✅ Terminé |
| `session-02/B-ingenierie-ia.md` | 17 | ✅ Terminé |
| `session-03/A-evaluer-solution-ia.md` | 18 | ✅ Terminé |
| `session-03/B-methodologie-projet.md` | 17 | ✅ Terminé |
| `session-04/A-ecosysteme-ia.md` | 18 | ✅ Terminé |
| `session-04/B-business-models.md` | 17 | ✅ Terminé |
| `session-05/A-regulation-ethique.md` | 23 | ✅ Terminé |
| `extra-decks/architectures.md` | 4 | ✅ Extra |
| `extra-decks/D-biais-ethique.md` | 3 | ✅ Extra |
| `session-02/B-au-dela-des-llms.md` | 23 | ✅ Archive (ex-S01-B) |

### QCMs

| Séance | Statut |
|--------|--------|
| Session 1 | ✅ `docs/qcm/session-01-qcm.md` |
| Session 2 | ❌ À faire |
| Session 3 | ✅ `docs/qcm/session-03-qcm.md` |
| Session 4 | ❌ À faire |
| Session 5 | ❌ À faire |

### Blocs C (pratique)

| Séance | Statut |
|--------|--------|
| Session 1 — Votre premier projet IA | ✅ `session-01/C-premier-projet-ia.md` (22 slides) |
| Session 2 — N8N #2 | ❌ Design TBD |
| Session 3 | ❌ TBD |
| Session 4 — Intervenants | ✅ Confirmé (Tanguy + Maxime) |
| Session 5 — Présentations + QCM | ✅ Format défini |

## Éléments non encore conçus

- Progression des ateliers N8N (sessions 2C, 3C) — S1-C terminé
- Compétition prompt engineering : timing, design du dataset
- Logistique des présentations finales : 28 étudiants, composition des équipes
