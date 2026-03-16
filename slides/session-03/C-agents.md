---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: Agents IA — introduction progressive : Tools, Skills, MCP, patterns Anthropic, mémoire, production, Context Engineering, produits agents, AutoResearch. -->
<!-- ABOUTME: Session 3C pour étudiants M2 IMT&E Paris 1 : comprendre, construire et déployer des agents IA. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Agents IA : du workflow à l'autonomie

## Session 3C — Comprendre, construire et déployer des agents IA

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Qu'est-ce qu'un Agent ?

## Du chatbot à l'autonomie

---

<!-- _class: img-right -->

# 01 — L'analogie : Alfred, l'assistant IA

Vous dites à Alfred : **"Organise un dîner d'affaires pour jeudi."**

Alfred ne vous redemande rien :
1. **Comprend** la demande et identifie les sous-tâches
2. **Raisonne et planifie** l'ordre des actions
3. **Utilise des outils** (email, calendrier, réservation)
4. **Livre le résultat** — confirmation envoyée

> Un Agent = un LLM capable de **raisonner**, **planifier** et **interagir avec son environnement** pour atteindre un objectif [1].

![bg right:55% contain](assets/infographics/agent-alfred-narrative.png)

<small>Sources : [1] [HuggingFace — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/what-are-agents)</small>

---

<!-- _class: img-right -->

# 02 — Le spectre d'agence : 5 niveaux

<!-- TODO: regenerate agency-spectrum-5-levels.png with corrected star ratings (★★★ for both Multi-Step and Multi-Agent) -->

Tous les systèmes IA ne sont pas des agents. L'**agence** se mesure sur un spectre [1] :

- **☆☆☆** Simple processor — la sortie n'affecte rien
- **★☆☆** Router — la sortie détermine le flux
- **★★☆** Tool Caller — la sortie déclenche une fonction
- **★★★** Multi-step Agent — la sortie contrôle l'itération
- **★★★** Multi-Agent — un agent lance d'autres agents

> **La plupart des cas business = niveaux ★☆☆ et ★★☆.** Les agents multi-steps sont la frontière de ce qui fonctionne en production.

![bg right:55% contain](assets/infographics/agency-spectrum-5-levels.png)

<small>Sources : [1] [HuggingFace — smolagents](https://huggingface.co/docs/smolagents/)</small>

---

<!-- _class: img-right -->

# 03 — Le cycle agent : Think → Act → Observe

La boucle fondamentale de tout agent [1][2] :

1. **Think** — le modèle raisonne sur la tâche
2. **Act** — il exécute une action (recherche, API, calcul)
3. **Observe** — il analyse le résultat
4. **"Ai-je atteint mon objectif ?"** → si non, retour au Think

**Exemple** :
- *Think* : "Je dois trouver le CA de Mistral AI"
- *Act* : Recherche web → "Mistral AI revenue"
- *Observe* : "Mistral a atteint $300M ARR"
- *Think* : "J'ai la réponse, je peux synthétiser"

![bg right:55% contain](assets/agent-cycle-hf.gif)

<small>Sources : [1] [HuggingFace — Agents Course](https://huggingface.co/learn/agents-course/en/unit1/agent-steps-and-structure) · [2] [ReAct — Princeton/Google](https://arxiv.org/abs/2210.03629)</small>

---

<!-- _class: img-right -->

# 04 — Le LLM Augmenté : les 3 extensions

Tout système agentique repose sur un LLM **augmenté** de 3 capacités [1] :

- **Retrieval** — injecter du savoir (RAG, vu en Deck B)
- **Tools** — agir sur le monde (APIs, recherche, code)
- **Memory** — retenir l'information entre les interactions

> Avant de construire un agent, il faut un LLM bien augmenté. Les 3 extensions sont les fondations. Retrieval = ce que vous maîtrisez déjà depuis le Deck B.

![bg right:55% contain](assets/infographics/augmented-llm-3-extensions.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

# 05 — Discussion : agent ou pas agent ?

> Vous recevez **200 CV** pour un poste de Data Analyst. Vous voulez présélectionner les 10 meilleurs candidats.

**Questions pour la classe** :

- À quel niveau du spectre d'agence se situe ce cas ? (Router ? Tool Caller ? Multi-step ?)
- Un simple Prompt Chain suffirait-il ? À quel moment passeriez-vous à un agent ?
- Quel serait le **coût de l'erreur** si l'agent élimine un bon candidat ?
- Comment vérifieriez-vous que l'agent fait un bon travail ?

---

<!-- _class: section -->

# Tools & Skills

## Les briques fondamentales de l'agent

---

# 06 — Tool Use : donner des mains au LLM

Le **Function Calling** permet au LLM de déclencher des actions dans le monde réel :

| Limite du LLM seul | Tool qui résout | Exemple |
|---|---|---|
| Ne sait pas calculer | `calculator()` | "Quel est 15% de 847€ ?" |
| Pas d'accès au web | `search_web()` | "Dernières nouvelles Mistral AI" |
| Pas d'accès aux données | `query_database()` | "Commandes du mois dernier" |
| Ne peut pas agir | `send_email()` | "Envoie un résumé au client" |

**Comment ça marche** : le LLM génère un **JSON structuré** décrivant l'action, le système l'exécute et renvoie le résultat.

> Le Tool Use transforme un LLM "qui parle" en un LLM "qui agit". C'est la brique fondamentale des agents.

---

<!-- _class: compact -->

# 07 — Skills : un exemple concret

Un **Tool** connecte l'agent à un service. Une **Skill** lui apprend un **processus complet** [1].

**Exemple de fichier SKILL.md** (standard ouvert, 26+ plateformes) :

```yaml
---
name: translate-document
description: Translate a document while preserving formatting
---
# Steps
1. Read the source file with the Read tool
2. Detect the source language from the first 500 characters
3. Translate section by section, preserving all markdown
4. Write the output file with suffix _<lang>.md
5. Report: source language, target language, word count
```

> Tool = **"comment se connecter"** (une fonction). Skill = **"quoi faire"** (un processus complet, testable, partageable) [1].

<small>Sources : [1] [Anthropic — Skills](https://www.anthropic.com/)</small>

---

<!-- _class: cols -->

# 08 — Skills vs Tools : la bonne abstraction

<div class="left">

- **Tool** : `search_web(query)` → une seule action atomique
- **Skill** : "Veille concurrentielle" = recherche + filtrage + comparaison + alerte
- Les Skills sont testables, versionnables, partageables entre agents

</div>
<div class="right">

- Les Skills invoquent des sub-agents qui chargent d'autres Skills (composition)
- **26+ plateformes** adoptent le standard SKILL.md
- Vos Skills propriétaires = votre **avantage compétitif** en IA

</div>

> La Skill est à l'agent ce que le **savoir-faire** est à l'artisan : ce qui différencie un outil générique d'un expert.

---

<!-- _class: section -->

# MCP : le standard universel

## Un type particulier de Tool — le protocole qui connecte tout agent à tout outil

---

<!-- _class: img-right -->

# 09 — Le problème M×N des intégrations

Sans standard, **chaque application IA** doit écrire un connecteur dédié pour **chaque outil** [1] :

- 4 apps × 5 outils = **20 intégrations** à maintenir
- Chaque connecteur a son format, son auth, ses bugs
- Un nouvel outil ? Il faut le connecter à chaque app

C'est le monde **avant USB-C** : chaque appareil avait son propre câble.

> Le coût d'intégration croît de façon **multiplicative** (M×N). Chaque nouvel outil ou app augmente la dette technique [1].

![bg right:55% contain](assets/mcp-hf/mcp-vertical-stack.png)

<small>Sources : [1] [HuggingFace — MCP Course](https://huggingface.co/learn/mcp-course/unit1/key-concepts) · [2] [Anthropic — MCP](https://www.anthropic.com/news/model-context-protocol)</small>

---

<!-- _class: img-right -->

# 10 — La solution MCP : M+N

Le **Model Context Protocol** (Anthropic, nov. 2024) standardise la connexion LLM ↔ outils [1] :

- Chaque app implémente le **client** une seule fois
- Chaque outil implémente le **serveur** une seule fois
- Résultat : **M+N** intégrations au lieu de M×N

**L'adoption en 2026** :
- **~90M+ téléchargements SDK/mois** [1]
- **10 000+ serveurs** MCP actifs [1]
- Donné à l'**AAIF** (Linux Foundation) — **146 membres** [2]

![bg right:55% contain](assets/mcp-with-standard.png)

<small>Sources : [1] [Anthropic — MCP](https://www.anthropic.com/news/model-context-protocol) · [2] [AAIF — Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)</small>

---

<!-- _class: img-right -->

# 11 — Architecture MCP : Host, Client, Server

3 composants avec des rôles clairs [1] :

- **Host** = l'application utilisateur (Claude Desktop, Cursor, votre app)
- **Client** = le composant dans l'app qui communique (relation 1:1 avec un Server)
- **Server** = le programme externe qui expose des capacités

**Exemple concret** :
- Host = **n8n** (votre workflow)
- Client = n8n MCP connector
- Server = **Wikipedia Search MCP** → l'agent peut chercher Wikipedia

![bg right:55% contain](assets/mcp-components.png)

<small>Sources : [1] [HuggingFace — MCP Course](https://huggingface.co/learn/mcp-course/unit1/key-concepts)</small>

---

<!-- _class: img-right -->

# 12 — Les 4 types de capacités MCP

Un Server MCP peut exposer 4 types de capacités [1] :

- **Tools** — fonctions exécutables (`create_issue()`, `send_email()`)
- **Resources** — données en lecture seule (fichiers, docs, DB)
- **Prompts** — templates réutilisables ("Analyse ce code")
- **Sampling** — le serveur demande au LLM de raisonner

> **Tools** = ce que l'agent **fait**. **Resources** = ce que l'agent **sait**. **Prompts** = comment l'agent **aborde** un problème [1].

![bg right:55% contain](assets/mcp-hf/mcp-capabilities-8.png)

<small>Sources : [1] [HuggingFace — MCP Course](https://huggingface.co/learn/mcp-course/unit1/key-concepts)</small>

---

<!-- _class: cols -->

# 13 — L'écosystème MCP en 2026

<div class="left">

**Adoption massive** :
- Claude, ChatGPT, Gemini, Copilot, Cursor
- VS Code (via GitHub Copilot)
- AWS, Cloudflare, Google Cloud, Azure
- **AAIF** (Linux Foundation, 146 membres) [1]

</div>
<div class="right">

**Opportunité business** :
- 1 serveur MCP = compatible avec **tous** les agents
- Coût d'intégration : **heures** au lieu de semaines
- Exemples : Stripe MCP, GitHub MCP, Notion MCP, Slack MCP

</div>

> **Opportunité entrepreneuriale** : créer un serveur MCP pour un outil métier non couvert = accès instantané à l'écosystème entier.

<small>Sources : [1] [AAIF — Linux Foundation](https://www.linuxfoundation.org/press/agentic-ai-foundation-welcomes-97-new-members)</small>

---

<!-- _class: cols -->

# 14 — MCP : les risques de sécurité

<div class="left">

**3 attaques documentées** [1] :
- **Tool Poisoning** — description malveillante dans le tool qui injecte des instructions
- **Rug Pull** — outil légitime qui change de comportement après approbation
- **Cross-Server Shadowing** — un serveur malveillant qui intercepte les appels d'un autre

</div>
<div class="right">

**Mesures de protection** :
- Vérifier les descriptions des tools (pas seulement les noms)
- Utiliser des serveurs MCP de sources vérifiées
- Auditer les permissions accordées
- Monitorer les actions exécutées

</div>

> Sécurité MCP = sujet critique. Invariant Labs a démontré ces attaques dès avril 2025 [1].

<small>Sources : [1] [Invariant Labs — MCP Security](https://invariantlabs.ai/)</small>

---

<!-- _class: cols -->

# 15 — MCP : le débat

<div class="left">

**Pour MCP** :
- **Standardisation** — un seul protocole au lieu de N intégrations ad-hoc
- **Effet réseau** — 10K+ serveurs, 146 membres AAIF
- **Sécurité** — modèle de permissions intégré
- **Vendor-neutral** — donné à la Linux Foundation

</div>
<div class="right">

**Contre MCP** :
- **Couche d'abstraction supplémentaire** — complexité pour des cas simples
- **Function Calling natif** s'améliore rapidement (OpenAI, Google)
- **Standardisation prématurée ?** — le domaine évolue vite
- **Risque d'écosystème fermé** malgré l'ouverture formelle

</div>

> Le débat de fond : **une abstraction universelle est-elle nécessaire**, ou le Function Calling natif rendra-t-il MCP obsolète à terme ?

---

# 16 — Discussion : MCP pour votre startup ?

> Vous développez un **assistant IA pour la gestion de projet**. Il doit se connecter à Slack, Jira, Google Calendar et la base de données interne de l'entreprise.

**Questions pour la classe** :

- Implémentez-vous MCP ou des intégrations natives directes ? Quel est le trade-off ?
- Si vous choisissez MCP, comment gérez-vous la sécurité (un serveur malveillant pourrait lire vos tickets Jira) ?
- Quel serait l'avantage de publier votre intégration Jira comme un serveur MCP open source ?

---

<!-- _class: section -->

# L'échelle de complexité

## 5 patterns, du plus simple au plus autonome

---

<!-- _class: img-right -->

# 17 — La règle d'or : commencer simple

Anthropic "Building Effective Agents" [1] :

| Niveau | Pattern |
|---|---|
| 1 | Prompt Chaining |
| 2 | Routing |
| 3 | Parallelization |
| 4 | Orchestrator-Workers |
| 5 | Evaluator-Optimizer |
| 6 | Agent autonome |

> "The most successful implementations weren't using complex frameworks." — La plupart des problèmes business se résolvent aux niveaux 1–3.

![bg right:55% contain](assets/infographics/anthropic-complexity-ladder.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 18 — Prompt Chaining : la séquence maîtrisée

Décomposer une tâche en **étapes séquentielles** — chaque appel LLM traite la sortie du précédent [1].

**Exemple business** — Générer un brief marketing :
1. Analyser le produit → 2. Identifier le persona → 3. Rédiger le brief → 4. **Gate check** qualité

**Gate checks** : entre chaque étape, une vérification valide la sortie avant de continuer.

> Le Prompt Chaining couvre **la majorité des cas d'usage business** sans la complexité d'un agent.

![bg right:55% contain](assets/anthropic/prompt-chaining.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 19 — Routing : diriger vers le bon handler

Classifier l'input, puis **diriger vers un handler spécialisé**. Le LLM agit comme un aiguilleur [1].

**Exemple business** — Support client :
- Questions simples → LLM léger ($)
- Questions complexes → LLM premium ($$)
- Réclamations → escalade humaine

> Le Routing permet d'optimiser **coût et qualité simultanément** — les cas simples coûtent moins, les cas complexes reçoivent plus d'attention.

![bg right:55% contain](assets/anthropic/routing.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 20 — Parallélisation : plusieurs LLMs en simultané

Deux variantes complémentaires [1] :

**Sectioning** — sous-tâches indépendantes en parallèle :
- Analyser les aspects juridique, financier et technique d'un contrat *simultanément*

**Voting** — même tâche, plusieurs fois :
- 3 LLMs font un code review, la majorité gagne

> **Quand l'utiliser** : quand la vitesse ou la fiabilité importent plus que le coût (2–3x) [1].

![bg right:55% contain](assets/anthropic/parallelization.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 21 — Orchestrator-Workers : le chef de projet IA

Un LLM central **décompose dynamiquement** la tâche, délègue à des workers spécialisés, et synthétise [1].

**Exemple** — "Analyse ce marché" :
- L'orchestrateur décompose : taille, concurrents, réglementation, tendances, risques
- Workers en parallèle → synthèse cohérente

**Différence clé avec la Parallélisation** : les sous-tâches ne sont **pas prédéfinies** — l'orchestrateur les décide au runtime.

![bg right:55% contain](assets/anthropic/orchestrator-workers.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: img-right -->

# 22 — Evaluator-Optimizer : la boucle d'amélioration

Un LLM **génère**, un autre **évalue** et donne du feedback. On boucle jusqu'au seuil de qualité [1].

**Exemple** — Rédaction d'offre commerciale :
- Le Generator rédige l'offre
- L'Evaluator vérifie : ton, chiffres, conformité au brief
- Feedback → correction → reboucle

**Précaution** : chaque itération = coût. Mettez un **circuit breaker** (max 3–5 tours).

![bg right:55% contain](assets/anthropic/evaluator-optimizer.png)

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

# 23 — Discussion : quel pattern pour votre projet ?

> Vous lancez un service de **veille concurrentielle automatisée** pour des PME. Les clients envoient le nom d'un concurrent et reçoivent un rapport hebdomadaire.

**Questions pour la classe** :

- Quel(s) pattern(s) de l'échelle utiliseriez-vous ? Pourquoi ?
- À quel niveau commenceriez-vous ? Quel serait votre critère pour monter d'un cran ?
- Quel circuit breaker mettriez-vous en place ?

---

<!-- _class: section -->

# La mémoire des agents

## Comment un agent retient et s'améliore

---

# 24 — Pourquoi la mémoire change tout

Sans mémoire, l'agent est un **"poisson rouge"** — il recommence à zéro à chaque session.

Avec mémoire, l'agent connaît vos préférences, vos décisions passées, votre contexte métier.

**Connexion avec le Deck B** : la mémoire utilise les mêmes techniques que le RAG (embeddings, vector DB, retrieval) — appliquées à l'historique de l'agent plutôt qu'à des documents.

> La mémoire est ce qui transforme un outil jetable en **assistant fidèle**. C'est le pont entre le RAG (Deck B) et les Agents.

---

<!-- _class: compact-table -->

# 25 — Les types de mémoire : taxonomie LLM

Du point de vue du LLM, **4 mécanismes** pour retenir de l'information :

| Type | Durée de vie | Mécanisme | Exemple |
|---|---|---|---|
| **System Prompt** | Par session | Injecté à chaque requête | CLAUDE.md, system message |
| **Conversation History** | Par session | Buffer de messages (context window) | Chat, échanges précédents |
| **Persistent Files** | Cross-session | Fichiers lus/écrits par l'agent | memory.md, SOUL.md, config |
| **External Database** | Permanent | Vector DB, SQL, knowledge graph | RAG, historique client |

> Du plus éphémère (prompt) au plus durable (database) — chaque type répond à un besoin différent. L'agent combine les 4.

---

<!-- _class: cols -->

# 26 — Mémoire en pratique : du court au long terme

<div class="left">

**Court terme (session)** :
- **Conversation History** — les N derniers messages dans la fenêtre de contexte
- Quand ça déborde → **compaction** (résumé automatique)
- Ex : Claude résume les anciens messages pour garder le contexte

</div>
<div class="right">

**Long terme (cross-session)** :
- **Persistent Files** — CLAUDE.md, MEMORY.md, SOUL.md
- **External DB** — vector store (comme le RAG du Deck B) appliqué aux interactions passées
- Ex : "la dernière fois, on avait choisi la stratégie X"

</div>

> **Trade-off** : court terme = rappel exact mais éphémère. Long terme = durable mais nécessite un bon système de retrieval.

---

# 27 — Le pattern fichier-markdown

Le pattern le plus pragmatique : l'agent **écrit** sa mémoire dans des fichiers lisibles.

**Exemples concrets** :
- **CLAUDE.md** — instructions projet persistantes, relues à chaque session
- **MEMORY.md** — Claude Code écrit ses leçons apprises automatiquement
- **SOUL.md / IDENTITY.md** — OpenClaw stocke sa personnalité et le profil utilisateur

**Avantage clé** : mémoire lisible par l'humain, versionnable (Git), débugable — vous pouvez lire et éditer la mémoire de l'agent.

> Le fichier-markdown est la mémoire la plus simple et la plus puissante. Vous l'utilisez déjà dans ce cours avec CLAUDE.md.

---

# 28 — Discussion : quelle mémoire pour votre agent ?

> Vous construisez un **assistant IA pour une agence immobilière**. Il doit : (1) se souvenir des préférences de chaque client (budget, quartiers, critères), (2) rappeler les biens déjà visités, (3) adapter ses recommandations au fil du temps.

**Questions pour la classe** :

- Quels types de mémoire utiliseriez-vous pour chacun de ces 3 besoins ?
- Où stockeriez-vous cette mémoire ? (Fichier, vector DB, base relationnelle ?)
- Quel est le risque si l'agent "oublie" un client ?

---

<!-- _class: section -->

# Agents en production

## Erreurs composées, failure modes et garde-fous

---

# 29 — Le problème des erreurs composées

Pourquoi les agents autonomes échouent souvent ? Les **erreurs se multiplient** à chaque étape :

- 10 étapes × 95% de fiabilité chacune = **60% de succès global** (0,95^10)
- 20 étapes × 95% = **36%** de succès
- 50 étapes × 95% = **8%** de succès

**Les solutions** :
- **Réduire le nombre d'étapes** — simplifier le workflow au maximum
- **Augmenter la fiabilité par étape** — meilleurs prompts, meilleurs tools, validation
- **Human-in-the-Loop** — supervision humaine aux points critiques

> Gartner prévoit **40%** des projets agents annulés d'ici 2027 [1]. La fiabilité, pas la sophistication, est le vrai défi.

<small>Sources : [1] [Gartner](https://www.gartner.com/)</small>

---

<!-- _class: cols -->

# 30 — Failure Modes : quand les agents déraillent

<div class="left">

**Les modes de défaillance** :
- **Context Drift** — oublie son objectif
- **Infinite Loop** — boucle sans fin
- **Wrong Tool** — mauvais outil pour la tâche
- **Hallucinated Success** — déclare victoire sans vérifier

</div>
<div class="right">

**Les garde-fous** :
- **Human-in-the-Loop** aux étapes critiques
- **Retry + escalade** (3 essais → humain)
- **Observabilité** — logger chaque étape ReAct
- **Budget** tokens/étapes = circuit breaker

</div>

> La plupart des bugs d'agent se résolvent en améliorant le **prompt** ou les **descriptions des tools** [1].

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)</small>

---

<!-- _class: compact -->

# 31 — Quand NE PAS utiliser un agent

Anthropic le dit clairement : les agents ajoutent latence, coût et risque [1].

**Utilisez un agent quand** :
- La tâche nécessite des décisions flexibles et imprévisibles
- Le nombre d'étapes ne peut pas être défini à l'avance
- La valeur de la tâche justifie le coût supplémentaire

**N'utilisez PAS un agent quand** :
- Un simple Prompt Chain suffit (la majorité des cas)
- Le workflow est prévisible et fixe
- Le coût de l'erreur est élevé et la supervision est difficile

> **1 agent bien outillé > N agents mal coordonnés** — Cognition (Devin) et Cline ont tous deux choisi le Single-Agent : le multi-agent crée un "jeu du téléphone" où le contexte se perd [2][3].

<small>Sources : [1] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) · [2] [Cognition — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-cognition-does-not-use-multi-agent-systems/) · [3] [Cline — via jxnl.co](https://jxnl.co/writing/2025/09/11/why-i-stopped-using-rag-for-coding-agents-and-you-should-too/)</small>

---

<!-- _class: compact-table -->

# 32 — Investir dans l'IA : Discovery-first

**Ne commencez pas par construire — commencez par découvrir** [1]. 3 niveaux d'investissement :

| Niveau | Form Factor | Objectif | Investissement |
|---|---|---|---|
| **1 — Discovery** | Chatbot + MCP | Découvrir les cas d'usage organiquement | Faible (infra partagée) |
| **2 — Automation** | Agent | Automatiser les workflows validés | Moyen (après validation data) |
| **3 — Specialization** | Dashboard/UI | Interface dédiée pour workflows prouvés | Élevé (après ROI démontré) |

**Formule de priorisation** : `volume × taux de succès × valeur par interaction`

> "Si vous connaissez la valeur économique, construisez directement. Le Discovery-first, c'est quand vous ne savez pas encore où est la valeur." [1]

<small>Sources : [1] [Jason Liu — How to Invest in AI](https://jxnl.co/writing/2025/06/09/how-to-invest-in-ai-w-mcps-and-data-analytics/)</small>

---

# 33 — Le cas compliance : Discovery → Dashboard

**Timeline réelle** d'un projet IA Discovery-first [1] :

- **Jour 1** — Planning data exposé via MCP. Les managers demandent "Qui travaille aujourd'hui ?"
- **Semaine 2** — Demandes de vérification compliance → MCP de recherche
- **Semaine 4** — Besoin de contacter les non-conformes → MCP de messagerie
- **Mois 2** — Analyse des logs : compliance = **40%** des interactions → agent automatisé
- **Mois 4** — Dashboard compliance dédié avec agent en background

> **L'analyse des conversations** (clustering type Kura/Clio) révèle les vrais besoins. Sans data, vous construisez dans le vide [1].

<small>Sources : [1] [Jason Liu — How to Invest in AI](https://jxnl.co/writing/2025/06/09/how-to-invest-in-ai-w-mcps-and-data-analytics/)</small>

---

<!-- _class: section -->

# Context Engineering

## Concevoir l'environnement de l'agent

---

<!-- _class: img-right -->

# 34 — Context Engineering : au-delà du prompt

Le **Context Engineering** conçoit tout l'environnement informationnel de l'agent [1] :

- **Write** — persister (CLAUDE.md, bases)
- **Select** — retriever le pertinent (RAG)
- **Compress** — résumer et compacter
- **Isolate** — partitionner entre agents

**Les dangers** : **Context Pollution** (91% de bruit [2]) et **Context Rot** (dégradation sur les longues sessions).

> **Context Engineering > Prompt Engineering** — concevez l'environnement, pas juste le prompt [1].

![bg right:55% contain](assets/infographics/context-engineering-4-ops.png)

<small>Sources : [1] [Jason Liu — CE Index](https://jxnl.co/writing/2025/08/28/context-engineering-index/) · [2] [Jason Liu — Subagents](https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/)</small>

---

<!-- _class: cols -->

# 35 — Subagents : isoler le travail sale

<div class="left">

**Slash Commands** — tout dans le thread :
- Logs, tests, git history → injectés directement
- Thread : **169K tokens, 91% bruit**
- Le raisonnement se noie

</div>
<div class="right">

**Subagents** — workers séparés :
- Propre fenêtre de contexte
- Thread principal : **21K tokens, 76% signal**
- Subagent brûle 150K en isolation

</div>

> **Règle** : les lectures se parallélisent, les écritures se centralisent. Applications : due diligence, research synthesis [1].

<small>Sources : [1] [Jason Liu — Subagents](https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/)</small>

---

<!-- _class: img-right -->

# 36 — Compaction : le momentum de l'agent

La **Compaction** = résumer l'historique quand la fenêtre de contexte se remplit [1].

**L'analogie momentum** : la compaction préserve la **trajectoire d'apprentissage** :
- "J'ai essayé X, ça a échoué → Y a marché parce que Z"
- Trop tôt = perdre le momentum. Trop tard = overflow

**Trajectory Observability** : boucles infinies, conflits de linter, corrélation feedback ↔ performance.

> La compaction n'est pas un simple résumé — c'est une **lentille d'observation** sur le comportement de l'agent [1].

![bg right:55% contain](assets/infographics/compaction-momentum.png)

<small>Sources : [1] [Jason Liu — Compaction](https://jxnl.co/writing/2025/08/30/context-engineering-compaction/)</small>

---

<!-- _class: section -->

# Produits agents

## De Claude Code à OpenClaw

---

<!-- _class: img-right -->

# 37 — Claude Code : l'agent qui code

Un agent terminal-native qui lit, écrit et exécute du code de manière autonome [1] :

- Lit/écrit des fichiers, exécute bash, gère git
- **CLAUDE.md** — instructions projet persistantes
- **MEMORY.md** — mémoire automatique entre sessions
- **Skills** — capacités modulaires réutilisables
- **Subagents** — parallélise les sous-tâches

**Le Knowledge Work Stack** [2] :
1. Model → 2. Harness (Claude Code) → 3. Personal Scaffolding (CLAUDE.md) → 4. MCPs/APIs → 5. Agents

![bg right:55% contain](assets/agent_stack-claude_code.jpeg)

<small>Sources : [1] [Anthropic — Claude Code](https://www.anthropic.com/) · [2] [Taylor Pearson](https://x.com/TaylorPearsonMe/status/2029996204306866585)</small>

---

<!-- _class: compact -->

# 38 — OpenClaw : l'agent autonome viral

**OpenClaw** = agent IA local, open source, qui agit sur votre machine et vos services [1][2] :

- **315K+ GitHub stars** en 4 mois — le projet OSS à la croissance la plus rapide de l'histoire [1]
- Créé par Peter Steinberger (fondateur de PSPDFKit), lancé en nov. 2025

**Pulse Files** — la mémoire identitaire de l'agent :
- **SOUL.md** — personnalité, ton, valeurs, préférences de communication
- **IDENTITY.md** — profil utilisateur, habitudes, contexte professionnel
- Relus à chaque session → l'agent **se souvient de qui il est et de qui vous êtes**

**Les risques** : Cisco a trouvé que **26% des 31 000 Skills** contenaient des vulnérabilités [3]. L'incident MoltMatch : un agent a créé un profil de rencontre sans consentement explicite [4].

<small>Sources : [1] [GitHub — OpenClaw](https://github.com/openclaw/openclaw) · [2] [DigitalOcean](https://www.digitalocean.com/resources/articles/what-is-openclaw) · [3] [Cisco](https://blogs.cisco.com/ai/personal-ai-agents-like-openclaw-are-a-security-nightmare) · [4] [AFP/Taipei Times](https://www.taipeitimes.com/News/world/archives/2026/02/14/2003852326)</small>

---

# 39 — Discussion : quel produit agent pour votre startup ?

> Vous lancez une startup d'**analyse juridique automatisée**. Vous devez choisir comment intégrer l'IA dans votre produit.

**Questions pour la classe** :

- Commenceriez-vous avec **Claude Code** pour prototyper, ou directement un framework comme LangGraph ?
- Quel rôle joueraient les **Skills** dans votre produit ? Lesquelles seriez-vous prêts à partager, lesquelles garder propriétaires ?
- Comment géreriez-vous les risques de sécurité type MoltMatch — un agent qui agit au-delà de ce que le client a demandé ?

---

<!-- _class: section -->

# Agents en action

## Cas concrets et synthèse

---

<!-- _class: img-right -->

# 40 — Karpathy AutoResearch : la recherche autonome

**AutoResearch** (Karpathy, mars 2026) = boucle de recherche ML autonome [1] :

- **~630 lignes** de Python, 1 GPU (H100), MIT
- **~12 expériences/heure**, ~100 par nuit
- **Premier run** : 126 expériences en 10h [2]
- **Run étendu** : ~700 modifications, **11% de gain** sur "Time to GPT-2" [3]

**"Programming the program"** : l'humain itère sur `program.md`, l'agent itère sur le code [1].

> "You're not touching any of the Python files. You are programming the program.md files that provide context to the AI agents." — Karpathy [1]

![bg right:55% contain](assets/infographics/autoresearch-loop.png)

<small>Sources : [1] [Karpathy — AutoResearch](https://github.com/karpathy/autoresearch) · [2] [Discussion #43](https://github.com/karpathy/autoresearch/discussions/43) · [3] [Karpathy — X](https://x.com/karpathy/status/2031135152349524125)</small>

---

# 41 — AutoResearch : les leçons

Ce que ce projet nous enseigne sur les agents :

- **L'agent n'est pas créatif — il est systématique.** 126 expériences = aucun humain ne les ferait en une nuit. C'est la force brute intelligente.
- **"Programming the program"** : vous décrivez les contraintes et objectifs en langage naturel. L'agent explore l'espace des solutions.
- **Le pattern Evaluator-Optimizer à l'échelle** : c'est exactement le pattern de la slide 22, appliqué 100 fois par nuit avec un circuit breaker de 5 minutes.

**Applicable au-delà du ML** : tests A/B automatisés, optimisation de campagnes marketing, veille documentaire, fine-tuning de prompts.

> Tobi Lutke (CEO Shopify) a appliqué le pattern : 37 expériences en une nuit, **19% d'amélioration**, un modèle 0,8B qui bat son ancien modèle 1,6B [1].

<small>Sources : [1] [Tobi Lutke — X](https://x.com/tobi/status/2030771823151853938)</small>

---

<!-- _class: section -->

# Synthèse

## Les briques essentielles de l'agent IA

---

<!-- _class: compact-table -->

# 42 — La boîte à outils : vue d'ensemble

| Brique | Ce que c'est | Ce que vous savez faire |
|---|---|---|
| **Tools** | Fonctions atomiques (Function Calling) | Connecter un LLM au monde réel |
| **Skills** | Savoir-faire complet (SKILL.md) | Créer des processus réutilisables |
| **MCP** | Standard universel LLM ↔ outils | Évaluer les intégrations MCP |
| **Patterns** | 5 niveaux de complexité (Anthropic) | Choisir le bon pattern pour votre cas |
| **Mémoire** | 4 types LLM-centrés | Concevoir la persistance de l'agent |
| **Production** | Erreurs composées, garde-fous | Anticiper les failure modes |
| **Context Eng.** | Write/Select/Compress/Isolate | Concevoir l'environnement de l'agent |

> Vous avez maintenant toutes les briques. L'art est de **choisir les bonnes** et de **commencer simple**.

---

<!-- _class: compact -->

# 43 — Key Takeaways

1. **Le spectre d'agence** — 5 niveaux, de simple processor à multi-agent. La plupart des cas business = niveaux ★☆☆ et ★★☆
2. **Tools → Skills** — Tool = connectivité atomique. Skill = savoir-faire complet. Vos Skills = votre avantage compétitif
3. **MCP = USB-C pour l'IA** — M+N au lieu de M×N. ~90M+ downloads/mois, 10K+ serveurs. Mais le débat reste ouvert
4. **L'échelle Anthropic** — 5 patterns, commencez par le Prompt Chaining. La plupart des problèmes se résolvent aux niveaux 1–3
5. **Mémoire LLM-centrée** — prompt, historique, fichiers persistants, base externe. Le fichier-markdown est le pattern le plus pragmatique
6. **Discovery-first** — Chat → Agent → Dashboard. Analysez les conversations avant de construire
7. **Prudence en production** — erreurs composées, 1 agent bien outillé > N agents mal coordonnés

---

# 44 — Pour la suite

**À explorer** :
- Testez Claude Code avec un CLAUDE.md personnalisé pour votre projet de classification
- Identifiez quel pattern de l'échelle Anthropic convient à votre projet
- Explorez un serveur MCP existant (GitHub, Slack, Notion)
- Lisez le README d'AutoResearch : "programming the program" s'applique à vos propres agents

**Prochaine séance : Le business de l'IA**
- L'écosystème IA (qui fait quoi, la chaîne de valeur)
- Business Models & cas réels (Klarna, Mistral AI, L'Oréal)

> "Le LLM est le consultant. Le RAG est le dossier client. L'agent est l'assistant qui va chercher le dossier, l'analyse, et planifie les prochaines étapes."
