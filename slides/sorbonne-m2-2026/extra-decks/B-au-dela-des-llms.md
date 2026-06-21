---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0"
---

<!-- ABOUTME: L'IA en pratique — prompting, mécanique des LLMs, applications (Writing/Reading/Chatting), génération d'images, et reasoning models. -->
<!-- ABOUTME: Deck de référence déplacé en Session 2, business-framed pour étudiants M2 IMT&E Paris 1 Panthéon-Sorbonne. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 2B — L'IA au-delà des LLMs

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

> Ce principe est la base du *Chain-of-Thought Prompting*, technique clé des Reasoning Models (fin de ce deck).

---

<!-- _class: compact -->

# 04 — Principe 3 : expérimentez et itérez

Pas de prompt parfait universel — mais un *processus* pour s'améliorer :

1. *Écrivez* un premier prompt (ne réfléchissez pas trop)
2. *Évaluez* la sortie — qu'est-ce qui manque ?
3. *Affinez* (ajoutez du contexte, changez le format)
4. *Répétez* jusqu'à satisfaction

Le cycle du Prompt Engineering = le *cycle produit* des startups :
*Idée → Prompt → Réponse → Évaluation → Nouveau prompt → ...*

![bg right:35% contain](assets/infographics/prompt-iteration_run_20260217_012320_e9035e.png)

<!-- Speaker notes: Ne sur-réfléchissez pas le premier prompt — lancez-vous vite et itérez. -->

---

<!-- _class: section -->

# Comment fonctionnent les LLMs

## LLM Mechanics

---

# 05 — La preuve par les données

![bg right:45% contain vertical](assets/A/epoch-ai-dataset_size.png)
![bg contain](assets/A/METR-task-len-horizon.png)

- La taille des datasets d'entraînement croît de manière exponentielle [1]
- Les tâches que l'IA peut accomplir de manière autonome s'allongent rapidement [2]

> Ces deux courbes expliquent pourquoi chaque trimestre apporte des capacités IA que personne n'anticipait un an plus tôt.

<small>Sources : [1] [EpochAI](https://epoch.ai/data-insights/dataset-size-trend) · [2] [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)</small>

---

# 06 — Comment fonctionnent les LLMs

Les LLMs utilisent le Supervised Learning pour *prédire le mot suivant* :

| Input (A) | Output (B) |
|---|---|
| My favorite food is a | *bagel* |
| My favorite food is a bagel | *with* |
| My favorite food is a bagel with | *cream* |
| My favorite food is a bagel with cream | *cheese* |

![bg right:40% contain](assets/A/lllm-gen-example.png)

<!-- Speaker notes: Entraîné sur des centaines de milliards de mots, un LLM apprend les patterns du langage et génère du texte cohérent. -->

---

# 07 — Les LLMs comme partenaire de réflexion

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

<!-- _class: compact -->

# 08 — Les trois familles de tâches LLM

| Catégorie | Exemples | Type |
|---|---|---|
| *Writing* | Brainstorming, communiqués, traduction | Web + App |
| *Reading* | Classification, résumé, sentiment | Surtout App |
| *Chatting* | Service client, coaching, FAQ | Web + App |

*Deux modes d'utilisation* :
- *Web-based* : ChatGPT, Claude, Le Chat
- *Software application* : LLM intégré dans un produit (email routing, analyse)

![bg right:35% contain](assets/ng01/img-026.png)

---

# 09 — Coder avec l'IA : le paysage des outils

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

# 10 — Writing : brainstorming et rédaction assistée

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

<!-- _class: compact -->

# 11 — Reading : résumer et classifier

*Résumé* :
- Synthèse de rapports 50+ pages en bullet points
- 100 feedbacks clients en 5 min au lieu de 2h

*Classification automatique* :
- Routage d'emails vers le bon département
- Analyse de sentiment (positif/négatif)
- Veille e-réputation automatisée

> *Clé* : un bon prompt de classification = *tâche* + *choix possibles* + *données*.

![bg right:35% contain](assets/ng01/img-024.png)

---

# 12 — Chatting : du bot interne au service client

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

<!-- _class: compact -->

# 13 — La génération d'images par IA

Les modèles créent des visuels à partir de *descriptions textuelles*.

*Outils majeurs en 2026* :
- *Midjourney* [1] — qualité artistique, très populaire
- *DALL-E 3* (OpenAI) [2] — intégré à ChatGPT
- *Flux* (Black Forest Labs) [3] — open source, haute qualité
- *Stable Diffusion* [4] — open source, personnalisable

![bg right:40% contain](assets/ng01/img-028.png)
![bg contain](assets/ng01/img-030.png)

<small>Sources : [1] [Midjourney](https://www.midjourney.com/) · [2] [OpenAI DALL-E](https://openai.com/dall-e-3) · [3] [Black Forest Labs](https://blackforestlabs.ai/) · [4] [Stability AI](https://stability.ai/)</small>

---

# 13b — La génération d'images (suite)

*Pour les entrepreneurs* :
- Prototypage visuel rapide et quasi gratuit
- A/B testing de visuels marketing
- Attention aux *droits d'auteur* — sujet juridique en évolution

![bg right:40% contain](assets/ng01/img-029.png)

---

<!-- _class: compact -->

# 14 — Comment ça marche : les Diffusion Models

On entraîne un modèle à *enlever du bruit* d'une image :

![bg right:35% contain](assets/A/diffusion_model.gif)

*Entraînement* :
1. Prendre une image nette (ex : une pomme)
2. Ajouter du bruit progressivement
3. Entraîner : image bruitée → image moins bruitée

*Génération* :
1. Partir de *bruit pur* (image aléatoire)
2. Appliquer le modèle ~100 fois
3. L'image émerge progressivement

<!-- Speaker notes: C'est comme un sculpteur qui retire la pierre pour révéler la statue — sauf que le sculpteur est un réseau de neurones. -->

---

<!-- _class: compact -->

# 15 — Du No-Code au Full-Code : le spectre IA

| Niveau | Outils | Compétences | Délai MVP |
|---|---|---|---|
| *No-Code* | Bolt.new, Lovable, v0 | Vision produit, prompt | Heures |
| *Low-Code* | n8n, Make, Zapier | Logique métier, APIs | Jours |
| *Assisted Code* | Copilot, Cursor | Bases de programmation | Semaines |
| *Autonomous Code* | Claude Code, Devin | Architecture, review | Minutes/feature |

![bg right:35% contain](assets/infographics/ai-coding-spectrum_run_20260217_010852_676799.png)

---

# 15b — Le spectre IA (suite)

> En 2026, la question n'est plus *"savez-vous coder ?"* mais *"à quel niveau du spectre voulez-vous intervenir ?"*

*Question pour la classe* : Pour votre projet de chatbot, à quel niveau du spectre allez-vous vous positionner ?

---

<!-- _class: section -->

# Ce que l'IA sait et ne sait pas faire

## Capabilities and Limitations

---

# 16 — Le test du "fresh college grad"

Comment évaluer si un LLM peut réaliser une tâche ? Utilisez cette heuristique :

> *Un jeune diplômé compétent pourrait-il suivre les instructions du prompt pour accomplir la tâche ?*

- Classifier un email comme réclamation ? *Oui* → le LLM peut le faire
- Rédiger un communiqué de presse *sans aucune info* ? *Difficilement* → résultat générique
- Rédiger un communiqué *avec le contexte* ? *Oui* → bon travail

*Limites de l'analogie* — imaginez un diplômé *sans aucune ressource externe* :
- Pas d'accès Internet, pas de formation spécifique, pas de mémoire des tâches précédentes

> C'est l'heuristique la plus utile du cours. Gardez-la en tête pour évaluer chaque cas d'usage.

---

<!-- _class: compact -->

# 17 — Hallucinations et Knowledge Cutoffs

*Hallucinations* — le LLM *invente des informations avec un ton confiant* :
- Un avocat a soumis un mémoire contenant des *affaires inventées* par ChatGPT [1]
- Règle d'or : jamais de contenu IA sans *vérification humaine*

*Knowledge Cutoffs* — l'IA vit dans le passé :
- Connaissances *figées à la date d'entraînement*
- Données récentes inaccessibles (sauf accès web)

![bg right:35% contain](assets/ng01/img-022.png)

<small>Sources : [1] [NYT](https://www.nytimes.com/2023/05/27/nyregion/avianca-chatgpt-fake-citations.html)</small>

---

# 17b — Hallucinations (suite)

*Question pour la classe* : Quelles informations de votre entreprise ne devriez-vous JAMAIS mettre dans un prompt ChatGPT ?

---

# 18 — Récapitulatif — ce que l'IA sait et ne sait pas faire

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

<!-- _class: section -->

# Reasoning Models : quand l'IA apprend à réfléchir

## From Next-Token Prediction to Multi-Step Reasoning

---

<!-- _class: compact -->

# 19 — Trois disruptions simultanées

Trois disruptions transforment le paysage IA en 2025 :

1. *Reasoning Models* — décomposent un problème en étapes, *96,7%* aux olympiades de maths [1]
2. *Effondrement des coûts* — coût d'inference divisé par *280* en 2 ans [2]
3. *L'IA dans la poche* — Apple Intelligence : modèle 3B sur iPhone, sans cloud [3]

![bg right:35% contain](assets/B/cheapest_llm_MMLU.png)

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [Apple ML Research](https://machinelearning.apple.com/research/introducing-apple-foundation-models)</small>

---

# 19b — Trois disruptions (suite)

> En tant qu'entrepreneur, comprendre ce paysage = savoir *quel modèle utiliser, quand, et à quel prix*.

---

<!-- _class: compact -->

# 20 — Chain-of-Thought : penser avant de répondre

*Ce que font les Reasoning Models différemment* :
- *Extended Thinking* — chaîne de raisonnement *avant* de répondre
- *Token budget* — plus de "thinking tokens" = meilleure réponse (mais plus cher)
- *Vérification interne* — le modèle vérifie ses étapes, réduisant les hallucinations

| Modèle | AIME 2024 (maths) | Prix input / 1M tokens |
|--------|-----------|-----------------|
| GPT-4o | ~26% | $2,50 [1] |
| DeepSeek-R1 | 79,8% | $0,55 [2] |
| o1 | 74,3% | $15,00 [1] |
| o3 | 91,6% | $2,00 [1] |
| o4-mini | 93,4% | $1,10 [1] |

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [DeepSeek](https://arxiv.org/abs/2501.12948) · [3] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning)</small>

---

<!-- _class: cols compact -->

# 21 — Small Language Models : l'IA dans la poche

<div class="left">

### 5 avantages startups

1. *10-30x moins cher* [1]
2. *On-device* — pas de cloud
3. *< 2s de latence* [3]
4. *RGPD friendly* — données locales [2]
5. *Fine-tuning $50-500* via LoRA [4]

</div>
<div class="right">

### SLMs à connaître

| Modèle | Params | Force clé |
|--------|--------|-----------|
| Phi-4 | 14B | Math rivale 70B |
| Mistral Small 3 | 24B | 27 langues |
| Gemma 3 | 1-27B | On-device |
| SmolLM2 | 1,7B | Raspberry Pi |

</div>

> Les SLMs *complètent* les Frontier Models pour les tâches simples et sensibles.

<small>Sources : [1] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [MLCommons](https://mlcommons.org/2025/09/small-llm-inference-5-1/) · [4] [Stratagem Systems](https://www.stratagem-systems.com/blog/lora-fine-tuning-cost-analysis-2026)</small>

---

# 22 — Matrice de décision : quel modèle pour quel usage ?

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

# Récapitulatif Session 1

## Key Takeaways

---

<!-- _class: compact -->

# 23 — Points clés à retenir

### L'IA Générative (Session 1A)
- GenAI produit du contenu — mais le ML traditionnel = *~70% de la valeur IA*
- Trois axes : *technique, paradigme, tâche*
- Les Transformers (2017) : brique fondamentale des LLMs

### L'IA en pratique (Session 1B)
- *Prompt Engineering* : détail + Chain-of-Thought + itération
- Trois familles : *Writing, Reading, Chatting* + Coding
- Test du *fresh college grad* pour évaluer chaque use case
- *Hallucinations* et *Knowledge Cutoffs* = risques réels

### Les modèles de demain
- *Reasoning Models* : penser avant de répondre (o3, DeepSeek-R1)
- *Small Language Models* : bon modèle, bonne tâche, bon prix
