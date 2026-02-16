---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Kevin Vu / Dauphine"
---

<!-- ABOUTME: L'IA au-delà des LLMs — prompting, taxonomie IA, histoire, architectures et reasoning models. -->
<!-- ABOUTME: Seconde moitié de la Session 1, enrichie de Kevin Vu et des données recherche 2025. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 1B — L'IA au-delà des LLMs

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Bien prompter

## Tips for Prompting

---

# 01 — Les 3 principes du Prompting

| Principe | Description |
|---|---|
| *1. Soyez détaillé et spécifique* | Donnez assez de contexte pour que le LLM comprenne exactement ce que vous voulez |
| *2. Guidez le raisonnement* | Décomposez les tâches complexes en étapes (Chain-of-Thought) |
| *3. Expérimentez et itérez* | Il n'existe pas de prompt parfait — améliorez par itération |

> Le Prompt Engineering n'est pas un talent mystique. C'est une *compétence itérative* que tout le monde peut développer.

---

# 02 — Principe 1 : soyez détaillé et spécifique

*Mauvais prompt* : *"Aide-moi à écrire un email pour rejoindre le projet."*

*Bon prompt* :
*"Help me write an email asking to be assigned to the legal documents project. I have ample experience prompting LLMs to generate accurate text in a professional tone. Write a paragraph explaining why my background makes me a strong candidate."*

*Règles* :
- Donnez le *contexte* (qui vous êtes, quel est le projet)
- Décrivez la *tâche* en détail
- Précisez le *format* de sortie souhaité
- Spécifiez le *ton* (professionnel, décontracté, technique)

---

# 03 — Principe 2 : guidez le raisonnement (Chain-of-Thought)

Décomposer une tâche complexe en *étapes explicites* améliore la qualité :

*Prompt* : *"Brainstorm 5 names for a new cat toy.*
*Step 1: Come up with 5 fun, joyful words that relate to cats.*
*Step 2: For each word, come up with a rhyming name for a toy.*
*Step 3: For each toy name, add a fun, relevant emoji."*

| Step 1 | Step 2 | Step 3 |
|---|---|---|
| Purr | Purr-Twirl | Purr-Twirl 🐱 |
| Whisker | Whisker-Whisper | Whisker-Whisper 😺 |
| Pounce | Pounce-Bounce | Pounce-Bounce 🏀 |

> Ce principe est la base du *Chain-of-Thought Prompting*, technique clé des Reasoning Models (suite du cours).

---

# 04 — Principe 3 : expérimentez et itérez

Il n'existe *pas de prompt parfait universel* — mais un *processus* pour s'améliorer :

1. *Écrivez* un premier prompt (ne réfléchissez pas trop)
2. *Évaluez* la sortie — qu'est-ce qui manque ?
3. *Affinez* le prompt (ajoutez du contexte, changez le format)
4. *Répétez* jusqu'à satisfaction

*Le cycle du Prompt Engineering* = le *cycle produit* des startups :

*Idée → Prompt → Réponse LLM → Évaluation → Nouveau prompt → ...*

![bg right:45%](assets/ng01/img-027.png)

> Ne sur-réfléchissez pas le premier prompt — *lancez-vous vite* et itérez.

---

<!-- _class: section -->

# L'IA : taxonomie et histoire

## AI Taxonomy and History

---

<!-- _class: cols -->

# 05 — Machine Learning, Data Mining, Statistics

<div class="left">

### Trois termes, un même objectif ?

- *Statistics* : quantifier les données d'un échantillon, estimer le comportement d'une population
- *Machine Learning* : apprentissage à partir d'un jeu de données pour prédire ou estimer
- *Data Mining* : détection de patterns et de structures cachées dans les données

> En pratique, les frontières sont floues. Un entrepreneur doit comprendre ce que chaque approche peut *résoudre*.

</div>
<div class="right">

### Quand utiliser quoi ?

| Critère | Supervised | Unsupervised |
|---|---|---|
| Données étiquetées ? | Oui | Non |
| Objectif précis ? | Oui | Exploratoire |
| Cas typique | Prédiction | Segmentation |

> *Question* : Vous lancez une marketplace. La détection de faux avis est-elle du Supervised ou Unsupervised Learning ?

</div>

---

<!-- _class: cols -->

# 06 — Structured vs. Unstructured Data

<div class="left">

### Données structurées (tabulaire)
- Tableaux, bases de données, CSV
- Ex : CRM, comptabilité, logs serveur
- *Le ML classique est souvent meilleur* — LLMs non optimisés

</div>
<div class="right">

### Données non structurées
- Texte, images, audio, vidéo
- Ex : emails clients, photos produit, appels SAV
- *Terrain de jeu de la Generative AI*

> **80%** des données d'entreprise sont non structurées [1]

</div>

> *Règle pratique* : si votre cas repose sur un *tableur*, pensez ML classique. S'il repose sur du *texte libre*, pensez Generative AI.

<small>Sources : [1] [IDC — Data Age 2025](https://www.seagate.com/files/www-content/our-story/trends/files/idc-seagate-dataage-whitepaper.pdf)</small>

---

<!-- _class: section -->

# L'histoire de l'IA : les cycles hype-déception

## AI Winters and the Road to Deep Learning

---

# 07 — L'IA a une histoire cyclique

- *1950s–1960s* : Hype initiale — le Perceptron est « la machine qui pense »
- *1970s–1990s* : Deux AI Winters — financement coupé, promesses non tenues
- *2012* : Renaissance — AlexNet écrase ImageNet
- *2017* : Transformer — « Attention Is All You Need »
- *2022+* : Ère GenAI — ChatGPT, Claude, Mistral, adoption de masse

> *Leçon pour un entrepreneur* : connaître le cycle aide à évaluer les promesses. Nous sommes en phase de percée depuis 2012 — mais les déceptions passées sont instructives.

![bg right:50%](assets/infographics/ai-history_run_20260216_171305_8a5d6f.png)

---

# 08 — La percée de 2012 : ImageNet et le Deep Learning

*Le Deep Learning = convergence* de trois facteurs :
- *GPU* — puissance de calcul 100x supérieure
- *Data* — Internet génère des volumes massifs
- *Algorithmes* — techniques de Deep Learning plus efficaces

*AlexNet* (2012) réduit le taux d'erreur ImageNet de 26% à 15% [1] [2]. Quand les trois facteurs sont réunis, les performances explosent.

![bg right:50%](assets/infographics/dl-convergence_run_20260216_171308_a41957.png)

<small>Sources : [1] [Deng et al. 2009](https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf) · [2] [Krizhevsky et al. 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)</small>

---

<!-- _class: section -->

# Tour des architectures

## CNN, RNN, GAN, Transformer

---

# 09 — Quelle architecture pour quel problème ?

Cinq familles d'architectures, chacune optimisée pour un type de données :

- *CNN* — images et vidéo (détection de patterns visuels)
- *RNN / LSTM* — séquences et texte (mémoire temporelle)
- *GAN* — génération (compétition générateur vs discriminateur)
- *Encoder/Decoder* — multi-modal (traduction, sous-titrage)
- *Transformer* — texte, code, multi-modal (base de GPT, Claude, Mistral)

> *Pour un entrepreneur* : comprendre les forces de chaque architecture aide à *évaluer les solutions proposées*.

![bg right:55%](assets/infographics/architectures_run_20260216_171312_60551f.png)

---

<!-- _class: cols -->

# 10 — CNN : la vision par ordinateur

<div class="left">

### Convolutional Neural Network

- Architecture spécialisée pour les *images*
- Utilise des *filtres* qui balaient l'image
- Détecte des *patterns hiérarchiques* : bords → formes → objets

### Applications business

- Reconnaissance faciale
- Conduite autonome
- Contrôle qualité industriel
- Tri automatique de photos produit

</div>
<div class="right">

### Évolution sur ImageNet (top-5)

| Modèle | Année | Précision |
|---|---|---|
| AlexNet | 2012 | 84,7% [1] |
| VGGNet | 2014 | 92,7% [2] |
| ResNet | 2015 | 95,5% [3] |

> En 3 ans, la précision est passée de 85% à 96% — une accélération sans précédent.

<small>Sources : [1] [Krizhevsky et al. 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) · [2] [Simonyan & Zisserman 2014](https://arxiv.org/abs/1409.1556) · [3] [He et al. 2015](https://arxiv.org/abs/1512.03385)</small>

</div>

---

<!-- _class: cols -->

# 11 — RNN & GAN : séquences et génération

<div class="left">

### RNN / LSTM — les séquences

- Spécialisé pour texte, audio, séries temporelles
- Le réseau a une « *mémoire* » des éléments précédents
- Utilisé pour traduction, prédiction, reconnaissance vocale
- *Remplacé* depuis 2017 par les Transformers pour le texte

</div>
<div class="right">

### GAN — la génération

- Deux réseaux en *compétition* : Générateur vs Discriminateur
- Le Générateur fabrique des fausses données, le Discriminateur les détecte
- Applications : visages synthétiques, style transfer, deepfakes

> Comme un faussaire face à un expert en art : chacun s'améliore en réponse à l'autre.

</div>

---

# 12 — Encoder/Decoder et Transformer : la brique fondamentale

*L'architecture à deux étapes* :
1. *Encoder* : compresse l'information en une représentation dense (« le sens »)
2. *Decoder* : reconstruit une sortie à partir de cette représentation

*Exemples* : traduction (texte → texte), sous-titrage (image → texte), DALL-E (texte → image), Whisper (audio → texte)

> L'architecture Encoder/Decoder est la *brique fondamentale* derrière les LLMs que vous utilisez quotidiennement (ChatGPT, Claude, Mistral Le Chat).

![bg right:50%](assets/infographics/encoder-decoder_run_20260216_171310_3b56bd.png)

---

<!-- _class: section -->

# Reasoning Models : quand l'IA apprend à réfléchir

## From Next-Token Prediction to Multi-Step Reasoning

---

# 13 — Trois disruptions simultanées

Trois disruptions transforment le paysage IA en 2025 :

1. *Des modèles qui "réfléchissent"* — les Reasoning Models décomposent un problème en étapes avant de répondre, atteignant *96,7%* sur des olympiades de mathématiques [1]
2. *Un effondrement des coûts* — le coût d'inference a été divisé par *280* en 2 ans [2]
3. *L'IA dans la poche* — les Small Language Models tournent sur un smartphone, sans cloud, sans latence

> En tant qu'entrepreneur, comprendre ce paysage = savoir *quel modèle utiliser, quand, et à quel prix*.

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 14 — Chain-of-Thought : penser avant de répondre

*Ce que font les Reasoning Models différemment* :

- *Extended Thinking* — le modèle génère une chaîne de raisonnement *avant* de répondre
- *Token budget* — plus on alloue de "thinking tokens", meilleure est la réponse (mais plus cher)
- *Vérification interne* — le modèle vérifie ses propres étapes, réduisant les hallucinations

| Modèle | AIME 2024 (maths) | Prix input / 1M tokens |
|--------|-----------|-----------------|
| GPT-4o | ~26% | $2,50 |
| o1 | 74,3% | $15,00 |
| o3 | 91,6% | $2,00 |
| o4-mini | 93,4% | $1,10 |

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning)</small>

---

<!-- _class: cols -->

# 15 — Small Language Models : l'IA dans la poche

<div class="left">

### 5 avantages pour startups

1. *10-30x moins cher* — Phi-4 à $0,07/1M vs GPT-4o à $2,50/1M [1]
2. *On-device* — pas de cloud, pas de latence
3. *< 2s de latence* — seuil TTFT standard [3]
4. *Données locales = RGPD friendly* [2]
5. *Fine-tuning abordable* — $50-500 via LoRA [4]

</div>
<div class="right">

### SLMs à connaître

| Modèle | Params | Force clé |
|--------|--------|-----------|
| Phi-4 | 14B | Math rivale 70B |
| Mistral Small 3 🇫🇷 | 24B | 27 langues |
| Gemma 3 | 1-27B | On-device |
| SmolLM2 🇫🇷 | 1,7B | Raspberry Pi |

</div>

> Les SLMs ne remplacent pas les Frontier Models — ils les *complètent* pour les tâches simples et sensibles.

<small>Sources : [1] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [MLCommons](https://mlcommons.org/2025/09/small-llm-inference-5-1/) · [4] [Stratagem Systems](https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026)</small>

---

# 16 — Matrice de décision : quel modèle pour quel usage ?

| Use case | Modèle recommandé | Coût / mois | Pourquoi |
|----------|--------------------|-------------|----------|
| Support client | Mistral Small 3 (24B) | ~€150 | Rapide, multilingue, Apache 2.0 |
| Analyse complexe | o3 + Mistral Large 3 | ~€500 | Reasoning pour cas difficiles |
| App mobile offline | Gemma 3 / Phi-4 mini | ~€0 | On-device, pas de cloud |
| Génération de code | Claude Opus 4.6 / Devstral 2 | ~€300 | SWE-bench SOTA |
| Extraction de données | GPT-4o + o4-mini (hybride) | ~€200 | Routing coût/précision |

> *Règle d'or* : le bon modèle pour la bonne tâche > le plus gros modèle pour toutes les tâches.

<small>Sources : [1] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning) · [2] [SWE-bench](https://www.swebench.com/)</small>

---

<!-- _class: section -->

# Biais, éthique et IA responsable

## Ethics and Responsible AI

---

# 17 — Biais et toxicité dans les LLMs

Les LLMs *reflètent les biais* présents dans leurs données d'entraînement :

*Exemple de biais de genre* :
- "The surgeon walked to the parking lot and took out *his* car keys."
- "The nurse walked to the parking lot and took out *her* phone."

| Enjeu | Question clé | Exemple |
|---|---|---|
| *Fairness* | Les données sont-elles représentatives ? | Biais de genre dans le recrutement |
| *Vie privée* | Quelles données collecte-t-on ? | RGPD et droit à l'oubli |
| *Contrôle* | Qui est responsable des décisions ? | Le chatbot Tay de Microsoft (2016) |

> *Pour les entrepreneurs* : l'éthique n'est pas un frein — c'est un *avantage compétitif*. Les entreprises qui intègrent la responsabilité IA dès le départ sont mieux positionnées face au EU AI Act.

---

# 18 — Discussion : biais et responsabilité

> *Scénario* : votre startup utilise un LLM pour présélectionner des CV. Vous découvrez que le modèle favorise systématiquement les candidats masculins pour les postes techniques.

*Questions pour la classe* :

- Qui est légalement responsable ? Vous ? Le fournisseur du modèle ? Les deux ?
- Comment tester le biais *avant* de déployer en production ?
- Le EU AI Act classe le recrutement IA en « haut risque » — quelles obligations en découlent ?

> L'éthique de l'IA sera approfondie en Session 5. Mais dès aujourd'hui, retenez : *tester le biais avant de déployer, pas après*.

---

<!-- _class: section -->

# Récapitulatif Session 1

## Key Takeaways

---

# 19 — Ce qu'il faut retenir

### Comprendre la GenAI (Session 1A)
- La Generative AI produit du contenu à partir de prompts — *Writing, Reading, Chatting*
- Les LLMs fonctionnent par *prédiction du mot suivant* à très grande échelle
- Déployez progressivement : *interne → human-in-the-loop → client final*

### Au-delà des LLMs (Session 1B)
- *Prompt Engineering* : détail + Chain-of-Thought + itération
- L'IA a une histoire cyclique : *hype → déception → percée*
- Les architectures clés : *CNN (images), RNN (séquences), GAN (génération), Transformer (tout)*
- *Reasoning Models* + *Small Language Models* = le bon modèle pour la bonne tâche
- L'éthique et le biais sont *intégrés dès le jour 1*, pas optionnels

> *Prochaine session* : passer de l'utilisation à la *construction* de projets IA.
