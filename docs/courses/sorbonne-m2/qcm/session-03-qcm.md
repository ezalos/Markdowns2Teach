<!-- ABOUTME: QCM d'évaluation pour la Session 3 — métriques IA, méthodologie projet, Build vs Buy. -->
<!-- ABOUTME: 15 questions à choix multiples avec réponses détaillées et explications en français. -->

# QCM — Session 3 : Cadrer un projet IA

## Métriques de Classification et Regression · Méthodologie projet · Build vs Buy

---

### Q1 — Confusion Matrix

Un modèle de détection de fraude analyse 1 000 transactions. Voici sa Confusion Matrix :

|  | Prédit Fraude | Prédit Légitime |
|---|---|---|
| **Réel Fraude** | 40 | 10 |
| **Réel Légitime** | 30 | 920 |

Combien de **False Positives** le modèle a-t-il produit ?

- A) 10
- B) 30
- C) 40
- D) 920

<details><summary>Réponse</summary>

**B) 30** — Un False Positive est une transaction **légitime** que le modèle a classée comme fraude. C'est la case "Réel Légitime × Prédit Fraude" = 30. Ces 30 clients légitimes ont été bloqués à tort.

</details>

---

### Q2 — Precision

Avec la même Confusion Matrix (Q1), quelle est la **Precision** du modèle ?

- A) 40 / 50 = 80%
- B) 40 / 70 = 57%
- C) 40 / 1000 = 4%
- D) 960 / 1000 = 96%

<details><summary>Réponse</summary>

**B) 40 / 70 = 57%** — La Precision = TP / (TP + FP) = 40 / (40 + 30) = 57%. Cela signifie que parmi les 70 alertes de fraude, seulement 57% étaient de vraies fraudes. Presque 1 alerte sur 2 est un faux positif.

</details>

---

### Q3 — Recall

Toujours avec la même Confusion Matrix (Q1), quel est le **Recall** du modèle ?

- A) 40 / 70 = 57%
- B) 40 / 50 = 80%
- C) 920 / 950 = 97%
- D) 40 / 1000 = 4%

<details><summary>Réponse</summary>

**B) 40 / 50 = 80%** — Le Recall = TP / (TP + FN) = 40 / (40 + 10) = 80%. Le modèle détecte 80% des fraudes réelles, mais en manque 10 sur 50 (20%).

</details>

---

### Q4 — Le piège de l'Accuracy

Un dataset de crédit contient **950 clients solvables** et **50 clients en défaut**. Un modèle prédit systématiquement "solvable" pour tout le monde. Quelle est son Accuracy ?

- A) 0%
- B) 50%
- C) 95%
- D) 100%

<details><summary>Réponse</summary>

**C) 95%** — Le modèle a raison 950 fois sur 1 000, soit 95% d'Accuracy. Mais il n'a détecté **aucun** défaut de paiement (Recall = 0%). C'est le piège classique : sur des classes déséquilibrées, l'Accuracy seule est trompeuse. Un investisseur qui voit "95% d'Accuracy" doit demander la Precision et le Recall par classe.

</details>

---

### Q5 — Choix de métrique : détection de fraude

Vous construisez un système de détection de fraude bancaire. Quelle métrique devez-vous **prioriser** ?

- A) Accuracy
- B) Precision
- C) Recall
- D) F1-Score

<details><summary>Réponse</summary>

**C) Recall** — En détection de fraude, manquer une vraie fraude (False Negative) coûte très cher : perte financière directe pour le client et la banque. Mieux vaut quelques fausses alertes (FP = frustration temporaire) que de laisser passer une fraude (FN = perte financière). On priorise donc le Recall pour maximiser la détection.

</details>

---

### Q6 — Choix de métrique : filtre anti-spam

Vous développez un filtre anti-spam pour une boîte email professionnelle. Quelle métrique devez-vous **prioriser** ?

- A) Accuracy
- B) Precision
- C) Recall
- D) AUC

<details><summary>Réponse</summary>

**B) Precision** — Si le filtre anti-spam bloque un email légitime (False Positive), l'utilisateur peut rater un contrat, une facture ou un message important. Le coût d'un FP est élevé. On priorise la Precision pour s'assurer que les emails classés "spam" sont vraiment du spam.

</details>

---

### Q7 — Decision Threshold

Un modèle de scoring crédit calcule une probabilité de défaut. Si vous **abaissez le Decision Threshold** de 0.5 à 0.3, qu'arrive-t-il ?

- A) Le Recall augmente et la Precision augmente
- B) Le Recall diminue et la Precision augmente
- C) Le Recall augmente et la Precision diminue
- D) Le Recall et la Precision restent identiques

<details><summary>Réponse</summary>

**C) Le Recall augmente et la Precision diminue** — En abaissant le seuil, le modèle classe plus de cas comme "positifs" (défaut). Il détecte donc plus de vrais cas de défaut (Recall ↑), mais en créant aussi plus de fausses alertes (Precision ↓). C'est le compromis fondamental Precision-Recall : le Decision Threshold est un curseur business, pas technique.

</details>

---

### Q8 — AUC

Un prestataire vous présente son modèle avec un **AUC de 0.52**. Que signifie ce chiffre ?

- A) Le modèle est excellent, presque parfait
- B) Le modèle est bon, au-dessus de la moyenne
- C) Le modèle est à peine mieux qu'un tirage aléatoire
- D) Le modèle est impossible à évaluer sans plus de données

<details><summary>Réponse</summary>

**C) Le modèle est à peine mieux qu'un tirage aléatoire** — Un AUC de 0.5 correspond à un modèle qui fait des prédictions aléatoires (pile ou face). Un AUC de 0.52 est marginalement meilleur que le hasard, donc inutile en production. Un bon modèle a typiquement un AUC > 0.8. Un AUC de 1.0 serait parfait (et suspect).

</details>

---

### Q9 — Balanced Accuracy

Un modèle de diagnostic médical a 98% d'Accuracy sur un dataset où 97% des patients sont sains. La **Balanced Accuracy** est de 55%. Quelle interprétation est correcte ?

- A) Le modèle est excellent — 98% d'Accuracy le prouve
- B) Le modèle est médiocre — il détecte mal la classe minoritaire (malades)
- C) La Balanced Accuracy est toujours inférieure à l'Accuracy, c'est normal
- D) Il faut ignorer la Balanced Accuracy car le dataset est déséquilibré

<details><summary>Réponse</summary>

**B) Le modèle est médiocre** — La Balanced Accuracy = (TPR + TNR) / 2 donne une performance moyenne pondérée sur les deux classes. À 55%, le modèle ne fait guère mieux que le hasard (50%) pour distinguer malades et sains. L'Accuracy de 98% est artificiellement gonflée par la classe majoritaire (sains). La Balanced Accuracy révèle la vérité : le modèle ne sait presque pas détecter les malades.

</details>

---

### Q10 — Benchmark marketing

Un prestataire annonce : "Notre modèle atteint **97% d'Accuracy** sur le benchmark standard." Quelle est la **première question** à poser ?

- A) Combien coûte votre licence ?
- B) Quel benchmark exactement, et quelle Precision/Recall sur ma classe critique ?
- C) Pouvez-vous améliorer à 99% ?
- D) Utilisez-vous du Deep Learning ?

<details><summary>Réponse</summary>

**B) Quel benchmark exactement, et quelle Precision/Recall sur ma classe critique ?** — "97% d'Accuracy" ne signifie rien sans contexte. Il faut savoir : quel dataset ? quelles classes ? quelle distribution ? Le modèle a-t-il été testé sur **vos** données ? Les bons prestataires répondent sans hésiter. Les mauvais changent de sujet.

</details>

---

### Q11 — MAE vs RMSE

Votre modèle de prédiction de prix immobilier affiche **MAE = 12 000 €** et **RMSE = 35 000 €**. Que pouvez-vous en déduire ?

- A) Le modèle est très bon car les erreurs sont faibles
- B) Le modèle a des outliers importants — quelques prédictions sont très éloignées du prix réel
- C) MAE et RMSE mesurent la même chose, la différence est un arrondi
- D) Le RMSE est toujours supérieur au MAE, c'est un artefact sans signification

<details><summary>Réponse</summary>

**B) Le modèle a des outliers importants** — Quand RMSE >> MAE, cela signifie que quelques erreurs sont très grandes. Le RMSE pénalise davantage les grosses erreurs (car il élève au carré avant de moyenner). Si MAE ≈ RMSE, les erreurs sont uniformément réparties. Ici, le RMSE est presque 3x le MAE, ce qui indique que certaines estimations sont très loin du prix réel (outliers).

</details>

---

### Q12 — Métriques de Regression

Vous présentez les performances de votre modèle de prédiction de stock à un investisseur non-technique. Quelle métrique est la **plus facile à communiquer** ?

- A) MSE (Mean Squared Error)
- B) RMSE (Root Mean Squared Error)
- C) MAE (Mean Absolute Error)
- D) R² (coefficient de détermination)

<details><summary>Réponse</summary>

**C) MAE (Mean Absolute Error)** — Le MAE s'exprime dans les mêmes unités que la donnée et représente l'erreur moyenne absolue. "En moyenne, notre prédiction se trompe de ±500 unités" est immédiatement compréhensible. Le MSE est en unités au carré (peu intuitif), le RMSE est mieux mais pénalise les outliers, et le R² est un ratio abstrait pour un non-technicien.

</details>

---

### Q13 — CRISP-DM

Dans la méthodologie **CRISP-DM**, quelle phase consomme typiquement **50 à 70%** de l'effort total d'un projet ?

- A) Business Understanding
- B) Modeling
- C) Data Preparation
- D) Deployment

<details><summary>Réponse</summary>

**C) Data Preparation** — La préparation des données (nettoyage, transformation, feature engineering) représente 50 à 70% de l'effort dans un projet data. C'est souvent sous-estimé par les entrepreneurs qui pensent que la valeur est dans le modèle. En réalité, "garbage in, garbage out" : la qualité des données détermine la qualité du résultat.

</details>

---

### Q14 — Build vs Buy

Votre startup veut lancer un chatbot client en 2 semaines. Vous avez 2 développeurs et 5 000 € de budget. Quelle approche est la plus adaptée ?

- A) Build from scratch avec un Transformer custom
- B) Fine-tuning QLoRA sur Mistral 7B
- C) API Claude ou GPT-4o avec Prompt Engineering
- D) Entraîner un modèle sur vos données depuis zéro

<details><summary>Réponse</summary>

**C) API Claude ou GPT-4o avec Prompt Engineering** — Avec 2 semaines et 5K€, la seule option réaliste est une API existante. Le coût initial est quasi nul, le time-to-value est de 1-2 semaines, et le Prompt Engineering suffit pour 57% des cas d'usage GenAI. Build from scratch prendrait 6-18 mois et >1M€. Le Fine-tuning nécessite 4-12 semaines et des compétences ML spécialisées.

</details>

---

### Q15 — No-code : quel outil pour quel besoin

Vous êtes entrepreneur et vous voulez créer un **prototype de site web** pour tester votre idée ce week-end, sans écrire de code. Quel outil choisir ?

- A) Ollama + Open WebUI
- B) n8n
- C) Bolt.new ou Lovable
- D) NotebookLM

<details><summary>Réponse</summary>

**C) Bolt.new ou Lovable** — Ce sont des outils de **Vibe Coding** qui permettent de créer un prototype web fonctionnel en 30 minutes sans écrire de code. Bolt.new est passé de $0 à $40M ARR en 5 mois. Lovable est un concurrent européen (Stockholm). Ollama est pour le self-hosting de modèles, n8n est pour l'automatisation de workflows, et NotebookLM est pour la recherche documentaire.

</details>
