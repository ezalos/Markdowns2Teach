---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 1 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Bloc C de la Session 1 — introduction aux outils techniques (JSON, API, HuggingFace, n8n), démo live Sentiment Analysis, et lancement du projet de groupe. -->
<!-- ABOUTME: Premier atelier pratique du cours, pont entre la théorie (S1-A/B) et le travail projet (S2-C, S3-C). -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Deep Tech & Machine Learning

## Session 1C — Votre premier projet IA

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# La boîte à outils du projet

## JSON, API, HuggingFace, n8n

---

# 01 — JSON : le langage des machines

Quand deux logiciels communiquent, ils échangent du **JSON** :

```json
{
  "label": "POSITIVE",
  "score": 0.9987
}
```

Les deux structures de base :
- **Objet** `{ }` — des paires clé/valeur : `"label": "POSITIVE"`
- **Tableau** `[ ]` — une liste ordonnée : `["POSITIVE", "NEGATIVE"]`

> Retenez : chaque résultat d'IA que vous recevrez sera du JSON. Savoir le lire, c'est savoir interpréter le résultat.

---

<!-- _class: cols -->

# 02 — API : commander un service à distance

<div class="left">

**L'analogie du restaurant** 🍽️

1. Vous (le client) passez une **requête**
2. Le serveur transmet à la cuisine
3. La cuisine prépare le plat
4. Vous recevez la **réponse**

Le menu = la **documentation** de l'API
Le serveur = le **endpoint** (URL)

</div>
<div class="right">

**Concrètement avec HuggingFace**

```
POST /models/distilbert-sst-2
Body: { "inputs": "I love this!" }
```

→ Réponse :
```json
[{ "label": "POSITIVE",
   "score": 0.9987 }]
```

Vous envoyez du texte, l'API renvoie une classification.

</div>

---

<!-- _class: cols -->

# 03 — Webhook : quand le service vous rappelle

<div class="left">

**API vs Webhook**

- **API** = *vous* appelez le service
  → "Serveur, apportez-moi le plat"
- **Webhook** = *le service* vous appelle
  → "Votre commande est prête !"

Un Webhook est une **URL que vous exposez**. Quand un événement se produit (message Telegram, paiement Stripe, push GitHub), le service envoie une requête HTTP à votre URL.

</div>
<div class="right">

**Concrètement avec n8n**

```
Telegram → message envoyé
        ↓
POST votre-webhook-n8n.com
  { "text": "Bonjour !" }
        ↓
n8n déclenche le workflow
```

- **Chat Trigger** = webhook intégré (chat n8n)
- **Webhook node** = URL publique pour services externes
- **Telegram Trigger** = webhook pré-configuré pour Telegram

</div>

> Les Webhooks sont le pont entre les services externes et vos workflows. Sans eux, il faudrait *vérifier en boucle* si quelque chose s'est passé (polling).

---

# 04 — HuggingFace : le GitHub de l'IA

La plus grande plateforme de modèles IA open-source : **1 M+ modèles** disponibles [1]

| Tâche | Modèle | Ce qu'il fait |
|-------|--------|---------------|
| Sentiment Analysis | `distilbert-sst-2` | Positif / Négatif |
| Content Moderation | `toxic-bert` | Détection de toxicité |
| Zero-shot Classification | `bart-large-mnli` | Catégories personnalisées |
| Spam Detection | `roberta-spam` | Spam / Légitime |

**Inference API** : envoyez du texte → recevez un résultat. Pas besoin de GPU ni d'installation.

> Vous allez utiliser cette API *aujourd'hui* pour construire votre premier système IA.

<small>Sources : [1] [HuggingFace](https://huggingface.co/models)</small>

---

# 05 — n8n : automatiser sans coder

![bg right:50% contain](assets/C/n8n-workflow-3nodes.png)

**n8n** = Workflow Automation : des **nodes** connectés par des flèches [1]

Chaque node fait *une seule chose* :
- **Chat Trigger** — reçoit un message
- **HTTP Request** — appelle une API
- **Set** — transforme les données

Notre instance : `http://77.134.130.112:1111`

> Pas de code, pas d'installation. Vous configurez visuellement, vous testez en un clic.

<small>Sources : [1] [n8n](https://n8n.io/)</small>

---

<!-- _class: cols -->

# 06 — Les 3 nodes de votre premier workflow

<div class="left">

**Node 1 : Chat Trigger**
Reçoit le message de l'utilisateur
→ `$json.chatInput`

**Node 2 : HTTP Request**
Envoie le texte à HuggingFace
→ Reçoit `[{label, score}]`

**Node 3 : Set (Format Response)**
Formate le résultat en texte lisible
→ `"POSITIVE: 99.9%"`

</div>
<div class="right">

**Flux de données**

```
"This product is great!"
        ↓
   Chat Trigger
        ↓
  { inputs: "This product
     is great!" }
        ↓
   HTTP Request → HuggingFace
        ↓
  [{ label: "POSITIVE",
     score: 0.9987 }]
        ↓
   Format Response
        ↓
  "POSITIVE: 99.9%"
```

</div>

---

<!-- _class: section -->

# Démo live : Sentiment Analysis

## Construisons ensemble un workflow en 3 nodes

---

# 07 — Étape 1 : créer le workflow

1. Ouvrez `http://77.134.130.112:1111` dans votre navigateur
2. Connectez-vous (identifiants fournis)
3. Cliquez sur **"Create new workflow"**
4. Nommez-le : `Sentiment - Equipe X`

Ensuite :
- Cliquez sur **"+"** pour ajouter un node
- Cherchez **"Chat Trigger"** → ajoutez-le
- Ce node crée une interface de chat intégrée

> Le Chat Trigger est votre point d'entrée. Chaque message tapé dans le chat devient une donnée JSON exploitable.

---

# 08 — Étape 2 : configurer le Chat Trigger

Le Chat Trigger ne nécessite **aucune configuration** :

- Il expose automatiquement `{{ $json.chatInput }}`
- Ce champ contient le texte que l'utilisateur tape dans le chat

**Ce qu'il faut savoir** :
- Le chat n8n est accessible via le bouton **"Chat"** en bas de l'éditeur
- En mode test, les messages restent locaux à votre workflow
- Chaque message génère une **exécution** visible dans l'historique

> On garde Telegram pour plus tard (Session 2). Aujourd'hui : chat intégré uniquement.

---

# 09 — Étape 3 : appeler l'API HuggingFace

Ajoutez un node **HTTP Request** et configurez-le :

| Champ | Valeur |
|-------|--------|
| **Method** | `POST` |
| **URL** | `https://router.huggingface.co/hf-inference/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english` |
| **Authentication** | Generic Credential → **Bearer Auth** |
| **Token** | Votre clé HuggingFace (`hf_...`) |
| **Body Type** | JSON |
| **JSON Body** | `{{ JSON.stringify({ inputs: $json.chatInput }) }}` |

> Pour obtenir votre token : [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) → **Create new token** → accès en lecture suffit.

---

<!-- _class: cols -->

# 10 — Étape 4 : formater la réponse

<div class="left">

Ajoutez un node **Set** :
- Mode : **Raw**
- JSON Output :

```javascript
{{ (() => {
  const results =
    $json[0] || $json;
  const lines =
    (Array.isArray(results)
      ? results : [results])
    .map(r =>
      `${r.label}: ${
        (r.score * 100)
        .toFixed(1)}%`)
    .join('\n');
  return JSON.stringify(
    { output: lines });
})() }}
```

</div>
<div class="right">

**Avant (brut de l'API)** :
```json
[[
  {"label": "POSITIVE",
   "score": 0.9987},
  {"label": "NEGATIVE",
   "score": 0.0013}
]]
```

**Après (formaté)** :
```
POSITIVE: 99.9%
NEGATIVE: 0.1%
```

Le champ `output` est ce que le chat affiche à l'utilisateur.

</div>

---

# 11 — Testez ! Envoyez vos messages

Cliquez sur **"Chat"** en bas de l'éditeur et essayez :

| Message | Résultat attendu |
|---------|-----------------|
| `This product is amazing!` | POSITIVE ~99% |
| `Terrible service, never again` | NEGATIVE ~99% |
| `The weather is okay I guess` | Plus nuancé (~60-70%) |
| `Ce produit est excellent !` | ? |

> **Question pour la classe** : Pourquoi le modèle est-il moins fiable en français ? Que faudrait-il changer pour un usage francophone ?

*Indice* : le modèle `distilbert-sst-2` a été entraîné sur des avis en **anglais** uniquement.

---

# 12 — Ce qu'on vient de construire

En 10 minutes, sans une seule ligne de code :

- ✅ Un **système de classification IA** fonctionnel
- ✅ Qui utilise un **modèle open-source** (HuggingFace)
- ✅ Accessible via une **interface chat**
- ✅ Sans GPU, sans installation, sans serveur à gérer

**Ce qui manque encore** :
- Un modèle adapté à votre cas d'usage
- Des données de test pour évaluer la qualité
- Une analyse honnête des limites

> C'est exactement ce que vous allez faire dans le **projet de groupe**.

---

<!-- _class: section -->

# Projet de groupe

## Classification IA — de l'idée au déploiement

---

# 13 — Le projet en une slide

**7 équipes de 4 étudiants** · 5 semaines (S1 → S5)

| Livrable | Description |
|----------|-------------|
| **Workflow n8n** | Système de classification fonctionnel |
| **Interface publique** | Accessible en ligne : site web (Lovable, bolt.new) ou bot Telegram |
| **Modèle OpenRouter** | Intégrer un modèle free-tier via OpenRouter pour formuler la réponse finale |
| **Jeu de test** | 20+ cas de test en JSON avec résultats attendus |
| **Présentation** | 5 min en Session 5 : démo live + analyse des résultats |

> Votre projet doit être **accessible publiquement** — l'enseignant testera chaque projet en live. Pas de démo locale : un vrai lien, un vrai bot.

---

# 14 — Exemples de projets

| # | Projet | Modèle HuggingFace | Cas d'usage |
|---|--------|-------------------|-------------|
| 1 | Sentiment Analysis | `distilbert-sst-2` | Avis clients e-commerce |
| 2 | Content Moderation | `toxic-bert` | Modération de commentaires |
| 3 | Product Category | `bart-large-mnli` | Catégorisation produits (zero-shot) |
| 6 | Intent Classification | `bart-large-mnli` | Routage support client |
| 8 | Email Spam | `roberta-spam` | Filtrage d'emails |

**10 projets pré-construits** avec workflow n8n fourni — ou proposez le vôtre !

> Chaque projet a un workflow n8n prêt à l'emploi. Vous pouvez l'importer et le modifier.

---

<!-- _class: cols -->

# 15 — Format du jeu de test

<div class="left">

```json
{
  "project": "Sentiment -
    Avis Clients",
  "team": "Équipe 3",
  "model": "distilbert-sst-2",
  "test_cases": [
    {
      "id": 1,
      "input": "This product
        is excellent!",
      "expected_label":
        "POSITIVE",
      "category":
        "clear_positive",
      "language": "en"
    }
  ]
}
```

</div>
<div class="right">

**Pourquoi un jeu de test ?**

- Mesurer la **précision** du modèle
- Identifier les **cas limites** (sarcasme, langues, ambiguïté)
- Documenter les **échecs** honnêtement

**Minimum 20 cas**, au moins 5 catégories :
- `clear_positive` / `clear_negative`
- `ambiguous`
- `sarcasm`
- `non_english`

> Un bon jeu de test vaut plus qu'un bon modèle. C'est lui qui révèle les vraies limites.

</div>

---

# 16 — Critères d'évaluation

| Critère | Poids | Ce qu'on évalue |
|---------|-------|-----------------|
| **Choix du modèle** | 25% | Justification du modèle vs alternatives |
| **Évaluation** | 25% | Qualité du jeu de test et des métriques |
| **Honnêteté** | 20% | Analyse franche des limites et erreurs |
| **Déploiement** | 15% | Le workflow fonctionne et est accessible |
| **Présentation** | 15% | Clarté, structure, réponse aux questions |

> **L'honnêteté compte autant que la performance.** Un modèle à 70% de précision bien analysé vaut mieux qu'un modèle à 95% sans recul critique.

---

# 17 — Planning et prochaines étapes

| Session | Étape | Objectif |
|---------|-------|----------|
| **S1** (aujourd'hui) | Lancement | Former les équipes, choisir le projet |
| **S2** | Construction | Workflow complet + intro évaluation IA |
| **S3** | Évaluation | Jeu de test finalisé + analyse des résultats |
| **S4** | **Soumission** | Affiner le workflow, **soumettre le projet final** |
| **S5** | **Revue collective** | Présentations 5 min + on parcourt les projets ensemble |

**Pour la prochaine session** :
- ✅ Former votre équipe de 4
- ✅ Créer un compte HuggingFace (un par équipe suffit)
- ✅ Choisir votre projet sur le Google Sheet

---

# 18 — Récapitulatif

**Ce qu'on a vu aujourd'hui** :

| Concept | En une phrase |
|---------|---------------|
| **JSON** | Le format universel d'échange entre logiciels |
| **API** | Un service distant qu'on appelle par URL |
| **HuggingFace** | 1M+ modèles IA accessibles via Inference API |
| **n8n** | Automatisation visuelle : des nodes, des flèches, zéro code |

**Ce qu'on a construit** : un système de Sentiment Analysis en 3 nodes

**Ce qui vient** : votre propre projet de classification, de l'idée au déploiement

---

# 19 — Inscrivez votre équipe !

**Google Sheet** : *(lien à projeter en cours)*

<!-- TODO: Louis — insérer le lien Google Sheet et le QR code -->

**Règles** :
- **4 personnes** par équipe (7 équipes max)
- **Pas de doublons** — un projet par équipe, premier arrivé premier servi
- Vous pouvez choisir parmi les 10 projets pré-construits **ou** proposer le vôtre
- Les projets personnalisés doivent être validés par l'enseignant

> Formez vos équipes et inscrivez-vous *avant de partir*. En Session 2, on construit !
