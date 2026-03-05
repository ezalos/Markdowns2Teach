---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Évaluation · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Recherche LLM Evaluation 2024–2026 · Données publiques"
---

<!-- ABOUTME: Deck de référence sur l'évaluation des LLMs : métriques de génération, benchmarks, VQA, pricing et pièges. -->
<!-- ABOUTME: Cadré pour étudiants M2 non-ingénieurs, approche business-first avec données vérifiées février 2026. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Évaluer les LLMs

## Métriques, Benchmarks et Pricing

Deep Tech & ML (UE3) · Évaluation
M2 IMT&E · Paris 1 Panthéon-Sorbonne

---

<!-- _class: section -->

# Introduction

## Un prestataire annonce 95 % sur MMLU — est-ce suffisant ?

---

# 01 — Le défi de l'évaluation LLM

- Votre startup doit choisir entre **GPT-5**, **Claude Opus 4.6** et **Gemini 3 Pro**
- Le prestataire annonce "95 % de précision" — mais sur **quel test** ? Avec **quelles données** ?
- Deux grandes familles de mesures à maîtriser :
  - **Métriques de génération** : la qualité du texte produit (BLEU, ROUGE, BERTScore)
  - **Benchmarks** : des examens standardisés (MMLU, GSM8K, HumanEval)
- Enjeu business : un mauvais choix de modèle peut **coûter 100x trop cher** [1]
- Ou pire : un modèle performant sur un benchmark mais médiocre sur **votre cas d'usage**

> **Objectif du deck** : vous donner les outils pour évaluer, comparer et choisir un LLM en connaissance de cause.

<small>Sources : [1] [CostGoat](https://costgoat.com/compare/llm-api)</small>

---

<!-- _class: cols -->

# 02 — Deux familles de mesures

<div class="left">

**Métriques de génération**

- Qualité du **texte produit**
- Comparaison à une référence humaine
- Ex. : BLEU, ROUGE, BERTScore

> Comme noter une copie vs un corrigé type.

</div>
<div class="right">

**Benchmarks standardisés**

- **Capacités** du modèle (QCM, maths, code)
- Score sur un jeu de données fixe
- Ex. : MMLU, GSM8K, HumanEval

> Comme un concours : même épreuve pour tous.

</div>

---

<!-- _class: section -->

# Métriques de Génération

## Mesurer la qualité du texte produit par un LLM

---

<!-- _class: compact -->

# 03 — Perplexity : le modèle hésite-t-il ?

- Mesure l'**incertitude** du modèle devant le mot suivant
- Intuition : "parmi combien de mots hésite-t-il à chaque pas ?"
- **Formule** : PP(W) = 2^(−1/N × Σ log₂ P(wᵢ))
- PP = **10** → hésite entre 10 mots · PP = **50** → 50 mots (plus incertain)
- **Plus c'est bas, mieux c'est** — le modèle est plus "sûr de lui"
- Utilisée pour comparer des modèles **entre eux** sur un même corpus

![bg right:35%](assets/infographics/perplexity-visual_run_20260301_174623_1ebe11.png)
<!-- PB: Illustration of perplexity as choosing between N doors/words -->

---

<!-- _class: compact -->

# 04 — Perplexity : les limites

- **Faible Perplexity ≠ bon texte** — confiant mais **ennuyeux** possible
- "le le le le" → Perplexity très basse, texte inutile
- Ne mesure **ni la cohérence, ni la créativité, ni l'utilité**
- Dépend du **tokenizer** : GPT vs Llama incomparables directement
- Utile pour le **pré-training**, rarement pour l'évaluation produit

> Le "pouls" du modèle : dit s'il est vivant, pas s'il est en bonne santé.

![bg right:35%](assets/infographics/perplexity-failure_run_20260301_174625_8f317e.png)
<!-- PB: Low perplexity but repetitive/boring text vs high perplexity but creative -->

---

<!-- _class: compact -->

# 05 — BLEU : précision des n-grams

- **BLEU** (2002) : compare les **n-grams** générés vs référence [1]
- Mesure la **Precision** : fraction des mots générés présents dans la référence
- BLEU-1 = unigrammes · BLEU-4 = séquences de 4 mots (standard)
- **Brevity Penalty** : pénalise les traductions trop courtes
- Score **0–1** (souvent en %) — plus c'est haut, mieux c'est
- Limite : ignore **synonymes** et paraphrases

![bg right:35%](assets/infographics/bleu-ngram_run_20260301_183046_0888ca.png)
<!-- PB: N-gram matching between generated and reference sentences -->

<small>Sources : [1] [Papineni et al., ACL 2002](https://aclanthology.org/P02-1040/)</small>

---

<!-- _class: compact -->

# 06 — ROUGE : le rappel du résumé

- **ROUGE** (2004) : conçu pour évaluer le résumé automatique [1]
- Mesure le **Recall** : fraction des mots de la référence capturée
- **ROUGE-N** : rappel n-grams (ROUGE-1 unigrammes, ROUGE-2 bigrammes)
- **ROUGE-L** : plus longue sous-séquence commune (LCS) — capture l'ordre
- Complémentaire à BLEU : BLEU = precision, ROUGE = recall
- Standard industrie pour les **pipelines de résumé**

![bg right:35%](assets/infographics/rouge-coverage_run_20260301_183046_8e1288.png)
<!-- PB: Reference text with highlighted words showing recall coverage -->

<small>Sources : [1] [Lin, ACL 2004](https://aclanthology.org/W04-1013/)</small>

---

<!-- _class: cols -->

# 07 — BLEU vs ROUGE : Precision vs Recall

<div class="left">

**BLEU (Precision)**

- "Ce que le modèle dit est-il **juste** ?"
- Pénalise les mots inventés
- Idéal : traduction, génération fidèle

> Résumé de 3 mots corrects → BLEU parfait.

</div>
<div class="right">

**ROUGE (Recall)**

- "Le modèle a-t-il **tout capturé** ?"
- Pénalise les omissions
- Idéal : résumé, extraction d'info

> Résumé très long → ROUGE parfait mais bruyant.

![bg right:30%](assets/infographics/bleu-vs-rouge_run_20260301_183046_c713a2.png)
<!-- PB: Precision vs Recall visual for text generation metrics -->

</div>

---

# 08 — METEOR : au-delà des mots exacts

- **METEOR** ajoute trois améliorations clés par rapport à BLEU [1] :
  - **Stemming** : "running" et "ran" sont considérés comme un match
  - **Synonymes** : "car" et "automobile" sont reconnus via WordNet
  - **Ordre des mots** : pénalise les permutations excessives
- Combine Precision et Recall avec une **moyenne harmonique pondérée**
- Corrèle mieux avec le **jugement humain** que BLEU sur la traduction [1]
- Limite : dépend de ressources linguistiques (WordNet) → moins robuste en français
- En pratique : utilisé comme complément à BLEU, rarement seul


<small>Sources : [1] [Banerjee & Lavie, ACL 2005](https://aclanthology.org/W05-0909/)</small>

---

<!-- _class: compact -->

# 09 — BERTScore : la similarité sémantique

- Utilise les **embeddings** BERT pour comparer les textes [1]
- **Similarité cosinus** entre vecteurs au lieu de compter les mots identiques
- Détecte les **paraphrases** : "le chat dort" ≈ "le félin sommeille"
- Produit Precision, Recall et F1 — **indépendant de la formulation exacte**
- Utilisé pour chatbots, génération créative, résumé abstractif
- Limite : plus lent, dépend du modèle BERT sous-jacent

![bg right:35%](assets/infographics/bertscore-embedding_run_20260301_183117_90814c.png)
<!-- PB: Embedding vectors showing cosine similarity between paraphrased sentences -->

<small>Sources : [1] [Zhang et al., ICLR 2020](https://arxiv.org/abs/1904.09675)</small>

---

# 10 — Le paradoxe BLEU : GPT-3.5 bat GPT-4

- Observation contre-intuitive : GPT-4o-mini **sous-performe** GPT-3.5 sur BLEU [1]
- Pourtant GPT-4o-mini est meilleur sur Accuracy (99,9 %) et Helpfulness (97 %)
- **Explication** : GPT-4 reformule davantage → moins de mots identiques à la référence
- Les modèles plus puissants produisent des **paraphrases** de meilleure qualité
- BLEU pénalise la reformulation car il ne comprend **que les mots exacts**
- BERTScore (82-83 % pour les deux) reflète mieux la qualité **sémantique** réelle

> Le paradoxe BLEU montre pourquoi une seule métrique ne suffit jamais.


<small>Sources : [1] [Weights & Biases](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)</small>

---

# 11 — Comparatif : 5 métriques de génération

| Métrique | Mesure | Forces | Faiblesses | Usage type |
|---|---|---|---|---|
| **Perplexity** | Incertitude | Rapide, universel | Pas lié à la qualité | Pré-training |
| **BLEU** | Precision n-grams | Standard traduction | Ignore synonymes | Traduction |
| **ROUGE** | Recall n-grams | Mesure la couverture | Ignore la précision | Résumé |
| **METEOR** | Precision+Recall+ordre | Synonymes, stemming | Dépend de WordNet | Traduction |
| **BERTScore** | Similarité sémantique | Paraphrases, sens | Lent, modèle-dépendant | Chatbots, créatif |

> **Règle d'or** : utilisez toujours **au moins deux métriques** complémentaires.

---

# 12 — Discussion : startup de traduction juridique

- **Scénario** : une startup de LegalTech vous propose un service de traduction de contrats
- Leur pitch : "notre modèle obtient **BLEU-4 de 0.45** sur les documents juridiques"
- Vous devez décider si vous signez un contrat de **€200k/an**

> **Questions pour la classe** :
> 1. BLEU seul est-il suffisant pour évaluer un traducteur juridique ?
> 2. Quels risques si le modèle utilise un synonyme "acceptable" au lieu du terme légal exact ?
> 3. Quelle combinaison de métriques proposeriez-vous dans le cahier des charges ?

---

<!-- _class: section -->

# Benchmarks par Type de Tâche

## Les examens standardisés des LLMs

---

<!-- _class: compact -->

# 13 — Qu'est-ce qu'un Benchmark ?

- **Examen standardisé** passé par tous les modèles
- Analogie : le **BAC** — même épreuve, correction uniforme
- Composé de : **dataset** + **protocole** + **score**
- Compare objectivement des modèles de différents fournisseurs
- Ex. : MMLU (culture gén.), GSM8K (maths), HumanEval (code)
- Un bon benchmark ne garantit pas la performance sur **votre tâche**

![bg right:35%](assets/infographics/benchmark-concept_run_20260301_183117_d8323a.png)
<!-- PB: Analogy diagram showing BAC exam vs LLM benchmark components -->

---

# 14 — MMLU : le QCM universel

- **MMLU** = Massive Multitask Language Understanding [1]
- **57 matières** : histoire, droit, médecine, physique, informatique...
- **16 000+ QCM** à 4 choix — couvre du lycée au niveau expert
- Score SOTA (fév. 2026) : **GPT-5.3 Codex — 93 %** [2]
- Le benchmark historique le plus cité — mais en voie de **saturation**
- L'écart entre le top-1 et le top-10 est passé de 11,9 % à **5,4 %** en un an [3]
- Variante plus dure : **MMLU-Pro** (10 choix, questions plus complexes)

<small>Sources : [1] [Hendrycks et al., ICLR 2021](https://arxiv.org/abs/2009.03300) · [2] [LXT.ai](https://www.lxt.ai/blog/llm-benchmarks/) · [3] [Stanford HAI 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: cols -->

# 15 — Exemple MMLU : question type

<div class="left">

**Question (Astronomie)**

Où la plupart des comètes à courte période trouvent-elles leur origine ?

- (A) Le nuage d'Oort
- (B) L'espace interstellaire
- (C) La ceinture de Kuiper ✓
- (D) La ceinture d'astéroïdes

</div>
<div class="right">

**Ce que ça teste**

- Connaissance factuelle universitaire
- QCM 4 choix → évaluation automatique

> Simple à noter, mais ne teste pas la capacité à expliquer.

</div>

---

# 16 — Benchmarks de raisonnement

| Benchmark | Domaine | Format | SOTA (fév. 2026) | Saturé ? |
|---|---|---|---|---|
| **MMLU-Pro** | 57 matières | QCM 10 choix | Gemini 3 Pro — 89,8 % [1] | Non |
| **GPQA Diamond** | Sciences PhD | QCM expert | Gemini 3.1 Pro — 94,3 % [2] | Approche |
| **HellaSwag** | Sens commun | Complétion | Multiples — 95 %+ [2] | Oui |
| **TruthfulQA** | Véracité | QCM + libre | Variable selon config | Non |

- **GPQA Diamond** : questions rédigées par des doctorants, les non-experts obtiennent ~34 % [2]
- **HellaSwag** est saturé à 95 %+ — il ne discrimine plus les modèles frontier

<small>Sources : [1] [Awesome Agents](https://awesomeagents.ai/leaderboards/overall-llm-rankings-feb-2026/) · [2] [LXT.ai](https://www.lxt.ai/blog/llm-benchmarks/)</small>

---

# 17 — Benchmarks de mathématiques

| Benchmark | Niveau | Format | SOTA (fév. 2026) | Saturé ? |
|---|---|---|---|---|
| **GSM8K** | CM2/collège | Word problems | ~95 %+ | Oui |
| **MATH-500** | Lycée/prépa | Problèmes formels | Kimi K2.5 — 98 % [1] | Approche |
| **AIME 2025** | Compétition | Olympiade | Step-3.5 — 97,3 % [1] | Non |
| **FrontierMath** | Recherche | Problèmes ouverts | ~2 % [2] | Non |

- **GSM8K** était le gold standard — aujourd'hui saturé, tous les frontier > 95 %
- **FrontierMath** : les meilleurs modèles ne résolvent que **2 % des problèmes** [2]
- La difficulté a explosé : du collège en 2022 à la recherche en 2025

<small>Sources : [1] [Open LLM Leaderboard 2026](https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now/) · [2] [Stanford HAI 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report)</small>

---

<!-- _class: cols -->

# 18 — Exemple GSM8K : problème de maths

<div class="left">

**Question**

Natalia a vendu 48 barrettes en avril, puis la moitié en mai. Total ?

**Chain-of-thought** :
1. Avril : 48
2. Mai : 48 / 2 = 24
3. Total : 48 + 24 = **72**

</div>
<div class="right">

**Ce que ça teste**

- Raisonnement **multi-étapes**
- Le chain-of-thought est la clé

> Niveau CM2 pour un humain, mais les LLMs n'ont atteint 95 %+ qu'en 2024.

</div>

---

# 19 — Benchmarks de code

| Benchmark | Tâche | Format | SOTA (fév. 2026) | Saturé ? |
|---|---|---|---|---|
| **HumanEval** | Génération Python | 164 fonctions | Kimi K2.5 — 99 % [1] | Oui |
| **SWE-bench Verified** | Résolution de bugs | Pull requests réels | Claude Opus 4.6 — 79,2 % [2] | Non |
| **LiveCodeBench** | Problèmes frais | Concours récents | Step-3.5 — 86,4 % [1] | Non |

- **HumanEval** : saturé à 99 %, ne discrimine plus les modèles frontier
- **SWE-bench** : le vrai test — résoudre des bugs dans de vrais repos GitHub
- **LiveCodeBench** : problèmes de compétition récents → impossible de tricher par mémorisation

<small>Sources : [1] [Open LLM Leaderboard 2026](https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now/) · [2] [VALS.ai](https://www.vals.ai/benchmarks/swebench)</small>

---

# 20 — Instruction Following et évaluation humaine

- **IFEval** : teste si le modèle respecte des **contraintes précises** [1]
  - "Écris en 3 paragraphes, commence par 'Bonjour', utilise au moins 2 citations"
- **MT-Bench** : un LLM-juge (GPT-4) note les réponses de 1 à 10
- **Chatbot Arena** : le "classement Elo" des LLMs par **vote humain** [2]
  - 6M+ votes en A/B testing aveugle — la référence pour la préférence humaine
- Scores IFEval (fév. 2026) : Kimi K2.5 — 94 %, Claude Opus 4.6 — ~89 % [1]

> Les benchmarks automatiques mesurent la **capacité**. L'Arena mesure la **préférence** humaine.

<small>Sources : [1] [Open LLM Leaderboard 2026](https://vertu.com/lifestyle/open-source-llm-leaderboard-2026-rankings-benchmarks-the-best-models-right-now/) · [2] [LM Arena](https://arena.ai/leaderboard)</small>

---

<!-- _class: compact -->

# 21 — Chatbot Arena : le classement par vote humain

- Deux modèles anonymes répondent → l'utilisateur vote pour le meilleur
- Système **Elo** (comme aux échecs) · **Top 5 (fév. 2026)** [1] :

| Rang | Modèle | Elo | Force principale |
|---|---|---|---|
| 1 | Claude Opus 4.6 Thinking | 1 503 | Coding, instruction |
| 2 | Claude Opus 4.6 | 1 503 | Agentic planning |
| 3 | Gemini 3.1 Pro | 1 500 | Sciences, math |
| 4 | Grok 4.20 | 1 495 | Raisonnement |
| 5 | Gemini 3 Pro | 1 486 | Multimodal |

![bg right:30%](assets/infographics/chatbot-arena_run_20260301_183117_eb7580.png)
<!-- PB: Arena blind comparison process: prompt → two anonymous models → user vote → Elo update -->

<small>Sources : [1] [LM Arena](https://arena.ai/leaderboard) (fév. 2026)</small>

---

# 22 — Carte des benchmarks par tâche

- Chaque benchmark teste une **facette** du modèle — aucun ne teste tout

| Capacité | Benchmarks clés |
|---|---|
| **Connaissance générale** | MMLU, MMLU-Pro |
| **Raisonnement scientifique** | GPQA Diamond, TruthfulQA |
| **Mathématiques** | GSM8K, MATH-500, AIME 2025 |
| **Code** | HumanEval, SWE-bench, LiveCodeBench |
| **Instruction following** | IFEval, MT-Bench |
| **Préférence humaine** | Chatbot Arena Elo |

![bg right:30%](assets/infographics/benchmark-taxonomy-matrix_run_20260301_183148_1a1e1c.png)
<!-- PB: Task-to-benchmark matrix color-coded by saturation level -->

---

# 23 — Benchmarks frontier : les derniers remparts

- Les benchmarks classiques sont **saturés** → il faut des tests plus durs [1]
- **Humanity's Last Exam (HLE)** : 2 500 questions d'experts, score max : **8,8 %** [1]
- **FrontierMath** : problèmes mathématiques de recherche, score max : **2 %** [1]
- **BigCodeBench** : tâches de code complexes, meilleur score : **35,5 %** (humain : 97 %) [1]
- **ARC-AGI-2** : puzzles de raisonnement abstrait, Gemini 3.1 Pro : **77,1 %** [2]
- Ces benchmarks montrent que les LLMs sont encore **loin** des capacités humaines expertes
- Ils sont conçus pour rester pertinents **plusieurs années**

<small>Sources : [1] [Stanford HAI 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [2] [AI Dev Day India](https://aidevdayindia.org/blogs/lmsys-chatbot-arena-current-rankings/)</small>

---

# 24 — Discussion : MMLU #1 = le meilleur pour vous ?

- **Scénario** : vous développez un chatbot juridique pour un cabinet d'avocats parisien
- Trois modèles candidats :

| Modèle | MMLU | SWE-bench | Arena Elo | IFEval | Prix (in/out 1M) |
|---|---|---|---|---|---|
| Modèle A | **93 %** | 65 % | 1 402 | 85 % | $10 / $30 |
| Modèle B | 91 % | **80 %** | 1 503 | **89 %** | $15 / $75 |
| Modèle C | 90 % | 63 % | 1 486 | 87 % | $1,25 / $5 |

> **Questions** :
> 1. Quel modèle choisiriez-vous et pourquoi ?
> 2. Quel benchmark manque dans ce tableau pour un chatbot juridique ?

---

<!-- _class: section -->

# Visual Question Answering (VQA)

## Quand l'IA lit vos documents, photos et graphiques

---

<!-- _class: compact -->

# 25 — Qu'est-ce que le VQA ?

- **VQA** = Visual Question Answering : image + question texte → réponse texte
- Le modèle doit **comprendre** l'image ET la question pour répondre
- **Cas d'usage business** :
  - Extraction de données depuis des **factures PDF**
  - Analyse de **graphiques** dans des rapports financiers
  - Lecture de **panneaux**, **menus**, **étiquettes** dans des photos
  - Assistance visuelle pour personnes **malvoyantes**
- Nécessite des modèles **multimodaux** : GPT-5, Gemini, Claude

![bg right:35%](assets/infographics/vqa-pipeline_run_20260301_183148_f1c158.png)
<!-- PB: VQA pipeline: image + text question → multimodal model → text answer -->

---

# 26 — Benchmarks VQA : le paysage

| Benchmark | Tâche | Taille | SOTA (fév. 2026) |
|---|---|---|---|
| **VQAv2** | Questions sur images | 1,1M | > 84 % (saturé) [1] |
| **TextVQA** | Texte dans les images | 45K | Gemini ≈ 78 % [2] |
| **DocVQA** | Documents scannés | 50K | Qwen2.5 VL — 96,4 % [3] |
| **ChartQA** | Graphiques, charts | 33K | Llama 4 ≈ 90 % [4] |
| **MMMU** | Raisonnement multimodal | 11,5K | Llama 4 — 73,4 % [4] |

- **DocVQA** est le plus pertinent pour les cas business (factures, contrats)
- **MMMU** teste le raisonnement visuel avancé (diagrammes scientifiques, art)

<small>Sources : [1] [Stanford HAI](https://hai.stanford.edu/news/ai-benchmarks-hit-saturation) · [2] [HuggingFace](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) · [3] [LLM Stats](https://llm-stats.com/benchmarks/docvqa) · [4] [Ultra AI Guide](https://ultraaiguide.com/llama-4-series-2026-comprehensive-guide/)</small>

---

<!-- _class: cols -->

# 27 — Exemples VQA : TextVQA et DocVQA

<div class="left">

**TextVQA**

- Photo d'un **panneau** → "Nom de la rue ?"
- Le modèle doit **lire** le texte dans l'image
- Difficulté : reflets, angles, polices

</div>
<div class="right">

**DocVQA**

- **Facture** scannée → "Montant total ?"
- Comprendre la **structure** du document
- Difficulté : tableaux, mise en page

> Pour la fintech, DocVQA est le benchmark le plus prédictif du réel.

</div>

---

# 28 — ChartQA : lire un graphique

- **ChartQA** teste la capacité à **extraire des données** de graphiques [1]
- Types de charts : barres, lignes, camemberts, scatter plots
- Questions : "Quel pays a le PIB le plus élevé ?" ou "De combien le chiffre a-t-il augmenté ?"
- Nécessite : OCR + compréhension spatiale + raisonnement numérique
- Score SOTA : **Llama 4 Maverick ≈ 90 %**, GPT-4o ≈ 86 % [2]
- **Cas business** : automatiser l'analyse de rapports financiers, études de marché
- Limite : les graphiques réels sont souvent **plus complexes** que ceux du benchmark

<small>Sources : [1] [Masry et al., ACL 2022](https://aclanthology.org/2022.findings-acl.177/) · [2] [Ultra AI Guide](https://ultraaiguide.com/llama-4-series-2026-comprehensive-guide/)</small>

---

# 29 — DocVQA : le standard pour les documents

- **DocVQA** : 50 000 questions sur 12 000+ documents (lettres, mémos, rapports) [1]
- Métrique : **ANLS** (Average Normalized Levenshtein Similarity) — tolère les fautes OCR
- **Leaderboard (fév. 2026)** [2] :

| Rang | Modèle | Score | Paramètres |
|---|---|---|---|
| 1 | Qwen2.5 VL 72B | 96,4 % | 72B |
| 2 | Qwen2.5 VL 7B | 95,7 % | 8B |
| 3 | Claude 3.5 Sonnet | 95,2 % | N/A |
| 4 | Llama 4 Maverick | 94,4 % | 400B |

- Le fait que Qwen 7B rivalise avec des modèles 50x plus gros est remarquable

<small>Sources : [1] [DocVQA](https://www.docvqa.org/) · [2] [LLM Stats](https://llm-stats.com/benchmarks/docvqa)</small>

---

# 30 — Discussion : startup fintech et extraction PDF

- **Scénario** : votre startup traite **10 000 factures/mois** pour des PME
- Vous devez extraire : montant total, date, numéro de TVA, lignes de détail
- Deux options :

| Option | Modèle | DocVQA | Coût/1M tokens |
|---|---|---|---|
| A | Qwen2.5 VL 72B | 96,4 % | Open-source (infra) |
| B | Claude 3.5 Sonnet | 95,2 % | $3 / $15 |

> **Questions** :
> 1. 1,2 point d'écart sur DocVQA justifie-t-il le coût d'hébergement d'un modèle 72B ?
> 2. Quels tests devriez-vous faire **en plus** du benchmark sur vos propres factures ?

---

<!-- _class: section -->

# Prix vs Performance

## Combien coûte l'intelligence ?

---

# 31 — Paysage tarifaire 2026

| Modèle | Input/1M | Output/1M | Arena Elo | Tier |
|---|---|---|---|---|
| **DeepSeek V3.2** | $0,27 | $0,42 | 1 361 | Budget |
| **GPT-5 Mini** | $0,25 | $2,00 | — | Budget |
| **Gemini 2.5 Flash** | $0,15 | $0,60 | 1 335 | Budget |
| **Claude Sonnet 4** | $3,00 | $15,00 | — | Mid |
| **GPT-5.2** | $1,75 | $14,00 | 1 481 | Mid-Premium |
| **Claude Opus 4.6** | $5,00 | $25,00 | 1 503 | Premium |
| **GPT-5.2 Pro** | $21,00 | $168,00 | — | Ultra-Premium |

<small>Sources : [CostGoat](https://costgoat.com/compare/llm-api) · [TLDL](https://www.tldl.io/resources/llm-api-pricing-2026) · [SiliconData](https://www.silicondata.com/blog/llm-cost-per-token) (fév. 2026)</small>

---

# 32 — Déflation des prix : -80 % par an

- Le coût d'un LLM de niveau GPT-3.5 a chuté de **1 000x en 3 ans** [1]
  - Nov. 2021 (GPT-3) : **$60/M tokens** → 2024 (Llama 3.2 3B) : **$0,06/M tokens**
- Le coût de niveau GPT-4 a chuté de **98 %** depuis 2023 : de $60 à $0,75/M [2]
- Selon Epoch AI, la baisse médiane est de **50x/an** tous benchmarks confondus [3]
- Après janvier 2024, la baisse s'est accélérée à **200x/an** pour les tâches scientifiques [3]
- L'écart entre le moins cher et le plus cher est de **1 000x** [4]
  - Gemini Flash-Lite : $0,10/M vs GPT-5.2 Pro : $94,50/M (blended)

<small>Sources : [1] [a16z](https://a16z.com/llmflation-llm-inference-cost/) · [2] [CloudIDR](https://www.cloudidr.com/blog/llm-pricing-comparison-2026) · [3] [Epoch AI](https://epoch.ai/data-insights/llm-inference-price-trends) · [4] [TLDL](https://www.tldl.io/resources/llm-api-pricing-2026)</small>

---

<!-- _class: compact -->

# 33 — Prix vs Score : le scatter plot

- Les modèles les plus chers ne sont **pas toujours** les meilleurs [1]
- **Best value** : DeepSeek V3.2 — quality 79/100, $0,28/M output
- **Best premium** : Claude Opus 4.6 — quality 100/100, $25/M output
- Sweet spot : **$0,50 – $2,00/M tokens** [2]
- Gemini 3 Pro : frontier à $1,25/$10 — 5× moins cher qu'Opus

![bg right:35%](assets/infographics/price_vs_score_scatter.png)
<!-- PB: Scatter plot of price (x) vs quality score (y) with model labels -->

<!-- Speaker notes: L'IA la plus chère n'est pas forcément la meilleure pour votre cas d'usage. -->

<small>Sources : [1] [CostGoat](https://costgoat.com/compare/llm-api) · [2] [TLDL](https://www.tldl.io/resources/llm-api-pricing-2026)</small>

---

<!-- _class: compact -->

# 34 — Prix vs Arena Elo

- Arena Elo reflète la **préférence humaine réelle** [1]
- Top Elo (1 503) : Claude Opus 4.6 à $5/$25
- Elo comparable (1 500) : Gemini 3.1 Pro à $2/$12 — **2× moins cher** [2]
- DeepSeek V3.2 (Elo 1 361) à $0,27/$0,42 — **60× moins cher** qu'Opus
- Coût par point Elo : de **$0,003 à $0,05** selon le modèle

![bg right:35%](assets/infographics/price_vs_elo_scatter.png)
<!-- PB: Scatter plot of Elo rating (y) vs output price (x) with model bubbles -->

<!-- Speaker notes: La question n'est pas "quel est le meilleur ?" mais "quel est le meilleur pour mon budget ?" -->

<small>Sources : [1] [LM Arena](https://arena.ai/leaderboard) · [2] [Vertu](https://vertu.com/lifestyle/ai-model-leaderboard-2026-intelligence-speed-price-context-a-complete-ranking-guide/)</small>

---

<!-- _class: cols -->

# 35 — Trois stratégies de pricing

<div class="left">

**Budget (< $1/M)**
- DeepSeek V3.2, Gemini Flash
- Chatbots, classification — 90 % des cas

**Mid-tier ($1–5/M)**
- GPT-5, Gemini Pro, Claude Sonnet
- RAG, rédaction, analyse

</div>
<div class="right">

**Premium ($5–75/M)**
- Claude Opus, GPT-5.2 Pro
- Juridique, médical, code critique

> **Règle des 90/10** : 90 % sur budget, 10 % critiques sur premium.

</div>

---

# 36 — Optimisation des coûts

- **Prompt Caching** : stocker les prompts système — jusqu'à **-90 %** sur l'input [1]
  - DeepSeek cache hit : $0,028/M au lieu de $0,28/M (10x moins cher)
- **Batch Processing** : API batch d'OpenAI → **-50 %** sur les tâches non temps réel [2]
- **Model Routing** : diriger les requêtes simples vers un modèle léger, les complexes vers le premium
- **Output Limits** : fixer `max_tokens` pour éviter les réponses trop longues
- **Coûts cachés** : le modèle API = seulement **10-17 %** du coût total IA [3]
  - Infrastructure, observabilité, équipe, embedding, stockage = 83-90 %

<small>Sources : [1] [DeepSeek API](https://api-docs.deepseek.com/) · [2] [OpenAI Batch API](https://platform.openai.com/docs/guides/batch) · [3] [Inkeep](https://inkeep.com/blog/50-000-llm-calls-cost-less-than-you-think-a-2026-pricing-rea)</small>

---

# 37 — Discussion : budget 500 €/mois, 3 cas d'usage

- **Scénario** : votre startup a un budget IA de **500 €/mois** pour 3 services :
  - **Chatbot client** : 100K requêtes/mois, réponses courtes
  - **Résumé de contrats** : 500 docs/mois, 50K tokens chacun
  - **Analyse de code** : 200 reviews/mois, qualité critique

> **Questions** :
> 1. Comment répartiriez-vous le budget entre les 3 services ?
> 2. Quel modèle pour chaque service ? (Budget/Mid/Premium)
> 3. Quelles optimisations (caching, routing) appliqueriez-vous ?

---

<!-- _class: section -->

# Pièges de la Méta-Évaluation

## Quand les benchmarks mentent

---

<!-- _class: compact -->

# 38 — Contamination : quand le modèle a vu l'examen

- **Contamination** = modèle entraîné sur les données du benchmark [1]
- Analogie : un étudiant avec le sujet du BAC **avant l'épreuve**
- Meta a admis avoir "ajusté" les résultats de Llama 4 [2]
- "Leaderboard Illusion" : soumissions sélectives par Meta, OpenAI, Google [2]
- Benchmarks **publics** (MMLU, GSM8K) sont les plus vulnérables
- Solution : benchmarks **dynamiques** à questions renouvelées

![bg right:35%](assets/infographics/contamination-teaching-test_run_20260301_174654_1f9a7c.png)
<!-- PB: Training data leaking into benchmark test set through a sieve -->

<small>Sources : [1] [AntiLeak-Bench](https://www.emergentmind.com/topics/antileak-bench) · [2] [The Multivac](https://open.substack.com/pub/themultivac/p/every-ai-benchmark-is-rigged-9-frontier)</small>

---

# 39 — Saturation : quand le test est trop facile

- Le Stanford HAI AI Index 2025 constate que les benchmarks classiques sont **saturés** [1]
- **Benchmarks saturés** : MMLU, GSM8K, HumanEval, HellaSwag (scores > 95 %)
- En 2023, MMMU, GPQA et SWE-bench ont été introduits comme tests plus durs [1]
- Un an après, les scores ont bondi : +18,8 (MMMU), +48,9 (GPQA), +67,3 pp (SWE-bench) [1]
- La course benchmarks ↔ modèles s'accélère : "Je continue de penser que ça va plafonner... mais ce n'est pas le cas" — Yolanda Gil, Stanford [2]
- Le coût d'un modèle de niveau GPT-3.5 a baissé de **280x** entre nov. 2022 et oct. 2024 [1]

<small>Sources : [1] [Stanford HAI 2025](https://hai.stanford.edu/ai-index/2025-ai-index-report) · [2] [IEEE Spectrum](https://spectrum.ieee.org/ai-index-2025)</small>

---

<!-- _class: cols -->

# 40 — Benchmarks statiques vs dynamiques

<div class="left">

**Statiques** (MMLU, GSM8K)

- Questions **fixes** et publiques
- Reproductibles et comparables
- Risque de mémorisation, saturent vite

</div>
<div class="right">

**Dynamiques** (LiveCodeBench, Arena)

- Questions **renouvelées** régulièrement
- Résistants à la contamination
- Plus représentatifs du réel

> L'avenir : vos propres tests, sur vos propres données.

</div>

---

# 41 — Le vrai test : vos propres données

- Aucun benchmark public ne remplace un **test sur votre cas d'usage**
- **Protocole recommandé** :
  1. Constituer un **golden set** de 100-500 exemples annotés par vos experts
  2. Tester 3-5 modèles candidats dans les **mêmes conditions**
  3. Mesurer les métriques **pertinentes pour votre business** (pas MMLU)
  4. Inclure des cas **adversariaux** (edge cases, données bruitées)
  5. Évaluer le **coût total** (API + infra + latence + maintenance)
- Les entreprises qui déploient avec succès testent **en continu** (A/B testing en prod)

> Un modèle #1 sur MMLU peut être #5 sur **vos factures** ou **votre domaine juridique**.

---

# 42 — Discussion : faut-il faire confiance aux benchmarks ?

- **Scénario** : vous êtes CTO d'une scale-up et vous devez choisir un LLM
- Le CEO a lu un article : "Gemini 3.1 Pro est #1 sur GPQA Diamond !"
- Votre équipe a testé 3 modèles sur vos données internes → résultats différents du leaderboard

> **Questions** :
> 1. Comment expliquer au CEO que les benchmarks publics ≠ performance réelle ?
> 2. Quels arguments pour justifier un budget de test interne ?
> 3. Contamination, saturation, sélection : quels sont les 3 biais majeurs ?

---

<!-- _class: section -->

# Synthèse

## Évaluer un LLM : la méthode en 5 questions

---

<!-- _class: compact -->

# 43 — Framework d'évaluation en 5 questions

1. **Quelle tâche ?** → Benchmarks pertinents (BLEU, MMLU, SWE-bench…)
2. **Quel niveau de qualité ?** → Frontier vs mid-tier vs budget
3. **Quel budget ?** → Model routing par criticité
4. **Quels risques ?** → Contamination, saturation, domain gap
5. **Mes propres données ?** → Golden set + A/B testing en prod

![bg right:35%](assets/infographics/llm-decision-flowchart_run_20260301_174657_9c7994.png)
<!-- PB: Decision tree with 5 questions branching to evaluation strategies -->

---

# 44 — Key Takeaways

- **Les métriques de génération** (BLEU, ROUGE, BERTScore) mesurent la qualité du texte, pas l'intelligence
- **Les benchmarks** sont des examens standardisés — utiles mais **imparfaits**
- **Le paradoxe BLEU** : un meilleur modèle peut avoir un score BLEU plus bas
- **La déflation des prix** : -50x/an en médiane, l'IA premium d'hier est le budget d'aujourd'hui
- **La saturation** touche MMLU, GSM8K, HumanEval → les nouveaux tests (HLE, FrontierMath) résistent

> **Le vrai test** : vos propres données, votre propre cas d'usage, votre propre budget.

---

# 45 — Ressources pour aller plus loin

| Ressource | URL | Usage |
|---|---|---|
| **Chatbot Arena** | arena.ai/leaderboard | Classement Elo par vote humain |
| **Artificial Analysis** | artificialanalysis.ai | Prix, vitesse, benchmarks comparés |
| **HF Open LLM Leaderboard** | huggingface.co/spaces/open-llm-leaderboard | Modèles open-source |
| **Stanford HAI AI Index** | hai.stanford.edu/ai-index | Rapport annuel complet |
| **Epoch AI** | epoch.ai/data-insights | Tendances prix et compute |
| **CostGoat** | costgoat.com/compare/llm-api | Calculateur de coûts API |

> Tous ces outils sont **gratuits** et mis à jour régulièrement. Bookmarkez-les.
