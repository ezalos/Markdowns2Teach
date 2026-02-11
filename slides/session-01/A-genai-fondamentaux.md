---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — Session 1 · M2 Entrepreneuriat Sorbonne"
footer: "Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"
---

<!-- ABOUTME: Introduction à la Generative AI — concepts, capacités (Writing/Reading/Chatting) et génération d'images. -->
<!-- ABOUTME: Première moitié de la Session 1, business-framed pour étudiants M2 Entrepreneuriat. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 1A — L'IA Générative : ce qu'elle sait faire

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Qu'est-ce que la Generative AI ?

## What is Generative AI

---

# 01 — L'essor de la Generative AI

- *$2,6 – 4,4 trillions* de valeur annuelle potentielle *(McKinsey)*
- *+7% du PIB mondial* sur 10 ans *(Goldman Sachs)*
- *80% des travailleurs* verront au moins 10% de leurs tâches impactées *(OpenAI / UPenn)*

> Après le lancement de ChatGPT (nov. 2022), les mentions d'"IA" dans les *earnings calls* du S&P 500 ont explosé.

![bg right:45%](assets/ng01/img-002.png)

*Question pour la classe* : Si le coût de l'intelligence machine tend vers zéro, quel service aujourd'hui trop coûteux pour être automatisé devient une opportunité de startup demain ?

---

# 02 — Qu'est-ce que la Generative AI ?

Des systèmes d'intelligence artificielle capables de *produire du contenu de haute qualité* : texte, images, audio, vidéo.

*Fonctionnement de base* :
- L'utilisateur écrit un *prompt* (une instruction en langage naturel)
- Le modèle génère une *réponse* (texte, image, code...)

*Acteurs majeurs en 2026* :
- *ChatGPT* (OpenAI) — rédaction, analyse, code
- *Claude* (Anthropic) — raisonnement, analyse documentaire
- *Gemini* (Google) — recherche augmentée
- *Le Chat* (Mistral AI) — alternative européenne

![bg right:45%](assets/ng01/img-006.png)

---

# 03 — La Generative AI, aussi un outil de développement

Au-delà des chatbots grand public, la Generative AI est un *developer tool* puissant :

- Génération de code et debugging
- Automatisation de pipelines de données
- Prototypage rapide d'applications

*Pour les entrepreneurs* : même sans équipe technique, les LLMs permettent de construire des *MVPs fonctionnels* en quelques jours.

> En 2025, des startups comme Bolt.new et Lovable permettent de coder des apps entières via prompt.

![bg right:45%](assets/ng01/img-008.png)

---

# 04 — L'IA est déjà partout

| Technologie IA | Exemples | Vous l'utilisez déjà ? |
|---|---|---|
| Web Search | Google, Bing | Tous les jours |
| Fraud Detection | Paiements CB | À chaque achat |
| Recommender Systems | Amazon, Netflix, Spotify | Constamment |
| Machine Translation | DeepL, Google Translate | Régulièrement |
| Speech Recognition | Siri, Alexa, Whisper | Souvent |

> *Point clé pour entrepreneurs* : L'IA "classique" (prédictive) crée de la valeur depuis 15 ans. La *Generative AI* ouvre un nouvel espace — la création de contenu et le raisonnement.

---

# 05 — Au-delà du texte : images, audio, vidéo

La Generative AI ne se limite pas au texte :

- *Images* : Midjourney, DALL-E, Stable Diffusion, Flux
- *Audio* : génération de voix (ElevenLabs), musique (Suno)
- *Vidéo* : Sora (OpenAI), Runway, Kling

*Cas d'usage business* :
- Créer des visuels marketing sans graphiste
- Produire des voix-off pour des formations
- Générer des vidéos de démonstration produit

![bg right:45%](assets/ng01/img-009.png)
![bg](assets/ng01/img-010.png)

---

# 06 — Ce que vous allez apprendre

Trois piliers pour maîtriser la Generative AI en tant qu'entrepreneur :

| Pilier | Ce que vous saurez faire |
|---|---|
| *Comprendre la technologie* | Ce que l'IA peut et ne peut pas faire, les cas d'usage |
| *Construire des projets GenAI* | Identifier, cadrer et construire des solutions IA |
| *Impact business et société* | Comment les équipes peuvent en tirer parti, risques et IA responsable |

> Objectif du cours : vous donner les clés de décision, pas vous transformer en Data Scientists.

---

<!-- _class: cols -->

# 07 — Les grandes familles de l'IA

<div class="left">

### Supervised Learning
- *Input A → Output B* — ex : email → spam ? image → diagnostic ?

### Unsupervised Learning
- Patterns sans labels (ex : segmentation clients)

</div>
<div class="right">

### Generative AI
- Génère du *contenu original* (texte, images, audio, vidéo, code)

### Reinforcement Learning
- Apprend par essai/erreur (ex : jeux, robotique, trading)

</div>

---

# 08 — Supervised Learning — exemples business

| Input (A) | Output (B) | Application métier |
|---|---|---|
| Email | Spam ? (0/1) | Filtrage automatique |
| Pub + profil utilisateur | Clic ? (0/1) | Publicité ciblée |
| Image radar | Position véhicules | Conduite autonome |
| Image radio | Diagnostic | Healthcare |
| Photo produit | Défaut ? (0/1) | Contrôle qualité |
| Enregistrement audio | Transcription texte | Speech Recognition |
| Avis client | Sentiment (pos/neg) | Veille e-réputation |

> *Pour un entrepreneur* : le Supervised Learning reste la technologie IA la plus *déployée* et la plus *rentable*. La Generative AI est plus récente mais croît le plus vite.

---

# 09 — Pourquoi l'IA explose maintenant

*2010–2020 : l'ère du Large Scale Supervised Learning*

- La performance des modèles IA augmente avec *plus de données* et des *modèles plus grands*
- Les petits modèles plafonnent vite — les grands modèles continuent de progresser
- Cela a motivé la course au *scale* : plus de compute, plus de data

*2020+ : l'ère des Large Language Models*

- Application du même principe au texte : entraîner des modèles *massifs* sur des *centaines de milliards de mots*
- Résultat : des modèles capables de générer du texte de qualité humaine

---

# 10 — Comment fonctionnent les LLMs

Les LLMs utilisent le Supervised Learning pour *prédire le mot suivant*, mot par mot :

| Input (A) | Output (B) |
|---|---|
| My favorite food is a | *bagel* |
| My favorite food is a bagel | *with* |
| My favorite food is a bagel with | *cream* |
| My favorite food is a bagel with cream | *cheese* |

> Un LLM entraîné sur des centaines de milliards de mots apprend les patterns du langage et devient capable de générer du texte cohérent et pertinent.

---

# 11 — Les LLMs comme partenaire de réflexion

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

# 12 — Les trois familles de tâches LLM

| Catégorie | Exemples | Type d'app |
|---|---|---|
| *Writing* | Brainstorming noms de produits, communiqués de presse, traduction | Web + App |
| *Reading* | Classification d'emails, résumé de conversations, analyse de sentiment | Surtout App |
| *Chatting* | Service client bot, coaching, FAQ interne | Web + App |

*Deux modes d'utilisation* :
- *Web-based* : ChatGPT, Claude, Le Chat — interaction directe
- *Software application* : le LLM est intégré dans un produit (email routing, analyse automatisée)

![bg right:45%](assets/ng01/img-026.png)

---

# 13 — Writing : brainstorming et rédaction assistée

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

# 14 — Reading : résumer et classifier

Un des cas d'usage les plus puissants pour les entreprises :

*Résumé* :
- Synthèse de rapports de 50+ pages en bullet points
- Traitement de 100 feedbacks clients en 5 minutes au lieu de 2 heures

*Classification automatique* :
- Routage d'emails vers le bon département
- Analyse de sentiment (avis positifs/négatifs)
- Veille e-réputation automatisée

> *Clé du succès* : un bon prompt de classification a 3 éléments — la *tâche*, les *choix possibles*, et les *données* à analyser.

![bg right:45%](assets/ng01/img-024.png)

---

# 15 — Chatting : du bot interne au service client

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

# 16 — La génération d'images par IA

Les modèles de génération d'images créent des visuels à partir de *descriptions textuelles* :

*Outils majeurs en 2026* :
- *Midjourney* — qualité artistique, très populaire
- *DALL-E 3* (OpenAI) — intégré à ChatGPT
- *Flux* (Black Forest Labs) — open source, haute qualité
- *Stable Diffusion* — open source, très personnalisable

*Pour les entrepreneurs* :
- Prototypage visuel rapide et quasi gratuit
- A/B testing de visuels marketing
- Attention aux *droits d'auteur* — sujet juridique en évolution

![bg right:33%](assets/ng01/img-028.png)
![bg](assets/ng01/img-030.png)
![bg](assets/ng01/img-029.png)

---

# 17 — Comment ça marche : les Diffusion Models

Le principe est élégant — on entraîne un modèle à *enlever du bruit* d'une image :

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

# 18 — Le test du "fresh college grad"

Comment évaluer si un LLM peut réaliser une tâche ? Utilisez cette heuristique :

> *Un jeune diplômé compétent pourrait-il suivre les instructions du prompt pour accomplir la tâche ?*

- Classifier un email comme réclamation ? *Oui* → le LLM peut le faire
- Rédiger un communiqué de presse *sans aucune info* ? *Difficilement* → résultat générique
- Rédiger un communiqué *avec le contexte* ? *Oui* → bon travail

*Limites de l'analogie* — imaginez un diplômé *sans aucune ressource externe* :
- Pas d'accès Internet, pas de formation spécifique, pas de mémoire des tâches précédentes

> C'est l'heuristique la plus utile du cours. Gardez-la en tête pour évaluer chaque cas d'usage.

---

# 19 — Hallucinations et Knowledge Cutoffs

*Hallucinations* — le LLM *invente des informations avec un ton très confiant* :
- Un avocat américain a soumis un mémoire juridique contenant des *affaires inventées* par ChatGPT (*NYT*, 2023)
- Règle d'or : ne jamais publier un contenu IA sans *vérification humaine*

*Knowledge Cutoffs* — l'IA vit dans le passé :
- Les connaissances sont *figées à la date d'entraînement*
- Les données de la semaine dernière restent inaccessibles (sauf accès web)

![bg right:45%](assets/ng01/img-022.png)

*Question pour la classe* : Quelles informations de votre entreprise ne devriez-vous JAMAIS mettre dans un prompt ChatGPT ?

---

# 20 — Récapitulatif — ce que l'IA sait et ne sait pas faire

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

# 21 — Points clés à retenir

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
