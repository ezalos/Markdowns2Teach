---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML — Session 3 · M2 Entrepreneuriat Sorbonne"
footer: "Sources multiples · Kevin Vu / Dauphine · Données publiques"
---

<!-- ABOUTME: Évaluer une solution IA — métriques business, architecture decision matrix, benchmarks, Build vs Buy, no-code. -->
<!-- ABOUTME: Première moitié de la Session 3, cadré pour entrepreneurs M2 non-ingénieurs. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Cadrer un projet IA

## Session 3A — Évaluer une solution IA

M2 Entrepreneuriat · Sorbonne · 2026

---

<!-- _class: section -->

# Les métriques IA vues par le business

## Quand votre modèle se trompe, combien ça coûte ?

---

# 01 — Pourquoi les métriques comptent pour vous

- Un prestataire annonce "95% de précision" — est-ce suffisant pour décider ?
- Les KPIs permettent de :
  - **Comparer** des solutions concurrentes (build vs. buy)
  - **Fixer des seuils** d'acceptabilité avant mise en production
  - **Communiquer** la performance à vos investisseurs
- **Unsupervised Learning** : KPIs mesurent la qualité de l'algorithme (rarement liés au produit)
- **Supervised Learning** : KPIs standardisés selon le type de problème

> **Question pour la classe** : vous achetez un outil de détection de fraude. Le vendeur annonce "95% de précision". Est-ce suffisant pour prendre une décision ?

---

<!-- _class: cols -->

# 02 — La Confusion Matrix : le tableau de bord de votre IA

<div class="left">

### Cas binaire (oui / non)

Un modèle de Classification binaire se trompe de **deux manières** :

|  | Prédit Positif | Prédit Négatif |
|---|---|---|
| **Réel Positif** | True Positive (TP) | False Negative (FN) |
| **Réel Négatif** | False Positive (FP) | True Negative (TN) |

</div>
<div class="right">

### Coût business de chaque erreur

| Erreur | Exemple | Coût |
|---|---|---|
| **FP** | Bloquer une transaction légitime | Frustration client |
| **FN** | Laisser passer une fraude | Perte financière |

> Pensez au pêcheur de thon : **FP** = attraper un dauphin, **FN** = rater un thon.

> Le choix entre minimiser les FP ou les FN est une **décision business**, pas technique.

</div>

---

# 03 — Precision, Recall, F1-Score

| Métrique | Formule | Question business |
|---|---|---|
| **Accuracy** | (TP + TN) / Total | Quel % de prédictions sont correctes ? |
| **Precision** | TP / (TP + FP) | Parmi mes alertes, combien sont vraies ? |
| **Recall** (Sensitivity) | TP / (TP + FN) | Parmi les vrais cas, combien ai-je détectés ? |
| **F1-Score** | 2 x (P x R) / (P + R) | Compromis entre Precision et Recall |
| **Balanced Accuracy** | (TPR + TNR) / 2 | Quelle performance sur classes déséquilibrées ? |

> **Piège classique** : l'Accuracy seule est trompeuse. Si 99% de vos transactions sont légitimes, un modèle qui dit toujours "légitime" a 99% d'Accuracy mais **0% de Recall** sur la fraude.

---

<!-- _class: cols -->

# 04 — Quel KPI choisir ? Ça dépend de votre business

<div class="left">

### Priorisez la Precision quand...

- Les fausses alertes coûtent cher
- Ex : email marketing (trop de spam = désabonnement)
- Ex : recommandation produit (suggestion absurde = perte de crédibilité)

### Priorisez le Recall quand...

- Les cas manqués sont critiques
- Ex : détection de fraude (FN = perte financière)
- Ex : diagnostic médical (FN = risque vital)

</div>
<div class="right">

| Secteur | KPI prioritaire | Pourquoi |
|---|---|---|
| Fraude bancaire | **Recall** | Manquer une fraude coûte cher |
| Spam email | **Precision** | Bloquer un vrai mail = perte client |
| Diagnostic cancer | **Recall** | Manquer un cas = risque vital |
| Chatbot urgences | **Recall** | Ignorer une urgence est grave |

</div>

---

# 05 — Le Decision Threshold : un curseur business

- Un modèle de Classification ne prédit pas "oui/non" — il calcule une **probabilité** (0 à 1)
- Le **Decision Threshold** transforme cette probabilité en décision :
  - Seuil = 0.5 : standard
  - Seuil = 0.3 : plus sensible (+ Recall, - Precision)
  - Seuil = 0.8 : plus strict (+ Precision, - Recall)

> **Exemple** : votre startup de crédit en ligne. Un seuil bas approuve plus de clients (+ revenu) mais augmente le risque de défaut. Un seuil haut est prudent mais rejette des bons clients.

**Question pour la classe** : qui devrait fixer le seuil dans une startup — le CTO ou le CEO ? Pourquoi ?

---

<!-- _class: cols -->

# 06 — ROC Curve et AUC : comparer des prestataires

<div class="left">

### L'outil de benchmark

- La **ROC Curve** trace le Recall vs. le False Positive Rate pour chaque seuil
- L'**AUC** (Area Under the Curve) résume la performance en un chiffre (0 à 1)
  - AUC = 0.5 : modèle aléatoire (inutile)
  - AUC = 0.8 : bon modèle
  - AUC = 1.0 : modèle parfait (suspect)

</div>
<div class="right">

### Usage concret

- Comparer deux prestataires d'IA sur un **même jeu de données**
- Évaluer le rapport qualité/prix entre solutions
- Identifier le seuil optimal pour **votre** tolérance au risque

> L'AUC est votre outil de benchmark. Exigez-le de chaque fournisseur.

</div>

---

# 07 — Métriques de Regression : MAE, MSE, RMSE

| Métrique | Formule intuitive | Question business |
|---|---|---|
| **MAE** | Erreur moyenne absolue | En moyenne, de combien mon modèle se trompe ? |
| **MSE** | Erreur quadratique moyenne | Les grosses erreurs sont-elles fréquentes ? |
| **RMSE** | Racine de MSE | Erreur "typique" dans les mêmes unités que la donnée |

**Exemple** : prédiction de prix immobilier
- MAE = 15 000 € → en moyenne, l'estimation est à ±15K du prix réel
- RMSE = 25 000 € → les grosses erreurs (outliers) tirent la moyenne vers le haut

> **Règle** : MAE pour communiquer simplement, RMSE pour pénaliser les grosses erreurs. Si MAE ≈ RMSE, peu d'outliers.

---

<!-- _class: section -->

# Choisir la bonne architecture

## Decision Matrix, Transfer Learning, Explainability

---

<!-- _class: cols -->

# 08 — Quelle architecture pour quel problème ?

<div class="left">

| Architecture | Spécialité | Points forts |
|---|---|---|
| **MLP** | Données tabulaires | Simple, rapide |
| **CNN** | Images, vidéo | Détection de patterns visuels |
| **RNN / LSTM** | Séquences, texte | Mémoire temporelle |
| **Transformer** | Multi-modal | Très polyvalent |

</div>
<div class="right">

### Pour l'entrepreneur

Vous n'avez pas besoin de choisir l'architecture vous-même. Mais comprendre les forces de chacune vous aide à **évaluer les solutions proposées**.

> Si un prestataire propose un CNN pour analyser du texte, posez des questions.

</div>

---

# 09 — Transfer Learning : la stratégie startup

### Le principe

- Un modèle entraîné sur des millions d'images sait déjà "voir"
- Vous n'avez pas besoin de repartir de zéro
- Il suffit d'**ajuster les dernières couches** à votre problème spécifique

| Étape | Action | Coût |
|---|---|---|
| **Modèle de base** | ResNet pré-entraîné sur ImageNet | Gratuit (open source) |
| **Fine-tuning** | Réentraîner sur 500 images de vos produits | Quelques heures de GPU |
| **Déploiement** | API pour classifier vos images | Quelques EUR/mois |

> **90%** des applications business en 2026 utilisent des modèles pré-entraînés ajustés, pas des modèles construits de zéro [1].

<small>Sources : [1] [Gartner](https://www.gartner.com/en/articles/what-s-new-in-artificial-intelligence-from-the-2023-gartner-hype-cycle)</small>

---

# 10 — Explainability : quand la boîte noire pose problème

- Un Neural Network profond a **des millions de paramètres**
- Impossible d'expliquer simplement **pourquoi** il a pris une décision

| Domaine | Enjeu |
|---|---|
| **Banque** | Refuser un crédit sans explication = illégal (RGPD Art. 22) |
| **Santé** | Un diagnostic doit être justifiable |
| **Justice** | Un score de récidive doit être auditable |
| **Assurance** | Un refus de couverture doit être motivé |

> **EU AI Act** : les systèmes à haut risque doivent fournir des explications compréhensibles. L'Explainability n'est plus optionnelle [1].

<small>Sources : [1] [EU AI Act](https://artificialintelligenceact.eu/)</small>

---

# 11 — Matrice de décision pour votre projet

| Question | Si oui... | Si non... |
|---|---|---|
| Beaucoup de données étiquetées ? | Supervised Deep Learning | Transfer Learning ou APIs |
| Le problème concerne des images ? | CNN | Considérez d'autres architectures |
| Besoin d'Explainability ? | Modèles interprétables | Deep Learning viable |
| Budget GPU limité ? | Modèles pré-entraînés et APIs | Entraînez vos propres modèles |
| Domaine réglementé ? | Conformité EU AI Act dès J1 | Restez vigilant |

> **Règle d'or** : commencez par le plus simple qui fonctionne. Montez en complexité uniquement si nécessaire.

---

<!-- _class: section -->

# Benchmarks et leaderboards

## Lire, interpréter et ne pas se faire piéger

---

# 12 — Comment lire un benchmark IA

Les benchmarks sont partout en 2026 — mais tous ne se valent pas :

| Benchmark | Ce qu'il mesure | Fiabilité |
|---|---|---|
| **MMLU** | Connaissances générales (57 sujets) | Bonne, mais saturé |
| **HumanEval** | Génération de code | Bonne pour le code |
| **MT-Bench** | Qualité conversationnelle | Évaluée par GPT-4 |
| **Arena Elo** (LMSYS) | Préférence humaine | Meilleur indicateur [1] |

- Les modèles sont optimisés **pour** les benchmarks — attention au "teaching to the test"
- Un modèle #1 sur MMLU peut être médiocre sur **votre** tâche spécifique

> **Conseil** : testez toujours sur **vos propres données** avant d'acheter. Les benchmarks publics sont un point de départ, pas une garantie.

<small>Sources : [1] [LMSYS Chatbot Arena](https://chat.lmsys.org/)</small>

---

# 13 — Discussion : Décrypter les annonces marketing

> Un prestataire IA vous présente sa solution. Son pitch :
> "Notre modèle atteint **97% d'Accuracy** sur le benchmark standard et utilise du **Deep Learning de pointe**."

**Quelles questions posez-vous ?**

- Quel benchmark exactement ? Sur quelles données ?
- 97% d'Accuracy, mais quelle Precision/Recall sur **ma** classe critique ?
- Le modèle est-il explicable ? Compatible EU AI Act ?
- Avez-vous testé sur **mes** données (pas le benchmark) ?
- Quel Decision Threshold est utilisé ?
- Quelle est la performance sur les **edge cases** ?

> Les bons prestataires répondent sans hésiter. Les mauvais changent de sujet.

---

<!-- _class: section -->

# Build vs Buy

## Le framework de décision le plus important

---

# 14 — Les 5 approches d'implémentation

| Approche | Coût | Time-to-value | Contrôle |
|----------|------|--------------|----------|
| **Buy API** (GPT-4o, Claude) | EUR EUR | 1-2 semaines | Faible |
| **RAG** (API + vos données) | EUR EUR EUR | 2-6 semaines | Moyen |
| **Fine-tune** (QLoRA, PEFT) | EUR EUR EUR EUR | 4-12 semaines | Fort |
| **Build from scratch** | EUR EUR EUR EUR EUR | 6-18 mois | Total |
| **Agentic** (LLM + outils) | EUR EUR EUR | 4-8 semaines | Moyen |

- **57%** des organisations ne fine-tunent pas — Prompt Engineering + RAG suffit [1]
- **60%** des apps GenAI en production utilisent RAG plutôt que Fine-tuning [2]

<small>Sources : [1] [LangChain State of AI 2025](https://langchain.com/) · [2] [Deloitte](https://www.deloitte.com/)</small>

---

<!-- _class: cols -->

# 15 — Combien ça coûte vraiment ?

<div class="left">

| Approche | Coût initial | Coût mensuel |
|----------|-------------|-------------|
| **API GPT-4o** | ~0 EUR | $2,50-$10/M tokens |
| **API DeepSeek** | ~0 EUR | $0,28-$0,42/M tokens |
| **RAG** | 5-15K EUR | 50-8 000 EUR/mois |
| **Fine-tune QLoRA** | 100-5 000 EUR | ~500 EUR/mois |
| **Build from scratch** | >1M EUR | >10K EUR/mois |

</div>
<div class="right">

### Règles pratiques

- Si coûts API > **15K EUR/mois** : évaluez le self-hosting Mistral ou Llama [1]
- Les abonnements/licences = **< 40%** des dépenses réelles [2]
- **65%** des surcoûts imprévus viennent de l'infra et du talent

> Budgétez l'iceberg : Data Preparation, intégration, et Change Management sont les vrais postes.

</div>

<small>Sources : [1] [a16z](https://a16z.com/) · [2] [Gartner](https://www.gartner.com/)</small>

---

# 16 — Discussion : Build vs Buy pour une legaltech

> Vous construisez une startup **legaltech à Paris** qui analyse des contrats. Votre prototype utilise l'API Claude. Les clients (cabinets d'avocats) posent des questions sur la **confidentialité**.

| Option | Modèle | Hébergement | Coût 6 mois | Risque |
|--------|--------|------------|-------------|--------|
| A | API Claude | Cloud US | ~8K EUR | Cloud Act, vendor lock-in |
| B | Mistral Large (self-hosted) | OVHcloud | ~25K EUR | Infra à gérer |
| C | QLoRA Mistral 7B + RAG | Scaleway | ~18K EUR | Complexité technique |

**Questions pour la classe** :
- Quel critère pèse le plus : coût, performance, ou confiance client ?
- À partir de quel CA mensuel l'option B devient-elle rentable ?

---

<!-- _class: section -->

# Le paysage No-Code IA

## Construire sans coder — le superpower de l'entrepreneur

---

<!-- _class: cols -->

# 17 — No-code IA : 25 outils, 7 familles

<div class="left">

| Famille | Exemples | UE ? |
|---------|----------|:----:|
| Chatbot | GPT Builder, Mistral, Voiceflow | Mistral |
| Automatisation | Zapier, Make, n8n | n8n, Make |
| Contenu | Canva, Gamma, Runway | — |
| Vibe Coding | Bolt.new, Lovable, Replit | Lovable |
| Recherche | NotebookLM, Perplexity | — |
| Self-hosted | Ollama, Flowise | — |

</div>
<div class="right">

### Chiffres clés

- Marché low-code/no-code : **$65 Mds** (2024) [1]
- Bolt.new : de **$0 à $40M ARR** en 5 mois [2]
- Cursor : **$1 Mds ARR**, SaaS le plus rapide de l'histoire [3]
- **58%** des utilisateurs Replit ne sont **pas** développeurs [4]

> Tous ces outils ont un **free tier suffisant** pour démarrer.

</div>

<small>Sources : [1] [Gartner](https://www.gartner.com/) · [2] [Bloomberg](https://www.bloomberg.com/) · [3] [CNBC](https://www.cnbc.com/) · [4] [Replit](https://blog.replit.com/)</small>

---

# 18 — Grille de décision : quel outil pour quel besoin

| Besoin | Outil recommandé | Free | 1er résultat |
|--------|-----------------|:----:|:------------:|
| Chatbot client | Mistral / Dify | Oui | 1h |
| Automatisation | n8n / Make | Oui | 2h |
| Slides et pitch | Gamma / Canva | Oui | 10 min |
| Prototype web | Bolt.new / Lovable | Oui | 30 min |
| Recherche | NotebookLM / Perplexity | Oui | 5 min |
| Self-hosted | Ollama + Open WebUI | Oui | 30 min |

> Le budget n'est plus une excuse. Le **bottleneck** est l'idée, plus la technique.

---

# 19 — Key Takeaways

1. **Precision vs Recall est un choix business** — c'est vous qui définissez ce qui coûte le plus cher entre une fausse alerte et un cas manqué

2. **L'AUC est votre outil de benchmark** — exigez-le de chaque fournisseur, puis testez sur vos propres données

3. **Transfer Learning est la stratégie dominante** — 90% des apps business réutilisent des modèles pré-entraînés

4. **Buy d'abord, build ensuite** — 57% n'ont pas besoin de Fine-tuning, API + RAG couvre la majorité des use cases

5. **Les outils no-code sont gratuits** — de la recherche au prototype en passant par le chatbot, chaque famille a un free tier viable

> **Prochaine étape** : choisissez un use case et testez un outil no-code cet après-midi.
