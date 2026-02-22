<!-- ABOUTME: Student-facing guide for using the shared n8n instance. -->
<!-- ABOUTME: Covers login, naming conventions, credentials, allowed/blocked nodes, and troubleshooting. -->

# Guide n8n — Projet de Classification IA

## Connexion

- **URL** : `[URL communiquée en cours]`
- **Login** : email et mot de passe partagés (distribués en séance)
- Tous les groupes partagent la même instance — soyez respectueux

## Convention de nommage

Préfixez **tous** vos workflows avec votre numéro de groupe :

```
G01 — Sentiment Analysis
G03 — Telegram Bot Classification
```

- Format : `GXX — Description` (XX = 01–10, tiret cadratin)
- **Ne modifiez ni ne supprimez jamais** les workflows d'un autre groupe
- Pour un workflow de test : `GXX — TEST — description`

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
| HuggingFace | HTTP Header Auth | huggingface.co/settings/tokens |
| Replicate | HTTP Bearer Auth | replicate.com/account/api-tokens |
| OpenRouter | HTTP Bearer Auth | openrouter.ai/keys |

### Règles importantes

- **N'utilisez jamais** les credentials d'un autre groupe
- **Ne supprimez jamais** les credentials partagés ou pré-configurés
- Votre token Telegram est celui de **votre** groupe — créez votre propre bot via @BotFather

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
2. **Classification** — HTTP Request vers un modèle HuggingFace
3. **Post-traitement** — Code node pour formater le résultat
4. **Réponse** — Renvoyer le résultat à l'utilisateur (Telegram ou Chat)

## Évaluer votre modèle

Des workflows d'évaluation sont pré-chargés dans n8n pour tester la précision de votre modèle sur un jeu de données de test.

### Comment ça marche

Le workflow d'évaluation envoie 20 cas de test à l'API HuggingFace, compare les résultats attendus avec les prédictions du modèle, et calcule un score de précision (accuracy).

### Lancer une évaluation

1. Ouvrez le workflow `Eval XX — Description` correspondant à votre projet
2. Cliquez **Execute Workflow** (le bouton ▶ en haut)
3. Cliquez sur le nœud **Compute Score** pour voir le résultat
4. Le résultat affiche : `total`, `pass`, `fail`, `accuracy`, et un tableau `details` avec le détail par item

### Créer votre propre jeu de test

1. **Dupliquez** un workflow d'évaluation existant (clic droit → Duplicate)
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
5. Si vous avez changé de modèle : mettez à jour l'URL dans le nœud **Call HuggingFace**
6. Pour les projets zero-shot : mettez à jour les `candidate_labels` dans le body JSON
7. Cliquez **Execute Workflow** → lisez le score dans **Compute Score**

### Conseils pour un bon dataset

- **Équilibré** : même nombre d'exemples par label
- **Varié** : mélangez des cas faciles et des cas limites (ambigus)
- **Réaliste** : utilisez des exemples proches de votre cas d'usage réel
- **20 items minimum**, 50 recommandé pour l'évaluation finale

## Dépannage

| Problème | Solution |
|---|---|
| "Node not found" | Certains nœuds sont désactivés pour la sécurité. Utilisez HTTP Request comme alternative universelle. |
| Erreur dans le Code node | Vous ne pouvez pas importer de modules. Utilisez uniquement du JS/Python natif. |
| Webhook ne fonctionne pas | Vérifiez que votre workflow est **Active** (toggle en haut à droite). |
| Quelqu'un a modifié mon workflow | Consultez le log d'exécution, prévenez l'enseignant. |
