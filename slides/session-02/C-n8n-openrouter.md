---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 2 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: Bloc C de la Session 2 — atelier pratique OpenRouter + Structured Output dans n8n pour le projet de classification. -->
<!-- ABOUTME: Suite de S1-C (HuggingFace), introduit l'approche LLM avec structured output. Hands-on en équipes. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 2C — Classification par LLM avec OpenRouter

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Rappel et contexte

## Où en est votre projet ?

---

# 01 — Point d'étape projet

En Session 1C, vous avez :
- Formé vos équipes (7 groupes de 4)
- Choisi un projet de classification parmi les 10 proposés
- Construit un premier workflow n8n avec **HuggingFace**

**Aujourd'hui** : découvrir la deuxième approche — classifier avec un **LLM** via OpenRouter.

> À la fin de cette séance, vous aurez **deux workflows fonctionnels** pour votre projet : un HuggingFace, un OpenRouter. Vous pourrez les comparer.

---

<!-- _class: cols -->

# 02 — Deux approches de classification

<div class="left">

**HuggingFace (S1-C)** :
- Modèle spécialisé (ex : `distilbert-sst-2`)
- Retourne un label + score directement
- Rapide, pas de prompt à écrire

</div>
<div class="right">

**LLM via OpenRouter (aujourd'hui)** :
- LLM généraliste (ex : Mistral Small)
- Prompt de classification + Structured Output
- Flexible, zero-shot, multilingue

</div>

> Les deux approches sont valides. L'objectif : **les tester et comparer** sur votre dataset.

---

# 03 — Pourquoi un LLM pour classifier ?

Quand un modèle spécialisé HuggingFace n'existe pas pour votre tâche, un LLM est la solution :

- **Zero-shot** — pas besoin de données d'entraînement, juste un bon prompt
- **Multilingue** — fonctionne en français, anglais, ou tout mélange
- **Flexible** — changez les catégories en modifiant le prompt, pas le modèle
- **Structured Output** — le LLM retourne du JSON garanti avec label + confidence + reasoning

**Quand préférer HuggingFace ?** : si un modèle spécialisé existe, il sera plus rapide et souvent plus précis sur sa tâche spécifique.

> En Session 2A, on a vu le Structured Output et le Field Ordering. Aujourd'hui, on les met en pratique dans n8n.

---

<!-- _class: section -->

# OpenRouter

## Un routeur universel de LLMs

---

# 04 — OpenRouter : accéder à 30+ modèles gratuits

**OpenRouter** est un routeur d'API : une seule URL, un seul format, accès à des centaines de modèles.

| Ce que vous envoyez | Ce qu'OpenRouter fait | Ce que vous recevez |
|---|---|---|
| Modèle choisi + messages | Route vers le bon fournisseur | Réponse du LLM au format standard |

**Modèle recommandé** (gratuit) : `mistralai/mistral-small-3.1-24b-instruct:free`

- Suffixe `:free` = pas de facturation
- Mistral Small : bon équilibre qualité/vitesse pour la classification
- Fonctionne en français nativement (Mistral AI, Paris)

> OpenRouter abstrait la complexité des providers : vous changez de modèle en changeant **une ligne**.

---

<!-- _class: cols -->

# 05 — Free Tier et limites

<div class="left">

**Sans paiement** :
- **50 requêtes/jour** sur les modèles `:free`
- Suffisant pour développer et tester
- 1 évaluation (20 tests) = 20 requêtes

</div>
<div class="right">

**Avec $10 de crédits** :
- **1 000 requêtes/jour** sur les modèles `:free`
- Accès aux modèles payants (GPT-4o, Claude)
- Non obligatoire pour le projet

</div>

> La limite de 50 req/jour est suffisante pour le développement. Planifiez vos évaluations (20 req chacune) en conséquence.

---

# 06 — Créer votre clé API OpenRouter

**Étapes** :

1. Allez sur [openrouter.ai/keys](https://openrouter.ai/keys)
2. Créez un compte (email ou GitHub)
3. Cliquez **Create Key** → copiez la clé (commence par `sk-or-...`)
4. Dans n8n : **Credentials** → **Add Credential** → **HTTP Bearer Auth**
5. Nommez : `G0X — OpenRouter API Key`
6. Collez votre clé dans le champ Bearer Token

> Chaque membre du groupe peut créer sa propre clé. Utilisez celle du groupe dans le workflow Prod.

---

<!-- _class: section -->

# Structured Output dans n8n

## Du prompt au JSON garanti

---

# 07 — Le prompt de classification

**System prompt** — qui vous êtes :
```
Tu es un classificateur de texte. Retourne ta réponse en JSON.
```

**User message** — le texte à classifier :
```
Texte : "J'adore ce produit !"
```

**Réponse attendue** (JSON) :
```json
{ "reasoning": "Sentiment positif exprimé",
  "confidence": 0.95, "label": "POSITIVE" }
```

> L'ordre des champs compte : `reasoning` **avant** `label` = le LLM réfléchit avant de répondre (cf. S2-A slide 32).

---

<!-- _class: cols -->

# 08 — Anatomie du body HTTP

<div class="left">

- `model` : `"mistralai/mistral-small-3.1-24b-instruct:free"`
- `messages` : tableau system + user
- `temperature` : 0 (déterministe)

</div>
<div class="right">

- La réponse arrive dans `choices[0].message.content`
- C'est une string — à parser avec `JSON.parse()`
- Testez d'abord sans `response_format`

</div>

> Le format est identique à l'API OpenAI — un avantage d'OpenRouter est cette compatibilité directe.

---

# 09 — Ajouter le champ confidence

En S2-A (slides 34-35), on a vu que le score de confiance verbalisé par un LLM est **approximatif** :

- Les scores se concentrent entre 80-100%, multiples de 5
- Ce n'est pas une probabilité calibrée — c'est une estimation

**En pratique pour votre projet** :
- Ajoutez `"confidence": 0.0-1.0` dans votre schema JSON
- Utilisez-le comme **indicateur relatif** (comparer les items entre eux)
- Ne le traitez pas comme une probabilité absolue
- Seuil recommandé : items avec confidence < 0.7 → vérification manuelle

> La confiance est utile pour **trier et prioriser**, pas pour garantir la précision.

---

<!-- _class: section -->

# Demo live dans n8n

## Construire le workflow pas à pas

---

# 10 — Architecture du workflow OpenRouter

Le workflow suit 4 étapes, comme pour HuggingFace :

| Nœud | Type | Rôle |
|---|---|---|
| **Chat Trigger** | Trigger | Reçoit le message utilisateur |
| **HTTP Request** | Action | Envoie le texte à OpenRouter |
| **Code** | Transformation | Parse le JSON, extrait label + confidence |
| **Respond** | Action | Renvoie le résultat à l'utilisateur |

Consultez `TEACHER_EXAMPLE-Prod-OpenRouter` dans n8n pour voir le workflow complet.

> La structure est identique à HuggingFace — seul le nœud HTTP Request change (URL, body, parsing).

---

<!-- _class: cols -->

# 11 — Configurer le nœud HTTP Request

<div class="left">

- **URL** : `https://openrouter.ai/api/v1/chat/completions`
- **Method** : POST
- **Auth** : HTTP Bearer (votre credential `G0X — OpenRouter...`)

</div>
<div class="right">

- `model` : votre modèle `:free`
- `messages` : system + user
- `temperature` : 0 (déterministe)
- Utilisez `{{ $json.chatInput }}` pour le texte

</div>

> Consultez `TEACHER_EXAMPLE-Prod-OpenRouter` pour voir la configuration complète.

---

# 12 — Le Code node : parser la réponse

Le LLM retourne sa réponse dans `choices[0].message.content` — une **string JSON** à parser :

```javascript
const content = $input.first().json
  .choices[0].message.content;
const parsed = JSON.parse(content);
return [{json: {
  label: parsed.label,
  confidence: parsed.confidence,
  reasoning: parsed.reasoning
}}];
```

> Si le LLM retourne du texte au lieu de JSON, ajoutez un `try/catch` et retournez `"ERROR"` comme label.

---

# 13 — Tester et itérer

**Workflow de test** :

1. Ouvrez votre workflow dans n8n
2. Cliquez **Execute Workflow** (bouton play)
3. Envoyez un message test via le Chat Trigger
4. Cliquez sur chaque nœud pour voir les données à chaque étape
5. Vérifiez : le JSON est-il bien parsé ? Le label est-il correct ?

**Itérer sur le prompt** :
- Trop de mauvaises classifications ? → Ajoutez des exemples dans le system prompt
- Labels incohérents ? → Listez explicitement les labels valides
- Confidence toujours à 0.95 ? → Ajoutez "Sois calibré, utilise toute l'échelle 0-1"

> Le prompt est votre principal levier de qualité. Modifiez-le, testez, mesurez, répétez.

---

<!-- _class: section -->

# À vous de jouer

## Implémenter et comparer

---

# 14 — Exercice : votre workflow OpenRouter

**Objectif** : créer un workflow de classification via OpenRouter pour votre projet.

**Étapes** :
1. Dupliquez `TEACHER_EXAMPLE-Prod-OpenRouter`
2. Renommez : `G0X — Prod — [Votre projet]`
3. Remplacez le credential par votre clé OpenRouter
4. Adaptez le system prompt à votre tâche de classification
5. Testez avec 5 exemples variés (faciles + difficiles)
6. Ajustez le prompt jusqu'à satisfaction

> Vous avez 20-25 minutes. Appelez l'enseignant si vous êtes bloqués.

---

<!-- _class: cols -->

# 15 — Checklist de validation

<div class="left">

- Workflow nommé `G0X — Prod — ...`
- Credential nommé `G0X — OpenRouter...`
- Réponse structurée : label + confidence
- Le Code node parse sans erreur

</div>
<div class="right">

- 5+ tests manuels passent
- Labels correspondent à vos catégories
- Confidence varie (pas toujours 0.95)
- Reasoning est cohérent

</div>

> Si tout est vert, activez le workflow (toggle en haut à droite).

---

# 16 — Préparer la comparaison

Pour la prochaine séance (Session 3 — Évaluation), vous devrez **comparer** vos deux approches :

| À préparer | HuggingFace | OpenRouter |
|---|---|---|
| **Workflow Prod** | `G0X — Prod — HF` | `G0X — Prod — OR` |
| **Workflow Eval** | `G0X — Eval — HF` | `G0X — Eval — OR` |
| **Dataset test** | ≥20 exemples avec labels attendus | Même dataset |

**Dupliquez** un workflow `TEACHER_EXAMPLE-Eval-*` et adaptez-le à votre modèle.

> L'évaluation sur le **même dataset** avec les **deux approches** est ce qui vous permettra de justifier votre choix final lors de la présentation.
