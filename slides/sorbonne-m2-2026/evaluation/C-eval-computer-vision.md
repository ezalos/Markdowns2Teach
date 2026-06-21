---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Évaluation · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche Evaluation Metrics 2024–2026 · Données publiques"
---

<!-- ABOUTME: Métriques d'évaluation pour la Computer Vision — IoU, Object Detection, Segmentation, Classification, Generation, Tracking. -->
<!-- ABOUTME: Deck de référence pour étudiants M2 non-ingénieurs, orienté décision business et cas pratiques. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Évaluer la Computer Vision

## Object Detection, Segmentation, Classification, Generation

Deep Tech & ML (UE3) · Évaluation
M2 IMT&E · Paris 1 Panthéon-Sorbonne

---

# 01 — Pourquoi ça compte

- Un bounding box **décalé de 30%** sur une voiture autonome → freinage trop tard
- Un Dice Score de **92%** en imagerie médicale → le chirurgien fait confiance au masque
- Un FID de **12.4** pour Midjourney → les images semblent réalistes, mais est-ce suffisant ?

> Chaque tâche de Computer Vision a ses propres métriques.
> Choisir la mauvaise = optimiser dans le vide.

- **5 familles de tâches** → chacune avec ses métriques dédiées
- Ce deck couvre : Detection, Segmentation, Classification, Generation, Tracking

---

# 02 — Carte des métriques CV

| Tâche | Métriques clés | Benchmark |
|---|---|---|
| Object Detection | mAP, AP@50, AP@75 | COCO, Pascal VOC |
| Segmentation | mIoU, Dice, PQ | ADE20K, Cityscapes |
| Classification | Top-1, Top-5, F1 | ImageNet |
| Image Generation | FID, IS, CLIPScore | COCO-30k |
| Object Tracking | MOTA, HOTA, IDF1 | MOT Challenge |

> Toutes partagent une brique fondamentale : l'**IoU** (Intersection over Union).

![bg right:40%](assets/infographics/cv-taxonomy_run_20260301_174307_cc52bd.png)

<!-- PB: Mind map with 5 branches from "CV Evaluation" center: Detection, Segmentation, Classification, Generation, Tracking — each with 2-3 metric labels -->

---

<!-- _class: section -->

# IoU : la brique fondamentale

## Intersection over Union

---

# 03 — IoU : l'intuition

- Deux personnes dessinent un cercle autour du même chat — l'IoU mesure le chevauchement

$$\text{IoU} = \frac{\text{Aire d'intersection}}{\text{Aire d'union}}$$

- Plage : **0** (aucun chevauchement) → **1** (superposition parfaite)

| IoU | Interprétation | Verdict |
|:---:|---|---|
| 0.1 | Presque raté | Mauvais |
| 0.5 | Seuil minimal COCO | Acceptable |
| 0.9 | Quasi-parfait | Excellent |

![bg right:40%](assets/infographics/iou-three-levels_run_20260301_174524_70b0da.png)

<!-- PB: Three pairs of overlapping rectangles showing IoU=0.1 (barely touching), IoU=0.5 (half overlap), IoU=0.9 (nearly identical), each with shaded intersection area -->

---

<!-- _class: compact -->

# 04 — Les limites de l'IoU

- Si deux boxes ne se chevauchent pas, IoU = 0 **quelle que soit la distance**
- Gradient **nul** → le modèle ne sait pas comment corriger

| Variante | Ajout | Avantage |
|---|---|---|
| **GIoU** (2019) | Pénalise l'espace vide englobant | Gradient même sans overlap |
| **DIoU** (2020) | Distance entre centres | Convergence 3× plus rapide |
| **CIoU** (2020) | Ratio d'aspect | Meilleure précision finale |

> **CIoU** est le standard dans YOLOv8+ et DETR modernes [1].

<small>Sources : [1] [LearnOpenCV](https://learnopencv.com/iou-loss-functions-object-detection/)</small>

![bg right:35%](assets/infographics/iou-failure_run_20260301_174527_e995e0.png)

<!-- PB: Side-by-side comparison of IoU, GIoU, DIoU showing the same non-overlapping box pair and how each loss function provides different gradient signals -->

---

<!-- _class: section -->

# Object Detection

## Localiser et identifier chaque objet

---

# 05 — Precision-Recall pour la détection

- **True Positive** : IoU avec le ground truth > seuil (ex: 0.5)
- **False Positive** : le modèle hallucine un objet
- **False Negative** : objet non détecté
- La **courbe PR** trace le compromis à différents seuils de confiance
- **AP** (Average Precision) = aire sous cette courbe

> AP élevé = à la fois précis (peu de FP) et complet (peu de FN).

![bg right:40%](assets/infographics/ap-pr-curve_run_20260301_174530_318ee0.png)

<!-- PB: PR curve for object detection showing the area under curve shaded, with annotations for "high confidence = high precision, low recall" and "low confidence = high recall, low precision" -->

---

<!-- _class: cols -->

# 06 — AP@50, AP@75, mAP@[.5:.95]

<div class="left">

**AP@50** — tolérant (Pascal VOC)
**AP@75** — exigeant (robotique)
**mAP@[.5:.95]** — standard COCO

> Plus le seuil est élevé, plus on exige de **précision spatiale**.

</div>
<div class="right">

| Seuil | Usage typique |
|---|---|
| AP@50 | Comptage, tri |
| AP@75 | Précision spatiale |
| mAP | Standard industrie |

</div>

![bg right:30%](assets/infographics/ap-thresholds_run_20260301_174533_d3cb52.png)

<!-- PB: Three detection examples on the same object showing IoU=0.52 (passes AP@50 only), IoU=0.78 (passes AP@75), IoU=0.92 (passes all thresholds) -->

---

# 07 — mAP en pratique : COCO SOTA 2025

| Modèle | Architecture | mAP@[.5:.95] | Params | Vitesse |
|---|---|:---:|:---:|---|
| **ScyllaNet** | CNN optimisé | 66.1% | ~40M | Temps réel |
| **DEIMv2-X** | DETR + Transformer | 57.8% | ~50M | Temps réel |
| **RF-DETR-L** | DETR + DINOv2 | 60.5% | 128M | 25+ FPS (T4) |
| **YOLOv12-X** | CNN-Attention hybride | 55.2% | 59M | 35+ FPS |
| **RT-DETRv2** | DETR | 53.4% | — | Temps réel |

- ScyllaNet : 2e au classement COCO test-dev (sept. 2025) [1]
- RF-DETR : Pareto-optimal vitesse/précision, sans NMS [2]

<small>Sources : [1] [Scylla AI](https://www.scylla.ai/scyllanet-ranked-2nd-on-coco-leaderboard/) · [2] [Roboflow](https://blog.roboflow.com/rf-detr/)</small>

---

# 08 — Discussion : contrôle qualité en usine

> **Scénario** : Vous déployez un système de détection de défauts sur une ligne de production automobile. Le modèle détecte fissures, rayures et bosses sur les carrosseries.

- **Question 1** : Faut-il optimiser AP@50 ou AP@75 ? Pourquoi ?
- **Question 2** : Un FP (faux défaut) arrête la ligne 2 min. Un FN (défaut raté) coûte un rappel produit à 50 k€. Comment calibrer le seuil de confiance ?
- **Question 3** : Les défauts sont petits (< 32×32 px). Quelle métrique COCO surveiller en priorité ?

---

# 09 — AP par taille d'objet

- COCO définit **3 catégories** de taille :
  - **AP_small** : objets < 32² pixels
  - **AP_medium** : objets 32²–96² pixels
  - **AP_large** : objets > 96² pixels
- L'écart est massif — même les meilleurs modèles :

| Modèle | AP_small | AP_large | Écart |
|---|:---:|:---:|:---:|
| ScyllaNet | 50.0% | 79.0% | −29 pts |
| RF-DETR-L | ~38% | ~72% | −34 pts |

> Les petits objets restent le **talon d'Achille** de la détection [1].

<small>Sources : [1] [Scylla AI](https://www.scylla.ai/scyllanet-ranked-2nd-on-coco-leaderboard/)</small>


---

# 10 — NMS : le post-traitement critique

- Un détecteur produit des **centaines de boxes** par image
- **NMS** (Non-Maximum Suppression) élimine les doublons :
  1. Trier par confiance décroissante
  2. Garder le meilleur box
  3. Supprimer les boxes avec IoU > seuil (ex: 0.5) avec le box gardé
  4. Répéter

| Méthode | Avantage | Limite |
|---|---|---|
| NMS standard | Simple, rapide | Supprime les vrais objets proches |
| Soft-NMS | Réduit le score au lieu de supprimer | Plus lent |
| Sans NMS (DETR) | End-to-end, pas de seuil | Modèle plus complexe |


---

# 11 — 5 pièges du mAP

1. **mAP masque les classes faibles** — un modèle à 55% mAP peut avoir 90% sur "voiture" et 10% sur "vélo"
2. **Le seuil IoU change tout** — AP@50 vs AP@75 racontent des histoires différentes
3. **Taille d'objet ignorée** — mAP global cache l'échec sur les petits objets
4. **NMS est un hyperparamètre** — un mauvais seuil NMS fait chuter le mAP de 5+ points
5. **Vitesse non incluse** — un mAP de 66% à 0.5 FPS est inutilisable en production

> Toujours regarder mAP **+ AP par taille + vitesse d'inférence**.

---

<!-- _class: section -->

# Segmentation

## Pixel par pixel

---

<!-- _class: cols -->

# 12 — Trois types de segmentation

<div class="left">

**Semantic** — pixel → classe
**Instance** — objet → masque distinct
**Panoptic** — semantic + instance

> Chaque type a ses métriques dédiées.

</div>
<div class="right">

| Type | Métrique | Benchmark |
|---|---|---|
| Semantic | mIoU | ADE20K |
| Instance | AP mask | COCO |
| Panoptic | PQ | COCO |

</div>

![bg right:30%](assets/infographics/segmentation-types_run_20260301_174535_81e120.png)

<!-- PB: Same street scene shown three ways: semantic (flat colors per class), instance (different shades per car/person), panoptic (both combined) -->

---

# 13 — Pixel Accuracy & mIoU

- **Pixel Accuracy** = pixels correctement classifiés / total pixels
- Problème : si le fond couvre 95% de l'image, un modèle qui prédit "tout = fond" obtient **95% Accuracy**

$$\text{mIoU} = \frac{1}{C} \sum_{c=1}^{C} \frac{TP_c}{TP_c + FP_c + FN_c}$$

- **mIoU** (mean IoU) = moyenne de l'IoU par classe
- Chaque classe pèse autant, même les rares → métrique **équitable**
- SOTA ADE20K (150 classes) : **63.6% mIoU** (ViT-P, 2025) [1]

<small>Sources : [1] [arXiv:2505.19795](https://arxiv.org/html/2505.19795v1)</small>

![bg right:30%](assets/infographics/pixel-accuracy-trap_run_20260301_174537_1fb332.png)

<!-- PB: Split image showing a scene where 95% is sky: left shows "Pixel Accuracy = 95%" with wrong foreground, right shows "mIoU = 32%" revealing the true failure -->

---

<!-- _class: compact -->

# 14 — Dice Coefficient

- Référence en **imagerie médicale** (tumeurs, organes), aussi appelé F1 pixel :

$$\text{Dice} = \frac{2 \times |A \cap B|}{|A| + |B|}$$

- Relation avec l'IoU :

$$\text{Dice} = \frac{2 \times \text{IoU}}{1 + \text{IoU}}$$

- Dice ≥ IoU pour la même prédiction — un Dice de **0.85** ≈ IoU de **0.74**

> En médecine, on exige **Dice > 0.90** pour la validation clinique.

![bg right:35%](assets/infographics/dice-medical_run_20260301_174540_9d068b.png)

<!-- PB: Venn diagram of prediction mask vs ground truth mask showing intersection, with formula and a medical imaging example (tumor outline) -->

---

# 15 — Boundary F1 Score

- mIoU et Dice mesurent la **surface**, pas les **contours**
- Deux prédictions avec le même Dice peuvent avoir des bords très différents
- Le **Boundary F1 (BF1)** mesure la précision des contours à une distance tolérée

| Application | Pourquoi les bords comptent |
|---|---|
| Chirurgie assistée | Couper 2mm trop large = dommage tissulaire |
| Conduite autonome | Bord du trottoir flou = monte sur le trottoir |
| Satellite / agriculture | Contour de parcelle = calcul de surface |

> Quand la **frontière** entre classes a un impact physique, utilisez BF1 en complément du Dice.


---

# 16 — Panoptic Quality (PQ)

- Métrique unifiée pour la Panoptic Segmentation :

$$\text{PQ} = \underbrace{\text{SQ}}_{\text{Segmentation Quality}} \times \underbrace{\text{RQ}}_{\text{Recognition Quality}}$$

- **SQ** = IoU moyen des matches (qualité des masques)
- **RQ** = F1 des instances (le modèle trouve-t-il les bons objets ?)
- Un match = IoU > 0.5 entre prédiction et ground truth
- SOTA COCO Panoptic : **~59.5% PQ** (MaskDINO) [1]
- SOTA ADE20K Panoptic : **54.0% PQ** (ViT-P, 2025) [2]

<small>Sources : [1] [BasicAI](https://www.basic.ai/blog-post/comprehensive-guide-of-panoptic-segmentation) · [2] [arXiv:2505.19795](https://arxiv.org/html/2505.19795v1)</small>


---

# 17 — Discussion : imagerie médicale

> **Scénario** : Vous évaluez un modèle de segmentation de tumeurs cérébrales sur IRM. Le modèle affiche un Dice de 0.88 et un BF1 de 0.62.

- **Question 1** : Le Dice est bon, mais le BF1 est faible. Que signifie ce décalage pour le chirurgien ?
- **Question 2** : Le dataset contient 80% d'images sans tumeur. Pourquoi le Pixel Accuracy serait-il trompeur ici ?
- **Question 3** : Faut-il plutôt optimiser Dice ou BF1 pour la planification chirurgicale ?

---

<!-- _class: section -->

# Image Classification

## La tâche historique du Deep Learning

---

# 18 — Top-1 & Top-5 Accuracy : la saga ImageNet

| Année | Modèle | Top-1 | Architecture |
|:---:|---|:---:|---|
| 2012 | AlexNet | 63.3% | CNN (8 couches) |
| 2014 | VGG-19 | 74.5% | CNN (19 couches) |
| 2015 | ResNet-152 | 78.6% | CNN + Skip connections |
| 2020 | EfficientNet-L2 | 88.4% | CNN + NAS scaling |
| 2021 | Meta Pseudo Labels | 90.2% | Semi-supervised |
| 2025 | CoCa (2.1B params) | 91.0% | Vision-Language |

- **Top-1** : classe la plus probable correcte · **Top-5** : bonne classe dans le top 5
- Challenge ImageNet déclaré "résolu" en 2017 [1]

<small>Sources : [1] [Articsledge](https://www.articsledge.com/post/image-classification)</small>


---

# 19 — Confusion Matrix pour la vision

- En classification d'images, les confusions révèlent des **biais visuels** :

| Confusion fréquente | Cause probable |
|---|---|
| Loup → Husky | Arrière-plan neigeux similaire |
| Léopard → Jaguar | Motif de pelage quasi-identique |
| Champignon → Méduse | Forme similaire vue de dessous |

- La matrice de confusion **par classe** est plus utile que l'Accuracy globale
- Elle révèle si le modèle apprend les **features discriminantes** ou le **contexte**

> Un modèle qui confond loup et husky a peut-être appris "neige" au lieu de "museau".

---

# 20 — Les limites de l'Accuracy en vision

- Même piège qu'en classification tabulaire : le **déséquilibre des classes**
- Un dataset médical avec 98% d'images "saines" → Accuracy de 98% en prédisant toujours "sain"
- Solutions identiques : **F1 macro**, **F1 pondéré**, **MCC**
- Spécifique à la vision : **Robustesse** — le modèle est-il fiable sur :
  - Images floues ou bruitées ? (ImageNet-C)
  - Conditions d'éclairage différentes ?
  - Distribution différente du training set ?

> L'Accuracy sur un test set propre n'est qu'un **minimum**. En production, testez la robustesse.


---

<!-- _class: section -->

# Image Generation

## Évaluer ce qui n'a pas de "bonne réponse"

---

<!-- _class: compact -->

# 21 — FID : Fréchet Inception Distance

- Pas de ground truth pixel-exact → comparer les **distributions** réelles vs générées
- Pipeline : features Inception → moyenne + covariance → distance de Fréchet
- **FID bas = mieux** (distributions proches)

| Modèle | FID (COCO-30k) |
|---|:---:|
| Imagen (Google) | 7.27 |
| Stable Diffusion 1.5 | 8.74 |
| DALL·E 2 | 10.39 |
| SDXL (MLPerf ref.) | ~23.5 |

<small>Sources : [1] [Diffusion2GAN](https://mingukkang.github.io/Diffusion2GAN/)</small>

![bg right:30%](assets/infographics/fid-distributions_run_20260301_183015_d42af0.png)
<!-- PB: Two gaussian distributions in feature space (real vs generated) with Fréchet distance arrow -->


---

<!-- _class: cols -->

# 22 — IS & CLIPScore

<div class="left">

**Inception Score (IS)**
- Mesure **qualité + diversité**
- IS élevé = mieux
- Limite : ne compare pas aux réelles

</div>
<div class="right">

**CLIPScore**
- Mesure l'**alignement texte-image**
- DALL·E 3 : **32.0** vs SDXL : **30.5** [1]
- Indépendant d'un dataset de référence

</div>

<small>Sources : [1] [OpenAI](https://cdn.openai.com/papers/dall-e-3.pdf)</small>


---

<!-- _class: cols -->

# 23 — SSIM & LPIPS

<div class="left">

**SSIM** (Structural Similarity)
- Compare luminance, contraste, structure
- Plage : −1 à 1 (1 = identique)
- Limite : insensible aux textures

</div>
<div class="right">

**LPIPS** (Learned Perceptual)
- Features d'un réseau VGG pré-entraîné
- **LPIPS bas = plus similaire**
- Corrèle mieux avec l'humain [1]

</div>

<small>Sources : [1] [arXiv:2601.19680](https://arxiv.org/html/2601.19680v1)</small>


---

# 24 — 4 cas où les métriques échouent

| Cas | FID dit... | Humain dit... | Problème |
|---|---|---|---|
| Images floues mais réalistes | FID bon (~10) | "C'est flou" | FID ignore la netteté |
| Copies du dataset | FID parfait (~0) | "C'est du plagiat" | FID ne détecte pas l'overfitting |
| Style artistique fort | FID mauvais (~40) | "C'est beau" | FID pénalise la créativité |
| Texte illisible dans l'image | CLIPScore bon | "Je ne lis rien" | CLIP évalue le concept, pas le rendu |

> Aucune métrique automatique ne remplace l'**évaluation humaine** pour la génération.


---

<!-- _class: section -->

# Object Tracking

## Suivre les objets à travers le temps

---

<!-- _class: compact -->

# 25 — MOTA, HOTA, IDF1

- Le tracking ajoute la **cohérence temporelle** entre frames

| Métrique | Mesure | Formule simplifiée |
|---|---|---|
| **MOTA** | Précision globale | 1 − (FN + FP + ID switches) / GT |
| **IDF1** | Cohérence d'identité | F1 des associations correctes |
| **HOTA** | Détection × Association | √(DetA × AssA) |

- MOTA dominé par la détection · IDF1 pénalise les changements d'ID
- **HOTA** équilibre les deux — recommandée depuis 2021 [1]
- SOTA MOT17 : MOTA **81.8%**, HOTA **66.4%** (FastTracker) [2]

<small>Sources : [1] [MOTChallenge](https://motchallenge.net/) · [2] [MOT17 Leaderboard](https://motchallenge.net/results/MOT17/)</small>

![bg right:30%](assets/infographics/tracking-timeline_run_20260301_174553_67ad1b.png)

<!-- PB: Video frame sequence showing a tracked person with consistent ID (green box with "Person #3") vs an ID switch event (box changes from green #3 to red #7 after occlusion) -->

---

# 26 — Quand le tracking échoue

- **ID Switch** : personne A passe derrière un pilier, ressort étiquetée B
- **Occlusion prolongée** : objet disparaît 2 s → tracker le perd
- **Foule dense** : 50 piétons se croisent → cascades d'ID switches

| Scénario | Métrique impactée | Conséquence business |
|---|---|---|
| Supermarché | IDF1 chute | Parcours client mal attribué |
| Stade de foot | MOTA chute | Comptage spectateurs faux |
| Voiture autonome | HOTA chute | Prédiction trajectoire erronée |

> Le tracking reste un **problème ouvert** : même le SOTA fait des ID switches.

![bg right:30%](assets/infographics/tracking-failure_run_20260301_174614_088f2a.png)

<!-- PB: Three failure scenarios illustrated: ID switch after occlusion, lost track during prolonged occlusion, cascade of switches in a crowd -->

---

<!-- _class: section -->

# Benchmarks & Datasets

## Les terrains de jeu standardisés

---

# 27 — 6 benchmarks à connaître

| Benchmark | Tâche | Classes | Images | Depuis |
|---|---|:---:|:---:|:---:|
| **COCO** | Detect. + Segm. | 80 things + 53 stuff | 330k | 2014 |
| **ImageNet** | Classification | 1 000 | 1.4M | 2009 |
| **ADE20K** | Segm. sémantique | 150 | 25k | 2017 |
| **Cityscapes** | Conduite autonome | 30 | 25k | 2016 |
| **Pascal VOC** | Detect. + Segm. | 20 | 11k | 2005 |
| **MOT Challenge** | Tracking piétons | — | Vidéo | 2015 |

> **COCO** et **ImageNet** sont les deux références incontournables. Tout modèle CV sérieux les cite.

---

<!-- _class: cols -->

# 28 — COCO vs Pascal VOC

<div class="left">

**Pascal VOC** (2005)
- 20 classes, 11k images
- AP@50 uniquement (tolérant)
- Historique, peu utilisé en 2025

</div>
<div class="right">

**MS COCO** (2014)
- 80 classes, 330k images
- mAP@[.5:.95] (exigeant)
- Standard industriel actuel

</div>

> Un "bon" modèle sous VOC peut être "moyen" sous COCO — le protocole change le verdict.

---

<!-- _class: section -->

# Synthèse

## Choisir la bonne métrique

---

<!-- _class: compact -->

# 29 — Arbre de décision

- **Étape 1** : Quelle tâche ?
  - Détection → mAP@[.5:.95]
  - Segmentation → mIoU (sémantique) ou PQ (panoptique)
  - Classification → Top-1 Accuracy + F1 macro
  - Génération → FID + CLIPScore + éval humaine
  - Tracking → HOTA
- **Étape 2** : Contexte métier ?
  - Médical → Dice + BF1
  - Petits objets → AP_small
  - Temps réel → ajouter contrainte FPS

![bg right:35%](assets/infographics/cv-decision-tree_run_20260301_174614_ee0075.png)

<!-- PB: Flowchart decision tree: "What is your CV task?" branching into 5 paths (detection, segmentation, classification, generation, tracking), each leading to recommended metrics and benchmark -->

---

# 30 — 5 pièges des métriques CV

1. **Le piège du benchmark unique** — un modèle excellent sur COCO peut échouer sur votre dataset industriel (domain gap)
2. **Le piège de la moyenne** — mAP, mIoU cachent les classes faibles et les petits objets
3. **Le piège du FID** — un FID parfait ne garantit ni la qualité perçue ni l'originalité
4. **Le piège de la vitesse** — les papiers de recherche ignorent souvent la latence d'inférence
5. **Le piège du dataset** — COCO n'a pas été mis à jour depuis 2017, ImageNet depuis 2012

> En production : **toujours** évaluer sur vos propres données, avec vos propres contraintes.

---

# 31 — Key Takeaways

1. **L'IoU** est la brique fondamentale — elle sous-tend la détection, la segmentation et le tracking

2. **mAP@[.5:.95]** est le standard de l'industrie pour l'Object Detection — mais regardez aussi AP par taille d'objet

3. **mIoU > Pixel Accuracy** pour la segmentation — le Dice et le BF1 complètent selon le domaine

4. **FID ≠ qualité perçue** pour la génération — combinez FID, CLIPScore et évaluation humaine

5. **Le choix de la métrique dépend du coût des erreurs** — un FP en médecine ≠ un FP en e-commerce

> La métrique parfaite n'existe pas. La bonne métrique est celle qui reflète votre **impact business**.
