---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Évaluation · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche Evaluation Metrics 2024–2026 · Données publiques"
---

<!-- ABOUTME: Métriques d'évaluation pour la Classification — de la Confusion Matrix au MCC, en passant par les courbes et le multi-class. -->
<!-- ABOUTME: Deck de référence pour étudiants M2 non-ingénieurs, complément aux notebooks interactifs Jupyter. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Évaluer une Classification

## Au-delà de l'Accuracy

Deep Tech & ML (UE3) · Évaluation
M2 IMT&E · Paris 1 Panthéon-Sorbonne

---

<!-- _class: section -->

# Confusion Matrix

## La base de toute évaluation

---

# 01 — Rappel : TP, TN, FP, FN

- Le modèle produit une **prédiction** (Positive ou Negative)
- La réalité est le **ground truth** (Positive ou Negative)
- Le croisement donne **4 cas** :

| | Prédit Positive | Prédit Negative |
|---|---|---|
| **Réel Positive** | True Positive (TP) | False Negative (FN) |
| **Réel Negative** | False Positive (FP) | True Negative (TN) |

> **Mnémotechnique** : le 2e mot = réponse du modèle, le 1er mot = avait-il raison ?

![bg right:35%](assets/infographics/confusion-matrix_run_20260301_174305_3b3c59.png)

<!-- PB: 2x2 confusion matrix with color coding: green for TP/TN, red for FP/FN, with the mnemonic rule annotated -->

---

# 02 — Confusion Matrix multi-class

- En multi-class, la matrice est **NxN** (une ligne/colonne par classe)
- La diagonale = prédictions correctes
- Les cellules hors-diagonale révèlent les **confusions systématiques**

| | Prédit Chat | Prédit Chien | Prédit Oiseau | Prédit Poisson |
|---|:---:|:---:|:---:|:---:|
| **Chat** | **42** | 5 | 2 | 1 |
| **Chien** | 8 | **35** | 4 | 3 |
| **Oiseau** | 1 | 2 | **44** | 3 |
| **Poisson** | 0 | 1 | 6 | **43** |

> Le modèle confond souvent Oiseau et Poisson — un pattern que l'Accuracy globale masque.


---

<!-- _class: section -->

# Basic Metrics

## Les métriques que vous connaissez (et leurs pièges)

---

# 03 — Accuracy : qu'est-ce que c'est ?

- **Définition** : proportion de prédictions correctes parmi toutes les prédictions
- **Formule** : Accuracy = (TP + TN) / (TP + TN + FP + FN)
- Intuition : "sur 100 passagers scannés, combien ont été correctement identifiés ?"

> Pensez au **scanner d'aéroport** : il doit identifier les objets dangereux parmi des milliers de bagages inoffensifs.


---

# 04 — Accuracy : quand l'utiliser ?

- Pertinente quand les classes sont **équilibrées** (~50/50)
- Exemples adaptés :
  - Classification de sentiments (positif / négatif) — souvent ~50/50
  - Prédiction de match sportif (victoire / défaite)
  - Test A/B : conversion oui / non

> L'Accuracy est fiable quand **chaque classe a un poids similaire** dans votre business.


---

# 05 — Accuracy : les limites

- **Le piège du 99/1** : dataset avec 99% classe A, 1% classe B
- Un modèle qui prédit toujours "A" obtient **99% d'Accuracy**
- Mais il n'a **jamais détecté** un seul cas de classe B (Recall = 0%)

| Modèle | Accuracy | Recall classe B |
|---|---|---|
| Prédit toujours "A" | 99% | **0%** |
| Modèle entraîné | 96% | **78%** |

> Le 2e modèle est bien meilleur malgré une Accuracy plus basse.

![bg right:35%](assets/infographics/accuracy-imbalance-trap_run_20260301_174359_8dc3a7.png)

<!-- PB: 99 blue dots and 1 red dot, model says "all blue" with 99% badge but a big red X on the missed red dot -->

---

# 06 — Precision : qu'est-ce que c'est ?

- **Définition** : parmi les prédictions Positive, combien sont vraiment Positive ?
- **Formule** : Precision = TP / (TP + FP)
- Intuition : "dans mon filet, quel % est du thon (et pas des dauphins) ?"

> Le **filet du pêcheur** : la Precision mesure la pureté de votre prise.

![bg right:40%](assets/infographics/precision-visual_run_20260301_174457_2ac3b1.png)

<!-- PB: Fisherman's net with tuna (TP) and dolphins (FP) caught, formula showing Precision = tuna / total catch -->

---

# 07 — Precision : quand l'utiliser ?

- Quand le coût d'un **False Positive est élevé** :
  - **Filtre anti-spam** : bloquer un vrai email = perte de business
  - **Justice pénale** : condamner un innocent est inacceptable
  - **Recommandation produit** : suggestion absurde = perte de crédibilité
  - **Email marketing** : trop de messages non pertinents = désabonnement

> Maximiser la Precision = "je préfère rater des cas que de lancer de fausses alertes."


---

# 08 — Precision : les limites

- **Aveugle aux False Negatives** : elle ignore ce que le modèle a manqué
- **Piège de la prédiction unique** : si le modèle ne prédit "Positive" qu'une seule fois et a raison → Precision = 100%
- Mais il a manqué des centaines de vrais cas

| Modèle | Prédictions Pos. | TP | FP | Precision | Recall |
|---|:---:|:---:|:---:|:---:|:---:|
| Ultra-prudent | 1 | 1 | 0 | **100%** | **1%** |
| Équilibré | 80 | 60 | 20 | 75% | 60% |

> Une Precision de 100% n'a aucune valeur si le Recall est catastrophique.

![bg right:30%](assets/infographics/precision-failure_run_20260301_174457_4ced45.png)

<!-- PB: Single fish in a tiny net with "100% precision" badge, next to a sea full of uncaught fish -->

---

# 09 — Recall : qu'est-ce que c'est ?

- **Définition** : parmi tous les vrais Positives, combien le modèle a-t-il détectés ?
- **Formule** : Recall = TP / (TP + FN)
- Intuition : "sur tous les patients malades, combien le test a-t-il repérés ?"

> Le **dépistage du cancer** : le Recall mesure votre capacité à ne rater aucun malade.

![bg right:40%](assets/infographics/recall-visual_run_20260301_174457_b5c74d.png)

<!-- PB: Hospital screening room with patients — detected patients (TP) highlighted, missed patients (FN) in shadow, formula overlay -->

---

# 10 — Recall : quand l'utiliser ?

- Quand le coût d'un **False Negative est élevé** :
  - **Dépistage médical** : rater un cancer = risque vital
  - **Détection de fraude** : laisser passer une fraude = perte financière
  - **Sécurité aérienne** : manquer un objet dangereux = catastrophe
  - **Détection d'intrusion** : ignorer une attaque = faille critique

> Maximiser le Recall = "je préfère trop d'alertes que de rater un seul vrai cas."


---

# 11 — Recall : les limites

- **Aveugle aux False Positives** : il ignore les fausses alertes
- **Piège du "tout Positive"** : prédire toujours Positive → Recall = 100%
- Mais la Precision s'effondre (le modèle crie "au feu" en permanence)

| Modèle | Prédictions Pos. | TP | FN | Recall | Precision |
|---|:---:|:---:|:---:|:---:|:---:|
| Tout Positive | 1000 | 50 | 0 | **100%** | **5%** |
| Équilibré | 80 | 40 | 10 | 80% | 50% |

> Un Recall de 100% n'a aucune valeur si la Precision est catastrophique.

![bg right:30%](assets/infographics/recall-failure_run_20260301_174457_ef4426.png)

<!-- PB: Fire alarm ringing constantly with "100% recall" badge, exhausted firefighters responding to false alarms -->

---

# 12 — Le Trade-off Precision-Recall

- **Tension fondamentale** : monter l'un fait baisser l'autre
- En ajustant le Decision Threshold :
  - Seuil **bas** (0.2) → + Recall, - Precision (plus d'alertes, plus de faux positifs)
  - Seuil **haut** (0.8) → + Precision, - Recall (moins d'alertes, plus de cas manqués)
- C'est une **bascule** (seesaw) — impossible de maximiser les deux

> Le choix du point d'équilibre est une **décision business**, pas technique.

![bg right:40%](assets/infographics/precision-recall-tradeoff_run_20260301_174457_f4e6ea.png)

<!-- PB: Seesaw/balance with Precision on one side and Recall on the other, threshold slider below controlling the tilt -->

---

# 13 — Discussion : Spam vs Cancer

> Vous êtes CTO et devez configurer le seuil de deux modèles pour votre startup :
> **Modèle A** — filtre anti-spam pour un client email.
> **Modèle B** — dépistage préliminaire de mélanomes pour une app de télé-dermatologie.

**Questions pour la classe** :
- Pour chaque modèle, quelle erreur est la plus coûteuse : FP ou FN ?
- Quel compromis Precision/Recall privilégiez-vous dans chaque cas ?
- Un investisseur vous demande "quelle est la performance de votre modèle ?" — quelle métrique communiquez-vous pour chaque produit ?

---

<!-- _class: section -->

# Advanced Metrics

## Au-delà de Precision et Recall

---

# 14 — F1-Score : le compromis en un chiffre

- **Définition** : moyenne harmonique de Precision et Recall
- **Formule** : F1 = 2 × (Precision × Recall) / (Precision + Recall)
- La moyenne harmonique **pénalise les écarts** : si l'un est bas, le F1 chute
- Exemple : Precision = 90%, Recall = 10% → F1 = **18%** (pas 50%)

> Le F1 est votre "note globale" quand Precision et Recall comptent autant.

![bg right:40%](assets/infographics/f1-harmonic-mean_run_20260301_174458_2e972d.png)

<!-- PB: Venn diagram of Precision and Recall with F1 at the intersection, showing how the harmonic mean punishes imbalance -->

---

# 15 — F-beta : ajuster le curseur

- **Formule** : F_β = (1 + β²) × (P × R) / (β² × P + R)
- Le paramètre **β** contrôle l'importance relative du Recall vs Precision :

| β | Effet | Cas d'usage |
|---|---|---|
| β = 0.5 | **Precision-heavy** (Recall compte 2× moins) | Filtre anti-spam, recommandation |
| β = 1 | Équilibré = F1-Score | Usage général |
| β = 2 | **Recall-heavy** (Recall compte 4× plus) | Dépistage médical, fraude |

> **Règle pratique** : β = 2 si rater un cas coûte bien plus cher qu'une fausse alerte.


---

<!-- _class: cols -->

# 16 — Specificity et Balanced Accuracy

<div class="left">

**Specificity** (True Negative Rate) :
- Formule : TNR = TN / (TN + FP)
- "Parmi les vrais Negatives, combien correctement identifiés ?"
- Complément du Recall sur la classe négative

</div>
<div class="right">

**Balanced Accuracy** :
- Formule : BalAcc = (Recall + Specificity) / 2
- Moyenne du Recall par classe
- Insensible au déséquilibre des classes

</div>

> La Specificity répond à : "mon modèle reconnaît-il aussi bien les cas négatifs ?"

---

# 17 — Balanced Accuracy : pourquoi c'est essentiel

- Le cas classique : 95% positifs, 5% négatifs
- Le modèle "tout Positive" obtient Accuracy = 95% mais **BalAcc = 50%**

| Modèle | Accuracy | Recall (Pos.) | Specificity (Neg.) | Balanced Accuracy |
|---|:---:|:---:|:---:|:---:|
| Tout Positive | 95% | 100% | 0% | **50%** |
| Modèle entraîné | 88% | 90% | 70% | **80%** |

> Un gap **Accuracy vs Balanced Accuracy** révèle que le modèle "triche" sur la classe majoritaire.


---

# 18 — MCC : la meilleure métrique binaire ?

- **Matthews Correlation Coefficient** — corrélation entre prédictions et réalité
- **Formule** : MCC = (TP×TN − FP×FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))
- **Range** : de **-1** (désaccord total) à **+1** (prédiction parfaite), **0** = aléatoire
- Utilise **les 4 quadrants** de la Confusion Matrix (seule métrique à le faire)

> Le MCC est le seul score scalaire qui est élevé uniquement quand le modèle performe bien sur les deux classes [1].


<small>Sources : [1] [Chicco & Jurman 2023, BioData Mining](https://pmc.ncbi.nlm.nih.gov/articles/PMC9938573/)</small>

---

# 19 — MCC : pourquoi les chercheurs le recommandent

- Chicco & Jurman (2020, 2023) démontrent que le MCC devrait remplacer le ROC-AUC comme métrique standard [1]
- **Avantages** sur les autres métriques :
  - Pas trompeur sur données déséquilibrées (contrairement à l'Accuracy)
  - Considère les 4 cases (contrairement à F1 qui ignore les TN)
  - Corrélation statistique interprétable (comme un coefficient de Pearson)
- **Limite** : ne dit pas *pourquoi* la classification échoue — combiner avec les 4 rates

> Quand vous ne pouvez reporter qu'**un seul chiffre** pour un classifieur binaire, choisissez le MCC [1].

<small>Sources : [1] [Chicco & Jurman 2023, BioData Mining](https://pmc.ncbi.nlm.nih.gov/articles/PMC9938573/)</small>

![bg right:30%](assets/infographics/mcc-vs-f1_run_20260301_174458_d9fee6.png)

<!-- PB: Comparison table showing MCC vs Accuracy vs F1 vs ROC-AUC, with checkmarks for properties like "uses all 4 quadrants", "handles imbalance" -->

---

# 20 — Log Loss : la qualité de la confiance

- **Définition** : mesure la qualité des **probabilités** prédites, pas juste la classe
- **Formule** : LogLoss = −(1/N) × Σ [yᵢ·log(pᵢ) + (1−yᵢ)·log(1−pᵢ)]
- Pénalise **exponentiellement** les prédictions confiantes mais fausses
- Un modèle qui prédit 0.99 pour un cas négatif est **lourdement puni**

| Prédiction | Réalité | Log Loss contribution |
|:---:|:---:|:---:|
| 0.9 | Positive | **Faible** (bonne confiance) |
| 0.9 | Negative | **Très élevée** (confiance mal placée) |

> Utile quand vous avez besoin de **probabilités calibrées** (scoring crédit, triage médical).

![bg right:30%](assets/infographics/log-loss-penalty_run_20260301_174504_f6539d.png)

<!-- PB: Graph of -log(p) curve showing steep penalty near 0, with two examples: confident-correct (low loss) vs confident-wrong (high loss) -->

---

# 21 — Cohen's Kappa : l'accord ajusté par le hasard

- **Définition** : mesure l'accord entre prédictions et réalité, corrigé par le hasard
- **Formule** : κ = (pₒ − pₑ) / (1 − pₑ) où pₒ = accord observé, pₑ = accord attendu par hasard
- **Interprétation** (échelle de Landis & Koch) [1] :

| κ | Interprétation |
|---|---|
| < 0.20 | Faible |
| 0.21 – 0.40 | Acceptable |
| 0.41 – 0.60 | Modéré |
| 0.61 – 0.80 | Substantiel |
| 0.81 – 1.00 | Quasi-parfait |

> Un modèle à 80% d'Accuracy sur un dataset 80/20 a un κ faible — il ne fait guère mieux que le hasard.

<small>Sources : [1] [Landis & Koch 1977, via Wikipedia](https://en.wikipedia.org/wiki/Cohen%27s_kappa)</small>


---

# 22 — Discussion : quelle métrique communiquer ?

> Votre startup de recrutement IA filtre des CVs pour des grandes entreprises.
> Le DRH de votre client veut **un chiffre** pour évaluer votre outil.
> Votre dataset de test contient 500 CVs dont 50 "profil idéal" (10%).

**Questions pour la classe** :
- L'Accuracy est-elle pertinente avec 90% de négatifs ?
- Communiquez-vous la Precision (peu de candidats à tort) ou le Recall (aucun bon profil manqué) ?
- Un concurrent annonce un MCC de 0.72. Comment l'interprétez-vous ?
- Le DRH comprendra-t-il le MCC ? Comment vulgariser ?

---

<!-- _class: section -->

# Curves & Thresholds

## Visualiser la performance globale

---

# 23 — ROC Curve et ROC-AUC

- La **ROC Curve** trace le True Positive Rate (Recall) vs le False Positive Rate à chaque seuil
- L'**AUC** (Area Under Curve) résume en un chiffre de 0 à 1 :
  - AUC = 0.5 → modèle aléatoire (diagonale)
  - AUC = 0.8 → bon modèle
  - AUC = 1.0 → parfait (suspect en pratique)
- **Avantage** : invariant au déséquilibre des classes [1]

> L'AUC mesure la capacité du modèle à **classer** un positif devant un négatif, quel que soit le seuil choisi.

![bg right:40%](assets/infographics/roc-curve-construction_run_20260301_174506_1da1f1.png)

<!-- PB: ROC curve with diagonal baseline, shaded AUC area, three example curves (bad/good/perfect) -->

<small>Sources : [1] [Bowers & Zhou 2024, Patterns](https://pmc.ncbi.nlm.nih.gov/articles/PMC11240176/)</small>

---

# 24 — PR Curve et PR-AUC

- La **PR Curve** trace Precision vs Recall à chaque seuil
- Le **PR-AUC** est l'aire sous cette courbe
- Mieux adaptée quand la classe positive est **rare** (fraude, maladie)
- Raison : la PR Curve se concentre sur la **classe positive** uniquement

| Aspect | ROC-AUC | PR-AUC |
|---|---|---|
| Influence des TN | Oui (via FPR) | Non |
| Sensible à l'imbalance | Moins | Plus |
| Baseline aléatoire | 0.5 (fixe) | = prévalence de la classe + |

> Si 1% de vos données sont positives, le ROC-AUC peut sembler excellent alors que votre modèle est médiocre sur la classe rare [1].

<small>Sources : [1] [Machine Learning Mastery](https://machinelearningmastery.com/roc-auc-vs-precision-recall-for-imbalanced-data/)</small>

![bg right:30%](assets/infographics/ap-pr-curve_run_20260301_174530_318ee0.png)

<!-- PB: PR curve with shaded area, showing how baseline drops with class imbalance unlike ROC -->

---

<!-- _class: cols -->

# 25 — ROC-AUC vs PR-AUC : même modèle, deux histoires

<div class="left">

**Dataset équilibré (50/50)** :
- ROC-AUC = 0.85, PR-AUC = 0.83
- Les deux racontent la même histoire

</div>
<div class="right">

**Dataset déséquilibré (99/1)** :
- ROC-AUC = 0.85 (inchangé)
- PR-AUC = **0.35** (chute drastique)

</div>

> **Règle** : classe positive < 10% du dataset → reportez le **PR-AUC** en priorité.

![bg right:25%](assets/infographics/roc-vs-pr-imbalance_run_20260301_174509_509209.png)

<!-- PB: Side-by-side comparison: same model evaluated on balanced vs imbalanced data, ROC stays stable while PR drops -->

---

<!-- _class: section -->

# Multi-Class

## Quand il y a plus de deux classes

---

# 26 — Macro, Micro et Weighted Averaging

- En multi-class, chaque classe a sa propre Precision/Recall
- **Comment agréger ?** Trois stratégies :

| Méthode | Calcul | Traite chaque... |
|---|---|---|
| **Macro** | Moyenne des scores par classe | Classe également |
| **Micro** | TP/FP/FN globaux, puis calcul | Instance également |
| **Weighted** | Moyenne pondérée par le support | Classe selon sa taille |

- **Macro** : pénalise si le modèle est mauvais sur une classe minoritaire
- **Micro** : converge vers l'Accuracy en single-label
- **Weighted** : reflète la performance "réelle" sur votre distribution

![bg right:30%](assets/infographics/macro-micro-weighted_run_20260301_174512_750fc7.png)

<!-- PB: Three-panel diagram showing same 3-class results aggregated via macro (equal boxes), micro (merged pool), and weighted (proportional boxes) -->

---

# 27 — Quand les classes n'ont pas le même coût

- En détection de fraude : manquer une fraude de **50 000 EUR** ≠ manquer un achat de **15 EUR**
- Les métriques standard traitent chaque erreur de la même manière
- **Solutions** :
  - **Macro averaging** : force l'attention sur les classes rares
  - **Cost-sensitive learning** : pondérer les erreurs par leur coût business
  - **Class weights** dans sklearn : `class_weight='balanced'`

> Choisissez votre méthode d'averaging en fonction de votre **question business** : toutes les classes comptent-elles autant ?

![bg right:35%](assets/infographics/cost-asymmetry_run_20260301_174516_096e8d.png)

<!-- PB: Two-panel: equal-weight errors (all same size) vs cost-weighted errors (fraud box much larger than legitimate box) -->

---

<!-- _class: section -->

# Synthèse

## Choisir la bonne métrique

---

# 28 — Tableau comparatif des métriques

| Métrique | Range | Gère l'imbalance ? | Utilise les 4 cases ? | Cas d'usage principal |
|---|:---:|:---:|:---:|---|
| Accuracy | [0, 1] | Non | Oui | Datasets équilibrés |
| Precision | [0, 1] | Partiel | Non (ignore TN, FN) | Coût FP élevé |
| Recall | [0, 1] | Partiel | Non (ignore TN, FP) | Coût FN élevé |
| F1 | [0, 1] | Partiel | Non (ignore TN) | Compromis P/R |
| Balanced Acc. | [0, 1] | Oui | Oui | Alternative à Accuracy |
| MCC | [-1, +1] | Oui | **Oui** | Meilleur score unique |
| Cohen's κ | [-1, +1] | Oui | Oui | Accord vs hasard |

---

# 29 — Arbre de décision en 5 questions

1. **Classes équilibrées ?** → Oui : Accuracy + F1 suffisent
2. **Classe positive rare (< 10%) ?** → PR-AUC + F2 ou MCC
3. **Quel type d'erreur coûte le plus ?** → FP : Precision · FN : Recall
4. **Besoin d'un score unique ?** → MCC (binaire) ou Macro-F1 (multi-class)
5. **Besoin de probabilités calibrées ?** → Log Loss

> En pratique, ne reportez jamais **une seule métrique**. La Confusion Matrix + 2-3 scores donne une image complète.

![bg right:35%](assets/infographics/classification-decision-tree_run_20260301_174519_84e0b7.png)

<!-- PB: Flowchart decision tree with 5 yes/no questions leading to recommended metrics at each leaf -->

---

# 30 — Key Takeaways

1. **L'Accuracy ment sur les datasets déséquilibrés** — utilisez la Balanced Accuracy ou le MCC pour un diagnostic fiable

2. **Precision vs Recall est un choix business** — le seuil optimal dépend du coût relatif des FP et FN dans votre domaine

3. **Le MCC est la métrique la plus complète** pour la classification binaire — c'est la seule qui utilise les 4 quadrants de la Confusion Matrix

4. **PR-AUC > ROC-AUC quand la classe positive est rare** — le ROC-AUC peut masquer une performance médiocre sur la classe d'intérêt

5. **Ne reportez jamais une seule métrique** — Confusion Matrix + 2-3 scores complémentaires donnent une image fiable

> **Pour aller plus loin** : explorez les notebooks `01_thresholding.ipynb` et `02_classification_metrics.ipynb` pour manipuler ces métriques interactivement.
