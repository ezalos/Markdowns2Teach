# Architecture du cours

<!-- ABOUTME: Calendrier, structure par séance, intervenants et état d'avancement des supports. -->
<!-- ABOUTME: Document de référence pour la planification et la coordination du cours. -->

## Calendrier

| Séance | Date | Titre |
|--------|------|-------|
| 1 | Lundi 23 février 2026 | Comprendre l'IA en 2026 |
| 2 | Lundi 9 mars 2026 | Les LLMs : de la théorie à la pratique |
| 3 | Lundi 16 mars 2026 | Construire avec l'IA |
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
| **Intro** | Présentation enseignant, plan du cours, dates, évaluation, règles | `slides/session-01/0-intro-cours.md` (10 slides) |
| **A** | L'IA Générative : ce qu'elle sait faire — GenAI intro, capabilities, taxonomie IA (techniques, paradigmes, tâches), algorithmes, timelines ML/DL/GenAI | `slides/session-01/A-genai-fondamentaux.md` (37 slides) |
| **C** | Votre premier projet IA — Toolbox (JSON, API, Webhooks, HuggingFace, n8n), démo live Sentiment Analysis en 3 nodes, lancement projet de groupe | `slides/session-01/C-premier-projet-ia.md` (25 slides) |

### Séance 2 — Les LLMs : de la théorie à la pratique

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Les LLMs : comprendre et utiliser — Impact, fonctionnement (next-token prediction), glossaire (Tokens, Context Window, Sampling, MoE), pipeline d'entraînement (Pretraining, Instruct, Thinking, Fine-tuning), accès (Web, API, Open-weights), taille et performance, Structured Output, multimodal, hallucinations & knowledge cutoff (bridge → RAG), principes du Prompting | `slides/session-02/A-llms.md` (40 slides) |
| **B** | Évaluer l'IA — Classification (Confusion Matrix, Accuracy, Precision, Recall, F1), Regression (MAE, RMSE, R²), Computer Vision (IoU, mAP, mIoU, Dice), LLM (benchmarks MMLU/GSM8K/HumanEval, Chatbot Arena, pricing landscape) | `slides/session-02/B-evaluer-ia.md` (18 slides) |
| **C** | N8N #2 — connexion OpenRouter + génération Structured Output | *(design TBD)* |

### Séance 3 — Construire avec l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | RAG & Agents IA — **RAG** : pourquoi (callback hallucinations/cutoff S2), pipeline 5 étapes, chunking, embeddings, vector DBs, hybrid search, applications, RAG vs Fine-tuning. **Agents** : ReAct, Tool Use, MCP protocol, Skills, méthodologie, écosystème 2026 | `slides/session-03/A-rag-agents.md` (27 slides) |
| **B** | Méthodologie projet IA — Prompt-based dev, 4 catégories d'apps GenAI, lifecycle Scope/Build/Evaluate/Deploy, CRISP-DM, LLMOps, AI Canvas, MVP patterns (Gmail story), choix de stack (API vs Open-weights vs Self-hosted), coûts, progression Prompting→RAG→Fine-tuning | `slides/session-03/B-methodologie-projet.md` (27 slides) |
| **C** | Démo agents — workflow MCP / agent guidé | *(design TBD)* |

### Séance 4 — Le business de l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | L'écosystème IA — Chaîne de valeur 9 couches, acteurs clés (NVIDIA, cloud, labs), marché et investissements, positionnement FR/EU, Mistral AI | `slides/session-04/A-ecosysteme-ia.md` (18 slides) |
| **B** | Business Models & Cas Réels — 7 patterns business, déflation des coûts, moats, data flywheel, cas réels (Klarna, L'Oréal, Schneider Electric, Cursor, failure cases, secteurs régulés), 5 tendances structurelles | `slides/session-04/B-business-models.md` (18 slides) |
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

### Decks actifs

| Fichier | Slides | Statut |
|---------|--------|--------|
| `session-01/0-intro-cours.md` | 10 | ✅ Terminé |
| `session-01/A-genai-fondamentaux.md` | 37 | ✅ Terminé |
| `session-01/C-premier-projet-ia.md` | 25 | ✅ Terminé |
| `session-02/A-llms.md` | 40 | ✅ Terminé |
| `session-02/B-evaluer-ia.md` | 18 | ✅ Terminé |
| `session-03/A-rag-agents.md` | 27 | ✅ Terminé (MCP/Skills/méthodologie agents = TODO recherche) |
| `session-03/B-methodologie-projet.md` | 27 | ✅ Terminé (Gmail story = TODO recherche) |
| `session-04/A-ecosysteme-ia.md` | 18 | ✅ Terminé |
| `session-04/B-business-models.md` | 18 | ✅ Terminé |
| `session-05/A-regulation-ethique.md` | 23 | ✅ Terminé |

### Decks de référence (evaluation/)

| Fichier | Slides | Usage |
|---------|--------|-------|
| `evaluation/A-eval-regression.md` | 27 | Référence — essentiels cherry-pickés → S2-B |
| `evaluation/B-eval-classification.md` | 30 | Référence — essentiels cherry-pickés → S2-B |
| `evaluation/C-eval-computer-vision.md` | 31 | Référence — essentiels cherry-pickés → S2-B |
| `evaluation/D-eval-llm.md` | 45 | Référence — essentiels cherry-pickés → S2-B |

### Decks archivés (extra-decks/)

| Fichier | Slides | Origine |
|---------|--------|---------|
| `extra-decks/A-prompt-au-produit.md` | 18 | Ex-S2-A — contenu absorbé dans S3-B |
| `extra-decks/B-ingenierie-ia.md` | 17 | Ex-S2-B — contenu absorbé dans S3-A |
| `extra-decks/B-au-dela-des-llms.md` | 23 | Ex-S1-B — prompting cherry-pické → S2-A |
| `extra-decks/A-evaluer-solution-ia.md` | 18 | Ex-S3-A — remplacé par S2-B |
| `extra-decks/B-methodologie-projet-v1.md` | 17 | Ex-S3-B — restructuré en S3-B + cas → S4-B |
| `extra-decks/architectures.md` | 4 | Extra — CNN, RNN, GAN, Transformer deep dive |
| `extra-decks/D-biais-ethique.md` | 3 | Extra — teaser biais & éthique (S5 couvre le sujet) |

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
| Session 1 — Votre premier projet IA | ✅ `session-01/C-premier-projet-ia.md` (25 slides) |
| Session 2 — N8N #2 (OpenRouter + Structured Output) | ❌ Design TBD |
| Session 3 — Démo agents (MCP workflow) | ❌ Design TBD |
| Session 4 — Intervenants | ✅ Confirmé (Tanguy + Maxime) |
| Session 5 — Présentations + QCM | ✅ Format défini |

## Éléments non encore conçus

- Blocs C pratiques (sessions 2C, 3C) — S1-C terminé
- Recherche approfondie : MCP protocol, Skills, méthodologie agents, RAG avancé (voir `docs/todos.md`)
- Gmail story comme cas d'étude MVP (S3-B slide 13)
- Logistique des présentations finales : 28 étudiants, composition des équipes
