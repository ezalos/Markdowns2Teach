# QCM — Sessions 1 à 4

## Deep Tech & Machine Learning (UE3) — M2 IMT&E — Paris 1 Panthéon-Sorbonne

- **Date** : Lundi 30 mars 2026
- **Format** : 20 questions, 5 propositions chacune (Vrai / Faux)
- **Périmètre** : Sessions 1 à 4

Bien mettre sur les feuilles imprimees : 
- les questions peuvent avoir plusieurs bonnes reponses
- bien noircir les cases des affirmations vraies. Ce sera corrige par un systeme automatique, donc attention


---

# Partie 1 — Questions

---

## Session 1 — L'IA Générative : ce qu'elle sait faire

### Question 1 — IA Générative vs IA Traditionnelle

Pour chaque proposition, indiquez si elle est **vraie** ou **fausse** :

- A) L'IA générative représente la majorité de la valeur économique totale créée par l'IA.
- B) Le Machine Learning traditionnel est plus déployé en entreprise que l'IA générative.
- C) L'IA générative sert principalement à la prédiction et l'optimisation.
- D) Le Deep Learning est un sous-ensemble du Machine Learning.
- E) ChatGPT est un exemple d'IA générative.

---

### Question 2 — Paradigmes d'apprentissage

- A) Le Reinforcement Learning apprend à partir d'exemples étiquetés (Input → Output).
- B) Le Self-Supervised Learning est le paradigme derrière les LLMs et les modèles de diffusion.
- C) L'algorithme kNN (k Nearest Neighbors) est un algorithme d'Unsupervised Learning.
- D) Le clustering est une technique de Supervised Learning.
- E) AlphaGo utilise le Reinforcement Learning pour apprendre à jouer au Go.

---

### Question 3 — Deep Learning et Transformers

- A) Le mécanisme d'attention (Transformer) est l'innovation de rupture qui a permis l'essor des LLMs.
- B) Plus un réseau de neurones a de couches, plus il peut détecter des patterns complexes.
- C) Le papier « Attention Is All You Need » qui introduit le Transformer a été publié en 2022.
- D) BERT (2018) utilise le Supervised Learning classique pour son pré-entraînement.
- E) ChatGPT a atteint 100 millions d'utilisateurs en 2 mois après son lancement.

---

### Question 4 — Tâches d'IA

- A) La Classification assigne une catégorie discrète à une entrée (ex. : Spam / Non-spam).
- B) La Régression prédit une valeur continue (ex. : prix d'un appartement).
- C) L'Object Detection identifie chaque pixel de l'image par catégorie.
- D) La Segmentation Sémantique sépare les objets individuels et la Segmentation d'Instance colore par catégorie.
- E) Un système de recommandation (Netflix, Spotify) est un cas d'usage typique du Machine Learning traditionnel.

---

### Question 5 — Définition du Machine Learning (Chip Huyen)

- A) Le Machine Learning nécessite des données existantes ou collectables.
- B) Le ML est particulièrement adapté quand les patterns sont simples et codables manuellement.
- C) Un problème de ML doit être formulable comme un problème de prédiction.
- D) Les patterns appris par un modèle ML n'ont pas besoin de se généraliser à de nouvelles données.
- E) Le K-Means classe un point en fonction de ses K voisins les plus proches.

---

## Session 2 — Les LLMs & Évaluer l'IA

### Question 6 — Mécanisme des LLMs

- A) Un LLM génère du texte en prédisant le prochain token.
- B) Un token correspond exactement à un mot.
- C) La Context Window est partagée entre l'entrée (prompt) et la sortie (réponse).
- D) Un vocabulaire de tokens plus grand signifie plus de tokens par phrase, donc un coût plus élevé.
- E) Les Thinking Tokens (raisonnement interne) sont facturés mais généralement supprimés de la réponse finale.

---

### Question 7 — Sampling et Mixture of Experts

- A) Une température basse (0.1) produit des réponses plus créatives et variées.
- B) Le Mixture of Experts (MoE) active tous ses experts pour chaque token généré.
- C) L'architecture de Mixture of Experts (MoE) est ideale pour reduire le besoin en vRAM d'un modele.
- D) Le Top-p (nucleus sampling) conserve les tokens dont la probabilité cumulée ne dépasse pas p.
- E) Le MoE offre la performance d'un grand modèle avec la vitesse d'un petit modèle.

---

### Question 8 — Pipeline d'entraînement des LLMs

- A) Le Pretraining apprend le langage à partir de trillions de tokens issus d'internet.
- B) Le RLHF (Reinforcement Learning from Human Feedback) est l'étape qui apprend au modèle à suivre des instructions.
- C) Un Thinking Model (ex. : o3, DeepSeek-R1) est entraîné avec une étape supplémentaire de raisonnement.
- D) Le Fine-tuning coûte aussi cher que le Pretraining d'un modèle.
- E) Le Supervised Instruction Finetuning est la troisieme etape d'entrainement d'un LLM.

---

### Question 9 — Métriques de classification

- A) L'Accuracy est généralement la meilleure métrique pour évaluer un classifieur.
- B) La Precision mesure : « parmi mes alertes, combien sont vraies ? ».
- C) Le Recall est prioritaire quand les faux négatifs sont coûteux (ex. : dépistage médical).
- D) Le F1-Score est calculé a partir de la Precision et du Recall.
- E) Un modèle avec 90% de Precision et 10% de Recall a un F1-Score de 50%.

---

### Question 10 — Benchmarks et modèles

- A) Aucun modèle ne domine sur l'ensemble des benchmarks indépendants.
- B) Chatbot Arena utilise un système de classement basé sur des notes attribuées par des experts.
- C) Le coût de l'inférence à performance équivalente diminue d'environ 2x par an.
- D) Les modèles open-weights ont un retard sur les benchmarks (comme GPQA) de 5 mois sur les modèles propriétaires.
- E) Le meilleur modèle pour une entreprise dépend de son cas d'usage spécifique, pas du leaderboard.

---

## Session 3 — Embeddings, RAG, Agents IA

### Question 11 — Embeddings

- A) Un embedding transforme du texte en coordonnées dans un espace mathématique.
- B) Il n'est pas possible de comparer a quel point un embedding est similaire a un autre.
- C) Deux textes avec un sens similaire auront des embeddings proches dans l'espace vectoriel.
- D) Les relations sémantiques capturées par les embeddings sont programmées manuellement.
- E) Il existe des embeddigns pour differents types de donnees (text, image, proteines, ...)

---

### Question 12 — RAG : Pipeline et recherche

- A) Le RAG réduit les hallucinations de 70 à 90% par rapport à un LLM seul.
- B) Le pipeline RAG comporte 5 étapes : Chunking, Embedding, Indexation, Retrieval, Generation.
- C) La recherche par embeddings seuls est toujours supérieure à la recherche par mots-clés (BM25).
- D) Le RAG injecte des documents pertinents dans le prompt pour améliorer les réponses du LLM.
- E) Le chunking sémantique est le plus rapide mais le moins précis des stratégies de découpage.

---

### Question 13 — RAG avancé et décisions

- A) Le RAG est toujours préférable au Fine-tuning, quel que soit le cas d'usage.
- B) Pour un corpus de moins de 500 pages, le Context Stuffing avec Prompt Caching peut remplacer le RAG.
- C) Le RAG permet de citer ses sources, contrairement au Fine-tuning.
- D) Plus de 90% des systèmes RAG complexes performent mieux qu'une baseline simple et bien évaluée.
- E) La combinaison RAG + Fine-tuning peut apporter 10 à 20% de précision supplémentaire par rapport à chacun utilisé seul.

---

### Question 14 — Agents IA : définition et spectre

- A) Un agent IA est un LLM capable de raisonner, planifier et interagir avec son environnement.
- B) Le cycle ReAct (Think → Act → Observe) est le pattern fondamental des agents.
- C) La majorité des cas business nécessitent des architectures multi-agents complexes.
- D) Le MCP (Model Context Protocol) transforme M×N intégrations en M+N.
- E) Un agent autonome est recommandé dès qu'une tâche est répétitive.

---

### Question 15 — Agents en production

- A) Plus un système agent a d'étapes, plus le risque d'erreur global augmente.
- B) Gartner prédit que 40% des projets agents seront annulés d'ici 2027.
- C) La complexité (frameworks, multi-agents) est recommandée dès le début d'un projet agent.
- D) Le Context Engineering comprend 4 opérations : Write, Select, Compress, Isolate.
- E) Les subagents augmentent le bruit dans le contexte principal de l'agent.

---

## Session 4 — Méthodologie, Écosystème, Business

### Question 16 — Méthodologie projet IA

- A) The Bitter Lesson (Sutton) montre que les méthodes générales utilisant le calcul l'emportent toujours sur l'ingénierie manuelle.
- B) Le cycle de vie GenAI est linéaire : Scope → Build → Evaluate → Deploy → terminé.
- C) La baseline (modèle le plus simple possible) doit être établie en premier avant d'itérer.
- D) Un MVP est une version dégradée du produit final.
- E) Règle #1 du ML chez Google : si vous pouvez résoudre le problème sans ML, faites-le d'abord.

---

### Question 17 — Infrastructure IA

- A) L'énergie, et non les puces, est le principal goulot d'étranglement qui détermine où l'IA est construite.
- B) ASML (Pays-Bas) est le seul fournisseur mondial de machines de lithographie EUV.
- C) NVIDIA tire l'essentiel de son chiffre d'affaires de ses cartes graphiques gaming.
- D) CUDA crée un effet de verrouillage (lock-in) avec 6 millions de développeurs.
- E) Les modèles open-weights représentent environ 70% de l'utilisation globale des LLMs.

---

### Question 18 — Souveraineté et écosystème européen

- A) Le CLOUD Act américain entre en conflit avec le RGPD européen pour l'accès aux données.
- B) Mistral AI atteint 90% de la performance des modèles frontier à 20% du prix.
- C) Hugging Face héberge plus d'un million de modèles d'IA.
- D) L'EU AI Act entre pleinement en vigueur pour les systèmes à haut risque en 2030.
- E) Les États-Unis investissent environ 8 fois plus que la France dans l'IA (investissement privé).

---

### Question 19 — Business Models IA

- A) Le modèle de pricing par siège (seat-based) est en croissance dans le SaaS IA.
- B) Le modèle hybride (abonnement + crédits à l'usage) est désormais le plus adopté.
- C) Les wrappers IA (simples interfaces autour d'un LLM) ont un taux de réussite d'environ 85%.
- D) Le Vertical AI SaaS offre un TAM (Total Addressable Market) jusqu'à 10x supérieur au SaaS traditionnel du même secteur.
- E) Le moat le plus durable en IA est le modèle lui-même (sa performance sur les benchmarks).

---

### Question 20 — Cas réels et leçons business

- A) Klarna a d'abord économisé $40M grâce à l'IA, puis a dû réembaucher des humains.
- B) La leçon principale de Klarna est qu'il faut remplacer les humains le plus rapidement possible pour maximiser les économies.
- C) L'Oréal a construit sa technologie IA (beauty tech) entièrement en interne.
- D) Air Canada a été juridiquement condamnée pour les erreurs commises par son chatbot.
- E) Cursor paie plus à Anthropic (son fournisseur de modèle) qu'il ne génère de chiffre d'affaires.

---
---

# Partie 2 — Corrigé

## Légende

- **Source** : Deck (ex. S1-A = Session 1, Deck A) et numéro de slide
- **Raison** : explication si la réponse n'est pas évidente

---

## Session 1

### Question 1 — IA Générative vs IA Traditionnelle

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S1-A, slide 08 | Le ML traditionnel génère ~75% de la valeur totale ($11–17,7 T vs $2,6–4,4 T pour la GenAI). |
| B | **VRAI** | S1-A, slide 08 | 71% des déploiements enterprise sont du ML traditionnel vs 29% GenAI. |
| C | **FAUX** | S1-A, slide 08 | Prédiction et optimisation = ML traditionnel. La GenAI sert à la génération et au raisonnement. |
| D | **VRAI** | S1-A, slide 10 | La taxonomie montre DL ⊂ ML ⊂ IA (emboîtement). |
| E | **VRAI** | S1-A, slide 02 | Present dans le screenshot. |

---

### Question 2 — Paradigmes d'apprentissage

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S1-A, slides 20 et 27 | Le RL apprend par essai-erreur avec un signal de récompense. Ce sont les modèles supervisés qui utilisent des exemples étiquetés. |
| B | **VRAI** | S1-A, slide 26 | Le Self-Supervised Learning est présenté comme « le secret de la GenAI » (LLMs et diffusion). |
| C | **FAUX** | S1-A, slide 23 | exemple de la slide |
| D | **FAUX** | S1-A, slide 24 | Le clustering est une technique d'Unsupervised Learning (sans étiquettes). |
| E | **VRAI** | S1-A, slide 27 | AlphaGo (2016) utilise le RL et a battu le champion du monde de Go. |

---

### Question 3 — Deep Learning et Transformers

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S1-A, slides 17–18 | Le Self-Attention résout le problème du vecteur fixe (bottleneck) qui perdait de l'information. |
| B | **VRAI** | S1-A, slide 15 | Plus de couches = patterns plus complexes détectables. |
| C | **FAUX** | S1-A, slide 35 | « Attention Is All You Need » date de **2017**, pas 2022. |
| D | **FAUX** | S1-A, slide 26 | BERT utilise le Self-Supervised Learning (prédiction de mots masqués), pas le Supervised Learning. |
| E | **VRAI** | S1-A, slide 36 | ChatGPT a atteint 100M d'utilisateurs en 2 mois (record historique). |

---

### Question 4 — Tâches d'IA

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S1-A, slide 29 | Définition exacte de la classification. |
| B | **VRAI** | S1-A, slide 30 | Définition exacte de la régression. |
| C | **FAUX** | S1-A, slide 31 | L'Object Detection localise avec des bounding boxes. C'est la Segmentation Sémantique qui identifie chaque pixel. |
| D | **FAUX** | S1-A, slide 31 | La Segmentation Sémantique colore par catégorie ; la Segmentation d'Instance sépare les objets individuels. |
| E | **VRAI** | S1-A, slide 08 | Systèmes de recommandation = cas d'usage classique du ML traditionnel (Amazon, Netflix, Spotify). |

---

### Question 5 — Définition du Machine Learning (Chip Huyen)

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S1-A, slide 12 | Condition 3 de Chip Huyen : les données existent ou sont collectables. |
| B | **FAUX** | S1-A, slide 12 | Condition 2 : le ML est adapté quand les patterns sont *trop complexes* pour être codés manuellement. |
| C | **VRAI** | S1-A, slide 12 | Condition 4 : le problème doit être formulable comme une prédiction. |
| D | **FAUX** | S1-A, slide 12 | Condition 5 : les patterns doivent se généraliser à des données jamais vues. |
| E | **FAUX** | S1-A, slide 23 | KNN classe par vote des K voisins les plus proches dans l'espace des features. |

---

## Session 2

### Question 6 — Mécanisme des LLMs

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S2-A, slide 03 | Mécanisme fondamental : Next-Token Prediction. |
| B | **FAUX** | S2-A, slide 04 | Un token ≈ ¾ d'un mot en anglais (ratio encore moins favorable en français). |
| C | **VRAI** | S2-A, slide 05 | La Context Window est partagée entre input et output (ex. : 200K pour Claude). |
| D | **FAUX** | S2-A, slide 04 | C'est l'inverse : un vocabulaire plus grand = moins de tokens par phrase = coût plus faible. |
| E | **VRAI** | S2-A, slide 05 | Les Thinking Tokens sont comptés pendant la génération (et facturés) puis retirés de la réponse. |

---

### Question 7 — Sampling et Mixture of Experts

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S2-A, slide 07 | Température basse = réponses déterministes. Température haute = créativité (mais risque). |
| B | **FAUX** | S2-A, slide 08 | Le MoE n'active qu'une fraction des experts par token (ex. : 37B actifs sur 671B pour DeepSeek-V3). |
| C | **FAUX** | S2-A, slide  26| dans "le piege" |
| D | **VRAI** | S2-A, slide 07 | Définition du nucleus sampling : conserver les tokens avec probabilité cumulée ≤ p. |
| E | **VRAI** | S2-A, slide 08 | Avantage clé du MoE : « Performance of big model, speed of small ». |

---

### Question 8 — Pipeline d'entraînement des LLMs

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S2-A, slide 09 | Le Pretraining utilise ~15T tokens pour apprendre le langage et les faits. |
| B | **FAUX** | S2-A, slide 09 | C'est le SFT (Supervised Fine-Tuning / Instruct) qui enseigne à suivre des instructions. Le RLHF rend le modèle utile et honnête (alignement). |
| C | **VRAI** | S2-A, slides 09–10 | Les Thinking Models ajoutent une 4ᵉ étape de raisonnement au pipeline. |
| D | **FAUX** | S2-A, slide 12 | Le Pretraining coûte des millions de dollars ; le Fine-tuning coûte des centaines de dollars. Rapport ~1000x. |
| E | **FAUX** | S2-A, slide 109 | . |

---

### Question 9 — Métriques de classification

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S2-B, slides 02–03 | L'Accuracy est trompeuse sur des données déséquilibrées (ex. : scanner bagages 99,9% accuracy mais 0% Recall). |
| B | **VRAI** | S2-B, slide 04 | Définition exacte de la Precision : TP / (TP + FP). |
| C | **VRAI** | S2-B, slide 05 | Le Recall est critique quand rater un cas positif est grave (cancer, fraude). |
| D | **FAUX** | S2-B, slide 06 | Le F1-Score est la moyenne **harmonique** (pas arithmétique) de Precision et Recall. |
| E | **FAUX** | S2-B, slide 06 | Avec la moyenne harmonique : 2 × (0.9 × 0.1) / (0.9 + 0.1) = **18%**, pas 50%. C'est ce qui rend le F1 exigeant. |

---

### Question 10 — Benchmarks et modèles

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S2-B, slide 13 | Sur 20+ benchmarks indépendants, aucun modèle ne domine partout. Chaque famille excelle dans un domaine. |
| B | **FAUX** | S2-B, slide 12 | Chatbot Arena utilise des votes d'**utilisateurs** (système Elo, 6M+ votes), pas des notes d'experts. |
| C | **FAUX** | S2-A, slide 20 | La baisse est d'environ **10x par an** (pas 2x). GPT-3.5 équivalent : $20 → $0,07 en 18 mois. |
| D | **VRAI** | S2-A, slide 23 | Retard estimé à 5 mois (compute differeent: 12-15 - IC 90% : 6–22 mois). |
| E | **VRAI** | S2-B, slide 13 | Chaque famille excelle dans un domaine différent : le choix dépend du cas d'usage, pas du classement général. |

---

## Session 3

### Question 11 — Embeddings

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S3-A, slides 01–02 | Définition : un embedding encode le sens d'un texte en coordonnées dans un espace mathématique. |
| B | **FAUX** | S3-A, slide 04 | Cosine similarity. |
| C | **VRAI** | S3-A, slides 01–04 | Définition fondamentale : des textes de sens proche ont des vecteurs proches dans l'espace. |
| D | **FAUX** | S3-A, slide 05 | Ces relations **émergent** de l'entraînement sur les données, elles ne sont pas programmées manuellement. |
| E | **VRAI** | S3-A, slide 07 | ccc |

---

### Question 12 — RAG : Pipeline et recherche

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S3-B, slide 05 | Chiffre documenté : réduction de 70–90% des hallucinations. |
| B | **VRAI** | S3-B, slide 05 | Les 5 étapes exactes du pipeline RAG. |
| C | **FAUX** | S3-B, slide 11 | Preuve mathématique (DeepMind) : BM25 atteint 97,8% de Recall@2 vs 29,5% pour les embeddings denses sur certaines requêtes. Limite structurelle, pas un problème d'entraînement. |
| D | **VRAI** | S3-B, slides 01–03 | Définition fondamentale du RAG : injecter des documents pertinents dans le prompt. |
| E | **FAUX** | S3-B, slide 06 | C'est l'inverse : le chunking sémantique est le **plus précis** mais le **plus lent**. |

---

### Question 13 — RAG avancé et décisions

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S3-B, slide 15 | Le choix dépend du cas d'usage : le Fine-tuning est meilleur pour la cohérence de style et les gros volumes. |
| B | **VRAI** | S3-B, slide 16 | Pour un petit corpus (~500 pages / 200K tokens), le Context Stuffing + Prompt Caching est plus simple. |
| C | **VRAI** | S3-B, slide 15 | Le RAG cite ses sources (traçabilité) ; le Fine-tuning ne le permet pas (boîte noire). |
| D | **FAUX** | S3-B, slide 19 | C'est l'inverse : >90% des systèmes complexes performent **moins bien** qu'une baseline bien évaluée. Anti-pattern de complexité prématurée. |
| E | **VRAI** | S3-B, slide 15 | RAG + Fine-tuning ensemble = +10–20% vs chacun seul (approches complémentaires). |

---

### Question 14 — Agents IA : définition et spectre

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S3-C, slide 01 | Définition exacte d'un agent IA. |
| B | **VRAI** | S3-C, slide 03 | Le cycle Think → Act → Observe (ReAct) est le pattern fondamental. |
| C | **FAUX** | S3-C, slide 02 | La majorité des cas = Router + Tool Caller. Le multi-agent est rare et problématique. |
| D | **VRAI** | S3-C, slide 10 | Avantage clé du MCP : passer de M×N intégrations (multiplicatif) à M+N (additif). |
| E | **FAUX** | S3-C, slide 17 | Pour les tâches répétitives et prévisibles, le Prompt Chaining suffit. Les agents sont pour les décisions flexibles et imprévisibles. |

---

### Question 15 — Agents en production

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S3-C, slide 29 | Plus d'étapes = plus de chances qu'une étape échoue. L'erreur se compose exponentiellement. |
| B | **VRAI** | S3-C, slide 29 | Prédiction Gartner citée dans le deck. |
| C | **FAUX** | S3-C, slide 17 | Anthropic : « Most successful implementations weren't using complex frameworks. » Commencer simple. |
| D | **VRAI** | S3-C, slide 34 | Les 4 opérations du Context Engineering : Write, Select, Compress, Isolate. |
| E | **FAUX** | S3-C, slide 35 | C'est l'inverse : les subagents **réduisent** le bruit (de 91% de bruit à 76% de signal dans le contexte principal). |

---

## Session 4

### Question 16 — Méthodologie projet IA

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S4-A, slide 01 | The Bitter Lesson (Sutton, 2019) : les méthodes générales + compute battent l'ingénierie manuelle. |
| B | **FAUX** | S4-A, slide 04 | Le cycle est **itératif** avec des retours constants entre étapes, pas linéaire. |
| C | **VRAI** | S4-A, slide 09 | La baseline est le point de référence initial. « Baseline en 1 jour > modèle parfait en 3 mois. » |
| D | **FAUX** | S4-A, slide 12 | Un MVP n'est pas une version dégradée : c'est le test le plus simple de l'hypothèse. |
| E | **VRAI** | S4-A, slide 11 | Google Rule of ML #1, citée explicitement dans le deck. |

---

### Question 17 — Infrastructure IA

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S4-B, slide 05 | « Energy, not chips, determines WHERE AI is built. » Délai de 7 ans pour une connexion réseau en Virginie. |
| B | **VRAI** | S4-B, slide 06 | ASML est le monopole mondial sur les machines EUV ($200–370M par machine, 2 ans de backlog). |
| C | **FAUX** | S4-B, slide 07 | 88% du CA de NVIDIA vient du **data center**, pas du gaming. |
| D | **VRAI** | S4-B, slide 07 | CUDA : 20 ans d'écosystème, 6M de développeurs verrouillés. Migrer = tout réécrire. |
| E | **FAUX** | S4-B, slide 13 | C'est l'inverse : ~30% open-weights vs ~70% propriétaire. |

---

### Question 18 — Souveraineté et écosystème européen

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S4-B, slide 09 | Le CLOUD Act US permet l'accès aux données, en conflit direct avec le RGPD. Microsoft l'a admis devant le Sénat français. |
| B | **VRAI** | S4-B, slide 14 | Positionnement de Mistral AI : efficience d'abord, 90% de la performance à 20% du prix. |
| C | **VRAI** | S4-B, slide 15 | Hugging Face héberge 2M+ modèles, valorisé à $4,5 Mds. |
| D | **FAUX** | S4-B, slide 16 | L'EU AI Act entre en vigueur le **2 août 2026** pour les systèmes à haut risque, pas 2030. |
| E | **VRAI** | S4-B, slide 19 | Les US investissent ~8x plus en privé. L'Europe ne gagnera pas la course au compute mais peut gagner celle de la confiance. |

---

### Question 19 — Business Models IA

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **FAUX** | S4-C, slide 01 | Le seat-based est en **déclin** : 21% → 15%. |
| B | **VRAI** | S4-C, slide 01 | Le modèle hybride passe de 27% à 41%, devenant le plus adopté. |
| C | **FAUX** | S4-C, slide 04 | C'est l'inverse : les wrappers ont un taux d'**échec** de 85–92%. |
| D | **VRAI** | S4-C, slide 03 | Le Vertical AI SaaS offre un TAM 10x plus large grâce à la spécialisation sectorielle. |
| E | **FAUX** | S4-C, slide 05 | « The AI model is NOT the moat. » Les moats les plus durables sont les données propriétaires et les effets de réseau. |

---

### Question 20 — Cas réels et leçons business

| # | Réponse | Source | Raison |
|---|---------|--------|--------|
| A | **VRAI** | S4-C, slide 07 | Klarna : $40M économisés (2024) puis réembauche d'humains début 2025, retour à une perte de $152M au S1. |
| B | **FAUX** | S4-C, slide 07 | C'est la leçon inverse : « Augmentation > remplacement total — the most expensive lesson of 2025. » |
| C | **FAUX** | S4-C, slide 08 | L'Oréal a **acheté** ModiFace (startup AR/AI beauté). L'acquisition est une stratégie IA légitime. |
| D | **VRAI** | S4-C, slide 12 | Jurisprudence : « You are responsible for your chatbot. » Condamnation à CAD $812. |
| E | **VRAI** | S4-C, slide 11 | Cursor paie ~$650M/an à Anthropic pour ~$500M de CA. Croissance ≠ profitabilité. |
