---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Reasoning Models & SLMs 2024–2025 · Données publiques"
---

<!-- ABOUTME: Panorama des Reasoning Models et Small Language Models (SLMs) de 2024-2025 avec benchmarks, pricing et cas d'usage. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : comment choisir le bon modèle selon son budget, ses contraintes et son use case. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Reasoning Models & Small Language Models

## De la pensée machine aux modèles de poche

M2 Entrepreneuriat · Sorbonne · 2026

---

# 01 — Pourquoi ces modèles changent la donne

Trois disruptions simultanées transforment le paysage IA :

1. **Des modèles qui "réfléchissent"** — les Reasoning Models décomposent un problème en étapes avant de répondre, atteignant **96,7%** sur des olympiades de mathématiques [1]
2. **Un effondrement des coûts** — le coût d'inference a été divisé par **280** en 2 ans [2]
3. **L'IA dans la poche** — les SLMs tournent sur un smartphone ou un laptop, sans cloud, sans latence

> En tant qu'entrepreneur, comprendre ce paysage = savoir **quel modèle utiliser, quand, et à quel prix**.

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

# 02 — Panorama 2024–2025 : 33 modèles, 4 familles

| Famille | Nb | Exemple phare | Prix / 1M tokens | Capacité clé |
|---------|----|---------------|-------------------|--------------|
| Reasoning Models | 12 | o3, DeepSeek-R1 | $0,55 – $10 | Résolution multi-étapes |
| Frontier General | 8 | GPT-4.1, Claude Sonnet 4.5 | $1,25 – $15 | Polyvalence maximale |
| Small Language Models | 10 | Phi-4, Mistral Small 3 | $0,04 – $1 | On-device, low-cost |
| Spécialisés / Coding | 3 | Codex CLI, Devstral 2 | $0,30 – $14 | Génération de code |

> **Tendance clé** : les modèles open-weight (Llama 4, Mistral, DeepSeek) rattrapent les modèles fermés sur la majorité des benchmarks.

<small>Sources : [1] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: section -->

# Reasoning Models

## Quand l'IA apprend à réfléchir

---

# 03 — Le Chain-of-Thought : penser avant de répondre

**Ce que font les Reasoning Models différemment** :

- **Extended Thinking** — le modèle génère une chaîne de raisonnement *avant* de répondre
- **Token budget** — plus on alloue de "thinking tokens", meilleure est la réponse (mais plus cher)
- **Vérification interne** — le modèle vérifie ses propres étapes, réduisant les hallucinations

**L'évolution OpenAI** : o1 (sept. 2024) → o3 (avril 2025) → o4-mini (avril 2025)

| Modèle | AIME 2024 | GPQA Diamond | Prix input / 1M |
|--------|-----------|--------------|-----------------|
| GPT-4o | ~26% | ~53% | $2,50 |
| o1 | 74,3% | 78,0% | $15,00 |
| o3 | 91,6% | 87,7% | $2,00 |
| o4-mini | 93,4% | 81,4% | $1,10 |

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning)</small>

---

# 04 — Les leaders du Reasoning

| Modèle | Créateur | AIME 2025 | GPQA | Prix input | Open-weight ? |
|--------|----------|-----------|------|------------|---------------|
| o3 | OpenAI | 88,9% | 87,7% | $2,00 | ❌ |
| o4-mini | OpenAI | 92,7% | 81,4% | $1,10 | ❌ |
| DeepSeek-R1 | DeepSeek | 87,5% | 81,0% | $0,55 | ✅ MIT |
| Gemini 2.5 Pro | Google | 86,7% | 84,0% | $1,25 | ❌ |
| QwQ-32B | Alibaba | ~70% | ~65% | $0,08 | ✅ Apache 2.0 |
| Grok 4 | xAI | 93–95% | 88,0% | $3,00 | ❌ |
| Claude Opus 4.6 | Anthropic | — | 91,3% | $5,00 | ❌ |

> **Fait marquant** : DeepSeek-R1 open-weight rivalise avec o3 fermé, pour **4x moins cher**.

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [DeepSeek](https://github.com/deepseek-ai/DeepSeek-R1) · [3] [Google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) · [4] [Anthropic](https://www.anthropic.com/news/claude-model-october-2025)</small>

---

<!-- _class: cols -->

# 05 — Spotlight : DeepSeek-R1

<div class="left">

- 671B MoE (**37B actifs**), licence **MIT** [1]
- Entraîné par **pure RL** (sans SFT)
- AIME 2024 : **79,8%** (R1-0528 : 91,4%)
- Coût entraînement : ~**$5,6M** [1]
- API : **$0,55** / 1M tokens input

</div>
<div class="right">

- **Choc géopolitique** : open-weight chinois rivalisant les fermés US
- Distillé **1,5B → 70B** pour tous les budgets
- Self-hosted **€0** (hors infra) — souveraineté [2]
- Bloqué en Italie, Allemagne — vérifier RGPD

</div>

<small>Sources : [1] [DeepSeek](https://github.com/deepseek-ai/DeepSeek-R1) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: cols -->

# 06 — Spotlight : OpenAI o3 & o4-mini

<div class="left">

**o3 — SOTA Reasoning** :

- AIME 2025 : **88,9%**, GPQA : **87,7%** [1]
- SWE-bench : **71,7%**, context 200K, vision
- Prix : **$2 / 1M** input (−80% depuis le lancement)

</div>
<div class="right">

**o4-mini — meilleur ratio coût/perf** :

- AIME 2024 : **93,4%** (sans outils) [1]
- AIME 2025 : **99,5%** avec Python tools
- Prix : **$1,10 / 1M** — 85-95% de o3 pour 2x moins
- **Idéal startups** : structured output supporté

</div>

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/)</small>

---

# 07 — Le coût du Reasoning : tokens visibles vs cachés

Les thinking tokens invisibles multiplient le coût **3-10x** :

| Tâche | GPT-4o | o3 | Facteur |
|-------|--------|----|---------|
| Requête simple | $0,01 | $0,15 | ×15 |
| Analyse complexe | $0,05 | $2,00 | ×40 |
| Session de code | $0,10 | $5,00 | ×50 |

**Routing hybride** : 80% standard (GPT-4o) + 20% Reasoning (o3) = **facture ÷5-10** [1]

> Router automatiquement les requêtes complexes vers o3, le reste vers GPT-4o.

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/)</small>

---

# 08 — Discussion : Quand activer le Reasoning ?

> **Scénario** : votre startup traite **10 000 factures/jour**. Vous devez en extraire les montants, dates et fournisseurs.

| Option | Modèle | Coût / jour | Précision | Remarque |
|--------|--------|-------------|-----------|----------|
| A | GPT-4o | ~$10 | 95% | Rapide, mais erreurs sur cas ambigus |
| B | o3 | ~$200 | 99,5% | Précis, mais 20x plus cher |
| C | Hybride | ~$30 | 99% | GPT-4o + o3 sur les 5% de cas limites |

**Questions pour la classe** :

- À partir de quel taux d'erreur le surcoût du Reasoning se justifie-t-il ?
- Comment identifier automatiquement les requêtes "complexes" ?
- Quel impact business d'une facture mal traitée ?

---

<!-- _class: section -->

# Modèles Frontier

## Les poids lourds du marché

---

# 09 — Frontier : la carte des géants

| Modèle | Créateur | Params | Context | SWE-bench | Prix input | Open ? |
|--------|----------|--------|---------|-----------|------------|--------|
| GPT-5.2 | OpenAI | — | 400K | 80,0% | $1,75 | ❌ |
| Claude Sonnet 4.5 | Anthropic | — | 200K | 77,2% | $3,00 | ❌ |
| Gemini 2.5 Pro | Google | MoE | 1M | 63,8% | $1,25 | ❌ |
| Llama 4 Maverick | Meta | 400B | 1M | 18,4% | $0,20 | ✅* |
| Mistral Large 3 | 🇫🇷 Mistral | 675B | 256K | — | $0,50 | ✅ Apache |
| DeepSeek-V3.2 | DeepSeek | 685B | — | 73,1% | $0,28 | ✅ MIT |

> \* Llama 4 : **entités UE exclues** des droits multimodaux (licence communautaire).

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Anthropic](https://www.anthropic.com/news/claude-model-october-2025) · [3] [Meta](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) · [4] [Mistral AI](https://mistral.ai/news/mistral-large-3/)</small>

---

# 10 — Open-weight vs Closed : le match 2025

L'écart de performance se **referme rapidement** :

- Llama 4 Maverick (400B open) **rivalise** avec GPT-4.1 en coding [1]
- DeepSeek-V3.2 (MIT) atteint **93,1%** sur AIME 2025 [2]
- Mistral Large 3 (Apache 2.0) = modèle frontier **le moins cher** ($0,50/1M) [3]

**Le paradoxe économique** :

| Métrique | Open-weight | Closed |
|----------|-------------|--------|
| Part du trafic tokens | 43% | 42% |
| Part du revenu | ~4% | **96%** |
| Écart de coût | 10-100x moins cher | Premium |

> **Le vrai match** n'est plus la performance — c'est le **business model**. Open-weight = commodité, closed = moat + service.

<small>Sources : [1] [Meta](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) · [2] [DeepSeek](https://github.com/deepseek-ai/DeepSeek-R1) · [3] [Menlo Ventures](https://menlovc.com/perspective/2025-mid-year-llm-market-update/)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Mistral AI — le champion européen

<div class="left">

- Large 3 : **675B MoE** (41B actifs), Apache 2.0 [1]
- Small 3 : **24B** dense, 27 langues, Apache 2.0
- Prix : **$0,50 / 1M** — frontier le moins cher [1]
- Le Chat : **20+ intégrations** MCP entreprise

</div>
<div class="right">

- Investissement ASML : **€1,3 Mds** [2]
- **Hébergé 100% UE** — pas soumis au CLOUD Act US
- Contrat **armée française** (infra classifiée) [2]
- **18 000** puces NVIDIA Grace Blackwell en France [1]

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-large-3/) · [2] [CNBC](https://www.cnbc.com/) · [3] [TechCrunch](https://techcrunch.com/)</small>

---

# 12 — Discussion : Build vs Buy vs Fine-tune

> **Scénario** : vous développez un **assistant juridique** pour avocats français. Il doit comprendre le droit français, répondre en français, et les données ne doivent pas quitter l'UE.

| Option | Modèle | Coût / mois | Souveraineté | Conformité |
|--------|--------|-------------|--------------|------------|
| Buy API | GPT-4.1 (OpenAI) | ~€3 000 | ❌ Données US | CLOUD Act |
| Self-host | Mistral Large 3 | ~€500 (GPU) | ✅ EU-only | RGPD ✅ |
| Fine-tune | Llama 4 | ~€200 + €2K setup | ⚠️ Licence UE exclue | Risque légal |

**Questions pour la classe** :

- Le RGPD est-il un **avantage compétitif** pour les modèles européens ?
- Un cabinet d'avocats accepterait-il d'envoyer ses données chez OpenAI ?
- Comment valoriser la souveraineté dans un pitch investisseur ?

---

<!-- _class: section -->

# Small Language Models

## La puissance dans la poche

---

# 13 — Pourquoi les SLMs changent tout

5 avantages qui transforment l'IA pour les startups :

1. **10-30x moins cher** — Phi-4 à $0,07/1M vs GPT-4o à $2,50/1M [1]
2. **On-device / Edge** — pas de cloud, pas de latence réseau
3. **< 2s de latence** — réponse instantanée pour l'utilisateur
4. **Données locales = RGPD friendly** — aucune donnée ne quitte l'appareil [2]
5. **Fine-tuning abordable** — $100-500 vs $100K+ pour un modèle frontier

**Marché SLM** : **$5,5 Mds** projetés d'ici 2028 [3]

> Les SLMs ne remplacent pas les Frontier Models — ils les **complètent** pour les tâches simples et sensibles.

<small>Sources : [1] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [2] [Stanford HAI](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [3] [MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/small-language-model-market)</small>

---

# 14 — Les SLMs à connaître

| Modèle | Créateur | Params | Licence | Force clé | Prix / 1M |
|--------|----------|--------|---------|-----------|-----------|
| Phi-4 | Microsoft | 14B | MIT | Math rivale 70B [1] | $0,07 |
| Mistral Small 3 | 🇫🇷 Mistral | 24B | Apache 2.0 | 27 langues, 150 tok/s [2] | $0,10 |
| Gemma 3 | Google | 1-27B | Open | On-device, 140+ langues [3] | $0,04 |
| Llama 4 Scout | Meta | 109B (17B actifs) | Communautaire* | Context 10M tokens | $0,10 |
| Qwen 2.5 | Alibaba | 0,6-32B | Apache 2.0 | 119 langues, mobile [4] | $0,08 |
| SmolLM2 | 🇫🇷 HuggingFace | 1,7B | Apache 2.0 | Raspberry Pi, 100% open [5] | Gratuit |
| Granite 3.1 | IBM | 8B | Apache 2.0 | Enterprise, RAG | $0,10 |

> \* Llama 4 Scout : licence communautaire, **UE exclue** pour le multimodal.

<small>Sources : [1] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [2] [Mistral AI](https://mistral.ai/news/mistral-large-3/) · [3] [Google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) · [4] [Alibaba](https://qwenlm.github.io/blog/qwq-32b/) · [5] [HuggingFace](https://huggingface.co/blog/smollm2)</small>

---

<!-- _class: cols -->

# 15 — Spotlight : Phi-4 de Microsoft

<div class="left">

- **14B** params, licence **MIT**, données synthétiques [1]
- MATH : **80,4%** — rivalise avec des modèles 5x plus gros
- Phi-4-reasoning-plus égale **DeepSeek-R1** (671B) en maths
- GPQA Diamond : **56,1%** [1]

</div>
<div class="right">

- GPU consumer (**16 GB** VRAM), mini (3,8B) sur iPhone [1]
- Coût API : **$0,07 / 1M** input
- Intégration **Azure AI Foundry** + Copilot+ PCs (NPU)
- Idéal **prototypage rapide** et MVPs

</div>

<small>Sources : [1] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [2] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning)</small>

---

# 16 — On-device et Edge AI : cas d'usage concrets

| Use case | Modèle | Hardware | Latence | Coût cloud évité |
|----------|--------|----------|---------|------------------|
| Chatbot offline mobile | Gemma 3 (1B) | Smartphone | <1s | 100% [1] |
| Classification documents on-premise | Phi-4 (14B) | RTX 4090 | ~2s | 100% [2] |
| Maintenance prédictive IoT | SmolLM2 (1,7B) | Raspberry Pi | <1s | 100% [3] |
| Traduction temps réel | Qwen 2.5 (7B) | Laptop | ~1,5s | 100% [4] |

**Performances on-device** :

- Gemma 3 (1B) : **2 585 tok/s** sur mobile via Google AI Edge SDK [1]
- SmolLM2 : **~15 tok/s** sur smartphone flagship [3]
- Qwen 3 (0,6B) : **55-60 tok/s** sur Snapdragon 8 / Apple M-series [4]

<small>Sources : [1] [Google](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/) · [2] [Microsoft](https://azure.microsoft.com/en-us/blog/introducing-phi-4-microsoft-s-newest-small-language-model/) · [3] [HuggingFace](https://huggingface.co/blog/smollm2) · [4] [Alibaba](https://qwenlm.github.io/blog/qwq-32b/)</small>

---

# 17 — Discussion : SLM ou API pour votre MVP ?

> **Scénario** : startup HealthTech, **1 000 patients**, résumé automatique de notes médicales. Hébergement certifié HDS (Hébergeur de Données de Santé) requis par la loi française.

| Option | Modèle | Coût / mois | Données | Conformité HDS |
|--------|--------|-------------|---------|----------------|
| A | GPT-4 API | ~€3 000 | Quittent l'UE | ❌ Non conforme |
| B | Phi-4 self-hosted | ~€200 (setup €500) | Restent locales | ✅ Conforme |
| C | Mistral Small 3 | ~€150 | Restent en UE | ✅ Conforme |

**Questions pour la classe** :

- Un investisseur santé préfère-t-il un MVP rapide (API) ou conforme (self-hosted) ?
- La performance de Phi-4 (14B) est-elle suffisante pour du résumé médical ?
- Comment le RGPD peut-il devenir un **argument commercial** face à des concurrents US ?

---

<!-- _class: section -->

# Modèles Spécialisés

## Du code aux agents autonomes

---

# 18 — Les modèles qui codent

**SWE-bench Verified** — le benchmark de référence pour la génération de code :

| Modèle | SWE-bench | Créateur | Prix input / 1M |
|--------|-----------|----------|-----------------|
| Claude Opus 4.6 | **80,8%** | Anthropic | $5,00 |
| GPT-5.2 | 80,0% | OpenAI | $1,75 |
| Gemini 3 Flash | 78,0% | Google | $0,50 |
| Kimi K2.5 | 76,8% | Moonshot | $0,60 |
| DeepSeek-V3.2 | 73,1% | DeepSeek | $0,28 |
| Devstral 2 | 72,2% | 🇫🇷 Mistral | $0,40 |
| o3 | 71,7% | OpenAI | $2,00 |

**Coding agents** : Cursor, Windsurf, Claude Code, Codex CLI — coût d'une session : **$0,50-$5** vs heure développeur **$50-150** [1]

<small>Sources : [1] [SWE-bench](https://www.swebench.com/) · [2] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [3] [Anthropic](https://www.anthropic.com/news/claude-model-october-2025)</small>

---

# 19 — L'essor des agents autonomes

Du **chatbot** à l'**agent** — l'évolution en 3 étapes :

1. **Chatbot** (2023) — question/réponse, pas d'action
2. **Tool use** (2024) — le modèle appelle des APIs, cherche sur le web
3. **Agent autonome** (2025) — multi-step reasoning, exécution de code, auto-correction

**Exemples concrets** :

- **Codex CLI** (OpenAI) — sandbox cloud, résout des bugs en 37+ étapes [1]
- **Claude Code** (Anthropic) — terminal, 30h+ d'opération autonome [2]
- **Devin** (Cognition) — agent développeur full-stack

**Marché** : **25% des dépenses IA** en agents d'ici 2028 [3]

> Les agents ne remplacent pas les développeurs — ils les rendent **5-10x plus productifs**.

<small>Sources : [1] [OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/) · [2] [Anthropic](https://www.anthropic.com/news/claude-model-october-2025) · [3] [Gartner](https://www.gartner.com/)</small>

---

<!-- _class: section -->

# Synthèse

## Choisir le bon modèle

---

# 20 — Matrice de décision : quel modèle pour quel usage ?

| Use case | Modèle recommandé | Coût / mois | Pourquoi |
|----------|--------------------|-------------|----------|
| Support client | Mistral Small 3 (24B) | ~€150 | Rapide, multilingue, Apache 2.0 [1] |
| Analyse juridique | o3 + Mistral Large 3 | ~€500 | Reasoning pour cas complexes [1] |
| App mobile offline | Gemma 3 / Phi-4 mini | ~€0 | On-device, pas de cloud |
| Génération de code | Claude Opus 4.6 / Devstral 2 | ~€300 | SWE-bench SOTA [2] |
| Extraction de données | GPT-4o + o4-mini (hybride) | ~€200 | Routing coût/précision |
| IoT / Edge | SmolLM2 (1,7B) | ~€0 | Raspberry Pi, Apache 2.0 |

> **Règle d'or** : le bon modèle pour la bonne tâche > le plus gros modèle pour toutes les tâches.

<small>Sources : [1] [Artificial Analysis](https://artificialanalysis.ai/leaderboards/reasoning) · [2] [SWE-bench](https://www.swebench.com/)</small>

---

# 21 — L'Europe dans la course aux modèles

L'écosystème européen se structure autour de **trois piliers** :

1. **Mistral AI** 🇫🇷 — Large 3 + Small 3 sous Apache 2.0, hébergement 100% UE, contrat militaire français [1]
2. **HuggingFace** 🇫🇷 — SmolLM2 100% open-source, hub de référence mondial [2]
3. **Cadre réglementaire** — EU AI Act (2026), avantage conformité pour startups UE [3]

**L'écosystème français en chiffres** :

- **750+ startups IA** en France [4]
- Investissement ASML dans Mistral : **€1,3 Mds** [1]
- Mistral Compute : **18 000 puces** NVIDIA Grace Blackwell en France

> L'EU AI Act n'est pas qu'une contrainte — c'est un **moat réglementaire** pour les entreprises européennes.

<small>Sources : [1] [Mistral AI](https://mistral.ai/news/mistral-large-3/) · [2] [HuggingFace](https://huggingface.co/blog/smollm2) · [3] [EU Commission](https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence) · [4] [France Digitale](https://www.frenchtechjournal.com/france-digital-ai-mapping/)</small>

---

# 22 — Key Takeaways

1. **Reasoning = saut qualitatif** — o3 et DeepSeek-R1 résolvent des problèmes impossibles pour les modèles standard, mais coûtent 10-50x plus → **routing hybride** obligatoire

2. **SLMs démocratisent l'IA** — Phi-4 (14B) rivalise avec des modèles 5x plus gros pour $0,07/1M tokens → MVP accessible à toute startup

3. **Open-weight rattrape closed** — DeepSeek, Mistral, Llama ferment l'écart → la valeur migre du modèle vers l'**application**

4. **Edge AI = avantage RGPD** — données locales, pas de cloud, conformité native → argument commercial fort pour startups UE

5. **Le bon modèle pour la bonne tâche** — un SLM à $0,10/1M pour 80% des requêtes + un Reasoning Model pour les 20% complexes = **budget optimisé**

> **En résumé** : la question n'est plus "quel est le meilleur modèle ?" mais "**quel est le bon modèle pour mon use case, mon budget et mes contraintes ?**"
