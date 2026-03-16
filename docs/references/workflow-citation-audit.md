# Workflow : audit et remédiation des citations

<!-- ABOUTME: Plan systématique pour auditer et corriger les claims non sourcés dans les decks de slides. -->
<!-- ABOUTME: Couvre l'outillage, le backlog de remédiation, le processus par fichier et la parallélisation. -->

Les règles de citation (classification des claims, hiérarchie d'autorité, format, récence, vérification) sont centralisées dans **`slide-creation-standards.md` §6**. Ce workflow y fait référence sans les répéter.

---

## 1. Outillage

| Outil | Usage | Limite |
|-------|-------|--------|
| **Tavily Search** | Recherche web pour trouver des sources autoritaires | 1 000 crédits/mois |
| **Tavily Extract** | Extraire le contenu d'une URL pour vérifier les chiffres | 1 000 crédits/mois |
| **WebSearch** (built-in) | Recherche web de base | Illimité |
| **WebFetch** (built-in) | Récupération de page de base | Illimité |

## 2. Processus par claim

Pour chaque claim non sourcé :

1. **Classifier** le claim — voir `slide-creation-standards.md` §6.1
2. **Chercher** une source en suivant le protocole — voir `slide-creation-standards.md` §6.5
3. **Valider** la source selon la hiérarchie d'autorité — voir §6.2
4. **Vérifier la récence** — voir §6.3
5. **Confirmer le chiffre** en lisant la page réelle — voir §6.6
6. **Formater** la citation — voir §6.4
7. Si non sourçable, appliquer le protocole — voir §6.7

## 3. Backlog de remédiation

### Résumé de l'audit : 30 claims non cités + 1 citation informelle + 2 fausses sources

| Priorité | Fichier | Issues | Claims clés |
|----------|---------|:------:|-------------|
| P1 | `session-02/A-prompt-au-produit.md` | 5 | Tableau pricing API, "90% projects", "~7 mois", "~10x price drop" |
| P2 | `session-05/A-regulation-ethique.md` | 6 | Flash Crash $1T, Amazon recruiting, Meta RAI, Thomson Reuters v. Ross |
| P3 | `session-01/B-au-dela-des-llms.md` | 5+1 | ImageNet, AlexNet, CNN benchmarks, "(Gartner)" informel, SLM pricing |
| P4 | `session-03/D-methodologie-projet.md` | 4 | Fausse "Estimations sectorielles", CRISP-DM "400+ citations", "50-70%" |
| P5 | `session-04/A-ecosysteme-ia.md` | 3 | Fausse "Estimations développeurs" (CUDA 98%), parts de marché cloud, ASML |
| P6 | `session-04/B-business-models.md` | 3 | Tableau pricing API, OpenAI $57B funding, L'Oréal experts/brevets |
| P7 | `session-03/A-evaluer-solution-ia.md` | 2 | Tableau fourchettes de coûts, stat "65% surcoûts" |
| P8 | `session-02/B-ingenierie-ia.md` | 1 | Pricing modèles d'embedding |
| P9 | `session-01/A-genai-fondamentaux.md` | 1 | Claim "Supervised Learning most deployed" |

## 4. Processus par fichier

1. Un **subagent lit le fichier** et extrait tous les claims non cités avec numéros de ligne
2. Un **agent de recherche** applique le protocole de recherche (§2 ci-dessus)
3. **Tavily Extract** vérifie la page source réelle pour confirmer les chiffres
4. Si un claim ne peut pas être sourcé : adoucir le langage ou signaler pour Louis
5. L'agent **édite le fichier** : ajoute les marqueurs `[N]` et les footers `<small>Sources</small>`
6. Lancer `make check` + `make check-citations`

## 5. Parallélisation

- Les fichiers sont indépendants — traiter 2–3 simultanément
- Budget Tavily : ~30 requêtes par fichier (1 000 total / 30 claims avec marge)
- Tavily Extract : ~1 crédit par vérification d'URL

## 6. Vérification finale

Après toutes les éditions :

```bash
make check           # Linter overflow (seuil 15 lignes)
make check-citations # Toutes les slides de données ont des sources
make html            # Build propre
```
