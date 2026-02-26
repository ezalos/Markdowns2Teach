<!-- ABOUTME: Student-facing guide for using the shared n8n instance. -->
<!-- ABOUTME: Covers login, naming conventions, credentials, two approaches (HF vs OpenRouter), evaluation, free tiers, and troubleshooting. -->

# Guide n8n — Projet de Classification IA

## Connexion

- **URL** : `https://n8n.develle.fr`
- **Login** : email et mot de passe partagés (distribués en séance)
- Tous les groupes partagent la même instance — soyez respectueux

## Convention de nommage

Préfixez **tous** vos workflows avec votre numéro de groupe et le type :

```
GXX — Prod — Sentiment Analysis     (workflow principal)
GXX — Eval — Sentiment Analysis     (workflow d'évaluation)
GXX — TEST — mon expérience         (brouillons/tests)
```

- Format : `GXX — Type — Description` (XX = 01–10, tiret cadratin)
- Types : `Prod` (workflow final), `Eval` (évaluation), `TEST` (brouillons)
- **Ne modifiez ni ne supprimez jamais** les workflows d'un autre groupe
- Les workflows `TEACHER_EXAMPLE-*` sont des exemples pré-chargés — consultez-les mais ne les modifiez pas

## Deux approches possibles

Vous pouvez construire votre classification de deux manières :

### Approche 1 : Modèle HuggingFace (Inference API)

Vous envoyez du texte à un modèle spécialisé hébergé sur HuggingFace. Le modèle retourne directement un label et un score de confiance.

- **Exemple** : voir `TEACHER_EXAMPLE-Prod-HuggingFace`
- **Avantage** : rapide, spécialisé, pas de prompt à écrire
- **Limite** : le modèle fait une seule tâche (celle pour laquelle il a été entraîné)

### Approche 2 : LLM via OpenRouter (Structured Outputs)

Vous envoyez du texte à un LLM (comme Mistral) avec un prompt qui lui demande de classifier. Le LLM retourne une réponse structurée (JSON) avec le label et la confiance.

- **Exemple** : voir `TEACHER_EXAMPLE-Prod-OpenRouter`
- **Avantage** : flexible, fonctionne pour n'importe quel type de classification
- **Limite** : plus lent, dépend de la qualité du prompt

Les deux approches sont valides pour le projet. Choisissez celle qui correspond le mieux à votre cas d'usage.

## Gérer vos Credentials (clés API)

n8n stocke les credentials de façon chiffrée. Chaque groupe gère les siens.

### Ajouter un credential

1. Allez dans **Credentials** (barre latérale gauche)
2. Cliquez **Add Credential**
3. Choisissez le type (ex. "Telegram API", "HTTP Bearer Auth")
4. Nommez-le avec le préfixe de votre groupe : `G01 — Telegram Bot Token`
5. Collez votre clé et sauvegardez

### Credentials dont vous aurez besoin

| Service | Type dans n8n | Comment l'obtenir |
|---|---|---|
| Telegram Bot | Telegram API | Parlez à @BotFather sur Telegram |
| HuggingFace | HTTP Bearer Auth | huggingface.co/settings/tokens |
| OpenRouter | HTTP Bearer Auth | openrouter.ai/keys |

### Règles importantes

- **N'utilisez jamais** les credentials d'un autre groupe
- **Ne supprimez jamais** les credentials partagés ou pré-configurés
- Votre token Telegram est celui de **votre** groupe — créez votre propre bot via @BotFather

## Coûts et Free Tiers

**Vous ne devez rien dépenser pour ce projet.** Les deux plateformes offrent des niveaux gratuits suffisants :

### HuggingFace (Inference API)

- **Free tier** : crédits mensuels inclus pour les requêtes routées (suffisant pour les modèles de classification texte sur CPU)
- Créez un token sur [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) (accès en lecture suffit)
- Les modèles de text-classification et zero-shot-classification sont sur CPU → très économiques

### OpenRouter

- **Sans paiement** : 200 requêtes/jour sur les modèles gratuits (suffixe `:free`)
- **Avec un achat de $10 de crédits** : 1 000 requêtes/jour sur les modèles gratuits
- 30+ modèles gratuits disponibles, dont `mistralai/mistral-small-3.1-24b-instruct:free`
- Créez une clé sur [openrouter.ai/keys](https://openrouter.ai/keys)

> Pour le projet, le free tier sans paiement (200 req/jour) est largement suffisant pour développer et tester. Gardez les limites en tête pour l'évaluation : avec 20 cas de test, une évaluation = 20 requêtes.

## Ce que vous pouvez faire

- Créer des workflows avec : Telegram Trigger, HTTP Request, Chat Trigger,
  Code node (JS/Python basique), If/Switch/Set, nœuds LangChain
- Exécuter et tester vos workflows
- Utiliser l'interface de chat intégrée pour tester

## Ce qui est bloqué (sécurité)

- Les nœuds Execute Command, SSH, Git, Read/Write File
- L'installation de community packages
- L'import de modules dans le Code node (pas de `require()`, pas de `import`)

## Structure de workflow recommandée

Votre workflow de classification devrait suivre ce schéma :

1. **Trigger** — Message Telegram ou widget Chat
2. **Classification** — HTTP Request vers HuggingFace ou OpenRouter
3. **Post-traitement** — Code node pour formater le résultat
4. **Réponse** — Renvoyer le résultat à l'utilisateur (Telegram ou Chat)

Consultez les exemples pré-chargés pour voir la structure complète :
- `TEACHER_EXAMPLE-Prod-HuggingFace` — classification via modèle HuggingFace
- `TEACHER_EXAMPLE-Prod-OpenRouter` — classification via LLM avec structured outputs

## Évaluer votre modèle

**Vous devez tester au moins 2 modèles différents** sur votre dataset et justifier votre choix final.

Deux workflows d'évaluation sont pré-chargés comme exemples dans n8n :

- `TEACHER_EXAMPLE-Eval-HuggingFace` — évalue un modèle HuggingFace
- `TEACHER_EXAMPLE-Eval-OpenRouter` — évalue un modèle via OpenRouter (LLM)

### Comment ça marche

Le workflow d'évaluation envoie vos cas de test à l'API, compare les résultats attendus avec les prédictions du modèle, et calcule un score.

### Lancer une évaluation

1. Ouvrez un workflow `TEACHER_EXAMPLE-Eval-*` pour voir la structure
2. Cliquez **Execute Workflow** (le bouton play en haut)
3. Cliquez sur le nœud **Compute Score** pour voir le résultat
4. Le résultat affiche : `total`, `pass`, `fail`, `accuracy`, et un tableau `details` avec le détail par item

### Créer votre propre jeu de test

1. **Dupliquez** un workflow d'évaluation existant (clic droit sur le workflow dans la liste, puis Duplicate)
2. Renommez-le : `GXX — Eval — Description`
3. Ouvrez le nœud **Load Dataset** (Code)
4. Remplacez le tableau JSON par vos propres cas de test :
   ```javascript
   const dataset = [
     {input: "Votre texte ici", expected: "LABEL_ATTENDU"},
     {input: "Un autre texte", expected: "AUTRE_LABEL"},
     // ... 20 items minimum
   ];
   return dataset.map(item => ({json: item}));
   ```
5. Si vous avez changé de modèle : mettez à jour l'URL dans le nœud HTTP Request
6. Cliquez **Execute Workflow** puis lisez le score dans **Compute Score**

### Exigences pour le dataset

- **20 exemples minimum** (50 recommandé pour l'évaluation finale)
- **Du facile au difficile** : incluez des cas évidents ET des cas limites (ambigus, sarcasme, multilingue...)
- **Proche de la production** : vos exemples doivent ressembler aux données réelles que votre système rencontrerait
- **Équilibré** : nombre comparable d'exemples par catégorie
- **Testez au moins 2 modèles** : comparez les résultats et justifiez votre choix

## Dépannage

| Problème | Solution |
|---|---|
| "Node not found" | Certains nœuds sont désactivés pour la sécurité. Utilisez HTTP Request comme alternative universelle. |
| Erreur dans le Code node | Vous ne pouvez pas importer de modules. Utilisez uniquement du JS/Python natif. |
| Webhook ne fonctionne pas | Vérifiez que votre workflow est **Active** (toggle en haut à droite). |
| Quelqu'un a modifié mon workflow | Consultez le log d'exécution, prévenez l'enseignant. |
| Erreur 429 (rate limit) | Vous avez atteint la limite de requêtes. Attendez quelques minutes ou passez au lendemain. |
| Erreur 402 (billing) | Vous avez dépassé le free tier. Vérifiez votre consommation sur le dashboard du fournisseur. |
