---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Évaluation · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche Evaluation Metrics 2024–2026 · Données publiques"
---

<!-- ABOUTME: Deck de référence sur les métriques d'évaluation de régression : distance, goodness-of-fit et losses robustes. -->
<!-- ABOUTME: Cadré pour étudiants M2 non-ingénieurs, approche business-first avec cas concrets et arbitrages décisionnels. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Évaluer une Régression

## Mesurer l'Erreur pour Prendre les Bonnes Décisions

Deep Tech & ML (UE3) · Évaluation
M2 IMT&E · Paris 1 Panthéon-Sorbonne

---

<!-- _class: section -->

# Introduction

## Quand votre modèle se trompe, de combien se trompe-t-il ?

---

# 01 — Pourquoi mesurer l'erreur de régression ?

- Un modèle prédit le prix de votre appartement à **€380k**. Le vrai prix : **€420k**
- Erreur de **€40k** — est-ce grave ? Ça dépend du contexte business
- **Même erreur, impacts différents** :
  - Pricing immobilier : €40k = marge de négociation normale
  - Dosage médical : 40mg d'écart = danger vital
  - Livraison : 40 min de retard = client perdu
- Les métriques de régression répondent à **trois questions** :
  - Quelle est l'erreur **moyenne** ? (MAE, RMSE)
  - Mon modèle **explique**-t-il la variance ? (R²)
  - Comment gérer les **cas extrêmes** ? (Huber, Quantile)

> Choisir la bonne métrique est une **décision business**, pas technique.

---

<!-- _class: compact compact-table -->

# 02 — Taxonomie des métriques de régression

| Famille | Métriques | Question clé |
|---------|-----------|--------------|
| Distance | MAE, MSE, RMSE, MAPE, SMAPE, MedAE | De combien se trompe-t-on ? |
| Goodness-of-fit | R², Adjusted R² | Le modèle explique-t-il les données ? |
| Losses robustes | Huber, Quantile | Comment gérer bruit et incertitude ? |

- **Distance** : compare prédiction vs réalité
- **Goodness-of-fit** : pouvoir explicatif global
- **Losses robustes** : combinent avantages des deux familles

![bg right:35%](assets/infographics/regression-taxonomy_run_20260301_174302_ecd6e1.png)

<!-- PB: Arbre à 3 branches montrant les 3 familles de métriques (Distance, Goodness-of-fit, Losses robustes) avec les métriques listées sous chaque branche et la question clé associée -->

---

<!-- _class: section -->

# Métriques de Distance

## Mesurer l'écart entre prédiction et réalité

---

<!-- _class: compact -->

# 03 — MAE : la moyenne des erreurs absolues

- **Mean Absolute Error** = moyenne des écarts absolus
- Formule : **MAE = (1/n) Σ |yᵢ − ŷᵢ|**
- Intuition : "en moyenne, le modèle se trompe de X unités"
- **Même unité** que la variable cible (€, minutes, kg)
- Traite toutes les erreurs de manière **égale**
- Facile à expliquer : "nos prédictions dévient de €10k en moyenne"

> La MAE est la métrique la plus **intuitive** pour communiquer avec des stakeholders.

![bg right:35%](assets/infographics/mae-residuals_run_20260301_174313_779eac.png)

<!-- PB: Visualisation de la MAE : axe avec points réels et prédits, flèches montrant les écarts absolus, puis calcul de la moyenne -->

---

# 04 — MAE : quand l'utiliser

- **Immobilier** : MAE de $25k signifie que les prédictions dévient de $25k en moyenne [1]
- **Sales forecasting** : évaluer l'erreur en unités vendues
- **Prévision énergétique** : erreur en kWh directement interprétable
- **Avantage clé** : robuste aux **outliers**
  - Un point aberrant n'explose pas la métrique
  - L'erreur reste linéaire : une erreur de 100 pèse 10× plus qu'une erreur de 10
- Idéal quand toutes les erreurs ont un **coût proportionnel** identique

> **Règle pratique** : si votre stakeholder demande "de combien se trompe le modèle ?", commencez par la MAE.

<small>Sources : [1] [Towards AI](https://towardsai.net/p/artificial-intelligence/the-essential-guide-to-ml-evaluation-metrics-for-regression)</small>


---

<!-- _class: compact -->

# 05 — MAE : limitations

- **Cache les catastrophes** parmi les petites erreurs
  - MAE = 5 min sur 1 000 livraisons, mais 1 client attend **45 min**
- **Non différentiable en zéro** — problème d'optimisation
- **Pas de pondération** — toutes les erreurs comptent pareil
  - €50k d'écart sur €2M = anodin (2,5%)
  - €50k d'écart sur €100k = grave (50%)
- Erreurs catastrophiques → **RMSE** ou **Max Error**
- Vue en pourcentage → **MAPE**

![bg right:35%](assets/infographics/mae-limitations_run_20260301_174316_887b6d.png)

<!-- PB: Exemple visuel : distribution d'erreurs avec MAE identique mais profils très différents — un uniforme, un avec un outlier extrême -->

---

<!-- _class: compact -->

# 06 — MSE & RMSE : pénaliser les grosses erreurs

- **MSE** = (1/n) Σ (yᵢ − ŷᵢ)² · **RMSE** = √MSE (unités de la cible)
- Le **carré** amplifie les grosses erreurs :
  - Erreur de 2 → contribue 4 · Erreur de 10 → **100** (25×)
- RMSE toujours **≥ MAE** — l'écart révèle les outliers [1]
- RMSE ≈ MAE → erreurs uniformes
- RMSE >> MAE → quelques prédictions très mauvaises

<!-- Speaker notes: RMSE est la métrique par défaut dans la majorité des compétitions ML. -->

<small>Sources : [1] [Vital Flux](https://vitalflux.com/mse-vs-rmse-vs-mae-vs-mape-vs-r-squared-when-to-use/)</small>

![bg right:35%](assets/infographics/mse-rmse-amplification_run_20260301_174319_79f468.png)

<!-- PB: Schéma montrant comment le carré amplifie les erreurs : barres d'erreur linéaires vs barres d'erreur au carré, avec RMSE = racine -->

---

# 07 — MSE & RMSE : quand l'utiliser

- **Dosage médical** : une erreur de 50mg est bien plus dangereuse qu'une de 5mg [1]
- **Ingénierie structurelle** : une sous-estimation de charge peut provoquer un effondrement
- **Finance** : les grosses erreurs de prédiction de stock coûtent exponentiellement plus [2]
- RMSE préféré au MSE car **même unité** que la cible
  - MSE en mg² n'est pas interprétable
  - RMSE en mg a du sens
- Idéal quand les **grosses erreurs sont catastrophiques**
- Utilisez RMSE pour comparer des modèles à **même échelle**

<small>Sources : [1] [Medium](https://medium.com/@duygujones/evaluation-metrics-for-regression-models-a-practical-guide-3e5d27ef628c) · [2] [CodeSignal](https://codesignal.com/learn/courses/deep-dive-into-regression-and-classification-metrics/lessons/understanding-mse-mae-rmse-and-their-differences)</small>


---

<!-- _class: compact -->

# 08 — MSE & RMSE : limitations

- **Sensible aux outliers** — 1 point aberrant domine la métrique
  - 999 parfaites + 1 erreur de 1 000 → RMSE ≈ 31,6
- **MSE** : unité au carré (€², min²) — pas interprétable
- **RMSE** : masque la distribution des erreurs
  - RMSE = 20 → "tout à 20" ou "moitié à 0, moitié à 28"
- **Non robuste** face au bruit d'entraînement
- Données bruitées avec outliers → **Huber Loss**

![bg right:35%](assets/infographics/rmse-outlier-sensitivity_run_20260301_174325_10234b.png)

<!-- PB: Exemple d'un seul outlier qui fait exploser le RMSE : graphique avant/après avec et sans outlier -->

---

# 09 — MAPE : l'erreur en pourcentage

- **Mean Absolute Percentage Error** = (1/n) Σ |yᵢ − ŷᵢ| / |yᵢ| × 100
- Exprime l'erreur comme un **pourcentage** de la valeur réelle
- **Indépendant de l'échelle** — compare des modèles sur des datasets différents
- Interprétation directe : "le modèle se trompe de **7% en moyenne**" [1]
- Très utilisée en **prévision des ventes**, **cash flow**, **projections financières**
- Un MAPE < 10% est généralement considéré comme excellent en forecasting

> Le MAPE parle le langage du **business** : des pourcentages, pas des unités techniques.

<small>Sources : [1] [Jonatasv/Medium](https://medium.com/@jonatasv/metrics-evaluation-mse-rmse-mae-and-mape-317cab85a26b)</small>


---

<!-- _class: compact -->

# 10 — MAPE : limitations critiques

- **Division par zéro** : si yᵢ = 0, MAPE est **indéfinie**
  - Ventes nulles un dimanche, demande nulle en basse saison
- **Asymétrie** : pénalise davantage les **sur-estimations**
  - Prédire 150 pour 100 → 50% · Prédire 50 pour 100 → 50%
  - Mais prédire 200 pour 100 → 100% · 0 pour 100 → 100%
  - Sous-estimation plafonnée à 100%, sur-estimation → ∞

![bg right:35%](assets/infographics/mape-division-by-zero_run_20260301_174327_6191b3.png)

<!-- PB: Schéma montrant l'asymétrie du MAPE : sur-estimation vs sous-estimation avec le même écart absolu -->

---

<!-- _class: compact -->

# 10b — MAPE : limitations critiques (suite)

- **Favorise les modèles qui sous-estiment** — biais systématique [1]
- **Petites valeurs** : erreur de 1 sur réel de 2 = 50%, mais 1 sur 1 000 = 0,1%
- Le MAPE est **instable** quand les valeurs cibles sont proches de zéro

> Si vos données contiennent des zéros ou de petites valeurs, évitez le MAPE.

<small>Sources : [1] [NVIDIA Developer](https://developer.nvidia.com/blog/a-comprehensive-overview-of-regression-evaluation-metrics/)</small>

---

<!-- _class: cols -->

# 11 — SMAPE & MedAE : alternatives robustes

<div class="left">

**SMAPE** (Symmetric MAPE)
- Corrige l'**asymétrie** du MAPE
- Bornée entre 0% et 200%
- Standard de la **M4 Competition** [1]

</div>
<div class="right">

**MedAE** (Median Absolute Error)
- Médiane des erreurs absolues
- **Immunisée** contre les outliers
- Idéale pour les données bruitées

</div>

<small>Sources : [1] [Towards AI](https://towardsai.net/p/artificial-intelligence/the-essential-guide-to-ml-evaluation-metrics-for-regression)</small>

<!-- PB: Côte à côte : SMAPE corrige l'asymétrie MAPE (gauche), MedAE ignore les outliers (droite) -->

---

# 12 — Max Error : le pire scénario

- **Max Error** = max |yᵢ − ŷᵢ| — la plus grande erreur sur l'ensemble du dataset
- Répond à : "dans le **pire des cas**, de combien le modèle se trompe-t-il ?"
- Critique pour les systèmes **safety-critical** :
  - Distance de freinage autonome : une sous-estimation = collision
  - Dosage médical : le pire cas définit le risque patient
  - Contrôle qualité : une seule pièce hors tolérance = lot rejeté
- Complémentaire aux métriques moyennes (MAE, RMSE)
- Un modèle avec MAE = 2 et Max Error = 200 est **dangereux**

> Les investisseurs regardent la moyenne. Les régulateurs regardent le **pire cas**.


---

# 13 — MSLE : pénaliser les sous-estimations

- **Mean Squared Logarithmic Error** = (1/n) Σ (log(yᵢ+1) − log(ŷᵢ+1))²
- Le log transforme les écarts en **ratios** — mesure l'erreur **relative**
- Pénalise les **sous-estimations** plus que les sur-estimations [1]
  - Prédire 50 au lieu de 100 (ratio 0.5) est pire que prédire 150 (ratio 1.5)
- Idéale pour l'**inventory forecasting** :
  - Sous-estimer la demande = rupture de stock = perte de ventes
  - Sur-estimer = surplus = coût de stockage (moins grave)
- Aussi utilisée quand les valeurs cibles varient sur **plusieurs ordres de grandeur**
  - Ventes de 10 unités vs 10 000 unités traitées équitablement

<small>Sources : [1] [Built In](https://builtin.com/data-science/msle-vs-mse)</small>


---

# 14 — Discussion : choisir sa métrique de distance

> Votre startup de livraison prédit les délais de livraison. Sur 1 000 commandes :
> MAE = 5 minutes, mais un client a attendu **45 minutes** de plus que prévu.
> Votre investisseur veut un chiffre pour le pitch deck.

**Questions pour la classe** :
- La MAE de 5 min **capte-t-elle** la catastrophe du client qui attend 45 min ?
- RMSE ou Max Error — **lequel présentez-vous** aux investisseurs, et lequel gardez-vous pour l'équipe technique ?
- Si vous êtes Uber Eats, préférez-vous **sous-estimer** (client surpris en bien) ou **sur-estimer** (client préparé) le délai ?

---

<!-- _class: section -->

# Goodness-of-Fit

## Le modèle explique-t-il vraiment les données ?

---

<!-- _class: compact -->

# 15 — R² : le pourcentage de variance expliquée

- **R²** = 1 − (SS_res / SS_tot)
  - SS_res = Σ(yᵢ − ŷᵢ)² · SS_tot = Σ(yᵢ − ȳ)²
- "Le modèle explique **X%** de la variance des données"
- **Plage** : −∞ à 1
  - R² = 1 → parfait · R² = 0 → vaut la moyenne
  - R² < 0 → **pire** que la moyenne
- Sans unité — comparable entre datasets

<!-- Speaker notes: R² = 0.85 signifie que le modèle capture 85% de la variation des données. -->

![bg right:35%](assets/infographics/r-squared-variance_run_20260301_174330_e3e034.png)

<!-- PB: Graphique nuage de points avec droite de régression, SS_res (écarts à la droite) vs SS_tot (écarts à la moyenne) -->

---

# 16 — R² : quand l'utiliser

- **Modèles linéaires** : R² est la métrique standard de fit
- **Feature importance** : comparer R² avec/sans une variable révèle son apport
- **Communication rapide** : "notre modèle explique 92% des variations de prix"
- Utile pour la **sélection de modèle** — comparer Linear Regression, Ridge, Lasso
- **Domaines typiques** :
  - Économétrie et finance
  - Études marketing (impact pub → ventes)
  - Sciences sociales
- Toujours **compléter** avec une métrique d'erreur (MAE ou RMSE)

> R² dit *à quel point* le modèle est bon. MAE/RMSE disent *de combien* il se trompe.


---

<!-- _class: compact -->

# 17 — R² : limitations — quand il ment

- **Anscombe's Quartet** : 4 datasets, même R² = 0.67, formes très différentes [1]
- R² **augmente toujours** en ajoutant des variables — même aléatoires
- **Peut être négatif** — pire que la moyenne
- **Insensible au biais** : prédire toujours +10k → bon R²
- Ne détecte pas si le modèle est **approprié**

<!-- Speaker notes: Règle d'or : ne jamais évaluer un modèle sur le seul R². Toujours visualiser les résidus. -->

<small>Sources : [1] [Anscombe 1973](https://en.wikipedia.org/wiki/Anscombe%27s_quartet)</small>

![bg right:35%](assets/infographics/anscombe-quartet_run_20260301_174352_50a169.png)

<!-- PB: Les 4 graphiques du Anscombe's Quartet : même R², même droite, formes visuellement très différentes -->

---

# 18 — Adjusted R² : corriger le biais

- **Problème** : ajouter n'importe quelle variable **augmente** R², même du bruit
  - Modèle avec 2 features : R² = 0.80
  - Même modèle + "couleur préférée" : R² = 0.81 — artificiellement meilleur
- **Adjusted R²** pénalise les features inutiles :
  - Adj R² = 1 − ((1 − R²)(n − 1)) / (n − p − 1)
  - **n** = nombre d'observations, **p** = nombre de features
- Adjusted R² peut **diminuer** en ajoutant une variable non pertinente
- **Règle** : si Adj R² baisse en ajoutant une feature → la retirer
- Essentiel pour comparer des modèles avec un **nombre différent de features**

> Adjusted R² est le garde-fou contre l'**overfitting** par accumulation de variables.


---

# 19 — Discussion : R² et les pièges du prestataire

> Un prestataire annonce **R² = 0.99** sur son modèle de prédiction des ventes.
> Il veut un contrat de 3 ans à €200k/an. Le modèle tourne sur vos données historiques.

**Questions pour la classe** :
- Un R² de 0.99 **suffit-il** pour signer le contrat ?
- Que **vérifiez-vous** avant de signer ? (indice : overfitting, données de test, biais)
- Le prestataire a utilisé **50 features** sur **60 observations** — que vous dit l'Adjusted R² ?

---

<!-- _class: section -->

# Losses Robustes

## Quand vos données sont bruitées ou incertaines

---

<!-- _class: compact -->

# 20 — Huber Loss : le meilleur des deux mondes

- **Hybride** MAE + MSE contrôlée par un paramètre **δ**
- |erreur| ≤ δ → **MSE** (quadratique) · |erreur| > δ → **MAE** (linéaire) [1]
- δ petit → robuste (quasi MAE) · δ grand → quasi MSE
- **Différentiable partout** — permet le gradient descent

<!-- Speaker notes: Huber Loss = "je veux la précision de MSE, mais sans que les outliers ne détruisent mon modèle." -->

<small>Sources : [1] [GeeksforGeeks](https://www.geeksforgeeks.org/machine-learning/huber-loss-function-in-machine-learning/)</small>

![bg right:35%](assets/infographics/huber-loss-curve_run_20260301_174352_89b5c0.png)

<!-- PB: Courbe Huber vs MSE vs MAE : zone quadratique au centre (≤δ), zone linéaire aux extrémités (>δ) -->

---

# 21 — Huber Loss en pratique

- **Données de capteurs** : les capteurs IoT génèrent des pics de bruit ponctuels
  - Un capteur de température qui affiche 500°C pendant 1 seconde → outlier
  - Huber Loss limite l'influence de ce point sans l'ignorer
- **Object detection** : Smooth L1 Loss (= Huber avec δ=1) est standard en Computer Vision [1]
  - Utilisée dans Faster R-CNN, SSD, YOLO pour la Bounding Box Regression
- **Prévision financière** : les crash days sont des outliers naturels
- **Choix de δ** : fixer δ au niveau de l'erreur "acceptable" pour votre cas
  - Livraison : δ = 10 min (au-delà = outlier)
  - Immobilier : δ = €20k

<small>Sources : [1] [DataCamp](https://www.datacamp.com/tutorial/loss-function-in-machine-learning)</small>


---

<!-- _class: compact -->

# 22 — Quantile Loss : prédire des intervalles

- Prédit des **quantiles** au lieu d'un point unique
- Pénalise **différemment** selon la direction de l'erreur
  - Quantile 0.9 : sous-estimer coûte **9×** plus [1]
  - Quantile 0.1 : sur-estimer coûte **9×** plus
- Résultat : un **intervalle de prédiction**
  - "Livraison entre **14h et 16h** (intervalle 80%)"
- **Amazon** : optimisation des niveaux de stock [2]

<small>Sources : [1] [Towards Data Science](https://towardsdatascience.com/quantile-loss-and-quantile-regression-b0689c13f54d/) · [2] [Amazon Science](https://www.amazon.science/blog/improving-forecasting-by-learning-quantile-functions)</small>

![bg right:35%](assets/infographics/quantile-loss-intervals_run_20260301_174352_bd5de3.png)

<!-- PB: Schéma Quantile Loss : courbe asymétrique avec pénalité forte d'un côté, faible de l'autre, pour quantiles 0.1, 0.5, 0.9 -->

---

<!-- _class: compact -->

# 23 — Quantile Loss : la puissance des intervalles

- **Livraison** : "entre 2h et 4h" plus utile que "3h" — SeatGeek utilise q=0.80 [1]
- **Supply chain** : arbitrage rupture vs stockage
  - q=0.95 → peu de ruptures, stock élevé
  - q=0.50 → stock minimal, 50% de risque
- **Énergie** : demande maximale pour dimensionner le réseau
- Le choix du quantile est un **arbitrage business** : plus élevé → plus conservateur → plus cher

<small>Sources : [1] [SeatGeek Engineering](https://chairnerd.seatgeek.com/smart-order-tracking/)</small>

![bg right:35%](assets/infographics/quantile-practical_run_20260301_174353_da48e6.png)

<!-- PB: Comparaison point vs intervalle pour la livraison : "3h" vs "2h-4h" avec distribution de probabilité et quantiles -->

---

<!-- _class: section -->

# Synthèse

## Quelle métrique pour quel problème ?

---

<!-- _class: cols -->

# 24 — Tableau comparatif des métriques (1/2)

<div class="left">

| Métrique | Outliers | Unité |
|----------|:-:|-------|
| MAE | Non | Cible |
| MSE | **Oui** | Cible² |
| RMSE | **Oui** | Cible |

</div>
<div class="right">

| Métrique | Meilleur usage |
|----------|---------------|
| MAE | Communication, robustesse |
| MSE | Optimisation, gradient |
| RMSE | Pénalise grosses erreurs |

</div>

---

<!-- _class: cols -->

# 25 — Tableau comparatif des métriques (2/2)

<div class="left">

| Métrique | Usage principal |
|----------|---------------|
| R² | Variance expliquée |
| Adj R² | + pénalité features |
| Max Error | Pire cas, sécurité |

</div>
<div class="right">

| Métrique | Usage principal |
|----------|---------------|
| Huber | Données bruitées |
| Quantile | Intervalles de confiance |
| MSLE | Sous-estimation coûteuse |

</div>

---

<!-- _class: compact -->

# 26 — Arbre de décision en 4 questions

- **Q1** : Grosses erreurs **catastrophiques** ?
  - Oui → RMSE, Max Error · Non → MAE
- **Q2** : Métrique en **pourcentage** ?
  - Oui (sans zéros) → MAPE / SMAPE · Non → unités absolues
- **Q3** : Données **bruitées** / outliers ?
  - Oui → Huber Loss, MedAE · Non → MSE/RMSE
- **Q4** : Besoin d'un **intervalle** ?
  - Oui → Quantile Loss · Non → métrique ponctuelle

![bg right:35%](assets/infographics/regression-decision-tree_run_20260301_174353_fc95d7.png)

<!-- PB: Arbre de décision à 4 niveaux de questions avec les métriques recommandées à chaque feuille -->

---

# 27 — Takeaways

1. **Aucune métrique n'est universelle** — le choix dépend du contexte business, pas de la théorie
2. **MAE pour communiquer**, RMSE pour les systèmes critiques, MAPE pour comparer des échelles
3. **R² seul est trompeur** — toujours visualiser les résidus et utiliser Adjusted R²
4. **Huber Loss** combine la robustesse de MAE et la précision de MSE — idéal pour données réelles
5. **Quantile Loss** transforme une prédiction ponctuelle en **intervalle actionnable**

> **Règle d'or** : utilisez toujours **au moins deux métriques** complémentaires. Une métrique de distance (MAE ou RMSE) + une métrique de fit (R²) + une métrique de pire cas (Max Error).
