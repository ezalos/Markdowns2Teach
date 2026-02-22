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

Notre instance : `https://7b97-77-134-130-112.ngrok-free.app`

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

1. Ouvrez `https://7b97-77-134-130-112.ngrok-free.app` dans votre navigateur
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

**7 équipes de 4 étudiants** · 5 semaines (S1 à S5) · **Présentation : 4 min**

| Livrable | Description |
|----------|-------------|
| **Workflow n8n** | Système de classification fonctionnel |
| **Interface publique** | Accessible en ligne (chat n8n, site web, ou bot Telegram) |
| **Dataset de test** | 20+ exemples, du facile au difficile, proches des données réelles |
| **Évaluation** | Au moins 2 modèles testés, résultats comparés, choix justifié |
| **Présentation** | 4 min en Session 5 : démo live + analyse des résultats |

Deux approches : **modèle HuggingFace** (Inference API) ou **LLM via OpenRouter** (Structured Outputs). Voir les exemples `TEACHER_EXAMPLE-Prod-*` sur n8n.

---

# 14 — Exemples de projets

| # | Projet | Cas d'usage |
|---|--------|-------------|
| 1 | Analyse de sentiment | Avis clients e-commerce (positif/négatif/neutre) |
| 2 | Modération de contenu | Détection de messages toxiques |
| 3 | Catégorisation produit | Trier des produits dans un catalogue |
| 4 | Classification audio | Identifier le type de contenu audio |
| 5 | Détection maladie plantes | Classifier des photos de feuilles |
| 6 | Routage support client | Diriger les demandes vers le bon service |
| 7 | Détection discours haineux | Repérer les messages discriminatoires |

Et aussi : détection de spam email, screening de CV, veille réseaux sociaux... ou **proposez le vôtre** !

---

<!-- _class: cols -->

# 15 — Votre dataset de test

<div class="left">

**Exigences**

- **20 exemples minimum**
- Du **facile au difficile** : cas évidents + cas limites
- **Proche de la prod** : données réalistes
- **Équilibré** : ~même nombre par catégorie

</div>
<div class="right">

**Exemple** : `[{"input": "...", "expected": "POSITIF"}, ...]`

Voir `TEACHER_EXAMPLE-Eval-*` sur n8n pour le format complet et le calcul automatique du score.

</div>

---

# 16 — Comparer les modèles

Vous devez **tester au moins 2 modèles différents** sur votre dataset :

| Approche | Exemple |
|----------|---------|
| **Modèle HuggingFace** | Modèle spécialisé via Inference API |
| **LLM via OpenRouter** | LLM avec Structured Outputs |
| **Variantes** | Deux modèles HF, ou deux LLMs, ou un mix |

Pour chaque modèle, relevez le **score sur votre dataset** et documentez :
- Où le modèle réussit bien, où il échoue
- Pourquoi vous choisissez le modèle final
- Ce qui pourrait être amélioré

> Un modèle à 70% bien analysé vaut mieux qu'un modèle à 95% sans recul critique.

---

<!-- _class: cols -->

# 17 — Évaluation : ce qui compte

<div class="left">

**Poids fort (la majorité des points)**

- La démo fonctionne en live
- Je peux interagir avec votre système en moins d'une minute
- Qualité du dataset et des tests
- Au moins 2 modèles comparés

</div>
<div class="right">

**Poids modéré**

- Présentation + démo tient en 4 min
- Produit expliqué clairement
- Choix du modèle justifié

**Poids faible** : esthétique, mise en forme

</div>

---

# 18 — Bonus possibles

Jusqu'à **2 bonus** parmi les suivants :

| Bonus | Description |
|-------|-------------|
| **Tests extensifs** | Comparaison détaillée de 10+ modèles avec rapport clair |
| **Interface web** | Un site (Lovable, bolt.new...) avec lequel je peux interagir |
| **Inputs complexes** | Traiter des images, vidéos, ou fichiers audio |
| **Base de données** | Système avec mémoire, corpus de données (type RAG) |

> Les bonus récompensent l'exploration et l'ambition. Mais un projet simple qui fonctionne bien vaut mieux qu'un projet ambitieux qui plante en démo.

---

# 19 — Coûts : tout est gratuit

**Vous ne devez rien dépenser pour ce projet.**

| Plateforme | Free Tier |
|------------|-----------|
| **HuggingFace** | Crédits mensuels inclus pour les modèles de classification (CPU) |
| **OpenRouter** | 200 requêtes/jour sur les modèles gratuits (suffixe `:free`) |
| **n8n** | Instance partagée fournie par l'enseignant |

> Avec 20 cas de test, une évaluation = 20 requêtes. Le free tier est largement suffisant pour développer, tester et évaluer.

---

# 20 — Apprendre à apprendre

Ce cours ne couvre **pas tout** ce dont vous aurez besoin — et c'est volontaire.

**Apprendre un outil spécifique < Apprendre à apprendre**

- Le guide n8n est volontairement minimal : cherchez en groupe comment faire ce que vous avez en tête
- Utilisez l'IA pour construire (ChatGPT, Claude, etc.) — mais vous êtes **responsables** de la qualité et devez **comprendre** ce qui est produit
- Dans la vraie vie professionnelle, personne ne vous donnera un tutoriel complet pour chaque outil

> La compétence la plus précieuse n'est pas de maîtriser n8n. C'est de savoir se débrouiller face à un outil nouveau, en équipe, avec les ressources disponibles.

---

# 21 — Planning et prochaines étapes

| Session | Étape | Objectif |
|---------|-------|----------|
| **S1** (aujourd'hui) | Lancement | Former les équipes, découvrir n8n |
| **S2** | Construction | Workflow complet + intro évaluation IA |
| **S3** | Évaluation | Dataset finalisé + analyse des résultats |
| **S4** | Soumission | Affiner, **soumettre le projet final** |
| **S5** | **Présentations** | 4 min par groupe + on parcourt les projets ensemble |

**Avant de partir aujourd'hui** : formez votre équipe de 4 sur le Google Sheet

**Avant vendredi 6 mars** : choisissez et décrivez votre projet sur le Google Sheet

---

# 22 — Inscrivez votre équipe !

**Google Sheet** : *(lien projeté en cours)*

<!-- TODO: Louis — insérer le lien Google Sheet et le QR code -->

**Aujourd'hui** :
- Formez votre équipe de **4 personnes** (7 équipes max)
- Inscrivez les noms sur le **Sheet 1** (Groupes)

**Avant vendredi 6 mars** :
- Choisissez votre projet sur le **Sheet 2** (Projets)
- Remplissez le titre et la description — premier arrivé, premier servi
- Les projets personnalisés doivent être validés par l'enseignant

> Le guide technique complet vous sera envoyé par email. En Session 2, on construit !
