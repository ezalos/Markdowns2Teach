---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — M2 Entrepreneuriat Sorbonne"
footer: "Recherche Fine-tuning 2024–2026 · Données publiques"
---

<!-- ABOUTME: Fine-tuning et personnalisation de modèles IA — méthodes, plateformes, données, économie. -->
<!-- ABOUTME: Cadré pour entrepreneurs M2 : décider quand, comment et où personnaliser un modèle. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Le Fine-tuning de Modèles IA

## Personnaliser l'IA pour son produit

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Pourquoi personnaliser un modèle ?

## Du prompt au modèle sur-mesure

---

# 01 — Quand (ne pas) fine-tuner

L'escalade de personnalisation suit un ordre de coût et complexité croissants :

| Étape | Coût | Délai | Quand l'utiliser |
|-------|------|-------|------------------|
| **Prompt Engineering** | $0 | Heures | 80% des cas — toujours commencer ici |
| **RAG** | $70–1 000/mois | Heures–jours | Données fraîches, sources vérifiables |
| **Fine-tuning (LoRA)** | $5–50/run | Jours | Style, format, tâche spécifique |
| **CPT** (Continued Pre-training) | $2K–25K+ | Semaines | Jargon de domaine (médical, juridique) |

> Règle d'or : **80% des besoins** se résolvent avec du Prompt Engineering + RAG. Ne fine-tuner que si le gain justifie le coût [1]

<small>Sources : [1] [Meta AI](https://ai.meta.com/blog/when-to-fine-tune-llms-vs-other-techniques/)</small>

---

<!-- _class: section -->

# Les méthodes de Fine-tuning

## LoRA, distillation, alignement

---

# 02 — Panorama des méthodes

| Méthode | Params entraînés | VRAM (7B) | Coût/run | Cas d'usage |
|---------|-----------------|-----------|----------|-------------|
| **FFT** (Full Fine-tuning) | 100% | ~120 GB | $50–300 | Max qualité, gros budget |
| **LoRA** | 0,1–1% | ~16–24 GB | $5–15 | Standard production |
| **QLoRA** | 0,1–1% (4-bit) | ~8–10 GB | $0–5 | Startups, Colab gratuit |
| **Prompt Tuning** | <0,01% | ~14 GB | $1–5 | Prototypage rapide |
| **CPT** | 100% (domaine) | ~120 GB+ | $2K–25K | Vocabulaire spécialisé |

> LoRA + QLoRA couvrent **90% des besoins startup** à 10–50x moins cher que le FFT [1]

<small>Sources : [1] [Anyscale](https://www.anyscale.com/blog/fine-tuning-llms-lora-or-full-parameter-an-in-depth-analysis-with-llama-2)</small>

---

# 03 — LoRA & QLoRA — la révolution

**LoRA** (Low-Rank Adaptation, ICLR 2022) entraîne de petites matrices au lieu du modèle entier :

- Entraîne **0,1–1%** des paramètres → **90–95%** de la qualité du FFT [1]
- Un adapter LoRA pèse **10–100 Mo** (vs 14+ Go pour un modèle complet)
- **QLoRA** (NeurIPS 2023) ajoute la quantification 4-bit → 7B sur **8 Go de VRAM** [2]

| Config | VRAM | Coût | Hardware minimum |
|--------|------|------|-----------------|
| 7B LoRA | ~16–24 GB | $5–15 | RTX 4090 |
| 7B QLoRA | ~8–10 GB | $0–5 | **Google Colab T4 gratuit** |
| 70B QLoRA | ~48 GB | $50–150 | A100 80 GB |

> Le rapport qualité/prix de QLoRA a **démocratisé** le Fine-tuning pour les startups

<small>Sources : [1] [Hu et al. ICLR 2022](https://arxiv.org/abs/2106.09685) · [2] [Dettmers et al. NeurIPS 2023](https://arxiv.org/abs/2305.14314)</small>

---

<!-- _class: cols -->

# 04 — Spotlight : Unsloth

<div class="left">

- **51 800+** stars GitHub, YC S24 [1]
- **2x** plus rapide, **80%** moins de VRAM
- QLoRA 7B sur Colab **gratuit** (T4 15 Go)
- Supporte GRPO jusqu'à 16B sur 16 Go VRAM
- Apache 2.0 — entièrement open-source

</div>
<div class="right">

- **Thèse** : rendre le Fine-tuning accessible à tous
- Contourne le coût GPU par l'optimisation CUDA
- Notebooks Colab prêts à l'emploi [2]
- LoRA, QLoRA, DPO, GRPO — tout en un
- L'outil de référence pour les GPU-poor

</div>

<small>Sources : [1] [Unsloth](https://unsloth.ai/) · [2] [GitHub Notebooks](https://github.com/unslothai/notebooks)</small>

---

# 05 — Techniques avancées

**Distillation** — transférer le savoir d'un gros modèle vers un petit :

- DeepSeek-R1 (671B) → Distill-Qwen-7B : **55,5%** sur AIME 2024, bat des modèles 4x plus gros [1]
- TensorZero : Gemini Flash fine-tuné sur GPT-4o → **24x** moins cher par succès [2]

**Model Merging** — fusionner des adapters sans entraînement supplémentaire (coût : $0)

**Données synthétiques** — générer ses données d'entraînement par LLM :

- 10K exemples via GPT-4 API : **$50–200** (vs $5 000–10 000 en annotation manuelle) [3]
- EntiGraph : 455M tokens synthétiques à partir de 1,3M réels → 80% de la qualité RAG [4]

<small>Sources : [1] [DeepSeek](https://arxiv.org/abs/2501.12948) · [2] [TensorZero](https://www.tensorzero.com/) · [3] Estimations agrégées · [4] [EntiGraph ICLR 2025](https://arxiv.org/abs/2409.07431)</small>

---

# 06 — Alignement : DPO, GRPO, RLHF

| Méthode | Complexité | Coût/run | Force | Limite |
|---------|-----------|----------|-------|--------|
| **DPO** | ⭐⭐ | $5–50 | Simple, pas de reward model | Moins flexible |
| **GRPO** | ⭐⭐⭐ | $10–30 | Reasoning, 50% moins de RAM que PPO | Besoin de réponses vérifiables |
| **RLHF/PPO** | ⭐⭐⭐⭐⭐ | $50–500+ | Gold standard, max contrôle | 4 modèles, très coûteux |

- **DPO** (Stanford, NeurIPS 2023) : 500–1 000 paires de préférences suffisent [1]
- **GRPO** (DeepSeek) : GSM8K 82,9% → 88,2% ; fonctionne avec 10 exemples [2]
- **RLHF** : réservé aux labs frontier (OpenAI, Anthropic) — 5–10x le coût du SFT

> Pour une startup : **DPO** pour l'alignement style/ton, **GRPO** pour le raisonnement

<small>Sources : [1] [Rafailov et al.](https://arxiv.org/abs/2305.18290) · [2] [DeepSeek](https://arxiv.org/abs/2402.03300)</small>

---

# 07 — Discussion : Choisir sa méthode

> Votre startup de **LegalTech** veut créer un assistant juridique. Vous avez **500 exemples** annotés par des avocats et un budget de **€5K**. Trois options :

| Option | Approche | Coût estimé | Résultat attendu |
|--------|----------|-------------|-----------------|
| A | **QLoRA** sur Mistral 7B via Unsloth | ~$0 (Colab) | +10–15% sur la tâche |
| B | **FFT** sur GPT-4o-mini via OpenAI | ~$3–5 | Qualité max, vendor lock-in |
| C | **RAG** avec base juridique | ~€200/mois | Données fraîches, citables |

**Questions pour la classe** :
- 500 exemples suffisent-ils pour du LoRA ? Pour du FFT ?
- Comment combiner RAG + Fine-tuning pour le meilleur des deux mondes ?
- Quel risque de vendor lock-in avec l'option B ?

---

<!-- _class: section -->

# Où fine-tuner ? Plateformes & outils

## Managed vs self-hosted

---

# 08 — Plateformes managées

| Plateforme | Modèles | Coût typique | Différenciateur |
|------------|---------|-------------|-----------------|
| **OpenAI** | GPT-4o, 4o-mini | ~$3–25/M tokens | DPO, RFT, écosystème mature |
| **Amazon Bedrock** | Claude, Llama, Titan | $8–50/run + hosting | Distillation, enterprise, RFT |
| **Google Vertex AI** | Gemini 2.5 Pro/Flash | Per-token, $300 crédits | LoRA natif, DPO Gemini |
| **Together AI** | 100+ open-source | $3–15/run (7B LoRA) | Multi-LoRA serverless |
| **Mistral** | Mistral, Mixtral | LoRA-based | **EU, RGPD natif** |

> Crédits gratuits : OpenAI 1M tokens/jour, Google $300, Together $5–25, AWS Activate $1K–100K

<small>Sources : [1] [OpenAI Pricing](https://platform.openai.com/docs/pricing) · [2] [Together AI](https://www.together.ai/pricing) · [3] [Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models)</small>

---

<!-- _class: cols -->

# 09 — Spotlight : Mistral La Plateforme

<div class="left">

- Fine-tuning **LoRA-based** natif
- Modèles français : Mistral, Mixtral, Magistral
- Data residency **Union Européenne**
- **RGPD** compliance by design
- API compatible OpenAI SDK

</div>
<div class="right">

- **Souveraineté** : alternative européenne aux GAFAM
- Vos données restent en **France/EU**
- Idéal pour secteurs régulés (santé, finance, public)
- Mistral valorisé **$6,2 Mds** (2025) [1]
- Levée de fonds €600M+ cumulés

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai/)</small>

---

# 10 — Outils open-source

| Outil | Stars GitHub | Interface | VRAM (7B QLoRA) | Force |
|-------|-------------|-----------|-----------------|-------|
| **LLaMA-Factory** | 67K+ | Web UI (LlamaBoard) | ~7–9 GB | 100+ modèles, zero-code [1] |
| **Axolotl** | 11K+ | YAML config | ~6–10 GB | GRPO, DPO, reproductibilité [2] |
| **Unsloth** | 51,8K+ | Python / Colab | ~5–8 GB | 2x vitesse, 80% moins VRAM [3] |

- Tous sous licence **Apache 2.0** — usage commercial libre
- Self-hosted = conformité **RGPD** totale (données ne quittent pas vos serveurs)
- **LLaMA-Factory** : Thomson Reuters +10% accuracy en analyse financière [1]

> Combinaison gagnante : **Unsloth** (moteur) + **Axolotl** (config YAML) + **Argilla** (données)

<small>Sources : [1] [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) · [2] [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) · [3] [Unsloth](https://unsloth.ai/)</small>

---

<!-- _class: cols -->

# 11 — Spotlight : Amazon Bedrock

<div class="left">

- Claude 3 Haiku fine-tuné : **99,6%** accuracy (+18%) [1]
- SK Telecom : **+73%** satisfaction client [2]
- Model Distillation : **500%** plus rapide, **75%** moins cher
- Reinforcement Fine-tuning (RFT) : +66% accuracy

</div>
<div class="right">

- Cas d'usage **enterprise** : données sensibles sur AWS
- Import de modèles custom (Llama, Mistral)
- **AWS Activate** : $1K–100K crédits startups
- ROI prouvé : modèle 7B bat un 70B sur tâches spécialisées
- Architecture complète MLOps intégrée

</div>

<small>Sources : [1] [AWS ML Blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/) · [2] [AWS Blog](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)</small>

---

# 12 — Discussion : Build vs Buy

> Votre **AI SaaS** sert 50 clients B2B, chacun veut un modèle personnalisé. Budget : **€30K/an** pour l'infrastructure ML. Trois architectures possibles :

| Option | Approche | Coût annuel estimé | Scalabilité |
|--------|----------|-------------------|-------------|
| A | **Managed** (OpenAI FT par client) | ~€15–50K | Simple mais vendor lock-in |
| B | **Self-hosted** + LLaMA-Factory | ~€10–30K | Contrôle total, ops lourdes |
| C | **Multi-LoRA** (1 base + N adapters) | ~€8–20K | Optimal, 5–20x moins de GPU |

**Questions pour la classe** :
- L'option C (Multi-LoRA) est 5–20x moins chère : quel est le piège ?
- Un client dans la santé exige que ses données restent en France — quelle option ?
- Comment facturer le Fine-tuning à vos clients B2B ?

---

<!-- _class: section -->

# La qualité des données : le vrai levier

## Data quality > model size

---

# 13 — Pourquoi les données > les paramètres

Le cas **Notus-7B** illustre la puissance de la qualité des données :

- L'équipe Argilla a corrigé **~100 exemples mal labelisés** dans UltraFeedback [1]
- Résultat : un modèle 7B **bat Claude 2** sur AlpacaEval
- Correction de quelques centaines d'exemples → **+5–15%** sur les benchmarks

| Levier | Impact typique | Coût |
|--------|---------------|------|
| Plus de données (quantité) | +2–5% | $$$ |
| Meilleur modèle (taille) | +3–8% | $$$$ |
| **Meilleures données (qualité)** | **+5–15%** | **$** |

> La qualité des données est le **meilleur ROI** en Fine-tuning. Investissez dans la curation, pas dans les GPU [1]

<small>Sources : [1] [Argilla / Notus-7B](https://argilla.io/blog/notus7b/)</small>

---

<!-- _class: cols -->

# 14 — Spotlight : Argilla

<div class="left">

- Acquis par **Hugging Face** ($10M, 2024) [1]
- **4 600+** stars GitHub, Apache 2.0
- Curation de données d'entraînement
- A produit le dataset derrière **Notus-7B** [2]
- Compagnon : **distilabel** (données synthétiques)

</div>
<div class="right">

- **Thèse** : la qualité des données est le moat
- Self-hosted = **RGPD** compliance totale
- Gratuit sur HF Spaces, $5/mois persistent
- Trouvé 50+ erreurs en **5 minutes** dans un benchmark
- Alternative à Scale AI ($0,08–0,40/annotation)

</div>

<small>Sources : [1] [Hugging Face Blog](https://huggingface.co/blog/argilla-ui-hub) · [2] [Notus-7B](https://argilla.io/blog/notus7b/)</small>

---

# 15 — Pipeline données : annotation → synthétique → évaluation

Le workflow complet pour des données de Fine-tuning de qualité :

| Étape | Outil | Rôle | Coût |
|-------|-------|------|------|
| **Annotation** | Label Studio / Argilla | Labeling humain + pré-annotation LLM | $0 (open-source) |
| **Synthétique** | distilabel / GPT-4 API | Générer 10K exemples | $50–200 |
| **Curation** | Argilla | Nettoyer, corriger, valider | $0 (open-source) |
| **Évaluation** | RAGAS / Arena / LLM-as-judge | Mesurer la qualité du modèle | $0–500 |

- Le pré-labeling par LLM réduit les coûts d'annotation de **50–80%** [1]
- Données labellisées correctement → **+15–30%** vs Prompt Engineering seul [1]

> Budget data : **80% du temps** sur la curation, 20% sur l'entraînement

<small>Sources : [1] [Label Studio](https://labelstud.io/)</small>

---

<!-- _class: section -->

# L'économie du Fine-tuning

## Coûts, ROI, architecture

---

# 16 — Coûts par approche

| Approche | Coût | Cas d'usage |
|----------|------|-------------|
| **QLoRA + Colab** | **$0** (gratuit) | POC, prototypage, formation |
| **LoRA cloud** (Together AI) | $3–15/run | Production startup |
| **Managed** (OpenAI, Bedrock) | $25–100/run | Enterprise, compliance |
| **CPT** (7B, 1B tokens) | $2K–25K | Domaine spécialisé (médical, juridique) |
| **CPT at scale** (BloombergGPT) | $1–3M+ | Foundation model propriétaire |

Coûts cachés à budgéter :

- Préparation des données : **20–40%** du coût total
- Compliance EU AI Act : **+10–20%** overhead [1]
- Safety evaluation : **$500–2 000** par version de modèle

<small>Sources : [1] Estimations agrégées depuis [Scopicsoftware](https://scopicsoftware.com/blog/cost-of-fine-tuning-llms/) · [Ptolemay](https://www.ptolemay.com/post/llm-total-cost-of-ownership)</small>

---

# 17 — Fine-tuning vs RAG : le framework décisionnel

| Critère | RAG | Fine-tuning | Gagnant |
|---------|-----|-------------|---------|
| **Données fraîches** | ✅ Temps réel | ❌ Statique | RAG |
| **Coût initial** | ~$70–1K/mois | $5–50/run | Fine-tuning |
| **Latence** | +200–500ms (retrieval) | Aucun overhead | Fine-tuning |
| **Traçabilité** | ✅ Sources citables | ❌ Boîte noire | RAG |
| **Style/format** | ❌ Limité | ✅ Total contrôle | Fine-tuning |

- Breakeven volume : Fine-tuning plus rentable à partir de **~10K–50K requêtes/jour** [1]
- L'approche hybride **RAFT** surpasse les deux de **+10–20%** [2]

> Le bon choix dépend du volume, de la fraîcheur et du budget — pas de la hype

<small>Sources : [1] [DEV Community](https://dev.to/remojansen/rag-vs-fine-tuning-which-one-wins-the-cost-game-long-term-12dg) · [2] [RAFT UC Berkeley](https://arxiv.org/abs/2403.10131)</small>

---

# 18 — Multi-LoRA : l'architecture SaaS pour l'IA

Le pattern **Multi-LoRA** permet de servir N clients avec un seul modèle de base :

- **1 base model** (ex : Llama 3 70B) + **N adapters LoRA** (10–100 Mo chacun)
- S-LoRA : gère **2 000+ adapters** simultanés, 4x le throughput [1]
- Réduction GPU : **5–20x** vs une instance par client

| Architecture | Coût pour 50 clients | Complexité |
|-------------|---------------------|------------|
| 1 modèle par client | 50× $500/mois = **$25K/mois** | Simple |
| Multi-LoRA | 1× $500 + 50× $2 = **$600/mois** | Moyenne |

> Le Multi-LoRA est le **nouveau SaaS pattern** pour les produits IA B2B personnalisés

<small>Sources : [1] [S-LoRA / LMSYS](https://lmsys.org/blog/2023-11-15-slora/)</small>

---

# 19 — Discussion : Le budget Fine-tuning

> Vous lancez une startup **MedTech** avec **€15K** de budget ML. Vous avez **10K exemples** médicaux annotés par des médecins. L'objectif : un assistant de pré-diagnostic. Trois stratégies :

| Option | Approche | Coût estimé | Risque |
|--------|----------|-------------|--------|
| A | **CPT** + LoRA sur Mistral 7B | ~€5–8K | Catastrophic forgetting |
| B | **QLoRA** directement sur Llama 3 8B | ~€0–500 | Pas de jargon médical |
| C | **RAG** + QLoRA hybride | ~€2–5K | Complexité ops |

**Questions pour la classe** :
- Domaine médical = haut risque. L'EU AI Act classe-t-il votre outil en "high risk" ?
- Comment évaluer qu'un modèle médical est assez bon pour la production ?
- Quel budget pour l'alignement safety (hallucinations médicales = danger vital) ?

---

# 20 — Sécurité & alignement : le coût caché

Le Fine-tuning peut **casser les garde-fous** d'un modèle :

- **10 exemples adversariaux** suffisent à jailbreak GPT-3.5 Turbo (<$0,20) [1]
- Le CPT est **15,7%** plus néfaste pour la safety que l'exposition à du contenu harmful [1]
- LoRA **réduit substantiellement** la dégradation safety vs FFT

Mitigation obligatoire :

| Mesure | Coût | Impact |
|--------|------|--------|
| 5–10% d'exemples safety dans le dataset | ~$0 | Préserve l'alignement |
| Safety evaluation post-training | $500–2K | Détecte les régressions |
| Audit tiers (EU AI Act) | $2K–10K/an | Compliance réglementaire |

> EU AI Act : non-compliance = jusqu'à **€15M** ou **3%** du CA global [2]

<small>Sources : [1] [Qi et al. ICLR 2024](https://arxiv.org/abs/2310.03693) · [2] [EU AI Act](https://artificialintelligenceact.eu/)</small>

---

# 21 — 5 décisions clés pour l'entrepreneur

| # | Décision | Recommandation |
|---|----------|---------------|
| 1 | **Méthode** | Commencer par **QLoRA** — gratuit, 90%+ de la qualité [1] |
| 2 | **Données** | Investir dans la **curation** (Argilla) avant les GPU [2] |
| 3 | **Souveraineté** | **Mistral / self-hosted** pour les données EU sensibles |
| 4 | **Alignement** | **Non optionnel** — 5–10% d'exemples safety dans chaque dataset |
| 5 | **Architecture B2B** | **Multi-LoRA** pour servir N clients à coût marginal ~$0 [3] |

> Le Fine-tuning n'est plus réservé aux Big Tech. Avec QLoRA + Unsloth + Colab, un étudiant peut fine-tuner un 7B **gratuitement** en 30 minutes.

Le vrai avantage compétitif n'est pas le modèle — c'est la **qualité de vos données** et votre **pipeline de curation**.

<small>Sources : [1] [Anyscale](https://www.anyscale.com/blog/fine-tuning-llms-lora-or-full-parameter-an-in-depth-analysis-with-llama-2) · [2] [Argilla](https://argilla.io/blog/notus7b/) · [3] [S-LoRA](https://lmsys.org/blog/2023-11-15-slora/)</small>

---

<!-- _class: section -->

# Synthèse

## Personnaliser avec méthode, déployer avec responsabilité
