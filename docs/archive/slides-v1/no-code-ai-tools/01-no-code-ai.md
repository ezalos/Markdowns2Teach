---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche No-Code AI Tools 2024–2026 · Données publiques"
---

<!-- ABOUTME: Les outils no-code & IA — chatbots, automatisation, contenu, vibe coding, recherche, self-hosted. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : construire, automatiser et pitcher avec zéro code et zéro budget. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Les Outils No-Code & IA

## Construire, automatiser, pitcher — sans écrire une ligne de code

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Pourquoi le no-code IA

## La barrière entre l'idée et le produit disparaît

---

# 01 — Le no-code IA : pourquoi maintenant ?

- Andrej Karpathy invente le terme **Vibe Coding** (février 2025), 4M+ vues [1]
- Collins Dictionary le nomme **Word of the Year** 2025 [2]
- Le marché low-code/no-code : **$65 Mds** (2024) → **$187 Mds** (2030), CAGR 19% [3]
- **58%** des utilisateurs Replit **ne sont pas développeurs** [4]
- Bolt.new : de **$0 à $40M ARR** en 5 mois [5]

> La promesse : décrivez votre app en langage naturel, obtenez un prototype fonctionnel. La barrière n'est plus technique — elle est créative.

<small>Sources : [1] [Karpathy](https://x.com/karpathy/status/1886192184808149383) · [2] [Collins Dictionary](https://www.collinsdictionary.com/) · [3] [Gartner](https://www.gartner.com/) · [4] [Replit](https://blog.replit.com/) · [5] [Bloomberg](https://www.bloomberg.com/)</small>

---

# 02 — Vue d'ensemble : 25 outils, 7 familles

| Famille | Nb | Exemples | Free tier | UE ? |
|---------|:--:|----------|:---------:|:----:|
| Chatbot / Assistant | 5 | GPT Builder, Mistral, Voiceflow | Oui | Mistral 🇫🇷 |
| Automatisation | 4 | Zapier, Make, n8n, Lindy | Oui | n8n 🇩🇪, Make 🇨🇿 |
| Création de contenu | 4 | Canva, Gamma, Runway, Synthesia | Oui | — |
| Vibe Coding | 4 | Bolt.new, Lovable, Replit, Cursor | Oui | Lovable 🇸🇪 |
| Recherche & Analyse | 3 | NotebookLM, Perplexity, Julius | Oui | — |
| Self-hosted | 2 | Open WebUI + Ollama, Flowise | Oui | — |
| Enterprise | 1 | MS Power Platform AI Builder | Non | — |

---

<!-- _class: section -->

# Construire un chatbot / assistant

## Du Custom GPT au chatbot souverain

---

# 03 — Les chatbot builders : comparatif

| Outil | Créateur | Free tier | Users / Stars | Différenciateur |
|-------|----------|:---------:|---------------|-----------------|
| GPT Builder | OpenAI | $20/mo (Plus) | 3M+ GPTs créés | Écosystème ChatGPT, 800M MAU |
| Mistral Le Chat | Mistral AI 🇫🇷 | Oui (~25 msg/j) | 1M+ mobile | Souverain UE, multilingue |
| Voiceflow | Voiceflow | Oui (100 crédits) | 130K users | Builder visuel, NLU avancé |
| Botpress | Botpress | Oui (500 msg/mo) | 14K stars | Open-core, AGPLv3 |
| Dify | Dify.AI | Oui (200 msg/mo) | **100K+ stars** | Open-source, 2 500+ intégrations |

- Dify : top 100 mondial GitHub, alternative open-source à LangChain [1]

<small>Sources : [1] [GitHub](https://github.com/langgenius/dify) · [OpenAI](https://openai.com/) · [Mistral AI](https://mistral.ai/)</small>

---

<!-- _class: cols -->

# 04 — Spotlight : Mistral Le Chat

<div class="left">

- Valorisation **€11,7 Mds** (sept 2025) [1]
- **€3 Mds+** levés au total [1]
- Le Chat **gratuit**, Pro €14,99/mo, étudiants €5,99
- App mobile : **1M** downloads en 2 semaines

</div>
<div class="right">

- Seul **frontier model UE** [2]
- Hébergé **exclusivement en France** [2]
- Armée française, BNP, AXA, CMA CGM
- **40%** du CAC 40 clients [1]
- RGPD by design, pas de transfert US

</div>

<small>Sources : [1] [TechCrunch](https://techcrunch.com/) · [2] [Mistral AI](https://mistral.ai/)</small>

---

# 05 — Discussion : Quel assistant IA pour votre startup ?

> Vous lancez un **SaaS pour PME françaises**. Vous devez intégrer un assistant IA pour l'onboarding client. Quatre options :

| Option | Approche | Coût | Données |
|--------|----------|------|---------|
| A | Custom GPT | $20/mo (Plus) | Serveurs US |
| B | Mistral Le Chat | Gratuit | 🇫🇷 France only |
| C | Voiceflow | Gratuit → $60/mo | Cloud US |
| D | Dify self-hosted | Gratuit (infra) | 🔒 Vos serveurs |

**Questions pour la classe** :
- Vos clients PME exigent le RGPD — quelle option élimine-t-on d'office ?
- Comment justifier le self-hosting Dify si vous êtes 2 cofondateurs non-tech ?

---

<!-- _class: section -->

# Automatiser avec l'IA

## Connecter, orchestrer, gagner du temps

---

# 06 — Les plateformes d'automatisation IA

| Outil | Users / Stars | Free tier | Intégrations | UE ? |
|-------|---------------|:---------:|:------------:|:----:|
| Zapier | **3M+** users, 100K payants | 100 tasks/mo | 8 000+ | — |
| Make | 250K+ clients | 1 000 ops/mo | 2 500+ | 🇨🇿 Czech |
| n8n | **100K+** stars | Illimité (self) | 400+ core | 🇩🇪 Berlin |
| Lindy AI | $50M+ levés | 400 crédits/mo | 4 000+ | — |

- Zapier : $5 Mds de valorisation, $310M de revenus (2024) [1]
- Make : acquis par Celonis, builder visuel 2D plus puissant que Zapier [2]
- n8n : **seul** à offrir le self-hosting gratuit et illimité [3]

<small>Sources : [1] [Zapier](https://zapier.com/) · [2] [Make](https://www.make.com/) · [3] [n8n](https://n8n.io/)</small>

---

<!-- _class: cols -->

# 07 — Spotlight : n8n

<div class="left">

- **100K+** stars GitHub (top 200 mondial) [1]
- Valorisation **$2,5 Mds** (oct 2025) [1]
- **100M+** Docker pulls, fair-code license
- Self-hosted = **gratuit illimité**

</div>
<div class="right">

- **Berlin, Allemagne** 🇩🇪 [2]
- Cloud hébergé **Azure Frankfurt** (UE)
- Self-hosted = **RGPD total**
- 400+ nœuds core, 5 800+ communauté
- Projet : RSS → résumé IA → réseaux sociaux

</div>

<small>Sources : [1] [n8n GitHub](https://github.com/n8n-io/n8n) · [2] [n8n](https://n8n.io/)</small>

---

<!-- _class: section -->

# Créer du contenu & pitcher

## Du brief au pitch deck en 30 minutes

---

# 08 — Les outils de création de contenu IA

| Outil | Users | Free tier | Output | Prix payant |
|-------|-------|:---------:|--------|-------------|
| Canva Magic Studio | **240M** MAU | Oui (limité) | Design, vidéo | $15/mo |
| Gamma | **70M** users | 400 crédits | Slides, sites | $10/mo |
| Runway ML | 300K+ clients | 125 crédits | Vidéo Gen-4.5 | $12/mo |
| Synthesia | 1M+ users | 3 min/mo | Avatar vidéo | $29/mo |

- Canva : **$3,3 Mds ARR**, 95% du Fortune 500, valorisation $42 Mds [1]
- Gamma : **$100M+ ARR**, $2,1 Mds de valorisation, propulsé par Claude [2]

<small>Sources : [1] [Canva](https://www.canva.com/newsroom/) · [2] [TechCrunch](https://techcrunch.com/)</small>

---

# 09 — Du brief au pitch en 30 minutes

Un workflow **100% gratuit** pour transformer une idée en pitch :

| Étape | Outil | Temps | Coût |
|-------|-------|:-----:|:----:|
| 1. Recherche marché | Perplexity / NotebookLM | 10 min | $0 |
| 2. Slides | Gamma (400 crédits gratuits) | 10 min | $0 |
| 3. Démo vidéo | Runway (125 crédits) | 5 min | $0 |
| 4. Avatar pitch | Synthesia (3 min gratuites) | 5 min | $0 |

- **Total : ~30 minutes, $0 dépensé**
- Il y a 5 ans, ce workflow nécessitait un designer, un vidéaste et 2 semaines

> Le superpower de l'entrepreneur en 2026 : combiner les free tiers pour créer un pitch professionnel en une après-midi.

<small>Sources : [Perplexity](https://www.perplexity.ai/) · [Gamma](https://gamma.app/) · [Runway](https://runwayml.com/) · [Synthesia](https://www.synthesia.io/)</small>

---

<!-- _class: section -->

# Le Vibe Coding

## Coder sans coder — décrire et obtenir

---

# 10 — Qu'est-ce que le Vibe Coding ?

> *"You just see stuff, say stuff, run stuff, and copy-paste stuff, and it mostly works."* — Andrej Karpathy, février 2025 [1]

- Terme créé par l'ex-directeur IA de Tesla, **4M+ vues** en 24h [1]
- Collins **Word of the Year** 2025 [2]
- Principe : décrire en langage naturel → obtenir une app fonctionnelle
- L'IA écrit **100%** du code, l'humain guide et valide

Les 4 plateformes majeures :

| Outil | Cible | Spécificité |
|-------|-------|-------------|
| Bolt.new | Non-devs, fondateurs | Browser, zéro install |
| Lovable | Designers, PMs | Full-stack React/Supabase |
| Replit Agent | Étudiants, builders | IDE cloud, 40M users |
| Cursor | Développeurs | IDE local, multi-modèle |

<small>Sources : [1] [Karpathy](https://x.com/karpathy/status/1886192184808149383) · [2] [Collins Dictionary](https://www.collinsdictionary.com/)</small>

---

# 11 — Les plateformes Vibe Coding : comparatif

| Outil | ARR / Valuation | Free | Prototype en… | UE ? |
|-------|-----------------|:----:|:-------------:|:----:|
| Bolt.new | $40M ARR, $700M | Oui (1M tokens/mo) | ~28 min | — |
| Lovable | $200M+ ARR, $6,6 Mds | 5 crédits/j | ~35 min | 🇸🇪 Stockholm |
| Replit | $253M ARR, $3 Mds | Oui (limité) | ~45 min | — |
| Cursor | **$1 Mds ARR**, $29,3 Mds | Oui (limité) | Variable | — |

- Cursor : le SaaS le plus rapide de l'histoire à atteindre **$1 Mds ARR** [1]
- Lovable : startup européenne la plus rapide à **$100M ARR** [2]
- Bolt.new : **2ᵉ produit** à la croissance la plus rapide après ChatGPT [3]

<small>Sources : [1] [CNBC](https://www.cnbc.com/) · [2] [TechCrunch](https://techcrunch.com/) · [3] [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: cols -->

# 12 — Spotlight : Bolt.new

<div class="left">

- **$0 → $40M ARR** en 5 mois [1]
- Valorisation **$700M** (jan 2025) [1]
- **5M** inscrits, **1M+ sites** Netlify [2]
- Free : 1M tokens/mo, Pro : $20/mo

</div>
<div class="right">

- Prompt → **app full-stack** en ~28 min [3]
- WebContainers : Node.js dans le browser
- bolt.diy : fork open-source (MIT) [3]
- Zero install, zero config, zero coût initial
- Leçon : **le prototypage à coût quasi-nul**

</div>

<small>Sources : [1] [Bloomberg](https://www.bloomberg.com/) · [2] [Netlify](https://www.netlify.com/) · [3] [GitHub](https://github.com/stackblitz/bolt.new)</small>

---

<!-- _class: section -->

# Rechercher & analyser

## Transformer l'information en avantage concurrentiel

---

# 13 — Les outils de recherche IA

| Outil | Créateur | Free tier | Différenciateur | Best for |
|-------|----------|:---------:|-----------------|----------|
| NotebookLM | Google | **100% gratuit** | AI Podcasts, source-grounded | Synthèse de docs |
| Perplexity | Perplexity AI | Illimité (basic) | Citations vérifiées, $20 Mds val. | Veille & recherche |
| Julius AI | Julius (YC W22) | 15 msg/mo | Data viz, 40+ graphiques | Analyse de données |

- NotebookLM : **48M** visites/mois, croissance 56% en 6 mois [1]
- Perplexity : **$148M ARR** (2025), projeté **$656M** en 2026 [2]
- Julius : **2M+** utilisateurs, utilisé à Harvard Business School [3]

<small>Sources : [1] [Google](https://blog.google/technology/ai/notebooklm/) · [2] [TechCrunch](https://techcrunch.com/) · [3] [Julius AI](https://julius.ai/)</small>

---

<!-- _class: cols -->

# 14 — Spotlight : NotebookLM

<div class="left">

- Propulsé par **Gemini 2.5** [1]
- **500K mots** par source, 50 sources [1]
- Audio Overviews = **podcasts IA** [1]
- **48M** visites/mois, synthèse multi-sources [2]

</div>
<div class="right">

- **100% gratuit** (Google) [1]
- Upload cours → guide d'étude + podcast
- Source-grounded = **pas d'hallucination**
- 14% du marché outils IA éducatifs [2]
- Leçon : **le meilleur outil de recherche gratuit**

</div>

<small>Sources : [1] [Google](https://notebooklm.google/) · [2] [SimilarWeb](https://www.similarweb.com/)</small>

---

<!-- _class: section -->

# Le stack souverain & open-source

## Garder le contrôle de ses données

---

# 15 — Self-hosted : la souveraineté des données

| Outil | Stars GitHub | Licence | Self-hosted | Données |
|-------|:-----------:|---------|:-----------:|---------|
| Ollama | **162K** | MIT | Oui | 100% local |
| Open WebUI | **123K** | MIT | Oui | 100% local |
| Dify | **100K** | Custom OSS | Oui | Vos serveurs |
| n8n | **100K** | Fair-code | Oui | Vos serveurs |
| Flowise | **47K** | Apache 2.0 | Oui | Vos serveurs |

Pourquoi self-hoster :
- **RGPD** : aucune donnée ne quitte votre infrastructure
- **EU AI Act** : conformité par design, audit possible
- **Coût** : zéro frais cloud après l'investissement initial

<small>Sources : [GitHub](https://github.com/) · [EU AI Act](https://artificialintelligenceact.eu/)</small>

---

# 16 — Hugging Face & l'écosystème français

- **Hugging Face** 🇫🇷 : Paris, **$4,5 Mds** de valorisation, **1M+ modèles**, 400K datasets [1]
- **Mistral AI** 🇫🇷 : Paris, **€11,7 Mds** de valorisation, seul frontier UE [2]
- **n8n** 🇩🇪 : Berlin, **$2,5 Mds**, 100K+ stars, automatisation souveraine [3]
- **Make** 🇨🇿 : Prague, 250K+ clients, acquis par Celonis [4]
- **Lovable** 🇸🇪 : Stockholm, **$6,6 Mds**, vibe coding européen [5]

> L'écosystème IA open-source européen est **unique au monde** : les 2 plus grandes plateformes open-source (HF + Mistral) sont françaises. Un atout pour les entrepreneurs qui veulent allier innovation et souveraineté.

<small>Sources : [1] [Hugging Face](https://huggingface.co/) · [2] [Mistral AI](https://mistral.ai/) · [3] [n8n](https://n8n.io/) · [4] [Make](https://www.make.com/) · [5] [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: section -->

# Synthèse

## Choisir, combiner, agir

---

# 17 — Grille de décision : quel outil pour quel besoin

| Besoin | Outil recommandé | Free | 1er résultat | Niveau |
|--------|-----------------|:----:|:------------:|--------|
| Chatbot client | Mistral / Dify | Oui | 1h | Débutant |
| Automatisation | n8n / Make | Oui | 2h | Débutant |
| Slides & pitch | Gamma / Canva | Oui | 10 min | Débutant |
| Prototype web | Bolt.new / Lovable | Oui | 30 min | Débutant |
| Recherche | NotebookLM / Perplexity | Oui | 5 min | Débutant |
| Self-hosted | Ollama + Open WebUI | Oui | 30 min | Intermédiaire |

> Tous ces outils ont un **free tier suffisant pour démarrer**. Le budget n'est plus une excuse.

---

# 18 — Discussion : Composez votre toolbox entrepreneur IA

> Vous avez une **idée de startup**, un après-midi de 3h, et **$0 de budget**. Composez votre toolbox :

| Étape | Options | Votre choix ? |
|-------|---------|:-------------:|
| Recherche marché | Perplexity / NotebookLM | ? |
| Prototype | Bolt.new / Lovable / Replit | ? |
| Pitch deck | Gamma / Canva | ? |
| Chatbot | Mistral / GPT Builder / Dify | ? |
| Automatisation | n8n / Make / Zapier | ? |

**Questions pour la classe** :
- Quels critères guident votre choix ? (UE, open-source, facilité, écosystème)
- Un concurrent vous copie en 48h avec les mêmes outils — quel est votre **vrai moat** ?

---

# 19 — Les 5 tendances à retenir

1. **Le Vibe Coding démocratise la création logicielle** — 58% des utilisateurs Replit ne codent pas, Bolt.new de $0 à $40M ARR en 5 mois

2. **L'open-source domine** — Ollama 162K stars, Open WebUI 123K, Dify 100K, n8n 100K : les outils souverains sont aussi les plus populaires

3. **Le gratuit suffit pour démarrer** — chaque catégorie a un free tier viable : NotebookLM, Gamma, Bolt.new, n8n self-hosted, Mistral Le Chat

4. **L'UE a des champions** — Mistral 🇫🇷, Hugging Face 🇫🇷, n8n 🇩🇪, Lovable 🇸🇪, Make 🇨🇿 : un écosystème européen compétitif

5. **La stack IA = le nouveau stack startup** — recherche + prototype + pitch + chatbot + automatisation, le tout en une après-midi

<small>Sources : [Replit](https://blog.replit.com/) · [GitHub](https://github.com/) · [Bloomberg](https://www.bloomberg.com/)</small>

---

# 20 — Key Takeaways

1. **Les outils sont gratuits et accessibles** — chaque famille (chatbot, automatisation, contenu, code, recherche) a un free tier suffisant pour valider une idée

2. **Le Vibe Coding change qui peut construire** — décrire en français → obtenir un prototype en 30 minutes. La compétence clé est le prompting, pas le code

3. **L'Europe a des cartes à jouer** — Mistral (souveraineté), Hugging Face (open-source), n8n (automatisation), Lovable (vibe coding) : des alternatives UE crédibles

4. **Combinez les outils en workflows** — Perplexity → Gamma → Bolt.new → n8n : la valeur est dans la combinaison, pas dans l'outil isolé

5. **Commencez aujourd'hui** — le coût d'un prototype est passé de $50K et 3 mois à $0 et 3 heures. Le bottleneck est l'idée, plus la technique
