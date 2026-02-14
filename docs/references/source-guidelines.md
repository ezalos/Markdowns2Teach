# Guide des sources et citations

<!-- ABOUTME: Standards de sélection des sources et de citation pour les slides du cours. -->
<!-- ABOUTME: Classification des claims, hiérarchie d'autorité, format de citation et protocole de recherche. -->

## Classification des claims

### Nécessite une source (`[1]` + `<small>Sources</small>`)

- Tout **chiffre** : montants en dollars, pourcentages, taux de croissance, tailles de marché, effectifs
- Toute **statistique nommée** : "X% des entreprises font Y"
- Tout **fait spécifique à une entreprise** : chiffre d'affaires, valorisation, levée de fonds, nombre d'utilisateurs
- Tout **résultat de benchmark** : scores de précision, taux d'erreur, comparaisons de performance
- Toute **donnée de pricing** : coûts API, tarifs d'abonnement, fourchettes de prix
- Toute **prédiction/prévision** : "le marché atteindra $X en 2030"

### Ne nécessite PAS de source

- **Déductions logiques** : raisonnements, pas de claims factuels
- **Définitions** : explications de concepts niveau manuel
- **Cadrage pédagogique** : métaphores, analogies d'enseignement
- **Descriptions d'outils** (sans statistiques) : ce qu'un outil fait, pas combien d'utilisateurs il a
- **Questions de discussion** : pas de claim factuel

### Zone grise — résoudre vers le sourçage

- "Andrew Ng dit X" → Trouver d'où Ng tire l'info. Citer la source amont, pas Ng.
- "Il est bien connu que..." → S'il y a un chiffre, sourcer.
- "Estimations sectorielles" ou "Estimations développeurs" → **Pas des vraies sources**. Remplacer par un vrai rapport/enquête ou adoucir le langage.

## Hiérarchie d'autorité des sources

| Rang | Type de source | Exemples |
|------|---------------|----------|
| 1 | **IR d'entreprise / SEC filings** | Rapports annuels, documents investors — chiffres audités |
| 2 | **Publications peer-reviewed** | arXiv, NeurIPS, ICML — benchmarks et claims techniques |
| 3 | **Recherche Tier-1** | Gartner, McKinsey, Stanford HAI, OECD — données marché/adoption |
| 4 | **Presse Tier-1** | Bloomberg, Reuters, CNBC, Financial Times — news/funding/events |
| 5 | **Presse Tier-2** | TechCrunch, The Verge, Ars Technica — quand Tier-1 indisponible |
| 6 | **Bases de données startups** | Crunchbase, Sacra, PitchBook — valorisations/funding sans couverture presse |

## Filtre de récence

| Règle | Détail |
|-------|--------|
| **Rejet dur** | Source > 2 ans pour tout claim sur le marché/adoption IA |
| **Exception** | Faits historiques (AlexNet 2012, Flash Crash 2010) et jurisprudence |
| **Préférence** | Source < 6 mois quand disponible |
| **Conflit** | Le plus récent gagne, sauf si la source plus ancienne est nettement plus autoritaire |

## Format de citation

### Marqueurs in-text

Superscript-style `[1]`, `[2]` placés directement après chaque claim chiffré.

### Footer de slide

```markdown
<small>Sources : [1] [Gartner](https://www.gartner.com/...) · [2] [McKinsey](https://www.mckinsey.com/...)</small>
```

| Élément | Convention |
|---------|------------|
| Texte affiché | Nom court de l'autorité (ex : "Stanford HAI", "Gartner") |
| Lien | URL complète |
| Séparateur | ` · ` (point médian) |
| Correspondance | Les `[N]` in-text correspondent aux `[N]` du footer |
| Position | Une seule ligne `<small>Sources</small>` par slide, en bas |

### Exemple complet

```markdown
- Le marché atteint **$2 527 Mds** en 2026 [1]
- L'adoption passe de 55% à **88%** en deux ans [2]

<small>Sources : [1] [Gartner](https://www.gartner.com/...) · [2] [McKinsey](https://www.mckinsey.com/...)</small>
```

### Impact sur le budget de lignes

La ligne de sources coûte ~1 ligne de contenu. Budgeter **~13 lignes effectives** par slide standard (seuil linter = 15). Pour les slides `cols` : **~8–9 lignes** de contenu réel par colonne + 1 ligne de source.

Les slides de discussion et séparateurs de section peuvent omettre les citations s'il n'y a pas de claim factuel.

## Protocole de recherche par type de claim

| Type de claim | Sources primaires | Stratégie de recherche |
|--------------|-------------------|----------------------|
| Taille de marché / prévision | Gartner, IDC, Statista, McKinsey, CB Insights | `"[sujet] market size 2025" site:gartner.com OR site:statista.com` |
| Financiers d'entreprise | Pages IR, SEC filings, Bloomberg | `"[entreprise] revenue 2024" site:investor.[entreprise].com` |
| Stats d'adoption / enquêtes | McKinsey, Deloitte, Stanford HAI AI Index | `"[stat]" survey 2024 2025` |
| Résultats de benchmarks | Papiers originaux (arXiv), HuggingFace, WizWand | `"[modèle] [benchmark]" site:arxiv.org` |
| Pricing API | Pages pricing des fournisseurs directement | Aller sur openai.com/pricing, anthropic.com/pricing, etc. |
| Événements historiques | Reuters, Bloomberg, NYT, archives judiciaires | `"[événement]" [année] site:reuters.com OR site:nytimes.com` |
| Régulation EU | EUR-Lex, Parlement Européen, CEPS | `"EU AI Act" [disposition spécifique]` |

## Vérification

Utiliser Tavily extract pour lire la page réelle et confirmer que le chiffre correspond. Ne pas se fier aux snippets de recherche.

## Claims non sourçables

Si un claim ne peut pas être sourcé après un effort de recherche raisonnable :

| Action | Quand |
|--------|-------|
| **Adoucir** | Remplacer le chiffre exact par "environ", "de l'ordre de", "plusieurs" |
| **Retirer** | Supprimer la stat spécifique si la slide fonctionne sans |
| **Signaler** | Marquer avec `<!-- TODO: source needed for [claim] -->` pour décision |
| **Jamais** | Inventer une source ou citer une source secondaire qui ne contient pas la donnée réelle |

## Résolution de conflits

Quand les sources se contredisent, préférer la donnée la plus récente provenant de la source la plus réputée :

**company IR > Bloomberg/CNBC > TechCrunch > Crunchbase**

Si une source contredit le chiffre dans la slide, mettre à jour la slide pour correspondre à la meilleure source.
