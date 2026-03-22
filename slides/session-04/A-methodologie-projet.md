---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 4 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Méthodologie projet IA — Bitter Lesson, prompt-based development, lifecycle, MVP patterns, pièges et Gmail story. -->
<!-- ABOUTME: Deck A de la Session 4, cadré pour entrepreneurs M2 non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Méthodologie projet IA

## Session 4A — Du cadrage au déploiement

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: compact -->

# 01 — The Bitter Lesson

Richard Sutton (2019) résume **70 ans de recherche en IA** en une leçon :

> *"General methods that leverage computation are ultimately the most effective, and by a large margin."*

**Le pattern récurrent** :
- Les chercheurs encodent du savoir humain → ça marche **à court terme**, puis ça plafonne
- Les méthodes générales (Search + Learning) finissent **toujours** par gagner
- Pourquoi ? **Moore's Law** : le compute double tous les ~2 ans

**Exemples** : Chess (Deep Blue), Go (AlphaGo), Speech (HMMs → Deep Learning), Vision (SIFT → CNNs → VLMs)

> **Pour les entrepreneurs** : les plateformes générales (GPT, Claude, Gemini) battent les solutions sur-mesure. Pariez sur le compute, pas sur l'ingénierie manuelle.

<small>Sources : [1] [Richard Sutton — The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html)</small>

---

<!-- _class: img-right -->

# 02 — Exemple : la Vision par ordinateur, avant et maintenant

**Avant (2015)** — Détection de genre sur une photo :
- Collecter des **milliers d'images** labelisées
- Entraîner un **1er modèle** (détection de visage)
- Entraîner un **2e modèle** (classification genre)
- Pipeline complexe, **6–12 mois** de travail

**Maintenant (2025)** — Même tâche :
- Image → VLM → Structured Output
- **0 entraînement**, **0 données**, **~1 jour**
- Performance compétitive

> The Bitter Lesson en action : le compute général a remplacé l'ingénierie spécialisée.

![bg right:55% contain](assets/infographics/cv-before-vs-now_run_20260322_155403_87a8f5.png)

<small>Sources : [1] [Andrew Ng — ML Specialization](https://www.youtube.com/watch?v=c3zw6KI6dLc&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=22)</small>

---

# 03 — La révolution : Prompt-based Development

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

<!-- _class: section -->

# Le cycle projet IA

## Scope, Build, Evaluate, Deploy

---

<!-- _class: img-right -->

# 04 — Le GenAI Lifecycle : Scope → Build → Evaluate → Deploy

Tout projet GenAI suit un cycle itératif en 4 phases :

1. **Scope** — Définir le projet et ses objectifs
2. **Build** — Construire le système (prompt, pipeline)
3. **Evaluate** — Tester en interne, détecter les erreurs
4. **Deploy** — Mettre en production, surveiller

> Ce n'est **pas linéaire**. Les retours entre étapes sont la norme.

![bg right:55% contain](assets/infographics/genai-lifecycle_run_20260216_171314_f23e16.png)

---

<!-- _class: compact -->

# 05 — Scope — Bien cadrer le projet

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

# 06 — Build — Un processus empirique

Construire avec la GenAI est **hautement expérimental** :

- Écrire un prompt, tester, corriger, itérer
- Le cycle **Idea → Prompt → LLM Response** se répète des dizaines de fois
- Chaque itération prend des minutes, pas des semaines

**Le prototype initial ne sera pas parfait** — et c'est normal. L'objectif : progresser vite vers une version fonctionnelle.

> Lean Startup : Build → Measure → Learn — même logique appliquée à l'IA.

![bg right:55% contain](assets/ng02/img-011.png)

---

# 07 — Evaluate — Tester avant de déployer

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

# 08 — Deploy — Mettre en production intelligemment

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

# 09 — Première itération : le baseline

La première itération est différente — l'objectif est d'avoir un **point de référence**, pas un bon modèle.

**Le "AI toy model"** :
- **Classification** → prédire la classe majoritaire (ex : si 70% des emails sont "non-spam", toujours prédire "non-spam")
- **Régression** → prédire la valeur moyenne (ex : prix moyen des appartements)

**Commencer petit** :
- Constituer un dataset initial de **~20 exemples** représentatifs
- Ce baseline "stupide" donne un **score plancher** à battre
- Il révèle immédiatement si vos métriques et votre pipeline d'évaluation fonctionnent

> Un baseline en 1 jour vaut mieux qu'un modèle parfait dans 3 mois. Si votre baseline bat déjà les attentes, peut-être que le ML n'est pas nécessaire.

---

# 10 — Itérer sur le baseline

Une fois le baseline en place, améliorer par **itérations successives** :

**Le cycle Build / Evaluate** :
- Modifier le système (prompt, modèle, pipeline)
- Évaluer → garder le changement **uniquement s'il améliore le score**
- La complexité ne se justifie que si elle apporte un gain mesurable

**Enrichir le dataset au fil du temps** :
- Un cas manqué en production ? → Ajoutez-le au dataset de test
- Une prédiction incorrecte ? → Ajoutez l'exemple corrigé
- Couverture insuffisante ? → Ajoutez des exemples du domaine sous-représenté

> **Principe** : chaque erreur en production est une opportunité d'amélioration du dataset. Le modèle s'améliore par la boucle de feedback, pas par la complexité architecturale.

---

<!-- _class: section -->

# Du prototype à la production

## MVP, pièges et progression

---

# 11 — MVP Patterns : valider avant d'investir

Avant de construire un modèle, **5 patterns** pour tester la valeur [1] :

| Pattern | Principe | Coût | Exemple |
|---------|----------|------|---------|
| **Wizard of Oz** | Humain derrière le rideau | EUR EUR | Un expert répond comme le ferait l'IA |
| **Concierge** | Service manuel, promesse automatique | EUR EUR | Analyse de contrats faite "a la main" |
| **Rule-Based First** | Règles simples avant le ML | EUR | Filtrage par mots-clés avant NLP |
| **Prompt Eng. MVP** | LLM via API, zero-code | EUR | Prototype GPT-4o en 1 journée |
| **API Wrapper** | Assemblage d'APIs existantes | EUR EUR | Combine OCR + LLM + CRM |

> **Google "Rule of ML #1"** : si vous pouvez résoudre le problème sans ML, faites-le d'abord [2].

<small>Sources : [1] [MIT Sloan](https://sloanreview.mit.edu/article/what-is-a-minimum-viable-ai-product/) · [2] [Google Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml) · [3] [YC — Startup Ideas](https://www.youtube.com/watch?v=0kARDVL2nZg) · [4] [YC — Build an MVP](https://www.youtube.com/watch?v=1hHMwLxN6EM)</small>

---

# 12 — Construire un MVP : les ingrédients

Un MVP n'est **pas** une version dégradée du produit final — c'est le **test le plus simple** de votre hypothèse.

**Les 3 ingrédients** :
- **Hypothèse claire** — "Les recruteurs gagneront 2h/jour si l'IA pré-filtre les CVs"
- **Métrique de succès** — taux de filtrage correct, temps gagné, NPS
- **Time-box** — 1-2 semaines max. Si c'est plus long, votre scope est trop large

**L'anti-pattern "faux MVP"** :
- Construire "le produit" mais en l'appelant MVP
- Ajouter des features "au cas où"
- Oublier de mesurer

> **Gmail** : version zero = 1 feature (recherche email), 1 jour, code réutilisé. Le reste est venu après validation.

---

# 13 — Prototypage rapide d'agents

La plupart des équipes **perdent des mois** à construire l'infrastructure agent avant de valider l'idée [1].

**L'approche Jason Liu** — tester avec Claude Code comme harness :
- `CLAUDE.md` = spécification en langage naturel (mission, outils, critères de succès)
- `tools/` = scripts CLI wrappant les APIs réelles
- `tests/` = scénarios avec `request.txt` (input) + `check.py` (validation pass/fail)

**Le test décisif** : si Claude Code ne peut pas accomplir la tâche avec un accès parfait aux outils, votre agent de production ne le pourra pas non plus.

> C'est le **Prompt Engineering MVP** (slide 11) appliqué aux agents. Un test passant = concept validé [1].

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

<!-- _class: img-right compact-table -->

# 15 — Progression : Prompting → RAG → Fine-tuning

| Outil | Complexité | Coût | Quand l'utiliser |
|---|---|---|---|
| **Prompting** | Faible | Très faible | Toujours commencer ici |
| **RAG** | Moyenne | Faible | Connaissances spécifiques |
| **Fine-tuning** | Élevée | Moyen | Style ou savoir-faire spécialisé |
| **Pretraining** | Très élevée | Très élevé | Domaine ultra-spécialisé (rare) |

> Commencez par le Prompting. Montez en complexité uniquement si nécessaire.

![bg right:55% contain](assets/infographics/tool-decision_run_20260216_171316_911dd4.png)

---

<!-- _class: compact -->

# 16 — The Gmail Story — Le MVP comme méthodologie

Paul Buchheit (Google, employé #23) a écrit **Gmail v0 en un jour** — en réutilisant le code de Google Groups pour chercher dans ses propres emails [1].

**Les principes de Buchheit** :
- **"Version zero" = résoudre un seul problème** — Gmail v0 ne faisait que de la recherche d'emails
- **Code toujours live** — 6 réécritures du frontend, 3 du backend, mais toujours avec des vrais utilisateurs
- **Trois features, pas plus** — Gmail = vitesse + stockage illimité (1 Go vs 2-4 Mo chez Yahoo) + conversations

**Le bonus** : AdSense est né d'un prototype "d'une mauvaise idée" codé en une soirée. Résultat : un business à plusieurs milliards de dollars [1].

> *"Pick three key attributes, get those things very, very right, and forget about everything else."* — Paul Buchheit

<small>Sources : [1] [Paul Buchheit — YC Startup Library](https://www.ycombinator.com/library/Jc-paul-buchheit-creator-of-gmail)</small>

---

<!-- _class: section -->

# Synthèse

---

# 17 — Key Takeaways

1. **The Bitter Lesson** — les méthodes générales + compute battent toujours l'ingénierie manuelle. Pariez sur les plateformes, pas sur le sur-mesure

2. **Prompt-based Development** — de 6-12 mois à quelques jours, l'IA est accessible à tous

3. **Lifecycle itératif** — Scope → Build → Evaluate → Deploy, avec des retours constants

4. **Baseline d'abord** — commencez par le modèle le plus simple (classe majoritaire, valeur moyenne), puis itérez en gardant uniquement ce qui améliore le score

5. **MVP avant le modèle** — Wizard of Oz, Prompt Engineering MVP, ou Rule-Based First. Validez la valeur avant d'investir

6. **Gmail = 3 features** — vitesse, stockage, conversations. Oubliez le reste

> **Prochaine étape** : choisissez un use case, testez avec un MVP, mesurez.
