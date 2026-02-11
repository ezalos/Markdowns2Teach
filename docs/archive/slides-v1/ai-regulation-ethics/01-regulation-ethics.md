---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Régulation & Éthique IA 2024–2026 · Sources publiques"
---

<!-- ABOUTME: Panorama de la régulation, de l'éthique et de la gouvernance de l'IA — EU AI Act, approches mondiales, risques concrets et frameworks. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : naviguer le labyrinthe réglementaire comme avantage compétitif, pas comme contrainte. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Régulation, Éthique & Gouvernance de l'IA

## Naviguer le labyrinthe réglementaire en tant qu'entrepreneur

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Pourquoi la régulation IA concerne les entrepreneurs

Trois questions à se poser **avant** de lancer un produit IA :

1. **Combien ça coûte ?** — La conformité EU AI Act représente **€160K–330K** par système high-risk [1]
2. **Où peut-on vendre ?** — L'EU AI Act s'applique à toute IA dont l'output est **utilisé dans l'UE**, même depuis les US [2]
3. **C'est un moat ou un mur ?** — Le marché de la conformité IA atteint **€17 Mds** d'ici 2030 [1]

> **Amendes** : jusqu'à **€35M ou 7%** du CA mondial pour les pratiques interdites. C'est plus sévère que le RGPD.

**Questions** : Connaissez-vous la catégorie de risque de votre projet IA ? Avez-vous budgété la conformité ?

<small>Sources : [1] [European Parliament](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) · [2] [EU AI Act Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

# 02 — Vue d'ensemble : le paysage réglementaire mondial

| Régulation | Juridiction | Statut | Approche |
|------------|-------------|--------|----------|
| **EU AI Act** | UE 27 | En vigueur (août 2024) | Horizontale, 4 niveaux de risque |
| **Trump EOs** | USA | Actif (2025) | Déréglementation, préemption états |
| **Chine (3 lois)** | Chine | En vigueur (2022-2023) | Contrôle étatique, CCP-aligned |
| **OECD AI Principles** | 47 pays | Mis à jour mai 2024 | Volontaire, soft law |
| **ISO/IEC 42001** | International | Publié nov. 2023 | Certifiable, management system |
| **NIST AI RMF** | USA | Publié 2023 | Volontaire, 4 fonctions |
| **RGPD + IA** | UE 27 | En vigueur | Données perso dans l'IA |

> **Tendance** : l'UE régule par la loi, les US par les tribunaux, la Chine par le Parti.

<small>Sources : [1] [OECD](https://oecd.ai/en/ai-principles) · [2] [ISO](https://www.iso.org/standard/81230.html) · [3] [NIST](https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence)</small>

---

<!-- _class: section -->

# L'Europe en première ligne

## EU AI Act, AI Office, sandboxes

---

# 03 — EU AI Act : les 4 niveaux de risque

**Pyramide de risque** (du plus au moins encadré) :

| Niveau | Exemples | Obligation |
|--------|----------|------------|
| 🚫 **Interdit** | Social scoring, manipulation subliminale, biométrie temps réel | Banni dès fév. 2025 |
| ⚠️ **High-risk** | Recrutement IA, scoring crédit, diagnostic médical | Conformité complète, audit |
| ℹ️ **Limited** | Chatbots, deepfakes, reconnaissance d'émotion | Transparence obligatoire |
| ✅ **Minimal** | Filtres spam, IA dans les jeux vidéo | Aucune obligation |

**Attention** : **18–50%** des systèmes IA pourraient être "high-risk" — bien au-delà de l'estimation initiale de la Commission (5–15%) [1]

<small>Sources : [1] [European Parliament](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) · [2] [EU AI Act Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

# 04 — EU AI Act : coûts, calendrier et open-source

**Calendrier d'application progressive** :

| Date | Obligation |
|------|-----------|
| Fév. 2025 | Pratiques interdites + AI literacy |
| Août 2025 | Obligations GPAI + gouvernance |
| Août 2026 | Systèmes high-risk + pénalités |
| Août 2027 | High-risk dans produits régulés |

**Coûts** : **€160K–330K** par système + **€52K/an** pour l'évaluation de conformité continue [1]

**Open-source** : modèles <10²⁵ FLOPs exemptés de documentation technique **si** : licence libre, poids publics, non monétisé. Pas d'exemption pour les modèles à risque systémique [2]

**Digital Omnibus Act** (nov. 2025) : +16-24 mois pour high-risk, seuil PME élargi à 750 employés [3]

<small>Sources : [1] [CEPS](https://www.ceps.eu/) · [2] [EU AI Act Art. 53](https://eur-lex.europa.eu/eli/reg/2024/1689) · [3] [EC COM(2025) 836](https://digital-strategy.ec.europa.eu/)</small>

---

<!-- _class: cols -->

# 05 — Spotlight : European AI Office

<div class="left">

- **140+** employés, 5 unités, budget **€46,5M** [1]
- Amendes GPAI : jusqu'à **3%** du CA mondial
- Dirigée par **Lucilla Sioli** (PhD, DG CONNECT)
- Compétence exclusive sur les modèles GPAI

</div>
<div class="right">

- Budget critiqué : €46,5M vs. UK AISI £100M [2]
- Enforcement GPAI débute **août 2026**
- Coordination avec **27 autorités nationales**
- MEP Axel Voss critique le sous-effectif

</div>

<small>Sources : [1] [EU AI Office](https://digital-strategy.ec.europa.eu/en/policies/ai-office) · [2] [European Parliament](https://www.europarl.europa.eu/)</small>

---

# 06 — GPAI, Sandboxes & Code of Practice

**Modèles GPAI — deux seuils** :

- **>10²³ FLOPs** : obligations de transparence + politique copyright
- **>10²⁵ FLOPs** : classification **risque systémique** → tests adversariaux, red-teaming, incident reporting

**Code of Practice** (juillet 2025) :
- **26+ signataires** : Amazon, Anthropic, Google, Microsoft, OpenAI, Mistral [1]
- **Meta a refusé** de signer (Joel Kaplan : "overreach")
- Crée une "présomption de conformité" — pas obligatoire mais stratégique

**Sandboxes réglementaires** (Art. 57) :
- Obligatoires dans **chaque État membre** d'ici août 2026 [2]
- **Accès gratuit** pour PME et startups
- Participation de bonne foi = **safe harbor** contre les amendes

<small>Sources : [1] [Code of Practice](https://code-of-practice.ai/) · [2] [EU AI Act Art. 57-59](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

# 07 — Discussion : l'EU AI Act — contrainte ou avantage compétitif ?

> **Scénario** : vous lancez un outil IA de **screening RH** qui analyse les CV et classe les candidats. L'outil est déployé en France et en Allemagne.

**Vos données** :
- Conformité EU AI Act : **~€330K** (système high-risk, Annex III)
- 33% des startups IA européennes sont dans des catégories high-risk
- Un concurrent US ne se conforme pas et ne peut pas vendre en UE

**Questions pour la classe** :

- Le coût de conformité (€330K) est-il un **mur** ou un **moat** ?
- Un concurrent non-conforme qui entre quand même en UE — quel risque ?
- Comment financer la conformité ? (Sandbox gratuit, aides BPI, investisseurs ?)

---

<!-- _class: section -->

# Le monde se fragmente

## USA, Chine, standards internationaux

---

# 08 — USA : les Trump EOs de 2025

| EO | Date | Contenu clé |
|----|------|-------------|
| **14179** | Jan. 2025 | "Removing Barriers" — annule l'EO Biden 14110 dès le premier jour [1] |
| **14319** | Juil. 2025 | "Preventing Woke AI" — interdit biais idéologique dans l'IA fédérale |
| **14365** | Déc. 2025 | Préemption fédérale — bloque les lois IA étatiques "onéreuses" |

- DOJ AI Litigation Task Force créée pour poursuivre les abus IA
- **$42,45 Mds** de fonds BEAD conditionnés au non-enforcement des lois IA étatiques
- **Exception** : la sécurité des enfants est **explicitement exemptée** de la préemption [2]

> **Paradoxe** : Washington dérégule, mais NYC, Colorado et California légifèrent quand même.

<small>Sources : [1] [White House](https://www.whitehouse.gov/presidential-actions/) · [2] [Federal Register](https://www.federalregister.gov/documents/2025/12/16/2025-23092/ensuring-a-national-policy-framework-for-artificial-intelligence)</small>

---

# 09 — Chine : le contrôle étatique de l'IA

**Trois réglementations en cascade** :

| Loi | Date | Cible |
|-----|------|-------|
| Algorithmic Recommendation | Mars 2022 | Algorithmes de recommandation — licensing, opt-out utilisateurs |
| Deep Synthesis | Jan. 2023 | Deepfakes — watermarks obligatoires, consentement biométrique |
| Generative AI Interim | Août 2023 | LLMs — contenu aligné "valeurs socialistes", filing CAC |

**Spécificités** :
- **Enregistrement réel** obligatoire pour tous les services algorithmiques [1]
- Évaluations de sécurité pour tout service ayant une "influence sur l'opinion publique"
- AI Labeling Standard (sept. 2025) : étiquetage obligatoire des contenus IA
- Le contenu ne doit pas "porter atteinte à la sécurité de l'État ou à l'unité nationale"

> **Pour un entrepreneur** : accéder au marché chinois = se soumettre à la censure du contenu.

<small>Sources : [1] [DigiChina/Stanford](https://digichina.stanford.edu/) · [2] [ChinaLawTranslate](https://www.chinalawtranslate.com/)</small>

---

# 10 — Standards internationaux

| Standard | Type | Adhérents | Caractéristique clé |
|----------|------|-----------|---------------------|
| **OECD AI Principles** | Volontaire | 47 pays | 5 principes : croissance inclusive, transparence, accountability [1] |
| **ISO/IEC 42001** | Certifiable | 76% des orgs planifient l'adoption | Premier standard certifiable AI Management System [2] |
| **NIST AI RMF** | Volontaire | USA | 4 fonctions : Govern, Map, Measure, Manage [3] |
| **AISI Network** | Coopération | 10 pays (dont FR) | Lancé nov. 2024 — sécurité des modèles frontier |
| **Safety Report 2026** | Académique | International | Dirigé par Yoshua Bengio — base pour la gouvernance |

> **Tendance** : le UK et les US ont rebaptisé leurs instituts en retirant le mot "safety" — signal politique.

<small>Sources : [1] [OECD](https://oecd.ai/en/ai-principles) · [2] [ISO](https://www.iso.org/standard/81230.html) · [3] [NIST](https://www.nist.gov/artificial-intelligence)</small>

---

# 11 — Discussion : où construire votre startup IA ?

> **Scénario** : vous créez une startup IA qui fait de la **modération de contenu automatisée**. Vous devez choisir votre juridiction principale.

| Critère | 🇪🇺 UE | 🇺🇸 USA | 🇨🇳 Chine |
|---------|--------|---------|-----------|
| Cadre légal | Strict, prévisible | Déréglementation, états fragmentés | Contrôle étatique total |
| Sandbox | Gratuit, obligatoire 2026 | Inexistant fédéral | Existant mais opaque |
| Accès marché | 450M consommateurs | 330M, pas de loi fédérale | 1,4 Mds, censure obligatoire |
| Data privacy | RGPD stricte | Pas de loi fédérale | Cybersecurity Law |
| Coût compliance | €160K–330K high-risk | Variable par état | Opaque, risque politique |

**Questions pour la classe** :

- Quel marché choisiriez-vous en premier ? Pourquoi ?
- Peut-on être conforme partout simultanément ?

---

<!-- _class: section -->

# Les risques concrets

## Biais, enfants, copyright, environnement

---

# 12 — AI Bias : le risque juridique n°1

**Mobley v. Workday (2025)** — première class action nationale sur le biais IA [1] :
- **1,1 milliard** de candidatures rejetées potentiellement concernées
- Le tribunal a jugé les **fournisseurs IA directement responsables** (agents des employeurs)
- "Des centaines de millions" de membres potentiels dans la classe

**Autres signaux** :
- **Amazon** a abandonné son outil de recrutement IA en 2018 (biais de genre irréparable)
- **NYC Local Law 144** : audit de biais obligatoire, **$10K–50K/an** par outil [2]
- **Colorado SB 205** (juin 2026) : obligations de prévention + disclosure au Procureur sous 90 jours [3]

> **Pour un entrepreneur** : si votre IA touche au recrutement, au crédit ou à l'assurance, le biais est votre **risque juridique n°1**.

<small>Sources : [1] [Bloomberg Law](https://news.bloomberglaw.com/) · [2] [NYC](https://www.nyc.gov/) · [3] [Colorado](https://leg.colorado.gov/bills/sb24-205)</small>

---

<!-- _class: cols -->

# 13 — Spotlight : Character.AI — quand l'IA menace les enfants

<div class="left">

- Sewell Setzer, 14 ans — suicide après interactions prolongées (fév. 2024)
- Procès landmark par sa mère Megan Garcia (oct. 2024) [1]
- **SB 243** (CA) : **$1K/violation** + frais d'avocat
- **GUARD Act** : interdirait compagnons IA aux **<18 ans** [2]

</div>
<div class="right">

- Character.AI : **teens bannis** (nov. 2025)
- **42+ procureurs généraux** → lettre à 13 entreprises (déc. 2025)
- **FTC** : enquête Section 6(b) sur 7 entreprises [3]
- Sécurité enfants = seule catégorie **exemptée** de la préemption Trump

</div>

<small>Sources : [1] [CA Gov](https://www.gov.ca.gov/) · [2] [US Congress S.3062](https://www.congress.gov/) · [3] [FTC](https://www.ftc.gov/)</small>

---

# 14 — Copyright, Deepfakes & Contenu Synthétique

**Copyright — les procès qui dessinent le droit** :
- **NYT v. OpenAI** : en cours, juge ordonne divulgation de 20M de logs ChatGPT (jan. 2026) [1]
- **Thomson Reuters v. Ross** : premier rejet du fair use pour l'entraînement IA (fév. 2025)
- **Getty v. Stability AI** : UK High Court — contrefaçon de marque limitée (nov. 2025) [2]
- **Opt-out** : Directive DSM Art. 4 — robots.txt ou TDMRep pour refuser le text mining

**Deepfakes & contenu synthétique** :
- **EU AI Act Art. 50** (août 2026) : marquage machine-readable obligatoire des contenus IA [3]
- **C2PA** v2.3 (2025) : **200+ membres** (Adobe, Microsoft, Google, Meta, OpenAI, BBC) [4]
- Les deployers doivent révéler les deepfakes **dès la première exposition**

<small>Sources : [1] [NYT](https://www.nytimes.com/) · [2] [UK Courts](https://www.judiciary.uk/) · [3] [EU AI Act Art. 50](https://eur-lex.europa.eu/eli/reg/2024/1689) · [4] [C2PA](https://c2pa.org/)</small>

---

<!-- _class: cols -->

# 15 — Spotlight : impact environnemental de l'IA

<div class="left">

- Data centers : **945 TWh** d'ici 2030 [1]
- Google : émissions **+50%** en 5 ans [2]
- Microsoft : électricité **x3** (10,8M → 29,8M MWh)
- Eau : **731M–1,1 Mds m³/an** projetés [3]

</div>
<div class="right">

- **GPAI energy reporting** obligatoire dès **août 2025** (Art. 53)
- **EU EED** : data centers ≥500 kW → rapport annuel PUE, WUE
- Green AI (pruning, quantization) → **50–70%** d'économies [4]
- Documentation conservée **10 ans**

</div>

<small>Sources : [1] [IEA](https://www.iea.org/) · [2] [Google](https://sustainability.google/) · [3] [Nature Sustainability](https://www.nature.com/natsustain/) · [4] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 16 — Export Controls : la géopolitique des puces

**La bataille des semiconducteurs IA** :

| Action | Date | Impact |
|--------|------|--------|
| Biden AI Diffusion Rule | Jan. 2025, annulé mai 2025 | Système 3 tiers, seuil 10²⁶ FLOPs [1] |
| Trump replacement | Jan. 2026 | Tarif **25%** sur puces IA (H200, MI325X), review case-by-case Chine |
| ASML | Actif | Interdiction d'exporter la lithographie **EUV** vers la Chine [2] |
| Taiwan entity list | Juin 2025 | Huawei et SMIC ajoutés |
| **EU Chips Act** | En cours | "Autonomie stratégique" — réduire la dépendance US |

**Pour un entrepreneur** :
- Le seuil **10²⁵ FLOPs** (EU) / **10²⁶ FLOPs** (US) détermine qui est régulé
- Les startups US sont exemptées du tarif sur les puces
- L'accès aux GPUs de pointe est un enjeu géopolitique direct

<small>Sources : [1] [BIS/Commerce Dept](https://www.bis.gov/) · [2] [ASML](https://www.asml.com/)</small>

---

# 17 — Discussion : quel risque anticiperiez-vous ?

> **Scénario** : votre startup IA propose **trois produits** :

| Produit | Description | Marché |
|---------|-------------|--------|
| **A** | Screening CV automatisé | France, Allemagne |
| **B** | Génération de contenu marketing | UE + USA |
| **C** | Prévision de consommation énergétique | France |

**Questions pour la classe** :

- Classez les 3 produits par **niveau de risque réglementaire** (EU AI Act)
- Quel produit lanceriez-vous **en premier** et pourquoi ?
- Le produit A est-il viable sans un budget conformité de €330K ?
- Le produit B risque-t-il des poursuites copyright (NYT v. OpenAI) ?

---

<!-- _class: section -->

# Gouvernance en pratique

## Frameworks, secteurs, auto-régulation

---

# 18 — Responsible AI : les frameworks d'entreprise

| Entreprise | Approche | Fait marquant |
|------------|----------|---------------|
| **Microsoft** | 6 principes, ORA | **67** red-teams en 2024 [1] |
| **Google** | 7 AI Principles, Frontier Safety v3.0 | Critical Capability Levels [2] |
| **Anthropic** | Responsible Scaling Policy v2.2 | **ASL-3** activé mai 2025 [3] |
| **Meta** | Équipe RAI **dissoute** nov. 2023 | Open-source : LlamaFirewall, Llama Guard 4 |

**Outils open-source** : IBM **AIF360** (70+ métriques fairness), Microsoft **Fairlearn** (post-processing + viz)

> Meta a refusé le Code of Practice GPAI **et** dissous son équipe RAI — signal contradictoire.

<small>Sources : [1] [Microsoft](https://www.microsoft.com/en-us/ai/principles-and-approach) · [2] [Google](https://deepmind.google/discover/blog/) · [3] [Anthropic](https://www.anthropic.com/responsible-scaling-policy)</small>

---

# 19 — Régulation sectorielle : santé & finance

**Santé — triple couche réglementaire** :
- **FDA** : cadre AI/ML pour dispositifs médicaux, protocole de mise à jour continue [1]
- **EU MDR + AI Act** : un dispositif médical IA = high-risk sous les **deux** régulations
- Transposition deadline : **décembre 2026**
- Enjeu : les algorithmes évoluent mais la certification est statique

**Finance — multi-juridictionnelle** :
- **EU MiFID II** : pas encore de provisions IA contraignantes (guidance ESMA non-binding) [2]
- **SEC** (US) : enforcement "AI washing" — Delphia et Global Predictions sanctionnées
- **MAS** (Singapour) : sandbox IA pour les services financiers [3]

> **Pour un entrepreneur** : les secteurs santé et finance cumulent les couches réglementaires. Budget x2 pour la conformité.

<small>Sources : [1] [FDA](https://www.fda.gov/medical-devices/software-medical-device-samd/artificial-intelligence-and-machine-learning-aiml-software-medical-device) · [2] [ESMA](https://www.esma.europa.eu/) · [3] [MAS](https://www.mas.gov.sg/)</small>

---

# 20 — Discussion : auto-régulation ou loi dure ?

> **Scénario** : vous siégez au comité éthique IA. Un concurrent coupe les coins ronds sur les tests de biais et gagne des parts de marché.

| Option | Avantage | Risque |
|--------|----------|--------|
| **A — Loi contraignante** | Level playing field, confiance | Lent, coûteux, freine l'innovation |
| **B — Code volontaire** | Flexibilité, rapidité | Free-riders, pas d'enforcement |

**Le cas réel** : Meta a refusé le Code of Practice GPAI et dissous son équipe RAI. Google et Microsoft ont signé et investissent massivement.

**Questions pour la classe** :
- L'auto-régulation fonctionne-t-elle quand un acteur majeur refuse ?
- Le RGPD a créé un standard mondial de facto — l'EU AI Act peut-il faire pareil ?

---

<!-- _class: section -->

# Synthèse

## Naviguer le labyrinthe réglementaire

---

# 21 — Stratégies réglementaires pour entrepreneurs

**5 stratégies concrètes** :

1. **Compliance-first comme moat** — être conforme EU AI Act quand les concurrents ne le sont pas verrouille le marché européen (450M consommateurs)
2. **Sandbox dès le premier jour** — accès gratuit pour les startups, safe harbor contre les amendes, retour des régulateurs [1]
3. **Souveraineté premium** — les entreprises européennes paient plus pour du "made in EU" conforme RGPD + AI Act (Mistral, OVHcloud)
4. **Veille réglementaire US** — le patchwork étatique (NYC, Colorado, California) crée des opportunités de compliance-as-a-service [2]
5. **Green AI comme différenciateur** — le reporting environnemental est obligatoire dès août 2025, anticiper = avantage concurrentiel

> La conformité n'est pas un coût — c'est un **investissement dans l'accès au marché**.

<small>Sources : [1] [EU AI Act Art. 57-59](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [European Parliament](https://www.europarl.europa.eu/)</small>

---

# 22 — 5 faits à retenir

1. **L'EU AI Act est la première loi IA complète au monde** — en vigueur depuis août 2024, application progressive jusqu'en 2027. Amendes : jusqu'à **€35M / 7% CA** [1]

2. **Les US dérégulent mais les états résistent** — Trump a annulé l'EO Biden et tente de préempter les lois étatiques, mais NYC, Colorado et California légifèrent quand même [2]

3. **Le biais est le risque juridique n°1** — Mobley v. Workday (2025) crée un précédent : les fournisseurs IA sont **directement responsables** du biais

4. **La conformité est un marché de €17 Mds** — les outils, audits et services de compliance IA forment une industrie en explosion

5. **Le reporting environnemental IA est obligatoire dès août 2025** — les fournisseurs GPAI doivent documenter consommation énergétique et empreinte carbone [3]

<small>Sources : [1] [EU AI Act Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [White House](https://www.whitehouse.gov/presidential-actions/) · [3] [EU AI Act Art. 53](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>
