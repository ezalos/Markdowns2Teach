---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"
---
<!-- ABOUTME: AI in business and society — task analysis, team building, sector impacts, ethics, and EU regulation. -->
<!-- ABOUTME: French body with English technical terms, business-framed for M2 Entrepreneurship. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## L'IA dans l'entreprise et la société

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# L'IA au quotidien

## Daily LLM Usage

---

# 01 — Quatre profils, un même outil

Aujourd'hui, des millions de professionnels utilisent les LLM dans leur métier :

| Profil | Cas d'usage | Exemple de prompt |
|---|---|---|
| **Writing Assistant** | Reformuler un rapport | "Rewrite for a professional business report" |
| **Marketer** | Brainstormer une campagne | "Help me brainstorm an email campaign to reactivate lapsed SaaS users" |
| **Recruiter** | Résumer un feedback | "Summarize this candidate review in 50 words" |
| **Programmer** | Générer du code | "Write Python code to calculate the average of the last column" |

> Quel que soit votre métier, les LLM sont un **copilote** — pas un remplacement.

---

# 02 — Ce que vous faites déjà (sans le savoir)

Les cas d'usage les plus courants en entreprise :

- **Rédaction** — emails, rapports, présentations, posts LinkedIn
- **Analyse** — résumer des documents, extraire des données, comparer des offres
- **Brainstorming** — idéation produit, naming, stratégie marketing
- **Code** — prototypage rapide, scripts d'automatisation, debugging

**Point clé pour entrepreneurs** : l'adoption des LLM ne nécessite aucune infrastructure technique. Un navigateur web suffit pour commencer.

**Question pour la classe** : Ouvrez votre historique ChatGPT ou Claude. Quel est votre usage le plus fréquent ? Rédaction, analyse, brainstorming ou code ?

---

# 03 — Du copilote au workflow automatisé

L'utilisation quotidienne des LLM suit une progression naturelle :

1. **Exploration** — poser des questions ponctuelles
2. **Intégration** — intégrer systématiquement dans son workflow
3. **Automatisation** — créer des chaînes de prompts, des templates, des agents

> Les entreprises les plus avancées ne "promptent" plus manuellement. Elles construisent des **pipelines** qui intègrent les LLM dans leurs processus métier.

**Pour les startups** : chaque étape de cette progression représente une opportunité de produit — du simple template au SaaS complet.

---

<!-- _class: section -->

# Analyser les tâches, pas les métiers

## Task Analysis Framework

---

# 04 — L'IA automatise des tâches, pas des métiers

Le principe fondamental à retenir :

- L'IA **n'automatise pas des jobs**. Elle automatise des **tâches**.
- La plupart des métiers sont une **collection de tâches** variées
- Certaines tâches sont fortement automatisables, d'autres pas du tout

**Exemple : Customer Service Representative**

| Tâche | Potentiel GenAI |
|---|---|
| Répondre aux appels téléphoniques | Low |
| Répondre aux chats clients | **High** |
| Vérifier le statut des commandes | Medium |
| Tenir un historique des interactions | **High** |
| Évaluer la pertinence des réclamations | Low |

<!-- TODO: insert diagram from W3 p9 (customer service task table) -->

---

# 05 — Augmentation vs. Automation

Deux stratégies distinctes pour intégrer l'IA dans un métier :

**Augmentation**
- L'IA **assiste** l'humain dans sa tâche
- L'humain garde le contrôle et valide le résultat
- Ex : recommander une réponse au service client pour édition/approbation

**Automation**
- L'IA **exécute** la tâche de bout en bout
- Aucune intervention humaine nécessaire
- Ex : transcrire et résumer automatiquement les interactions clients

> Pour la plupart des tâches, les entreprises commencent par l'**Augmentation** et migrent progressivement vers l'**Automation** quand la confiance est établie.

<!-- TODO: insert diagram from W3 p10 (augmentation vs automation) -->

---

<!-- _class: cols -->

# 06 — Évaluer le potentiel IA d'une tâche

<div class="left">

### Technical Feasibility

**L'IA peut-elle le faire ?**

- Un jeune diplômé pourrait-il accomplir cette tâche en suivant les instructions d'un prompt ?
- En cas de doute, **testez** avec un LLM
- Un AI Engineer peut évaluer si RAG ou Fine-tuning aideraient

</div>
<div class="right">

### Business Value

**Est-ce rentable de l'automatiser ?**

- Combien de **temps** est consacré à cette tâche ?
- L'automatiser crée-t-elle une valeur **substantielle** (vitesse, coût, qualité) ?
- Quel est le **risque** si l'IA se trompe ?

</div>

> **Framework clé pour entrepreneurs** : priorisez les tâches à haute faisabilité technique ET haute valeur business.

<!-- TODO: insert diagram from W3 p12 (feasibility vs value framework) -->

---

# 07 — La ressource O*NET : décomposer n'importe quel métier

Le site **O*NET** (onetonline.org) répertorie les tâches de **900+ métiers** avec un niveau de détail précis.

**Méthode pour entrepreneurs** :
1. Identifier le métier que votre produit cible
2. Consulter la liste des tâches sur O*NET
3. Évaluer chaque tâche : potentiel GenAI (Low / Medium / High)
4. Cibler les tâches à haut potentiel pour votre MVP

> Cette démarche est la base d'une **analyse de marché IA**. Avant de construire un produit, décomposez le métier en tâches.

<!-- TODO: insert diagram from W3 p13 (O*NET screenshot for customer service) -->

---

# 08 — Exemple : Computer Programmer

| Tâche | Potentiel GenAI |
|---|---|
| Écrire du code | Medium |
| Écrire de la documentation | **High** |
| Répondre aux demandes de support | Medium |
| Relire le code des collègues | Low |
| Recueillir les besoins utilisateurs | Low |

**Analyse** : même un métier "technique" comme le développement n'est pas entièrement automatisable. Les tâches relationnelles (recueil de besoins, code review collaboratif) restent humaines.

> Les développeurs qui utilisent des outils comme **GitHub Copilot** ou **Claude Code** sont **2 à 3x plus productifs** sur les tâches d'écriture de code et documentation.

---

# 09 — Exemple : Lawyer

| Tâche | Potentiel GenAI |
|---|---|
| Rédiger et relire des documents juridiques | **High** |
| Interpréter lois et réglementations | **High** |
| Examiner des preuves | Low |
| Négocier des accords | Low |
| Représenter des clients au tribunal | Low |

**Analyse** : le droit est un secteur où la GenAI a un fort impact sur les tâches de **recherche et rédaction**, mais un impact faible sur les tâches de **jugement humain et négociation**.

**Question pour la classe** : si vous lancez une LegalTech, quelles tâches ciblez-vous en priorité ? Pourquoi ?

---

# 10 — Exemple : Landscaper (Paysagiste)

| Tâche | Potentiel GenAI |
|---|---|
| Entretenir et soigner les plantes | Low |
| Acheter et transporter les végétaux | Low |
| Entretenir l'équipement | Low |
| Communiquer avec les clients | Medium |
| Maintenir le site web de l'entreprise | Low |

**Analyse** : un métier très **physique** avec peu de tâches automatisables par la GenAI. La majorité des tâches nécessitent une présence et une action dans le monde réel.

> **Contraste révélateur** : tous les métiers ne sont pas également impactés. Les métiers manuels sont les moins exposés à l'automatisation par GenAI.

---

# 11 — La matrice d'analyse : votre outil stratégique

Pour chaque métier que vous ciblez avec votre startup :

| | Business Value faible | Business Value forte |
|---|---|---|
| **Feasibility forte** | Quick wins, faible ROI | **Cible prioritaire** |
| **Feasibility faible** | Ignorer | R&D long terme |

**Méthode en 4 étapes** :
1. Lister les tâches du métier (via O*NET ou interviews)
2. Évaluer la Technical Feasibility de chaque tâche
3. Évaluer la Business Value de chaque tâche
4. Prioriser les tâches dans le quadrant **forte feasibility + forte value**

> C'est cette analyse qui distingue une bonne idée IA d'un produit IA qui trouve son marché.

---

<!-- _class: section -->

# De nouveaux workflows, de nouvelles opportunités

## New Workflows & Opportunities

---

# 12 — Exemple workflow : Surgeon

**Sans GenAI** : le chirurgien consacre beaucoup de temps à la **recherche de procédures médicales**, laissant moins de temps pour les chirurgies.

**Avec GenAI** : la recherche est accélérée par l'IA, libérant du temps pour **plus d'opérations** et un meilleur soin aux patients.

> L'Augmentation ne supprime pas le métier. Elle **redistribue le temps** vers les tâches à plus haute valeur ajoutée.

**Leçon pour entrepreneurs** : ne vendez pas "un outil IA". Vendez du **temps récupéré** et une **capacité augmentée**.

<!-- TODO: insert diagram from W3 p19 (surgeon time reallocation bar chart) -->

---

# 13 — Exemple workflow : Legal Documentation Review

**Document juridique complexe** :
- **Sans GenAI** : collecte d'info + relecture + feedback client (100% humain)
- **Avec GenAI** : l'IA accélère la collecte et la relecture, l'humain se concentre sur le feedback

**Document juridique simple** :
- **Sans GenAI** : relecture complète + feedback client
- **Avec GenAI** : l'IA traite le document, l'humain vérifie rapidement + feedback

> Pour les documents simples, on passe d'un processus entièrement humain à une **Automation avec vérification humaine**. Pour les documents complexes, c'est de l'**Augmentation**.

<!-- TODO: insert diagram from W3 p20 (legal review workflow before/after) -->

---

# 14 — Exemple workflow : Marketing Automation

**Sans GenAI** : rédiger le copy du site web + publier. Processus lent et linéaire.

**Avec GenAI** : un tout **nouveau workflow** devient possible :
1. **Générer** plusieurs variantes de copy via LLM
2. **Lancer** un A/B test automatisé
3. **Analyser** la performance de chaque variante
4. **Améliorer** les prompts en fonction des résultats
5. **Itérer** en continu

> Ce n'est pas une simple accélération. C'est un **workflow entièrement nouveau** qui n'existait pas avant la GenAI. C'est ici que naissent les startups les plus innovantes.

<!-- TODO: insert diagram from W3 p21 (marketing automation workflow) -->

---

# 15 — Analyser les tâches de vos clients

Si vous construisez un produit B2B, analysez aussi les tâches de vos **clients** :

**Exemple : aider vos clients à créer un site web**

| Tâche du client | Potentiel GenAI |
|---|---|
| Choisir un template | Low |
| Écrire le titre | **High** |
| Sélectionner les images | Medium |
| Rédiger le contenu de la homepage | Medium |
| Optimiser le copy pour le SEO | **High** |

> **Insight produit** : intégrez la GenAI directement dans le parcours client. Ne la proposez pas comme un outil séparé — intégrez-la dans le workflow existant.

<!-- TODO: insert diagram from W3 p22 (customer task analysis for website building) -->

---

# 16 — Synthèse : le Task Analysis Framework

Le framework en résumé pour les entrepreneurs :

1. **Identifier** le métier cible (le vôtre ou celui de vos clients)
2. **Décomposer** en tâches (O*NET, interviews, observation)
3. **Évaluer** chaque tâche : Augmentation ou Automation ?
4. **Prioriser** selon Technical Feasibility x Business Value
5. **Concevoir** le nouveau workflow (pas juste accélérer l'ancien)
6. **Mesurer** le temps/coût économisé et la valeur créée

> Ce framework est votre **boussole stratégique** pour tout projet IA. Il s'applique à n'importe quel secteur et n'importe quel métier.

**Question pour la classe** : choisissez un métier lié à votre projet. Listez 5 tâches et évaluez leur potentiel GenAI.

---

<!-- _class: section -->

# Construire des équipes IA et analyser les secteurs

## Teams & Sector Analysis

---

# 17 — Les rôles clés d'une équipe GenAI

| Rôle | Responsabilité |
|---|---|
| **Software Engineer** | Développer l'application, connaître les bases du prompting |
| **Machine Learning Engineer** | Implémenter le système IA (LLM, RAG, Fine-tuning) |
| **Product Manager** | Cadrer le projet, identifier les use cases prioritaires |
| **Prompt Engineer ?** | En général **pas un rôle dédié** — c'est une compétence |

**Rôles complémentaires** (selon la taille du projet) :
- **Data Engineer** — qualité et organisation des données
- **Data Scientist** — analyser les données pour guider les décisions
- **Project Manager** — coordonner l'exécution
- **ML Researcher** — pour les projets de R&D avancée

---

# 18 — Démarrer avec une petite équipe

**Équipe de 1 personne** :
- Un Software Engineer qui a appris le prompting, ou
- Un Machine Learning Engineer, ou
- **Vous-même !** (avec des outils no-code et des API)

**Équipe de 2 personnes** :
- ML Engineer + Software Engineer
- Mais de nombreuses autres configurations fonctionnent

> **Message clé pour les entrepreneurs** : ne laissez pas la taille de votre équipe vous freiner. Grâce aux API et outils no-code, une seule personne peut construire un prototype fonctionnel.

**Question pour la classe** : pour votre projet de startup, de quelle configuration d'équipe auriez-vous besoin au lancement ?

---

# 19 — Les métiers les mieux payés sont les plus exposés

Résultat contre-intuitif de la recherche (Eloundou et al., 2023) :

- Les métiers à **hauts salaires** ont une **exposition plus forte** à l'IA
- Les métiers à **bas salaires** (souvent physiques) sont moins impactés
- La courbe d'exposition augmente fortement au-dessus de **$80K/an**

> Ce résultat est **contre-intuitif** : on pourrait croire que l'IA menace surtout les emplois peu qualifiés. En réalité, ce sont les **knowledge workers** les plus touchés.

**Implication pour entrepreneurs** : les clients prêts à payer le plus pour des outils IA sont ceux dont les tâches sont les plus automatisables.

<!-- TODO: insert diagram from W3 p28 (exposure to AI by wage scatter plot, Eloundou et al.) -->

---

<!-- _class: cols -->

# 20 — Impact par fonction métier (McKinsey)

<div class="left">

**Top 6 fonctions** (75% de l'impact total) :

1. **Sales** — ~$500Md
2. **Marketing** — ~$460Md
3. **Software Engineering** (corporate IT) — ~$480Md
4. **Software Engineering** (product) — ~$370Md
5. **Customer Operations** — ~$400Md
6. **Product R&D** — ~$320Md

</div>
<div class="right">

**Fonctions moins impactées** :

- Supply Chain — ~$200Md
- Finance — ~$130Md
- Manufacturing — ~$110Md
- Legal — ~$80Md
- Procurement — ~$80Md
- Pricing — ~$50Md

</div>

> Les fonctions **orientées contenu et communication** captent l'essentiel de la valeur GenAI.

<!-- TODO: insert diagram from W3 p29 (McKinsey functional role impact scatter plot) -->

---

# 21 — Impact par secteur d'industrie (McKinsey)

| Secteur | Impact potentiel (% d'automatisation) |
|---|---|
| Éducation & Formation | **39%** |
| Business & Legal Professions | **30%** |
| STEM Professionals | **29%** |
| Community Services | 26% |
| Creative & Arts Management | 25% |
| Office Support | 21% |
| Managers | 17% |
| Health Professionals | 14% |
| Customer Service & Sales | 12% |
| Property Management | 9% |

> La GenAI pourrait avoir le plus grand impact sur les **knowledge workers**. L'éducation, le droit et les métiers STEM sont en tête.

<!-- TODO: insert diagram from W3 p30 (industry sector bar chart) -->

---

# 22 — Que signifient ces données pour un entrepreneur ?

**Trois insights stratégiques** à retenir :

1. **Les secteurs à haut impact = les marchés les plus réceptifs.** Éducation, legal, marketing — ces secteurs cherchent activement des solutions IA.

2. **"Plus exposé" ne signifie pas "menacé".** Les métiers les plus exposés sont ceux qui bénéficient le plus de l'Augmentation. C'est un marché, pas une menace.

3. **Le contraste physique/cognitif est net.** Si votre startup cible des tâches physiques, la GenAI n'est probablement pas votre levier principal.

> Croisez ces données sectorielles avec le Task Analysis Framework : vous obtenez une **carte de chaleur des opportunités** pour votre startup.

---

<!-- _class: section -->

# Préoccupations sociétales et Responsible AI

## AI Concerns & Responsible AI

---

# 23 — Préoccupation 1 : Bias et toxicité

Les LLM sont entraînés sur des textes d'internet — qui reflètent les **meilleurs et les pires** aspects de l'humanité.

**Exemple de bias** :

Prompt : *"The _______ was a CEO."*
- Les premiers LLM complétaient systématiquement par **"man"**
- Ce bias reflète les stéréotypes présents dans les données d'entraînement

**Solution : RLHF** (Reinforcement Learning from Human Feedback)
- Entraîner un **reward model** qui note la qualité des réponses
- "man" et "woman" reçoivent un score élevé (5/5)
- "airplane" ou des réponses toxiques reçoivent un score faible (1/5)
- Puis entraîner le LLM à générer des réponses à haut score

<!-- TODO: insert diagram from W3 p32-33 (RLHF reward model table) -->

---

# 24 — Préoccupation 2 : Job Displacement

En 2016, Geoffrey Hinton déclarait :

> *"If you work as a radiologist, you're like the coyote that's already over the edge of the cliff, but hasn't yet looked down. [...] People should stop training radiologists now."*

**8 ans plus tard** : il y a **plus** de radiologues qu'en 2016, et ils gagnent mieux leur vie.

**Pourquoi ?** Parce qu'un radiologue a **30+ tâches** (O*NET), et l'IA n'en automatise que quelques-unes.

---

# 25 — La citation à retenir

> *"AI won't replace radiologists. But radiologists that use AI will replace radiologists that don't."*
>
> **— Curtis Langlotz**, Professor of Radiology, Stanford University

Cette citation s'applique à **tous les métiers** :

- L'IA ne remplacera pas les avocats. Mais les avocats qui utilisent l'IA remplaceront ceux qui ne l'utilisent pas.
- L'IA ne remplacera pas les marketeurs. Mais les marketeurs qui utilisent l'IA...
- L'IA ne remplacera pas les entrepreneurs. Mais...

> **Le vrai risque** n'est pas d'être remplacé par l'IA. C'est d'être remplacé par quelqu'un qui utilise l'IA **mieux que vous**.

---

# 26 — Préoccupation 3 : risques réels de l'IA

Les dommages causés par l'IA sont **concrets et documentés** :

| Incident | Détails |
|---|---|
| **Accidents de voitures autonomes** | Uber (2018), Tesla — des morts réels |
| **Flash Crash boursier (2010)** | Algorithmes de trading — perte de $1T en minutes |
| **Sentencing injuste** | COMPAS — bias racial dans les recommandations de peine |

> Ces risques sont **réels et immédiats**. Ils méritent plus d'attention que les scénarios d'extinction.

**Pour les entrepreneurs** : chaque produit IA que vous lancez porte une responsabilité. Les erreurs de votre IA sont **vos** erreurs.

<!-- TODO: insert diagram from W3 p39 (examples of harm: car crash, flash crash, sentencing) -->

---

# 27 — Extinction, AGI et perspective équilibrée

**Le scénario "Terminator"** est omniprésent dans les médias, mais les arguments sur l'extinction restent **peu concrets** — la plupart se résument à *"it could happen"*. L'humanité contrôle déjà des entités plus puissantes qu'un individu (entreprises, États).

**AGI** (Artificial General Intelligence) : une IA capable de **toute tâche intellectuelle** humaine (conduire, faire une thèse, programmer). L'IA actuelle est très performante sur des tâches spécifiques, mais reste loin d'une intelligence générale. La timeline est incertaine.

**Position équilibrée** :
- Les risques réels (bias, accidents, surveillance) méritent plus d'attention que les scénarios d'extinction
- Face aux vrais défis de l'humanité (climat, pandémies), l'IA sera probablement **une partie de la solution**

> Pour un entrepreneur : planifiez pour l'IA **d'aujourd'hui**, pas pour l'AGI hypothétique de demain.

---

<!-- _class: cols -->

# 28 — Les 5 dimensions du Responsible AI

<div class="left">

**Fairness**
L'IA ne doit pas perpétuer ou amplifier les biais existants

**Transparency**
Les décisions de l'IA doivent être compréhensibles par les parties prenantes

**Privacy**
Protéger les données personnelles et garantir la confidentialité

</div>
<div class="right">

**Security**
Protéger les systèmes IA contre les attaques malveillantes

**Ethical Use**
S'assurer que l'IA est utilisée à des fins bénéfiques

</div>

> **Pour chaque produit IA**, posez-vous la question : "Qu'est-ce qui pourrait mal tourner ?" en termes de Fairness, Transparency, Privacy, Security, Ethical Use.

<!-- TODO: insert diagram from W3 p44 (five dimensions of responsible AI) -->

---

# 29 — Responsible AI en pratique

**Trois recommandations concrètes** pour votre startup :

1. **Créer une culture du questionnement éthique**
   - Encourager la discussion et le débat sur les enjeux éthiques
   - Ne pas attendre qu'un problème survienne

2. **Brainstormer les scénarios de défaillance**
   - "Que se passe-t-il si notre IA discrimine ?"
   - "Que se passe-t-il si les données sont compromises ?"
   - Passer chaque dimension en revue systématiquement

3. **Inclure des perspectives diverses**
   - Équipe diverse = angles morts réduits
   - Consulter les parties prenantes impactées par votre produit

> La Responsible AI n'est pas une contrainte. C'est un **avantage compétitif** — surtout en Europe.

---

<!-- _class: section -->

# Le cadre européen : EU AI Act et écosystème français

## EU Regulation & French Ecosystem

---

<!-- _class: cols -->

# 30 — EU AI Act : les 4 niveaux de risque

<div class="left">

**Risque inacceptable** (interdit)
- Scoring social à la chinoise
- Manipulation subliminale
- Exploitation de vulnérabilités
- Identification biométrique en temps réel (sauf exceptions)

**Risque élevé** (obligations strictes)
- Recrutement et RH
- Crédit et assurance
- Justice et forces de l'ordre
- Éducation (admission, notation)

</div>
<div class="right">

**Risque limité** (obligations de transparence)
- Chatbots — signaler que c'est une IA
- Deepfakes — étiquetage obligatoire
- Contenu généré par IA — mention requise

**Risque minimal** (libre)
- Filtres anti-spam
- Jeux vidéo
- La majorité des applications IA

</div>

> **90% des applications IA** sont à risque minimal ou limité. Mais si votre startup touche au recrutement, au crédit ou à la santé, l'EU AI Act vous concerne directement.

---

# 31 — EU AI Act : timeline et obligations

**Calendrier d'application** :

| Date | Étape |
|---|---|
| Août 2024 | Entrée en vigueur |
| Février 2025 | Interdiction des pratiques à risque inacceptable |
| Août 2025 | Obligations pour les modèles à usage général (GPAI) |
| Août 2026 | **Obligations complètes pour les systèmes à haut risque** |

**Obligations clés pour les startups** :
- **Transparence** — informer les utilisateurs qu'ils interagissent avec une IA
- **Documentation** — maintenir une documentation technique des systèmes
- **Human oversight** — garantir une supervision humaine pour les systèmes à haut risque
- **Data governance** — qualité et représentativité des données d'entraînement

> L'EU AI Act est le **RGPD de l'IA**. Les startups qui s'y conforment tôt auront un avantage concurrentiel massif.

---

# 32 — EU AI Act + RGPD : le double cadre européen

L'Europe impose **deux couches de régulation** aux produits IA :

| | RGPD (2018) | EU AI Act (2024-2026) |
|---|---|---|
| **Focus** | Protection des données personnelles | Sécurité et droits fondamentaux |
| **Concepts clés** | Consentement, minimisation, droit à l'oubli | Niveaux de risque, transparence, oversight |
| **Amende max** | 4% du CA mondial | 7% du CA mondial (ou 35M) |
| **Autorité** | CNIL (en France) | Autorités nationales + AI Office (UE) |

**Pour les entrepreneurs** : ce double cadre est une **barrière à l'entrée** pour les concurrents non-européens — et un **argument commercial** pour vos clients.

> En Europe, "Responsible AI" n'est pas optionnel. C'est la **loi**.

---

# 33 — L'écosystème IA français et européen

La France est un **hub mondial** de l'IA :

| Acteur | Contribution |
|---|---|
| **Mistral AI** | LLM souverains européens (Le Chat, Mistral Large, Codestral) |
| **Hugging Face** | Plateforme open-source #1 mondiale pour les modèles IA |
| **Kyutai** | Recherche IA ouverte (fondé par Xavier Niel) |
| **LightOn** | Infrastructure IA pour entreprises |
| **French Tech** | 30+ licornes, écosystème startup dynamique |

**Avantages pour les entrepreneurs français** :
- Accès à des modèles **souverains** (données hébergées en Europe)
- Financements **Bpifrance** et **France 2030** dédiés à l'IA
- Vivier de talents (Polytechnique, ENS, INRIA)
- Conformité RGPD/EU AI Act intégrée dès le départ

---

# 34 — Case study : Klarna et le remplacement des agents

**Klarna** (fintech suédoise, BNPL) a déployé un assistant IA en 2024 :

- **700 postes de service client** remplacés en quelques mois
- L'assistant IA gère **2/3 des conversations** client
- Temps de résolution : de **11 minutes à 2 minutes**
- Satisfaction client : **équivalente** aux agents humains

**Leçons pour entrepreneurs** :
- L'Automation complète est possible pour certaines tâches de service client
- Mais Klarna opère sur des tâches **répétitives et bien cadrées** (BNPL, remboursements)
- Les tâches complexes (litiges, exceptions) restent humaines

> Klarna illustre parfaitement le Task Analysis Framework : automatiser les tâches à haut potentiel, garder l'humain pour le reste.

---

# 35 — Case study : L'Oréal et le Beauty AI

**L'Oréal** utilise l'IA pour transformer l'expérience beauté :

- **ModiFace** — essayage virtuel de maquillage via caméra
- **Skin Genius** — diagnostic de peau par photo (IA + dermatologie)
- **Recommandations personnalisées** — routines adaptées à chaque profil
- **Marketing** — génération de contenu produit à grande échelle

**Résultats** :
- Taux de conversion **2-3x supérieur** avec l'essai virtuel
- **Millions d'analyses de peau** réalisées dans le monde
- Réduction des retours produit grâce à l'essai avant achat

> L'IA ne remplace pas l'expérience beauté. Elle la **personnalise à grande échelle** — un modèle pour tout entrepreneur B2C.

---

# 36 — Synthèse du cours

**Trois piliers** pour naviguer l'ère de la Generative AI :

**1. Comprendre la Generative AI**
- Ce qu'elle peut et ne peut pas faire
- Use cases : Writing, Reading, Chatting

**2. Construire avec la Generative AI**
- Lifecycle d'un projet GenAI
- Technologies : Prompting, RAG, Fine-tuning

**3. Impact sur l'entreprise et la société**
- Task Analysis Framework : analyser les tâches, pas les métiers
- Construire des équipes et identifier les secteurs à fort impact
- Responsible AI et cadre réglementaire européen

> Vous avez maintenant les outils pour **évaluer, construire et déployer** des solutions IA de manière responsable et stratégique.

---

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Construire un monde plus intelligent

## Votre avantage : comprendre l'IA, penser en entrepreneur, agir en européen

M2 Entrepreneuriat · Sorbonne · 2026
