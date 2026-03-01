---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Adapté de *Generative AI for Everyone* par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"
---
<!-- ABOUTME: Du prompt au produit — 4 catégories d'apps GenAI, lifecycle, prompt-based development, tokens, context windows et coûts. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : construire un premier produit IA, estimer les coûts, itérer rapidement. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Du Prompt au Produit

## Session 2A — Construire avec la Generative AI

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# De l'utilisation à la construction

## From Using to Building

---

# 01 — Quatre catégories d'applications GenAI

Les applications logicielles utilisant la Generative AI se classent en quatre familles :

| Catégorie | Ce que fait l'IA | Exemple concret |
|---|---|---|
| **Writing** | Génère du texte à partir d'instructions | FAQ bot, rédaction automatique |
| **Reading** | Analyse et classifie du contenu | Sentiment Analysis, extraction de données |
| **Chatting** | Dialogue interactif avec l'utilisateur | Chatbot de commande, support client |
| **Coding** | Génère, corrige et optimise du code | Copilot, Cursor, Claude Code |

> Ces quatre catégories se retrouvent dans presque tous les produits IA que vous utilisez au quotidien. Le Coding est devenu une famille à part entière en 2025.

---

# 02 — L'ancienne approche : Supervised Learning

Pour construire un classifieur de sentiment, il fallait :

1. **Collecter des données labellisées** — des milliers d'exemples annotés
2. **Entraîner un modèle** — écrire du code spécialisé (LSTM, Transformers...)
3. **Déployer le modèle** — infrastructure serveur, monitoring

**Durée typique** : ~6–12 mois (1 mois données + 3 mois entraînement + 3 mois déploiement) [1]

> Ce processus nécessitait une équipe d'ingénieurs ML et un budget significatif. Et le déploiement n'est que le début : la "hidden technical debt" [2] — maintenance, monitoring, data pipelines — représente la majorité du travail.

![bg right:45% contain](assets/hidden-technical-debt.png)

<small>Sources : [1] [Andrew Ng, *Generative AI for Everyone*, DeepLearning.AI](https://www.coursera.org/learn/generative-ai-for-everyone) · [2] [Sculley et al. NeurIPS 2015](https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf)</small>

---

# 03 — La révolution : Prompt-based Development

Avec la Generative AI, le même classifieur de sentiment s'écrit en **3 lignes** :

```
prompt = """
  Classify the following review as positive or negative:
  The banana pudding was really tasty!
"""
response = llm_response(prompt)
```

**Durée typique** : minutes à heures pour le prompt, heures à jours pour le déploiement

> Pas besoin de données labellisées, pas besoin d'entraîner un modèle. Vous décrivez la tâche en langage naturel.

![bg right:45% contain](assets/ng02/img-010.png)

---

<!-- _class: cols -->

# 04 — 7 mois vs. quelques jours

<div class="left">

### Supervised Learning

- Données labellisées (1 mois) + entraînement (3 mois) + déploiement (3 mois)
- **Total : ~7 mois** — nécessite une équipe ML

</div>
<div class="right">

### Prompt-based AI

- Écrire et tester le prompt — **minutes/heures**
- Déployer — **heures/jours**
- **Total : quelques jours** — un entrepreneur peut le faire seul

</div>

> C'est **l'argument business le plus puissant** pour la Generative AI : elle démocratise la construction d'applications IA.

---

# 05 — Ce que cela change pour les entrepreneurs

<!-- INSTRUCTOR: Réponses attendues pour la question :
- L'avantage concurrentiel se déplace vers la COMPRÉHENSION DU PROBLÈME et la QUALITÉ DES DONNÉES
- La technologie est commoditisée — tout le monde a accès aux mêmes APIs
- Ce qui différencie : connaissance du domaine, relation client, qualité du pipeline de données, rapidité d'itération
- Exemples : Perplexity (meilleure UX de recherche), Harvey (expertise juridique), Cursor (comprend le workflow dev)
- Piège classique : penser que "wrapper GPT" = startup viable — sans valeur ajoutée propre, pas de moat
-->

Le Prompt-based Development transforme l'équation économique :

- **Coût d'entrée quasi nul** — plus besoin de lever des fonds pour une équipe ML
- **Time-to-market réduit** — prototyper un produit IA en un week-end
- **Itération rapide** — modifier un prompt prend des minutes, pas des mois
- **Compétence clé = comprendre le problème** — pas coder un algorithme

**Exemples en 2025-2026** :
- Des startups lancent des MVP IA en quelques jours sur Replit, Vercel, Streamlit
- Mistral AI propose une API compétitive pour les startups européennes

> **Question pour la classe** : Si construire une app IA prend des jours au lieu de mois, qu'est-ce qui devient votre véritable avantage concurrentiel ?

---

<!-- _class: section -->

# Le cycle de vie d'un projet GenAI

## GenAI Project Lifecycle

---

# 06 — Les quatre étapes du Lifecycle

Tout projet Generative AI suit un cycle itératif en 4 phases :

1. **Scope** — Définir le projet et ses objectifs
2. **Build** — Construire le système (prompt, pipeline)
3. **Evaluate** — Tester en interne, détecter les erreurs
4. **Deploy** — Mettre en production, surveiller

> Ce n'est **pas un processus linéaire**. Les retours entre étapes sont la norme.

![bg right:50% contain](assets/infographics/genai-lifecycle_run_20260216_171314_f23e16.png)

---

# 07 — Scope — Bien cadrer le projet

Le cadrage est l'étape la plus critique. Un mauvais scope = un projet qui échoue.

**Questions à se poser** :
- Quel problème business précis résout-on ?
- Qui est l'utilisateur final ?
- Comment mesurer le succès ? (métriques claires)
- Quel niveau de qualité est acceptable ?

**Mesurer le succès** — Définir des KPIs dès le scope :
- *Précision* : % de réponses correctes (détaillé en Session 3 avec Precision/Recall)
- *Satisfaction utilisateur* : NPS, taux de résolution au premier contact
- *ROI* : coût IA vs coût du processus manuel remplacé

> **Conseil pratique** : commencez par le cas d'usage le plus simple qui apporte de la valeur. Vous pourrez toujours élargir ensuite.

---

# 08 — Build — Un processus empirique

Construire avec la Generative AI est un processus **hautement expérimental** :

- On écrit un prompt, on teste, on corrige, on itère
- Le cycle **Idea → Prompt → LLM Response** se répète des dizaines de fois
- Chaque itération prend des minutes (pas des semaines)

**Le prototype initial ne sera pas parfait** — et c'est normal. L'objectif est de progresser rapidement vers une version fonctionnelle.

> Pensez au Lean Startup : Build → Measure → Learn. C'est exactement la même logique appliquée à l'IA.

![bg right:45% contain](assets/ng02/img-011.png)

---

# 09 — Evaluate — Tester avant de déployer

L'évaluation interne permet de **détecter les erreurs avant vos clients** :

- Faire tester le système par votre équipe
- Créer un jeu de tests représentatifs
- Identifier les cas limites (Edge Cases)
- Mesurer la précision sur vos métriques

**Exemple** : un chatbot qui classe "My pasta was cold" comme positif — erreur détectable en évaluation interne.

> Quand l'évaluation révèle des erreurs, on **retourne à l'étape Build** pour améliorer le prompt ou ajouter du contexte. C'est la boucle de feedback.

---

# 10 — Deploy — Mettre en production intelligemment

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

# 11 — Cas pratique : BettaBurgers

**Contexte** : BettaBurgers veut un chatbot pour prendre les commandes en ligne.

**Scope** : le chatbot doit accueillir les clients, prendre leur commande, et confirmer.

**Build** → l'équipe écrit un premier prompt avec le menu et les instructions.

**Evaluate** → l'équipe teste en interne. Résultat :
- Le chatbot dit "nous n'avons pas de champignons" alors que c'est faux
- Il ne connaît pas les calories des produits
- Il invente des promotions qui n'existent pas

> Ces erreurs sont typiques : le LLM "hallucine" quand il manque d'informations contextuelles.

![bg right:40% contain](assets/ng02/img-012.png)

---

# 12 — Lifecycle : les erreurs classiques

<!-- INSTRUCTOR: Réponses attendues pour la question :
- Test 1 : soumettre des cas CONNUS avec réponses attendues (regression test)
- Test 2 : soumettre des cas LIMITES (questions hors-scope, requêtes ambiguës, injections de prompt)
- Test 3 : mesurer le TEMPS DE RÉPONSE et la COHÉRENCE sur 100+ requêtes
- Bonus : tester le chatbot avec de VRAIS utilisateurs internes avant les clients
- Piège : ne tester que les cas "happy path" — les erreurs sont dans les edge cases
- Métriques à suivre : taux de résolution, taux d'escalade vers un humain, satisfaction post-interaction
-->

| Erreur | Conséquence | Solution |
|---|---|---|
| Scope trop large | Projet qui n'aboutit jamais | Cibler une seule tâche précise |
| Pas d'évaluation | Bugs découverts par les clients | Tester avec des cas réels |
| Déploiement "big bang" | Crise si le système hallucine | Déployer progressivement |
| Pas de monitoring | Dégradation silencieuse | Alertes + revue régulière |

> **Question pour la classe** : Vous lancez un chatbot de support client pour votre startup. Quels sont les 3 premiers tests que vous feriez en évaluation interne ?

---

<!-- _class: section -->

# Coûts des APIs

## Comprendre la facturation des LLMs

---

# 13 — Combien coûte un appel API ?

| Modèle | Input (par 1M tokens) | Output (par 1M tokens) | Positionnement |
|---|---|---|---|
| GPT-4o | $2,50 | $10,00 | Premium, multimodal [1] |
| GPT-4o mini | $0,15 | $0,60 | Rapide, économique [1] |
| Claude 3.5 Sonnet | $3,00 | $15,00 | Raisonnement avancé [2] |
| Claude 3 Haiku | $0,25 | $1,25 | Rapide, bon marché [2] |
| Mistral Large | $2,00 | $6,00 | Souveraineté européenne [3] |
| Mistral Small | $0,10 | $0,30 | Ultra-économique [3] |

> Les prix chutent d'environ **~10x par an** à performance équivalente [4]. La tendance continue : le coût marginal de l'intelligence baisse drastiquement.

<small>Sources : [1] [OpenAI](https://openai.com/api/pricing/) · [2] [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) · [3] [Mistral AI](https://mistral.ai/pricing) · [4] [a16z](https://a16z.com/llmflation-llm-inference-cost/)</small>

---

# 14 — Exercice : estimer le coût d'un produit IA

**Scénario** : un chatbot de support client, 1 000 conversations/jour.

**Hypothèses** :
- Conversation moyenne : ~500 mots input + ~300 mots output
- ~670 tokens input + ~400 tokens output par conversation

**Avec GPT-4o mini** :
- Input : 670K tokens/jour × $0,15/1M = **$0,10/jour**
- Output : 400K tokens/jour × $0,60/1M = **$0,24/jour**
- **Total : ~$0,34/jour soit ~$10/mois**

> Pour 1 000 conversations par jour, le coût IA est de **$10/mois**. Comparez avec le coût d'un agent humain (~$3 000/mois).

---

# 15 — Les outils pour améliorer la performance

Quand le Prompting seul ne suffit pas, il existe une progression :

| Outil | Complexité | Coût | Quand l'utiliser |
|---|---|---|---|
| **Prompting** | Faible | Très faible | Toujours commencer ici |
| **RAG** | Moyenne | Faible | Besoin de connaissances spécifiques |
| **Fine-tuning** | Élevée | Moyen | Style ou savoir-faire spécialisé |
| **Pretraining** | Très élevée | Très élevé | Domaine ultra-spécialisé (rare) |

> **Règle d'or** : commencez toujours par le Prompting. Montez en complexité uniquement si nécessaire.

---

# 16 — Guide de décision : quel outil pour votre projet ?

L'arbre de décision suit une logique d'escalade progressive :

- *Prompting* → premier réflexe, toujours commencer ici
- *RAG* → si le modèle manque de contexte spécifique
- *Fine-tuning* → si le modèle a besoin d'un style ou format précis
- *Pretraining* → domaine ultra-spécialisé (rare)

> **90%** des projets GenAI en startup se résolvent avec Prompting + RAG [1].

![bg right:55% contain](assets/infographics/tool-decision_run_20260216_171316_911dd4.png)

<small>Sources : [1] Adapté de *Generative AI for Everyone* par Andrew Ng · [DeepLearning.AI](https://www.coursera.org/learn/generative-ai-for-everyone) · CC BY-SA 2.0</small>

---

# 17 — Les 5 messages clés

1. **Le Prompt-based Development réduit le time-to-market de mois à jours** — l'IA n'est plus réservée aux grandes entreprises

2. **Le Lifecycle est itératif** — Scope → Build → Evaluate → Deploy, avec des retours en arrière constants

3. **Le coût marginal de l'IA est très faible** — un chatbot peut coûter $10/mois pour 1 000 conversations/jour

4. **Commencez simple, montez en complexité** — Prompting → RAG → Fine-tuning → Pretraining

5. **Votre avantage compétitif = votre compréhension du problème** — pas la technologie elle-même

---

# 18 — Pour la suite

**Deck B — L'ingénierie IA** :
- Comment fonctionne le RAG en profondeur (Embeddings, Vector Databases)
- Quand et pourquoi faire du Fine-tuning
- Les agents IA : architecture, outils, limites

> Passons de la stratégie à la mécanique : comprendre les briques techniques pour faire les bons choix.
