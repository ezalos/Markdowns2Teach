---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche AI Project Frameworks 2024–2026 · Données publiques"
---

<!-- ABOUTME: Frameworks et méthodologies pour cadrer, décider, exécuter et mesurer un projet IA — de la priorisation au ROI. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : outils pratiques, décisions business, exemples concrets avec coûts réels. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Cadrer un projet IA

## De l'idée au ROI — frameworks et méthodologies

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Pourquoi cadrer un projet IA ?

**85%** des projets IA échouent à délivrer le ROI attendu [1]. Les causes :

- Pas de problème business clair → on construit une solution sans problème
- Données insuffisantes → seulement **12%** des orgs ont des données "AI-ready" [2]
- Coûts sous-estimés → **85%** sous-estiment de plus de 10% [3]
- Pas de framework de décision → on build quand il faudrait buy

> **24 frameworks** existent pour éviter ces erreurs. Ce cours couvre les plus utiles pour un entrepreneur.

<small>Sources : [1] [Gartner](https://www.gartner.com/) · [2] [MIT](https://mitsloan.mit.edu/) · [3] [Mavvrik](https://mavvrik.com/)</small>

---

# 02 — La boîte à outils du projet IA

| Phase | Question clé | Frameworks |
|-------|-------------|------------|
| **Prioriser** | Quel projet lancer ? | Use Case Prioritization, Feasibility Matrix |
| **Cadrer** | Quoi et pourquoi ? | AI Project Canvas, ML Canvas |
| **Décider** | Comment construire ? | Build vs Buy vs Fine-tune vs RAG |
| **Exécuter** | Comment piloter ? | CRISP-DM, LLMOps Lifecycle, MVP Patterns |
| **Mesurer** | Quel ROI ? | AI ROI Framework, TCO, Data Flywheel |
| **Gouverner** | Quels risques ? | EU AI Act, NIST AI RMF, ISO 42001 |

> On suit ce parcours dans l'ordre — de la **priorisation** au **ROI**. Chaque phase a ses outils.

---

<!-- _class: section -->

# Prioriser

## Quel projet IA lancer en premier ?

---

# 03 — Use Case Prioritization

BCG 2025 : se concentrer sur **3,5 use cases** donne **2,1x plus de ROI** que d'en disperser 6,1 [1]

**Phase 1 — Filtrage Go/No-Go** (élimine 40-60% des idées) :
- EU AI Act : use case "high-risk" ? → +6-12 mois de compliance
- Données disponibles ? Équipe ? Cadre légal ?

**Phase 2 — Scoring multi-critères** (5 dimensions, 1-10) :
- Impact business · Faisabilité · Data readiness · ROI · Scalabilité
- Méthode "budget 100 pts" → force les arbitrages stratégiques [2]

> **Piège** : les équipes surestiment la qualité de leurs données (score 7 quand c'est 4)

<small>Sources : [1] [BCG](https://www.bcg.com/) · [2] [Toptal/GSAIF](https://www.toptal.com/product-managers/artificial-intelligence/use-case-prioritization-framework)</small>

---

# 04 — Discussion : Prioriser ses projets IA

> Votre startup fintech (30 personnes, 5M€ CA, budget IA 150K€) a brainstormé **15 use cases**. Après filtrage, il en reste 7. Budget pour 2-3 maximum.

| Use case | Impact | Faisabilité | Data | Score |
|----------|--------|------------|------|-------|
| OCR reçus + catégorisation | 7 | 9 | 8 | **8,25** |
| Scoring crédit PME | 9 | 5 | 4 | 5,80 |
| Chatbot support client | 6 | 8 | 7 | 7,10 |
| Détection fraude | 8 | 4 | 3 | 4,90 |

**Questions pour la classe** :
- Pourquoi le scoring crédit est-il mal classé malgré un impact élevé ?
- Le chatbot est tentant — mais est-ce le meilleur usage de 150K€ ?

---

<!-- _class: section -->

# Cadrer

## Définir le quoi et le pourquoi avant de coder

---

# 05 — Les canvases IA

Deux outils visuels one-page pour cadrer un projet IA **avant d'écrire une ligne de code** :

| | AI Project Canvas [1] | ML Canvas [2] |
|---|----------------------|---------------|
| **Créateur** | Jan Zawadzki (2019) | Louis Dorard 🇫🇷 (2015, v1.1 2021) |
| **Blocs** | 9 blocs, 4 quadrants | 10 blocs, 3 groupes |
| **Focus** | Business (coûts, revenus, stakeholders) | Technique (prédiction, features, évaluation) |
| **Durée** | 20-30 min première version | 90-120 min en atelier |
| **Idéal pour** | Pitch investisseur, cadrage initial | Spécification ML, cahier des charges |

> **Complémentaires** : commencez par l'AI Canvas (business), puis détaillez avec le ML Canvas (technique).

<small>Sources : [1] [Towards Data Science](https://medium.com/data-science/introducing-the-ai-project-canvas-e88e29eb7024) · [2] [ownml.co](https://www.ownml.co/machine-learning-canvas)</small>

---

<!-- _class: cols -->

# 06 — Spotlight : ML Canvas (Louis Dorard)

<div class="left">

- Créé par **Louis Dorard** 🇫🇷 (PhD UCL, fondateur PAPIs)
- **10 blocs** : Value Proposition → Prediction → Learning → Evaluation
- Utilisé à **Microsoft AI School** et conférences PAPIs [1]
- Endorsé par Carlos Escapa (AWS) et Bill Schmarzo (Hitachi)

</div>
<div class="right">

- Force la question clé : **"quelle prédiction crée de la valeur ?"**
- Le bloc "Decisions" traduit les prédictions en actions produit
- Template gratuit : [ownml.co](https://www.ownml.co/machine-learning-canvas) [2]
- Validé en 2026 pour l'ère GenAI (arXiv:2601.01839)

</div>

<small>Sources : [1] [ml-ops.org](https://ml-ops.org/) · [2] [GitHub](https://github.com/louisdorard/machine-learning-canvas)</small>

---

<!-- _class: section -->

# Décider

## Build vs Buy vs Fine-tune vs RAG

---

# 07 — Les 5 approches d'implémentation

| Approche | Coût | Time-to-value | Contrôle | Quand ? |
|----------|------|--------------|----------|---------|
| **Buy API** (GPT-4o, Claude) | €€ | 1-2 semaines | Faible | MVP, validation rapide |
| **RAG** (API + vos données) | €€€ | 2-6 semaines | Moyen | Données propriétaires à jour |
| **Fine-tune** (QLoRA, PEFT) | €€€€ | 4-12 semaines | Fort | Style/format spécifique |
| **Build from scratch** | €€€€€ | 6-18 mois | Total | Moat fondamental |
| **Agentic** (LLM + outils) | €€€ | 4-8 semaines | Moyen | Workflows multi-étapes [1] |

- **57%** des organisations ne fine-tunent pas — prompt engineering + RAG suffit [2]
- **60%** des apps GenAI en production utilisent RAG plutôt que fine-tuning [3]

<small>Sources : [1] [KPMG AI Pulse 2026](https://kpmg.com/) · [2] [LangChain 2025](https://langchain.com/) · [3] [Deloitte](https://www.deloitte.com/)</small>

---

# 08 — Combien ça coûte vraiment ?

| Approche | Coût initial | Coût mensuel | Break-even vs API |
|----------|-------------|-------------|-------------------|
| **API** (GPT-4o) | ~0 € | $2,50-$10 /M tokens [1] | — |
| **API** (DeepSeek) | ~0 € | $0,28-$0,42 /M tokens [1] | — |
| **RAG** | 5-15K € | 50-8 000 €/mois | ~6 mois |
| **Fine-tune QLoRA** | 100-5 000 €/run | ~500 €/mois hosting | ~12 mois |
| **Fine-tune complet** | 5-50K € | 1-5K €/mois hosting | ~18-24 mois |
| **Build from scratch** | >1M € | >10K €/mois | >36 mois |

> **Règle pratique** : si vos coûts API dépassent **15K€/mois**, évaluez le self-hosting Mistral ou Llama [2]

<small>Sources : [1] Pricing APIs 2025 · [2] [a16z](https://a16z.com/)</small>

---

# 09 — Discussion : Build vs Buy pour une legaltech

> Vous construisez une startup **legaltech à Paris** qui analyse des contrats. Votre prototype utilise l'API Claude. Les clients (cabinets d'avocats) posent des questions sur la **confidentialité**.

| Option | Modèle | Hébergement | Coût 6 mois | Risque |
|--------|--------|------------|-------------|--------|
| A | API Claude | Cloud US | ~8K € | Cloud Act, vendor lock-in |
| B | Mistral Large (self-hosted) | OVHcloud 🇫🇷 | ~25K € | Infra à gérer |
| C | QLoRA Mistral 7B + RAG | Scaleway 🇫🇷 | ~18K € | Complexité technique |

**Questions pour la classe** :
- Quel critère pèse le plus : coût, performance, ou confiance client ?
- À partir de quel CA mensuel l'option B devient-elle rentable ?

---

<!-- _class: section -->

# Exécuter

## Piloter le projet de bout en bout

---

# 10 — CRISP-DM : le standard depuis 25 ans

Le framework le plus utilisé en Data Science — **6 phases cycliques** [1] :

1. **Business Understanding** — définir le problème et les critères de succès
2. **Data Understanding** — explorer, inventorier, évaluer la qualité
3. **Data Preparation** — nettoyer, transformer (**50-70% de l'effort** total)
4. **Modeling** — entraîner, comparer, tuner les modèles
5. **Evaluation** — valider vs les critères business (pas que les métriques ML)
6. **Deployment** — mettre en production + monitoring continu

> Né d'un **programme de recherche européen** (EU ESPRIT, 1996-1999). Jamais mis à jour — mais toujours dominant.

<small>Sources : [1] [DataScience-PM](https://www.datascience-pm.com/crisp-dm-2/) · [IBM](https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/14.2/es/CRISP-DM.pdf)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : CRISP-DM

<div class="left">

- **Consortium européen** : DaimlerChrysler, NCR, SPSS, OHRA [1]
- **43% d'adoption** dans les sondages KDnuggets — #1 depuis 2002
- CRISP-ML(Q) (2021) ajoute Monitoring + Quality Assurance [2]
- Cité **400+ fois** en littérature académique depuis 2021

</div>
<div class="right">

- Parler CRISP-DM **signale la maturité** aux investisseurs et clients
- Red flag : un prestataire qui saute le Business Understanding
- Data Preparation = **50-70%** du temps — budgétez en conséquence
- Framework gratuit, non propriétaire, applicable à tout projet data

</div>

<small>Sources : [1] [CRISP-DM](https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/14.2/es/CRISP-DM.pdf) · [2] [ml-ops.org](https://ml-ops.org/content/crisp-ml)</small>

---

# 12 — LLMOps : le cycle GenAI

CRISP-DM date de 1999. Pour les projets **LLM/GenAI**, un cycle en **9 phases** [1] :

1. **Problem Definition** — cadrer le use case et les critères de succès
2. **Model Selection** — benchmark sur votre domaine (Mistral vs Claude vs GPT)
3. **Data Preparation** — knowledge base, chunking, embeddings pour RAG
4. **Prompt Engineering** — system prompts, few-shot, chain-of-thought
5. **Evaluation (Evals)** — golden datasets, métriques automatisées + humaines
6. **Guardrails** — filtrage toxicité, PII, hallucinations (< 100ms) [2]
7. **Deployment** — API serving, caching, rate limiting
8. **Observability** — tracing distribué, coûts par requête (Langfuse, Arize)
9. **Feedback Loops** — corrections humaines → amélioration continue

<small>Sources : [1] [DataScience-PM](https://www.datascience-pm.com/the-genai-life-cycle/) · [2] [NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-llmops/)</small>

---

# 13 — MVP Patterns : valider avant d'investir

Avant de construire un modèle, **5 patterns** pour tester la valeur [1] :

| Pattern | Principe | Coût | Exemple |
|---------|----------|------|---------|
| **Wizard of Oz** | Humain derrière le rideau | €€ | Un expert répond comme le ferait l'IA |
| **Concierge** | Service manuel, promesse auto. | €€ | Analyse de contrats faite "à la main" |
| **Rule-Based First** | Règles simples avant le ML | € | Filtrage par mots-clés avant NLP |
| **Prompt Eng. MVP** | LLM via API, zero-code | € | Prototype GPT-4o en 1 journée |
| **API Wrapper** | Assemblage d'APIs existantes | €€ | Combine OCR + LLM + CRM |

> **Google "Rule of ML #1"** : si vous pouvez résoudre le problème sans ML, faites-le d'abord [2]

<small>Sources : [1] [MIT Sloan](https://mitsloan.mit.edu/) · [2] [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)</small>

---

<!-- _class: section -->

# Mesurer et défendre

## ROI, coûts cachés et Data Flywheel

---

# 14 — AI ROI Framework

La pression investisseurs sur le ROI IA est passée de **68% à 90%** en un an [1]. Quatre piliers :

| Pilier | Horizon | Impact typique |
|--------|---------|----------------|
| **Efficience** | 6-18 mois | 100K-2M €/an (automatisation, temps) |
| **Revenus** | 12-24 mois | 200K-5M €/an (upsell, personnalisation) |
| **Risque** | Immédiat | Réduction fraude, compliance, erreurs |
| **Agilité** | 12+ mois | Time-to-market, capacité d'adaptation |

> **"Reality Discount"** : ne projetez que **50%** des bénéfices en Year 1, **80%** en Year 2, **100%** en Year 3 [2]

- McKinsey 2025 : **74%** des organisations atteignent un ROI dès la première année [3]

<small>Sources : [1] [KPMG](https://kpmg.com/) · [2] [OpenKit](https://openkit.co.uk/blog/posts/business-case-for-ai-roi-calculation) · [3] [McKinsey](https://www.mckinsey.com/)</small>

---

# 15 — Les coûts cachés de l'IA (l'iceberg)

Ce que vous voyez : licence API, salaires data scientists. Ce que vous ne voyez pas [1] :

| Coût caché | Part du budget | Exemple |
|------------|---------------|---------|
| **Data preparation** | 25-40% | Nettoyage, labeling, pipelines ETL |
| **Intégration** | 60-200K € | Connexion CRM, ERP, bases legacy |
| **Maintenance annuelle** | 15-30% du coût initial | Drift, retraining, mise à jour modèles |
| **Change management** | Jusqu'à 3x le technique | Formation, adoption, résistance |
| **Compliance** | Variable | RGPD, EU AI Act, audits |

- Les abonnements/licences représentent **< 40%** des dépenses réelles [2]
- **65%** des surcoûts imprévus viennent de l'infra et du talent [2]

<small>Sources : [1] [Gartner](https://www.gartner.com/) · [2] Estimations sectorielles 2024-2025</small>

---

# 16 — Data Flywheel : construire un moat par la donnée

Le **cycle vertueux** qui rend votre produit IA défendable [1] :

1. **Déployer** le produit → 2. **Collecter** les données utilisateurs →
3. **Améliorer** le modèle → 4. **Enrichir** le produit → retour à 1.

Exemples :
- **Cursor** : 1M+ devs → patterns d'édition → meilleur auto-complétion → plus de devs
- **Waze** : plus de conducteurs → meilleur trafic temps réel → plus de conducteurs

**Attention** : a16z prévient que les data moats montrent des **rendements décroissants après 20-40%** de la distribution capturée [2]

> Concevez votre produit pour collecter des données **dès le jour 1** — même avant le ML.

<small>Sources : [1] [NVIDIA](https://www.nvidia.com/en-us/glossary/data-flywheel/) · [2] [a16z](https://a16z.com/)</small>

---

<!-- _class: cols -->

# 17 — Spotlight : Data Flywheel en pratique

<div class="left">

- **Jim Collins** (2001) a inventé le concept de flywheel
- **Jeff Bezos** l'a appliqué à Amazon (recommandations → ventes)
- **NVIDIA NeMo** : plateforme dédiée au GenAI Data Flywheel [1]
- Argument #1 de **defensibility** pour les VCs

</div>
<div class="right">

- Fintech 🇫🇷 : catégoriseur → 50 users → 10K labels → fine-tune → 90%
- Concevez le **feedback loop** avant le modèle
- Synthetic data peut **bootstrapper** le cycle initial [2]
- Piège : optimiser pour le feedback → **sycophancy** (GPT-4o, avril 2025)

</div>

<small>Sources : [1] [NVIDIA Blueprint](https://build.nvidia.com/nvidia/build-an-enterprise-data-flywheel) · [2] [a16z](https://a16z.com/)</small>

---

# 18 — Discussion : Calculer le ROI d'un chatbot

> Votre e-commerce français (50 personnes, 8M€ CA) envisage un **chatbot IA** pour le support client. Le CFO demande un business case chiffré.

| Poste | Coût Year 1 |
|-------|------------|
| Plateforme + API | 42K € |
| Data prep + intégration | 60K € |
| Formation + maintenance | 20K € |
| **Total** | **122K €** |

Bénéfices projetés : 125K€/an — mais avec le **Reality Discount** → **63K€** en Year 1 [1]

**Questions pour la classe** :
- Le payback est à **19 mois**. Votre board accepte-t-il ?
- Quel **kill-switch** définissez-vous ? (indice : deflection < 30% à 3 mois = pivot)

<small>Sources : [1] [OpenKit](https://openkit.co.uk/blog/posts/business-case-for-ai-roi-calculation)</small>

---

<!-- _class: section -->

# Synthèse

## Quel framework choisir ?

---

# 19 — Gouvernance : l'essentiel pour le chef de projet

La gouvernance IA impacte votre **timeline et votre budget** dès la Phase 1 [1] :

| Standard | Origine | Obligatoire ? | Impact projet |
|----------|---------|--------------|---------------|
| **EU AI Act** | 🇪🇺 UE (2024) | Oui (dès 2025) | Filtrage use cases, amendes jusqu'à 35M€ |
| **NIST AI RMF** | 🇺🇸 USA (2023) | Non | 72 contrôles, référence internationale |
| **ISO 42001** | International (2023) | Certifiable | 38 contrôles, exigé par grands comptes |
| **ALTAI** | 🇪🇺 UE (2020) | Non | Auto-évaluation, pilotée par 350+ orgs [2] |

> Session 5 approfondira l'EU AI Act. Pour le projet IA : **intégrez le risk screening dès la Phase 1**.

<small>Sources : [1] [EU AI Act](https://artificialintelligenceact.eu/) · [2] [European Commission](https://ec.europa.eu/)</small>

---

# 20 — Choisir son parcours

Trois phases, trois sets d'outils :

**Phase 1 — Valider une idée** (0-3 mois) :
- Use Case Prioritization → AI Project Canvas → MVP Prompt Engineering
- Budget : < 10K€, 1-2 personnes, livrable en 1-4 semaines [1]

**Phase 2 — Construire un produit** (3-12 mois) :
- ML Canvas → Build vs Buy → CRISP-DM ou LLMOps → ROI Framework
- Budget : 50-200K€, 3-5 personnes, cycles de 2-4 semaines [1]

**Phase 3 — Scaler** (12+ mois) :
- Data Flywheel → FinOps → ISO 42001 / EU AI Act compliance

> **Commencez toujours par la Phase 1** — même si vous pensez connaître la réponse.

<small>Sources : [1] Estimations sectorielles — voir slides 08 et 14 pour le détail des coûts</small>

---

# 21 — Key Takeaways

1. **Priorisez férocement** — 3,5 use cases ciblés battent 6,1 dispersés (BCG). Filtrez par EU AI Act dès le départ.

2. **Cadrez avant de coder** — 20 min d'AI Canvas économisent des mois. Le ML Canvas de Louis Dorard 🇫🇷 est votre cahier des charges.

3. **Buy d'abord, build ensuite** — 57% n'ont pas besoin de fine-tuning. API + RAG couvre la majorité des use cases. Self-host quand l'API dépasse 15K€/mois.

4. **Budgétez l'iceberg** — les coûts visibles (API, salaires) sont < 40% du total. Data prep, intégration et change management sont les vrais postes.

5. **Concevez le flywheel dès le jour 1** — votre produit doit collecter des données qui améliorent le modèle. C'est votre principal argument de defensibility.

> **Prochaine étape** : choisissez un use case, remplissez l'AI Canvas, et testez avec un Prompt Engineering MVP.
