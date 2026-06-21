---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Panorama des métriques d'évaluation IA — classification, régression, computer vision et LLMs en un seul deck. -->
<!-- ABOUTME: Version condensée ("greatest hits") des 4 decks de référence, cadrée pour étudiants M2 non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Évaluer l'IA

## Le guide essentiel des métriques

Deep Tech & ML (UE3) · Session 2
M2 IMT&E · Paris 1 Panthéon-Sorbonne

---

<!-- _class: section -->

# Classification

## Quand le modèle doit répondre oui ou non

---

<!-- _class: img-right -->

# 01 — La Confusion Matrix

- Le modèle produit une **prédiction** (Positive ou Negative)
- La réalité est le **ground truth** (Positive ou Negative)
- Le croisement donne **4 cas** : TP, TN, FP, FN

> **Mnémotechnique** : le 2e mot = réponse du modèle, le 1er mot = avait-il raison ?

<small>Source : [stratusdata.io](https://stratusdata.io/gone-fishing-4-metrics-for-evaluating-binary-classifiers/)</small>

![bg right:45% contain](assets/eval/confusion-matrix.png)

---

<!-- _class: img-right -->

# 02 — Accuracy

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)
- Intuition : "sur 100 cas, combien le modèle a-t-il correctement classés ?"
- La métrique la plus **intuitive** — la première question de tout stakeholder
- Facile à communiquer : "notre modèle est juste dans 96% des cas"

> Simple, parlante... mais **trompeuse** dans certains cas. Voir la slide suivante.

<small>Source : [stratusdata.io](https://stratusdata.io/gone-fishing-4-metrics-for-evaluating-binary-classifiers/)</small>

![bg right:45% contain](assets/eval/accuracy.png)

---

# 03 — Le piège de l'Accuracy

- **Scanner d'aéroport** : détecter 10 bagages suspects sur 10 000
- Un modèle qui dit "tous les bagages sont OK" → **99,9% d'Accuracy**
- Mais il a raté **100%** des vrais positifs — Recall = **0%**

| Modèle | Accuracy | Recall |
|---|---|---|
| Prédit toujours "OK" | 99,9% | **0%** |
| Modèle entraîné | 97% | **85%** |

> L'Accuracy ment sur les datasets déséquilibrés. Toujours vérifier le Recall sur la classe rare.

---

<!-- _class: img-right -->

# 04 — Precision

- **Precision** = TP / (TP + FP)
- "Parmi mes alertes, combien sont vraies ?"
- Coût FP élevé → maximiser Precision
- Ex. : filtre anti-spam, justice pénale

> Le **filet du pêcheur** : quel % de la prise est du thon ?

<small>Source : [stratusdata.io](https://stratusdata.io/gone-fishing-4-metrics-for-evaluating-binary-classifiers/)</small>

![bg right:45% contain](assets/eval/precision.png)

---

<!-- _class: img-right -->

# 05 — Recall

- **Recall** = TP / (TP + FN)
- "Parmi les vrais cas, combien ai-je détectés ?"
- Coût FN élevé → maximiser Recall
- Ex. : dépistage cancer, détection de fraude

> Le **scanner médical** : combien de malades repérés ?

<small>Source : [stratusdata.io](https://stratusdata.io/gone-fishing-4-metrics-for-evaluating-binary-classifiers/)</small>

![bg right:45% contain](assets/eval/recall.png)

---

# 06 — F1-Score : le compromis en un chiffre

![w:500](assets/eval/f1-equation.png)

- **Moyenne harmonique** de Precision et Recall
- Pénalise les écarts : Precision = 90%, Recall = 10% → F1 = **18%** (pas 50%)
- Le trade-off est une **bascule** — impossible de maximiser les deux
- Le choix du point d'équilibre est une **décision business**, pas technique

> Quand vous hésitez, le F1 est votre **meilleur choix par défaut**.

---

# 07 — Classification : quand choisir quoi

1. **Classes équilibrées ?** → Accuracy + F1 suffisent
2. **Classe positive rare (< 10%) ?** → F1 ou Recall en priorité
3. **Quel type d'erreur coûte le plus ?**
   - FP coûteux → maximiser **Precision**
   - FN coûteux → maximiser **Recall**

> **En cas de doute** : le F1-Score est le meilleur choix par défaut — une seule métrique claire, facile à optimiser.

---

<!-- _class: section -->

# Régression

## De combien le modèle se trompe-t-il ?

---

<!-- _class: img-right -->

# 08 — MAE (Mean Absolute Error)

- **MAE = |y − ŷ|**
- Moyenne des écarts absolus
- Même unité que la cible (€, min)
- **Robuste** aux outliers
- Idéal pour communiquer aux stakeholders

> "Nos prédictions dévient de €10k en moyenne."

<small>Source : [Medium](https://miro.medium.com/v2/resize:fit:1200/0*s6YGm5hBneEVNc7U.jpg)</small>

![bg right:45% contain](assets/eval/mae.jpg)

---

<!-- _class: img-right -->

# 09 — MSE (Mean Squared Error)

- **MSE = (y − ŷ)²**
- Pénalise les **grosses erreurs** (carré)
- Erreur de 10 contribue **100×** plus qu'une erreur de 1
- Si √MSE >> MAE → quelques prédictions catastrophiques

> Détection de prédictions catastrophiques : comparez √MSE et MAE.

<small>Source : [byam.github.io](https://byam.github.io/assets/img/model-eval-val/mean-squared-error.png)</small>

![bg right:45% contain](assets/eval/mse.png)

---

<!-- _class: section -->

# Computer Vision

## IoU et détection d'objets

---

<!-- _class: img-right -->

# 10 — IoU : la brique de la Computer Vision

- **IoU** (Intersection over Union) = chevauchement prédiction vs réalité
- Score de 0 (aucun overlap) à 1 (match parfait)
- Détection = **TP** si IoU > seuil, sinon **FP** ; objet manqué → **FN**
- **mAP** = Average Precision moyenné sur toutes les classes
- Standard COCO : mAP@[.5:.95]

> L'IoU est la brique fondamentale — détection, segmentation et tracking.

![bg vertical right:50% contain](assets/eval/iou-illustration.png)
![bg contain](assets/eval/iou-birds.jpg)

---

<!-- _class: section -->

# LLM Evaluation

## Benchmarks, classements et pricing

---

<!-- _class: compact-table -->

# 11 — Benchmarks : les examens standardisés des LLMs

| Benchmark | Teste | Leader | Score |
|---|---|---|---|
| **MMLU-Pro** | 57 matières, QCM avancé | Gemini 3 Pro | **89,8%** |
| **SWE-bench** | Vrais bugs GitHub | Claude Opus 4.5 | **80,9%** |
| **ARC-AGI 2** | Raisonnement abstrait | GPT-5.2 | **~54%** |
| **Humanity's Last Exam** | 2 500 questions experts | Gemini 3.1 Pro | **44,7%** |

- ARC-AGI 2 : baseline humain = **60%** — les frontier s'en approchent
- HLE : passé de **<10% à ~45%** en un an — le benchmark le plus discriminant [1]

> MMLU est le "BAC des LLMs" — ARC-AGI 2 et HLE testent ce que MMLU ne mesure pas.

<small>Sources : [1] [Scale AI SEAL](https://scale.com/leaderboard/humanitys_last_exam) · [ARC Prize](https://arcprize.org/leaderboard) · [Epoch AI](https://epoch.ai/benchmarks/swe-bench-verified)</small>

---

# 12 — Chatbot Arena : le vote humain

- Deux modèles anonymes répondent → l'utilisateur vote pour le meilleur
- Système **Elo** (comme aux échecs) : **6M+ votes** en A/B testing aveugle [1]

| Rang | Modèle | Elo |
|---|---|---|
| 1 | Claude Opus 4.6 Thinking | 1 503 |
| 2 | Gemini 3.1 Pro | 1 500 |
| 3 | Grok 4.20 | 1 495 |

> **Bémol** : les grands labos testent des versions privées et reçoivent ~20% du feedback chacun — les modèles open-weights < 30% au total [2]

<small>Sources : [1] [LM Arena](https://arena.ai/leaderboard) · [2] [Hackster.io](https://www.hackster.io/news/chatbot-arena-shenanigans-09bd3fa3e6fa)</small>

---

# 13 — Il n'y a pas de meilleur modèle

- Across **20 benchmarks** indépendants, aucun modèle ne domine tout [1]
- Chaque famille excelle dans un domaine différent :

| Domaine | Leader | Benchmark |
|---|---|---|
| Vision & raisonnement | **Gemini** | HLE, GPQA, GeoBench |
| Agentic & coding | **Claude** | SWE-bench, METR, WebDev |
| Maths & optimisation | **GPT** | OTIS AIME, GSO, FrontierMath |

- Les scores sont **évalués par des tiers** (Epoch AI, Scale AI) — pas par les labos eux-mêmes
- Pour un entrepreneur : le "meilleur modèle" dépend de **votre cas d'usage**

> Ne demandez pas "quel est le meilleur LLM ?" — demandez "quel LLM est le meilleur **pour ma tâche** ?"

<small>Sources : [1] [LM Council](https://lmcouncil.ai/benchmarks)</small>

---

# 14 — ECI : l'accélération s'accélère

- L'**Epoch Capabilities Index** agrège **37 benchmarks** en un score unique — un QI pour les modèles [1]
- Résultat clé : la progression a **doublé** depuis avril 2024

| Période | Rythme | Facteur |
|---|---|---|
| Avant avril 2024 | ~8 points ECI/an | Baseline |
| Après avril 2024 | ~15 points ECI/an | **~2× plus rapide** |

- Coïncide avec les Reasoning Models (o1, DeepSeek-R1)
- **Implication business** : des capacités prévues dans 2–3 ans arrivent en 1–1,5 an

> L'IA ne ralentit pas — elle accélère. Le calcul "attendre vs. investir" a changé.

<small>Sources : [1] [Epoch AI — ECI](https://epoch.ai/benchmarks/eci)</small>

---

# 15 — GDPval : de la performance au business

- **1 320 tâches réelles**, 44 métiers, 9 secteurs du PIB américain [1]
- Modèles frontier : **100× plus rapides** et **100× moins chers** que les experts

| Dimension | IA Frontier | Experts humains |
|---|---|---|
| Vitesse | ~100× plus rapide | Baseline |
| Coût | ~100× moins cher | Baseline |
| Qualité (win rate) | **35–44%** | 56–65% |

- Le **"production tax"** : égaler l'humain ne suffit pas, il faut le **dépasser** nettement

> Rapide et pas cher ≠ déployable. Les benchmarks ne prédisent pas le remplacement d'emplois.

<small>Sources : [1] [OpenAI — GDPval](https://evals.openai.com/gdpval/leaderboard) · [LM Council](https://lmcouncil.ai/benchmarks)</small>

---

# 16 — Pricing LLM : 1 000× d'écart

| Modèle | Input/1M | Output/1M | Elo | Tier |
|---|---|---|---|---|
| **DeepSeek V3.2** | $0,27 | $0,42 | 1 361 | Budget |
| **Gemini 2.5 Flash** | $0,15 | $0,60 | 1 335 | Budget |
| **Claude Opus 4.6** | $5,00 | $25,00 | 1 503 | Premium |
| **GPT-5.2 Pro** | $21,00 | $168,00 | — | Ultra |

- Coût niveau GPT-4 : **-98%** depuis 2023 — de $60 à $0,75/M tokens [1]
- Baisse médiane : **50×/an** tous benchmarks confondus [2]

> **Règle des 90/10** : 90% de vos requêtes sur un modèle budget, 10% critiques sur premium.

<small>Sources : [1] [CloudIDR](https://www.cloudidr.com/blog/llm-pricing-comparison-2026) · [2] [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends)</small>

---

# 17 — Key Takeaways

1. **Classification** : l'Accuracy ment sur les datasets déséquilibrés — le F1 est votre meilleur choix par défaut

2. **Régression** : MAE pour communiquer, MSE pour détecter les prédictions catastrophiques — toujours les deux ensemble

3. **Computer Vision** : l'IoU est la brique fondamentale de la détection et de la segmentation

4. **LLMs** : il n'y a pas de "meilleur modèle" — choisissez par **tâche**, pas par leaderboard

5. **Accélération** : le rythme de progrès a **doublé** — vos plans IA à 3 ans sont déjà obsolètes

6. **Pricing** : la déflation à 50×/an rend les modèles premium d'hier accessibles — commencez maintenant

> **Pour aller plus loin** : les 4 decks de référence complets sont disponibles dans `slides/evaluation/`.
