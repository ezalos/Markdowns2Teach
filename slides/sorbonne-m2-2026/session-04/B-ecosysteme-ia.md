---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 4 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche AI Value Chain & Market Intelligence 2024–2025 · Données publiques"
---

<!-- ABOUTME: Ecosysteme IA — value chain 9 couches, acteurs cles, taille du marche, investissements et positionnement UE. -->
<!-- ABOUTME: Deck B de la Session 4, cadre business pour entrepreneurs M2. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# L'ecosysteme IA

## 9 couches, 50 entreprises — qui capture la valeur ?

M2 IMT&E · Paris 1 Pantheon-Sorbonne · 2026

---

<!-- _class: section -->

# Le marche IA en 2025

## Taille, vitesse, investissements

---

# 01 — L'IA en chiffres : un marche a $2 500+ Mds

| Metrique | Valeur | Source |
|----------|--------|--------|
| PIB mondial (reference) | **~$100 000 Mds** | Wikipedia |
| Marche mondial IA 2025 | **$1 757 Mds** | Gartner |
| Projection 2026 | **$2 527 Mds** (+44% YoY) | Gartner |
| Investissement corporate 2024 | **$252 Mds** | Stanford HAI |
| Part de l'IA dans le VC mondial | **~50%** (2025) | Crunchbase [5] |
| Adoption en entreprise | 55% → **88%** (en 2 ans) | McKinsey |
| Licornes IA | **498** ($2 700 Mds cumules) | CB Insights |

> L'IA capte **1 dollar de VC sur 2** et represente deja **~2,5%** du PIB mondial.

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [4] [CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/) · [5] [Crunchbase](https://news.crunchbase.com/venture/funding-data-third-largest-year-2025/) · [6] [Wikipedia — GWP](https://en.wikipedia.org/wiki/Gross_world_product)</small>

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

- **Cumule 2025-2027** : $1 150 Mds (Goldman Sachs) [2]
- Amazon prevoit un **FCF negatif de -$17 Mds** en 2026 [1]

> Pari existentiel : ces entreprises brulent du cash a un rythme historique.

<small>Sources : [1] [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html) · [2] [Goldman Sachs](https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026)</small>

---

<!-- _class: cols -->

# 03 — Bulle ou boom ? Les signaux contradictoires

<div class="left">

**Signaux haussiers**

- Marche **$2 527 Mds** en 2026 [1]
- **88%** d'adoption en entreprise [2]
- Couts d'inference **÷280** en 2 ans [3]
- **498 licornes** IA dans le monde [4]

</div>
<div class="right">

**Signaux baissiers**

- **95%** des pilotes IA = zero ROI [5]
- Hyperscalers FCF en negatif [6]
- **$1 500 Mds** de nouvelle dette [7]
- S&P top 10 = **40,7%** (record) [7]

</div>

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-1-15-gartner-says-worldwide-ai-spending-will-total-2-point-5-trillion-dollars-in-2026) · [2] [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [3] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [4] [CB Insights](https://www.cbinsights.com/research/report/ai-trends-2025/) · [5] [MIT / Fortune](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) · [6] [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html) · [7] [Goldman Sachs](https://www.goldmansachs.com/insights/articles/why-ai-companies-may-invest-more-than-500-billion-in-2026)</small>

---

<!-- _class: section -->

# La AI Value Chain

## 9 couches, de l'energie aux applications

---

<!-- _class: img-right -->

# 04 — Vue d'ensemble : les 9 couches du stack IA

![bg right:55% contain](assets/infographics/ai-stack-9_run_20260216_171301_8858a8.png)

**9 couches** structurent l'ecosysteme :

- **0-1 Energy & Hardware** — NVIDIA, TSMC, ASML
- **2-3 Cloud & Data** — AWS, Azure, Scale AI
- **4-5 Models & Hubs** — OpenAI, Mistral, HF
- **6-7 APIs & Safety** — OpenRouter, Giskard
- **8 Applications** — Cursor, Perplexity

> Bas = plus de **capital** et concentration. Haut = plus de **differenciation**.

---

<!-- _class: img-right -->

# 05 — (🔷0) Energy — le bottleneck invisible

- Un cluster de **100K GPUs** = **87,5 MW** avant refroidissement [1]
- Les data centers IA consommeront **432 TWh** en 2030 (**44%** du total) [1]
- Goulot d'etranglement : **7 ans** d'attente pour connexion reseau en Virginie [1]

**La ruee vers le nucleaire** :
- Microsoft relance Three Mile Island (**835 MW**, $1,6 Mds) [2]
- Amazon : 1,92 GW nucleaire + $700M dans les SMR [2]

**L'avantage francais** : EDF dispose de **3 GW** nucleaire disponible maintenant. Mistral construit un data center nucleaire au sud de Paris [2].

> L'energie, pas les puces, determine **ou** l'IA se construit.

<small>Sources : [1] [Epoch AI](https://epoch.ai/blog/can-ai-scaling-continue-through-2030) · [2] [CNBC](https://www.cnbc.com/2025/11/18/trump-nuclear-three-mile-island-crane-loan-constellation-ceg.html) · [3] [Data Center Dynamics](https://www.datacenterdynamics.com/en/analysis/france-ai-data-center-build-out-emmanuel-macron/) · [4] [Sifted](https://sifted.eu/articles/mistral-data-center-news)</small>

![bg right:55% contain](assets/infographics/energy-layer_run_20260322_230538_d2822c.png)

---

<!-- _class: img-right -->

# 06 — (🔷1) Hardware & Silicon — 3 entreprises, tout le pouvoir

**3 chokepoints** controlent la chaine :

- **ASML** (Pays-Bas) — seul fournisseur EUV mondial. Machines a $200-370M, 2 ans de backlog. N'a **jamais** vendu d'EUV a la Chine [1]
- **TSMC** (Taiwan) — fabrique les puces NVIDIA, Apple. **62%** de marge brute [1]
- **NVIDIA** — H100 coute **$3 320** a fabriquer, vendu **$28-40K** [2]

**Memoire HBM** : SK Hynix detient **53-62%** du marche, fournit **~90%** de la HBM NVIDIA. Prix DRAM : **+171,8%** YoY [2].

> Le silicon IA est un oligopole ou 3 entreprises concentrent tout le pouvoir de negociation.

<small>Sources : [1] [ASML Q4 2024](https://www.asml.com/en/news/press-releases/2025/q4-2024-financial-results) · [TSMC](https://investor.tsmc.com/english/quarterly-results/2024/q4) · [2] [The Decoder](https://the-decoder.com/nvidias-h100-gpu-sells-like-hot-cakes-with-high-profit-margins/) · [3] [Tom's Hardware](https://www.tomshardware.com/pc-components/dram/dram-prices-surge-171-percent-year-over-year-ai-demand-drives-a-higher-yoy-price-increase-than-gold)</small>

![bg right:55% contain](assets/infographics/hardware-layer_run_20260322_230538_4c5044.png)

---

<!-- _class: cols -->

# 07 — NVIDIA — le triple verrouillage

<div class="left">

**Hardware** — $130,5 Mds CA (+114%), **88%** du CA = data center [1]

**Software** — CUDA : 20 ans d'ecosysteme, **6M developpeurs** verrouilles. Migrer = reecrire tout le code [2]

**Ecosysteme** — $5 Mds investis dans Intel, CoreWeave, Lambda Labs. Controle le tier cloud niche [2]

</div>
<div class="right">

**Les menaces** :
- **Google TPU** Ironwood : egalise Blackwell. Anthropic signe pour **1M puces TPU** [3]. Google controle le workload ET le silicon [2]
- **Amazon Trainium2** : **30-40%** meilleur rapport prix/perf. AWS oriente les workloads vers ses propres puces [4]
- ASICs custom = **15-25%** du marche d'ici 2026. Mais le TAM NVIDIA croit quand meme : **$242B → $1,2T** [4]

</div>

<small>Sources : [1] [NVIDIA IR FY2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2025/) · [2] [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the) · [3] [Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) · [4] [CNBC](https://www.cnbc.com/2025/11/21/nvidia-gpus-google-tpus-aws-trainium-comparing-the-top-ai-chips.html)</small>

---

<!-- _class: img-right -->

# 08 — Scaling compute : jusqu'ou ?

![bg right:55% contain](assets/epoch/epoch-scaling-2030-summary-slideshow-figure.png)

- Training runs **5 000x plus grands** que GPT-4 d'ici 2030 [1]
- Equivalent : refaire le saut GPT-2 → GPT-4 **une deuxieme fois** [1]
- Clusters a **$100 Mds+**, consommant des **gigawatts** [2]
- Croissance actuelle : **~4x par an** en compute d'entrainement [1]

> 4 bottlenecks potentiels : energie, puces, donnees, latence. **L'energie** est la contrainte la plus serree.

<small>Sources : [1] [Epoch AI — Scaling Through 2030](https://epoch.ai/blog/can-ai-scaling-continue-through-2030) · [2] [Epoch AI — AI in 2030](https://epoch.ai/blog/what-will-ai-look-like-in-2030)</small>

---

<!-- _class: img-right -->

# 09 — (🔷2) Cloud — les 3 geants et le cloud souverain

**Hyperscalers** (65% du marche) [1] : AWS ($128,7 Mds), Azure (~$75 Mds), Google Cloud (~$58,8 Mds)

**Le basculement souverain** :
- **61%** des DSI europeens veulent migrer localement [2]
- Le **CLOUD Act** US permet l'acces aux donnees — en conflit avec le RGPD [2]
- **OVHcloud** : EUR 1,085 Mds · **Scaleway** : ~EUR 200M (CA double en 2024), 1er cloud europeen Blackwell Ultra [2]

> Microsoft a admis devant le Senat francais ne pas pouvoir "garantir" la securite des donnees UE.

<small>Sources : [1] [Canalys Q1 2025](https://www.e-channelnews.com/global-cloud-spending-surged-21-in-q1-2025/) · [2] [Computerworld](https://www.computerworld.com/article/4088666/gartner-european-it-leaders-to-boost-spending-on-local-clouds-amid-geopolitical-worries.html) · [3] [ActuIA](https://www.actuia.com/en/news/sensitive-data-and-cloud-act-microsoft-france-admits-it-cannot-oppose-an-american-injunction/) · [4] [Scaleway](https://www.scaleway.com/en/news/scaleway-announces-at-ai-pulse-major-advancements-in-ai-model-accessibility-new-compute-capabilities-and-expansion-of-its-presence-across-europe/)</small>

![bg right:55% contain](assets/infographics/cloud-layer_run_20260322_230538_981702.png)

---

<!-- _class: img-right -->

# 10 — (🔷3) Data — la ressource la plus rare

Le bottleneck n'est plus le compute — c'est la **donnée** [1] :

- Coût marginal d'annotation > compute **3:1** en post-training. Croissance labeling **88x** en 1 an vs compute **1,3x** [1]
- Chaque lab frontière dépense **~$1 Md/an** en annotation — jamais déclaré séparément [1]
- **Meta** rachète 49% de Scale AI pour **$14,3 Mds** → exode de Google, OpenAI, xAI vers Surge/Mercor [2]
- Paradoxe synthétique : coût unitaire **÷100** — mais les besoins explosent : marché total **$2,3 Mds → $10-17 Mds** d'ici 2030 [3]

> Celui qui contrôle la boucle data → modèle → users → data gagne.

<small>Sources : [1] [Kang 2025 / UC Irvine](https://ddkang.substack.com/p/human-data-is-probably-more-expensive) + [Foundation Capital](https://foundationcapital.com/) · [2] [TechCrunch](https://techcrunch.com/2025/06/13/scale-ai-confirms-significant-investment-from-meta-says-ceo-alexandr-wang-is-leaving/) · [3] [Epoch AI](https://epoch.ai/) + [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/synthetic-data-market)</small>

![bg right:55% contain](assets/infographics/data-layer_run_20260322_230615_b8c131.png)

---

# 11 — (🔷4) Foundation Models — le paradoxe des couts

| Lab | ARR fin 2025 [1] | Note |
|-----|-----------|------|
| OpenAI | ~$20 Mds | 400M+ WAU, pertes prevues $14 Mds |
| Anthropic | ~$9 Mds | Claude Code seul = **$2,5 Mds** ARR [2] |
| Google DeepMind | Parent: $402,8 Mds CA | Gemini 750M MAU |
| Meta AI | Parent: $201 Mds CA | Llama open-weight, le plus deploye |
| Mistral AI | 300M EUR | Champion europeen, on-prem UE |

**Le paradoxe** : construire l'usine coute **28x** plus cher a chaque generation. Mais la faire tourner coute **280x** moins cher ($20 → $0,07 / M tokens en 18 mois) [2].

<small>Sources : [1] [Sherwood News](https://sherwood.news/business/openais-arr-reached-over-usd20-billion-in-2025-cfo-says/) · [2] [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends) · [3] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: img-right -->

# 12 — Inference : le cout qui s'effondre

![bg right:55% contain](assets/epoch/epoch-inference-econ-01.png)

- Le cout d'inference baisse de **3x par an** [1]
- **DeepSeek R1** : entraine pour **$5,6M** vs GPT-4 **$78M** — l'innovation architecturale bat le brute-force [2]
- NVIDIA perd **$589 Mds** de market cap en un jour [2]
- Bottleneck cache : la **latence reseau** (30 us fixes par echange GPU) domine sous 10 MB par tensor [1]

> L'effondrement des couts d'inference rend l'IA accessible a toutes les startups. Mais jeter plus de GPUs **n'accelere pas lineairement** la reponse.

<small>Sources : [1] [Epoch AI](https://epoch.ai/blog/inference-economics-of-language-models) · [2] [Yahoo Finance](https://finance.yahoo.com/news/nvidia-stock-plummets-loses-record-589-billion-as-deepseek-prompts-questions-over-ai-spending-135105824.html)</small>

---

<!-- _class: cols -->

# 13 — Open-Source vs Closed : la progression

<div class="left">

**L'open-source progresse vite** [1]

- Usage global : **~30%** open vs **~70%** proprietary
- En roleplay : open-source a **43%**, quasi-parite [1]
- Ecart de performance : de 8% a **1,7%** en 1 an [2]

</div>
<div class="right">

**Mais la monetisation reste closed** [1]

- L'essentiel des revenus va aux modeles proprietary [1]
- **Meta strategy** : donner les modeles pour commoditiser la couche, profiter de Instagram/WhatsApp [3]
- Seul Meta ($160B+ CA pub) peut subsidier indefiniment [3]

</div>

<small>Sources : [1] [OpenRouter / arXiv 2601.10088](https://openrouter.ai/state-of-ai) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [Stratechery](https://stratechery.com/2024/meta-and-open/)</small>

---

<!-- _class: cols -->

# 14 — Mistral AI — le champion europeen

<div class="left">

- **Paris**, fondee en **2023** — 2 ans seulement [1]
- **300M EUR ARR** (Sep 2025, 25x YoY) [1]
- **~$14 Mds** val., **~$3 Mds** leves [1]
- **ASML investit EUR 1,3 Md** pour 11% — alliance industrielle pan-europeenne [3]

</div>
<div class="right">

- **Seul** fournisseur frontier avec hebergement natif UE [2]
- Medium 3 : **$0,40/$2** vs GPT-4o **$2,50/$10** [2]
- Contrat armee francaise [3]
- 90% de la perf. frontier a **20% du prix** — validation de l'approche **efficiency-first** [3]

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [2] [Mistral AI Pricing](https://mistral.ai/pricing) · [3] [CNBC](https://www.cnbc.com/2025/09/09/ai-firm-mistral-valued-at-14-billion-as-asml-takes-major-stake.html)</small>

---

<!-- _class: img-right -->

# 15 — (🔷5-6) Models Hub & APIs — les picks & shovels

**Ceux qui profitent quel que soit le gagnant** :

- **Hugging Face** (Paris) — 2M+ modeles, **0% commission** aux createurs (vs Apple 30%). $4,5 Mds val. Investisseurs : Google, Amazon, NVIDIA [1]
- **OpenRouter** — 400+ LLMs, API unifiee, **5%** commission. 8,4T tokens/mois. Moat = intelligence de routage [2]
- **Together AI** — $15M → **$300M** ARR en 2 ans. Construit ses propres data centers. Chaque release open-weight = catalyseur [3]

> Les plateformes de distribution accelerent la **commoditisation** des modeles — mais expandent le marche total.

<small>Sources : [1] [Ars Technica](https://arstechnica.com/information-technology/2024/09/ai-hosting-platform-surpasses-1-million-models-for-the-first-time/) · [2] [Sacra](https://sacra.com/research/openrouter/) · [3] [Sacra](https://sacra.com/c/together-ai/)</small>

![bg right:55% contain](assets/infographics/distribution-layer_run_20260322_230616_bbdbe2.png)

---

<!-- _class: img-right -->

# 16 — (🔷7) Safety & Compliance — milliards d'opportunite

L'EU AI Act entre en vigueur : **2 aout 2026**, application complete pour les systemes a haut risque [1].

- **65 000+** systemes a haut risque a certifier [1]
- Marche compliance estime a **EUR 7,6-31 Mds** sur 5 ans (fourchette haute contestee) [1]
- Penalites : jusqu'a **EUR 35M** ou **7%** du CA mondial [1]

**Giskard** (Paris, ~24 pers.) : open-source pour tester hallucinations, biais, injections. Clients : **AXA, BNP, Michelin, L'Oreal, Banque de France**. Benchmark Phare avec **Google DeepMind** [2].

> La regulation **cree** des marches. Le RGPD a cree un marche privacy de milliards — l'AI Act fera pareil.

<small>Sources : [1] [CDI](https://www2.datainnovation.org/2021-aia-costs.pdf) · [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [TechCrunch](https://techcrunch.com/2023/11/14/giskards-open-source-framework-evaluates-ai-models-before-theyre-pushed-into-production/)</small>

![bg right:55% contain](assets/infographics/safety-layer_run_20260322_230617_919b22.png)

---

<!-- _class: img-right -->

# 17 — (🔷8) Applications AI-natives — vertical vs wrapper

**Vertical AI = croissance explosive** :
- **Cursor** : $0 → **$2 Mds** ARR en 2 ans (record SaaS) [1]
- **Harvey** : 50 des 100 top cabinets US, $8 Mds val. [2]
- **ElevenLabs** : $330M ARR, 41% du Fortune 500 [3]

**Wrappers = effondrement** :
- **Jasper** : $120M → **$35-55M** apres ChatGPT. Les 2 co-fondateurs partis [4]

**La formule gagnante** : data flywheel proprietaire + profondeur workflow + strategie multi-modeles

> **Le modele IA n'est PAS le moat.** C'est le workflow, la donnee et l'expertise domaine autour qui creent la defensibilite.

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [2] [Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/andreessen-horowitz-invests-in-legal-ai-startup-harvey-at-an-8-billion-valuation) · [3] [ElevenLabs](https://elevenlabs.io/blog/series-d) · [4] [GetLatka](https://getlatka.com/companies/jasper.ai)</small>

![bg right:55% contain](assets/infographics/applications-layer_run_20260322_234235_572d5a.png)

---

<!-- _class: section -->

# L'Europe dans le stack

## Forces, faiblesses, positionnement

---

<!-- _class: cols -->

# 18 — L'ecosysteme europeen : forces et faiblesses

<div class="left">

**Forces**

- ASML (monopole EUV) [1]
- Mistral AI (frontier, efficiency-first) [2]
- Hugging Face (hub dominant) [3]
- OVHcloud / Scaleway (cloud souverain)
- Giskard (EU AI Act compliance)
- ElevenLabs ($11 Mds) [4]

</div>
<div class="right">

**Faiblesses**

- Aucun NVIDIA europeen
- Financement **10-50x inferieur** [5]
- Pas de hyperscaler top 3
- Fuite des talents (salaires 2-3x)
- Marche fragmente (27 regulateurs)

</div>

<small>Sources : [1] [ASML](https://www.asml.com/en/news/press-releases/2025/q4-2024-financial-results) · [2] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [3] [Ars Technica](https://arstechnica.com/information-technology/2024/09/ai-hosting-platform-surpasses-1-million-models-for-the-first-time/) · [4] [ElevenLabs](https://elevenlabs.io/blog/series-d) · [5] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 19 — L'ecosysteme francais en chiffres

La France se positionne comme hub IA europeen :

- **750+ startups IA** en France, dont **43%** utilisent la GenAI [1]
- **~36 000 emplois** dans l'IA, croissance des offres : **+91% YoY** [1]
- Plan France IA : **EUR 109 Mds** annonces, Bpifrance : **EUR 10 Mds** dedies [2]
- EU InvestAI : **EUR 200 Mds** mobilises sur 5 ans [3]

> **Contexte** : l'UE mobilise EUR 200 Mds via InvestAI, mais les US investissent **8x plus** en prive. L'Europe ne gagnera pas la course au compute, mais peut gagner celle de la **confiance**.

<small>Sources : [1] [France Digitale](https://www.frenchtechjournal.com/france-digital-ai-mapping/) · [2] [Bpifrance](https://www.bpifrance.com/2025/03/27/bpifrance-deploys-e10-billion-to-develop-the-ai-ecosystem/) · [3] [EU Commission](https://commission.europa.eu/topics/competitiveness/ai-continent_en)</small>

---

<!-- _class: section -->

# Synthese

---

<!-- _class: img-right -->

# 20 — Discussion : L'IA en 2030

![bg right:55% contain](assets/epoch/epoch-econ-value-01.png)

**Que vaudra l'IA ?** GDPval : **74%** des taches resolues. RLI : seulement **4%**. Software engineering : **20-70%** de gains dans 6/7 etudes, mais 1 etude montre **-20%** [1].

**Faites vos predictions** :

- L'IA remplacera des **metiers entiers** ou transformera la **facon de travailler** ?
- A **$100 Mds** le cluster, combien d'entreprises restent dans la course ? Consequences pour la concurrence ?
- L'energie (**40 → 90 GW** aux US) : frein ecologique ou accelerateur de souverainete ?

<small>Sources : [1] [Epoch AI](https://epoch.ai/blog/what-do-economic-value-benchmarks-tell-us)</small>

---

<!-- _class: compact -->

# 21 — Discussion : Ou se positionner dans le stack ?

> **500K EUR**, **4 personnes** techniques, 18 mois de runway.

| Couche | Capital requis | Concurrence | Opportunite |
|--------|---------------|-------------|-------------|
| Hardware | >$1 Mds | Extreme | Quasi impossible |
| Foundation Models | >$100 M | Tres forte | Niche (code, medical) |
| Hubs / APIs | $1-10 M | Forte | Orchestration, vertical |
| Safety / Eval. | $500K-5 M | Moderee | EU AI Act, compliance |
| Applications | $200K-5 M | Variable | Vertical + workflow |

**Questions** :
- Quel ratio impact/capital est le meilleur ?
- Safety viable a 4 ? (Giskard : EUR 7,5M leves)

---

# 22 — Key Takeaways

1. **La value chain = des dependances** — votre startup IA depend de toutes les couches en dessous. Cartographiez vos risques fournisseurs

2. **L'energie est le nouveau bottleneck** — pas les puces. La France et son nucleaire ont un avantage strategique reel

3. **La donnee est plus rare que le compute** — couts de labeling 88x en 1 an. Construisez votre data flywheel des le jour 1

4. **NVIDIA : triple verrouillage** — hardware + CUDA + ecosysteme. Mais Google TPU et Amazon Trainium menacent 15-25% du marche

5. **La regulation cree des marches** — l'EU AI Act n'est pas qu'une contrainte : c'est **EUR 31 Mds sur 5 ans** pour ceux qui vendent la compliance

> **Prochaine partie** : comment monetiser l'IA — business models, case studies et unit economics.
