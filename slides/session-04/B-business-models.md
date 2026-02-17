---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 4 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche Business Models & Case Studies 2024–2025 · Données publiques"
---

<!-- ABOUTME: Business models IA, pricing, moats, et études de cas (Klarna, L'Oréal, Mistral, Cursor). -->
<!-- ABOUTME: Seconde moitié de la Session 4, focus entrepreneurial : comment monétiser et défendre une startup IA. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Business Models & Cas Réels

## Tarifer, structurer, défendre — le guide entrepreneur

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Comment tarifer l'IA

## Du seat-based à l'outcome-based

---

# 01 — L'effondrement des coûts : le fait structurant

L'inférence IA connaît une **déflation historique** :

- GPT-3.5 : de $20 à **$0,07** / M tokens en 2 ans = **÷280** [1]
- Rythme post-2024 : **200x/an** de baisse [1]
- Efficience algorithmique : doublement tous les **~16 mois** [1]

**Niveaux de prix début 2026** (par million de tokens) :

| Tier | Modèle | Prix input/output |
|------|--------|-------------------|
| Budget | GPT-4o mini | $0,15 / $0,60 [3] |
| Budget | DeepSeek R1 | $0,55 / $2,19 [4] |
| Mid | Claude Sonnet 4.5 | $3,00 / $15,00 [5] |
| Premium | GPT-4 Turbo | $10,00 / $30,00 [3] |

<small>Sources : [1] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [2] [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends) · [3] [OpenAI Pricing](https://openai.com/api/pricing/) · [4] [DeepSeek Pricing](https://api-docs.deepseek.com/quick_start/pricing) · [5] [Anthropic Pricing](https://www.anthropic.com/pricing)</small>

---

# 02 — De la licence seat à l'outcome-based

| Modèle | Part 2024 → 2025 [1] | Exemple | Prix |
|--------|-------------------|---------|------|
| Seat-based | 21% → **15%** | GitHub Copilot | $19-39/user/mois |
| Hybride | 27% → **41%** | Cursor | $20/mois + crédits |
| Outcome-based | Émergent | Intercom Fin | $0,99/résolution |
| Per-action | Émergent | Salesforce | $0,10/action |

- Intercom Fin : **$0,99/résolution** vs $39/seat humain → adoption **+40%** [2]
- D'ici 2030, **40%+** des dépenses SaaS passeront à l'usage/outcome [1]

> Chaque trimestre, le même output coûte moins cher. Votre pricing doit **anticiper cette déflation**.

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom) · [2] [Intercom](https://www.intercom.com/fin)</small>

---

# 03 — Discussion : Tarifer votre produit IA

> Vous lancez un **assistant juridique IA** pour PME. Trois options de pricing :

| Option | Modèle | Avantage | Risque |
|--------|--------|----------|--------|
| A | $49/seat/mois | Revenus prévisibles | Sous-utilisation → churn |
| B | $2/contrat analysé | Aligné sur la valeur | Revenus volatils |
| C | $29/seat + $0,50/contrat | Prévisible + incitatif | Complexe à expliquer |

**Questions pour la classe** :
- Vos clients (PME) préfèrent-ils la prévisibilité ou l'alignement valeur ?
- Si vos coûts d'inférence baissent de 10x/an, quelle option vous protège le mieux ?

---

<!-- _class: section -->

# Les 7 patterns de business model

## Quel modèle pour quel profil de startup

---

# 04 — Vue d'ensemble : 7 familles de business models IA

| Pattern | Exemple | Métrique clé [1] |
|---------|---------|-------------|
| Vertical AI SaaS | Harvey (legal) | $195 M ARR, $8 Mds val. |
| AIaaS (plateforme) | Databricks | $4,8 Mds ARR |
| Wrappers | Jasper, Copy.ai | 85-92% de taux d'échec |
| Open-Source | Mistral, Llama | Distribution → conversion |
| Embedded AI | Microsoft Copilot | +20-37% d'uplift prix |
| Agents autonomes | Sierra, Salesforce | $7,8 Mds → $50 Mds (2030) |
| Digital Labor | Klarna AI, Cursor | $3 340 Mds cumulés d'ici 2030 |

> Chaque pattern a un profil risque/rendement distinct. Le choix dépend de votre capital et votre timeline.

<small>Sources : [1] [a16z](https://a16z.com/) · [IDC](https://www.idc.com/) · [Gartner](https://www.gartner.com/)</small>

---

# 05 — Vertical AI SaaS — la mine d'or

Le Vertical AI SaaS cible un secteur précis avec des données domain-specific :

- **Harvey** (legal) : $195 M ARR, $8 Mds val. [1]
- **Abridge** (santé) : $100 M ARR, $5,3 Mds val. [1]
- **Kling AI** (vidéo) : $240 M ARR en 10 mois [2]

Pourquoi ça marche :
- TAM **10x** plus grand que le SaaS legacy du même secteur
- Net Revenue Retention **120%+** (expansion naturelle)
- **Data domain-specific** = moat que les généralistes ne peuvent pas copier

<small>Sources : [1] [Bloomberg](https://www.bloomberg.com/) · [2] [TechCrunch](https://techcrunch.com/)</small>

---

# 06 — Wrappers, Agents & Embedded AI

**Wrappers** — le piège de la commoditisation :
- **85-92%** échouent dans les 5 ans [1]
- 8 000+ assistants d'écriture IA : seulement **10-15** génèrent du revenu [1]

**Agents autonomes** — la prochaine vague :
- Marché **$7,8 Mds** (2025) → **$50,3 Mds** (2030), CAGR 45,8% [2]
- Sierra : $100 M ARR en 21 mois, $10 Mds val. [3]
- Attention : **40%** des projets agents annulés d'ici 2027 [2]

**Embedded AI** — l'IA dans les produits existants :
- Microsoft 365 Copilot : **$30/user/mois** d'uplift sur licence [3]

<small>Sources : [1] [a16z](https://a16z.com/) · [2] [IDC](https://www.idc.com/) · [3] [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: section -->

# Construire des moats en IA

## Comment défendre sa position

---

# 07 — Les moats de l'IA : taxonomie

| Moat | Durabilité | Exemple |
|------|-----------|---------|
| Data propriétaire | Très forte | Tempus (5M dossiers patients) |
| Network effects | Très forte | Hugging Face (2M+ modèles) |
| Switching costs | Forte | Cursor (workflows intégrés) |
| Expertise domaine | Forte | Harvey (legal AI) |
| Régulation | Forte | Mistral (hébergement UE) |
| Échelle compute | Moyenne | OpenAI ($57,9 Mds levés) [1] |
| Marque / confiance | Moyenne | Anthropic ("responsible AI") |

> Les moats les plus durables sont basés sur les **données** et les **effets de réseau**. Le modèle seul n'est plus un moat.

<small>Sources : [1] [Tracxn](https://tracxn.com/d/companies/openai/__kElhSG7uVGeFk1i71Co9-nwFtmtyMVT7f-YHMn4TFBg/funding-and-investors) · [a16z](https://a16z.com/data-moats/) · [Bessemer](https://www.bvp.com/)</small>

---

# 08 — Data flywheel : le cercle vertueux

![bg right:50% contain](assets/infographics/data-flywheel_run_20260216_171303_bb1a21.png)

**Plus d'utilisateurs → plus de données → meilleur produit → plus d'utilisateurs**

- **Cursor** : 1M+ DAU → chaque keystroke alimente le fine-tuning [1]
- **OpenAI** : 900M WAU, **2,5 Mds+** de prompts/jour [2]

> Les données ne sont un moat que si elles sont **uniques**, **croissantes**, et **intégrées au produit**. Des données génériques ≠ avantage défendable (a16z).

<small>Sources : [1] [Sacra](https://sacra.com/c/cursor/) · [2] [Sherwood News](https://sherwood.news/)</small>

---

<!-- _class: section -->

# Études de cas

## Succès, échecs, leçons pour entrepreneurs

---

<!-- _class: cols -->

# 09 — Cas : Klarna — remplacer puis réembaucher

<div class="left">

**Le succès initial** [1]

- IA remplace **700 agents** (jan 2024)
- 2,3M conversations/mois, 11→2 min
- **$40 M** d'économies annuelles
- $244M perte → **$21M profit**

</div>
<div class="right">

**Le retour de bâton** [2]

- Qualité en baisse, CEO : *"on est allés trop loin"*
- **Réembauchage** d'humains (400 SEK/h)
- H1 2025 : **$152 M de perte** malgré les économies
- Leçon : **augmentation > remplacement total**

</div>

<small>Sources : [1] [Klarna SEC F-1](https://www.sec.gov/) · [2] [Bloomberg](https://www.bloomberg.com/)</small>

---

# 10 — Cas : L'Oréal — acquérir l'IA, transformer le CA

| Dimension | Résultat [1] |
|-----------|---------|
| Stratégie | Acquisition de **ModiFace** (AR/AI beauty) |
| Impact e-commerce | Conversion **3x** avec essayage virtuel |
| Revenue Tech | **€150 M** CA d'un segment BeautyTech entier |
| Organisation | 8 000+ experts tech/data, 694 brevets déposés (2024) [1] |

- **Build vs Buy** : L'Oréal a choisi d'**acquérir** l'expertise plutôt que de construire
- Schneider Electric a fait l'inverse : build in-house → **€700 M** économisés depuis 2019 [2]
- Renault a partnered avec Google Cloud → **-26%** consommation énergie [3]

> Il n'y a pas une bonne réponse — l'approche dépend de votre timing et de vos capacités internes.

<small>Sources : [1] [L'Oréal Annual Report 2024](https://www.loreal-finance.com/en/annual-report-2024/beauty-tech-champion/) · [2] [Schneider](https://www.se.com/) · [3] [Renault](https://www.renaultgroup.com/)</small>

---

# 11 — Cas : La France championne des secteurs régulés

| Entreprise | Secteur | Valorisation | Métrique IA clé [1] |
|------------|---------|:-----------:|-----------------|
| Doctolib | Santé | **€6,5 Mds** | 1,6M consultations IA, 80M users |
| Alan | Assurance | **$4,5 Mds** | €505M ARR, +48% YoY |
| Shift Technology | Assurance | $1 Mds+ | **$5 Mds** fraude détectée/an |
| Doctrine | Legal | >€100M | 25K juristes, 27M+ documents |
| Owkin | Biotech | $1 Mds+ | Federated learning, 35 hôpitaux |

> **5 sur 5 sont français.** La France domine l'IA dans les secteurs régulés — le RGPD et l'expertise métier créent un moat naturel.

<small>Sources : [1] [Doctolib](https://about.doctolib.fr/) · [Alan](https://alan.com/) · [Shift](https://www.shift-technology.com/) · [Doctrine](https://www.doctrine.fr/) · [Owkin](https://owkin.com/)</small>

---

<!-- _class: cols -->

# 12 — Cas : Cursor — croissance record, rentabilité incertaine

<div class="left">

- **$0 → $1 Mds ARR** en 24 mois [1]
- **$29,3 Mds** val., **1M+** DAU [1]
- 4 fondateurs MIT, ~150 pers., **$0 marketing**
- Fork VS Code → **0 friction** de migration

</div>
<div class="right">

- **Marge brute négative** : $650 M/an à Anthropic [2]
- Pas de modèle propre → dépendance fournisseur
- OpenAI et Anthropic sont ses concurrents directs
- Leçon : **croissance ≠ rentabilité** en AI-native SaaS

</div>

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [2] [Foundamental](https://www.foundamental.com/)</small>

---

# 13 — Discussion : Le risque de plateforme

> **Scénario** : OpenAI annonce "ChatGPT Code Editor" — un IDE gratuit intégré à ChatGPT. C'est le cauchemar de Cursor.

- Cursor dépense **$650 M/an** chez Anthropic et n'a **pas de modèle propre**
- Si votre produit peut devenir une **feature gratuite** de votre fournisseur, votre moat est trop mince

**Questions pour la classe** :
- Comment Cursor peut-il se défendre ? (data flywheel, intégration multi-modèles, vitesse)
- Exemples historiques : Zoom vs Teams, Slack vs Teams — qui survit et pourquoi ?
- Votre startup est-elle dans le même risque ? Comment l'évaluer ?

---

# 14 — Quand l'IA dérape : 4 échecs à connaître

| Cas | Ce qui s'est passé | Conséquence [1] |
|-----|---------------------|-------------|
| Air Canada | Chatbot donne fausse info tarifaire | Condamné : CAD $812 |
| Grok/xAI | 3M deepfakes en 11 jours | Enquête UE, perquisition FR |
| UnitedHealth | Algo refuse soins, 90% overturned | Class action, 1,1 Mds rejets |
| Workday | 100% rejet candidats 40+ ans | Class action nationale |

- Air Canada : **"vous êtes responsable de votre chatbot"** — première jurisprudence [1]
- Workday : première fois qu'un **vendor IA** (pas l'employeur) est poursuivi [2]

> **Règle d'or** : déployez toujours avec un human-in-the-loop pour les décisions à impact.

<small>Sources : [1] [CRT Canada](https://decisions.civilresolutionbc.ca/) · [2] [Law360](https://www.law360.com/)</small>

---

<!-- _class: section -->

# Synthèse

## Votre grille de décision

---

# 15 — Grille de décision pour entrepreneurs

| Critère | Vertical SaaS | Wrapper | Open-Source | Agents |
|---------|--------------|---------|-------------|--------|
| Capital d'entrée | $500K-2M | $50-200K | $1-5M | $500K-2M |
| Temps → revenu | 12-18 mois | 3-6 mois | 18-24 mois | 18-24 mois |
| Force du moat | Très forte | Faible | Moyenne | Moyenne |
| Avantage UE | RGPD = barrière | Aucun | Mistral Apache | Giskard compliance |
| Risque #1 | Cycle vente long | Commoditisation | Monétisation | ROI flou (40% annulés) |

> Le sweet spot pour un entrepreneur européen : **Vertical SaaS** dans un secteur régulé avec données locales et compliance RGPD.

<small>Sources : [a16z](https://a16z.com/) · [Gartner](https://www.gartner.com/) · [IDC](https://www.idc.com/)</small>

---

# 16 — Les 5 tendances structurantes

1. **Cost deflation** — le coût d'inférence baisse de **10x/an** ; ce qui coûte $1 aujourd'hui coûtera $0,01 dans 2 ans [1]

2. **Moat shift** — la valeur migre des modèles vers les **données + workflows** ; les modèles se commoditisent [2]

3. **Pricing revolution** — le seat-based recule (21% → 15%), l'hybride domine (**41%**), l'outcome émerge [3]

4. **L'IA augmente, ne remplace pas** — Klarna réembauche, Doctolib garde le médecin, Duolingo perd en qualité [4]

5. **La régulation crée des marchés** — l'EU AI Act ouvre un marché de **€17 Mds** pour la compliance [5]

<small>Sources : [1] [Epoch AI](https://epochai.org/) · [2] [a16z](https://a16z.com/) · [3] [Gartner](https://www.gartner.com/) · [4] [Bloomberg](https://www.bloomberg.com/) · [5] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/)</small>

---

# 17 — Key Takeaways

1. **Le marché est massif et accélère** — $2 530 Mds de dépenses, 53% du VC mondial, 498 licornes. L'opportunité est réelle.

2. **Le pricing se réinvente** — le seat-based recule, l'hybride et l'outcome montent. Anticipez la déflation des coûts (10x/an).

3. **Le Vertical AI SaaS est le meilleur pari** — data domain-specific, NRR 120%+, TAM 10x le legacy. Harvey, Abridge, Cursor l'ont prouvé.

4. **Les moats se construisent avec les données** — pas avec le modèle. Data flywheel + switching costs + expertise domaine = défense durable.

5. **Apprenez des échecs autant que des succès** — Air Canada (responsabilité), Klarna (qualité), wrappers (85-92% d'échec). Chaque cas raconte une leçon.

> **Prochain cours** : Éthique, gouvernance et présentations finales.
