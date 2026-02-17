---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0"
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

![bg right:50% contain](assets/A/suno.png)
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

# 08 — Comment l'IA apprend-elle ?

Vous avez vu ce que l'IA *produit* — mais comment *apprend*-elle ?

| Approche | Analogie | Données requises |
|---|---|---|
| **Supervised Learning** | Un professeur corrige des copies | Exemples étiquetés (input → output) |
| **Unsupervised Learning** | Un explorateur classe ses découvertes | Données brutes, sans étiquettes |
| **Reinforcement Learning** | Un enfant apprend par essai-erreur | Environnement + signal de récompense |

> Chaque approche résout un type de problème différent. Les slides suivantes détaillent chaque famille.

![bg right:40% contain](assets/A/unsupervise-supervise-reinforcement.png)

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
| Image radio | Diagnostic | Healthcare |
| Photo produit | Défaut ? (0/1) | Contrôle qualité |
| Avis client | Sentiment (pos/neg) | Veille e-réputation |

> *Pour un entrepreneur* : le Supervised Learning reste la technique IA la plus *rentable* en production [1]. La Generative AI l'a dépassé en déploiement depuis 2024 [2], mais croissance ≠ revenus prouvés.

![bg right:45% contain](assets/infographics/supervised-learning-pipeline_run_20260217_010840_95e2a7.png)

<small>Sources : [1] [McKinsey State of AI 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024) · [2] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2024-05-07-gartner-survey-finds-generative-ai-is-now-the-most-frequently-deployed-ai-solution-in-organizations)</small>

---

# 12 — Unsupervised Learning — exemples business

L'Unsupervised Learning découvre des *patterns cachés* dans les données — sans étiquettes, sans supervision humaine.

| Données brutes | Pattern découvert | Application métier |
|---|---|---|
| Historique d'achats | Groupes de clients similaires | Segmentation marketing |
| Avis produits | Thèmes récurrents de plaintes | Amélioration produit |
| Messages de forums | Sujets de discussion émergents | Topic Modeling |
| Historique de visionnage | Profils de goûts similaires | Recommandation (Netflix, Spotify) |

> *Pour un entrepreneur* : l'Unsupervised Learning révèle ce que vos clients ne vous disent pas explicitement — leurs comportements naturels et leurs regroupements.

![bg right:45% contain](assets/infographics/unsupervised-learning-patterns_run_20260217_010844_c89082.png)

<small>Sources : [1] [McKinsey State of AI 2024](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-2024)</small>

---

# 13 — Reinforcement Learning — exemples business

L'agent apprend par *essai-erreur* dans un environnement simulé, guidé par un *signal de récompense*.

| Environnement simulé | Action de l'agent | Application métier |
|---|---|---|
| Simulateur de conduite | Accélérer, freiner, tourner | Conduite autonome |
| Simulateur physique | Saisir, marcher, assembler | Robotique industrielle |
| Flux d'utilisateurs | Recommander un article | Recommandation de contenu |
| Marché boursier | Acheter, vendre, attendre | Trading algorithmique |

> *Jalon historique* : en 2016, AlphaGo (DeepMind) a battu le champion du monde de Go — un jeu avec plus de positions possibles que d'atomes dans l'univers [1].

![bg right:45% contain](assets/infographics/reinforcement-learning-cycle_run_20260217_010848_d4776e.png)

<small>Sources : [1] [DeepMind](https://deepmind.google/research/breakthroughs/alphago/)</small>

---

# 14 — Les jalons de l'IA : du Deep Learning aux Transformers

| Année | Jalon | Impact |
|---|---|---|
| 1986 | Hinton : Backpropagation [1] | Rend l'entraînement de réseaux profonds possible |
| 1998 | LeCun : LeNet / MNIST [2] | Première reconnaissance d'écriture industrielle |
| 2012 | AlexNet + ImageNet [3] | Erreur divisée par 2 — lance l'ère du Deep Learning |
| 2016 | Google Neural Machine Translation [4] | Traduction quasi-humaine |
| 2017 | "Attention Is All You Need" [5] | Naissance des Transformers |

> Chaque percée repose sur la précédente : sans la Backpropagation de 1986, pas d'AlexNet en 2012 ; sans AlexNet, pas de Transformers en 2017.

<small>Sources : [1] [Nature](https://www.nature.com/articles/323533a0) · [2] [IEEE](https://ieeexplore.ieee.org/document/726791) · [3] [NeurIPS](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) · [4] [arXiv](https://arxiv.org/abs/1609.08144) · [5] [arXiv](https://arxiv.org/abs/1706.03762)</small>

---

# 15 — De BERT à Claude Code : l'accélération

| Année | Jalon | Impact |
|---|---|---|
| 2018 | BERT (Google) [1] | Le Pre-Training bidirectionnel révolutionne le NLP |
| 2019 | BERT déployé sur Google Search [2] | L'IA touche des milliards de requêtes quotidiennes |
| 2022 | ChatGPT (OpenAI) [3] | 100 millions d'utilisateurs en 2 mois |
| 2025 | DeepSeek-R1 [4] | Raisonnement open source rivalisant avec les modèles fermés |
| 2025 | Claude Code (Anthropic) [5] | Agent de code autonome |

> En 7 ans, l'IA est passée d'une avancée académique (BERT) à des outils grand public (ChatGPT) puis à des agents autonomes (Claude Code). Le rythme *s'accélère*.

<small>Sources : [1] [Google AI Blog](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) · [2] [Google Blog](https://blog.google/products/search/search-language-understanding-bert/) · [3] [Reuters](https://www.reuters.com/technology/chatgpt-sets-record-fastest-growing-user-base-analyst-note-2023-02-01/) · [4] [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) · [5] [Anthropic](https://docs.anthropic.com/en/docs/claude-code/overview)</small>

---

# 16 — La preuve par les données

![bg right:45% contain vertical](assets/A/epoch-ai-dataset_size.png)
![bg contain](assets/A/METR-task-len-horizon.png)

- La taille des datasets d'entraînement croît de manière exponentielle [1]
- Les tâches que l'IA peut accomplir de manière autonome s'allongent rapidement [2]

> Ces deux courbes expliquent pourquoi chaque trimestre apporte des capacités IA que personne n'anticipait un an plus tôt.

<small>Sources : [1] [EpochAI](https://epoch.ai/data-insights/dataset-size-trend) · [2] [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)</small>

---

# 17 — Comment fonctionnent les LLMs

Les LLMs utilisent le Supervised Learning pour *prédire le mot suivant*, mot par mot :

| Input (A) | Output (B) |
|---|---|
| My favorite food is a | *bagel* |
| My favorite food is a bagel | *with* |
| My favorite food is a bagel with | *cream* |
| My favorite food is a bagel with cream | *cheese* |

> Un LLM entraîné sur des centaines de milliards de mots apprend les patterns du langage et devient capable de générer du texte cohérent et pertinent.

![bg right:45% contain](assets/A/lllm-gen-example.png)

---

# 18 — Les LLMs comme partenaire de réflexion

Un LLM n'est pas un moteur de recherche amélioré — c'est un *partenaire de réflexion* :

| Tâche | Web Search | LLM |
|---|---|---|
| Résumer un article de 20 pages | Impossible | Synthèse en 5 bullet points |
| Analyser un business plan | Cherche des templates | Identifie forces et faiblesses |
| Traduire un contrat juridique | Traduction littérale | Adaptation du registre et du contexte |

*Exemples en production* : Klarna a traité *2,3 millions de conversations* via son assistant IA dès le premier mois [1]. Notion AI résume et organise les documents de travail [2].

*Question pour la classe* : Pour quelle tâche hebdomadaire utilisez-vous déjà un LLM ?

<small>Sources : [1] [Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · [2] [Notion](https://www.notion.so/product/ai)</small>

---

<!-- _class: section -->

# Applications GenAI : Writing, Reading, Chatting

## The Three Families of LLM Tasks

---

# 19 — Les trois familles de tâches LLM

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

# 20 — Coder avec l'IA : le paysage des outils

*76% des développeurs* utilisent ou prévoient d'utiliser des outils de code IA [1].

| Outil | Type | Pour qui ? |
|---|---|---|
| Bolt.new [2] / Lovable [3] | No-Code AI | Non-techniques, prototypage rapide |
| n8n [4] / Make | Low-Code | Automatisation de workflows |
| GitHub Copilot [5] | Assisted Code | Développeurs, autocomplétion |
| Cursor | Assisted Code | Développeurs, édition contextuelle |
| Claude Code [6] | Autonomous Code | Développeurs, agent autonome |

> *Pour les entrepreneurs* : vous n'avez plus besoin de savoir coder pour construire un MVP. Les outils No-Code IA produisent des applications complètes à partir d'un prompt.

<small>Sources : [1] [Stack Overflow 2024](https://survey.stackoverflow.co/2024/ai) · [2] [Bolt.new](https://bolt.new/) · [3] [Lovable](https://lovable.dev/) · [4] [n8n](https://n8n.io/) · [5] [GitHub Copilot](https://github.com/features/copilot) · [6] [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)</small>

---

# 21 — Writing : brainstorming et rédaction assistée

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

# 22 — Reading : résumer et classifier

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

# 23 — Chatting : du bot interne au service client

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

# 24 — La génération d'images par IA

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

# 25 — Comment ça marche : les Diffusion Models

Le principe est élégant — on entraîne un modèle à *enlever du bruit* d'une image :

![bg right:40% contain](assets/A/diffusion_model.gif)

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

# 26 — Du No-Code au Full-Code : le spectre IA

| Niveau | Outils | Compétences requises | Délai MVP |
|---|---|---|---|
| *No-Code* | Bolt.new, Lovable, v0 | Vision produit, bon prompt | Heures |
| *Low-Code* | n8n, Make, Zapier | Logique métier, APIs | Jours |
| *Assisted Code* | Copilot, Cursor, Windsurf | Bases de programmation | Jours à semaines |
| *Autonomous Code* | Claude Code, Devin | Architecture, code review | Minutes par feature |

> En 2026, la question n'est plus *"savez-vous coder ?"* mais *"à quel niveau du spectre voulez-vous intervenir ?"*

*Question pour la classe* : Pour votre projet de chatbot, à quel niveau du spectre allez-vous vous positionner ?

![bg right:45% contain](assets/infographics/ai-coding-spectrum_run_20260217_010852_676799.png)

---

<!-- _class: section -->

# Ce que l'IA sait et ne sait pas faire

## Capabilities and Limitations

---

# 27 — Le test du "fresh college grad"

Comment évaluer si un LLM peut réaliser une tâche ? Utilisez cette heuristique :

> *Un jeune diplômé compétent pourrait-il suivre les instructions du prompt pour accomplir la tâche ?*

- Classifier un email comme réclamation ? *Oui* → le LLM peut le faire
- Rédiger un communiqué de presse *sans aucune info* ? *Difficilement* → résultat générique
- Rédiger un communiqué *avec le contexte* ? *Oui* → bon travail

*Limites de l'analogie* — imaginez un diplômé *sans aucune ressource externe* :
- Pas d'accès Internet, pas de formation spécifique, pas de mémoire des tâches précédentes

> C'est l'heuristique la plus utile du cours. Gardez-la en tête pour évaluer chaque cas d'usage.

---

# 28 — Hallucinations et Knowledge Cutoffs

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

# 29 — Récapitulatif — ce que l'IA sait et ne sait pas faire

| L'IA *sait* faire | L'IA *ne sait pas* (encore) faire |
|---|---|
| Résumer des documents | Raisonner de manière fiable sur des sujets complexes |
| Classifier du texte (sentiment, catégorie) | Accéder à des données en temps réel (sans outils) |
| Traduire et adapter le ton | Garantir la véracité de ses réponses |
| Brainstormer et générer du contenu | Comprendre le contexte spécifique de votre entreprise |
| Générer des images à partir de texte | Travailler sur des données structurées/tabulaires sans outils |
| Corriger et réécrire | Remplacer le jugement humain sur des décisions critiques |

> Testez avec l'heuristique du *fresh college grad* : si un jeune diplômé pourrait le faire avec les instructions du prompt, le LLM peut probablement le faire aussi.

---

# 30 — Points clés à retenir

*Comprendre* :
- La Generative AI produit du contenu (texte, image, audio, vidéo) à partir de prompts
- Les LLMs fonctionnent par *prédiction du mot suivant* à très grande échelle
- L'IA a *40 ans d'histoire* — chaque percée repose sur la précédente

*Appliquer* :
- Trois familles de tâches : *Writing*, *Reading*, *Chatting*
- Les outils de code IA rendent le *prototypage accessible* à tous
- Déployez progressivement : interne → human-in-the-loop → client final

*Rester vigilant* :
- Les *Hallucinations* sont un risque réel — toujours vérifier
- Les *biais* existent — tester avant de déployer

> *Suite* : Session 1B — L'IA au-delà des LLMs
