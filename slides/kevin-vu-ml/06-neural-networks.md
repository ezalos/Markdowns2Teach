---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Adapté du cours de Kevin Vu · Paris Dauphine PSL"
---
<!-- ABOUTME: Neural networks and Deep Learning — history, architectures, applications, and challenges. -->
<!-- ABOUTME: High-level business perspective for non-engineer M2 Entrepreneuriat students. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Cours 6 — Réseaux de neurones

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Plan du cours

1. **Un peu d'histoire** — des origines biologiques aux AI Winters
2. **Le Deep Learning : pourquoi maintenant ?** — la renaissance
3. **Principes de base** — comment un Neural Network apprend
4. **Architectures clés** — CNN, RNN, GAN, Encoder/Decoder
5. **Applications concrètes** — vision, génération, jeux, robotique
6. **Défis & enjeux** — explicabilité, régulation, coûts, intégrité

> **Objectif** : comprendre ce que les Neural Networks peuvent faire pour votre business, sans entrer dans les mathématiques.

---

<!-- _class: section -->

# Un peu d'histoire

## From Biological Inspiration to AI Winters

---

<!-- _class: cols -->

# 02 — L'intuition biologique

<div class="left">

### Imiter le cerveau humain

- **1943** : McCulloch & Pitts modélisent un neurone artificiel
- **1958** : Frank Rosenblatt invente le **Perceptron**
- Idée fondatrice : des unités simples, connectées en réseau, peuvent apprendre des tâches complexes

### Le rêve initial

- Reproduire la capacité d'apprentissage du cerveau
- Premières promesses très ambitieuses
- Intérêt massif des gouvernements et militaires

</div>
<div class="right">

*#TODO ADD IMAGE — frise chronologique de l'histoire des Neural Networks, des années 1940 aux années 2020*

</div>

---

# 03 — Les AI Winters : le cycle hype-déception

| Période | Phase | Ce qui s'est passé |
|---|---|---|
| **1950s–1960s** | Hype initiale | Promesses irréalistes, le Perceptron est « la machine qui pense » |
| **1969** | Douche froide | Minsky & Papert montrent les limites du Perceptron simple |
| **1970s–1980s** | 1er AI Winter | Financement coupé, recherche en déclin |
| **1986** | Renouveau | Backpropagation relance l'intérêt |
| **1990s** | 2e AI Winter | Les résultats ne suivent pas les promesses commerciales |
| **2012** | Renaissance | AlexNet écrase la compétition ImageNet |

> **Leçon pour un entrepreneur** : l'histoire de l'IA est cyclique. Savoir où l'on se situe dans le cycle aide à prendre de meilleures décisions d'investissement.

---

<!-- _class: cols -->

# 04 — La percée de 2012 : ImageNet

<div class="left">

### Le moment charnière

- **ImageNet** : base de données de 14 millions d'images, 1000 catégories
- **AlexNet** (2012) : un CNN profond réduit le taux d'erreur de 26% à 16%
- Amélioration sans précédent en un seul bond

### Pourquoi maintenant ?

- **GPU** : puissance de calcul 100x supérieure
- **Data** : Internet génère des volumes massifs
- **Algorithmes** : techniques de Deep Learning plus efficaces

</div>
<div class="right">

*#TODO ADD IMAGE — courbe de la compétition ImageNet montrant la chute du taux d'erreur après 2012*

</div>

---

# 05 — Deep Learning : un sujet central mais complexe

- Le Deep Learning est devenu **le sujet principal de recherche** en Machine Learning
- Publication scientifique en croissance exponentielle depuis 2012
- Investissements massifs : Google, Meta, OpenAI, Mistral AI

### Mais aussi des difficultés persistantes

- Besoin de **volumes de données colossaux** pour entraîner
- **Coûts de calcul** élevés (GPU, énergie)
- Un puissant **argument marketing** mais souvent mal compris

> **Question pour la classe** : Quand un fournisseur vous dit « notre solution utilise le Deep Learning », est-ce nécessairement un gage de qualité ? Pourquoi ?

---

<!-- _class: section -->

# Les principes de base

## How Neural Networks Learn

---

<!-- _class: cols -->

# 06 — Un programme universel ?

<div class="left">

### L'idée fondamentale

- Un Neural Network est un **programme qui s'adapte** aux données
- Rappel : une Machine de Turing peut simuler n'importe quel calcul
- Un réseau de neurones suffisamment grand peut **approximer n'importe quelle fonction**

### Fonctionnement par blocs

- Les données traversent des **couches** (layers) successives
- Chaque couche transforme l'information
- La sortie finale = la prédiction

</div>
<div class="right">

*#TODO ADD IMAGE — schéma simplifié d'un Neural Network avec input, hidden layers, output*

</div>

---

# 07 — Le vocabulaire essentiel

| Terme anglais | Ce que c'est en pratique |
|---|---|
| **Neuron** | Unité de calcul qui reçoit des inputs et produit un output |
| **Weights** | Les « réglages » que le réseau ajuste pendant l'entraînement |
| **Layer** | Couche de neurones — un étage de transformation |
| **Activation Function** | Fonction qui décide si un neurone « s'active » ou non |
| **Feed-Forward** | Passage des données de l'entrée vers la sortie |
| **Backpropagation** | Le réseau apprend de ses erreurs en « remontant » les corrections |
| **Perceptron** | Le neurone artificiel le plus simple |

> Pas besoin de maîtriser les maths : l'idée clé est que le réseau **ajuste ses weights** pour minimiser ses erreurs.

---

<!-- _class: cols -->

# 08 — Comment un réseau apprend (intuition)

<div class="left">

### L'analogie du photographe

1. Le réseau fait une **prédiction** (Feed-Forward)
2. On compare avec la **bonne réponse**
3. On calcule l'**erreur**
4. On ajuste les weights en **remontant** (Backpropagation)
5. On recommence des milliers de fois

### C'est comme apprendre un sport

- Au début, beaucoup d'erreurs
- À chaque essai, on corrige ses gestes
- Après des milliers de répétitions, le geste devient naturel

</div>
<div class="right">

*#TODO ADD IMAGE — schéma du cycle Feed-Forward puis Backpropagation avec flèches*

</div>

---

# 09 — Activation Functions : faire des choix

- Un neurone sans Activation Function = une simple régression linéaire
- L'Activation Function introduit de la **non-linéarité**
- C'est ce qui permet au réseau de résoudre des problèmes complexes

### Les plus courantes (pas besoin de les mémoriser)

| Fonction | Usage typique |
|---|---|
| **ReLU** | Standard dans la plupart des réseaux modernes |
| **Sigmoid** | Classification binaire (oui/non) |
| **Softmax** | Classification multi-classes (chat, chien, oiseau...) |

> **Analogie business** : l'Activation Function, c'est le filtre de décision. Sans elle, un réseau ne saurait pas dire « oui ou non » — juste « peut-être 0.47 ».

---

<!-- _class: section -->

# Les architectures clés

## CNN, RNN, GAN, Encoder/Decoder

---

<!-- _class: cols -->

# 10 — MLP : le réseau basique

<div class="left">

### Multi-Layer Perceptron

- L'architecture la plus simple : couches entièrement connectées
- Prolongement des modèles linéaires (GLM)
- Chaque neurone est connecté à tous les neurones de la couche suivante

### Limites

- Trop de connexions = trop de paramètres
- Peu efficace sur images, texte, séquences
- Remplacé par des architectures spécialisées

</div>
<div class="right">

*#TODO ADD IMAGE — schéma d'un MLP avec input layer, 2 hidden layers, output layer*

</div>

---

<!-- _class: cols -->

# 11 — CNN : la vision par ordinateur

<div class="left">

### Convolutional Neural Network

- Architecture spécialisée pour les **images**
- Utilise des **filtres** (noyaux de convolution) qui balaient l'image
- Détecte des **patterns hiérarchiques** : bords → formes → objets

### Évolution des performances sur ImageNet

| Modèle | Année | Paramètres | Précision |
|---|---|---|---|
| AlexNet | 2012 | 62M | 84.7% |
| VGGNet | 2014 | 138M | 92.3% |
| ResNet | 2015 | 60M | 95.5% |

</div>
<div class="right">

*#TODO ADD IMAGE — schéma d'un CNN montrant convolution, pooling, et classification finale*

</div>

---

# 12 — CNN : l'intuition visuelle

### Comment un filtre de convolution fonctionne

- Imaginez une **petite fenêtre** qui glisse sur l'image pixel par pixel
- À chaque position, elle calcule un score de **similarité** avec un pattern
- Premiers filtres : détectent les **bords** et les **textures**
- Filtres profonds : détectent les **objets** complets (visage, voiture...)

### Techniques clés

- **Maxpooling** : réduit la taille de l'image tout en gardant l'information importante
- **Stride** : le pas de déplacement du filtre
- **Padding** : ajoute des pixels autour de l'image pour préserver les bords

> **Business** : les CNN sont derrière la reconnaissance faciale, la conduite autonome, le contrôle qualité industriel, et le tri automatique de photos produit.

---

<!-- _class: cols -->

# 13 — RNN : traiter les séquences

<div class="left">

### Recurrent Neural Network

- Architecture spécialisée pour les **données séquentielles**
- Texte, audio, séries temporelles, vidéo
- Le réseau a une « **mémoire** » : il tient compte des éléments précédents

### Le problème de la mémoire courte

- Les RNN classiques « oublient » rapidement
- Solution : **LSTM** (Long Short-Term Memory)
- Le LSTM gère la mémoire avec des « portes » qui décident quoi retenir ou oublier

</div>
<div class="right">

*#TODO ADD IMAGE — schéma d'un RNN déplié montrant la connexion récurrente entre les étapes temporelles*

</div>

---

# 14 — RNN / LSTM : cas d'usage business

| Application | Comment ça marche | Exemple concret |
|---|---|---|
| **Traduction automatique** | Lit une phrase mot par mot, produit la traduction | Google Translate (avant 2017) |
| **Prédiction de séries temporelles** | Analyse l'historique pour prédire le futur | Prévision de ventes, cours de bourse |
| **Génération de texte** | Prédit le mot suivant à partir des précédents | Chatbots de première génération |
| **Reconnaissance vocale** | Traite le signal audio séquentiellement | Siri, Google Assistant (premières versions) |

> **Note** : depuis 2017, les architectures **Transformer** (Encoder/Decoder) ont largement remplacé les RNN/LSTM pour le texte. Mais comprendre le RNN aide à saisir l'évolution.

---

<!-- _class: cols -->

# 15 — GAN : la machine qui crée

<div class="left">

### Generative Adversarial Network

- Deux réseaux en **compétition** :
  - Le **Générateur** fabrique de fausses données
  - Le **Discriminateur** essaie de les détecter
- À force de s'affronter, le Générateur devient excellent

### Le principe en une phrase

> C'est comme un faussaire face à un expert en art : chacun s'améliore en réponse à l'autre.

</div>
<div class="right">

*#TODO ADD IMAGE — schéma du GAN avec Generator et Discriminator en boucle adversariale*

</div>

---

# 16 — GAN : applications spectaculaires

### Génération de visages

- **ThisPersonDoesNotExist.com** : des visages hyperréalistes qui n'existent pas
- Facebook a supprimé des comptes utilisant des photos générées par GAN

### Style Transfer

- Appliquer le style d'un peintre (Van Gogh, Picasso) à n'importe quelle photo
- Papier fondateur : *A Neural Algorithm of Artistic Style* (2015)
- Même applicable à la **vidéo** en temps réel

### Enjeu business

- Publicité : générer des visuels sans shooting photo
- Mode : essayage virtuel
- Immobilier : staging virtuel d'appartements

> **Question pour la classe** : si un GAN peut générer des visages parfaits, comment vérifier l'authenticité d'une photo de profil sur votre plateforme ?

---

<!-- _class: cols -->

# 17 — Encoder/Decoder : comprendre et restituer

<div class="left">

### L'architecture à deux étapes

1. **Encoder** : compresse l'information en une représentation dense (« le sens »)
2. **Decoder** : reconstruit une sortie à partir de cette représentation

### Pourquoi c'est révolutionnaire

- Permet la **traduction** : encoder une phrase en français → décoder en anglais
- Permet la **génération** : encoder une image → décoder une description textuelle
- Base de l'architecture **Transformer** (GPT, BERT, Mistral)

</div>
<div class="right">

*#TODO ADD IMAGE — schéma Encoder/Decoder avec compression au milieu et reconstruction en sortie*

</div>

---

# 18 — Encoder/Decoder : cas d'usage multi-modaux

| Input (Encoder) | Output (Decoder) | Application |
|---|---|---|
| Texte français | Texte anglais | Traduction automatique |
| Image | Texte descriptif | Sous-titrage automatique |
| Texte | Image | DALL-E, Midjourney, Stable Diffusion |
| Audio | Texte | Transcription (Whisper) |
| Texte | Audio | Synthèse vocale (TTS) |

> L'architecture Encoder/Decoder est la **brique fondamentale** derrière les LLM que vous utilisez quotidiennement (ChatGPT, Claude, Mistral Le Chat).

---

<!-- _class: section -->

# Récapitulatif des architectures

## Choosing the Right Architecture

---

# 19 — Quelle architecture pour quel problème ?

| Architecture | Spécialité | Points forts | Limites |
|---|---|---|---|
| **MLP** | Données tabulaires | Simple, rapide | Peu puissant sur données complexes |
| **CNN** | Images, vidéo | Détection de patterns visuels | Pas adapté au texte |
| **RNN / LSTM** | Séquences, texte | Mémoire temporelle | Lent, mémoire limitée |
| **GAN** | Génération | Résultats spectaculaires | Difficile à entraîner |
| **Encoder/Decoder** | Multi-modal | Très polyvalent | Coûteux en calcul |

> **Pour un entrepreneur** : vous n'avez pas besoin de choisir l'architecture vous-même. Mais comprendre les forces de chacune vous aide à **évaluer les solutions proposées**.

---

<!-- _class: section -->

# Entraîner un réseau : les défis

## Training Challenges (Simplified)

---

# 20 — Overfitting : le piège principal

### Le réseau apprend trop bien... les données d'entraînement

- Un réseau trop complexe **mémorise** au lieu d'**apprendre**
- Il fonctionne parfaitement sur les données connues, mais échoue sur les nouvelles

### Solutions en bref

| Technique | Principe | Analogie |
|---|---|---|
| **Dropout** | Désactive des neurones aléatoirement pendant l'entraînement | Forcer un élève à réviser sans ses notes |
| **Régularisation** | Pénalise les weights trop grands | Empêcher le réseau de devenir trop sûr de lui |
| **Data Augmentation** | Génère des variantes des données (rotation, zoom, bruit) | Montrer le même concept sous différents angles |

---

<!-- _class: cols -->

# 21 — Dropout : l'intuition

<div class="left">

### Comment ça marche

- À chaque étape d'entraînement, on « éteint » **aléatoirement** une partie des neurones
- Le réseau doit apprendre à être performant **sans dépendre d'un seul chemin**
- Résultat : un modèle plus **robuste** et **généralisable**

### Pourquoi ça marche (analogie)

- Une équipe qui dépend d'un seul expert est fragile
- Si chacun peut contribuer, l'organisation est résiliente
- C'est le même principe pour un Neural Network

</div>
<div class="right">

*#TODO ADD IMAGE — schéma avant/après Dropout, certains neurones barrés*

</div>

---

# 22 — Data Augmentation : plus de données sans plus de données

- Le Deep Learning est **gourmand en données**
- Collecter de nouvelles données est cher et lent
- Solution : **transformer** les données existantes

### Exemples pour les images

| Transformation | Ce que ça fait |
|---|---|
| Rotation | Tourne l'image de quelques degrés |
| Flip horizontal | Miroir gauche-droite |
| Zoom / Crop | Recadre une partie de l'image |
| Ajout de bruit | Légère perturbation des pixels |
| Changement de luminosité | Simule différentes conditions d'éclairage |

> **Business** : la Data Augmentation permet de construire un modèle performant même avec un **budget données limité** — crucial pour une startup.

---

<!-- _class: section -->

# Applications concrètes

## Real-World Deep Learning Applications

---

<!-- _class: cols -->

# 23 — Génération de visages avec les GAN

<div class="left">

### ThisPersonDoesNotExist

- Des visages **photoréalistes** générés de toutes pièces
- Aucune personne réelle n'est photographiée
- Qualité suffisante pour tromper un humain

### Les risques

- Création de **faux comptes** sur les réseaux sociaux
- Usurpation d'identité à grande échelle
- Facebook a retiré des milliers de comptes avec des photos GAN

</div>
<div class="right">

*#TODO ADD IMAGE — grille de visages générés par GAN, photorealistes*

</div>

---

# 24 — Neural Style Transfer : l'art par algorithme

- Un CNN peut **séparer le contenu et le style** d'une image
- On peut appliquer le **style de Van Gogh** à une photo de la Tour Eiffel
- Papier fondateur : Gatys et al., 2015

### Applications business

| Domaine | Usage |
|---|---|
| **Apps photo** | Prisma, filtres artistiques Instagram |
| **Publicité** | Création de visuels uniques à moindre coût |
| **Jeu vidéo** | Génération de textures et d'environnements |
| **Mode** | Prototypage de patterns textiles |

> **Vidéo** : le Style Transfer fonctionne aussi en temps réel sur la vidéo — imaginez un filtre « Monet » sur votre flux TikTok.

---

# 25 — Deepfakes : la face sombre de la génération

### Qu'est-ce qu'un Deepfake ?

- Utilise des autoencoders ou des GAN pour **remplacer un visage** dans une vidéo
- Qualité de plus en plus indistinguable de la réalité
- Le terme vient de « deep learning » + « fake »

### Les enjeux

- **Désinformation politique** : fausses déclarations de dirigeants
- **Fraude** : usurpation d'identité en vidéoconférence
- **Revenge porn** : manipulation d'images personnelles

### Les réponses

- Outils de **détection** de Deepfakes (eux-mêmes basés sur le Deep Learning)
- Régulation : EU AI Act classe les Deepfakes dans les risques élevés
- Initiatives de **watermarking** et de traçabilité des contenus générés

---

# 26 — AlphaGo : quand l'IA bat le champion du monde

- **2016** : AlphaGo (DeepMind/Google) bat Lee Sedol au jeu de Go
- Le Go a 10^170 positions possibles — impossible de tout calculer
- Combinaison de **Deep Learning** + **Reinforcement Learning**

### Pourquoi c'est important pour le business

- Preuve que l'IA peut exceller dans des **problèmes de décision complexes**
- La même approche s'applique à :
  - Optimisation logistique
  - Gestion de portefeuille
  - Pilotage de systèmes complexes

> **Ne pas confondre** : Deep Blue (échecs, 1997) = force brute de calcul. AlphaGo = véritable apprentissage. La différence est fondamentale.

---

<!-- _class: cols -->

# 27 — Génération de texte automatique

<div class="left">

### Des RNN aux Transformers

- Premiers modèles : RNN/LSTM pour prédire le mot suivant
- Révolution : architecture **Transformer** (2017)
- Aujourd'hui : GPT-4, Claude, Mistral, Llama

### Ce que ça permet

- Rédaction d'articles, de mails, de code
- Résumé automatique de documents
- Chatbots conversationnels

</div>
<div class="right">

### Ce que ça ne permet pas (encore)

- Raisonnement fiable à 100%
- Vérification factuelle intégrée
- Créativité véritablement originale

> **Question pour la classe** : si un article est entièrement rédigé par une IA, qui en est l'auteur ? Le créateur du prompt ? L'entreprise qui opère le modèle ?

</div>

---

# 28 — Reconnaissance vocale et assistants

### Le pipeline classique

1. **Audio** → Conversion en spectrogramme (image du son)
2. **CNN/RNN** → Extraction de features acoustiques
3. **Decoder** → Transcription en texte
4. **NLP** → Compréhension de l'intention

### Produits concrets

| Assistant | Entreprise | Technologie sous-jacente |
|---|---|---|
| Siri | Apple | Deep Learning + NLP |
| Google Assistant | Google | Transformer (BERT, T5) |
| Alexa | Amazon | CNN + RNN + Transformers |

> Derrière chaque « Ok Google » ou « Hey Siri », il y a un pipeline complet de Neural Networks qui travaillent en cascade.

---

# 29 — Robotique et jeux vidéo

### Reinforcement Learning + Deep Learning

- L'agent apprend par **essai-erreur** dans un environnement
- Deep Learning pour percevoir l'environnement (vision, capteurs)
- Reinforcement Learning pour prendre des décisions

### Exemples marquants

| Domaine | Réalisation | Impact |
|---|---|---|
| **Jeux vidéo** | OpenAI Five bat des pros à Dota 2 | Stratégie en temps réel |
| **Robotique** | Robots de Boston Dynamics | Navigation et manipulation |
| **Kinect** | Microsoft Xbox | Détection de posture par CNN |
| **Véhicules autonomes** | Tesla, Waymo | Perception + décision |

> **Pour un entrepreneur** : la convergence robotique + IA ouvre de nouveaux marchés en logistique, agriculture, santé, et industrie.

---

<!-- _class: section -->

# Les défis du Deep Learning

## Challenges for Business Leaders

---

# 30 — Plus de data = toujours plus de performance ?

### La promesse

- Les Neural Networks s'améliorent avec plus de données
- « Scaling laws » : performance proportionnelle à la taille des modèles et des datasets

### La réalité

- **Rendements décroissants** au-delà d'un certain volume
- La **qualité** des données compte plus que la quantité
- Des modèles plus petits, bien entraînés, peuvent battre des modèles géants

> **Conseil entrepreneur** : avant d'investir dans la collecte massive de données, vérifiez que vos données existantes sont **propres, étiquetées, et pertinentes**.

*#TODO ADD IMAGE — courbe performance vs volume de données montrant les rendements décroissants*

---

<!-- _class: cols -->

# 31 — Le problème hardware : GPU et coûts

<div class="left">

### Pourquoi les GPU ?

- Les Neural Networks font des **milliards d'opérations matricielles**
- Les GPU (Graphics Processing Units) sont conçus pour le calcul parallèle
- Un GPU peut être **10-100x plus rapide** qu'un CPU pour le Deep Learning

### Les coûts

- Entraîner GPT-4 : estimé à **100M$+**
- Un GPU H100 NVIDIA : ~30 000 EUR
- Location cloud (AWS, GCP) : 2-30 EUR/heure par GPU

</div>
<div class="right">

### Impact business

- Le Deep Learning n'est **pas gratuit**
- Le coût d'entraînement est un **barrière à l'entrée**
- Solutions pour startups :
  - **Transfer Learning** : réutiliser un modèle pré-entraîné
  - **Fine-tuning** : ajuster un modèle existant à vos données
  - **API as a Service** : payer à l'usage (OpenAI, Mistral)

</div>

---

# 32 — Transfer Learning et Fine-tuning : la stratégie startup

### Le principe

- Un modèle entraîné sur des millions d'images sait déjà « voir »
- Vous n'avez pas besoin de repartir de zéro
- Il suffit d'**ajuster les dernières couches** à votre problème spécifique

### Exemple concret

| Étape | Action | Coût |
|---|---|---|
| **Modèle de base** | ResNet pré-entraîné sur ImageNet | Gratuit (open source) |
| **Fine-tuning** | Réentraîner sur 500 images de vos produits | Quelques heures de GPU |
| **Déploiement** | API pour classifier vos images | Quelques EUR/mois |

> **C'est la stratégie dominante en 2026** : 90% des applications business utilisent des modèles pré-entraînés ajustés, pas des modèles construits de zéro.

---

<!-- _class: section -->

# Défis éthiques et sociétaux

## Ethics, Regulation, and Trust

---

# 33 — Explainability : la boîte noire

- Un Neural Network profond a **des millions de paramètres**
- Impossible d'expliquer simplement **pourquoi** il a pris une décision
- On parle de **« boîte noire »** (Black Box)

### Pourquoi c'est un problème

| Domaine | Enjeu |
|---|---|
| **Banque** | Refuser un crédit sans explication = illégal (RGPD Art. 22) |
| **Santé** | Un diagnostic doit être justifiable |
| **Justice** | Un score de récidive doit être auditable |
| **Assurance** | Un refus de couverture doit être motivé |

> **EU AI Act** : les systèmes à haut risque doivent fournir des explications compréhensibles. L'Explainability n'est plus optionnelle.

---

# 34 — Adversarial Attacks : tromper un réseau

### Le concept

- En modifiant **quelques pixels** d'une image, on peut tromper un CNN
- Le changement est **invisible** pour un humain
- Le réseau peut confondre un panda avec un gibbon

### Implications business

- **Sécurité** : un véhicule autonome peut être trompé par un sticker sur un panneau stop
- **Fraude** : contourner les systèmes de vérification d'identité
- **Confiance** : les clients acceptent-ils qu'un système aussi fragile prenne des décisions ?

> La robustesse aux Adversarial Attacks est un **critère de qualité** à vérifier chez vos fournisseurs d'IA.

*#TODO ADD IMAGE — exemple d'adversarial attack : image originale + perturbation = mauvaise classification*

---

# 35 — Régulation : le cadre européen

### EU AI Act (entré en vigueur 2024-2026)

- **Risque inacceptable** : interdit (scoring social, manipulation subliminale)
- **Haut risque** : réglementé (santé, justice, recrutement, crédit)
- **Risque limité** : obligations de transparence (chatbots, Deepfakes)
- **Risque minimal** : libre (filtres photo, jeux)

### Ce que ça signifie pour votre startup

- Classifier votre application IA selon le **niveau de risque**
- Documenter votre **pipeline de données** et vos choix de modèle
- Prévoir un **budget conformité** dès le départ

> **Question pour la classe** : votre startup développe un outil de présélection de CV par IA. Dans quelle catégorie de risque se situe-t-il selon l'EU AI Act ?

---

# 36 — Reproductibilité : un défi technique

- Deux entraînements du **même modèle** sur les **mêmes données** peuvent donner des résultats différents
- Sources de variabilité : initialisation aléatoire, ordre des données, parallélisme GPU

### Pourquoi c'est important

| Pour la recherche | Pour le business |
|---|---|
| Vérifier les résultats publiés | Garantir la stabilité du produit |
| Comparer les approches équitablement | Auditer les décisions du modèle |
| Détecter les erreurs | Satisfaire les exigences réglementaires |

> **Bonne pratique** : exigez de votre équipe technique qu'elle **sauvegarde** le modèle, les données, et la configuration exacte de chaque entraînement.

---

<!-- _class: section -->

# Récapitulatif

## Key Takeaways

---

# 37 — Ce qu'il faut retenir

### Histoire et contexte

- L'IA est cyclique : **hype → déception → percée**. Nous sommes dans une phase de percée depuis 2012
- Le Deep Learning fonctionne grâce à la convergence **data + GPU + algorithmes**

### Les architectures en un coup d'oeil

- **CNN** = images | **RNN/LSTM** = séquences | **GAN** = génération | **Encoder/Decoder** = transformation

### Pour l'entrepreneur

- **Transfer Learning** et **Fine-tuning** : la stratégie dominante pour les startups
- L'Explainability et la régulation ne sont **pas optionnelles** en Europe
- Plus de data n'est pas toujours la réponse — la **qualité prime**

---

# 38 — Matrice de décision pour votre projet

| Question | Si oui... | Si non... |
|---|---|---|
| Avez-vous beaucoup de données étiquetées ? | Envisagez le Supervised Deep Learning | Explorez le Transfer Learning ou les APIs |
| Votre problème concerne des images ? | Orientez-vous vers les CNN | Considérez d'autres architectures |
| Avez-vous besoin d'explicabilité ? | Préférez des modèles interprétables | Le Deep Learning est une option viable |
| Votre budget GPU est limité ? | Utilisez des modèles pré-entraînés et des APIs | Vous pouvez entraîner vos propres modèles |
| Votre domaine est réglementé ? | Prévoyez conformité EU AI Act dès le jour 1 | Restez vigilant, la régulation évolue |

> **Pour la prochaine séance** : identifiez un cas d'usage dans votre projet entrepreneurial qui pourrait bénéficier du Deep Learning. Précisez le type de données, l'architecture probable, et les risques.
