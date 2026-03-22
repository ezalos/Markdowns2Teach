---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Méthodologie projet IA — du prompt-based development au déploiement, CRISP-DM, LLMOps, AI Canvas, MVP, choix de stack. -->
<!-- ABOUTME: Block D de la Session 3, cadré pour entrepreneurs M2 non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Méthodologie projet IA

## Session 3D — Du cadrage au déploiement

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Du Prompt au Produit

## La nouvelle façon de construire

---

# 01 — La révolution : Prompt-based Development

Avant la GenAI, un classifieur de sentiment nécessitait **6-12 mois** [1]. Aujourd'hui, quelques lignes suffisent :

```
prompt = """
  Classify the following review as positive or negative:
  The banana pudding was really tasty!
"""
response = llm_response(prompt)
```

**Ce que cela change** :
- **Coût d'entrée quasi nul** — pas besoin d'équipe ML
- **Time-to-market réduit** — prototyper en un week-end
- **Compétence clé = comprendre le problème**, pas coder

<small>Sources : [1] [Andrew Ng, *Generative AI for Everyone*, DeepLearning.AI](https://www.coursera.org/learn/generative-ai-for-everyone)</small>

---

# 02 — Quatre catégories d'applications GenAI

Les applications logicielles utilisant la Generative AI se classent en quatre familles :

| Catégorie | Ce que fait l'IA | Exemple concret |
|---|---|---|
| **Writing** | Génère du texte à partir d'instructions | FAQ bot, rédaction automatique |
| **Reading** | Analyse et classifie du contenu | Sentiment Analysis, extraction de données |
| **Chatting** | Dialogue interactif avec l'utilisateur | Chatbot de commande, support client |
| **Coding** | Génère, corrige et optimise du code | Copilot, Cursor, Claude Code |

> Ces quatre catégories se retrouvent dans presque tous les produits IA. Le Coding est devenu une famille à part entière en 2025.

---

<!-- _class: img-right -->

# 03 — Le GenAI Lifecycle : Scope → Build → Evaluate → Deploy

Tout projet GenAI suit un cycle itératif en 4 phases :

1. **Scope** — Définir le projet et ses objectifs
2. **Build** — Construire le système (prompt, pipeline)
3. **Evaluate** — Tester en interne, détecter les erreurs
4. **Deploy** — Mettre en production, surveiller

> Ce n'est **pas linéaire**. Les retours entre étapes sont la norme.

![bg right:55% contain](assets/infographics/genai-lifecycle_run_20260216_171314_f23e16.png)

---

<!-- _class: compact -->

# 04 — Scope — Bien cadrer le projet

Le cadrage est l'étape la plus critique. Un mauvais scope = un projet qui échoue.

**Questions à se poser** :
- Quel problème business précis résout-on ?
- Qui est l'utilisateur final ?
- Comment mesurer le succès ? (métriques claires)
- Quel niveau de qualité est acceptable ?

**Mesurer le succès** — Définir des KPIs dès le scope :
- *Précision* : % de réponses correctes (cf. Session 2B, Precision/Recall)
- *Satisfaction utilisateur* : NPS, résolution au premier contact
- *ROI* : coût IA vs coût du processus manuel remplacé

> **Conseil** : commencez par le cas d'usage le plus simple qui apporte de la valeur.

---

<!-- _class: img-right -->

# 05 — Build — Un processus empirique

Construire avec la GenAI est **hautement expérimental** :

- Écrire un prompt, tester, corriger, itérer
- Le cycle **Idea → Prompt → LLM Response** se répète des dizaines de fois
- Chaque itération prend des minutes, pas des semaines

**Le prototype initial ne sera pas parfait** — et c'est normal. L'objectif : progresser vite vers une version fonctionnelle.

> Lean Startup : Build → Measure → Learn — même logique appliquée à l'IA.

![bg right:55% contain](assets/ng02/img-011.png)

---

# 06 — Evaluate — Tester avant de déployer

L'évaluation interne permet de **détecter les erreurs avant vos clients** :

- Faire tester le système par votre équipe
- Créer un jeu de tests représentatifs
- Identifier les cas limites (Edge Cases)
- Mesurer la précision sur vos métriques

| Erreur fréquente | Conséquence | Solution |
|---|---|---|
| Scope trop large | Projet qui n'aboutit jamais | Cibler une seule tâche précise |
| Pas d'évaluation | Bugs découverts par les clients | Tester avec des cas réels |
| Déploiement "big bang" | Crise si le système hallucine | Déployer progressivement |

---

# 07 — Deploy — Mettre en production intelligemment

Le déploiement ne signifie pas "ouvrir à tout le monde d'un coup" :

- **Phase 1** : test interne (votre équipe utilise le système)
- **Phase 2** : bêta limitée (quelques clients, avec monitoring humain)
- **Phase 3** : déploiement progressif (scaling avec alertes automatiques)

**Monitoring continu** — Après le déploiement, surveiller :
- Les réponses incorrectes ou inappropriées
- La satisfaction utilisateur
- Les nouveaux cas d'usage imprévus

> Le monitoring peut révéler de nouveaux problèmes, ce qui déclenche un retour aux étapes Build ou Evaluate.

---

<!-- _class: section -->

# Frameworks et outils

## Structurer la démarche projet

---

<!-- _class: img-right -->

# 08 — CRISP-DM : 6 phases cycliques

![bg right:55% contain](assets/infographics/crisp-dm_run_20260216_171255_a6ef8c.png)

Le standard Data Science — **43% d'adoption**, #1 depuis 2002 [1] :

1. **Business Understanding** — problème + critères de succès
2. **Data Understanding** — explorer, évaluer la qualité
3. **Data Preparation** — **50-70% de l'effort** [2]
4. **Modeling** — entraîner, comparer, tuner
5. **Evaluation** — valider vs critères business
6. **Deployment** — production + monitoring

<!-- Speaker notes: Né d'un programme européen (EU ESPRIT, 1996-1999). Jamais mis à jour — toujours dominant. -->

<small>Sources : [1] [DataScience-PM](https://www.datascience-pm.com/crisp-dm-2/) · [2] [IBM SPSS Modeler CRISP-DM Guide](https://www.ibm.com/docs/en/spss-modeler/18.5.0?topic=dm-data-preparation)</small>

---

<!-- _class: cols -->

# 09 — CRISP-DM en pratique

<div class="left">

### Ce qui signale la maturité

- **Consortium européen** : DaimlerChrysler, NCR, SPSS, OHRA [1]
- CRISP-ML(Q) (2021) ajoute Monitoring + Quality Assurance [2]
- Le paper fondateur cité **1 100+ fois** en littérature académique [3]
- Parler CRISP-DM **signale la maturité** aux investisseurs

</div>
<div class="right">

### Les red flags

- Un prestataire qui saute le **Business Understanding**
- Data Preparation = **50-70%** du temps [4] — budgétez en conséquence
- Un projet "fini" au premier essai — le cycle est **itératif**
- Pas de phase **Evaluation** avec des critères business

</div>

<small>Sources : [1] [CRISP-DM](https://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/14.2/es/CRISP-DM.pdf) · [2] [ml-ops.org](https://ml-ops.org/content/crisp-ml) · [3] [Semantic Scholar](https://www.semanticscholar.org/paper/48b9293cfd4297f855867ca278f7069abc6a9c24) · [4] [IBM SPSS Modeler CRISP-DM Guide](https://www.ibm.com/docs/en/spss-modeler/18.5.0?topic=dm-data-preparation)</small>

---

<!-- _class: img-right -->

# 10 — LLMOps : le cycle GenAI

![bg right:55% contain](assets/infographics/llmops_run_20260216_171257_39e262.png)

CRISP-DM date de 1999. Pour la GenAI, **9 phases** en 3 blocs [1] :

**Define** — cadrer le projet
- Problem Definition, Model Selection, Data Preparation

**Build** — construire la solution
- Prompt Engineering, Evaluation (Evals), Guardrails [2]

**Operate** — maintenir en production
- Deployment, Observability, Feedback Loops

<!-- Speaker notes: Différence clé vs CRISP-DM : Guardrails et Observability sont des phases à part entière, pas des options. -->

<small>Sources : [1] [DataScience-PM](https://www.datascience-pm.com/the-genai-life-cycle/) · [2] [NVIDIA](https://developer.nvidia.com/blog/mastering-llm-techniques-llmops/)</small>

---

<!-- _class: cols -->

# 11 — AI Project Canvas vs ML Canvas

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

# 12 — MVP Patterns : valider avant d'investir

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

# 13 — Prototypage rapide d'agents

La plupart des équipes **perdent des mois** à construire l'infrastructure agent avant de valider l'idée [1].

**L'approche Jason Liu** — tester avec Claude Code comme harness :
- `CLAUDE.md` = spécification en langage naturel (mission, outils, critères de succès)
- `tools/` = scripts CLI wrappant les APIs réelles
- `tests/` = scénarios avec `request.txt` (input) + `check.py` (validation pass/fail)

**Le test décisif** : si Claude Code ne peut pas accomplir la tâche avec un accès parfait aux outils, votre agent de production ne le pourra pas non plus.

> C'est le **Prompt Engineering MVP** (slide 12) appliqué aux agents. Un test passant = concept validé [1].

<small>Sources : [1] [Jason Liu — Rapid Agent Prototyping](https://jxnl.co/writing/2025/09/04/context-engineering-rapid-agent-prototyping/)</small>

---

<!-- _class: compact -->

# 14 — Les 6 pièges de l'AI Engineering

Chip Huyen identifie **6 erreurs récurrentes** dans les projets GenAI [1] :

1. **Utiliser la GenAI quand ce n'est pas nécessaire** — un algorithme classique suffit souvent (cf. slide précédente)
2. **Confondre "mauvais produit" et "mauvaise IA"** — Intuit a transformé son chatbot fiscal en ajoutant des questions suggérées, sans toucher au modèle [1]
3. **Démarrer trop complexe** — vector DB, agents, fine-tuning… avant d'avoir validé qu'un simple prompt ne suffit pas
4. **Surestimer un succès précoce** — LinkedIn : **1 mois pour 80%**, puis **4 mois supplémentaires** pour dépasser 95% [1]
5. **Négliger la compliance et la safety** — copyright, vie privée, abus par des acteurs malveillants
6. **Crowdsourcer les use cases** — sans stratégie, on finit avec "un million de Slack bots" et zéro ROI [1]

> *"It's easy to build a demo, but hard to build a product."* — Chip Huyen

<small>Sources : [1] [Chip Huyen](https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html)</small>

---

# 15 — Discussion : Avez-vous besoin de GenAI ?

> **Scénario** : votre startup veut ajouter de l'IA à son produit. Un investisseur vous demande : *"Pourquoi de la GenAI et pas une simple regex ou un modèle classique ?"*

**Questions pour la classe** :

- Quand la GenAI est-elle **overkill** ? Citez un cas où une règle simple suffirait
- Comment savez-vous qu'il faut **monter en complexité** (Prompting → RAG → Fine-tuning) ?
- Si votre démo fonctionne en 1 mois, combien de temps budgétez-vous pour la production ? (indice : slide 14, piège #4)

> **Rappel** : Google Rule of ML #1 — *"If you can build it without ML, do so first."* Le même principe s'applique à la GenAI.

---

<!-- _class: compact -->

# 16 — The Gmail Story — Le MVP comme méthodologie

<!-- TODO: Louis will present the Gmail story live — prepare slide with key points after discussion -->

Gmail a démarré comme **la chose la plus simple possible**.

**Principes du MVP appliqués à l'IA** :
- Quel est le **minimum** qui prouve la valeur ?
- Ce "minimum" est souvent plus petit qu'on imagine
- Le feedback utilisateur guide chaque itération

**Questions clés avant de construire** :
- Livrer de la valeur en **1 semaine** ?
- MVP nécessite-t-il du ML, ou un prompt suffit ?
- Quel **signal faible** valide votre hypothèse ?

> **Lean AI** : pas de modèle tant qu'un prompt ne marche pas. Pas de RAG tant que le prompt seul n'a pas atteint ses limites.

---

# 17 — Discussion : Canvas en action

> Votre startup fintech (30 personnes, 5M EUR CA, budget IA 150K EUR) a brainstormé **15 use cases**. Après filtrage, il en reste 7. Budget pour 2-3 maximum.

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

# Choisir sa stack

## Le choix stratégique de l'infrastructure

---

<!-- _class: cols -->

# 18 — Trois modèles d'accès aux LLMs

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

<!-- _class: img-right -->

# 19 — Le guide de décision

![bg right:55% contain](assets/infographics/decision-guide_run_20260216_171259_3f18b9.png)

Quatre niveaux d'investissement technique :

- **Prompting** — premier réflexe, suffisant pour la majorité des cas
- **RAG** — contexte spécifique manquant
- **Fine-tuning** — style ou savoir-faire particulier
- **Pretraining** — domaine totalement unique (rare, coûteux)

> **90%** des projets GenAI startup = Prompting + RAG [1].

<small>Sources : [1] Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0</small>

---

# 20 — L'écosystème open-source européen

- **Hugging Face** : Paris, **$4,5 Mds** valorisation, **1M+ modèles**, 400K datasets [1]
- **Mistral AI** : Paris, **EUR 11,7 Mds** valorisation, seul frontier UE [2]
- **n8n** : Berlin, **$2,5 Mds**, 100K+ stars, automatisation souveraine [3]
- **Lovable** : Stockholm, **$6,6 Mds**, vibe coding européen [4]

> L'écosystème IA open-source européen est **unique au monde** : les 2 plus grandes plateformes open-source (HF + Mistral) sont françaises. Un atout pour les entrepreneurs qui veulent allier innovation et souveraineté.

<small>Sources : [1] [Hugging Face](https://huggingface.co/) · [2] [Mistral AI](https://mistral.ai/) · [3] [n8n](https://n8n.io/) · [4] [TechCrunch](https://techcrunch.com/)</small>

---

# 21 — Combien coûte un appel API ?

| Modèle | Input (par 1M tokens) | Output (par 1M tokens) | Positionnement |
|---|---|---|---|
| GPT-4o | $2,50 | $10,00 | Premium, multimodal [1] |
| GPT-4o mini | $0,15 | $0,60 | Rapide, économique [1] |
| Claude 3.5 Sonnet | $3,00 | $15,00 | Raisonnement avancé [2] |
| Claude 3 Haiku | $0,25 | $1,25 | Rapide, bon marché [2] |
| Mistral Large | $2,00 | $6,00 | Souveraineté européenne [3] |
| Mistral Small | $0,10 | $0,30 | Ultra-économique [3] |

> Les prix chutent d'environ **~10x par an** à performance équivalente [4]. Le coût marginal de l'intelligence baisse drastiquement.

<small>Sources : [1] [OpenAI](https://openai.com/api/pricing/) · [2] [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) · [3] [Mistral AI](https://mistral.ai/pricing) · [4] [a16z](https://a16z.com/llmflation-llm-inference-cost/)</small>

---

<!-- _class: img-right compact-table -->

# 22 — Progression : Prompting → RAG → Fine-tuning

| Outil | Complexité | Coût | Quand l'utiliser |
|---|---|---|---|
| **Prompting** | Faible | Très faible | Toujours commencer ici |
| **RAG** | Moyenne | Faible | Connaissances spécifiques |
| **Fine-tuning** | Élevée | Moyen | Style ou savoir-faire spécialisé |
| **Pretraining** | Très élevée | Très élevé | Domaine ultra-spécialisé (rare) |

> Commencez par le Prompting. Montez en complexité uniquement si nécessaire.

![bg right:55% contain](assets/infographics/tool-decision_run_20260216_171316_911dd4.png)

---

<!-- _class: img-right -->

# 23 — Cas pratique : BettaBurgers

**Contexte** : BettaBurgers veut un chatbot pour prendre les commandes.

**Scope** : accueillir les clients, prendre la commande, confirmer.

**Build** → premier prompt avec le menu et les instructions.

**Evaluate** → test interne. Résultat :
- Le chatbot dit "pas de champignons" alors que c'est faux
- Il ne connaît pas les calories
- Il invente des promotions inexistantes

> Erreurs typiques : le LLM "hallucine" sans contexte. Solution : RAG avec le menu et les fiches produit.

![bg right:55% contain](assets/ng02/img-012.png)

---

<!-- _class: section -->

# Synthèse

## Choisir son parcours

---

<!-- _class: compact -->

# 24 — Trois phases, trois sets d'outils

**Phase 1 — Valider** (0-3 mois) :
- Use Case Prioritization, AI Project Canvas, MVP Prompt Engineering
- Budget : ~10-30K EUR, 1-2 pers., livrable en 1-4 semaines [1]

**Phase 2 — Construire** (3-12 mois) :
- ML Canvas, Build vs Buy, CRISP-DM ou LLMOps, ROI Framework
- Budget : 50-150K EUR, 3-5 pers., cycles de 2-4 semaines [1]

**Phase 3 — Scaler** (12+ mois) :
- Data Flywheel, FinOps, ISO 42001 / EU AI Act compliance

> **Commencez toujours par la Phase 1** — même si vous pensez connaître la réponse.

<small>Sources : [1] [Azilen — AI Development Cost 2025](https://www.azilen.com/blog/ai-development-cost/)</small>

---

# 25 — Key Takeaways

1. **Prompt-based Development** — de 7 mois à quelques jours, l'IA accessible à tous

2. **Lifecycle itératif** — Scope → Build → Evaluate → Deploy, retours en arrière constants

3. **CRISP-DM reste le standard** — 43% d'adoption, 25 ans de recul. LLMOps ajoute Guardrails + Observability

4. **Cadrez avant de coder** — 20 min d'AI Canvas économisent des mois

5. **Open Source européen** — Mistral et Hugging Face sont français. Souveraineté + RGPD

> **Prochaine séance** : choisissez un use case, remplissez l'AI Canvas, testez avec un MVP.
