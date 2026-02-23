---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · Données publiques"
---

<!-- ABOUTME: Panorama complet de l'IA — capacités GenAI, taxonomie des techniques, paradigmes d'apprentissage et tâches. -->
<!-- ABOUTME: Première moitié de la Session 1, business-framed pour étudiants M2 IMT&E Paris 1 Panthéon-Sorbonne. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 1A — L'IA Générative : ce qu'elle sait faire

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Qu'est-ce que la Generative AI ?

## What is Generative AI

---

# 01 — L'essor de la Generative AI

- *$2,6 – 4,4 trillions* de valeur annuelle potentielle [1]
- *+15% du PIB mondial* d'ici 2035 [2]
- *66% des jobs aux US* veront leurs taches quotidiennes transformees par l'IA [3]

> Après le lancement de ChatGPT (nov. 2022), les mentions d'"IA" dans les *earnings calls* du S&P 500 ont explosé.

![bg right:45% contain](assets/A/01-number-of-sp500-earnings-calls-citing-AI-10-year.webp) [4]

*Question pour la classe* : Si le coût de l'intelligence machine tend vers zéro, quel service aujourd'hui trop coûteux pour être automatisé devient une opportunité de startup demain ?

<small>Sources : [1] [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier) [2] [PWC](https://www.pwc.com/gx/en/news-room/press-releases/2025/ai-adoption-could-boost-global-gdp-by-an-additional-15-percentage.html) [3] [EY](https://www.ey.com/en_gl/insights/ai/how-gen-ai-will-impact-the-labor-market) [4] [Factset](https://insight.factset.com/highest-number-of-sp-500-earnings-calls-citing-ai-over-the-past-10-years-1)</small>

---

# 02 — Qu'est-ce que la Generative AI ?

Des systèmes d'intelligence artificielle capables de *produire du contenu de haute qualité* : texte, code, images, audio, vidéo.

![bg right:55% contain](assets/A/02-chatgpt_screenshot.png)
![bg contain](assets/A/02-mistral_screenshot.png)

---

# 03 — La Generative AI, aussi un outil de développement

Au-delà des chatbots grand public, la Generative AI est un *developer tool* puissant :

- Génération de code et debugging
- Automatisation de pipelines de données
- Prototypage rapide d'applications

*Pour les entrepreneurs* : même sans équipe technique, les LLMs permettent de construire des *MVPs fonctionnels* en quelques jours.

> En 2025, des startups comme Bolt.new et Lovable permettent de coder des apps entières via prompt. [1][2]

![bg right:45% contain](assets/A/03-googlecolab-generation.png)

<small>Sources : [1] [Bolt.new](https://bolt.new/) · [2] [Lovable](https://lovable.dev/)</small>

---

# 04 — L'IA est déjà partout

| Technologie IA | Exemples |
|---|---|
| Web Search | Google, Bing |
| Fraud Detection | Paiements CB |
| Recommender Systems | Amazon, Netflix, Spotify |
| Machine Translation | DeepL, Google Translate |
| Speech Recognition | Siri, Alexa, Whisper |

> *Point clé pour entrepreneurs* : L'IA "classique" (prédictive) crée de la valeur depuis 15 ans. La *Generative AI* ouvre un nouvel espace — la création de contenu et le raisonnement.

---

# 05 — Au-delà du texte : images, audio, vidéo

La Generative AI ne se limite pas au texte :

- *Images* : Midjourney [1], DALL-E [2], Stable Diffusion [3], Flux [4]

*Cas d'usage business* :
- Créer des visuels marketing sans graphiste

![bg right:45% contain](assets/ng01/img-009.png)
![bg contain](assets/ng01/img-010.png)

<small>Sources : [1] [Midjourney](https://www.midjourney.com/) · [2] [OpenAI DALL-E](https://openai.com/dall-e-3) · [3] [Stability AI](https://stability.ai/) · [4] [Black Forest Labs](https://blackforestlabs.ai/)</small>

---

# 06 — Au-delà du texte : audio

La Generative AI ne se limite pas au texte :

- *Audio* : génération de voix (ElevenLabs [1]), musique (Suno [2])

![bg right:50% contain](assets/A/suno.png)
[Suno](https://suno.com/s/0wLOtKpawnA132Pz)

*Cas d'usage business* :
- Produire des voix-off pour des formations

<small>Sources : [1] [ElevenLabs](https://elevenlabs.io/) · [2] [Suno](https://suno.com/)</small>

---

# 07 — Au-delà du texte : vidéo

La Generative AI ne se limite pas au texte :

- *Vidéo* : Sora (OpenAI) [1], Runway [2], Kling (Kuaishou) [3], Seedance2

[Prompt example : drone racing an abandoned factory](https://www.youtube.com/watch?v=-MluR9dqt5w&t=12s)

*Cas d'usage business* :
- Générer des vidéos de démonstration produit

<small>Sources : [1] [OpenAI Sora](https://openai.com/sora) · [2] [Runway](https://runwayml.com/) · [3] [Kling AI](https://klingai.com/)</small>

---

<!-- _class: section -->

# L'IA : bien plus que la Generative AI

## AI is Much More Than GenAI

---

# 08 — L'IA traditionnelle reste la majorité de la valeur

La Generative AI fait les gros titres — mais le Machine Learning traditionnel crée *plus de valeur économique* :

| | ML traditionnel | Generative AI |
|---|---|---|
| **Dépenses 2025** | ~$94 Mds [1] | ~$38 Mds [2] |
| **Valeur potentielle** | $11 – 17,7 T/an (McKinsey 2023) [3] | + $2,6 – 4,4 T/an [3] |
| **Investissements 2024** | 150 Mds [6] | $30 Mds [6] |
| **Déploiement** | 71% des entreprises [4] | 29% comme type le + fréquent [5] |
| **Maturité** | Prouvé depuis 15 ans | En phase d'adoption rapide |
| **Cas typiques** | Prédiction, optimisation | Génération, raisonnement |

> *Pour un entrepreneur* : connaître les deux mondes est un avantage compétitif. La GenAI fait le buzz, le ML classique fait le chiffre d'affaires.

<small>Sources : [1] [Precedence Research ML](https://www.precedenceresearch.com/machine-learning-market) · [2] [Precedence Research GenAI](https://www.precedenceresearch.com/generative-ai-market) · [3] [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier) · [4] [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [5] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-05-07-gartner-survey-finds-generative-ai-is-now-the-most-frequently-deployed-ai-solution-in-organizations) [6] [Standford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report/economy) </small>

---

# 09 — Les multiples facettes de l'IA

L'IA se classe selon trois axes complémentaires :

| Axe | Question | Exemples |
|---|---|---|
| **Par technique** | *Comment* est construit le modèle ? | Statistics, ML, Deep Learning, GenAI |
| **Par paradigme** | *Comment* le modèle apprend-il ? | Supervised, Unsupervised, RL, Self-Supervised |
| **Par tâche** | *Que fait* le modèle ? | Classification, détection, génération |

> Les slides suivantes explorent chaque axe avec des exemples concrets et des démos interactives.

![bg right:40% contain](assets/infographics/ai-taxonomy-overview_run_20260219_095043_3593d3.png)

---

<!-- _class: section -->

# Par technique — de la Statistique à la GenAI

## From Statistics to Generative AI

---

<!-- _class: cols -->

# 10 — Vue d'ensemble : Stats → ML → DL → GenAI

<div class="left">

Chaque couche ajoute de la complexité et de la capacité :

- **Statistics** — analyser et quantifier des données
- **Machine Learning** — apprendre des patterns à partir de données
- **Deep Learning** — réseaux de neurones profonds, données massives
- **Generative AI** — créer du contenu original

> Chaque couche *inclut* les précédentes : la GenAI repose sur le Deep Learning, qui repose sur le ML, qui repose sur les statistiques.

</div>
<div class="right">

![](assets/A/ai-onion-raghunitb.png)

</div>

---

# 11 — Statistics : l'A/B Testing

L'outil statistique le plus accessible — et le plus utilisé par les startups :

| | Version A | Version B |
|---|---|---|
| **Bouton** | "Acheter" (vert) | "Commander maintenant" (orange) |
| **Visiteurs** | 10 000 | 10 000 |
| **Conversions** | 230 (2,3%) | 310 (3,1%) |
| **p-value** | — | 0,0005 (significatif) |

> **Ce n'est pas de l'IA.** L'A/B Testing est un outil statistique pur — pas de modèle, pas d'apprentissage. Et c'est souvent l'outil le plus adapté pour des décisions business simples.

*Question pour la classe* : Quelle variable de votre projet pourriez-vous tester avec un A/B test cette semaine ?

![bg right:40% contain](assets/A/stats-ab-test.png)

---

# 12 — Machine Learning : définition

D'après Chip Huyen, le ML est une approche qui réunit **5 conditions** [1] :

| # | Condition | Signification |
|---|---|---|
| 1 | **Learn** | Le système a la capacité d'apprendre par lui-même |
| 2 | **Complex Patterns** | Les patterns sont trop complexes pour être codés à la main |
| 3 | **Existing Data** | Des données existent ou peuvent être collectées |
| 4 | **Predictions** | Le problème est formulable comme une prédiction |
| 5 | **Unseen Data** | Les patterns appris se généralisent à de nouvelles données |

> Si l'une de ces 5 conditions manque, le ML n'est probablement pas la bonne solution.

![bg right:40% contain](assets/infographics/ml-definition-checklist_run_20260222_182359_190bac.png)

<small>Sources : [1] [Chip Huyen, *Designing ML Systems*, O'Reilly 2022](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)</small>

---

# 13 — Machine Learning : cas d'usage business

Les cas les plus déployés en production — souvent invisibles pour l'utilisateur :

| Cas d'usage | Secteur | Exemple |
|---|---|---|
| **Recommandation** | E-commerce, streaming | Amazon, Netflix, Spotify |
| **Détection de fraude** | Banques, paiements | Visa, Mastercard en temps réel |
| **Scoring risque** | Assurance, crédit | Décisions en millisecondes |
| **Prédiction de churn** | SaaS, télécoms | Rétention client proactive |
| **Diagnostic** | Santé, industrie | Dépistage, maintenance prédictive |

> Ces systèmes ML "traditionnels" génèrent ~75% de la valeur IA totale [1].

<small>Sources : [1] [McKinsey](https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/the-economic-potential-of-generative-ai-the-next-productivity-frontier)</small>

---

# 14 — Machine Learning : la Linear Regression

L'algorithme ML le plus simple — tracer une droite à travers des données :

- **Input** : budget marketing mensuel (€)
- **Output** : chiffre d'affaires prédit (€)
- Le modèle apprend la relation `CA = a × Budget + b`

*Exemples business* :
- Prédire le prix d'un bien immobilier à partir de sa surface
- Estimer les revenus en fonction des dépenses publicitaires
- Prévoir la demande d'un produit

> La Linear Regression est le "Hello World" du Machine Learning. Simple, interprétable, et souvent suffisante.

![bg right:40% contain](assets/infographics/ml-linear-regression_run_20260219_095044_81b289.png)

---

# 15 — Deep Learning : pourquoi et comment

**Pourquoi** : quand les patterns sont trop complexes pour des features manuelles (images, audio, texte).

**Comment** : empiler des couches de "neurones artificiels" (perceptrons) :

- **Input Layer** — reçoit les données brutes (pixels, mots, nombres)
- **Hidden Layers** — extrait des features de plus en plus abstraites
- **Output Layer** — produit la prédiction finale

> Plus on ajoute de couches (= "deep"), plus le réseau capture des patterns complexes. C'est ce qui a permis la reconnaissance d'images, la traduction et la GenAI.

![bg right:40% contain](assets/mlp-diagram-full.png)

---

# 16 — Deep Learning : TensorFlow Playground

*Démo interactive* : [playground.tensorflow.org](https://playground.tensorflow.org)

Essayez ces 3 expériences :

1. **Changez le nombre de couches** — observez comment des patterns plus complexes sont capturés
2. **Ajoutez des neurones** — le réseau apprend plus de détails
3. **Modifiez le learning rate** — trop haut = instable, trop bas = lent

> Aucun code nécessaire — glissez et observez le réseau apprendre en temps réel.

---

# 17 — GenAI : le Bottleneck Problem

Avant les Transformers, les modèles utilisaient un **Encoder-Decoder** :

- L'**Encoder** compresse toute l'entrée en un seul vecteur de taille fixe
- Le **Decoder** doit reconstruire la sortie à partir de ce vecteur unique

*Le problème* : c'est comme résumer un film de 3h en une seule phrase — on perd forcément de l'information.

> Plus la séquence d'entrée est longue, plus l'information est compressée et dégradée. C'est le **bottleneck** que l'Attention résout.

![bg right:45% contain](assets/infographics/encoder-decoder_run_20260216_171310_3b56bd.png)

---

# 18 — GenAI : les Transformers et l'Attention

L'architecture qui a tout changé (Vaswani et al. 2017) [1] — le **Self-Attention** permet au modèle de pondérer chaque mot par rapport à *tous les autres*.

**Analogie de la bibliothèque** :
- **Query** = votre question ("Qui a écrit Hamlet ?")
- **Key** = l'étiquette de chaque livre ("Théâtre", "Shakespeare"...)
- **Value** = le contenu du livre correspondant

*Démos interactives* :
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) · [LLM Visualization](https://bbycroft.net/llm) · [BertViz](https://colab.research.google.com/drive/1hXIQ77A4TYS4y3UthWF-Ci7V7vVUoxmQ)

![bg right:40% contain](assets/A/transformer-architecture.png)

<small>Sources : [1] [Vaswani et al. 2017](https://arxiv.org/abs/1706.03762)</small>

---

<!-- _class: section -->

# Par paradigme — comment l'IA apprend

## How AI Learns

---

# 19 — Les trois paradigmes d'apprentissage

| Paradigme | En une phrase |
|---|---|
| **Supervised Learning** | Un prof corrige des copies |
| **Unsupervised Learning** | Un explorateur classe ses découvertes |
| **Reinforcement Learning** | Essai-erreur, comme un jeu vidéo |

> Le **Self-Supervised Learning** (LLMs, Diffusion Models) est un cas particulier présenté en slide 26.

*Question pour la classe* : Pour votre projet de groupe, quel paradigme vous semble le plus adapté — et pourquoi ?

![bg right:40% contain](assets/A/unsupervise-supervise-reinforcement.png)

---

# 20 — Supervised Learning : définition

Le paradigme le plus déployé en production [1] — le modèle apprend à partir d'**exemples étiquetés** :

- On donne au modèle des paires **(Input A → Output B)**
- Il apprend la règle qui relie A à B
- Il peut ensuite prédire B pour de nouveaux A

| Input (A) | Output (B) |
|---|---|
| Email | Spam ? (0/1) |
| Photo produit | Défaut ? (0/1) |
| Profil client | Score de crédit |

> C'est l'équivalent d'un étudiant qui apprend avec un corrigé : il voit les bonnes réponses, et apprend à les reproduire.

<small>Sources : [1] [McKinsey State of AI 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024)</small>

---

# 21 — Supervised Learning : cas d'usage

| Cas d'usage | Input (A) | Output (B) |
|---|---|---|
| **Détection de spam** | Texte d'email | Spam / Pas spam |
| **Diagnostic médical** | Image radiologie | Pathologie / Normal |
| **Scoring crédit** | Profil financier | Score de risque (0-100) |
| **Recommandation** | Historique d'achat | Produit suivant probable |
| **Maintenance prédictive** | Données capteurs | Panne dans X jours |

> *Algorithmes classiques* : Linear Regression, Random Forest, KNN, Gradient Boosting (XGBoost).

---

# 22 — Supervised Learning : Decision Tree

Un **arbre de décision** — un enchaînement de questions binaires (if/else) :

- Chaque **nœud** pose une question oui/non sur une feature
- Chaque **branche** suit la réponse (oui → gauche, non → droite)
- Chaque **feuille** donne la prédiction finale

> Un Decision Tree, c'est un *if/else sur stéroïdes* — le modèle apprend automatiquement quelles questions poser et dans quel ordre.

*Avantages business* :
- **Interprétable** : on peut tracer chaque décision du début à la fin
- Fonctionne sur les **données tabulaires** (le format le plus courant en entreprise)
- Rapide à entraîner — idéal pour un premier prototype

![bg right:45% contain](assets/decision-tree-diagram.png)

---

# 23 — Supervised Learning : KNN

**K-Nearest Neighbors** — l'algorithme le plus intuitif du ML :

- Pour classer un nouveau point, on regarde ses **K voisins les plus proches**
- La catégorie majoritaire parmi les voisins = la prédiction

*Avantages* : aucun entraînement, simple à comprendre
*Limites* : lent sur de gros datasets, sensible aux dimensions

> *Analogie* : pour deviner si un restaurant est bon, demandez l'avis des 5 personnes les plus proches.

![bg right:45% contain](assets/KNN_decision_surface_animation.gif)

---

# 24 — Unsupervised Learning : définition

Le modèle découvre des **structures cachées** dans des données *sans étiquettes* :

- Pas de "bonnes réponses" fournies — le modèle explore seul
- Il identifie des groupes, des anomalies, des patterns latents

| Technique | Ce qu'elle fait | Exemple |
|---|---|---|
| **Clustering** | Regrouper des données similaires | Segmentation clients |
| **Détection d'anomalies** | Identifier les points atypiques | Fraude, panne |
| **Réduction de dimensions** | Simplifier des données complexes | Visualisation |

> *Analogie* : un explorateur qui arrive sur une île inconnue et classe les espèces qu'il découvre — sans guide.

---

# 25 — Unsupervised Learning : K-Means

L'algorithme le plus intuitif — regrouper des données en *clusters* sans supervision :

1. **Initialiser** — placer K centres aléatoirement
2. **Assigner** — chaque point rejoint le centre le plus proche
3. **Recalculer** — déplacer chaque centre au barycentre de son cluster
4. **Répéter** — jusqu'à stabilisation

*Cas business* :
- Segmentation clients (groupes de comportement d'achat similaire)
- Détection d'anomalies (transactions frauduleuses = points isolés)
- Topic modeling (regrouper des avis produits par thème)

> *Pour un entrepreneur* : le K-Means révèle des segments de marché que vos clients ne vous décrivent pas explicitement.

![bg right:40% contain](assets/A/K_means_Clustering.gif)

---

# 26 — Self-Supervised Learning : le secret de la GenAI

Le paradigme qui a rendu la Generative AI possible — apprendre *sans données étiquetées* :

| Modalité | Méthode | Modèles |
|---|---|---|
| **Texte** | Prédire le mot suivant / masqué | GPT, BERT, Claude, Mistral |
| **Image** | Retirer le bruit d'une image bruitée | Stable Diffusion, DALL-E, Flux |

*Pourquoi c'est révolutionnaire* :
- Pas besoin d'humains pour étiqueter les données
- S'entraîne sur *tout Internet* — des trillions de tokens
- Plus de données = meilleur modèle (loi d'échelle)

![bg right:40% contain](assets/A/diffusion_model.gif)

---

# 27 — Reinforcement Learning

L'agent apprend par *essai-erreur*, guidé par un signal de récompense :

| Environnement | Agent | Application |
|---|---|---|
| Jeu de Go | AlphaGo (DeepMind) [1] | Bat le champion du monde (2016) |
| Échecs | AlphaZero | Réinvente les ouvertures en 4h |
| Marchés financiers | Trading agents | Optimisation de portefeuille |
| Conversations humaines | ChatGPT, Claude | RLHF aligne le modèle sur les préférences humaines |

> Le RLHF (Reinforcement Learning from Human Feedback) est l'étape qui transforme un LLM brut en assistant utile et sûr.

![bg right:45% contain](assets/infographics/reinforcement-learning-cycle_run_20260217_010848_d4776e.png)

<small>Sources : [1] [DeepMind](https://deepmind.google/research/breakthroughs/alphago/)</small>

---

<!-- _class: section -->

# Par tâche — que fait l'IA concrètement ?

## What Does AI Actually Do?

---

# 28 — Pourquoi le vocabulaire des tâches compte

Connaître les **noms des tâches** en anglais vous permet de :

1. **Expliquer** ce que vous voulez construire — "Je cherche un modèle de *Text Classification*"
2. **Chercher** efficacement sur HuggingFace, Papers With Code, GitHub

> Les tâches sont la langue commune entre business et technique. Dire "Classification" plutôt que "trier des trucs" montre que vous parlez le langage de l'écosystème.

Les slides suivantes présentent les tâches fondamentales : **Classification**, **Regression**, **Object Detection**, **Segmentation**, **Génération de texte**.

---

# 29 — Classification

Attribuer une **catégorie discrète** à une entrée :

| Input | Output | Application |
|---|---|---|
| Email | Spam / Pas spam | Filtrage Gmail |
| Image | Chat / Chien / Voiture | Reconnaissance visuelle |
| Transaction | Frauduleuse / Légitime | Sécurité bancaire |
| CV | Shortlist / Rejet | Recrutement |
| Avis client | Positif / Négatif / Neutre | Analyse de sentiment |

> La sortie est toujours une *catégorie parmi un ensemble fini*. Binaire (oui/non) ou multi-classes (A, B, C...).

![bg right:40% contain](assets/infographics/classification-task_run_20260222_182359_2508a6.png)

---

# 30 — Regression

Prédire une **valeur continue** (un nombre) :

| Input | Output | Application |
|---|---|---|
| Surface, quartier | Prix immobilier (€) | Estimation bien |
| Budget pub | Chiffre d'affaires (€) | Planification marketing |
| Données patient | Risque (0-100%) | Diagnostic médical |
| Historique ventes | Demande future (unités) | Gestion de stock |
| Données capteurs | Durée de vie restante (jours) | Maintenance prédictive |

> La sortie est un *nombre sur un continuum*, pas une catégorie. La Linear Regression (slide 14) en est l'exemple le plus simple.

![bg right:40% contain](assets/infographics/regression-task_run_20260222_182706_946870.png)

---

# 31 — Object Detection & Segmentation

Des tâches de vision qui vont au-delà de la simple Classification :

| Tâche | Ce qu'elle fait | Exemple |
|---|---|---|
| **Image Classification** | Une étiquette par image | "C'est un chat" |
| **Object Detection** | Localise chaque objet (bounding box) | "Chat à (x,y), chien à (x,y)" |
| **Semantic Segmentation** | Colore chaque pixel par catégorie | Route vs trottoir vs piéton |
| **Instance Segmentation** | Sépare chaque objet individuel | "Piéton 1, Piéton 2, Piéton 3" |

*Outils clés* : YOLO (détection temps réel) [1], Segment Anything (Meta) [2]

> Ces tâches sont au cœur de la conduite autonome, du contrôle qualité industriel et de l'imagerie médicale.

![bg right:45% contain](assets/tasks_cv.webp)

<small>Sources : [1] [Ultralytics YOLO](https://ultralytics.com/) · [2] [Meta SAM](https://segment-anything.com/)</small>

---

# 32 — Génération de texte : le terrain de jeu des LLMs

L'architecture Transformer alimente *toutes* ces tâches de génération :

| Tâche | Input | Output |
|---|---|---|
| **Traduction** | Texte en français | Texte en anglais |
| **Résumé** | Document de 50 pages | 5 bullet points |
| **Question-Answering** | Question + contexte | Réponse précise |
| **Génération de code** | Description en langage naturel | Code fonctionnel |
| **Analyse de sentiment** | Avis client | Positif / Négatif / Neutre |

> Un même modèle Transformer peut accomplir toutes ces tâches — c'est la puissance du *Transfer Learning* et du *Self-Supervised Pretraining*.

---

# 33 — HuggingFace Tasks : votre vocabulaire de recherche

Ces noms de tâches sont votre *vocabulaire* pour chercher des modèles sur HuggingFace :

![bg right:50% contain](assets/hf_tasks_1.png)
![bg right:50% contain](assets/hf_tasks_2.png)

**Lien** : [huggingface.co/models](https://huggingface.co/models)

| Domaine | Tâches clés |
|---|---|
| **NLP** | Text Classification, Summarization, Translation, Question Answering |
| **Vision** | Image Classification, Object Detection, Image Segmentation |
| **Audio** | Speech Recognition, Text-to-Speech, Audio Classification |
| **Multimodal** | Image-to-Text, Visual Question Answering |

> Maîtrisez ces noms de tâches en anglais — c'est le langage commun de l'écosystème IA open source.

---

<!-- _class: section -->

# Chronologie de l'IA

## From Linear Regression to Autonomous Agents

---

# 34 — Timeline Machine Learning

![w:500 center](assets/infographics/timeline-ml_run_20260219_095936_b48914.png)

| Année | Jalon | Impact |
|---|---|---|
| 1805 | Linear Regression (Legendre) | Le premier algorithme de prédiction |
| 1951 | KNN (Fix & Hodges) | Classification par voisinage |
| 1958 | Logistic Regression (Cox) | Classification binaire — toujours utilisée |
| 2001 | Random Forest (Breiman) | Ensembles d'arbres de décision |
| 2014 | XGBoost (Chen & Guestrin) [1] | Champion des compétitions Kaggle |

<small>Sources : [1] [XGBoost (arXiv)](https://arxiv.org/abs/1603.02754)</small>

---

# 35 — Timeline Deep Learning

![w:500 center](assets/infographics/timeline-dl_run_20260219_095938_43643a.png)

| Année | Jalon | Impact |
|---|---|---|
| 1986 | Backpropagation (Hinton) [1] | Rend l'entraînement de réseaux profonds possible |
| 1998 | LeNet / MNIST (LeCun) [2] | Première reconnaissance d'écriture industrielle |
| 2012 | AlexNet + ImageNet [3] | Erreur divisée par 2 — lance l'ère du Deep Learning |
| 2017 | "Attention Is All You Need" [4] | Naissance des Transformers |

<small>Sources : [1] [Nature](https://www.nature.com/articles/323533a0) · [2] [IEEE](https://ieeexplore.ieee.org/document/726791) · [3] [NeurIPS](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) · [4] [arXiv](https://arxiv.org/abs/1706.03762)</small>

---

# 36 — Timeline Generative AI : l'accélération

![w:500 center](assets/infographics/timeline-genai_run_20260219_095942_450ee6.png)

| Année | Jalon | Impact |
|---|---|---|
| 2018 | BERT (Google) [1] | Pre-Training bidirectionnel révolutionne le NLP |
| 2022 | ChatGPT (OpenAI) [2] | 100 millions d'utilisateurs en 2 mois |
| 2024 | O1 (OpenAI) | Premier Reasoning Model grand public |
| 2025 | DeepSeek-R1 [3], Claude Code [4] | Raisonnement open source + agents autonomes |
| 2026 | OpenClaw [5] | Agent autonome viral — 150K ⭐ GitHub |

<small>Sources : [1] [Google AI Blog](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) · [2] [Reuters](https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/) · [3] [GitHub DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1) · [4] [Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview) · [5] [OpenClaw](https://openclaw.ai/)</small>

---

<!-- _class: section -->

# Points clés à retenir

## Key Takeaways

---

# 37 — Récapitulatif Session 1A

### La Generative AI en contexte
- La GenAI produit du contenu — mais le ML traditionnel représente *la majorité de la valeur IA totale*

### La taxonomie de l'IA
- **Par technique** : Statistics → ML → Deep Learning → GenAI (chaque couche inclut les précédentes)
- **Par paradigme** : Supervised, Unsupervised, Self-Supervised, Reinforcement Learning
- **Par tâche** : Classification, Regression, Object Detection, Segmentation, Génération

### Ce qui fait du ML du ML (Chip Huyen)
- 5 conditions : Learn, Complex Patterns, Existing Data, Predictions, Unseen Data

### Le vocabulaire des tâches
- Les noms de tâches en anglais sont votre clé pour chercher des modèles sur HuggingFace

### Les timelines
- ML (1805–2014) → Deep Learning (1986–2017) → GenAI (2018–2026) : accélération exponentielle
