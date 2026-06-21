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
| **Intro** | Présentation enseignant, plan du cours, dates, évaluation, règles | `slides/sorbonne-m2-2026/session-01/0-intro-cours.md` (10 slides) |
| **A** | L'IA Générative : ce qu'elle sait faire — GenAI intro, capabilities, taxonomie IA (techniques, paradigmes, tâches), algorithmes, timelines ML/DL/GenAI | `slides/sorbonne-m2-2026/session-01/A-genai-fondamentaux.md` (37 slides) |
| **C** | Votre premier projet IA — Toolbox (JSON, API, Webhooks, HuggingFace, n8n), démo live Sentiment Analysis en 3 nodes, lancement projet de groupe | `slides/sorbonne-m2-2026/session-01/C-premier-projet-ia.md` (25 slides) |

### Séance 2 — Les LLMs : de la théorie à la pratique

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Les LLMs : comprendre et utiliser — Impact, fonctionnement (next-token prediction), glossaire (Tokens, Context Window, Sampling, MoE), pipeline d'entraînement (Pretraining, Instruct, Thinking, Fine-tuning), coûts d'entraînement (2.4x/an, >$1B en 2027, breakdown hardware/staff/énergie), données d'entraînement (mur des 300T tokens, Synthetic Data), accès (Web, API, Open-weights, gap open/closed 12-15 mois), taille et performance, Structured Output, multimodal, hallucinations & knowledge cutoff (bridge → RAG), principes du Prompting | `slides/sorbonne-m2-2026/session-02/A-llms.md` (45 slides) |
| **B** | Évaluer l'IA — Classification (Confusion Matrix, Accuracy, Precision, Recall, F1), Regression (MAE, RMSE, R²), Computer Vision (IoU, mAP, mIoU, Dice), LLM (benchmarks MMLU/GSM8K/HumanEval, Chatbot Arena, LM Council "pas de meilleur modèle", ECI accélération ×2, GDPval 44 métiers, pricing landscape) | `slides/sorbonne-m2-2026/session-02/B-evaluer-ia.md` (21 slides) |
| **C** | N8N #2 — connexion OpenRouter + génération Structured Output | *(design TBD)* |

### Séance 3 — Construire avec l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **Info** | Informations pratiques — logistique S4 (42 Paris), intervenants S4/S5, rappels QCM et présentations | `slides/sorbonne-m2-2026/session-03/0-infos.md` (9 slides) |
| **A** | Embeddings — intuition (GPS du sens, 2D→768d), mécanique (PCA, cosine similarity, clusters, word arithmetic), applications (multimodal, choix de modèle) | `slides/sorbonne-m2-2026/session-03/A-embeddings.md` (9 slides) |
| **B** | RAG — pourquoi (hallucinations/cutoff), pipeline (chunking, TF-IDF, BM25, embeddings, hybrid search, vector DB), avancé (reranking, contextual retrieval, production patterns), amélioration (Jason Liu: maturity levels, quick wins, anti-patterns, 6 evals, flywheel) | `slides/sorbonne-m2-2026/session-03/B-rag.md` (25 slides) |
| **C** | Agents IA — spectre d'agence, cycle Think→Act→Observe, Tools & Skills (SKILL.md concret), MCP (HuggingFace diagrams, n8n exemple, débat), 5 patterns Anthropic (avec diagrammes), mémoire LLM-centrée, production (erreurs composées), Context Engineering (3 slides essentielles), produits agents (Claude Code, OpenClaw + pulse files), AutoResearch | `slides/sorbonne-m2-2026/session-03/C-agents.md` (44 slides) |

### Séance 4 — Le business de l'IA

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Méthodologie projet IA — Bitter Lesson, prompt-based dev, GenAI lifecycle (Scope→Build→Evaluate→Deploy), baseline + itération, MVP patterns, 6 pièges AI Engineering, progression Prompting→RAG→Fine-tuning, Gmail Story | `slides/sorbonne-m2-2026/session-04/A-methodologie-projet.md` (17 slides) |
| **B** | L'écosystème IA — Value chain 9 couches (Energy, Hardware, Cloud, Data, Models, Distribution, Safety, Applications), NVIDIA triple verrouillage, Scaling/Inference/Energy intégrés dans les couches, Mistral AI, positionnement FR/EU | `slides/sorbonne-m2-2026/session-04/B-ecosysteme-ia.md` (22 slides) |
| **C** | Business Models & Cas Réels — 7 patterns business, déflation des coûts, moats, data flywheel, cas réels (Klarna, L'Oréal, Schneider Electric, Cursor, failure cases, secteurs régulés), 5 tendances structurelles | `slides/sorbonne-m2-2026/session-04/C-business-models.md` (18 slides) |
| **D** | Intervenants externes (~1h total) | Voir section ci-dessous |

### Séance 5 — Éthique, gouvernance & clôture

| Bloc | Contenu | Fichier |
|------|---------|---------|
| **A** | Régulation & IA responsable — EU AI Act (4 niveaux de risque, calendrier, coûts), RGPD, biais, copyright, impact environnemental, emploi, IA responsable, **Constitutional AI** (Claude's Constitution 83 pages, hiérarchie Safe>Ethical>Compliant>Helpful, Dario Amodei "adolescence de la technologie", débat gouvernance Anthropic), veille techno | `slides/sorbonne-m2-2026/session-05/A-regulation-ethique.md` (27 slides) |
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
| `sorbonne-m2-2026/session-01/0-intro-cours.md` | 10 | ✅ Terminé |
| `sorbonne-m2-2026/session-01/A-genai-fondamentaux.md` | 37 | ✅ Terminé |
| `sorbonne-m2-2026/session-01/C-premier-projet-ia.md` | 25 | ✅ Terminé |
| `sorbonne-m2-2026/session-02/A-llms.md` | 45 | ✅ Terminé — enrichi coûts entraînement (Epoch AI), données limitées, synthetic data, gap open/closed |
| `sorbonne-m2-2026/session-02/B-evaluer-ia.md` | 21 | ✅ Terminé — enrichi LM Council, ECI accélération, GDPval |
| `sorbonne-m2-2026/session-03/A-embeddings.md` | 9 | ✅ Terminé — extrait de A-rag-embeddings |
| `sorbonne-m2-2026/session-03/B-rag.md` | 25 | ✅ Terminé — restructuré avec slides TF-IDF/BM25, intro simplifiée |
| `sorbonne-m2-2026/session-03/C-agents.md` | 44 | ✅ Terminé — restructuré : Tools/Skills→MCP→Patterns→Mémoire→Production→Context Eng.→Produits→AutoResearch. Diagrammes Anthropic + HuggingFace, mémoire LLM-centrée, Context Eng. compacté (5 slides → extra-deck) |
| `sorbonne-m2-2026/session-04/A-methodologie-projet.md` | 17 | ✅ Terminé — restructuré depuis S3-D : Bitter Lesson, CV avant/maintenant, baseline+itération, MVP enrichi, Gmail Story |
| `sorbonne-m2-2026/session-04/B-ecosysteme-ia.md` | 22 | ✅ Terminé — restructuré : 9 couches avec narratif (PDF source), Energy+Data ajoutées, Scaling/Inference intégrés dans couches, 6 PaperBanana, NVIDIA triple verrouillage |
| `sorbonne-m2-2026/session-04/C-business-models.md` | 18 | ✅ Terminé |
| `sorbonne-m2-2026/session-05/A-regulation-ethique.md` | 27 | ✅ Terminé — enrichi Constitutional AI, Amodei, débat gouvernance Anthropic |

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
| `extra-decks/D-methodologie-projet-v1.md` | 25 | Ex-S3-D — restructuré et déplacé vers S4-A |

### QCMs

| Séance | Statut |
|--------|--------|
| Session 1 | ✅ `docs/courses/sorbonne-m2/qcm/session-01-qcm.md` |
| Session 2 | ❌ À faire |
| Session 3 | ✅ `docs/courses/sorbonne-m2/qcm/session-03-qcm.md` |
| Session 4 | ❌ À faire |
| Session 5 | ❌ À faire |

### Blocs C (pratique)

| Séance | Statut |
|--------|--------|
| Session 1 — Votre premier projet IA | ✅ `sorbonne-m2-2026/session-01/C-premier-projet-ia.md` (25 slides) |
| Session 2 — N8N #2 (OpenRouter + Structured Output) | ❌ Design TBD |
| Session 3 — Démo agents (MCP workflow) | ❌ Design TBD |
| Session 4 — Intervenants | ✅ Confirmé (Tanguy + Maxime) |
| Session 5 — Présentations + QCM | ✅ Format défini |

## Éléments non encore conçus

- Blocs C pratiques (sessions 2C, 3C) — S1-C terminé
- Recherche approfondie : MCP protocol, Skills, méthodologie agents, RAG avancé (voir `docs/todos.md`)
- Gmail story comme cas d'étude MVP (S3-B slide 13)
- Logistique des présentations finales : 28 étudiants, composition des équipes
