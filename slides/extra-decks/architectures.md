---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Extra · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Tour des architectures de Deep Learning — CNN, RNN, GAN, Encoder/Decoder, Transformer. -->
<!-- ABOUTME: Deck optionnel extrait de la Session 1A pour approfondissement technique. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Tour des architectures

## CNN, RNN, GAN, Transformer

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Tour des architectures

## CNN, RNN, GAN, Transformer

---

# 01 — Quelle architecture pour quel problème ?

Cinq familles d'architectures, chacune optimisée pour un type de données :

- *CNN* — images et vidéo (détection de patterns visuels)
- *RNN / LSTM* — séquences et texte (mémoire temporelle)
- *GAN* — génération (compétition générateur vs discriminateur)
- *Encoder/Decoder* — multi-modal (traduction, sous-titrage)
- *Transformer* — texte, code, multi-modal (base de GPT, Claude, Mistral)

> *Pour un entrepreneur* : comprendre les forces de chaque architecture aide à *évaluer les solutions proposées*.

![bg right:55% contain](assets/infographics/architectures_run_20260216_171312_60551f.png)

---

<!-- _class: cols -->

# 02 — CNN : la vision par ordinateur

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

# 03 — RNN & GAN : séquences et génération

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

# 04 — Encoder/Decoder et Transformer : la brique fondamentale

*L'architecture à deux étapes* :
1. *Encoder* : compresse l'information en une représentation dense (« le sens »)
2. *Decoder* : reconstruit une sortie à partir de cette représentation

*Exemples* : traduction (texte → texte), sous-titrage (image → texte), DALL-E (texte → image), Whisper (audio → texte)

> L'architecture Encoder/Decoder est la *brique fondamentale* derrière les LLMs que vous utilisez quotidiennement (ChatGPT, Claude, Mistral Le Chat).

![bg right:50% contain](assets/infographics/encoder-decoder_run_20260216_171310_3b56bd.png)
