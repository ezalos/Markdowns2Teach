# Guide PaperBanana — Infographies pour slides

<!-- ABOUTME: Guide pratique pour générer des infographies avec PaperBanana CLI. -->
<!-- ABOUTME: Couvre la préparation des inputs, la génération, le rangement et l'intégration Marp. -->

## Qu'est-ce que PaperBanana ?

PaperBanana est un outil CLI qui génère des diagrammes académiques/éducatifs via un pipeline multi-agents (Retriever → Planner → Stylist → Visualizer ↔ Critic). Il produit des infographies au style NeurIPS, adaptées à des slides de cours.

## Prérequis

```bash
source .envrc   # exporte GOOGLE_API_KEY depuis GEMINI_API_KEY
```

L'outil s'exécute via `uvx` (pas besoin d'installation permanente).

## Commande de base

```bash
uvx paperbanana generate \
  -i /tmp/description.txt \
  -c "Descriptive caption explaining the diagram's purpose" \
  -n 5
```

## Flags CLI

| Flag | Description | Obligatoire |
|------|------------|-------------|
| `-i` / `--input` | Fichier texte décrivant le contenu du diagramme | Oui |
| `-c` / `--caption` | Caption / intention communicative du diagramme | Oui |
| `-n` / `--iterations` | Nombre de passes de raffinement (défaut : 3) | Non |
| `-o` / `--output` | Chemin de sortie (auto-généré si omis) | Non |
| `--vlm-model` | Modèle VLM (défaut : `gemini-2.0-flash`) | Non |
| `--image-model` | Modèle image (défaut : `gemini-3-pro-image-preview`) | Non |
| `--config` | Fichier YAML de configuration | Non |

**Flags qui n'existent PAS** (erreurs courantes) :
- ~~`--context-file`~~ → utiliser `--input` / `-i`
- ~~`--diagram-type`~~ → uniquement disponible via l'API Python

## Écrire un bon input

La qualité de l'input détermine la qualité du résultat.

**Longueur minimum : 300+ mots.** Les inputs de 100-200 mots produisent des résultats génériques. Le Planner enrichit l'input, mais il a besoin de matière.

**Structure recommandée pour l'input** :
1. **Contexte** — à quoi sert ce diagramme, pour quel public
2. **Éléments à représenter** — lister les composants, étapes, relations
3. **Hiérarchie** — préciser ce qui est principal vs secondaire
4. **Flux** — décrire les connexions et l'ordre de lecture
5. **Annotations** — mots-clés, chiffres, exemples à inclure

**Structure recommandée pour la caption** :
- Pas juste un titre ("Architecture RAG")
- Une intention communicative ("Illustrate the three-step RAG pipeline showing how user queries flow through retrieval, augmentation, and generation to produce sourced answers")

## Nombre d'itérations

| Itérations | Qualité | Temps | Usage |
|-----------|---------|-------|-------|
| 2 | Brouillon acceptable | ~1 min | Test rapide |
| 5 | Publication-ready | ~3 min | **Recommandé pour slides** |
| 7 | Maximum de raffinement | ~5 min | Diagrammes complexes (10+ composants) |

**Toujours utiliser 5 itérations minimum pour les slides de cours.**

## Sortie et provenance

Par défaut, les résultats atterrissent dans `outputs/run_<timestamp>_<hash>/`.

Chaque run contient :
- `final_output.png` — le résultat final (seul fichier à intégrer aux slides)
- `planning.json` — description détaillée générée par le Planner, exemples récupérés
- `metadata.json` — modèles utilisés, nombre d'itérations, timestamps
- `diagram_iter_*.png` — images intermédiaires (utile pour voir la progression)
- `iter_*/` — critique et prompts de chaque itération

## Rangement des infographies

Après génération, organiser les résultats dans `infographics/` :

```
infographics/
├── ai-history_run_20260216_171305_8a5d6f.png
├── dl-convergence_run_20260216_171308_a41957.png
└── ...
```

**Convention de nommage** : `<descriptive-name>_<run_id>.png`
- Partie gauche : nom descriptif en kebab-case (ex : `ai-history`)
- Partie droite : l'identifiant du run PaperBanana (ex : `run_20260216_171305_8a5d6f`)
- Cela permet de retrouver le dossier `outputs/<run_id>/` original (planning, metadata, itérations)

**Règles** :
- Copier `final_output.png` avec le nom descriptif + run ID
- `infographics/` et `outputs/` sont gitignorés

## Intégration dans les slides Marp

Copier les PNGs nécessaires dans `slides/session-XX/assets/infographics/` :

```bash
cp infographics/my-diagram_run_20260216_171305_8a5d6f.png slides/session-02/assets/infographics/
```

Utiliser la syntaxe Marp background image :

```markdown
# 07 — Titre de la slide

- Point clé condensé
- Deuxième point

> Callout ou insight

![bg right:50%](assets/infographics/my-diagram_run_20260216_171305_8a5d6f.png)
```

**Conventions d'intégration** :
- `![bg right:50%]` ou `![bg left:50%]` — partage la slide en deux
- `![bg right:55%]` — donne un peu plus de place à l'image (pour les diagrammes denses)
- Le texte restant doit tenir en **~8-9 lignes** (même budget qu'une slide `cols`)
- Les infographies remplacent avantageusement les tableaux lourds (5+ colonnes)
- Conserver les sources `<small>` même quand l'image résume le contenu

## Checklist avant génération

1. Le fichier input fait-il **300+ mots** ?
2. La caption décrit-elle l'**intention communicative** (pas juste un titre) ?
3. Le nombre d'itérations est-il à **5 minimum** ?
4. Le `GOOGLE_API_KEY` est-il bien exporté (`source .envrc`) ?

## Checklist après génération

1. Le `final_output.png` est-il lisible à la taille d'une demi-slide ?
2. Les éléments clés sont-ils tous présents et correctement labelés ?
3. Le PNG a-t-il un nom `<descriptive>_<run_id>.png` ?
