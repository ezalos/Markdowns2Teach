---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 5 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Données publiques"
---

<!-- ABOUTME: Session 5 — Régulation IA (EU AI Act, RGPD, paysage mondial incl. Chine), risques concrets (biais, copyright, environnement, santé), impact sociétal et clôture du cours. -->
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

1. **Combien ça coûte ?** — La conformité EU AI Act représente **€193K–330K** par système high-risk [1]
2. **Où peut-on vendre ?** — L'EU AI Act s'applique à toute IA utilisée dans l'UE, même déployée depuis les US [2]
3. **Les non-conformes sont exclus** — le marché unique EU = **450M consommateurs** inaccessibles sans conformité

> **Amendes** : jusqu'à **€35M ou 7%** du CA mondial — plus sévère que le RGPD (4%) [2].

<small>Sources : [1] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/) · [2] [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

<!-- _class: cols compact -->

# 02 — RGPD + EU AI Act : le double cadre européen

<div class="left">

**RGPD** (2018) — données personnelles :
- **Consentement** : l'utilisateur doit accepter explicitement le traitement de ses données
- **Minimisation** : ne collecter que les données strictement nécessaires
- **Droit à l'oubli** : l'utilisateur peut exiger la suppression de ses données
- Amende max : **4% du CA mondial**

</div>
<div class="right">

**EU AI Act** (2024–2027) — sécurité :
- 4 niveaux de risque (interdit → minimal)
- Transparence et oversight humain
- Amende max : **7% du CA** (ou €35M)
- Autorités : AI Office (UE) + CNIL (FR)

</div>

> Les deux cadres se **cumulent** : un outil IA utilisant des données personnelles doit respecter les deux.

<small>Sources : [1] [RGPD](https://eur-lex.europa.eu/eli/reg/2016/679) · [2] [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

<!-- _class: img-right -->

# 03 — EU AI Act : les 4 niveaux de risque

- **Interdit** — manipulation, surveillance de masse → **banni** fév. 2025
- **High-risk** — emploi, crédit, santé → conformité complète [1]
- **Limited** — chatbots, deepfakes → doivent **s'identifier comme IA** auprès de l'utilisateur
- **Minimal** — spam, jeux vidéo → aucune obligation (pas d'impact sur les droits)

> La Commission estimait **5–15%** de systèmes high-risk — appliedAI en trouve **18%** [2].

![bg right:55% contain](assets/infographics/eu-ai-act-risk-pyramid_run_20260330_144415_20c1f0.png)

<small>Sources : [1] [EU AI Act Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [appliedAI](https://www.appliedai.de/en/hub-en/ai-act-impact-survey)</small>

---

<!-- _class: compact -->

# 04 — EU AI Act : calendrier et coûts

| Date | Qui est concerné | Ce qui change |
|------|-----------------|---------------|
| Fév. 2025 | Tous | Pratiques interdites (social scoring, biométrie temps réel) |
| Août 2025 | Fournisseurs de **GPAI** (General-Purpose AI = modèles fondation comme GPT, Gemini, Mistral) | Documentation technique, reporting énergie, résumé des données d'entraînement |
| Août 2026 | Fournisseurs de systèmes **high-risk** (recrutement, crédit, santé...) | Conformité complète + les amendes s'appliquent |
| Août 2027 | High-risk **intégrés dans un produit déjà régulé** (dispositifs médicaux, machines industrielles) | Même conformité, mais délai supplémentaire car double certification (AI Act + MDR/MDR) |

**Coûts** : **€193K–330K** par système + **€71K/an** en maintenance [1]

<small>Sources : [1] [CEPS](https://www.ceps.eu/clarifying-the-costs-for-the-eus-ai-act/) · [2] [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689)</small>

---

<!-- _class: img-right -->

# 05 — Paysage mondial : 3 philosophies de régulation

- **UE** : loi horizontale, 4 niveaux de risque (2025–2027)
- **USA** : pas de loi fédérale, **600+** textes d'états en 2025 [1]. Politique IA fixée par **EOs** (Executive Orders = décrets présidentiels)
- **Chine** : 1ère loi GenAI au monde (**août 2023**), **3 739** outils enregistrés [2][3]

> L'UE régule par la **loi**, les US par les **tribunaux** et les **EOs**, la Chine par le **Parti**.

![bg right:55% contain](assets/infographics/global-regulation-comparison_run_20260330_144420_8d655e.png)

<small>Sources : [1] [NCSL](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation) · [2] [China Briefing](https://www.china-briefing.com/news/how-to-interpret-chinas-first-effort-to-regulate-generative-ai-measures/) · [3] [Trivium China](https://triviumchina.com/research/seeking-the-next-deepseek-what-chinas-generative-ai-registration-data-can-tell-us-about-chinas-ai-competitiveness/)</small>

---

<!-- _class: compact -->

# 06 — USA : déréglementation fédérale, régulation des états

| EO | Date | Impact |
|----|------|--------|
| **14179** | Jan. 2025 | Annule l'EO Biden — "Removing Barriers" [1] |
| **14319** | Juil. 2025 | Interdit "biais idéologique" dans l'IA fédérale [1] |
| **14365** | Déc. 2025 | Préemption fédérale — tente de bloquer les lois IA étatiques [1] |

**Mais les états légifèrent quand même** — environ **100 lois** adoptées dans **38 états** en 2025 [2] :
- **NYC Local Law 144** (2023) : audit biais obligatoire pour le recrutement IA [3]
- **Colorado SB 205** (eff. juil. 2026) : 1ère loi IA comprehensive aux US — **$20K/violation** [4]
- **California SB 53** (eff. jan. 2026) : transparence pour modèles frontier (>10²⁶ FLOPs) [5]

<small>Sources : [1] [White House](https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/) · [2] [NCSL](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation) · [3] [NYC LL 144](https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page) · [4] [Colorado SB 205](https://leg.colorado.gov/bills/sb24-205) · [5] [CA Gov](https://www.gov.ca.gov/2025/09/29/governor-newsom-signs-sb-53-advancing-californias-world-leading-artificial-intelligence-industry/)</small>

---

<!-- _class: compact -->

# 07 — Chine : pionnière de la régulation GenAI

La Chine a adopté la **1ère loi au monde** sur l'IA générative — **avant l'UE** [1].

| Date | Loi | Cible |
|------|-----|-------|
| Mars 2022 | Algorithm Recommendation Provisions | Algorithmes de recommandation (opt-out utilisateurs) |
| Jan. 2023 | Deep Synthesis Provisions | Deepfakes — marquage obligatoire, logs 6+ mois |
| **Août 2023** | **Generative AI Interim Measures** | **Toute IA générative** — 1ère loi GenAI mondiale |
| Sept. 2025 | AI Labeling Rules | Marquage explicite + implicite de tout contenu IA |

**Registre obligatoire** : **3 739 outils GenAI** déclarés — le seul registre public et exhaustif au monde [2]

> **Différence clé** : la Chine régule par **type de technologie**, l'UE par **niveau de risque**. Le contenu doit s'aligner sur les "valeurs socialistes fondamentales" — pas d'équivalent EU [3].

<small>Sources : [1] [China Briefing](https://www.china-briefing.com/news/how-to-interpret-chinas-first-effort-to-regulate-generative-ai-measures/) · [2] [Trivium China](https://triviumchina.com/research/seeking-the-next-deepseek-what-chinas-generative-ai-registration-data-can-tell-us-about-chinas-ai-competitiveness/) · [3] [Carnegie Endowment](https://carnegieendowment.org/research/2023/07/chinas-ai-regulations-and-how-they-get-made)</small>

---

<!-- _class: section -->

# Les risques concrets

## Biais, copyright, environnement, santé

---

# 08 — AI Bias : le risque juridique n°1

**Mobley v. Workday (2025)** — première class action sur le biais IA [1] :
- **1,1 milliard** de candidatures rejetées potentiellement concernées
- Le tribunal a jugé les **fournisseurs IA directement responsables**

**Autres cas** :
- **Amazon** a abandonné son outil de recrutement IA en 2018 (biais de genre irréparable) [2]
- **COMPAS** — biais racial dans les recommandations de peine pour la justice US [3]

> **Pour un entrepreneur** : si votre IA touche au recrutement, au crédit ou à l'assurance, le biais est votre **risque juridique n°1**.

<small>Sources : [1] [Bloomberg Law](https://news.bloomberglaw.com/daily-labor-report/employers-find-openings-to-share-ai-bias-liability-with-vendors) · [2] [Reuters](https://www.reuters.com/article/us-amazon-com-jobs-automation-insight-idUSKCN1MK08G) · [3] [ProPublica](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)</small>

---

<!-- _class: compact -->

# 09 — Copyright et contenu synthétique

**Les procès qui dessinent le droit** :
- **NYT v. OpenAI** : en cours — juge ordonne divulgation de **20M de logs** (jan. 2026) [1]
- **Thomson Reuters v. Ross** : premier rejet du fair use pour l'entraînement IA (fév. 2025) [2]
- **EU Directive DSM Art. 4** : les ayants droit peuvent refuser le text mining via robots.txt ou TDMRep [3]

**Deepfakes & contenu synthétique** :
- **EU AI Act Art. 50** : marquage machine-readable obligatoire des contenus IA (août 2026) — amende **3% du CA** [4]
- **C2PA** v2.3 (Coalition for Content Provenance and Authenticity) : standard technique qui ajoute un **certificat d'origine vérifiable** aux images, vidéos et audio — comme un passeport numérique. **446+ membres** dont Adobe, Microsoft, Google, OpenAI, BBC [5]

<small>Sources : [1] [NYT](https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit.html) · [2] [Loeb & Loeb](https://www.loeb.com/en/insights/publications/2025/02/thomson-reuters-v-ross-intelligence-inc) · [3] [Directive DSM 2019/790](https://eur-lex.europa.eu/eli/dir/2019/790) · [4] [EU AI Act Art. 50](https://eur-lex.europa.eu/eli/reg/2024/1689) · [5] [C2PA](https://c2pa.org/membership/)</small>

---

<!-- _class: compact -->

# 10 — Copyright : comment les labs entraînent leurs modèles

**Le précédent Bartz v. Anthropic** (sept. 2025) — plus gros settlement copyright de l'histoire [1] :
- Entraîner sur des livres achetés légalement = **fair use** ("spectacularly transformative")
- Entraîner sur des copies piratées (LibGen) = **infringement** → settlement de **$1,5 Mds** (~$3K/œuvre)

**70+ procès copyright** pendants contre les labs IA aux US [2] :

| Lab | Licensing | Contentieux majeur |
|-----|-----------|-------------------|
| **OpenAI** | 18+ deals, 53% du spend licensing [3] | NYT (en cours, 20M logs) |
| **Anthropic** | Settlement $1,5 Mds (LibGen) [1] | UMG/Concord ($3 Mds réclamés) |
| **Meta** | Tardif, refuse le Code GPAI [4] | Accusé de piratage BitTorrent |
| **xAI** | Aucun deal | DPC Irlande : arrêt définitif données EU [5] |

<small>Sources : [1] [Copyright Alliance](https://copyrightalliance.org/participating-bartz-v-anthropic-settlement/) · [2] [NPR](https://www.npr.org/2025/09/05/g-s1-87367/anthropic-authors-settlement-pirated-chatbot-training-material) · [3] [Digiday](https://digiday.com/media/media-briefing-publisher-report-cards-for-ai/) · [4] [Bruegel](https://www.bruegel.org/analysis/what-eus-code-practice-general-purpose-ai-means-innovation) · [5] [Irish DPC](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-welcomes-conclusion-proceedings-relating-xs-ai-tool-grok)</small>

---

<!-- _class: cols compact -->

# 11 — Impact environnemental de l'IA

<div class="left">

**Par requête** :
- 1 requête ChatGPT (GPT-4o) ≈ **0,3 Wh** [1]
- Eau : **0,26 ml** par requête Gemini (refroidissement) [2]
- Utilisateur modéré : **~1 kWh/an** — négligeable

**À l'échelle** :
- ChatGPT total : **22 TWh/an** > Slovénie [3]
- Data centers mondiaux : **945 TWh** d'ici 2030 [4]

</div>
<div class="right">

**Émissions des labs** :
- Google : émissions **+48%** depuis 2019 [5]
- Microsoft : électricité quasi **triplée** (~11→30 TWh) [6]

**La réponse** :
- GPAI energy reporting obligatoire (août 2025) [7]
- Green AI : pruning, quantization → **50–90%** d'économies [8]

</div>

<small>Sources : [1] [Epoch AI](https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use) · [2] [Google/DeepMind](https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference) · [3] [BestBrokers](https://www.bestbrokers.com/forex-brokers/ais-power-demand-calculating-chatgpts-electricity-consumption-for-handling-over-78-billion-user-queries-every-year/) · [4] [IEA](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) · [5] [Google ESR](https://sustainability.google/reports/google-2024-environmental-report/) · [6] [Microsoft ESR](https://www.microsoft.com/en-us/corporate-responsibility/sustainability/report) · [7] [EU AI Act Art. 53](https://eur-lex.europa.eu/eli/reg/2024/1689) · [8] [Schwartz et al.](https://dl.acm.org/doi/10.1145/3381831)</small>

---

<!-- _class: img-right -->

# 12 — France : IA en santé et certification HDS

- **HDS** obligatoire pour héberger des données de santé [1]
- **HDS v2** (mai 2024) : hébergement physique **exclusivement dans l'EEE** [2]
- **3 voies** : self-hosted (Mistral sur HDS), cloud HDS (Google Cloud HDS v2) [3], ou API directe (⚠️ pas garanti HDS)
- L'AI Act classe la santé en **high-risk** (août 2027) [4]

> *"Puis-je utiliser Gemini API pour une IA psy ?"* — Pas directement. L'API traite les données sur l'infra du provider, hors de votre contrôle.

![bg right:55% contain](assets/infographics/france-hds-decision-tree_run_20260330_144420_f5609b.png)

<small>Sources : [1] [ANS](https://esante.gouv.fr/produits-services/hds) · [2] [Wavestone](https://www.riskinsight-wavestone.com/en/2025/05/evolution-of-the-hds-framework-towards-enhanced-security-and-sovereignty/) · [3] [Google Cloud HDS](https://cloud.google.com/security/compliance/hds) · [4] [EU AI Act Annex III](https://eur-lex.europa.eu/eli/reg/2024/1689) · [5] [CNIL](https://www.cnil.fr/fr/ia-et-sante-la-has-et-la-cnil-lancent-une-consultation-publique-sur-un-projet-de-guide)</small>

---

<!-- _class: compact -->

# 13 — Risques réels vs risques fantasmés

Les dommages causés par l'IA sont **concrets et documentés** :

| Incident | Impact | Source |
|---|---|---|
| **Mobley v. Workday** (2025) | Biais IA : **1,1 Mds** de candidatures rejetées, fournisseurs directement responsables | [1] |
| **Flash Crash** (2010) | Perte de **$1T** en minutes sur les marchés — algorithmes en cascade | [2] |
| **Character.AI** (fév. 2024) | Suicide d'un adolescent de 14 ans après interactions prolongées avec un chatbot | [3] |
| **Arup deepfake** (2024) | **$25M** volés via visioconférence deepfake imitant le CFO à Hong Kong | [4] |
| **Bartz v. Anthropic** (2025) | Settlement copyright **$1,5 Mds** — livres piratés pour l'entraînement | [5] |

> Ces risques **réels et immédiats** méritent plus d'attention que les scénarios d'extinction.

<small>Sources : [1] [Bloomberg Law](https://news.bloomberglaw.com/daily-labor-report/employers-find-openings-to-share-ai-bias-liability-with-vendors) · [2] [SEC/CFTC](https://www.sec.gov/news/studies/2010/marketevents-report.pdf) · [3] [NBC News](https://www.nbcnews.com/tech/characterai-lawsuit-florida-teen-death-rcna176791) · [4] [CNN](https://www.cnn.com/2024/02/04/asia/deepfake-cfo-scam-hong-kong-intl-hnk/index.html) · [5] [Copyright Alliance](https://copyrightalliance.org/participating-bartz-v-anthropic-settlement/)</small>

---

<!-- _class: section -->

# Partie 2 — Impact sociétal

## Emploi, IA responsable et gouvernance

---

<!-- _class: compact -->

# 14 — L'IA automatise des tâches, pas des métiers

- L'IA **n'automatise pas des jobs** — elle automatise des **tâches**
- **80%** de la main-d'œuvre US pourrait voir **au moins 10%** de ses tâches affectées par les LLMs [1]
- Résultat contre-intuitif : les métiers les **mieux payés** sont les **plus exposés** [1][2]

| Revenu annuel | Exposition IA moyenne |
|---|---|
| > $100K | **6,7 / 10** (très exposé) |
| < $35K | **3,4 / 10** (peu exposé) |

**Exemples** : développeurs, analystes financiers, traducteurs, paralegals → **8–9/10**. Plombiers, électriciens, pompiers → **2–3/10** [2].

> Voir la cartographie interactive : [karpathy.ai/jobs](https://karpathy.ai/jobs/) — 342 métiers US scorés par exposition IA.

<small>Sources : [1] [Eloundou et al. (Science, 2024)](https://arxiv.org/abs/2303.10130) · [2] [Karpathy Job Visualizer](https://karpathy.ai/jobs/)</small>

---

# 15 — La citation à retenir

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

# 16 — Augmentation vs Automation

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
- Ex : transcrire et résumer automatiquement les interactions

</div>

> Les entreprises commencent par l'**Augmentation** et migrent vers l'**Automation** quand la confiance est établie. Le cas **Klarna** : 700 postes automatisés, résolution de 11 min à 2 min [1].

<small>Sources : [1] [Klarna](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/) · Adapté de Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

<!-- _class: section -->

# IA responsable & gouvernance

## Des principes aux structures

---

<!-- _class: img-right -->

# 17 — Les 5 piliers de l'IA Responsable

- **Fairness** — ne pas perpétuer les biais
- **Transparency** — décisions compréhensibles
- **Privacy** — protéger les données (RGPD)
- **Robustness** — résister aux attaques et erreurs
- **Accountability** — responsabilité claire

> Pour chaque produit IA : *"Qu'est-ce qui pourrait mal tourner ?"* sur chacun de ces 5 axes. Le cadre OECD (2019) sert de référence à **46 pays** [1].

![bg right:55% contain](assets/infographics/responsible-ai-5-pillars_run_20260330_144519_0f3d32.png)

<small>Sources : [1] [OECD AI Principles](https://oecd.ai/en/ai-principles) · [2] [Microsoft RAI](https://www.microsoft.com/en-us/ai/principles-and-approach) · Adapté de Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

<!-- _class: compact compact-table -->

# 18 — Responsible AI : les frameworks des labs

| Lab | Framework | Ce qu'il protège | Fait marquant |
|-----|-----------|-----------------|---------------|
| **Microsoft** | 6 principes + Office of RAI | Fairness, sécurité, inclusivité | **67** red-teams en 2024, guide EU AI Act [1] |
| **Google** | 7 AI Principles + Frontier Safety v3.0 | Bénéfice social, biais, sécurité | Critical Capability Levels (bio, cyber, autonomie) [2] |
| **Anthropic** | Responsible Scaling Policy v2.2 | Contrôle humain, risques catastrophiques | **ASL-3** activé mai 2025 — 1er test réel [3] |
| **Meta** | Équipe RAI **dissoute** nov. 2023 | Open-source safety tools (LlamaGuard) | Refuse le Code of Practice GPAI [4] |

> **Le test du copyright** : Anthropic a payé **$1,5 Mds** en settlement copyright (Bartz, 2025). La conformité copyright est devenue un **poste budgétaire frontier** pour les labs [5].

<small>Sources : [1] [Microsoft](https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai-transparency-report/) · [2] [DeepMind](https://deepmind.google/blog/introducing-the-frontier-safety-framework/) · [3] [Anthropic](https://www.anthropic.com/responsible-scaling-policy) · [4] [CNBC](https://www.cnbc.com/2023/11/18/facebook-parent-meta-breaks-up-its-responsible-ai-team.html) · [5] [Copyright Alliance](https://copyrightalliance.org/participating-bartz-v-anthropic-settlement/)</small>

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

> *"A country of geniuses in a datacenter"* — les systèmes IA futurs auront la capacité collective d'un État-nation [1].

<small>Sources : [1] [Dario Amodei](https://www.darioamodei.com/essay/the-adolescence-of-technology)</small>

---

<!-- _class: cols -->

# 21 — Anthropic : le paradoxe safety + copyright

<div class="left">

**Critiques** [1] :
- Engagement de pause RSP **retiré**
- Lobbying contre SB-1047 (CA)
- Piratage de **500K livres** via LibGen pour entraîner Claude
- Settlement copyright **$1,5 Mds** [2]

</div>
<div class="right">

**Défense** :
- Mission safety **fondatrice** (raison d'être)
- RSP évolue, pas abandonnée [3]
- Le juge a qualifié l'entraînement de **"fair use"** [2]
- Constitution publiée en **CC0**

</div>

> **Tension clé** : la structure compte plus que l'intention. La sécurité est la mission, mais le copyright a coûté **$1,5 Mds**. Les engagements volontaires résistent-ils à la pression commerciale ?

<small>Sources : [1] [LessWrong](https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/) · [2] [Copyright Alliance](https://copyrightalliance.org/participating-bartz-v-anthropic-settlement/) · [3] [Anthropic RSP](https://www.anthropic.com/responsible-scaling-policy)</small>

---

<!-- _class: section -->

# Partie 3 — Clôture & Veille

## Ressources, récapitulatif, perspectives

---

<!-- _class: compact-table -->

# 22 — Votre boîte à outils de veille IA

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

# 23 — Construire sa routine de veille en 30 min/jour

| Profil | Newsletter | Podcast | YouTube | Communauté |
|--------|------------|---------|---------|------------|
| Entrepreneur généraliste | The Rundown AI | Hard Fork | The AI Advantage | r/ChatGPT |
| Entrepreneur tech | Ben's Bites | No Priors | AI Explained | r/LocalLLaMA |
| Stratège / investisseur | Stratechery | No Priors | 3Blue1Brown | AlphaSignal |

**Conseil** : choisissez **1 ressource par colonne** et tenez-y pendant 1 mois avant d'ajuster.

> **Discussion** : quel profil vous correspond ? Quelles 4 ressources choisissez-vous et pourquoi ?

---

# 24 — Récapitulatif : ce que nous avons couvert

| Session | Thème | Compétence clé |
|:-------:|-------|----------------|
| **S1** | Fondamentaux & paysage IA | Distinguer AI / ML / DL / GenAI |
| **S2** | LLMs & évaluation | Prompter efficacement, évaluer les résultats |
| **S3** | Embeddings, RAG & Agents | Construire avec l'IA (RAG, agents, workflows) |
| **S4** | Business models & stratégie | Value chain, unit economics, projet IA |
| **S5** | Éthique, gouvernance & clôture | EU AI Act, Responsible AI, veille structurée |

> En 5 sessions, vous avez acquis un socle pour **évaluer, cadrer et déployer** des solutions IA en tant qu'entrepreneurs.

---

# 25 — 5 stratégies pour entrepreneurs face à la régulation

1. **Compliance-first comme avantage** — être conforme EU AI Act quand les concurrents ne le sont pas verrouille le marché européen (450M consommateurs)
2. **Sandbox réglementaire** — espace de test gratuit pour startups, protection contre les amendes pendant la phase de développement [1]
3. **Souveraineté premium** — les entreprises européennes paient plus pour du "made in EU" conforme RGPD + AI Act (ex : données de santé + HDS)
4. **Green AI comme différenciateur** — le reporting environnemental est obligatoire dès août 2025, anticiper = avantage concurrentiel
5. **Veille réglementaire continue** — le patchwork US (600+ textes législatifs, 38 états) crée des opportunités de compliance-as-a-service [2]

> La conformité n'est pas un coût — c'est un **investissement dans l'accès au marché**.

<small>Sources : [1] [EU AI Act Art. 57-59](https://eur-lex.europa.eu/eli/reg/2024/1689) · [2] [NCSL](https://www.ncsl.org/technology-and-communication/artificial-intelligence-2025-legislation)</small>

---

# 26 — 5 faits à retenir de cette session

1. **L'EU AI Act** est la première loi IA complète au monde — amendes : jusqu'à **€35M / 7% CA**. Mais la Chine a été la première à réguler spécifiquement le GenAI (août 2023) [1]

2. **Le biais est le risque juridique n°1** — Mobley v. Workday (2025) : les fournisseurs IA sont **directement responsables** [2]

3. **Le copyright coûte cher** — Anthropic a payé **$1,5 Mds** pour avoir entraîné Claude sur des livres piratés. 70+ procès pendants aux US [3]

4. **Les métiers les mieux payés sont les plus exposés** à l'IA (6,7/10 pour >$100K vs 3,4/10 pour <$35K) — mais aussi les plus **augmentés** [4]

5. **La santé en France** = HDS obligatoire + hébergement EEE. Pas de raccourci via les API IA classiques [5]

<small>Sources : [1] [China Briefing](https://www.china-briefing.com/news/how-to-interpret-chinas-first-effort-to-regulate-generative-ai-measures/) · [2] [Bloomberg Law](https://news.bloomberglaw.com/daily-labor-report/employers-find-openings-to-share-ai-bias-liability-with-vendors) · [3] [Copyright Alliance](https://copyrightalliance.org/participating-bartz-v-anthropic-settlement/) · [4] [Karpathy](https://karpathy.ai/jobs/) · [5] [ANS](https://esante.gouv.fr/produits-services/hds)</small>

---

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Construire un monde plus intelligent

## Comprendre l'IA, penser en entrepreneur, agir en européen

Bonne continuation et bonne veille !

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026
