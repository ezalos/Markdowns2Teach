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

# 01 — La Confusion Matrix

- Le modèle produit une **prédiction** (Positive ou Negative)
- La réalité est le **ground truth** (Positive ou Negative)
- Le croisement donne **4 cas** :

| | Prédit Positive | Prédit Negative |
|---|---|---|
| **Réel Positive** | True Positive (TP) | False Negative (FN) |
| **Réel Negative** | False Positive (FP) | True Negative (TN) |

> **Mnémotechnique** : le 2e mot = réponse du modèle, le 1er mot = avait-il raison ?

---

# 02 — Accuracy et son piège

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)
- Intuition : "sur 100 cas, combien le modèle a-t-il correctement classés ?"
- **Le piège du 99/1** : dataset avec 99% classe A, 1% classe B
- Un modèle qui prédit toujours "A" obtient **99% d'Accuracy** mais Recall = 0%

| Modèle | Accuracy | Recall classe B |
|---|---|---|
| Prédit toujours "A" | 99% | **0%** |
| Modèle entraîné | 96% | **78%** |

> L'Accuracy ment sur les datasets déséquilibrés. Le 2e modèle est bien meilleur.

---

<!-- _class: cols -->

# 03 — Precision vs Recall

<div class="left">

**Precision** = TP / (TP + FP)
- "Parmi mes alertes, combien sont vraies ?"
- Coût FP élevé → maximiser Precision
- Ex. : filtre anti-spam, justice pénale

> Le **filet du pêcheur** : quel % de la prise est du thon ?

</div>
<div class="right">

**Recall** = TP / (TP + FN)
- "Parmi les vrais cas, combien ai-je détectés ?"
- Coût FN élevé → maximiser Recall
- Ex. : dépistage cancer, détection de fraude

> Le **scanner médical** : combien de malades repérés ?

</div>

---

# 04 — F1-Score : le compromis en un chiffre

- **Moyenne harmonique** de Precision et Recall
- **Formule** : F1 = 2 × (Precision × Recall) / (Precision + Recall)
- La moyenne harmonique **pénalise les écarts** :
  - Precision = 90%, Recall = 10% → F1 = **18%** (pas 50%)
- Le trade-off Precision/Recall est une **bascule** — impossible de maximiser les deux
- Le choix du point d'équilibre est une **décision business**, pas technique

> Le F1 est votre "note globale" quand Precision et Recall comptent autant.

---

# 05 — Classification : arbre de décision

1. **Classes équilibrées ?** → Oui : Accuracy + F1 suffisent
2. **Classe positive rare (< 10%) ?** → PR-AUC + F2 ou MCC
3. **Quel type d'erreur coûte le plus ?** → FP : Precision · FN : Recall
4. **Besoin d'un score unique ?** → MCC (binaire) ou Macro-F1 (multi-class)
5. **Besoin de probabilités calibrées ?** → Log Loss

> Ne reportez jamais **une seule métrique**. La Confusion Matrix + 2-3 scores donne une image complète.

---

<!-- _class: section -->

# Régression

## De combien le modèle se trompe-t-il ?

---

<!-- _class: cols -->

# 06 — MAE vs RMSE

<div class="left">

**MAE** (Mean Absolute Error)
- Moyenne des écarts absolus
- Même unité que la cible (€, min)
- **Robuste** aux outliers
- Idéal pour communiquer aux stakeholders

> "Nos prédictions dévient de €10k en moyenne."

</div>
<div class="right">

**RMSE** (Root Mean Squared Error)
- Pénalise les **grosses erreurs** (carré)
- Erreur de 10 contribue **25×** plus qu'une erreur de 2
- Si RMSE >> MAE → quelques prédictions catastrophiques

> Métrique par défaut des compétitions ML.

</div>

---

# 07 — R² et arbre de décision régression

- **R²** = 1 − (SS_res / SS_tot) — "le modèle explique **X%** de la variance"
- Plage : −∞ à 1 (1 = parfait, 0 = aussi bien que la moyenne, < 0 = pire)
- **Piège** : R² augmente en ajoutant des variables — même aléatoires → utiliser **Adjusted R²** [1]
- **Arbre de décision** pour choisir la bonne métrique :
  - Grosses erreurs catastrophiques ? → RMSE · Sinon → MAE
  - Données bruitées avec outliers ? → Huber Loss
  - Besoin d'un intervalle ? → Quantile Loss

> R² dit *à quel point* le modèle est bon. MAE/RMSE disent *de combien* il se trompe. Toujours utiliser les deux.

<small>Sources : [1] [Anscombe 1973, American Statistician](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)</small>

---

<!-- _class: section -->

# Computer Vision

## IoU, détection et segmentation

---

# 08 — IoU et mAP : détecter des objets

- **IoU** (Intersection over Union) = chevauchement entre prédiction et réalité (0 → 1)
- Une détection est un **TP** si IoU > seuil, sinon **FP** ; objet manqué → **FN**
- **mAP** = moyenne de l'Average Precision sur toutes les classes

| Variante | Seuil IoU | Usage |
|---|---|---|
| AP@50 | 0.5 (tolérant) | Comptage, tri |
| AP@75 | 0.75 (exigeant) | Robotique, précision spatiale |
| mAP@[.5:.95] | Moyenne 0.5 à 0.95 | Standard industriel (COCO) |

> L'IoU est la brique fondamentale de toute la Computer Vision — détection, segmentation et tracking.

---

<!-- _class: cols -->

# 09 — Segmentation : mIoU et Dice

<div class="left">

**mIoU** (mean IoU)
- IoU calculé **par classe**, puis moyenné
- Chaque classe pèse autant, même les rares
- Standard pour la Semantic Segmentation
- SOTA ADE20K : **63,6% mIoU** [1]

</div>
<div class="right">

**Dice Coefficient**
- Dice = 2 × |A ∩ B| / (|A| + |B|)
- Aussi appelé F1 au niveau pixel
- Référence en **imagerie médicale**
- Dice > 0.90 exigé pour la validation clinique

</div>

> Pixel Accuracy est trompeuse (95% du fond = 95% Accuracy). mIoU et Dice sont les vraies métriques.

<small>Sources : [1] [arXiv:2505.19795](https://arxiv.org/html/2505.19795v1)</small>

---

<!-- _class: section -->

# LLM Evaluation

## Benchmarks, classements et pricing

---

# 10 — Benchmarks : les examens standardisés des LLMs

- Un benchmark est un **examen standardisé** — même épreuve, correction uniforme
- **MMLU** : 57 matières, 16 000+ QCM — SOTA : **GPT-5.3 Codex — 93%** [1][2]
- **GSM8K** : problèmes de maths CM2/collège — saturé à 95%+ [3]
- **HumanEval** : génération de code Python — saturé à 99% [3]
- **SWE-bench** : résolution de vrais bugs GitHub — le vrai test code [3]
- Un bon benchmark ne garantit pas la performance sur **votre tâche**

> MMLU est le "BAC des LLMs" — indispensable mais insuffisant seul.

<small>Sources : [1] [Hendrycks et al., ICLR 2021](https://arxiv.org/abs/2009.03300) · [2] [LXT.ai](https://www.lxt.ai/blog/llm-benchmarks/) · [3] [Stanford HAI 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 11 — Chatbot Arena : le vote humain

- Deux modèles anonymes répondent → l'utilisateur vote pour le meilleur
- Système **Elo** (comme aux échecs) : chaque victoire ajuste les scores
- **6M+ votes** en A/B testing aveugle — la référence pour la préférence humaine [1]
- **Top 3 (fév. 2026)** :

| Rang | Modèle | Elo |
|---|---|---|
| 1 | Claude Opus 4.6 Thinking | 1 503 |
| 2 | Gemini 3.1 Pro | 1 500 |
| 3 | Grok 4.20 | 1 495 |

> Les benchmarks automatiques mesurent la **capacité**. L'Arena mesure la **préférence** humaine.

<small>Sources : [1] [LM Arena](https://arena.ai/leaderboard) (fév. 2026)</small>

---

# 12 — Pricing LLM : 1 000× d'écart

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

# 13 — Key Takeaways

1. **Classification** : l'Accuracy ment sur les datasets déséquilibrés — le F1 et la Confusion Matrix sont vos alliés

2. **Régression** : MAE pour communiquer, RMSE pour les systèmes critiques, R² pour le pouvoir explicatif — jamais une seule métrique

3. **Computer Vision** : l'IoU est la brique fondamentale ; mIoU et Dice révèlent ce que la Pixel Accuracy masque

4. **LLMs** : les benchmarks (MMLU, Arena) sont des indicateurs — le vrai test est sur **vos propres données**

5. **Pricing** : la déflation à 50×/an rend les modèles premium d'hier accessibles — choisissez par **cas d'usage**, pas par leaderboard

> **Pour aller plus loin** : les 4 decks de référence complets sont disponibles dans `slides/evaluation/`.
