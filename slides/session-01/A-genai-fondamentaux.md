---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"
---

<!-- ABOUTME: Introduction à la Generative AI — concepts, capacités (Writing/Reading/Chatting) et génération d'images. -->
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

![](assets/A/suno.png)
[Suno](https://suno.com/s/TDY3F2UiDfBxkIVI)

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

# 08 — Ce que vous allez apprendre

Trois piliers pour maîtriser la Generative AI en tant qu'entrepreneur :

| Pilier | Ce que vous saurez faire |
|---|---|
| *Comprendre la technologie* | Ce que l'IA peut et ne peut pas faire, les cas d'usage |
| *Construire des projets GenAI* | Identifier, cadrer et construire des solutions IA |
| *Impact business et société* | Comment les équipes peuvent en tirer parti, risques et IA responsable |

> Objectif du cours : vous donner les clés de décision, pas vous transformer en Data Scientists.

---

<!-- _class: cols -->

# 09 — Les grandes familles de l'IA

<div class="left">

| Type | Principe | Exemple business |
|------|----------|-----------------|
| **Supervised Learning** | Input A → Output B | Email → spam ? |
| **Unsupervised Learning** | Patterns sans labels | Segmentation clients |
| **Reinforcement Learning** | Essai/erreur + récompense | Trading algorithmique |
| **Generative AI** | Génère du contenu original | Texte, images, code |

> Les slides suivantes détaillent chaque famille avec des exemples concrets.

</div>
<div class="right">

![](assets/A/ai-onion-raghunitb.png)

</div>

---

# 10 — Supervised, Unsupervised & Reinforcement Learning

Comment l'algorithme interagit avec les données — chaque approche répond à un type de problème différent.

![bg right:50% contain](assets/A/unsupervise-supervise-reinforcement.png)

---

# 11 — Supervised Learning — exemples business

| Input (A) | Output (B) | Application métier |
|---|---|---|
| Email | Spam ? (0/1) | Filtrage automatique |
| Pub + profil utilisateur | Clic ? (0/1) | Publicité ciblée |
| Image radar | Position véhicules | Conduite autonome |
| Image radio | Diagnostic | Healthcare |
| Photo produit | Défaut ? (0/1) | Contrôle qualité |
| Enregistrement audio | Transcription texte | Speech Recognition |
| Avis client | Sentiment (pos/neg) | Veille e-réputation |

> *Pour un entrepreneur* : le Supervised Learning (classification, prédiction) reste la technologie IA la plus *rentable* en production [1]. La Generative AI l'a dépassé en fréquence de déploiement depuis 2024 [2], mais croissance ≠ revenus prouvés.

<small>Sources : [1] [McKinsey State of AI 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024) · [2] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-05-07-gartner-survey-finds-generative-ai-is-now-the-most-frequently-deployed-ai-solution-in-organizations)</small>

---

# 12 — Unsupervised Learning — exemples business


| Data mix  | Application métier |
| --------- | ------------------ |
| Application data usage | Customer Segmentation |
| Product reviews | Complains clustering |
| Forum Chats | Topic Modeling |
| Netflix videos | Recommender Systems |

---

# 13 — Reinforcement Learning — exemples business


| Simulateur               | Application métier    |
| ---------------------- | --------------------- |
| Driving simulator | Self-driving car |
| Physic similutor | Robotics pre-training |
| Website users influx | News Recommendation |
| Trading exchange | Algorithmic Trader |

---

# 14 — Pourquoi l'IA explose maintenant

![bg right:45% contain](assets/A/history-of-AI.png)

*2010–2020 : l'ère du Large Scale Supervised Learning*

- La performance des modèles IA augmente avec *plus de données* et des *modèles plus grands*
- Les petits modèles plafonnent vite — les grands modèles continuent de progresser
- Cela a motivé la course au *scale* : plus de compute, plus de data

*2020+ : l'ère des Large Language Models*

- Application du même principe au texte : entraîner des modèles *massifs* sur des *centaines de milliards de mots*
- Résultat : des modèles capables de générer du texte de qualité humaine

---

# 15 — La preuve par les données

![bg right:45% contain vertical](assets/A/epoch-ai-dataset_size.png)
![bg contain](assets/A/METR-task-len-horizon.png)

- La taille des datasets d'entraînement croît de manière exponentielle [1]
- Les tâches que l'IA peut accomplir de manière autonome s'allongent rapidement [2]

> Ces deux courbes expliquent pourquoi chaque trimestre apporte des capacités IA que personne n'anticipait un an plus tôt.

<small>Sources : [1] [EpochAI](https://epoch.ai/data-insights/dataset-size-trend) · [2] [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)</small>


---

# 16 — Comment fonctionnent les LLMs

Les LLMs utilisent le Supervised Learning pour *prédire le mot suivant*, mot par mot :

| Input (A) | Output (B) |
|---|---|
| My favorite food is a | *bagel* |
| My favorite food is a bagel | *with* |
| My favorite food is a bagel with | *cream* |
| My favorite food is a bagel with cream | *cheese* |

> Un LLM entraîné sur des centaines de milliards de mots apprend les patterns du langage et devient capable de générer du texte cohérent et pertinent.

![](assets/A/lllm-gen-example.png)

---

# 17 — Les LLMs comme partenaire de réflexion

Un LLM n'est pas juste un moteur de recherche amélioré. C'est un *Writing Partner* :

- *Réécriture* : "Reformule ce paragraphe pour plus de clarté"
- *Création* : "Écris une histoire de 300 mots pour enfants sur le brossage de dents"
- *Analyse* : "Quels sont les points faibles de mon business plan ?"

*Différence clé avec Google* :
- *Web Search* : retrouve des pages existantes
- *LLM* : synthétise et génère du contenu original

---

<!-- _class: section -->

# Applications GenAI : Writing, Reading, Chatting

## The Three Families of LLM Tasks

---

# 18 — Les trois familles de tâches LLM

| Catégorie | Exemples | Type d'app |
|---|---|---|
| *Writing* | Brainstorming noms de produits, communiqués de presse, traduction | Web + App |
| *Reading* | Classification d'emails, résumé de conversations, analyse de sentiment | Surtout App |
| *Chatting* | Service client bot, coaching, FAQ interne | Web + App |

*Deux modes d'utilisation* :
- *Web-based* : ChatGPT, Claude, Le Chat — interaction directe
- *Software application* : le LLM est intégré dans un produit (email routing, analyse automatisée)

![bg right:45% contain](assets/ng01/img-026.png)

---

# 19 — Writing : brainstorming et rédaction assistée

Les LLMs excellent pour le *brainstorming* — tâche à faible risque et forte valeur créative :

*Exemples pour entrepreneurs* :
- "Propose 5 noms créatifs pour une marque de cookies au beurre de cacahuète"
- "Donne 5 idées pour augmenter les ventes en Q4"
- "Suggère 3 angles marketing pour cibler les étudiants"

*Rédaction assistée* — plus vous donnez de *contexte*, meilleur est le résultat :
- Prompt vague → résultat générique (texte rempli de [placeholders])
- Prompt détaillé avec contexte → résultat personnalisé et exploitable

> *Astuce* : ne prenez jamais la première réponse. Itérez, combinez, affinez.

---

# 20 — Reading : résumer et classifier

Un des cas d'usage les plus puissants pour les entreprises :

*Résumé* :
- Synthèse de rapports de 50+ pages en bullet points
- Traitement de 100 feedbacks clients en 5 minutes au lieu de 2 heures

*Classification automatique* :
- Routage d'emails vers le bon département
- Analyse de sentiment (avis positifs/négatifs)
- Veille e-réputation automatisée

> *Clé du succès* : un bon prompt de classification a 3 éléments — la *tâche*, les *choix possibles*, et les *données* à analyser.

![bg right:45% contain](assets/ng01/img-024.png)

---

# 21 — Chatting : du bot interne au service client

*BettaBurgers* — un chatbot de prise de commande sans friction, sans attente téléphonique.

*Le spectre de déploiement* :

| Niveau | Description | Risque |
|---|---|---|
| *Humains seuls* | Agents humains uniquement | Zéro risque IA |
| *Bot assiste l'humain* | Le bot suggère, l'humain décide | Faible |
| *Bot trie, humain traite* | Le bot oriente les demandes | Moyen |
| *Bot seul* | Le bot gère tout sans humain | Élevé |

> *Conseil* : commencer par un chatbot *interne* → ajouter un *Human-in-the-Loop* → puis ouvrir au client final.

---

<!-- _class: section -->

# Génération d'images par IA

## Image Generation with Diffusion Models

---

# 22 — La génération d'images par IA

Les modèles de génération d'images créent des visuels à partir de *descriptions textuelles* :

*Outils majeurs en 2026* :
- *Midjourney* [1] — qualité artistique, très populaire
- *DALL-E 3* (OpenAI) [2] — intégré à ChatGPT
- *Flux* (Black Forest Labs) [3] — open source, haute qualité
- *Stable Diffusion* [4] — open source, très personnalisable

*Pour les entrepreneurs* :
- Prototypage visuel rapide et quasi gratuit
- A/B testing de visuels marketing
- Attention aux *droits d'auteur* — sujet juridique en évolution

![bg right:40% contain](assets/ng01/img-028.png)
![bg contain](assets/ng01/img-030.png)
![bg contain](assets/ng01/img-029.png)

<small>Sources : [1] [Midjourney](https://www.midjourney.com/) · [2] [OpenAI DALL-E](https://openai.com/dall-e-3) · [3] [Black Forest Labs](https://blackforestlabs.ai/) · [4] [Stability AI](https://stability.ai/)</small>

---

# 23 — Comment ça marche : les Diffusion Models

Le principe est élégant — on entraîne un modèle à *enlever du bruit* d'une image :

![](assets/A/diffusion_model.gif)

*Phase d'entraînement* :
1. Prendre une image nette (ex : une pomme)
2. Ajouter du bruit progressivement
3. Entraîner le modèle : image bruitée → image moins bruitée

*Phase de génération* :
1. Partir de *bruit pur* (image aléatoire)
2. Appliquer le modèle ~100 fois de suite
3. L'image émerge progressivement du bruit

> C'est comme un sculpteur qui retire la pierre pour révéler la statue — sauf que le sculpteur est un réseau de neurones.

---

<!-- _class: section -->

# Ce que l'IA sait et ne sait pas faire

## Capabilities and Limitations

---

# 24 — Le test du "fresh college grad"

Comment évaluer si un LLM peut réaliser une tâche ? Utilisez cette heuristique :

> *Un jeune diplômé compétent pourrait-il suivre les instructions du prompt pour accomplir la tâche ?*

- Classifier un email comme réclamation ? *Oui* → le LLM peut le faire
- Rédiger un communiqué de presse *sans aucune info* ? *Difficilement* → résultat générique
- Rédiger un communiqué *avec le contexte* ? *Oui* → bon travail

*Limites de l'analogie* — imaginez un diplômé *sans aucune ressource externe* :
- Pas d'accès Internet, pas de formation spécifique, pas de mémoire des tâches précédentes

> C'est l'heuristique la plus utile du cours. Gardez-la en tête pour évaluer chaque cas d'usage.

---

# 25 — Hallucinations et Knowledge Cutoffs

*Hallucinations* — le LLM *invente des informations avec un ton très confiant* :
- Un avocat américain a soumis un mémoire juridique contenant des *affaires inventées* par ChatGPT [1]
- Règle d'or : ne jamais publier un contenu IA sans *vérification humaine*

*Knowledge Cutoffs* — l'IA vit dans le passé :
- Les connaissances sont *figées à la date d'entraînement*
- Les données de la semaine dernière restent inaccessibles (sauf accès web)

![bg right:45% contain](assets/ng01/img-022.png)

*Question pour la classe* : Quelles informations de votre entreprise ne devriez-vous JAMAIS mettre dans un prompt ChatGPT ?

<small>Sources : [1] [NYT](https://www.nytimes.com/2023/05/27/nyregion/avianca-chatgpt-fake-citations.html)</small>

---

# 26 — Récapitulatif — ce que l'IA sait et ne sait pas faire

| L'IA *sait* faire | L'IA *ne sait pas* (encore) faire |
|---|---|
| Résumer des documents | Raisonner de manière fiable sur des sujets complexes |
| Classifier du texte (sentiment, catégorie) | Accéder à des données en temps réel (sans outils) |
| Traduire et adapter le ton | Garantir la véracité de ses réponses |
| Brainstormer et générer du contenu | Comprendre le contexte spécifique de votre entreprise |
| Générer des images à partir de texte | Travailler sur des données structurées/tabulaires |
| Corriger et réécrire | Remplacer le jugement humain sur des décisions critiques |

> Testez avec l'heuristique du *fresh college grad* : si un jeune diplômé pourrait le faire avec les instructions du prompt, le LLM peut probablement le faire aussi.

---

# 27 — Points clés à retenir

*Comprendre* :
- La Generative AI produit du contenu (texte, image, audio, vidéo) à partir de prompts
- Les LLMs fonctionnent par *prédiction du mot suivant* à très grande échelle

*Appliquer* :
- Trois familles de tâches : *Writing*, *Reading*, *Chatting*
- Les tâches de *Reading* sont souvent les plus rentables (automatisation)
- Déployez progressivement : interne → human-in-the-loop → client final

*Rester vigilant* :
- Les *Hallucinations* sont un risque réel — toujours vérifier
- Les *biais* existent — tester avant de déployer
- Le *Prompt Engineering* est une compétence itérative, pas un don

> *Suite* : Session 1B — L'IA au-delà des LLMs
