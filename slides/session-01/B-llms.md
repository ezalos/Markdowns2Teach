---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · Données publiques"
---

<!-- ABOUTME: Comprendre les LLMs — impact, mécanique, glossaire (Tokens, Context Window, MoE), pipeline d'entraînement, accès et taille des modèles. -->
<!-- ABOUTME: Seconde moitié de la Session 1, business-framed pour étudiants M2 IMT&E Paris 1 Panthéon-Sorbonne. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Les LLMs

## Session 1B — Comprendre et utiliser les modèles de langage

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Impact et capacités des LLMs

## Why LLMs Matter

---

# 01 — La preuve par les données

![bg right:45% contain vertical](assets/A/epoch-ai-dataset_size.png)
![bg contain](assets/A/METR-task-len-horizon.png)

- La taille des datasets d'entraînement croît de manière exponentielle [1]
- Les tâches que l'IA peut accomplir de manière autonome s'allongent rapidement [2]

> Ces deux courbes expliquent pourquoi chaque trimestre apporte des capacités IA que personne n'anticipait un an plus tôt.

<small>Sources : [1] [EpochAI](https://epoch.ai/data-insights/dataset-size-trend) · [2] [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)</small>

---

# 02 — Ce que les LLMs permettent

| Catégorie | Exemples | Type d'app |
|---|---|---|
| *Writing* | Brainstorming noms de produits, communiqués de presse, traduction | Web + App |
| *Reading* | Classification d'emails, résumé de conversations, analyse de sentiment | Surtout App |
| *Chatting* | Service client bot, coaching, FAQ interne | Web + App |
| *Coding* | Copilot, Cursor, Claude Code — 76% des développeurs utilisent des outils IA [1] | Web + App |

*Deux modes d'utilisation* :
- *Web-based* : ChatGPT, Claude, Le Chat — interaction directe
- *Software application* : le LLM est intégré dans un produit (email routing, analyse automatisée)

![bg right:40% contain](assets/ng01/img-026.png)

<small>Sources : [1] [Stack Overflow 2024](https://survey.stackoverflow.co/2024/ai)</small>

---

<!-- _class: section -->

# Comment fonctionne un LLM

## Next-Token Prediction

---

# 03 — Le mécanisme fondamental

Les LLMs utilisent le Self-Supervised Learning pour *prédire le mot suivant*, mot par mot :

| Input (A) | Output (B) |
|---|---|
| My favorite food is a | *bagel* |
| My favorite food is a bagel | *with* |
| My favorite food is a bagel with | *cream* |
| My favorite food is a bagel with cream | *cheese* |

> Un LLM entraîné sur des centaines de milliards de mots apprend les patterns du langage et devient capable de générer du texte cohérent et pertinent.

![bg right:45% contain](assets/A/lllm-gen-example.png)

---

<!-- _class: section -->

# Glossaire technique

## Tokens, Context Window, MoE

---

# 04 — Tokens : le vocabulaire des LLMs

Les LLMs ne raisonnent pas en mots mais en **Tokens** — des fragments de mots.

**Règle approximative** : 1 Token ≈ 3/4 d'un mot (en anglais)
- "the" → 1 token
- "programming" → 2 tokens
- "tonkotsu" → 4 tokens

| Modèle | Taille du vocabulaire | Particularité |
|---|---|---|
| Llama 2 | 32 000 tokens | Optimisé anglais |
| Llama 3 | 128 256 tokens | +4x, meilleur multilingue |
| Qwen 3 | 151 669 tokens [1] | Optimisé CJK + multilingue |

> En français, le ratio est moins favorable (~1 token ≈ 0,6 mot). Un vocabulaire plus large = moins de tokens par mot = *moins cher*.

<small>Sources : [1] [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)</small>

---

# 05 — Context Window : la mémoire de conversation

La **Context Window** est la mémoire de travail du LLM — tout ce qu'il peut "voir" pour générer sa réponse.

**Comment ça fonctionne** :
- Input + Output partagent la même fenêtre (ex : 200K tokens pour Claude)
- À chaque tour de conversation, le contexte *s'accumule*
- Le contexte croît linéairement — rien n'est supprimé silencieusement

**Les Thinking Tokens** (Reasoning Models) :
- Comptent dans le contexte *pendant* le tour où ils sont générés
- Sont *automatiquement retirés* du contexte pour les tours suivants [1]

> La Context Window limite la longueur des conversations et la taille des documents analysables. Les APIs facturent **par Token** (input + output).

<small>Sources : [1] [Anthropic](https://docs.anthropic.com/en/docs/build-with-claude/context-windows)</small>

---

<!-- _class: cols -->

# 06 — Mixture of Experts (MoE) : l'architecture qui change tout

<div class="left">

Un modèle MoE contient *plusieurs sous-réseaux spécialisés* (experts). Un **Router** sélectionne les experts pertinents pour chaque token.

- Le modèle a la *capacité* de tous les experts (total params)
- Mais n'*active* qu'une fraction par token (active params)
- *Résultat* : performance d'un gros modèle, vitesse d'un petit

> Analogie : un hôpital avec 8 spécialistes. Le triage (router) envoie chaque patient aux 2 spécialistes pertinents.

</div>
<div class="right">

| Modèle | Total | Actifs/token |
|--------|-------|-------------|
| Mixtral 8x7B 🇫🇷 | 46,7B | 12,9B |
| DeepSeek-V3 🇨🇳 | 671B | 37B |
| Qwen3 235B 🇨🇳 | 235B | 22B |
| Llama 4 Maverick 🇺🇸 | 400B | 17B |

<small>Sources : [1] [Mixtral](https://arxiv.org/abs/2401.04088) · [2] [DeepSeek-V3](https://arxiv.org/abs/2412.19437) · [3] [Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/)</small>

</div>

---

<!-- _class: section -->

# Le pipeline d'entraînement

## Pre-train → Instruct → Thinking → Fine-tune

---

# 07 — Vue d'ensemble du pipeline

| Étape | Ce qu'il apprend | Données | Résultat |
|-------|-----------------|---------|----------|
| **Pretraining** | Le langage, les faits, le raisonnement | Trillions de tokens (internet) | Base Model |
| **SFT** (Instruct) | Suivre des instructions, converser | Milliers de paires (instruction, réponse) | Instruct Model |
| **RLHF / DPO** | Être utile, honnête, inoffensif | Préférences humaines (A vs B) | Chatbot aligné |
| **Reasoning Training** | Réfléchir avant de répondre | Chain-of-Thought, preuves | Thinking Model |

> Chaque étape **ajoute une couche de capacité** sur la précédente. Le Fine-tuning que vous ferez en tant qu'entrepreneur s'appuie sur un modèle qui a déjà traversé ces étapes.

![bg right:40% contain](assets/infographics/training-pipeline_run_20260217_012323_723979.png)

---

# 08 — Les trois générations de LLMs

| Génération | Entraînement | Cas d'usage | Exemples |
|---|---|---|---|
| **Base Model** | Pretraining seul | Complétion de texte, Embeddings | GPT-3, BERT |
| **Instruct Model** | + SFT + RLHF | Chatbot, assistant | ChatGPT, Claude, Mistral |
| **Thinking Model** | + Reasoning Training | Maths, code, raisonnement | o3, DeepSeek-R1 |

> Comprendre ces 3 générations aide à choisir le bon modèle : un Base Model pour l'Embedding, un Instruct pour le chatbot, un Thinking pour l'analyse complexe.

---

# 09 — Thinking Models : penser avant de répondre

*Ce que font les Reasoning Models différemment* :

- *Extended Thinking* — le modèle génère une chaîne de raisonnement *avant* de répondre
- *Token budget* — plus on alloue de "Thinking Tokens", meilleure est la réponse (mais plus cher)
- *Vérification interne* — le modèle vérifie ses propres étapes, réduisant les hallucinations

| Modèle | AIME 2024 (maths) | Prix input / 1M tokens |
|--------|-----------|-----------------|
| GPT-4o | ~26% | $2,50 [1] |
| DeepSeek-R1 | 79,8% | $0,55 [2] |
| o3 | 91,6% | $2,00 [1] |
| o4-mini | 93,4% | $1,10 [1] |

![bg right:40% contain](assets/B/thinking-models-substack.png)

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [DeepSeek](https://arxiv.org/abs/2501.12948)</small>

---

<!-- _class: cols -->

# 10 — Fine-tuning : adapter un modèle à vos besoins

<div class="left">

Le **Fine-tuning** consiste à ré-entraîner un modèle existant sur vos propres données :

| | Pretraining | Fine-tuning |
|---|---|---|
| **Données** | Milliards de mots | Milliers d'exemples |
| **Objectif** | Apprendre le langage | Adapter à une tâche |
| **Coût** | Millions $ | Centaines $ |

**Quand fine-tuner ?**
- Le modèle a besoin d'un **style** spécifique
- Le jargon est trop technique (médical, juridique)
- Le RAG ne capture pas le **format** attendu

</div>
<div class="right">

**LoRA** — entraîner 0,1-1% des paramètres pour 90-95% de la qualité [1]

| Config | vRAM | Coût |
|---|---|---|
| 7B LoRA | ~16-24 GB | $5-15 |
| 7B QLoRA | ~8-10 GB | **$0-5** |

**Distillation** — un grand modèle entraîne un petit :
- DeepSeek-R1 distillé sur Qwen-7B : **55,5%** sur AIME 2024 [2]
- Coût divisé par 10-100x en production

<small>Sources : [1] [Hu et al. ICLR 2022](https://arxiv.org/abs/2106.09685) · [2] [DeepSeek](https://arxiv.org/abs/2501.12948)</small>

</div>

---

<!-- _class: section -->

# Accéder aux LLMs

## Web, API, Open-Weights

---

# 11 — Interface web : le plus simple

Les chatbots grand public — aucune compétence technique requise :

| Service | Fournisseur | Modèle(s) | Prix |
|---------|------------|-----------|------|
| **ChatGPT** | OpenAI | GPT-4o, o3 | Gratuit / $20/mois |
| **Claude** | Anthropic | Claude Sonnet 4.5, Opus 4.6 | Gratuit / $20/mois |
| **Gemini** | Google | Gemini 2.5 | Gratuit / $20/mois |
| **Le Chat** | Mistral AI 🇫🇷 | Mistral Large 3 | Gratuit / $15/mois |
| **Perplexity** | Perplexity AI | Multi-modèle + recherche web | Gratuit / $20/mois |

> *Pour les entrepreneurs* : commencez ici. Testez vos cas d'usage en 5 minutes, sans code, sans API.

---

# 12 — Accès API : intégrer un LLM dans votre produit

Les APIs permettent d'appeler un LLM *depuis votre code* — la base de tout produit IA :

| Fournisseur | Modèle phare | Input / 1M tokens | Output / 1M tokens |
|---|---|---|---|
| **OpenAI** | GPT-4o | $2,50 | $10,00 [1] |
| **Anthropic** | Claude Sonnet 4.5 | $3,00 | $15,00 [2] |
| **Mistral AI** 🇫🇷 | Mistral Large 3 | $2,00 | $6,00 [3] |
| **Google** | Gemini 2.5 Pro | $1,25 | $10,00 |
| **OpenRouter** | Multi-modèle | Variable | Variable |

> Les prix chutent d'environ **~10x par an** à performance équivalente [4]. Le coût marginal de l'intelligence baisse drastiquement.

<small>Sources : [1] [OpenAI](https://openai.com/api/pricing/) · [2] [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models) · [3] [Mistral AI](https://mistral.ai/pricing) · [4] [a16z](https://a16z.com/llmflation-llm-inference-cost/)</small>

---

<!-- _class: cols -->

# 13 — Open-Weights : télécharger et exécuter en local

<div class="left">

**HuggingFace** — la plateforme de référence :
- **+1 million** de modèles disponibles [1]
- Téléchargement gratuit (la plupart)
- Formats : SafeTensors, GGUF (quantifié)

**Ollama** — exécuter un LLM en une commande :
```
ollama run llama3.1:8b
```

**Avantages du local** :
- Données restent sur votre machine (RGPD)
- Pas de coût API récurrent
- Fonctionne hors ligne

</div>
<div class="right">

### Modèles open-weights à connaître

| Modèle | Taille | Force clé |
|--------|--------|-----------|
| Llama 3.1 🇺🇸 | 8-405B | Écosystème Meta |
| Mistral Large 3 🇫🇷 | 123B | Souveraineté EU |
| Qwen 3 🇨🇳 | 0,6-235B | 119 langues |
| DeepSeek-R1 🇨🇳 | 671B MoE | Reasoning SOTA |
| Gemma 3 | 1-27B | On-device Google |

<small>Sources : [1] [HuggingFace](https://huggingface.co/models)</small>

</div>

---

# 14 — Licences : ce que vous pouvez (et ne pouvez pas) faire

| Licence | Modèles | Usage commercial | Restrictions |
|---------|---------|-----------------|-------------|
| **Apache 2.0** | Mistral, DBRX | ✅ Libre | Aucune |
| **MIT** | Qwen 3 | ✅ Libre | Aucune |
| **Llama License** | Llama 3-4 | ✅ Sous conditions | >700M utilisateurs → licence spéciale |
| **DeepSeek License** | DeepSeek-R1, V3 | ✅ Sous conditions | Pas de modèles concurrents |
| **Propriétaire** | GPT-4, Claude | ❌ API uniquement | Pas de téléchargement |

> *Pour les entrepreneurs* : Apache 2.0 et MIT offrent la liberté maximale. Vérifiez toujours la licence *avant* de construire votre produit dessus.

---

<!-- _class: section -->

# Taille des modèles

## Parameters, vRAM, Hardware

---

<!-- _class: cols -->

# 15 — Paramètres → vRAM → Hardware

<div class="left">

Chaque paramètre occupe de la mémoire :

| Précision | Octets/param | 7B modèle |
|-----------|-------------|-----------|
| FP16 | 2 | 14 GB |
| INT8 | 1 | 7 GB |
| **INT4** | 0,5 | **3,5 GB** |

**La formule** :
`vRAM (GB) = Params (B) × Octets/param`

> La **Quantization** (réduire la précision) permet de faire tourner des modèles beaucoup plus gros sur du matériel limité — avec une perte de qualité minime.

</div>
<div class="right">

### Quel hardware pour quel modèle ?

| Hardware | vRAM | Modèle max (Q4) |
|----------|------|-----------------|
| MacBook M4 Pro | 24-48 GB | 14B-32B |
| RTX 4090 | 24 GB | 32B |
| RTX 5090 | 32 GB | 70B |
| MacBook M4 Max | 128 GB | 70B |
| H100 (cloud) | 80 GB | 70B FP16 |

<small>Sources : [1] [IntuitionLabs](https://intuitionlabs.ai/articles/local-llm-deployment-24gb-gpu-optimization)</small>

</div>

---

# 16 — Le paradoxe MoE : rapide mais gourmand en mémoire

Le MoE découple la *vitesse* de la *mémoire* :

| Dimension | Dense 70B (Llama 2) | MoE 671B (DeepSeek-V3) |
|-----------|---------------------|------------------------|
| Total params | 70B | 671B |
| Actifs par token | **70B** (tous) | **37B** (5,5%) |
| vRAM nécessaire (FP16) | ~140 GB | ~1 342 GB |
| vRAM nécessaire (INT4) | ~35 GB | ~336 GB |
| Vitesse d'inference | Baseline | **~2x plus rapide** (à compute égal) |

> *Le piège* : même si DeepSeek-V3 n'active que 37B params par token, il faut charger **les 671B** en mémoire. L'inference est rapide, mais le matériel est cher.

*Coût d'entraînement* : DeepSeek-V3 a été entraîné pour ~$5,5M — environ 18x moins cher que GPT-4 (~$100M+) [1].

<small>Sources : [1] [DeepSeek-V3](https://arxiv.org/abs/2412.19437) · [2] [Interconnects](https://www.interconnects.ai/p/deepseek-v3-and-the-actual-cost-of)</small>

---

# 17 — Plus gros = plus intelligent ?

Les benchmarks montrent des *rendements décroissants* :

| Modèle | Params | MMLU | MATH |
|--------|--------|------|------|
| Llama 3.1 8B | 8B | 69,4% | — |
| Llama 3.1 70B | 70B | 84,0% | — |
| Llama 3.1 405B | 405B | 87,7% | 73,8% |

- De 8B à 70B (×8,75 params) : **+14,6 points** MMLU
- De 70B à 405B (×5,8 params) : **+3,7 points** seulement

> **50x plus de paramètres** pour **+18 points** de MMLU. La courbe de performance *s'aplatit*. C'est la loi des rendements décroissants.

<small>Sources : [1] [Meta Llama 3.1](https://arxiv.org/abs/2407.21783)</small>

---

<!-- _class: cols -->

# 18 — Le bon modèle pour la bonne tâche

<div class="left">

### Coût API (par 1M tokens output)

| Modèle | Taille | Prix |
|--------|--------|------|
| Llama 3.1 8B | 8B | $0,06 |
| GPT-4o mini | ~Small | $0,60 |
| Mistral Large 3 | 123B | $6,00 |
| GPT-4o | ~Large | $10,00 |
| Claude Opus 4.6 | ~XL | $75,00 |

**Écart** : 1 250x entre le moins cher et le plus cher.

</div>
<div class="right">

### Recommandation par use case

| Use case | Modèle | Pourquoi |
|----------|--------|----------|
| Support client | Mistral Small 3 (24B) | Rapide, multilingue, Apache 2.0 |
| Analyse complexe | o3 / Claude Opus | Reasoning avancé |
| App mobile offline | Gemma 3 / Phi-4 | On-device, pas de cloud |
| Génération de code | Claude Opus / Devstral | SWE-bench SOTA |

</div>

> *Règle d'or* : ne pas utiliser GPT-4 pour classifier du sentiment quand GPT-4o-mini fait le travail — c'est **16x moins cher**.

---

# 19 — David bat Goliath : les petits modèles qui surprennent

| Modèle | Params | Performance | Comparé à |
|--------|--------|-------------|-----------|
| **Mistral Small 3** 🇫🇷 | 24B | MMLU 81%, **3x plus rapide** | Llama 3.3 70B (×3 plus gros) [1] |
| **Phi-4 Reasoning** | 14B | AIME 2024 : **75,3%** | o1-mini 63,6% (bien plus gros) [2] |
| **DeepSeek-R1 distillé** | 7B | AIME 2024 : **55,5%** | QwQ-32B-Preview 50,0% (×4,5 plus gros) [3] |
| **DeepSeek-R1 distillé** | 14B | AIME 2024 : **69,7%** | o1-mini 63,6% [3] |

> En 2025, la *méthodologie d'entraînement* et la *qualité des données* comptent plus que la taille brute du modèle. Un 14B bien entraîné bat un 671B sur des tâches spécifiques.

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-small-3) · [2] [Microsoft Research](https://www.microsoft.com/en-us/research/articles/phi-reasoning-once-again-redefining-what-is-possible-with-small-and-efficient-ai/) · [3] [DeepSeek](https://arxiv.org/abs/2501.12948)</small>

---

<!-- _class: section -->

# Récapitulatif

## Key Takeaways

---

# 20 — Points clés à retenir

### Les LLMs en pratique
- Les LLMs prédisent le *mot suivant* — entraînés sur des trillions de tokens
- Quatre familles d'applications : *Writing, Reading, Chatting, Coding*

### Le vocabulaire technique
- **Token** : unité de base des LLMs (~¾ d'un mot anglais)
- **Context Window** : mémoire de travail, partagée entre input et output
- **MoE** : architecture à experts qui découple capacité et coût d'inference

### Le pipeline d'entraînement
- Pretraining → Instruct (SFT+RLHF) → Thinking → Fine-tuning
- Trois générations : Base Model, Instruct Model, Thinking Model

### Taille et accès
- Plus gros ≠ toujours meilleur — rendements décroissants
- Le bon modèle pour la bonne tâche > le plus gros modèle pour tout
- Accès : web (gratuit), API (pay-per-token), open-weights (local)

> *Prochaine session* : passer de l'utilisation à la *construction* de projets IA.
