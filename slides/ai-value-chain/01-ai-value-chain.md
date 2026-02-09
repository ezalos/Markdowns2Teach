---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche AI Value Chain 2024–2026 · Données publiques"
---

<!-- ABOUTME: Vue d'ensemble de la value chain de l'IA — 50 entreprises, 9 couches, de l'énergie aux applications. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : qui capture la valeur, quels sont les moats, où sont les opportunités startup. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# La AI Value Chain

## Qui crée de la valeur dans l'IA ?

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Pourquoi cartographier la value chain ?

L'IA n'est pas un produit unique — c'est un **stack de dépendances** :

- Chaque couche dépend de celles du dessous (pas de ChatGPT sans GPU, pas de GPU sans lithographie)
- Les **marges** et les **moats** varient radicalement d'une couche à l'autre
- Comprendre le stack = comprendre **où entreprendre**

> Cette cartographie couvre **50 entreprises** à travers **9 couches**, de l'énergie aux applications utilisateur.

*Pour chaque couche, on se posera trois questions* :
1. Qui capture la valeur ?
2. Quels sont les moats ?
3. Où est l'opportunité startup ?

---

# 02 — Vue d'ensemble : les 9 couches

| # | Couche | Rôle | Exemples clés |
|---|--------|------|---------------|
| 0 | Energy | Alimentation des data centers | Crusoe Energy, CFS |
| 1 | Hardware | GPUs, puces, mémoire | NVIDIA, TSMC, ASML |
| 2 | Cloud Infrastructure | Location de compute GPU | AWS, Azure, OVHcloud |
| 3 | Data Infrastructure | Labeling, data platforms | Scale AI, Databricks |
| 4 | Foundation Models | Entraînement des LLMs | OpenAI, Mistral AI |
| 5 | Model Hubs | Distribution de modèles | Hugging Face, Ollama |
| 6 | APIs & Orchestration | Routing, Vector DBs | OpenRouter, Pinecone |
| 7 | Évaluation & Safety | Benchmarks, compliance | LMSYS, Giskard |
| 8 | Applications | Produits AI-natives | Cursor, Perplexity |

> Chaque couche vers le bas = plus de capital requis, plus de concentration. Chaque couche vers le haut = plus de différenciation possible.

---

<!-- _class: section -->

# Les fondations

## Energy, Hardware, Cloud

---

# 03 — Energy & Hardware — les bottlenecks physiques

| Entreprise | Pays | Revenu [1] | Rôle |
|------------|------|--------|------|
| ASML | 🇳🇱 Pays-Bas | €28,3 Mds | Monopole sur les machines EUV de lithographie |
| TSMC | 🇹🇼 Taïwan | $122,9 Mds | Fonderie : fabrique les puces NVIDIA, Apple, AMD |
| NVIDIA | 🇺🇸 USA | $130,5 Mds | GPUs dominants (H100, Blackwell), écosystème CUDA |
| Samsung / SK Hynix | 🇰🇷 Corée | $300 Mds (combiné) | Mémoire HBM — composant critique des GPUs IA |
| Cerebras | 🇺🇸 USA | $136 M (H1 2024) | Puces wafer-scale, alternative à NVIDIA [2] |
| Crusoe Energy | 🇺🇸 USA | ~$276 M | Data centers alimentés par énergie stranded [2] |

> **Bottleneck clé** : ASML est le *seul* fabricant de machines EUV. Si ASML s'arrête, toute la production de puces avancées s'arrête.

<small>Sources : [1] Rapports annuels 2024 ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/), [ASML](https://www.asml.com/en/news/press-releases/2025/q4-2024-financial-results), [TSMC](https://investor.tsmc.com/english/quarterly-results/2024/q4)) · [2] [Crunchbase](https://www.crunchbase.com/)</small>

---

<!-- _class: cols -->

# 04 — Spotlight : NVIDIA

<div class="left">

- **$130,5 Mds** de CA (FY2025, +114% YoY) [1]
- **~$4 500 Mds** de market cap — #1 mondial [1]
- **88%** du CA = Data Center (GPUs IA) [1]
- GPUs : H100, Blackwell B200, GB200 · DGX Cloud ~$37K/mois

</div>
<div class="right">

- **CUDA** : 18 ans d'écosystème, **98%** des devs IA l'utilisent
- Migration vers AMD = réécrire tout le stack logiciel
- Le compute est le **1er poste de coût** d'une startup IA
- >$500 Mds de commandes confirmées → pas de pénurie en vue

</div>

<small>Sources : [1] [NVIDIA IR FY2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/)</small>

---

# 05 — Cloud Infrastructure

| Entreprise | Pays | Revenu [1] | Rôle |
|------------|------|--------|------|
| AWS (Amazon) | 🇺🇸 USA | $128,7 Mds | #1 cloud, Bedrock (accès multi-modèles) |
| Microsoft Azure | 🇺🇸 USA | ~$75 Mds | #2 cloud, partenaire exclusif OpenAI |
| Google Cloud | 🇺🇸 USA | ~$58,8 Mds | #3 cloud, TPUs, intégration Gemini |
| CoreWeave | 🇺🇸 USA | $1,92 Mds | Cloud GPU spécialisé (+740% YoY) [2] |
| OVHcloud | 🇫🇷 France | €1,085 Mds | Cloud souverain européen, GPU instances |
| Scaleway (Iliad) | 🇫🇷 France | Filiale d'Iliad | Cloud européen, partenariat Mistral AI |

> **Les 3 hyperscalers US** (AWS, Azure, GCP) captent ~65% du marché cloud mondial. OVHcloud et Scaleway sont les alternatives souveraines européennes.

<small>Sources : [1] Résultats annuels 2024-2025 · [2] [CoreWeave IPO](https://investors.coreweave.com/)</small>

---

# 06 — Discussion : Souveraineté du compute

> Vous développez une application IA pour un **hôpital français**. Les données patients sont soumises au **RGPD** et au **Health Data Hub**. Votre modèle tourne actuellement sur AWS.

**Questions pour la classe** :

- Quels sont les risques juridiques d'héberger des données de santé sur un cloud US ?
- Quelles alternatives européennes existent ? À quel surcoût ?
- Le **Cloud Act** américain permet-il aux autorités US d'accéder à vos données ?
- Souveraineté = toujours plus cher. Quand le surcoût est-il justifié ?

---

<!-- _class: section -->

# Données et modèles

## Data Infrastructure & Foundation Models

---

# 07 — Data Infrastructure — le carburant de l'IA

Les modèles sont aussi bons que leurs données. Cette couche fournit le labeling, le stockage et les pipelines.

| Entreprise | Pays | Revenu / Valorisation [1] | Rôle |
|------------|------|----------------------|------|
| Scale AI | 🇺🇸 USA | $870 M CA / $29 Mds | Data labeling, RLHF pour modèles frontier |
| Databricks | 🇺🇸 USA | $4,8 Mds ARR / $134 Mds | Plateforme unifiée data + AI, Lakehouse |
| Snowflake | 🇺🇸 USA | $3,63 Mds / $54-68 Mds | Data warehouse cloud, Cortex AI |

> **Aucun acteur européen majeur** dans cette couche. Opportunité ou gap structurel ?

- Meta a investi $14,3 Mds pour 49% de Scale AI — preuve que la data est stratégique [2]

<small>Sources : [1] [Databricks](https://www.databricks.com/company/newsroom/press-releases/databricks-surpasses-4-8b-revenue-run-rate-growing-55-year-over-year) · [TechCrunch](https://techcrunch.com/) · [2] [Bloomberg](https://www.bloomberg.com/)</small>

---

# 08 — Foundation Models — la course (1/2)

| Entreprise | Pays | ARR / Valorisation [1] | Modèles phares |
|------------|------|--------------------|----------------|
| OpenAI | 🇺🇸 USA | ~$20 Mds / $500-830 Mds | GPT-4o, o3, ChatGPT (400M WAU) |
| Anthropic | 🇺🇸 USA | $9 Mds / $350 Mds | Claude (Opus, Sonnet, Haiku) |
| Google DeepMind | 🇬🇧🇺🇸 | Parent: $402,8 Mds CA | Gemini (750M MAU), AlphaFold |
| Meta AI | 🇺🇸 USA | Parent: $201 Mds CA | Llama (open-weight, le plus déployé) |
| Mistral AI | 🇫🇷 France | 300M€ ARR / ~$14 Mds | Mistral Large 3, Le Chat, Ministral [2] |

> Les 5 plus gros model creators ont levé collectivement **>$100 Mds**. La barrière à l'entrée est monumentale.

<small>Sources : [1] [Sherwood News](https://sherwood.news/business/openais-arr-reached-over-usd20-billion-in-2025-cfo-says/) · [Bloomberg](https://www.bloomberg.com/) · [2] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai)</small>

---

# 09 — Foundation Models — challengers (2/2)

| Entreprise | Pays | ARR / Valorisation [1] | Modèles phares |
|------------|------|--------------------|----------------|
| DeepSeek | 🇨🇳 Chine | ~$220 M / autofinancé | V3, R1 (MIT, open-source complet) |
| xAI (Grok) | 🇺🇸 USA | ~$300 M / $250 Mds | Grok, Colossus (100K+ H100s) |
| Alibaba / Qwen | 🇨🇳 Chine | Cloud: ~$22 Mds/an | Qwen (Apache 2.0, open-weight) |
| Cohere | 🇨🇦 Canada | $150 M ARR / $7 Mds | Enterprise LLMs, on-prem, multilingue |
| Poolside AI | 🇺🇸 (Paris) | $50 M / $3-12 Mds | Malibu, Point (code-specialized) |

> **DeepSeek** a démontré qu'on peut atteindre le niveau frontier avec une fraction du budget — mais la question de la dépendance à la Chine reste posée.

<small>Sources : [1] [DeepSeek](https://api-docs.deepseek.com/news/news250120) · [Bloomberg](https://www.bloomberg.com/) · [Crunchbase](https://www.crunchbase.com/)</small>

---

<!-- _class: cols -->

# 10 — Spotlight : OpenAI

<div class="left">

- **400M+** utilisateurs actifs par semaine [1]
- **~$20 Mds** ARR (triplé en 1 an) [1]
- **$40 Mds** levés en Series F (SoftBank) [2]
- ChatGPT Plus ($20/mois), Pro ($200/mois), API
- **$14 Mds** de pertes projetées en 2026 [2]

</div>
<div class="right">

- Lance des apps → **concurrence ses propres clients API**
- Baisses de prix agressives (o3 : -80%) → compression des marges
- Diversifiez vos providers (OpenAI + Mistral + open-source)
- Le risque : OpenAI lance votre produit en feature gratuite

</div>

<small>Sources : [1] [Sherwood News](https://sherwood.news/business/openais-arr-reached-over-usd20-billion-in-2025-cfo-says/) · [2] [CNBC](https://www.cnbc.com/)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Mistral AI

<div class="left">

- **Paris**, fondée en **2023** — 2 ans seulement
- **300M€ ARR** (Sep 2025, 25x YoY), objectif >1 Md€ en 2026 [1]
- **~$14 Mds** val., **~$3 Mds** levés (dont 1,3 Md€ d'ASML) [1]
- API (Large 3, Medium 3), Le Chat, Ministral (edge, Apache 2.0)

</div>
<div class="right">

- **Seul** fournisseur frontier avec hébergement natif UE
- Contrat armée française, ASML investisseur, consortium ArGiMi
- Medium 3 : **$0,40/$2** vs. GPT-4o **$2,50/$10** → **6x moins cher**
- On-premises pour RGPD strict → moat souveraineté [2]

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [2] [CNBC](https://www.cnbc.com/)</small>

---

# 12 — Discussion : Open-weight vs. Closed

> Vous construisez une **startup legaltech** qui analyse des contrats. Trois options s'offrent à vous :

| Option | Modèle | Licence | Hébergement | Risque |
|--------|--------|---------|-------------|--------|
| A | API OpenAI (GPT-4o) | Closed | Cloud US | Vendor lock-in, Cloud Act |
| B | Mistral Large 3 (self-hosted) | Apache 2.0 | Serveur UE | Coût infra, maintenance |
| C | DeepSeek R1 (self-hosted) | MIT | Serveur UE | Open-source chinois, perception clients |

**Questions pour la classe** :
- Quel critère pèse le plus : coût, performance, ou confiance client ?
- Vos clients (cabinets d'avocats) accepteront-ils que leurs contrats transitent par un cloud US ?

---

<!-- _class: section -->

# Distribution, tooling, évaluation

## Model Hubs, APIs, Safety

---

# 13 — Model Hubs — où trouver des modèles

| Entreprise | Pays | Métrique clé [1] | Rôle |
|------------|------|-------------|------|
| Hugging Face | 🇺🇸🇫🇷 | 2M+ modèles, $4,5 Mds val. | Hub open-source, Transformers library |
| CivitAI | 🇺🇸 USA | 3M+ utilisateurs | Hub communautaire pour image gen |
| Ollama | 🇺🇸 USA | Open-source (MIT) | LLMs en local sur laptop |
| Replicate | 🇺🇸 USA | Acquis par Cloudflare | Déploiement cloud de modèles |

> Les Model Hubs sont les **App Stores de l'IA** : celui qui contrôle la distribution contrôle l'écosystème.

<small>Sources : [1] [Crunchbase](https://www.crunchbase.com/) · Sites officiels</small>

---

<!-- _class: cols -->

# 14 — Spotlight : Hugging Face

<div class="left">

- **Fondé à Paris** (2016), HQ New York, **$4,5 Mds** val. [1]
- **~$130 M** CA (2024), **50 000+** clients payants [1]
- Hub : **2M+** modèles, **500K+** datasets, **1M+** Spaces
- Investisseurs : Google, Amazon, NVIDIA, Salesforce

</div>
<div class="right">

- **Network effects** : plus de modèles → plus de devs → plus de modèles
- **Transformers** = bibliothèque standard de l'IA (121K stars GitHub)
- Position de "Suisse" : Google, Meta, Microsoft y publient tous
- Fine-tune en heures, Spaces = démos gratuites pour startups

</div>

<small>Sources : [1] [Sacra](https://sacra.com/c/hugging-face/) · [Hugging Face](https://huggingface.co/)</small>

---

# 15 — API Providers, Orchestration, Vector DBs

| Entreprise | Pays | Métrique clé [1] | Rôle |
|------------|------|-------------|------|
| OpenRouter | 🇺🇸 USA | $500 M val. | API unifiée pour 200+ modèles |
| Together AI | 🇺🇸 USA | ~$300 M CA, $3,3 Mds val. | Inference open-source rapide |
| Fireworks AI | 🇺🇸 USA | $130 M ARR, $4 Mds val. | API low-latency, compound AI |
| AWS Bedrock | 🇺🇸 USA | Partie d'AWS | Accès managé multi-modèles |
| LangChain | 🇺🇸 USA | $1,25 Mds val. | Framework d'orchestration LLM |
| Pinecone | 🇺🇸 USA | $26,6 M CA | Vector DB managée (RAG) |
| Weaviate | 🇳🇱 Pays-Bas | $12,3 M CA, $200 M val. | Vector DB open-source |

> **Weaviate** (Amsterdam) est le seul acteur européen de cette couche. Les Vector DBs sont les "mémoires" du RAG.

<small>Sources : [1] [Crunchbase](https://www.crunchbase.com/) · [TechCrunch](https://techcrunch.com/)</small>

---

# 16 — Évaluation, Safety & MLOps

| Entreprise | Pays | Métrique clé [1] | Rôle |
|------------|------|-------------|------|
| LMSYS Arena | 🇺🇸 USA | $1,7 Mds val. | Chatbot Arena — benchmark crowdsourcé |
| Artificial Analysis | 🇺🇸🇦🇺 | Leaderboards gratuits | Benchmarks qualité / vitesse / prix |
| Giskard | 🇫🇷 France | Clients : AXA, BNP, Michelin | Red teaming LLM, compliance EU AI Act |
| Weights & Biases | 🇺🇸 USA | Acquis ~$1,7 Mds | ML experiment tracking, registre modèles |

> La **couche safety** est la plus jeune et la plus sous-financée — mais l'EU AI Act va créer une demande massive dès août 2025.

<small>Sources : [1] [Crunchbase](https://www.crunchbase.com/) · Sites officiels</small>

---

<!-- _class: cols -->

# 17 — Spotlight : Giskard

<div class="left">

- **Paris**, fondée en **2021**, **~15 personnes** [1]
- Clients : **AXA, BNP Paribas, Michelin, Google DeepMind**
- ~€7,5 M levés (Elaia, Bessemer, EIC, Bpifrance) [1]
- Giskard Hub (red teaming), open-source (Apache 2.0), GOAT (88% sur GPT-4)

</div>
<div class="right">

- Participe à la **rédaction des standards EU AI Act** (CEN-CENELEC)
- Consortium **ArGiMi** avec Mistral AI et Artefact (France 2030)
- **La compliance n'est pas un coût, c'est un marché**
- 15 personnes servent des Fortune 500 → niche + expertise = levier

</div>

<small>Sources : [1] [TechCrunch](https://techcrunch.com/2023/11/14/giskards-open-source-framework-evaluates-ai-models-before-theyre-pushed-into-production/) · [Giskard](https://www.giskard.ai/)</small>

---

# 18 — Discussion : Où se positionner ?

> Vous avez **500K€**, une **équipe de 4** personnes techniques, et 18 mois de runway. À quelle couche de la value chain attaquez-vous ?

| Couche | Capital requis | Concurrence | Opportunité |
|--------|---------------|-------------|-------------|
| Hardware | >$1 Mds | Extrême | Quasi impossible |
| Foundation Models | >$100 M | Très forte | Niche (code, médical) |
| Model Hubs / APIs | $1-10 M | Forte | Orchestration, vertical |
| Safety / Évaluation | $500K-5 M | Modérée | EU AI Act, compliance |
| Applications | $200K-5 M | Variable | Vertical + workflow |

**Questions pour la classe** :
- Quelle couche offre le meilleur ratio impact/capital ?
- La couche safety est-elle viable avec 4 personnes ? (Giskard l'a fait)

---

<!-- _class: section -->

# Applications AI-natives

## Where Value Meets the User

---

# 19 — Applications AI-natives

| Entreprise | Pays | ARR / Valorisation [1] | Produit |
|------------|------|--------------------|---------|
| Cursor | 🇺🇸 USA | $1 Mds+ / $29,3 Mds | Éditeur de code IA (+9 900% YoY) |
| GitHub Copilot | 🇺🇸 USA | $2 Mds / Microsoft | Pair-programming IA (77M+ devs) |
| Perplexity | 🇺🇸 USA | ~$200 M / $20 Mds | Moteur de recherche IA |
| Harvey | 🇺🇸 USA | $195 M / $8 Mds | IA pour juristes (contrats, recherche) |
| ElevenLabs | 🇬🇧 UK | $330 M+ / $11 Mds | Synthèse vocale (41% du Fortune 500) |

> La couche application est celle où **la valeur rencontre l'utilisateur** — et où le pricing power est le plus fort.

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [ElevenLabs](https://elevenlabs.io/blog/series-d) · [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: cols -->

# 20 — Spotlight : Cursor

<div class="left">

- **$0 → $1 Mds ARR** en 24 mois (+9 900% YoY) [1]
- **$29,3 Mds** val., **1M+** DAU, **50%+** Fortune 500 [1]
- 4 fondateurs MIT, 150-300 pers., $0 marketing — 100% PLG
- Fork VS Code → **0 coût de migration** pour 14M+ devs

</div>
<div class="right">

- N'a **pas de modèle propre** (utilise Claude, GPT, etc.)
- Data flywheel : 1M+ devs → patterns d'édition → meilleur produit
- GitHub Copilot a **20M+** utilisateurs, Windsurf à **$15/mois**
- Si OpenAI ou Anthropic lancent un IDE... que reste-t-il ?

</div>

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [Cursor](https://cursor.com/blog/series-d)</small>

---

# 21 — Discussion : Le risque de plateforme

> **Scénario** : OpenAI annonce "ChatGPT Code Editor" — un IDE gratuit intégré à ChatGPT, avec accès direct à GPT-5. C'est le cauchemar de Cursor.

**Questions pour la classe** :

- Comment Cursor peut-il se défendre ? (indices : data flywheel, intégration multi-modèles, vitesse)
- Ce scénario est-il un risque ou une opportunité pour d'autres startups ?
- **Règle générale** : si votre produit peut devenir une feature gratuite de votre fournisseur, votre moat est trop mince
- Quels exemples historiques connaissez-vous ? (Zoom vs. Teams, Slack vs. Teams...)

---

<!-- _class: section -->

# Synthèse

## What Does This Mean for You?

---

# 22 — Où se concentre la valeur ?

**En bas du stack** (Hardware, Cloud) :
- Marges élevées, capital massif, forte concentration
- NVIDIA : **56% de marge nette**, quasi-monopole [1]
- Inaccessible aux startups (sauf niche : Cerebras, Crusoe)

**Au milieu** (APIs, Orchestration, Safety) :
- Le modèle "picks & shovels" — vendre les outils pendant la ruée vers l'or
- Marges plus faibles, mais capital requis raisonnable
- Ex : Giskard avec **€7,5M** sert AXA et BNP [2]

**En haut** (Applications) :
- Pricing power fort ($20-200/mois/user), mais risque de plateforme
- **Le sweet spot pour les entrepreneurs** si le moat est clair

<small>Sources : [1] [NVIDIA IR](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/) · [2] [Giskard](https://www.giskard.ai/)</small>

---

<!-- _class: cols -->

# 23 — L'écosystème européen : forces et faiblesses

<div class="left">

**Forces** — ASML (monopole EUV), Mistral AI (frontier, Apache 2.0), Hugging Face (hub dominant), OVHcloud/Scaleway (cloud souverain), Giskard (EU AI Act), ElevenLabs ($11 Mds) [1]

</div>
<div class="right">

**Faiblesses** — Aucun NVIDIA européen, financement **10-50x inférieur** (Mistral ~$3 Mds vs. OpenAI ~$58 Mds), pas de hyperscaler top 3, fuite des talents (salaires 2-3x), marché fragmenté (27 régulateurs) [2]

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 24 — Open vs. Closed — le spectre stratégique

| Licence | Exemples | Self-host ? | Modifiable ? | Risque vendor |
|---------|----------|------------|-------------|---------------|
| **MIT** | DeepSeek R1 | ✅ | ✅ | Aucun |
| **Apache 2.0** | Mistral, Llama, Qwen | ✅ | ✅ | Aucun |
| **Open-core** | Hugging Face, Giskard | Partiel | Partiel | Faible |
| **API ouverte** | OpenAI, Anthropic | ❌ | ❌ | Élevé |
| **Closed** | Google (certains), xAI | ❌ | ❌ | Maximum |

> **Le choix open/closed est une décision stratégique**, pas technique. Il affecte votre coût, votre indépendance, et la confiance de vos clients.

- Pour un MVP : API (vitesse) → puis migration vers open-weight si traction
- Pour des données sensibles : self-hosting (Mistral Apache 2.0 ou Llama)
- Pour la compliance EU : hébergement UE obligatoire pour certains secteurs

---

# 25 — Key Takeaways

1. **La value chain = des dépendances** — votre startup IA dépend de toutes les couches en dessous. Cartographiez vos risques fournisseurs.

2. **Le compute est le bottleneck** — NVIDIA a un quasi-monopole, et le coût GPU est souvent votre premier poste. Négociez ou optimisez.

3. **Open vs. Closed est stratégique** — Apache 2.0 (Mistral, Llama) offre indépendance et meilleur unit economics. L'API est pratique mais crée du vendor lock-in.

4. **L'Europe a de vrais champions** — ASML, Mistral, Hugging Face, Giskard, ElevenLabs. Le gap est dans le financement et le compute, pas dans le talent.

5. **La régulation crée des marchés** — l'EU AI Act n'est pas qu'une contrainte : c'est une opportunité pour ceux qui vendent la compliance (Giskard, Mistral on-prem).

> **Prochaine étape** : choisissez une couche, identifiez un problème non résolu, et construisez.
