---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 5 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Données publiques"
---

<!-- ABOUTME: Session 5 — Régulation IA (EU AI Act, RGPD, global), impact sociétal, Responsible AI, veille et clôture du cours. -->
<!-- ABOUTME: Deck final du cours M2 IMT&E Paris 1 Panthéon-Sorbonne, cadré business pour non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Régulation & IA responsable

## Session 5 — Éthique, gouvernance & clôture

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Partie 1 — Régulation

## EU AI Act, RGPD et paysage mondial

---

# 01 — Pourquoi la régulation IA vous concerne

Trois questions à se poser **avant** de lancer un produit IA :

1. **Combien ça coûte ?** — La conformité EU AI Act représente **€160K–330K** par système high-risk [1]
2. **Où peut-on vendre ?** — L'EU AI Act s'applique à toute IA dont l'output est **utilisé dans l'UE**, même depuis les US [2]
3. **C'est un moat ou un mur ?** — Le marché de la conformité IA atteint **€17 Mds** d'ici 2030 [1]

> **Amendes** : jusqu'à **€35M ou 7%** du CA mondial. C'est plus sévère que le RGPD.

<small>Sources : [1] [European Parliament](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence) · [2] [EU AI Act Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

# 02 — EU AI Act : les 4 niveaux de risque

**Pyramide de risque** (du plus au moins encadré) :

| Niveau | Exemples | Obligation |
|--------|----------|------------|
| **Interdit** | Social scoring, manipulation subliminale, biométrie temps réel | Banni dès fév. 2025 |
| **High-risk** | Recrutement IA, scoring crédit, diagnostic médical | Conformité complète, audit |
| **Limited** | Chatbots, deepfakes, reconnaissance d'émotion | Transparence obligatoire |
| **Minimal** | Filtres spam, IA dans les jeux vidéo | Aucune obligation |

> **18–50%** des systèmes IA pourraient être classés "high-risk" — bien au-delà de l'estimation initiale de 5–15% [1].

<small>Sources : [1] [European Parliament](https://www.europarl.europa.eu/topics/en/article/20230601STO93804/eu-ai-act-first-regulation-on-artificial-intelligence)</small>

---

# 03 — EU AI Act : calendrier et coûts

**Application progressive** :

| Date | Obligation |
|------|-----------|
| Fév. 2025 | Pratiques interdites + AI literacy |
| Août 2025 | Obligations GPAI + gouvernance |
| Août 2026 | Systèmes high-risk + pénalités |
| Août 2027 | High-risk dans produits régulés |

**Coûts** : **€160K–330K** par système + **€52K/an** en évaluation continue [1]

**Open-source** : modèles <10²⁵ FLOPs exemptés **si** licence libre, poids publics, non monétisé [2]

<small>Sources : [1] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/) · [2] [EU AI Act Art. 53](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

<!-- _class: cols -->

# 04 — EU AI Act + RGPD : le double cadre européen

<div class="left">

**RGPD** (2018) :
- Données personnelles
- Consentement, minimisation, droit à l'oubli
- Amende max : **4% du CA mondial**
- Autorité : CNIL (France)

</div>
<div class="right">

**EU AI Act** (2024-2026) :
- Sécurité et droits fondamentaux
- Niveaux de risque, transparence, oversight
- Amende max : **7% du CA** (ou €35M)
- Autorité : AI Office (UE) + nationales

</div>

> Ce double cadre est une **barrière à l'entrée** pour les concurrents non-européens — et un **argument commercial**.

---

# 05 — Paysage mondial : EU vs US vs Chine

| Critère | UE | USA | Chine |
|---------|-----|------|-------|
| Approche | Horizontale, 4 niveaux de risque | Déréglementation Trump, états fragmentés | Contrôle étatique, CCP-aligned |
| Cadre | EU AI Act (août 2024) | EOs + patchwork étatique | 3 lois en cascade (2022-2023) |
| Sandbox | Gratuit, obligatoire 2026 | Inexistant fédéral | Existant mais opaque |
| Data privacy | RGPD stricte | Pas de loi fédérale | Cybersecurity Law |

> **Tendance** : l'UE régule par la loi, les US par les tribunaux, la Chine par le Parti [1].

<small>Sources : [1] [OECD](https://oecd.ai/en/ai-principles) · [2] [White House](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/)</small>

---

# 06 — USA : la déréglementation Trump

| EO | Date | Contenu clé |
|----|------|-------------|
| **14179** | Jan. 2025 | "Removing Barriers" — annule l'EO Biden dès le premier jour [1] |
| **14319** | Juil. 2025 | "Preventing Woke AI" — interdit biais idéologique dans l'IA fédérale |
| **14365** | Déc. 2025 | Préemption fédérale — bloque les lois IA étatiques "onéreuses" |

**Paradoxe** : Washington dérégule, mais NYC, Colorado et California légifèrent quand même [2].

**Exception** : la sécurité des enfants est **explicitement exemptée** de la préemption.

<small>Sources : [1] [White House](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/) · [2] [Federal Register](https://www.federalregister.gov/documents/2025/01/31/2025-02172/removing-barriers-to-american-leadership-in-artificial-intelligence)</small>

---

# 07 — Discussion : l'EU AI Act — contrainte ou avantage ?

> **Scénario** : vous lancez un outil IA de **screening RH** qui analyse les CV. Déployé en France et en Allemagne.

**Vos données** :
- Conformité EU AI Act : **~€330K** (système high-risk, Annex III)
- 33% des startups IA européennes se classent dans des catégories high-risk [1]
- Un concurrent US ne se conforme pas et ne peut pas vendre en UE

**Questions pour la classe** :

- Le coût de conformité (€330K) est-il un **mur** ou un **moat** ?
- Comment financer la conformité ? (Sandbox gratuit, aides BPI, investisseurs ?)
- Un concurrent non-conforme qui entre quand même en UE — quel risque ?

<small>Sources : [1] [appliedAI](https://www.appliedai.de/en/hub-en/ai-act-impact-survey)</small>

---

<!-- _class: section -->

# Les risques concrets

## Biais, enfants, copyright, environnement

---

# 08 — AI Bias : le risque juridique n°1

**Mobley v. Workday (2025)** — première class action sur le biais IA [1] :
- **1,1 milliard** de candidatures rejetées potentiellement concernées
- Le tribunal a jugé les **fournisseurs IA directement responsables**

**Autres cas** :
- **Amazon** a abandonné son outil de recrutement IA en 2018 (biais de genre irréparable) [2]
- **COMPAS** — biais racial dans les recommandations de peine pour la justice US

> **Pour un entrepreneur** : si votre IA touche au recrutement, au crédit ou à l'assurance, le biais est votre **risque juridique n°1**.

<small>Sources : [1] [Bloomberg Law](https://news.bloomberglaw.com/daily-labor-report/employers-find-openings-to-share-ai-bias-liability-with-vendors) · [2] [Reuters](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G)</small>

---

# 09 — Copyright et contenu synthétique

**Copyright — les procès qui dessinent le droit** :
- **NYT v. OpenAI** : en cours, juge ordonne divulgation de 20M de logs (jan. 2026) [1]
- **Thomson Reuters v. Ross** : premier rejet du fair use pour l'entraînement IA (fév. 2025) [4]
- **Opt-out** : Directive DSM Art. 4 — robots.txt ou TDMRep pour refuser le text mining

**Deepfakes & contenu synthétique** :
- **EU AI Act Art. 50** : marquage machine-readable obligatoire des contenus IA [2]
- **C2PA** v2.3 : **200+ membres** (Adobe, Microsoft, Google, Meta, OpenAI, BBC) [3]

> Les deployers doivent révéler les deepfakes **dès la première exposition**.

<small>Sources : [1] [NYT](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html) · [2] [EU AI Act Art. 50](https://eur-lex.europa.eu/eli/reg/2024/1689) · [3] [C2PA](https://c2pa.org/) · [4] [Loeb & Loeb](https://www.loeb.com/en/insights/publications/2025/02/thomson-reuters-v-ross-intelligence-inc)</small>

---

<!-- _class: cols -->

# 10 — Impact environnemental de l'IA

<div class="left">

**Les chiffres** :
- Data centers : **945 TWh** d'ici 2030 [1]
- Google : émissions **+50%** en 5 ans [2]
- Eau : **731M–1,1 Mds m³/an** projetés [3]

</div>
<div class="right">

**La réponse réglementaire** :
- **GPAI energy reporting** obligatoire dès août 2025
- **EU EED** : data centers ≥500 kW → rapport annuel
- Green AI (pruning, quantization) → **50–70%** d'économies [4]

</div>

> Le reporting environnemental IA est une **obligation légale**, pas un engagement RSE.

<small>Sources : [1] [IEA](https://www.iea.org/reports/electricity-2024) · [2] [Google](https://sustainability.google/reports/google-2024-environmental-report/) · [3] [Nature](https://www.nature.com/articles/d41586-024-00478-x) · [4] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 11 — Discussion : classez ces produits par risque

> **Scénario** : votre startup IA propose **trois produits** :

| Produit | Description | Marché |
|---------|-------------|--------|
| **A** | Screening CV automatisé | France, Allemagne |
| **B** | Génération de contenu marketing | UE + USA |
| **C** | Prévision de consommation énergétique | France |

**Questions pour la classe** :

- Classez les 3 produits par **niveau de risque réglementaire** (EU AI Act)
- Quel produit lanceriez-vous **en premier** et pourquoi ?
- Le produit B risque-t-il des poursuites copyright (NYT v. OpenAI) ?

---

<!-- _class: section -->

# Partie 2 — Impact sociétal

## Job displacement, Responsible AI

---

<!-- _class: compact -->

# 12 — L'IA automatise des tâches, pas des métiers

- L'IA **n'automatise pas des jobs** — elle automatise des **tâches**
- La plupart des métiers = collection de tâches variées
- Certaines tâches sont automatisables, d'autres pas du tout

| Tâche (Customer Service) | Potentiel GenAI |
|---|---|
| Répondre aux chats clients | **High** |
| Historique des interactions | **High** |
| Répondre aux appels téléphoniques | Low |
| Évaluer les réclamations complexes | Low |

> **Résultat contre-intuitif** : les métiers les **mieux payés** (>$80K/an) sont les **plus exposés** à l'IA [1].

<small>Sources : [1] [Eloundou et al., 2023](https://arxiv.org/abs/2303.10130) · Adapté de Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

# 13 — La citation à retenir

> *"AI won't replace radiologists. But radiologists that use AI will replace radiologists that don't."*
>
> — **Curtis Langlotz**, Professor of Radiology, Stanford University

En 2016, Hinton prédisait la fin des radiologues [1]. **8 ans plus tard** : +7%, et ils gagnent **mieux** [2].

S'applique à **tous les métiers** :
- L'IA ne remplacera pas les **avocats**. Mais ceux qui utilisent l'IA...
- L'IA ne remplacera pas les **marketeurs**. Mais ceux qui...
- L'IA ne remplacera pas les **entrepreneurs**. Mais...

> Le vrai risque n'est pas l'IA. C'est de ne pas l'utiliser.

<small>Sources : [1] [AuntMinnie](https://www.auntminnie.com/imaging-informatics/artificial-intelligence/article/15746014/hinton-acknowledges-mistake-in-predicting-ai-replacement-of-radiologists) · [2] [The New Republic](https://newrepublic.com/article/187203/ai-radiology-geoffrey-hinton-nobel-prediction)</small>

---

<!-- _class: cols -->

# 14 — Augmentation vs Automation

<div class="left">

**Augmentation** :
- L'IA **assiste** l'humain
- L'humain garde le contrôle
- Ex : recommander une réponse au service client pour validation

</div>
<div class="right">

**Automation** :
- L'IA **exécute** de bout en bout
- Aucune intervention humaine
- Ex : transcrire et résumer automatiquement les interactions clients

</div>

> Les entreprises commencent par l'**Augmentation** et migrent vers l'**Automation** quand la confiance est établie. Le cas **Klarna** : 700 postes de service client automatisés, résolution de 11 min à 2 min [1].

<small>Sources : [1] [Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · Adapté de Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

# 15 — Risques réels vs risques fantasmés

Les dommages causés par l'IA sont **concrets et documentés** :

| Incident | Impact |
|---|---|
| **COMPAS** (justice US) | Biais racial dans les recommandations de peine |
| **Flash Crash** (2010) | Perte de **$1T** en minutes sur les marchés [2] |
| **Character.AI** (2024) | Suicide d'un adolescent de 14 ans après interactions prolongées [1] |
| **Voitures autonomes** | Accidents mortels réels (Uber 2018, Tesla) |

> Ces risques **réels et immédiats** méritent plus d'attention que les scénarios d'extinction. L'AGI est incertaine — les biais et les accidents sont **certains**.

![w:200](assets/ng03/img-007.png) ![w:200](assets/ng03/img-008.png) ![w:200](assets/ng03/img-006.png)

<small>Sources : [1] [CA Gov](https://www.gov.ca.gov/2024/09/29/governor-newsom-announces-new-initiatives-to-advance-safe-and-responsible-ai-protect-californians/) · [2] [SEC/CFTC](https://www.sec.gov/news/studies/2010/marketevents-report.pdf) · Adapté de Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

<!-- _class: cols -->

# 16 — Les 5 dimensions du Responsible AI

<div class="left">

- **Fairness** — ne pas perpétuer ou amplifier les biais existants
- **Transparency** — décisions compréhensibles par les parties prenantes
- **Privacy** — protéger les données personnelles

</div>
<div class="right">

- **Security** — protéger les systèmes IA contre les attaques
- **Ethical Use** — s'assurer que l'IA est utilisée à des fins bénéfiques

</div>

> Pour chaque produit IA, posez-vous : *"Qu'est-ce qui pourrait mal tourner ?"* en termes de Fairness, Transparency, Privacy, Security, Ethical Use.

---

# 17 — Responsible AI : les frameworks d'entreprise

| Entreprise | Approche | Fait marquant |
|------------|----------|---------------|
| **Microsoft** | 6 principes, Office of Responsible AI | **67** red-teams en 2024 [1] |
| **Google** | 7 AI Principles, Frontier Safety v3.0 | Critical Capability Levels [2] |
| **Anthropic** | Responsible Scaling Policy v2.2 | **ASL-3** activé mai 2025 [3] |
| **Meta** | Équipe RAI **dissoute** nov. 2023 [4] | Refuse le Code of Practice GPAI |

> **Paradoxe Meta** : refuse l'auto-régulation **et** dissout son équipe RAI — tout en publiant des outils open-source (LlamaFirewall, Llama Guard 4).

<small>Sources : [1] [Microsoft](https://www.microsoft.com/en-us/ai/principles-and-approach) · [2] [DeepMind](https://deepmind.google/blog/introducing-the-frontier-safety-framework/) · [3] [Anthropic](https://www.anthropic.com/responsible-scaling-policy) · [4] [CNBC](https://www.cnbc.com/2023/11/18/facebook-parent-meta-breaks-up-its-responsible-ai-team.html)</small>

---

# 18 — Discussion : auto-régulation ou loi dure ?

> **Scénario** : vous siégez au comité éthique IA de votre startup. Un concurrent coupe les coins ronds sur les tests de biais et gagne des parts de marché.

| Option | Avantage | Risque |
|--------|----------|--------|
| **Loi contraignante** | Level playing field, confiance | Lent, coûteux, freine l'innovation |
| **Code volontaire** | Flexibilité, rapidité | Free-riders, pas d'enforcement |

**Le cas réel** : Meta a refusé le Code of Practice GPAI. Google et Microsoft ont signé.

**Questions pour la classe** :
- L'auto-régulation fonctionne-t-elle quand un acteur majeur refuse ?
- Le RGPD a créé un standard mondial de facto — l'EU AI Act peut-il faire pareil ?

---

<!-- _class: section -->

# Constitutional AI & gouvernance

## Des principes aux structures

---

# 19 — Claude's Constitution : l'IA guidée par des principes

Anthropic a publié en janvier 2026 une **constitution de 83 pages** qui définit les valeurs de Claude — pas une liste de règles, mais un document de philosophie morale [1].

**Hiérarchie de 4 priorités** (en cas de conflit, l'ordre prime) :

1. **Safe** — ne pas compromettre les mécanismes de contrôle humain
2. **Ethical** — honnêteté, bonnes valeurs, éviter les nuisances
3. **Compliant** — suivre les directives spécifiques d'Anthropic
4. **Helpful** — être utile aux utilisateurs

**Heuristique clé** : *"Comment un employé senior et réfléchi d'Anthropic réagirait-il ?"* [2]

> Publié sous licence **CC0** — n'importe quelle entreprise peut l'adopter ou l'adapter.

<small>Sources : [1] [Anthropic](https://www.anthropic.com/news/claude-new-constitution) · [2] [Anthropic Constitution](https://www.anthropic.com/constitution)</small>

---

# 20 — Dario Amodei : l'adolescence de la technologie

**Métaphore centrale** : l'humanité est un **adolescent technologique** — la puissance d'un adulte, sans la maturité institutionnelle [1].

**5 catégories de risque** :
- **Autonomy** — l'IA agit de manière désalignée (déception, manipulation)
- **Destruction** — acteurs malveillants exploitent l'IA (bioweapons)
- **Prise de pouvoir** — gouvernements ou entreprises monopolisent l'IA
- **Disruption économique** — **50%** des emplois white-collar d'entrée éliminés sous 1–5 ans
- **Concentration** — un petit nombre d'entreprises contrôle un pouvoir disproportionné

> *"A country of geniuses in a datacenter"* — les systèmes IA futurs auront la capacité collective d'un État-nation. La gouvernance d'entreprise classique n'est pas conçue pour ça.

<small>Sources : [1] [Dario Amodei](https://www.darioamodei.com/essay/the-adolescence-of-technology)</small>

---

<!-- _class: cols -->

# 21 — Le débat : Anthropic tient-elle ses promesses ?

<div class="left">

**Critiques** [1] :
- Engagement de pause RSP **retiré silencieusement**
- Lobbying contre SB-1047
- Trust (LTBT) potentiellement sans pouvoir réel
- Clauses de non-dénigrement secrètes

</div>
<div class="right">

**Défense** :
- Mission safety **fondatrice** (raison d'être)
- RSP évolue, pas abandonnée [2]
- Recherche safety **nécessite** des modèles frontier
- Gouvernance = expérimentation, pas solution finie

</div>

> **Tension clé** : la structure compte plus que l'intention. Les engagements volontaires résistent-ils à la pression commerciale ?

<small>Sources : [1] [LessWrong / AI Lab Watch](https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/) · [2] [Anthropic RSP](https://www.anthropic.com/responsible-scaling-policy)</small>

---

# 22 — Discussion : constitution IA — marketing ou engagement ?

> **Scénario** : votre startup IA publie une "constitution IA" inspirée de celle d'Anthropic. Votre investisseur applaudit la transparence. Votre CTO prévient : *"On se lie les mains face à la concurrence."*

**Questions pour la classe** :

- Publier ses principes éthiques est-il un **avantage concurrentiel** (confiance clients, recrutement) ou une **contrainte auto-imposée** ?
- Anthropic publie en CC0 — pourquoi offrir ses principes aux concurrents ?
- Si votre concurrent ignore ses propres principes publiés, quel recours avez-vous ?

---

<!-- _class: section -->

# Partie 3 — Clôture & Veille

## Ressources, récapitulatif, perspectives

---

# 23 — Votre boîte à outils de veille IA

| Catégorie | Ressource | Pourquoi |
|-----------|-----------|----------|
| Newsletter | **The Batch** (Andrew Ng) | Gratuit, hebdo, recherche traduite en pratique [1] |
| Podcast FR | **Comptoir IA** | 157+ épisodes, meetups Paris, communauté active [2] |
| YouTube | **3Blue1Brown** | Meilleure visualisation neural networks / Transformers [3] |
| Benchmark | **Chatbot Arena** | 6M+ votes, A/B blind, le plus cité par les labs [4] |
| Formation | **DeepLearning.AI** | 100+ cours gratuits, co-créés avec OpenAI/Anthropic/Google [1] |
| Radar FR | **Wavestone** | 190 startups GenAI françaises cartographiées [5] |

<small>Sources : [1] [DeepLearning.AI](https://www.deeplearning.ai/) · [2] [Comptoir IA](https://shows.acast.com/comptoir-ia) · [3] [3Blue1Brown](https://www.youtube.com/@3blue1brown) · [4] [Chatbot Arena](https://lmarena.ai/) · [5] [Wavestone](https://www.wavestone.com/en/insight/2025-radar-of-french-generative-ai-startups/)</small>

---

# 24 — Construire sa routine de veille en 30 min/jour

| Profil | Newsletter | Podcast | YouTube | Communauté |
|--------|------------|---------|---------|------------|
| Entrepreneur généraliste | The Rundown AI | Hard Fork | The AI Advantage | r/ChatGPT |
| Entrepreneur tech | Ben's Bites | No Priors | AI Explained | r/LocalLLaMA |
| Stratège / investisseur | Stratechery | No Priors | 3Blue1Brown | AlphaSignal |

**Conseil** : choisissez **1 ressource par colonne** et tenez-y pendant 1 mois avant d'ajuster.

> **Discussion** : quel profil vous correspond ? Quelles 4 ressources choisissez-vous et pourquoi ?

---

# 25 — Récapitulatif : ce que nous avons couvert

| Session | Thème | Compétence clé |
|:-------:|-------|----------------|
| **S1** | Fondamentaux & paysage IA | Distinguer AI / ML / DL / GenAI |
| **S2** | Prompt Engineering & outils no-code | Prompter efficacement, utiliser des outils sans code |
| **S3** | Cadrer un projet IA | CRISP-DM, AI Canvas, Build vs Buy |
| **S4** | Business models & stratégie | Value chain, unit economics, scaling |
| **S5** | Éthique, gouvernance & clôture | EU AI Act, Responsible AI, veille structurée |

> En 5 sessions, vous avez acquis un socle pour **évaluer, cadrer et déployer** des solutions IA en tant qu'entrepreneurs.

---

# 26 — 5 stratégies pour entrepreneurs face à la régulation

1. **Compliance-first comme moat** — être conforme EU AI Act quand les concurrents ne le sont pas verrouille le marché européen (450M consommateurs)
2. **Sandbox dès le premier jour** — accès gratuit pour startups, safe harbor contre les amendes [1]
3. **Souveraineté premium** — les entreprises européennes paient plus pour du "made in EU" conforme RGPD + AI Act
4. **Green AI comme différenciateur** — le reporting environnemental est obligatoire dès août 2025, anticiper = avantage concurrentiel
5. **Veille réglementaire continue** — le patchwork US crée des opportunités de compliance-as-a-service [2]

> La conformité n'est pas un coût — c'est un **investissement dans l'accès au marché**.

<small>Sources : [1] [EU AI Act Art. 57-59](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [European Parliament](https://www.europarl.europa.eu/thinktank/en/document/EPRS_BRI(2022)733544)</small>

---

# 27 — 5 faits à retenir de cette session

1. **L'EU AI Act** est la première loi IA complète au monde — amendes : jusqu'à **€35M / 7% CA** [1]

2. **Le biais est le risque juridique n°1** — Mobley v. Workday (2025) : les fournisseurs IA sont **directement responsables**

3. **L'IA automatise des tâches, pas des métiers** — les métiers les mieux payés sont les plus exposés, mais aussi les plus augmentés

4. **La conformité est un marché de €17 Mds** — outils, audits et services de compliance forment une industrie en explosion [1]

5. **Le reporting environnemental IA** est obligatoire dès août 2025 — les fournisseurs GPAI doivent documenter leur empreinte [2]

<small>Sources : [1] [EU AI Act Regulation 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [EU AI Act Art. 53](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Construire un monde plus intelligent

## Comprendre l'IA, penser en entrepreneur, agir en européen

Bonne continuation et bonne veille !

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026
