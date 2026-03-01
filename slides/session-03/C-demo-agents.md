---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: Bloc C de la Session 3 — démo live d'un agent IA dans n8n (AI Agent + tools + ReAct), teaser MCP, et point d'avancement projet. -->
<!-- ABOUTME: Atelier pratique qui concrétise les concepts agents vus en S3-A. Prépare les présentations finales (S5-B). -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 3C — Agents en action

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Rappel agents

## De la théorie à la pratique

---

<!-- _class: cols -->

# 01 — Rappel : la boucle ReAct

<div class="left">

En S3-A, on a vu le pattern **ReAct** :

1. **Thought** — le LLM raisonne
2. **Action** — il appelle un outil
3. **Observation** — il lit le résultat
4. **Thought** — il décide : continuer ou répondre ?

</div>
<div class="right">

**La différence avec un chatbot** :
- Le chatbot répond en 1 tour
- L'agent **boucle** jusqu'à avoir la réponse
- Il choisit quels outils utiliser et dans quel ordre

</div>

> Aujourd'hui, on va voir cette boucle **en action** dans n8n.

---

# 02 — Ce qu'on va construire

Un **agent IA** dans n8n qui :

- Reçoit une question en langage naturel (Chat Trigger)
- Raisonne sur la question et choisit quel outil utiliser
- Exécute l'outil (calculatrice, recherche web, API)
- Analyse le résultat et décide s'il a assez d'information
- Formule une réponse synthétique

**Exemple de question multi-étapes** :
> "Quel est le prix au m² moyen à Paris vs Lyon ? Calcule la différence en %."

L'agent devra : chercher les prix → calculer la différence → formuler la réponse.

---

<!-- _class: section -->

# Demo live

## Un agent qui raisonne et agit

---

# 03 — Architecture de l'agent dans n8n

| Nœud | Rôle |
|---|---|
| **Chat Trigger** | Reçoit la question de l'utilisateur |
| **AI Agent** | Le cerveau — raisonne et décide quels outils utiliser |
| **Calculator Tool** | Outil de calcul (addition, %, etc.) |
| **HTTP Request Tool** | Outil de recherche web ou API externe |

Le nœud **AI Agent** est le cœur : il reçoit la question, consulte ses outils disponibles, et boucle en ReAct jusqu'à avoir la réponse.

> Dans n8n, l'AI Agent est un nœud natif qui gère la boucle ReAct pour vous.

---

<!-- _class: cols -->

# 04 — Configurer l'AI Agent

<div class="left">

**Modèle** : OpenRouter (free)
- `mistralai/mistral-small-3.1-24b-instruct:free`
- Credential : votre clé OpenRouter

**System Prompt** :
- "Tu es un assistant qui utilise tes outils pour répondre"

</div>
<div class="right">

**Paramètres clés** :
- **Memory Window** : 5 messages (contexte conversationnel)
- **Max Iterations** : 5 (circuit breaker)
- **Temperature** : 0 (déterministe)

</div>

> Le `Max Iterations` est votre **circuit breaker** — il empêche l'agent de boucler à l'infini.

---

# 05 — Ajouter des Tools à l'agent

**Tool 1 — Calculator** :
- Nœud natif n8n, pas de configuration nécessaire
- L'agent l'utilise quand il détecte un calcul à faire

**Tool 2 — HTTP Request** :
- Connecté à une API de votre choix (ou web search)
- L'agent l'utilise pour chercher des informations externes
- Nécessite une description claire : "Utilise cet outil pour chercher des informations sur le web"

> La **description** de chaque tool est critique — c'est ce que le LLM lit pour décider quand utiliser l'outil.

---

# 06 — La boucle en action : lire les logs

Quand l'agent s'exécute, n8n affiche **chaque étape** de la boucle ReAct :

**Itération 1** :
- *Thought* : "Je dois chercher le prix au m² à Paris"
- *Action* : HTTP Request → recherche web
- *Observation* : "Le prix moyen à Paris est de 10 500€/m²"

**Itération 2** :
- *Thought* : "Maintenant je dois chercher Lyon"
- *Action* : HTTP Request → recherche web
- *Observation* : "Le prix moyen à Lyon est de 5 200€/m²"

**Itération 3** :
- *Thought* : "Je dois calculer la différence en %"
- *Action* : Calculator → (10500-5200)/5200 × 100

---

# 07 — Debug : quand l'agent déraille

| Problème | Symptôme | Solution |
|---|---|---|
| **Mauvais outil** | L'agent utilise Calculator au lieu de HTTP | Améliorer la description des tools |
| **Boucle infinie** | L'agent répète la même action | Réduire `Max Iterations` à 3-5 |
| **Réponse incomplète** | L'agent répond avant d'avoir toute l'info | Ajuster le system prompt : "Vérifie que tu as toutes les données" |
| **Hallucination** | L'agent invente un résultat | Ajouter : "N'invente jamais de données" dans le prompt |

> La plupart des bugs d'agent se résolvent en améliorant le **prompt** ou les **descriptions des tools**.

---

<!-- _class: section -->

# MCP : le teaser

## Quand l'agent accède au monde réel

---

# 08 — MCP en action : Claude + outils

En S3-A, on a vu que MCP connecte tout agent à tout outil via un standard ouvert.

**Démo rapide** — Claude Desktop + MCP server (filesystem) :
- L'agent peut lire et écrire des fichiers sur votre machine
- Pas de configuration custom — juste un serveur MCP standard
- Claude raisonne, décide quel fichier lire, et synthétise

**Autres exemples MCP** :
- **Slack MCP** — l'agent lit vos channels et répond
- **GitHub MCP** — l'agent crée des issues et des PRs
- **Database MCP** — l'agent requête votre base de données

> MCP transforme chaque SaaS en un outil accessible par n'importe quel agent.

---

<!-- _class: section -->

# Point projet

## Préparer la présentation finale

---

<!-- _class: cols -->

# 09 — État des lieux par équipe

<div class="left">

**Chaque équipe (1 min)** :
- Quel projet de classification ?
- Quel(s) modèle(s) testé(s) ?
- Accuracy obtenue (si évaluée) ?
- Principal blocage ?

</div>
<div class="right">

**Où vous devriez être** :
- 2 workflows Prod (HF + OpenRouter)
- Au moins 1 workflow Eval lancé
- Dataset de test ≥20 exemples
- Idée claire de votre choix final

</div>

---

# 10 — Préparer la présentation finale (Session 5)

**Format** : 5 minutes par équipe + 2 min de questions

**Structure recommandée** :

| Partie | Durée | Contenu |
|---|---|---|
| **Problème** | 30s | Quelle tâche de classification ? Pourquoi c'est utile ? |
| **Dataset** | 30s | Combien d'exemples ? Quelles catégories ? Cas difficiles ? |
| **Modèles testés** | 1 min | HuggingFace vs OpenRouter, scores comparés |
| **Choix final** | 1 min | Quel modèle retenu et pourquoi (accuracy, coût, latence) |
| **Démo live** | 2 min | Montrer le workflow Prod en action (Telegram ou Chat) |

> La qualité de l'**analyse comparative** compte plus que le score brut.

---

# 11 — Checklist de rendu

**Obligatoire** :
- Workflow `G0X — Prod — ...` actif et fonctionnel
- Workflow `G0X — Eval — ...` avec ≥20 test cases
- Au moins **2 modèles** comparés (scores documentés)

**Bonus** :
- Dataset ≥50 exemples
- Cas difficiles identifiés (sarcasme, ambiguïté, multilingue)
- Prompt optimisé avec exemples (few-shot)
- Intégration Telegram fonctionnelle

> Vous avez encore 2 séances (S4-C, S5-B) pour finaliser. Commencez la comparaison dès maintenant.
