---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Business Models IA 2024–2026 · Données publiques"
---

<!-- ABOUTME: Business models de l'IA — pricing, patterns, moats, case studies et données marché 2024-2026. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : comment tarifer, quel pattern choisir, comment se défendre. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Les Business Models de l'IA

## Tarifer, structurer, défendre — le guide entrepreneur

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Le marché IA — l'opportunité

## Taille, vitesse, benchmarks

---

# 01 — Le marché IA en chiffres

- Les dépenses IA mondiales atteignent **$2 530 Mds** en 2026 (+44% YoY) [1]
- L'IA capte **53%** de tout le Venture Capital en H1 2025 — $238 Mds sur l'année [2]
- Le marché enterprise LLM double à **$8,4 Mds** en 6 mois [3]
- **88%** des entreprises ont adopté l'IA générative (vs 55% en 2023) [1]
- Les mega-rounds ($100M+) représentent **79%** du financement IA [2]

> Le marché IA croît plus vite que le cloud, le mobile et le SaaS à des stades comparables.

<small>Sources : [1] [Gartner](https://www.gartner.com/en/newsroom) · [2] [Crunchbase](https://news.crunchbase.com/) · [3] [Menlo Ventures](https://menlovc.com/2024-the-state-of-generative-ai-in-the-enterprise/)</small>

---

# 02 — Revenue benchmarks & unicorns

| Entreprise | Pays | ARR (2025) | Temps → $100M ARR |
|------------|------|-----------|-------------------|
| OpenAI | 🇺🇸 USA | ~$20 Mds | ~18 mois |
| Anthropic | 🇺🇸 USA | ~$9 Mds | ~12 mois |
| Cursor | 🇺🇸 USA | ~$1 Mds | 12 mois (record) |
| Midjourney | 🇺🇸 USA | $500 M | ~14 mois |
| ElevenLabs | 🇬🇧 UK | $330 M | ~18 mois |
| Mistral AI | 🇫🇷 France | ~$100 M | ~20 mois |
| Harvey | 🇺🇸 USA | ~$195 M | ~15 mois |

- **~498 unicorns IA** pour une valeur cumulée de **$2 700 Mds** [1]

<small>Sources : [1] [Sacra](https://sacra.com/) · [CNBC](https://www.cnbc.com/) · [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: section -->

# Comment tarifer l'IA

## Du seat au outcome

---

# 03 — Token-based pricing & cost deflation

Le coût d'inférence chute à une vitesse sans précédent :

- GPT-4 equivalent : **$20 → $0,40** par million de tokens en 3 ans (**50x**) [1]
- Rythme médian post-2024 : **200x/an** de baisse (vs 50x/an avant) [1]
- Marché segmenté : frontier ($3-15/M tokens) vs economy ($0,03-0,40/M tokens)
- **49%** des entreprises IA utilisent déjà un pricing hybride [2]

> Chaque trimestre, le même output coûte moins cher. Votre pricing doit anticiper cette déflation.

<small>Sources : [1] [Epoch AI](https://epochai.org/data/notable-ai-models) · [2] [a16z](https://a16z.com/ai-pricing-playbook/)</small>

---

# 04 — De la licence seat à l'outcome-based

| Modèle | Part 2024 → 2025 | Exemple | Prix |
|--------|-------------------|---------|------|
| Seat-based | 21% → **15%** | GitHub Copilot | $19-39/user/mois |
| Hybride | 27% → **41%** | Cursor | $20/mois + crédits |
| Outcome-based | Émergent | Intercom Fin | $0,99/résolution |
| Per-action | Émergent | Salesforce | $0,10/action |

- Intercom : **$0,99/résolution** vs $39/seat humain → adoption **+40%** [1]
- D'ici 2030, **40%+** des dépenses SaaS passeront à l'usage/outcome [2]
- Défi : **47%** des acheteurs peinent à définir des outcomes mesurables [2]

<small>Sources : [1] [Intercom](https://www.intercom.com/fin) · [2] [Gartner](https://www.gartner.com/en/newsroom)</small>

---

<!-- _class: cols -->

# 05 — Spotlight : Klarna

<div class="left">

- **$2,81 Mds** de CA (2024, +24% YoY) [1]
- **40%** de réduction d'effectifs (5 527 → 3 422) [1]
- IA gère **62%** du service client (= 700 FTE) [2]
- **$40 M** d'économies annuelles, ROI 13-20x [2]

</div>
<div class="right">

- CEO : *"cost was a too predominant factor"* [1]
- Qualité en baisse → **réembauche d'humains** en 2025
- H1 2025 : **$152 M de perte** malgré les économies IA
- Leçon : **augmentation > remplacement total**

</div>

<small>Sources : [1] [Klarna SEC F-1](https://www.sec.gov/) · [2] [OpenAI Case Study](https://openai.com/customer-stories/klarna)</small>

---

# 06 — Discussion : Tarifer votre produit IA

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

# Les patterns de business model

## 7 familles pour entreprendre en IA

---

# 07 — Vue d'ensemble : 7 familles de business models

| Pattern | Exemple | Métrique clé |
|---------|---------|-------------|
| Vertical AI SaaS | Harvey (legal) | $195 M ARR, $8 Mds val. |
| AIaaS (plateforme) | Databricks | $4,8 Mds ARR |
| Wrappers | Jasper, Copy.ai | 85-92% de taux d'échec |
| Open-Source | Mistral, Llama | Distribution → conversion |
| Embedded AI | Microsoft Copilot | +20-37% d'uplift prix |
| Agents autonomes | Sierra, Salesforce | $7,8 Mds → $50 Mds (2030) |
| Digital Labor | Klarna AI, Cursor | $3 340 Mds cumulés d'ici 2030 |

> Chaque pattern a un profil risque/rendement distinct. Le choix dépend de votre capital et votre timeline.

<small>Sources : [a16z](https://a16z.com/) · [IDC](https://www.idc.com/) · [Gartner](https://www.gartner.com/)</small>

---

# 08 — Vertical AI SaaS — la mine d'or

Le Vertical AI SaaS cible un secteur précis avec des données domain-specific :

- **Harvey** (legal) : $195 M ARR, $8 Mds val. — contrats et recherche juridique [1]
- **Abridge** (santé) : $100 M ARR, $5,3 Mds val. — transcription clinique [1]
- **Kling AI** (vidéo) : $240 M ARR en 10 mois — génération vidéo [2]

Pourquoi ça marche :
- TAM **10x** plus grand que le SaaS legacy du même secteur
- Net Revenue Retention **120%+** (expansion naturelle)
- **Data domain-specific** = moat que les généralistes ne peuvent pas copier

<small>Sources : [1] [Bloomberg](https://www.bloomberg.com/) · [2] [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: cols -->

# 09 — Spotlight : Cursor

<div class="left">

- **$0 → $1 Mds ARR** en 24 mois (+9 900% YoY) [1]
- **$29,3 Mds** val., **1M+** DAU, 50%+ Fortune 500 [1]
- 4 fondateurs MIT, **~150 pers.**, $0 marketing
- Fork VS Code → **0 friction** de migration

</div>
<div class="right">

- **Marge brute négative** : $650 M/an à Anthropic [2]
- Pas de modèle propre → dépendance fournisseur totale
- Anthropic (Claude Code) et OpenAI sont concurrents
- Leçon : **croissance ≠ rentabilité** en AI-native SaaS

</div>

<small>Sources : [1] [CNBC](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) · [2] [Foundamental](https://www.foundamental.com/)</small>

---

# 10 — AIaaS, Wrappers & Open-Source

**AIaaS** — les plateformes d'infrastructure IA :
- Marché de **$8,4 Mds** (mid-2025), dominé par AWS Bedrock, Azure AI, GCP Vertex [1]
- Modèle consumption-based (Databricks : $4,8 Mds ARR, +55% YoY) [1]

**Wrappers** — le piège de la commoditisation :
- **85-92%** échouent dans les 5 ans [2]
- 8 000+ assistants d'écriture IA : seulement **10-15** génèrent du revenu significatif [2]

**Open-Source** — l'arme de distribution :
- Llama (Meta) : **1,2 Mds+** de téléchargements, Apache 2.0 [3]
- Mistral : open-weight → adoption dev → conversion enterprise

<small>Sources : [1] [Menlo Ventures](https://menlovc.com/) · [2] [a16z](https://a16z.com/) · [3] [Hugging Face](https://huggingface.co/meta-llama)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Mistral AI

<div class="left">

- **~$14 Mds** val., **$100 M** revenue, **25x** YoY [1]
- **$3 Mds+** levés, **600+** employés [1]
- API (Large 3, Medium 3) + Le Chat + Ministral
- Medium 3 : **$0,40/$2** vs GPT-4o **$5/$15** → **10x−** [2]

</div>
<div class="right">

- Open-weight (Apache 2.0) → funnel vers API commerciale
- **Seul** frontier provider avec hébergement natif UE [2]
- Contrat armée française, ASML investisseur
- Moat : **souveraineté + régulation** = avantage

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-ai-raises-1-7-b-to-accelerate-technological-progress-with-ai) · [2] [CNBC](https://www.cnbc.com/)</small>

---

# 12 — Agents, Embedded AI & Digital Labor

**Agents autonomes** — la prochaine vague :
- Marché de **$7,8 Mds** (2025) → **$50,3 Mds** (2030), CAGR 45,8% [1]
- Sierra : $100 M ARR en 21 mois, $10 Mds val. [2]
- Attention : **40%** des projets agents annulés d'ici 2027 (valeur floue) [1]

**Embedded AI** — l'IA dans les produits existants :
- Microsoft 365 Copilot : **$30/user/mois** d'uplift sur licence existante [2]
- Uplift prix de **20-37%** pour les incumbents qui intègrent l'IA [2]

**Digital Labor** — l'IA comme "employé" :
- **$3 340 Mds** de dépenses cumulées d'ici 2030 [1]

<small>Sources : [1] [IDC](https://www.idc.com/) · [2] [Bloomberg](https://www.bloomberg.com/)</small>

---

# 13 — Discussion : Quel pattern pour votre startup ?

> Vous avez **300K€**, une **équipe de 3**, et 12 mois de runway. Quel pattern choisissez-vous ?

| Pattern | Capital requis | Temps → $1M ARR | Moat | Risque |
|---------|---------------|-----------------|------|--------|
| Vertical SaaS | $500K-2M | 12-18 mois | Fort | Cycle de vente long |
| Wrapper | $50-200K | 3-6 mois | Faible | Commoditisation |
| Agents | $500K-2M | 18-24 mois | Moyen | Projets annulés (40%) |
| Embedded AI | $200K-1M | 6-12 mois | Moyen | Dépendance plateforme |

**Questions pour la classe** :
- Le wrapper est rapide mais fragile : dans quel cas vaut-il le coup ?
- Comment un vertical SaaS se finance-t-il avec seulement 300K€ ?

---

<!-- _class: section -->

# Construire des moats

## Défendre sa position en IA

---

# 14 — Les moats de l'IA : taxonomie

| Moat | Durabilité | Exemple |
|------|-----------|---------|
| Data propriétaire | ★★★★★ | Tempus (5M dossiers patients) |
| Network effects | ★★★★★ | Hugging Face (2M+ modèles) |
| Switching costs | ★★★★☆ | Cursor (workflows intégrés) |
| Expertise domaine | ★★★★☆ | Harvey (legal AI) |
| Régulation | ★★★★☆ | Mistral (hébergement UE) |
| Échelle compute | ★★★☆☆ | OpenAI ($57 Mds levés) |
| Marque / confiance | ★★★☆☆ | Anthropic ("responsible AI") |

> Les moats les plus durables sont basés sur les **données** et les **effets de réseau**. Le modèle seul n'est plus un moat.

<small>Sources : [a16z](https://a16z.com/data-moats/) · [Bessemer](https://www.bvp.com/)</small>

---

# 15 — Data moats & flywheel effects

Le data flywheel : **plus d'utilisateurs → plus de données → meilleur produit → plus d'utilisateurs**

- **Cursor** : 1M+ DAU → chaque keystroke alimente le fine-tuning → Composer propriétaire [1]
- **OpenAI** : 900M WAU, **2,5 Mds+** de prompts/jour = données RLHF massives [2]
- **Midjourney** : 600M+ images générées → apprentissage des préférences esthétiques [2]

Mais attention au "data moat = empty promise" (a16z, 2019) :
- Les données ne sont un moat que si elles sont **uniques**, **croissantes**, et **intégrées au produit**
- Des données génériques (web scraping) ne constituent pas un avantage défendable

<small>Sources : [1] [Sacra](https://sacra.com/c/cursor/) · [2] [Sherwood News](https://sherwood.news/)</small>

---

<!-- _class: cols -->

# 16 — Spotlight : DeepSeek

<div class="left">

- **$5,6 M** de training (V3) vs $100 M+ pour GPT-4 [1]
- **~200 personnes** vs 3 500 chez OpenAI [1]
- MoE : **671 Mds** params, **37 Mds** actifs/token [1]
- Licence **MIT** — open-source complet

</div>
<div class="right">

- **$1 000 Mds** effacés des marchés US en 1 jour [2]
- Efficience > échelle : le "Jevons paradox" de l'IA
- Risque géopolitique : ban Italie, enquêtes RGPD
- Leçon : **la disruption vient du coût**

</div>

<small>Sources : [1] [DeepSeek](https://api-docs.deepseek.com/news/news250120) · [2] [CNN](https://www.cnn.com/business)</small>

---

# 17 — Discussion : Construire la défensibilité

> Votre startup IA de recrutement atteint **$500K ARR**. OpenAI annonce une feature "Hiring Assistant" dans ChatGPT Enterprise. Que faites-vous ?

**Questions pour la classe** :
- Quels moats avez-vous déjà construits à $500K ARR ? (data candidats ? intégrations ATS ?)
- La réponse "on pivote" est-elle réaliste avec 12 mois de runway ?
- Comment Cursor se défend-il face au même risque (Claude Code, Windsurf) ?
- **Règle** : si votre produit peut devenir une feature gratuite de votre fournisseur, votre moat est trop mince

---

<!-- _class: section -->

# Synthèse

## Ce que ça change pour vous

---

# 18 — Les 5 tendances structurantes

1. **Cost deflation** — le coût d'inférence baisse de **10x/an** ; ce qui coûte $1 aujourd'hui coûtera $0,01 dans 2 ans [1]

2. **Moat shift** — la valeur migre des modèles vers les **données + workflows** ; les modèles se commoditisent [2]

3. **Pricing revolution** — le seat-based recule (21% → 15%), l'hybride domine (**41%**), l'outcome émerge [3]

4. **Régulation = créateur de marché** — l'EU AI Act crée de la demande pour la compliance (Giskard, Mistral on-prem) [2]

5. **Warning Klarna** — l'IA augmente, ne remplace pas. Les entreprises qui coupent trop vite **réembauchent** [3]

<small>Sources : [1] [Epoch AI](https://epochai.org/) · [2] [a16z](https://a16z.com/) · [3] [Gartner](https://www.gartner.com/)</small>

---

# 19 — Grille de décision pour entrepreneurs

| Critère | Vertical SaaS | Wrapper | Open-Source | Agents |
|---------|--------------|---------|-------------|--------|
| Capital d'entrée | $500K-2M | $50-200K | $1-5M | $500K-2M |
| Temps → revenu | 12-18 mois | 3-6 mois | 18-24 mois | 18-24 mois |
| Force du moat | ★★★★★ | ★☆☆☆☆ | ★★★☆☆ | ★★★☆☆ |
| Avantage UE | RGPD = barrière | Aucun | Mistral Apache | Giskard compliance |
| Risque #1 | Cycle vente long | Commoditisation | Monétisation | ROI flou (40% annulés) |

> Le sweet spot pour un entrepreneur européen : **Vertical SaaS** dans un secteur régulé (santé, legal, finance) avec données locales et compliance RGPD.

<small>Sources : [a16z](https://a16z.com/) · [Gartner](https://www.gartner.com/) · [IDC](https://www.idc.com/)</small>

---

# 20 — Key Takeaways

1. **Le marché est massif et accélère** — $2 530 Mds de dépenses, 53% du VC mondial, 498 unicorns. L'opportunité est réelle.

2. **Le pricing se réinvente** — le seat-based recule au profit de l'hybride et l'outcome. Anticipez la déflation des coûts (10x/an).

3. **Le Vertical AI SaaS est le meilleur pari** — data domain-specific, NRR 120%+, TAM 10x le legacy. Harvey, Abridge, Cursor l'ont prouvé.

4. **Les moats se construisent avec les données** — pas avec le modèle. Data flywheel + switching costs + expertise domaine = défense durable.

5. **L'Europe a des cartes à jouer** — Mistral (souveraineté), Giskard (compliance), RGPD comme moat. La régulation est un avantage, pas un frein.

> **Prochain cours** : comment cadrer et piloter un projet IA — du CRISP-DM à l'AI Canvas.
