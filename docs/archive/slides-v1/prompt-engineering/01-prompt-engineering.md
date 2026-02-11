---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Prompt Engineering 2024–2026 · Données publiques"
---

<!-- ABOUTME: Prompt Engineering avancé — 30 techniques en 8 familles, du Chain-of-Thought à la sécurité. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : comprendre, optimiser, sécuriser ses interactions avec les LLM. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Prompt Engineering Avancé

## 30 techniques pour maîtriser vos interactions IA

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Le nouveau paradigme

## Du prompt au contexte

---

# 01 — Du Prompt Engineering au Context Engineering

Le paradigme a changé : la qualité d'une réponse IA dépend à **80%** du contexte fourni, pas de la formulation [1]

- **Prompt Engineering** : "comment formuler ma question"
- **Context Engineering** : "quelles informations le modèle a-t-il besoin pour répondre"
- **57%** des organisations ont des agents en production — le contexte inclut désormais outils, mémoire, données [2]

> Tobi Lütke (CEO Shopify) a popularisé le terme "Context Engineering" en juin 2025 : assembler l'environnement d'information complet pour le modèle.

- Andrej Karpathy a validé cette vision : le vrai travail est en amont du prompt [1]

<small>Sources : [1] [Karpathy / Lütke sur X](https://x.com/) · [2] [LangChain State of AI Agents 2025](https://langchain.com/)</small>

---

# 02 — 30 techniques en 8 familles

| Famille | Exemples | Difficulté | Métrique clé |
|---------|----------|-----------|--------------|
| **Core Prompting** (4) | CoT, Few-Shot, System Prompts, Structured Output | Débutant | +78% accuracy (CoT) |
| **Raisonnement avancé** (4) | ToT, ReAct, Meta-Prompting, Claude techniques | Intermédiaire | +34% accuracy (ReAct) |
| **Orchestration** (3) | Chaining, Routing, Ensemble | Intermédiaire | 85% économies (Routing) |
| **Optimisation** (5) | DSPy, OPRO, Caching, Compression, Prompt Mgmt | Avancé | 90% économies (Caching) |
| **Sécurité** (5) | Injection, Jailbreaking, Défenses, Red Teaming, Hierarchy | Intermédiaire | #1 OWASP (Injection) |
| **Évaluation** (3) | LLM-as-Judge, Promptfoo, Guardrails | Intermédiaire | 95% moins cher (Judge) |
| **Context Eng.** (3) | Context Eng., MCP, Long Context | Intermédiaire | 10K+ serveurs MCP |
| **Tendances** (3) | Thinking Models, Code Gen, PII Prevention | Variable | +40 pts accuracy (o3) |

---

<!-- _class: section -->

# Les fondamentaux

## Les 4 techniques essentielles

---

# 03 — Core Prompting : les 4 essentiels

| Technique | Principe | Métrique clé | Coût |
|-----------|----------|-------------|------|
| **Chain-of-Thought** | "Réfléchis étape par étape" | 17% → 78% accuracy [1] | 2-5x tokens |
| **Few-Shot Learning** | Exemples dans le prompt | +5-15% vs zero-shot [2] | +tokens par exemple |
| **System Prompts** | Persona + instructions | +37% avec persona ciblée [3] | Fixe (cacheable) |
| **Structured Output** | JSON/XML garanti | 100% schema compliance [4] | Négligeable |

- Few-Shot "many-shot" : avec 1M tokens de contexte, on peut fournir des centaines d'exemples [2]
- System Prompts : 1 000 tokens × 1M requêtes/jour = **$2 500/jour** sans caching [3]
- Structured Output natif chez OpenAI (août 2024), Anthropic (bêta nov 2025), Google [4]

<small>Sources : [1] [Wei et al. 2022](https://arxiv.org/abs/2201.11903) · [2] [Brown et al. 2020](https://arxiv.org/abs/2005.14165) · [3] [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering) · [4] [OpenAI Structured Outputs](https://openai.com/index/introducing-structured-outputs-in-the-api/)</small>

---

<!-- _class: cols -->

# 04 — Spotlight : Chain-of-Thought

<div class="left">

- MultiArith : **17,7% → 78,7%** [1]
- Commonsense : **95,4%** (> humain 84%)
- Coût : **2-5x** plus de tokens
- Zero-shot : "Let's think step by step"

</div>
<div class="right">

- Reasoning models (o3, R1) : CoT **natif**
- Gain marginal seulement **+2,9%** sur o3 [2]
- Quand utiliser : raisonnement multi-étapes
- Quand éviter : tâches simples, extraction
- Le ROI dépend de la **complexité** du task

</div>

<small>Sources : [1] [Wei et al. NeurIPS 2022](https://arxiv.org/abs/2201.11903) · [2] [Wharton 2025](https://arxiv.org/)</small>

---

# 05 — Discussion : Précision vs coût

> Votre startup de **LegalTech** utilise un LLM pour analyser des contrats. En mode standard, le modèle fait **40% d'erreurs** sur les clauses critiques. Avec Chain-of-Thought, la précision monte à **90%** — mais le coût passe de **€0,02** à **€0,06** par contrat (3x).

**Questions pour la classe** :
- À quel volume cette différence de coût devient-elle significative ? (100 contrats/jour ? 10 000 ?)
- Une erreur sur une clause critique peut coûter combien à votre client ?
- Peut-on utiliser CoT sélectivement — seulement sur les clauses à risque ?

---

<!-- _class: section -->

# Patterns avancés & orchestration

## Raisonnement, agents, pipelines

---

# 06 — Raisonnement avancé : ToT, ReAct, Meta-Prompting

| Technique | Principe | Performance | Coût |
|-----------|----------|------------|------|
| **Tree-of-Thoughts** | Explore plusieurs chemins de raisonnement | 4% → **74%** (Game of 24) [1] | 10-30x API calls |
| **ReAct** | Boucle Thought → Action → Observation | +**34%** vs Act-only [2] | 3-5x tokens |
| **Meta-Prompting** | Le LLM génère/optimise ses propres prompts | Égale ou dépasse humain sur 19/24 tasks [3] | Coût d'optimisation |

- **ReAct** est le pattern fondateur des agents IA — utilisé par LangChain, Claude, GPT [2]
- **ToT** est réservé aux problèmes complexes : un seul problème peut coûter **$0,10-$1,00+** [1]
- **Meta-Prompting** : consoles Anthropic et OpenAI le proposent gratuitement [3]

<small>Sources : [1] [Yao et al. NeurIPS 2023](https://arxiv.org/abs/2305.10601) · [2] [Yao et al. ICLR 2023](https://arxiv.org/abs/2210.03629) · [3] [Zhou et al. 2022](https://arxiv.org/abs/2211.01910)</small>

---

<!-- _class: cols -->

# 07 — Spotlight : ReAct — la boucle des agents IA

<div class="left">

- Boucle : **Think → Act → Observe** [1]
- FEVER fact-check : **60,9%** vs 56,3% CoT
- ALFWorld : **71%** vs 45% Act-only
- Réduit les hallucinations via vérification

</div>
<div class="right">

- **57%** des orgs ont des agents en production [2]
- LangChain : **120K** stars, $125M levés
- Claude tool use : ReAct natif
- Coût : 3-5x tokens vs prompt direct
- Le pattern le plus déployé en entreprise

</div>

<small>Sources : [1] [Yao et al. ICLR 2023](https://arxiv.org/abs/2210.03629) · [2] [LangChain State of AI Agents 2025](https://langchain.com/)</small>

---

# 08 — Orchestration : chaining, routing, ensemble

| Technique | Principe | Gain | Coût |
|-----------|----------|------|------|
| **Prompt Chaining** | Pipeline séquentiel multi-étapes | 35% → **8%** erreurs [1] | 2-4x tokens |
| **Routing** | Diriger vers le bon modèle | **85%** économies, 95% qualité [2] | <$0,01/10K requêtes |
| **Ensemble** | N réponses + vote majoritaire | 82% → **96%** accuracy [3] | N × coût unitaire |

- **Chaining** : utiliser GPT-4o-mini pour les étapes simples, Opus pour le raisonnement [1]
- **RouteLLM** : 70% des requêtes vers le modèle léger = **~$2 000/jour** d'économies sur 100K requêtes [2]
- **Ensemble** : DeepSeek-R1 passe de 79,8% à **86,7%** avec majority voting [3]

<small>Sources : [1] [Anthropic Docs](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-prompts) · [2] [RouteLLM ICLR 2025](https://lmsys.org/blog/2024-07-01-routellm/) · [3] [Wang et al. ICLR 2023](https://arxiv.org/abs/2203.11171)</small>

---

# 09 — Discussion : Architecturer un pipeline LLM

> Votre SaaS de recrutement analyse **500 CV/jour**. En single prompt, le taux d'erreur est de **35%** (mauvais matching candidat-poste). Avec un pipeline chaîné (extraction → scoring → ranking), les erreurs tombent à **8%** — mais le coût passe de **€0,05** à **€0,15** par CV.

**Questions pour la classe** :
- À €2/CV vendu au client, quel pipeline est le plus rentable ?
- Comment utiliser le routing pour envoyer les CV "évidents" au modèle léger et les cas ambigus à GPT-4 ?
- À quel volume (1K ? 10K ? 100K CV/jour) l'optimisation du pipeline devient-elle critique ?

---

<!-- _class: section -->

# Optimisation & production

## Coûts, caching, automatisation

---

# 10 — Token Economics : le nerf de la guerre

| Modèle | Input (/M tokens) | Output (/M tokens) | Cas d'usage |
|--------|-------------------|---------------------|-------------|
| GPT-4o | $2,50 | $10,00 | Raisonnement, analyse |
| GPT-4o-mini | $0,15 | $0,60 | Routing, classification |
| Claude Sonnet 4.5 | $3,00 | $15,00 | Code, analyse complexe |
| o3 | $2,00 | $8,00 | Raisonnement avancé (5-30x tokens internes) |
| DeepSeek-R1 | $0,55 | $2,19 | Raisonnement open-source |

- Un prompt de **10K tokens** × **1M requêtes/jour** = **$25 000/jour** en GPT-4o [1]
- Les reasoning models consomment **5-30x** plus de tokens en réflexion interne [2]
- Optimiser = choisir le bon modèle × cacher × compresser × router

<small>Sources : [1] [OpenAI Pricing](https://openai.com/pricing) · [2] [Anthropic Pricing](https://www.anthropic.com/pricing)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Prompt Caching — 90% d'économies

<div class="left">

- **Anthropic** : 90% économies, TTL 5 min [1]
- **OpenAI** : 50% discount, automatique [2]
- **Google** : 75-90% discount [3]
- Rentable dès la **2e requête**
- Seuil : 1 024 tokens minimum

</div>
<div class="right">

- Cas réel : **$45K → $8K/mois** (82%) [1]
- Dev solo : **$720 → $72/mois** (90%)
- Enterprise : **$40K/mois** d'économies
- Agentic Plan Caching : **-50%** coût, **-27%** latence [1]

</div>

<small>Sources : [1] [Anthropic Caching](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching) · [2] [OpenAI](https://platform.openai.com/docs/) · [3] [Google Gemini](https://ai.google.dev/pricing)</small>

---

# 12 — L'optimisation automatique : DSPy, OPRO, EvoPrompt

| Framework | Principe | Performance | Coût/run |
|-----------|----------|------------|---------|
| **DSPy** (Stanford) | Compile les prompts comme du code | 33% → **82%** (GSM8K) [1] | $3-50 |
| **OPRO** (DeepMind) | Le LLM optimise son propre prompt | +**50%** sur Big-Bench Hard [2] | 100-1 000 appels |
| **EvoPrompt** (Tsinghua) | Algorithme évolutionnaire sur prompts | +**25%** sur tâches BBH [3] | Similaire OPRO |
| **TextGrad** (Stanford) | Backpropagation textuelle | 7% → **23%** coding [4] | Variable |

- DSPy : **29K+** stars GitHub, **160K+** téléchargements/mois pip [1]
- TextGrad : publié dans **Nature** (mars 2025), 7K+ stars [4]
- Le futur du Prompt Engineering = **compilation**, pas artisanat

<small>Sources : [1] [DSPy ICLR 2024](https://arxiv.org/abs/2310.03714) · [2] [OPRO ICLR 2024](https://arxiv.org/abs/2309.03409) · [3] [EvoPrompt ICLR 2024](https://arxiv.org/) · [4] [TextGrad Nature 2025](https://doi.org/10.1038/s41586-025-08661-4)</small>

---

# 13 — Prompt Management & Compression

| Outil | Type | Différenciateur | Prix |
|-------|------|----------------|------|
| **PromptLayer** | Management | SOC2/HIPAA, YC W23 | Freemium |
| **Braintrust** | Eval + Mgmt | Notion/Stripe l'utilisent, $45M levés | Freemium |
| **Portkey** | Gateway | 1 600+ modèles, cache sémantique | $49/mois |
| **Langfuse** | Observabilité | Open-source (MIT), acquis par ClickHouse | Gratuit (self-host) |
| **Promptfoo** | Testing | 200K+ devs, 80+ Fortune 500, MIT | Gratuit |

- **LLMLingua** (Microsoft) : compression **2-20x** avec seulement 1,5% de perte de qualité [1]
- Humanloop acquis par Anthropic (août 2025), fermé en septembre — **risque vendor lock-in** [2]

<small>Sources : [1] [LLMLingua](https://github.com/microsoft/LLMLingua) · [2] [Braintrust](https://www.braintrust.dev/articles/best-prompt-management-tools-2026)</small>

---

# 14 — Discussion : Artisan vs machine

> DSPy peut optimiser automatiquement un prompt et passer de **33% à 82%** de précision sur des tâches mathématiques — pour **$3 par run**. TextGrad, publié dans Nature, fait de la "backpropagation textuelle". Pendant ce temps, le métier de "Prompt Engineer" existe toujours avec des salaires de **$150-300K/an**.

**Questions pour la classe** :
- Si un algorithme optimise mieux qu'un humain, où est la valeur ajoutée du Prompt Engineer ?
- La réponse est-elle dans le **Context Engineering** — assembler les bonnes données, pas formuler le bon prompt ?
- Quel parallèle avec l'évolution des développeurs face aux agents de code ?

---

<!-- _class: section -->

# Sécurité & évaluation

## Attaques, défenses, tests

---

# 15 — Menaces : injection, jailbreaking, leakage

| Menace | Gravité | Métrique clé | Impact business |
|--------|---------|-------------|----------------|
| **Prompt Injection** | #1 OWASP [1] | 10% succès (filtres basiques) | Chevrolet : Tahoe à $1 [1] |
| **Jailbreaking** | Élevée | 42 sec en moyenne [2] | OpenAI : amende €15M (Italie) [2] |
| **PII Leakage** | Critique | 11% des données soumises sont confidentielles [3] | Samsung : ban total post-fuite [3] |

- **Pangea** : 300K+ tentatives d'injection analysées, 10% réussissent malgré les filtres [1]
- **DAN prompts** : 0,95 de taux de succès, persistent **240+ jours** sans correction [2]
- RGPD : jusqu'à **4% du CA mondial** ou **€20M** d'amende pour violation de données [3]

<small>Sources : [1] [OWASP LLM Top 10](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) · [2] [Shen et al. ACM CCS 2024](https://arxiv.org/abs/2407.04295) · [3] [CyberHaven 2023](https://www.cyberhaven.com/)</small>

---

<!-- _class: cols -->

# 16 — Spotlight : Prompt Injection — vulnérabilité #1

<div class="left">

- **#1 OWASP** LLM Top 10 (2023 et 2025) [1]
- Directe (user) et indirecte (données) [1]
- **Aucune solution complète** n'existe encore
- Claude Opus 4.5 : **4,7%** ASR (meilleur) [2]

</div>
<div class="right">

- Défense en profondeur obligatoire [1]
- Sandwich defense, delimiters, hierarchy
- Constitutional Classifiers : 86% → **4,4%** [2]
- EU AI Act art. 15 : tests adversariaux requis dès **août 2026** [3]
- Coût défensif : **+10-30%** par requête

</div>

<small>Sources : [1] [OWASP](https://genai.owasp.org/) · [2] [Anthropic](https://www.anthropic.com/) · [3] [EU AI Act](https://eur-lex.europa.eu/)</small>

---

# 17 — Défenses & Red Teaming

| Défense | Technique | Performance |
|---------|-----------|------------|
| **Instruction Hierarchy** | Priorités system > user > tools | +**63%** robustesse [1] |
| **Constitutional Classifiers** | Filtrage constitutionnel (Anthropic) | 86% → **4,4%** jailbreak [2] |
| **Red Teaming automatisé** | Promptfoo, Garak, DeepTeam | **3,9x** plus de vulnérabilités détectées vs humain [3] |
| **Guardrails** | NeMo, Llama Guard, Guardrails AI | **95%** de blocage, 0,38% faux positifs [2] |

- Le red teaming automatisé atteint **69,5%** de succès d'attaque vs 47,6% en manuel [3]
- Garak (NVIDIA) : **3 000+** templates d'attaque, 150+ probes [3]
- CC++ (Anthropic, jan 2026) : même robustesse à seulement **~1%** de surcoût compute [2]

<small>Sources : [1] [Wallace et al. ICLR 2025](https://arxiv.org/abs/2404.13208) · [2] [Anthropic Constitutional Classifiers](https://www.anthropic.com/) · [3] [Promptfoo / NVIDIA Garak](https://www.promptfoo.dev/)</small>

---

# 18 — Évaluer la qualité : LLM-as-a-Judge & Testing

| Approche | Outil | Avantage | Limite |
|----------|-------|----------|--------|
| **LLM-as-a-Judge** | Claude Opus, GPT-4o | **95%** moins cher, corrélation 0,86 [1] | Biais de position, manipulable |
| **Promptfoo** | CLI open-source | 200K+ devs, 80+ F500, MIT [2] | Config YAML requise |
| **DeepEval** | Python framework | 500K+ downloads/mois [3] | Écosystème Python only |

- **10,9%** des prédictions régressent à chaque mise à jour du modèle [2]
- **87,9%** des updates qui améliorent le score global causent au moins une régression [2]
- Promptfoo : **$23,6M** levés (a16z + Insight Partners, juillet 2025) [2]
- CI/CD pour prompts : tester **avant** chaque déploiement, comme du code

<small>Sources : [1] [Zheng et al. NeurIPS 2023](https://arxiv.org/abs/2306.05685) · [2] [Promptfoo](https://www.promptfoo.dev/) · [3] [DeepEval](https://github.com/confident-ai/deepeval)</small>

---

# 19 — Discussion : Sécurité IA — quel budget ?

> Lundi 9h : un tweet viral montre que votre chatbot client a été **jailbreaké** — il donne des conseils médicaux dangereux. Le tweet a 50K vues et les médias tech appellent. L'EU AI Act entre en enforcement **août 2026**.

**Questions pour la classe** :
- Quelles sont vos **3 premières actions** dans les 2 heures ?
- Quel budget sécurité IA pour une startup de 20 personnes ? (Promptfoo gratuit, red teaming ~$5-50/run, guardrails +10-30% par requête)
- Faut-il un **AI Red Team** interne ou externaliser ?
- Comment l'EU AI Act art. 15 change-t-il vos obligations dès août 2026 ?

---

<!-- _class: section -->

# Tendances & synthèse

## Thinking models, code, décisions

---

# 20 — Thinking Models & Extended Reasoning

| Modèle | Benchmark clé | vs Modèle standard | Coût |
|--------|--------------|--------------------| -----|
| **o3** (OpenAI) | GPQA Diamond **87,7%** | vs ~50% GPT-4o [1] | $2/$8 par M tokens |
| **Claude Extended Thinking** | AIME **90%**, GPQA Physics **96,5%** | Sonnet 4.5 @ $3/$15 [2] | Budget tokens configurable |
| **DeepSeek-R1** | MATH-500 **97,3%**, Codeforces **2029 Elo** | Open-source [3] | ~$0,55/$2,19 par M tokens |

- Gain moyen : **+40 points** d'accuracy sur les tâches de raisonnement [1]
- Mais coût **5-30x** supérieur : 500 tokens visibles peuvent consommer 2 000-5 000 tokens internes [1]
- Moins besoin de Prompt Engineering, plus besoin de **cost management** [2]

<small>Sources : [1] [OpenAI](https://openai.com/) · [2] [Anthropic](https://www.anthropic.com/) · [3] [DeepSeek](https://www.deepseek.com/)</small>

---

# 21 — Prompting for Code Generation

- **Vibe coding** (Karpathy, fév 2025) : Collins **Word of the Year** 2025 [1]
- GitHub Copilot : développeurs **55% plus rapides** [2]
- Y Combinator W25 : **25%** des startups ont un codebase **95% généré par IA** [3]
- SWE-bench : Claude **77,2%**, GPT-5 **74,9%** — les agents codent mieux que jamais [2]

Mais attention :
- **45%** du code généré contient des vulnérabilités OWASP Top 10 [4]
- Java : **70%** de taux d'échec sécurité, Python/JS : 38-45% [4]
- Best practice : fichiers `CLAUDE.md` / `.cursorrules` pour guider l'agent [1]

> Le code IA est un **accélérateur**, pas un substitut au code review et aux tests de sécurité.

<small>Sources : [1] [Karpathy](https://x.com/karpathy/) · [2] [GitHub](https://github.com/) · [3] [Y Combinator](https://www.ycombinator.com/) · [4] [Veracode 2025](https://www.veracode.com/)</small>

---

# 22 — Matrice de décision : quelle technique pour quel besoin

| Besoin | Technique recommandée | Coût relatif |
|--------|----------------------|-------------|
| Tâche simple (extraction, classification) | Zero-shot + Structured Output | Minimal |
| Raisonnement multi-étapes | CoT ou Thinking Model (o3, Claude) | 2-30x |
| Production à volume | Chaining + Caching + Routing | Optimisé |
| Haute précision critique | Ensemble (N=5) + LLM-as-Judge | 5-8x |
| Sécurité requise | Guardrails + Red Teaming + Hierarchy | +10-30% |
| Optimisation continue | DSPy + Promptfoo (CI/CD) | $3-50/run |

> La bonne question n'est pas "quel est le meilleur prompt ?" mais "quel est le bon **système** pour mon cas d'usage ?"

---

# 23 — Key Takeaways

1. **Le Context Engineering remplace le Prompt Engineering** — la qualité dépend à 80% du contexte (données, outils, mémoire), pas de la formulation du prompt

2. **Les coûts sont le vrai champ de bataille** — Caching (90% d'économies), Routing (85%), Compression (2-20x) : maîtriser les Token Economics est un avantage concurrentiel

3. **La sécurité n'est pas optionnelle** — Prompt Injection est la vulnérabilité #1, l'EU AI Act impose des tests adversariaux dès août 2026, et 45% du code IA est vulnérable

4. **L'automatisation arrive** — DSPy, TextGrad, OPRO optimisent les prompts mieux que les humains. Le métier évolue de "prompt crafter" à "AI system architect"

5. **Les Thinking Models changent les règles** — o3, Claude Extended Thinking et DeepSeek-R1 gagnent +40 pts de précision. Moins de prompt craft, plus de cost management

> Le Prompt Engineering de 2026, c'est de l'**architecture de systèmes IA**, pas de la rédaction de requêtes.
