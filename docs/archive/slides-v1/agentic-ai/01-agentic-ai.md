---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Agentic AI 2024–2026 · Données publiques"
---

<!-- ABOUTME: L'IA agentique — agents, frameworks, protocoles, produits et marché 2024-2026. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : comprendre les agents, choisir ses outils, évaluer les risques. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# L'IA Agentique

## Comprendre, construire, déployer les agents IA

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# L'ère des agents

## De l'assistant au collègue autonome

---

# 01 — Qu'est-ce qu'un agent IA ?

Un agent IA est un système qui **perçoit → raisonne → agit → apprend** en boucle :

- **Chatbot** : répond à une question, pas d'action réelle
- **Copilot** : suggère, l'humain décide et exécute
- **Agent** : planifie, utilise des outils, exécute, vérifie le résultat

Le pattern dominant est **ReAct** (Reasoning + Acting) : le modèle alterne réflexion et action dans une boucle itérative [1]

> Spectre d'autonomie : human-in-the-loop → supervised → fully autonomous. Plus d'autonomie = plus de valeur potentielle, mais plus de risque.

<small>Sources : [1] [Princeton/Google Research](https://arxiv.org/abs/2210.03629)</small>

---

# 02 — Le marché en chiffres

- Marché agentic AI : **$7 Mds** (2025) → **$139-260 Mds** (2034), CAGR **40-46%** [1]
- **67%** des Fortune 500 ont déployé des agents en 2025, 78% projeté en 2026 [2]
- **$2,8 Mds** investis en VC agentic AI au S1 2025 seul [3]
- IDC : les dépenses agentic AI atteindront **$1 300 Mds** (26% du IT mondial) d'ici 2029 [4]
- MAIS Gartner : **40%** des projets agents annulés d'ici 2027 [2]

> Un marché en hypercroissance, mais avec un taux d'échec élevé. L'opportunité est réelle — la prudence aussi.

<small>Sources : [1] [Precedence Research](https://www.precedenceresearch.com/) · [2] [Gartner](https://www.gartner.com/) · [3] [Crunchbase](https://news.crunchbase.com/) · [4] [IDC](https://www.idc.com/)</small>

---

# 03 — Qui utilise des agents ? Les cas d'usage

| Secteur | Part marché | Cas concret |
|---------|------------|-------------|
| Tech & Software | **38%** | Devin (Goldman Sachs, Cisco) |
| Finance / BFSI | **19%** | Banques UE : **€20 M+** d'économies en 3 ans |
| Healthcare | CAGR **48%** | Aide à la décision clinique |
| Retail | Croissance forte | Reddit : **46%** de deflection client |
| IT Operations | Triage autonome | ServiceNow : 85% Fortune 500 |

- **23%** des entreprises scalent l'agentic AI, **39%** expérimentent [1]
- Seulement **34%** réussissent le passage en production [2]

<small>Sources : [1] [McKinsey](https://www.mckinsey.com/) · [2] [Gartner](https://www.gartner.com/) · [Precedence Research](https://www.precedenceresearch.com/)</small>

---

<!-- _class: section -->

# Les outils pour construire

## Frameworks, protocoles, no-code

---

# 04 — Le stack agent : vue d'ensemble

Chaque couche = une décision **build vs buy** pour l'entrepreneur :

| Couche | Rôle | Exemples |
|--------|------|----------|
| **LLM** | Le cerveau | GPT-4o, Claude, Mistral, Gemini |
| **Framework** | L'ossature | LangChain, CrewAI, Strands |
| **Protocole** | La connectique | MCP (outils), A2A (inter-agents) |
| **Produit** | La solution | Devin, Cursor, Agentforce |

- Plus on monte dans le stack, plus c'est **accessible** mais moins c'est **personnalisable**
- Le choix dépend de votre compétence technique et de votre time-to-market

---

# 05 — Frameworks : LangChain, CrewAI & les autres

| Framework | Stars GitHub | Licence | Différenciateur |
|-----------|-------------|---------|-----------------|
| LangChain | **120K** | MIT | Écosystème le plus large, LangSmith |
| AutoGen (MS) | **52K** | MIT | Multi-agent, delegation patterns |
| CrewAI | **44K** | MIT | Agents par rôles (crew metaphor) |
| smolagents (HF) | **25K** | Apache 2.0 | Léger, intégré Hugging Face |
| Strands (AWS) | **5K** | Apache 2.0 | MCP + A2A natif, Amazon Q |
| Google ADK | Nouveau | Apache 2.0 | Intégration Vertex AI |

- LangChain : **70M+ téléchargements/mois**, $125M levés (Sequoia, oct 2025) [1]

<small>Sources : [1] [TechCrunch](https://techcrunch.com/) · [GitHub](https://github.com/)</small>

---

<!-- _class: cols -->

# 06 — Spotlight : MCP & A2A — les standards ouverts

<div class="left">

- **MCP** : Anthropic → donné à l'AAIF [1]
- **21,6K** stars, **60+** serveurs MCP
- Protocole universel IA → outils
- Adopté par LangChain, Strands, Cursor

</div>
<div class="right">

- **A2A** : Google → Linux Foundation [2]
- **21,8K** stars, protocole inter-agents
- IBM ACP fusionné dans A2A (sept 2025)
- AAIF gouverne MCP + A2A + AGENTS.md

</div>

<small>Sources : [1] [Anthropic](https://docs.anthropic.com/mcp/) · [2] [Google Cloud](https://cloud.google.com/blog/)</small>

---

# 07 — No-code vs code-first : choisir son approche

| Critère | No-Code | Code-First |
|---------|---------|------------|
| **Outil type** | n8n, Relevance AI, Replit Agent | LangChain, CrewAI, Strands |
| **Time-to-market** | Heures/jours | Semaines/mois |
| **Personnalisation** | Limitée | Totale |
| **Coût initial** | Faible | Moyen à élevé |
| **Compétence requise** | Business user | Développeur |

- **n8n** : $2,5 Mds de valorisation, **89K** stars GitHub, 200K+ utilisateurs actifs [1]
- **Relevance AI** : **40 000** agents créés en janvier 2025 seul [2]
- **Replit Agent** : **40M** utilisateurs, **58%** ne sont pas développeurs [3]

<small>Sources : [1] [n8n GitHub](https://github.com/n8n-io/n8n) · [2] [Relevance AI](https://relevanceai.com/) · [3] [Replit](https://blog.replit.com/)</small>

---

# 08 — Discussion : Build vs Buy pour votre agent

> Votre **SaaS de support client** reçoit 500 tickets/jour. Vous voulez déployer un agent pour automatiser les réponses niveau 1. Quatre options :

| Option | Approche | Budget | Délai |
|--------|----------|--------|-------|
| A | **n8n** (no-code) | ~$5K/an | 2 semaines |
| B | **LangChain** (custom) | ~$50K+ | 2-3 mois |
| C | **Salesforce Agentforce** | $2/conversation | 1 mois |
| D | **API directe** (from scratch) | $100K+ | 4-6 mois |

**Questions pour la classe** :
- Quel niveau d'autonomie pour un agent qui interagit avec vos vrais clients ?
- Comment justifier l'option C à $2/conversation si vous avez 500 tickets/jour ?

---

<!-- _class: section -->

# Les produits agents

## Qui fait quoi, et pour qui

---

# 09 — Les agents de code

| Produit | Stars / Users | Métrique clé |
|---------|-------------|--------------|
| OpenAI Codex | **60K** stars | Modes suggest/review/edit |
| Claude Code | **52K** stars | $1 Mds ARR (plateforme) |
| Devin | 350+ entreprises | **$73M** ARR, $10,2 Mds val. |
| Cursor | 1M+ DAU | **$1 Mds** ARR, $29 Mds val. |
| GitHub Copilot | **77M** devs | Standard de fait, intégré VS Code |
| Google Jules | GA août 2025 | Full-stack, Gemini 3 natif |

- **85%** des développeurs utilisent des outils IA au quotidien [1]

<small>Sources : [1] [JetBrains Survey 2025](https://www.jetbrains.com/lp/devecosystem/) · [GitHub](https://github.com/) · [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: cols -->

# 10 — Spotlight : Devin

<div class="left">

- **$1M → $73M** ARR en 9 mois [1]
- Valorisation **$10,2 Mds** [1]
- Goldman Sachs, Cisco, Palantir clients [2]
- Pricing : $500/mois → **$20/mois** (pivot)

</div>
<div class="right">

- Positionné "AI software engineer" [2]
- SWE-bench : 13,86% (premier agent)
- Goldman Sachs : Devin = "nouvel employé"
- Leçon : **l'agent augmente, pas remplace**

</div>

<small>Sources : [1] [Fortune](https://fortune.com/) · [2] [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Replit Agent

<div class="left">

- **$16M → $252,8M** ARR en 1 an [1]
- **40M** utilisateurs, **150K+** payants [1]
- Objectif CEO : **$1 Mds** ARR fin 2026
- Clients : Duolingo, Zillow, Rokt [2]

</div>
<div class="right">

- **58%** des builders ne sont pas devs [2]
- Enabler du Vibe Coding
- Démocratisation de la création logicielle
- Rokt : 135 apps construites en 24h
- Leçon : **l'audience s'élargit**

</div>

<small>Sources : [1] [TechCrunch](https://techcrunch.com/) · [2] [Replit Blog](https://blog.replit.com/)</small>

---

# 12 — Les agents enterprise

| Produit | Métrique clé | Pricing |
|---------|-------------|---------|
| Salesforce Agentforce | **18,5K** deals, 9,5K MAU | $2/conversation |
| ServiceNow AI Agents | **85%** Fortune 500, $3,6 Mds Q4 | Enterprise |
| Manus AI | **$100M** ARR → acquis par Meta ($2 Mds+) | SaaS |
| Vapi (Voice) | **1,5M** devs, 150M assistants | Pay-per-use |

Tendances émergentes :
- **Voice agents** : Vapi, Bland AI, ElevenLabs — IA conversationnelle téléphonique
- **Browser agents** : OpenAI Operator, Anthropic Computer Use — navigation web autonome
- **Digital Labor** : l'agent comme "employé", facturé à la tâche [1]

<small>Sources : [1] [Salesforce](https://www.salesforce.com/agentforce/) · [ServiceNow IR](https://www.servicenow.com/investors) · [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: cols -->

# 13 — Spotlight : Salesforce Agentforce

<div class="left">

- **18 500** deals signés depuis le lancement [1]
- **9 500** MAU, adoption croissante
- Reddit : **46%** de case deflection [1]
- Fisher & Paykel : **66%** requêtes autonomes

</div>
<div class="right">

- Pricing : **$2/conversation** ou $0,10/action
- Autonomie configurable (human → auto)
- Moat : intégration CRM Salesforce
- Framing : **"digital labor"** — l'agent remplace l'agent humain
- Leçon : **le CRM existant = distribution**

</div>

<small>Sources : [1] [Salesforce Earnings](https://www.salesforce.com/investors/) · [Salesforce Agentforce](https://www.salesforce.com/agentforce/)</small>

---

<!-- _class: section -->

# Les risques et les limites

## Hype, sécurité, réalité

---

# 14 — La réalité derrière le hype

- Gartner : **40%+** des projets agents annulés d'ici fin 2027 [1]
- Seulement **34%** des organisations scalent en production [1]
- Coût moyen d'implémentation enterprise : **$890 000** [2]
- **80%** des dirigeants citent la cybersécurité comme barrière n°1 [3]
- Offre > demande (octobre 2025) — consolidation du marché attendue [1]

> Le ROI médian des implémentations matures est de **540%** (McKinsey) — mais ce chiffre ne reflète que les 34% qui réussissent, pas les 40% qui échouent.

<small>Sources : [1] [Gartner](https://www.gartner.com/) · [2] [Axis Intelligence](https://axisintelligence.com/) · [3] [KPMG](https://kpmg.com/)</small>

---

# 15 — Sécurité : le top 10 OWASP Agentic

| # | Risque | Impact |
|---|--------|--------|
| ASI01 | **Excessive Agency** | L'agent agit au-delà de ses permissions |
| ASI02 | **Prompt Injection** | Manipulation via inputs malveillants |
| ASI03 | **Supply Chain** | Dépendances compromises (outils, MCP) |
| ASI04 | **Sensitive Info Disclosure** | Fuite de données via l'agent |
| ASI05 | **Insecure Code Exec** | Code dangereux exécuté sans sandbox |

- OWASP Agentic Top 10 publié le **9 décembre 2025** [1]
- NIST Cybersecurity Framework pour l'IA : **16 décembre 2025** [2]
- Seulement **6%** des organisations ont une stratégie de sécurité IA avancée [3]

<small>Sources : [1] [OWASP](https://owasp.org/) · [2] [NIST](https://www.nist.gov/) · [3] [Gartner](https://www.gartner.com/)</small>

---

<!-- _class: cols -->

# 16 — Spotlight : Vibe Coding

<div class="left">

- Terme créé par **Andrej Karpathy** (fév 2025) [1]
- Collins **Word of the Year** 2025 [2]
- **4M+** vues sur le post original
- Outils : Cursor, Replit, Claude Code, Bolt.new

</div>
<div class="right">

- 58% des utilisateurs Replit ne codent pas
- Création logicielle **démocratisée**
- MAIS : dette sécurité, pas de code review
- "Technical debt accelerator" [1]
- Leçon : **opportunité ET risque**

</div>

<small>Sources : [1] [Andrej Karpathy](https://x.com/karpathy/status/1886192184808149383) · [2] [Collins Dictionary](https://www.collinsdictionary.com/)</small>

---

# 17 — Discussion : Déployer un agent dans votre startup

> Votre **e-commerce** veut déployer un agent IA pour le suivi de commandes. L'agent accède aux données clients, au CRM, et au système de livraison.

**Questions pour la classe** :
- Quel **niveau d'autonomie** ? (Human-in-the-loop pour les remboursements ?)
- Comment gérer une **erreur sur une vraie commande** client ?
- L'EU AI Act s'applique-t-il ? (Données personnelles, décisions automatisées)
- Budget : le coût moyen enterprise est **$890K** — comment faire à l'échelle startup ?
- Quels risques OWASP sont les plus critiques pour votre cas ?

---

<!-- _class: section -->

# L'Europe et la gouvernance

## Régulation, souveraineté, opportunités

---

# 18 — L'EU AI Act et les agents

- Pas de cadre réglementaire spécifique aux agents IA (gap identifié) [1]
- MEP Lagodinsky a demandé des clarifications (sept 2025) — pas de réponse publique [1]
- Enforcement High-Risk AI : **août 2026** [1]
- **30%** citent la data privacy comme barrière, **21%** le manque de clarté réglementaire [2]

Implications pour les entrepreneurs :
- RGPD impose le **self-hosting** pour les données sensibles
- **Langfuse** (MIT, self-hostable) = réponse européenne au monitoring [3]
- **LangSmith** propose une résidence données UE [3]
- Banques européennes : agents compliant → **€20M+** d'économies en 3 ans [3]

<small>Sources : [1] [EU AI Act](https://eur-lex.europa.eu/) · [2] [Gartner](https://www.gartner.com/) · [3] [Langfuse](https://langfuse.com/blog)</small>

---

# 19 — Langfuse & l'écosystème européen

- **Langfuse** : fondé en Allemagne, **21,6K** stars, MIT, 2 000+ clients payants [1]
- Acquis par **ClickHouse** ($15 Mds de valorisation, janv 2026) [1]
- 19 des Fortune 50, 63 des Fortune 500 utilisent Langfuse [1]
- **Mistral AI** : seul provider frontier avec hébergement natif UE [2]
- Compute souverain européen : OVHcloud, Scaleway, GAIA-X

> Le gap réglementaire sur les agents = **opportunité** pour les startups européennes. Qui construira le "compliance layer" pour les agents ?

<small>Sources : [1] [ClickHouse/Langfuse](https://clickhouse.com/) · [2] [Mistral AI](https://mistral.ai/)</small>

---

<!-- _class: section -->

# Synthèse

## Ce qu'il faut retenir

---

# 20 — Les 5 tendances à retenir

1. **Les agents deviennent mainstream** — 67% des Fortune 500 déployés, $7 Mds de marché, tous les hyperscalers investissent massivement

2. **Les standards se consolident** — L'AAIF (AWS, Anthropic, Google, MS, OpenAI) gouverne MCP + A2A + AGENTS.md

3. **Le no-code démocratise** — 58% des utilisateurs Replit ne sont pas développeurs, n8n valorisé $2,5 Mds

4. **L'enterprise reste prudent** — 40% des projets annulés, seulement 34% en production, $890K de coût moyen

5. **Le gap réglementaire UE = opportunité** — pas de cadre spécifique agents, Langfuse/Mistral montrent la voie

<small>Sources : [Gartner](https://www.gartner.com/) · [Replit](https://blog.replit.com/) · [Linux Foundation/AAIF](https://www.linuxfoundation.org/)</small>

---

# 21 — Grille de décision : comment lancer un agent

| Critère | No-Code | Framework | Plateforme | Custom |
|---------|---------|-----------|------------|--------|
| **Outil** | n8n, Relevance | LangChain, CrewAI | Agentforce | API + from scratch |
| **Budget** | < $10K | $50-200K | $2/conv. | $200K+ |
| **Délai** | Jours | 2-3 mois | 1 mois | 4-6 mois |
| **Compétence** | Business user | Développeur | Admin CRM | ML engineer |
| **Risque** | Limites de perso | Maintenance | Vendor lock-in | Coût, délai |

> Le choix dépend de trois variables : **compétence technique**, **budget**, et **niveau de personnalisation requis**.

<small>Sources : [Salesforce](https://www.salesforce.com/agentforce/) · [n8n](https://n8n.io/) · [Axis Intelligence](https://axisintelligence.com/)</small>

---

# 22 — Key Takeaways

1. **Un agent IA perçoit, raisonne, agit et apprend** — c'est plus qu'un chatbot. Le pattern ReAct est le standard, l'autonomie est configurable.

2. **Le marché explose mais reste risqué** — $7 Mds → $260 Mds (2034), mais 40% des projets échouent. Le ROI n'est prouvé que pour les 34% qui scalent.

3. **Les standards ouverts structurent l'écosystème** — MCP (outils), A2A (inter-agents), AGENTS.md (config) sous l'AAIF. Choisir un framework compatible.

4. **Le no-code change la donne** — Replit (58% non-devs), n8n ($2,5 Mds), vibe coding. La création d'agents se démocratise.

5. **L'Europe a des cartes à jouer** — Langfuse (MIT, acquis $15 Mds), Mistral (souveraineté UE), gap réglementaire = terrain à prendre.
