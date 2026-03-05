---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 4 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche AI Value Chain & Market Intelligence 2024–2025 · Données publiques"
---

<!-- ABOUTME: Écosystème IA — value chain 9 couches, acteurs clés, taille du marché, investissements et positionnement UE. -->
<!-- ABOUTME: Première moitié de la Session 4, cadré business pour entrepreneurs M2. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# L'écosystème IA

## 9 couches, 50 entreprises — qui capture la valeur ?

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Le marché IA en 2025

## Taille, vitesse, investissements

---

# 01 — L'IA en chiffres : un marché à $2 500+ Mds

| Métrique | Valeur | Source |
|----------|--------|--------|
| Marché mondial IA 2025 | **$1 757 Mds** | Gartner |
| Projection 2026 | **$2 527 Mds** (+44% YoY) | Gartner |
| Investissement corporate 2024 | **$252 Mds** | Stanford HAI |
| Part de l'IA dans le VC mondial | **~50%** | PitchBook |
| Adoption en entreprise | 55% → **88%** (en 2 ans) | McKinsey |
| Licornes IA | **498** ($2 700 Mds cumulés) | CB Insights |

> L'IA capte **1 dollar de VC sur 2** dans le monde. C'est le marché le plus dynamique de la décennie.

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [4] [CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/)</small>

---

<!-- _class: compact -->

# 02 — La course aux data centers : $650+ Mds de capex

Les hyperscalers investissent massivement dans l'infra IA :

| Entreprise | Capex 2026 [1] | Croissance |
|------------|---------------|------------|
| Amazon | ~$200 Mds | Agressif |
| Google | $175-185 Mds | +40% YoY |
| Microsoft | ~$145 Mds | +57% YoY |
| Meta | $115-135 Mds | +64% YoY |

- **Cumulé 2025-2027** : $1 150 Mds (Goldman Sachs) [2]
- Amazon prévoit un **FCF négatif de -$17 Mds** en 2026 [1]

> Pari existentiel : ces entreprises brûlent du cash à un rythme historique.

<small>Sources : [1] [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html) · [2] Goldman Sachs Research</small>

---

<!-- _class: cols -->

# 03 — Bulle ou boom ? Les signaux contradictoires

<div class="left">

**Signaux haussiers**

- Marché **$2 527 Mds** en 2026 [1]
- **88%** d'adoption en entreprise [2]
- Coûts d'inférence **÷280** en 2 ans [3]
- **498 licornes** IA dans le monde [4]

</div>
<div class="right">

**Signaux baissiers**

- **95%** des pilotes IA = zéro ROI [5]
- Hyperscalers FCF en négatif [6]
- **$1 500 Mds** de nouvelle dette [7]
- S&P top 10 = **40,7%** (record) [7]

</div>

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026) · [2] [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [3] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [4] [CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/) · [5] MIT NANDA · [6] [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html) · [7] Goldman Sachs</small>

---

<!-- _class: section -->

# La AI Value Chain

## 9 couches, de l'énergie aux applications

---

<!-- _class: compact -->

# 04 — Vue d'ensemble : les 9 couches du stack IA

![bg right:40% contain](assets/infographics/ai-stack-9_run_20260216_171301_8858a8.png)

**9 couches** structurent l'écosystème :

- **0-1 Energy & Hardware** — NVIDIA, TSMC, ASML
- **2-3 Cloud & Data** — AWS, Azure, Scale AI
- **4-5 Models & Hubs** — OpenAI, Mistral, HF
- **6-7 APIs & Safety** — OpenRouter, Pinecone
- **8 Applications** — Cursor, Perplexity

> Bas = plus de **capital** et concentration. Haut = plus de **différenciation**.

---

# 05 — Energy & Hardware — les bottlenecks physiques

| Entreprise | Pays | Revenu [1] | Rôle |
|------------|------|--------|------|
| ASML | Pays-Bas | €28,3 Mds | Monopole sur les machines EUV |
| TSMC | Taïwan | $122,9 Mds | Fonderie : fabrique les puces NVIDIA, Apple |
| NVIDIA | USA | $130,5 Mds | GPUs dominants (H100, Blackwell), CUDA |
| Samsung / SK Hynix | Corée | $300 Mds (combiné) | Mémoire HBM critique |

> **Bottleneck clé** : ASML est le *seul* fabricant de machines EUV. Si ASML s'arrête, toute la production de puces avancées s'arrête.

<small>Sources : [1] Rapports annuels 2024 ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/), [ASML](https://www.asml.com/en/news/press-releases/2025/q4-2024-financial-results), [TSMC](https://investor.tsmc.com/english/quarterly-results/2024/q4))</small>

---

<!-- _class: cols -->

# 06 — Spotlight : NVIDIA — le roi du stack

<div class="left">

- **$130,5 Mds** de CA (FY2025, +114% YoY) [1]
- **~$4 500 Mds** de market cap — #1 mondial [1]
- **88%** du CA = Data Center (GPUs IA) [1]
- GPUs : H100, Blackwell B200, GB200

</div>
<div class="right">

- **CUDA** : 18 ans d'écosystème, **98%** du marché GPU IA [2]
- Migration vers AMD = réécrire tout le stack
- Le compute = **1er poste de coût** d'une startup IA
- **56%** de marge nette — quasi-monopole [1]

</div>

<small>Sources : [1] [NVIDIA IR FY2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/) · [2] [TechInsights via Tom's Hardware](https://www.tomshardware.com/tech-industry/nvidia-shipped-376m-data-center-gpus-in-2023-dominates-business-with-98-revenue-share)</small>

---

# 07 — Cloud Infrastructure — les 3 géants et les alternatives

| Entreprise | Pays | Revenu [1] | Rôle |
|------------|------|--------|------|
| AWS (Amazon) | USA | $128,7 Mds | #1 cloud, Bedrock (multi-modèles) |
| Microsoft Azure | USA | ~$75 Mds | #2 cloud, partenaire OpenAI |
| Google Cloud | USA | ~$58,8 Mds | #3 cloud, TPUs, Gemini |
| OVHcloud | France | €1,085 Mds | Cloud souverain européen |
| Scaleway (Iliad) | France | Filiale d'Iliad | Cloud européen, partenariat Mistral |

> Les 3 hyperscalers US captent **~65%** du marché cloud mondial [2]. OVHcloud et Scaleway sont les alternatives souveraines.

<small>Sources : [1] Résultats annuels 2024-2025 ([AWS](https://ir.aboutamazon.com/), [Microsoft](https://www.microsoft.com/en-us/Investor/), [Google](https://abc.xyz/investor/)) · [2] [Canalys Q1 2025](https://canalys.com/newsroom/global-cloud-q1-2025)</small>

---

<!-- _class: section -->

# Foundation Models & Distribution

## Qui entraîne les modèles, qui les distribue

---

# 08 — Foundation Models — la course au revenu

| Lab | ARR fin 2025 [1] | Croissance YoY | Note |
|-----|-----------|----------------|------|
| OpenAI | ~$20 Mds | +233% | 400M+ WAU, pertes prévues $14 Mds |
| Anthropic | ~$9 Mds | +800% | 40% du spend enterprise LLM [2] |
| Google DeepMind | Parent: $402,8 Mds CA | — | Gemini 750M MAU, AlphaFold |
| Meta AI | Parent: $201 Mds CA | — | Llama open-weight, le plus déployé |
| Mistral AI | 300M€ | 25x | Champion européen, on-prem UE |

> Les 5 plus gros model creators ont levé collectivement **>$100 Mds**. La barrière à l'entrée est monumentale.

<small>Sources : [1] [Sherwood News](https://sherwood.news/business/openais-arr-reached-over-usd20-billion-in-2025-cfo-says/) · [2] [Menlo Ventures](https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/)</small>

---

<!-- _class: cols -->

# 09 — Open-Source vs Closed : le grand basculement

<div class="left">

**L'open-source atteint la parité** [1]

- Usage (tokens) : **43%** open vs **42%** closed
- Coût moyen : **$0,23** vs **$1,86** / M tokens
- Écart de performance : de 8% à **1,7%** en 1 an [2]

</div>
<div class="right">

**Mais la monétisation reste closed** [1]

- Revenus : **4%** open vs **96%** closed
- L'open-source est **87% moins cher**
- Hugging Face : **2M+** modèles en 335 jours [2]

</div>

<small>Sources : [1] [OpenRouter](https://openrouter.ai/state-of-ai) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: cols -->

# 10 — Spotlight : Mistral AI — le champion européen

<div class="left">

- **Paris**, fondée en **2023** — 2 ans seulement [1]
- **300M€ ARR** (Sep 2025, 25x YoY) [1]
- **~$14 Mds** val., **~$3 Mds** levés [1]
- API (Large 3, Medium 3), Le Chat, Ministral

</div>
<div class="right">

- **Seul** fournisseur frontier avec hébergement natif UE [2]
- Medium 3 : **$0,40/$2** vs GPT-4o **$2,50/$10** [2]
- Contrat armée française, ASML investisseur (**€1,3 Md**) [3]
- On-premises pour RGPD strict → moat souveraineté

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [2] [CNBC](https://www.cnbc.com/) · [3] [CNBC](https://www.cnbc.com/2025/09/09/ai-firm-mistral-valued-at-14-billion-as-asml-takes-major-stake.html)</small>

---

# 11 — Discussion : Open-weight vs Closed pour votre startup

> Vous construisez une **startup legaltech** qui analyse des contrats. Trois options :

| Option | Modèle | Coût / M tokens | Souveraineté |
|--------|--------|-----------------|-------------|
| A | API OpenAI (GPT-4o) | $2,50-10 | Données chez OpenAI (Cloud Act) |
| B | Mistral Large 3 (self-hosted) | $0,40 | On-premise UE possible |
| C | DeepSeek R1 (open-source) | $0,55 | Modèle chinois, risque réputationnel |

**Questions pour la classe** :
- Quel critère pèse le plus : coût, performance, ou confiance client ?
- Vos clients (cabinets d'avocats) accepteront-ils que leurs contrats transitent par un cloud US ?

---

<!-- _class: section -->

# Distribution, Tooling, Safety

## Model Hubs, APIs, évaluation

---

# 12 — Model Hubs & APIs — les intermédiaires du stack

| Entreprise | Métrique clé [1] | Rôle |
|------------|-------------|------|
| Hugging Face (FR/US) | 2M+ modèles, $4,5 Mds val. | Hub open-source, "GitHub de l'IA" |
| OpenRouter | $500 M val. | API unifiée pour 200+ modèles |
| Together AI | $3,3 Mds val., ~$300 M CA | Inference open-source rapide |
| Pinecone | $26,6 M CA | Vector DB managée (RAG) |
| Weaviate (NL) | $200 M val. | Vector DB open-source européenne |

> Les Model Hubs sont les **App Stores de l'IA** : celui qui contrôle la distribution contrôle l'écosystème.

<small>Sources : [1] [Crunchbase](https://www.crunchbase.com/) · [Sacra](https://sacra.com/c/hugging-face/) · Sites officiels</small>

---

# 13 — Évaluation & Safety — la couche la plus jeune

| Entreprise | Pays | Métrique clé [1] | Rôle |
|------------|------|-------------|------|
| LMSYS Arena | USA | $1,7 Mds val. | Chatbot Arena — benchmark crowdsourcé |
| Giskard | France | Clients : AXA, BNP, Michelin | Red teaming LLM, compliance EU AI Act |
| Weights & Biases | USA | Acquis ~$1,7 Mds | ML experiment tracking |

- Giskard (Paris) : **~15 personnes** servent des Fortune 500 avec **€7,5 M** levés [2]
- Participe à la **rédaction des standards EU AI Act** (CEN-CENELEC) [2]
- L'EU AI Act crée un marché de compliance de **€17 Mds** [3]

> La couche safety est sous-financée — mais la régulation va créer une demande massive dès 2025.

<small>Sources : [1] [Crunchbase](https://www.crunchbase.com/) · [2] [TechCrunch](https://techcrunch.com/2023/11/14/giskards-open-source-framework-evaluates-ai-models-before-theyre-pushed-into-production/) · [3] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/)</small>

---

<!-- _class: section -->

# Applications & Synthèse

## Où la valeur rencontre l'utilisateur

---

# 14 — Applications AI-natives — la couche la plus visible

| Entreprise | ARR / Val. [1] | Produit |
|------------|----------------|---------|
| Cursor | $1 Mds+ / $29,3 Mds | Éditeur de code IA (+9 900% YoY) |
| GitHub Copilot | $2 Mds / Microsoft | Pair-programming IA (77M+ devs) |
| Perplexity | ~$200 M / $20 Mds | Recherche IA |
| Harvey | $195 M / $8 Mds | IA juridique |
| ElevenLabs | $330 M+ / $11 Mds | Voix IA (41% Fortune 500) |

> Pricing power max sur cette couche : **$20-200/mois/user**.

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [ElevenLabs](https://elevenlabs.io/blog/series-d) · [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: cols -->

# 15 — L'écosystème européen : forces et faiblesses

<div class="left">

**Forces**

- ASML (monopole EUV) [1]
- Mistral AI (frontier, Apache 2.0) [2]
- Hugging Face (hub dominant) [3]
- OVHcloud / Scaleway (cloud souverain)
- Giskard (EU AI Act compliance)
- ElevenLabs ($11 Mds) [4]

</div>
<div class="right">

**Faiblesses**

- Aucun NVIDIA européen
- Financement **10-50x inférieur** [5]
- Pas de hyperscaler top 3
- Fuite des talents (salaires 2-3x)
- Marché fragmenté (27 régulateurs)

</div>

<small>Sources : [1] [ASML](https://www.asml.com/) · [2] [Mistral AI](https://mistral.ai/) · [3] [Hugging Face](https://huggingface.co/) · [4] [ElevenLabs](https://elevenlabs.io/blog/series-d) · [5] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 16 — L'écosystème français en chiffres

La France se positionne comme hub IA européen :

- **750+ startups IA** en France, dont **43%** utilisent la GenAI [1]
- **~36 000 emplois** dans l'IA, croissance des offres : **+91% YoY** [2]
- Plan France IA : **€109 Mds** annoncés, Bpifrance : **€10 Mds** dédiés [3]
- EU InvestAI : **€200 Mds** mobilisés sur 5 ans [4]

> **Contexte** : l'UE mobilise €200 Mds via InvestAI, mais les US investissent **8x plus** en privé. L'Europe ne gagnera pas la course au compute, mais peut gagner celle de la **confiance**.

<small>Sources : [1] [France Digitale](https://www.frenchtechjournal.com/france-digital-ai-mapping/) · [2] [LinkedIn](https://economicgraph.linkedin.com/research/work-change-report) · [3] [Bpifrance](https://www.bpifrance.com/2025/03/27/bpifrance-deploys-e10-billion-to-develop-the-ai-ecosystem/) · [4] [EU Commission](https://commission.europa.eu/topics/competitiveness/ai-continent_en)</small>

---

<!-- _class: compact -->

# 17 — Discussion : Où se positionner dans le stack ?

> **500K€**, **4 personnes** techniques, 18 mois de runway.

| Couche | Capital requis | Concurrence | Opportunité |
|--------|---------------|-------------|-------------|
| Hardware | >$1 Mds | Extrême | Quasi impossible |
| Foundation Models | >$100 M | Très forte | Niche (code, médical) |
| Hubs / APIs | $1-10 M | Forte | Orchestration, vertical |
| Safety / Éval. | $500K-5 M | Modérée | EU AI Act, compliance |
| Applications | $200K-5 M | Variable | Vertical + workflow |

**Questions** :
- Quel ratio impact/capital est le meilleur ?
- Safety viable à 4 ? (Giskard : €7,5M levés)

---

# 18 — Key Takeaways

1. **La value chain = des dépendances** — votre startup IA dépend de toutes les couches en dessous. Cartographiez vos risques fournisseurs.

2. **Le compute est le bottleneck** — NVIDIA a un quasi-monopole (56% de marge nette). Le coût GPU est souvent votre 1er poste.

3. **Open vs Closed est stratégique** — Apache 2.0 (Mistral, Llama) offre indépendance et meilleur unit economics. L'API est pratique mais crée du vendor lock-in.

4. **L'Europe a de vrais champions** — ASML, Mistral, Hugging Face, Giskard, ElevenLabs. Le gap est dans le financement, pas dans le talent.

5. **La régulation crée des marchés** — l'EU AI Act n'est pas qu'une contrainte : c'est un marché de **€17 Mds** pour ceux qui vendent la compliance.

> **Prochaine partie** : comment monétiser l'IA — business models, case studies et unit economics.
