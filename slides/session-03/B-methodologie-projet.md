---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — Session 3 · M2 Entrepreneuriat Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0 · Données publiques"
---

<!-- ABOUTME: Méthodologie projet IA — CRISP-DM, AI Canvas, Open Source vs API, études de cas réelles. -->
<!-- ABOUTME: Seconde moitié de la Session 3, cadré pour entrepreneurs M2 non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Cadrer un projet IA

## Session 3B — Méthodologie projet IA

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# CRISP-DM

## Le standard depuis 25 ans

---

# 01 — CRISP-DM : 6 phases cycliques

Le framework le plus utilisé en Data Science — **43% d'adoption**, #1 depuis 2002 [1] :

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

# 02 — CRISP-DM en pratique

<div class="left">

### Ce qui signale la maturité

- **Consortium européen** : DaimlerChrysler, NCR, SPSS, OHRA [1]
- CRISP-ML(Q) (2021) ajoute Monitoring + Quality Assurance [2]
- Cité **400+ fois** en littérature académique depuis 2021
- Parler CRISP-DM **signale la maturité** aux investisseurs

</div>
<div class="right">

### Les red flags

- Un prestataire qui saute le **Business Understanding**
- Data Preparation = **50-70%** du temps — budgétez en conséquence
- Un projet "fini" au premier essai — le cycle est **itératif**
- Pas de phase **Evaluation** avec des critères business

</div>

<small>Sources : [1] [CRISP-DM](https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/14.2/es/CRISP-DM.pdf) · [2] [ml-ops.org](https://ml-ops.org/content/crisp-ml)</small>

---

# 03 — LLMOps : le cycle GenAI

CRISP-DM date de 1999. Pour les projets **LLM/GenAI**, un cycle en **9 phases** [1] :

1. **Problem Definition** — cadrer le use case et les critères de succès
2. **Model Selection** — benchmark sur votre domaine (Mistral vs Claude vs GPT)
3. **Data Preparation** — knowledge base, chunking, embeddings pour RAG
4. **Prompt Engineering** — system prompts, few-shot, chain-of-thought
5. **Evaluation (Evals)** — golden datasets, métriques automatisées + humaines
6. **Guardrails** — filtrage toxicité, PII, hallucinations [2]
7. **Deployment** — API serving, caching, rate limiting
8. **Observability** — tracing distribué, coûts par requête
9. **Feedback Loops** — corrections humaines, amélioration continue

<small>Sources : [1] [DataScience-PM](https://www.datascience-pm.com/the-genai-life-cycle/) · [2] [NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-llmops/)</small>

---

<!-- _class: section -->

# AI Canvas

## Cadrer avant de coder

---

<!-- _class: cols -->

# 04 — AI Project Canvas vs ML Canvas

<div class="left">

Deux outils visuels one-page pour cadrer un projet IA **avant d'écrire une ligne de code** :

| | AI Project Canvas | ML Canvas |
|---|---|---|
| **Créateur** | Jan Zawadzki (2019) | Louis Dorard (2015) |
| **Blocs** | 9 blocs | 10 blocs |
| **Focus** | Business | Technique |
| **Durée** | 20-30 min | 90-120 min |

</div>
<div class="right">

### Complémentaires

- Commencez par l'**AI Canvas** (business) [1]
- Détaillez avec le **ML Canvas** (technique) [2]
- Le ML Canvas force la question clé : **"quelle prédiction crée de la valeur ?"**
- Template gratuit : [ownml.co](https://www.ownml.co/machine-learning-canvas)

</div>

<small>Sources : [1] [Towards Data Science](https://medium.com/data-science/introducing-the-ai-project-canvas-e88e29eb7024) · [2] [ownml.co](https://www.ownml.co/machine-learning-canvas)</small>

---

# 05 — MVP Patterns : valider avant d'investir

Avant de construire un modèle, **5 patterns** pour tester la valeur [1] :

| Pattern | Principe | Coût | Exemple |
|---------|----------|------|---------|
| **Wizard of Oz** | Humain derrière le rideau | EUR EUR | Un expert répond comme le ferait l'IA |
| **Concierge** | Service manuel, promesse automatique | EUR EUR | Analyse de contrats faite "a la main" |
| **Rule-Based First** | Règles simples avant le ML | EUR | Filtrage par mots-clés avant NLP |
| **Prompt Eng. MVP** | LLM via API, zero-code | EUR | Prototype GPT-4o en 1 journée |
| **API Wrapper** | Assemblage d'APIs existantes | EUR EUR | Combine OCR + LLM + CRM |

> **Google "Rule of ML #1"** : si vous pouvez résoudre le problème sans ML, faites-le d'abord [2].

<small>Sources : [1] [MIT Sloan](https://mitsloan.mit.edu/) · [2] [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml)</small>

---

# 06 — Discussion : Canvas en action

> Votre startup fintech (30 personnes, 5M EUR CA, budget IA 150K EUR) a brainstormé **15 use cases**. Apres filtrage, il en reste 7. Budget pour 2-3 maximum.

| Use case | Impact | Faisabilité | Data | Score |
|----------|--------|------------|------|-------|
| OCR reçus + catégorisation | 7 | 9 | 8 | **8,25** |
| Scoring crédit PME | 9 | 5 | 4 | 5,80 |
| Chatbot support client | 6 | 8 | 7 | 7,10 |
| Détection fraude | 8 | 4 | 3 | 4,90 |

**Questions pour la classe** :
- Pourquoi le scoring crédit est-il mal classé malgré un impact élevé ?
- Quel MVP Pattern utiliseriez-vous pour tester l'OCR avant d'investir ?

---

<!-- _class: section -->

# Open Source vs API vs Self-hosted

## Le choix stratégique de l'infrastructure

---

<!-- _class: cols -->

# 07 — Trois modèles d'accès aux LLMs

<div class="left">

### Closed Source (API Cloud)

- **OpenAI** (GPT-4o), **Anthropic** (Claude), **Google** (Gemini)
- Facile, performant
- Pas de contrôle, vendor lock-in
- Données externalisées (Cloud Act US)

</div>
<div class="right">

### Open Source / Open Weights

- **Meta** (Llama 3), **Mistral AI**, **Google** (Gemma)
- Contrôle total, déploiement on-premise
- Fine-tuning libre
- Conformité RGPD plus simple
- Hub : **Hugging Face** (1M+ modèles) [1]

</div>

<small>Sources : [1] [Hugging Face](https://huggingface.co/)</small>

---

# 08 — Le guide de décision

```
Votre tâche est-elle bien définie en langage naturel ?
  OUI --> Commencez par le PROMPTING
       Le résultat est-il satisfaisant ?
         OUI --> Déployez !
         NON --> Le modèle manque-t-il de contexte spécifique ?
              OUI --> Utilisez le RAG
              NON --> Besoin d'un style/savoir spécifique ?
                   OUI --> Faites du FINE-TUNING
                   NON --> Votre domaine est-il totalement unique ?
                        OUI --> Envisagez le PRETRAINING (rare)
```

> **90%** des projets GenAI en startup se résolvent avec Prompting + RAG [1]. Le Fine-tuning est utile mais pas toujours nécessaire.

<small>Sources : [1] Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

# 09 — L'écosystème open-source européen

- **Hugging Face** : Paris, **$4,5 Mds** valorisation, **1M+ modèles**, 400K datasets [1]
- **Mistral AI** : Paris, **EUR 11,7 Mds** valorisation, seul frontier UE [2]
- **n8n** : Berlin, **$2,5 Mds**, 100K+ stars, automatisation souveraine [3]
- **Lovable** : Stockholm, **$6,6 Mds**, vibe coding européen [4]

> L'écosystème IA open-source européen est **unique au monde** : les 2 plus grandes plateformes open-source (HF + Mistral) sont françaises. Un atout pour les entrepreneurs qui veulent allier innovation et souveraineté.

<small>Sources : [1] [Hugging Face](https://huggingface.co/) · [2] [Mistral AI](https://mistral.ai/) · [3] [n8n](https://n8n.io/) · [4] [TechCrunch](https://techcrunch.com/)</small>

---

<!-- _class: section -->

# Études de cas

## Des entreprises réelles, des leçons concrètes

---

# 10 — Klarna : remplacer puis réembaucher

| Phase | Ce qui s'est passé | Résultat |
|-------|---------------------|----------|
| **Jan 2024** | IA remplace **700 agents** support [1] | 2,3M conversations/mois, 11 min --> 2 min |
| **Mi-2024** | $244M perte --> **$21M profit** | IPO à **$15 Mds** de valorisation [2] |
| **Fin 2024** | La qualité se dégrade | CEO : "on est allés trop loin" |
| **2025** | Réembauchage en gig (400 SEK/h) | L'IA augmente, pas remplace |

> **Leçon** : couper les coûts avec l'IA est tentant, mais couper la qualité coûte plus cher. Le modèle gagnant est l'**augmentation** humain + IA, pas le remplacement total.

<small>Sources : [1] [Klarna](https://www.klarna.com/international/press/) · [2] [Bloomberg](https://www.bloomberg.com/)</small>

---

<!-- _class: cols -->

# 11 — L'Oréal : acquérir l'IA plutôt que la construire

<div class="left">

### La stratégie acquisition

- Acquisition de **ModiFace** (essayage virtuel AR)
- **3x** conversion e-commerce [1]
- Intégrée sur tous les sites de la marque
- IA = avantage concurrentiel dans le retail beauté

</div>
<div class="right">

### La leçon pour les entrepreneurs

- L'Oréal n'a **pas** construit son IA en interne
- Ils ont acheté la **meilleure startup** du domaine
- L'intégration a pris du temps mais le ROI est massif
- Grand groupe : acquérir est souvent **plus rapide** que construire

> L'achat est aussi une stratégie IA légitime.

</div>

<small>Sources : [1] [L'Oréal](https://www.loreal.com/)</small>

---

# 12 — Schneider Electric : EUR 700M économisés

- **Build in-house** : a construit ses propres outils IA
- **EUR 700M** économisés depuis 2019 via maintenance prédictive et optimisation énergie [1]
- **5 Mds** de data points traités par jour
- A commencé par un cas d'usage simple : **maintenance prédictive**

### Ce que ça prouve

| Critère | Schneider | L'Oréal |
|---------|-----------|---------|
| Approche | Build in-house | Acquisition |
| Investissement | Élevé (temps + talent) | Élevé (prix d'achat) |
| Contrôle | Total | Partiel |
| ROI | EUR 700M sur 5 ans | 3x conversion |

> **Pas de réponse universelle** au Build vs Buy — ça dépend de vos ressources et de votre timeline.

<small>Sources : [1] [Schneider Electric](https://www.se.com/)</small>

---

<!-- _class: cols -->

# 13 — Doctolib et Alan : l'IA dans les secteurs régulés

<div class="left">

### Doctolib

- **EUR 6,5 Mds** de valorisation [1]
- **1,6M** consultations assistées par IA
- **80M** utilisateurs en Europe
- Le médecin reste **toujours** dans la boucle

</div>
<div class="right">

### Alan

- **$4,5 Mds** de valorisation [2]
- **EUR 505M ARR**, +48% YoY
- IA pour traitement des demandes d'assurance
- Taux de résolution automatique en hausse

</div>

> **Leçon** : dans les secteurs régulés, l'IA **augmente les experts** au lieu de les remplacer. Le Human-In-The-Loop n'est pas un frein — c'est un avantage de confiance.

<small>Sources : [1] [Doctolib](https://about.doctolib.fr/) · [2] [Alan](https://alan.com/)</small>

---

# 14 — Les échecs à connaître

| Cas | Année | Erreur | Conséquence |
|-----|:-----:|--------|-------------|
| Air Canada | 2024 | Chatbot donne fausse info tarifaire | Condamné : CAD $812 [1] |
| Grok/xAI | 2025 | 3M deepfakes en 11 jours | Enquête UE, perquisition FR [2] |
| UnitedHealth | 2023+ | Algo refuse soins, 90% overturned | Class action, 1,1 Mds rejets [3] |
| Workday | 2025 | 100% rejet candidats 40+ ans | Class action nationale [4] |

> **Règle n.1** : vous êtes responsable de votre IA. "C'est l'algorithme" n'est pas une défense.

<small>Sources : [1] [CRT Canada](https://decisions.civilresolutionbc.ca/) · [2] [EU Commission](https://ec.europa.eu/) · [3] [Reuters](https://www.reuters.com/) · [4] [Law360](https://www.law360.com/)</small>

---

# 15 — Discussion : Qui est responsable quand l'IA dérape ?

> Votre **startup** déploie un chatbot client. Il donne une mauvaise info qui coûte EUR 5 000 à un client.

| Cas | Responsable | Précédent |
|-----|-------------|-----------|
| Air Canada | **L'entreprise** | Le chatbot est votre agent |
| Workday | **Le vendor IA** | Le fournisseur aussi est liable |
| UnitedHealth | **L'assureur** | L'algo ne vous protège pas |

**Questions pour la classe** :
- Faut-il un **Human-In-The-Loop** pour tout chatbot client ?
- L'EU AI Act change-t-il la donne pour votre startup ?
- Qui est responsable si vous utilisez l'API d'OpenAI et que le résultat est faux ?

---

<!-- _class: section -->

# Synthèse

## Choisir son parcours

---

# 16 — Trois phases, trois sets d'outils

**Phase 1 — Valider une idée** (0-3 mois) :
- Use Case Prioritization, AI Project Canvas, MVP Prompt Engineering
- Budget : < 10K EUR, 1-2 personnes, livrable en 1-4 semaines

**Phase 2 — Construire un produit** (3-12 mois) :
- ML Canvas, Build vs Buy, CRISP-DM ou LLMOps, ROI Framework
- Budget : 50-200K EUR, 3-5 personnes, cycles de 2-4 semaines

**Phase 3 — Scaler** (12+ mois) :
- Data Flywheel, FinOps, ISO 42001 / EU AI Act compliance

> **Commencez toujours par la Phase 1** — même si vous pensez connaître la réponse.

<small>Sources : [1] Estimations sectorielles 2024-2026</small>

---

# 17 — Key Takeaways

1. **CRISP-DM reste le standard** — 43% d'adoption, 25 ans de recul. LLMOps ajoute 3 phases pour les projets GenAI.

2. **Cadrez avant de coder** — 20 min d'AI Canvas économisent des mois. Le ML Canvas traduit la vision business en specs techniques.

3. **L'Open Source européen est un atout** — Mistral et Hugging Face sont français. Souveraineté + performance + RGPD.

4. **Chaque cas d'usage a sa leçon** — Klarna (ne remplacez pas tout), L'Oréal (achetez si c'est plus rapide), Schneider (construisez si c'est stratégique).

5. **Vous êtes responsable de votre IA** — Air Canada, Grok, Workday : la justice ne distingue pas l'humain et l'algorithme.

> **Pour la prochaine séance** : choisissez un use case, remplissez l'AI Canvas, et testez avec un Prompt Engineering MVP.
