# Workflow : créer des slides

<!-- ABOUTME: Workflows complets pour créer des slides Marp — de zéro ou depuis un rapport de recherche. -->
<!-- ABOUTME: Couvre cadrage, recherche, narration, rédaction, PaperBanana et vérification. Référence slide-creation-standards.md. -->

## Quel workflow utiliser ?

| Situation | Workflow |
|-----------|----------|
| Ajouter 2–10 slides sur un sujet précis (pas de rapport existant) | **Partie A** — De zéro |
| Produire un deck complet (25–30 slides) depuis un rapport de recherche | **Partie B** — Depuis un rapport |
| Lancer une recherche multi-agents exhaustive (25–60 items) | Pipeline `/research` → `/research-deep` → `/research-report`, puis Partie B |
| Démarrer une nouvelle session Claude dédiée à la conversion | **Annexe D** — Prompt autonome |

Toutes les conventions de slide (format, budget, langue, citations) sont centralisées dans **`slide-creation-standards.md`**. Ce workflow y fait référence sans les répéter.

---

# Partie A : De zéro — explorer un sujet et produire 2–10 slides

## Phase 1 : Cadrage (~10 min)

### 1.1 Définir l'objectif d'apprentissage

Répondre en une phrase : **qu'est-ce que les étudiants sauront FAIRE après ces slides ?**

Exemples :
- "Évaluer si l'Explainability est un risque ou un avantage pour leur projet IA"
- "Choisir entre 3 stratégies de pricing API pour leur startup"
- "Identifier les étapes clés d'une due diligence IA"

### 1.2 Estimer le nombre de slides

Utiliser la table des formats dans `slide-creation-standards.md` §1.

### 1.3 Choisir le format d'intégration

| Format | Quand |
|--------|-------|
| **Nouvelle section dans un deck existant** | Le sujet enrichit un thème déjà couvert (ex : ajouter un cas dans session-04/B) |
| **Mini-deck autonome** | Le sujet justifie un bloc indépendant (ex : supplément pour le Bloc C pratique) |
| **Supplément discussion** | 1–2 slides de contexte + 1 slide discussion pour animer un échange |

---

## Phase 2 : Recherche ciblée (~30–45 min)

### 2.1 Budget de sources par taille

| Slides prévues | Sources minimum | Sources recommandées |
|----------------|----------------|---------------------|
| 2–3 | 3 | 5 |
| 4–6 | 5 | 8 |
| 7–10 | 8 | 12 |

### 2.2 Sélection des outils

| Besoin | Outil | Usage |
|--------|-------|-------|
| Données marché, chiffres récents | Tavily Search | `query: "[sujet] market size 2025 2026"` |
| Financiers entreprise, benchmarks | Tavily Search | `query: "[entreprise] revenue funding 2024 2025"` |
| Vérification d'un claim précis | Tavily Extract | Lire la page réelle, confirmer le chiffre |
| Documentation framework / lib | Context7 | `resolve-library-id` → `query-docs` |
| Régulation EU | Tavily Search | `query: "EU AI Act [disposition]" site:eur-lex.europa.eu` |

### 2.3 Templates de recherche

**Données marché** :
```
"[sujet] market size 2025 2026" OR "[sujet] adoption rate enterprise"
```

**Financiers entreprise** :
```
"[entreprise] revenue 2024 2025" OR "[entreprise] Series [A/B/C] funding"
```

**Benchmarks techniques** :
```
"[modèle/outil] benchmark performance 2024 2025" site:arxiv.org OR site:huggingface.co
```

**Cas d'étude** :
```
"[entreprise] AI use case" OR "[entreprise] machine learning deployment results"
```

**Régulation EU** :
```
"EU AI Act [article/annexe]" site:eur-lex.europa.eu OR site:europarl.europa.eu
```

### 2.4 Validation des sources

Appliquer la hiérarchie d'autorité et le filtre de récence définis dans `slide-creation-standards.md` §6.2–6.3.

Utiliser Tavily Extract pour vérifier chaque chiffre sur la page réelle (cf. `slide-creation-standards.md` §6.6).

### 2.5 Checkpoint de synthèse

Avant de passer à la phase 3, vérifier :

- [ ] L'objectif d'apprentissage est formulé (§1.1)
- [ ] Le nombre de slides est estimé (§1.2)
- [ ] Assez de sources vérifiées pour couvrir chaque slide de données
- [ ] Au moins 1 exemple français/européen identifié
- [ ] Les chiffres clés sont confirmés par lecture de la source réelle (pas juste un snippet)
- [ ] Pas de claim orphelin (chiffre sans source trouvée)

---

## Phase 3 : Conception narrative (~15 min)

### 3.1 Arc narratif en 5 temps

Chaque ensemble de slides suit cette progression :

| Étape | Rôle | Exemples |
|-------|------|----------|
| **1. Accroche** | Stat surprenante, tension, provocation | "83% des projets IA échouent avant la production" |
| **2. Pourquoi ça compte** | Pertinence business pour des entrepreneurs | "Si vous lancez un produit IA, c'est votre risque #1" |
| **3. Le savoir** | Framework, taxonomie, concept clé | Matrice de maturité, arbre de décision, classification |
| **4. Exemples concrets** | Entreprises réelles 2024–2026, EU/France intégrés | Mistral AI, Klarna, L'Oréal, Doctolib |
| **5. Synthèse** | Si 5+ slides : takeaways en 3–5 points | Points clés numérotés |

Pour 2–3 slides, condenser : accroche + savoir sur slide 1, exemples sur slide 2, leçon/discussion sur slide 3.

### 3.2 Allocation des types de slides

Voir les templates de chaque type dans `slide-creation-standards.md` §3.3.

| Contenu | Type de slide | Quand |
|---------|---------------|-------|
| Accroche avec stat forte | Standard | Toujours pour la première slide |
| Comparaison deux options (Build vs Buy, etc.) | `cols` | Quand 2 alternatives sont directement comparées |
| Spotlight entreprise (faits + analyse) | `cols` | Gauche = faits/métriques, Droite = analyse/leçons |
| Concept illustré par un diagramme | Standard + `![bg right:50%]` | Quand un visuel clarifie mieux que du texte |
| Échange avec la classe | Discussion | 1 par section majeure (groupe de 3–5 slides) |
| Transition entre sous-thèmes | `section` | Uniquement si 7+ slides avec 2+ sous-thèmes |

### 3.3 Décision PaperBanana

Appliquer les critères de décision définis dans `slide-creation-standards.md` §7.

---

## Phase 4 : Rédaction des slides

Appliquer les conventions de `slide-creation-standards.md` (§2 budget, §3 Marp, §4 langue, §6 citations).

Les templates de slide (titre, section, cols, discussion, infographie) se trouvent dans `slide-creation-standards.md` §3.3.

### Rappels pratiques pour la rédaction

- **Front matter** : adapter le header (numéro de session) et le footer (selon les sources) — voir `slide-creation-standards.md` §3.1
- **ABOUTME** : deux commentaires après le front matter — voir §3.2
- **Numérotation** : `# 01 — Titre`, redémarre par fichier — voir §3.4
- **Langue** : français + termes techniques en anglais directement — voir §4
- **Citations** : `[N]` in-text + `<small>Sources</small>` en bas — voir §6.4

---

## Phase 5 : Génération PaperBanana (si applicable, ~15–30 min)

Ne lancer cette phase que si la décision PaperBanana (§3.3 / `slide-creation-standards.md` §7) est positive.

### 5.1 Préparer l'input

Créer un fichier texte de **300+ mots** avec cette structure :

```
Contexte :
Ce diagramme illustre [concept] pour des étudiants M2 en management de
l'innovation. Ils ne sont pas ingénieurs — le visuel doit être accessible
et orienté business.

Éléments à représenter :
1. [Composant 1] — [description courte]
2. [Composant 2] — [description courte]
3. [Composant 3] — [description courte]
[... au moins 4–5 composants]

Hiérarchie :
- Principal : [ce qui doit dominer visuellement]
- Secondaire : [éléments de support]
- Optionnel : [annotations, exemples]

Flux :
[Décrire les connexions : quoi mène à quoi, dans quel ordre]

Annotations :
- Chiffres clés à inclure : [si applicable]
- Exemples d'entreprises : [si applicable]
- Mots-clés : [termes techniques importants]
```

### 5.2 Rédiger la caption

La caption n'est **pas** un titre — c'est une **intention communicative** :

**Formule** : `"[Verbe d'action] [quoi] by [comment] to [objectif]"`

Exemples :
- ❌ "Architecture RAG"
- ✅ "Illustrate the three-step RAG pipeline showing how user queries flow through retrieval, augmentation, and generation to produce sourced answers"
- ❌ "EU AI Act risk levels"
- ✅ "Visualize the four EU AI Act risk tiers from minimal to unacceptable, showing examples and obligations at each level"

### 5.3 Générer

```bash
source .envrc   # exporte GOOGLE_API_KEY

uvx paperbanana generate \
  -i /tmp/description.txt \
  -c "Intention communicative détaillée ici" \
  -n 5
```

#### Flags CLI

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

#### Itérations

| Itérations | Qualité | Usage |
|-----------|---------|-------|
| 5 | Publication-ready | **Standard pour les slides** |
| 7 | Maximum de raffinement | Diagrammes complexes (10+ composants) |

Ne pas descendre en dessous de 5 itérations pour les slides de cours.

### 5.4 Sortie et provenance

Par défaut, les résultats atterrissent dans `outputs/run_<timestamp>_<hash>/`.

Chaque run contient :
- `final_output.png` — le résultat final (seul fichier à intégrer aux slides)
- `planning.json` — description détaillée générée par le Planner, exemples récupérés
- `metadata.json` — modèles utilisés, nombre d'itérations, timestamps
- `diagram_iter_*.png` — images intermédiaires (utile pour voir la progression)
- `iter_*/` — critique et prompts de chaque itération

### 5.5 Ranger et intégrer

1. **Nommer** : `<nom-descriptif>_<run_id>.png`

   ```bash
   cp outputs/run_20260219_143000_abc123/final_output.png \
      infographics/explainability-framework_run_20260219_143000_abc123.png
   ```

2. **Copier** dans les assets de la session :

   ```bash
   cp infographics/explainability-framework_run_20260219_143000_abc123.png \
      slides/session-XX/assets/infographics/
   ```

3. **Référencer** dans la slide :

   ```markdown
   ![bg right:50%](assets/infographics/explainability-framework_run_20260219_143000_abc123.png)
   ```

**Conventions d'intégration** :
- `![bg right:50%]` ou `![bg left:50%]` — partage la slide en deux
- `![bg right:55%]` — donne un peu plus de place à l'image (pour les diagrammes denses)
- Le texte restant doit tenir en ~8–9 lignes (même budget qu'une slide `cols`)
- Les infographies remplacent avantageusement les tableaux lourds (5+ colonnes)
- Conserver les sources `<small>` même quand l'image résume le contenu

**Rangement** :
- `infographics/` et `outputs/` sont gitignorés
- Convention de nommage : partie gauche = nom descriptif en kebab-case, partie droite = identifiant du run PaperBanana

### 5.6 Checklists PaperBanana

**Avant génération** :
1. Le fichier input fait-il **300+ mots** ?
2. La caption décrit-elle l'**intention communicative** (pas juste un titre) ?
3. Le nombre d'itérations est-il à **5 minimum** ?
4. Le `GOOGLE_API_KEY` est-il bien exporté (`source .envrc`) ?

**Après génération** :
1. Le `final_output.png` est-il lisible à la taille d'une demi-slide ?
2. Les éléments clés sont-ils tous présents et correctement labelés ?
3. Le PNG a-t-il un nom `<descriptive>_<run_id>.png` ?

---

## Phase 6 : Vérification (~10 min)

Appliquer la checklist complète de `slide-creation-standards.md` §9.

### Checks automatiques

```bash
make check    # Linter overflow (seuil 15 lignes par slide)
make html     # Build propre, pas d'erreurs
```

### Checklist manuelle

- [ ] **ABOUTME** : deux commentaires présents après le front matter
- [ ] **Front matter** : `marp: true`, `theme: sorbonne`, `paginate: true`, header avec session, footer avec attribution
- [ ] **Numérotation** : `# 01 — Titre` continu, titre/section non numérotés
- [ ] **Langue** : français + termes techniques en anglais directement
- [ ] **Citations** : chaque claim chiffré a un `[1]` in-text + `<small>Sources</small>` en bas de slide
- [ ] **Budget de lignes** : ~13 effectives par slide standard, ~9 pour `cols` (voir §2 des standards)
- [ ] **Sources vérifiées** : chaque URL pointe vers la donnée citée
- [ ] **Contexte EU/France** : au moins 1 exemple européen intégré
- [ ] **Discussion** : si 5+ slides, au moins 1 question de discussion
- [ ] **Infographie** : si générée, lisible à taille demi-slide, éléments clés labelés

---

# Partie B : Depuis un rapport de recherche — convertir en deck complet

## 1. Pré-vol

Avant de démarrer la conversion, évaluer le matériel source :

- [ ] Lire le `report.md` — identifier les catégories/couches/sections
- [ ] Compter le nombre total d'items (entreprises, outils, frameworks, etc.)
- [ ] Estimer le nombre de slides avec la formule de `slide-creation-standards.md` §1
- [ ] Identifier 4–6 items pour les slides spotlight (diversifiés, intéressants, pertinents pour le public)
- [ ] Repérer les items EU/français à intégrer tout au long du deck

## 2. Plan du deck

Rédiger un plan slide-par-slide avant d'écrire :

- Slide titre + 1–2 slides introduction
- 1–2 slides par catégorie (tableaux plafonnés à 7 lignes, diviser si nécessaire)
- 1 spotlight par ~8–10 items (utiliser `_class: cols`)
- 1 question de discussion par section majeure
- 2–3 slides de synthèse + Key Takeaways

## 3. Patterns d'extraction du contenu

### Depuis les tables du rapport → slides de vue d'ensemble

```markdown
| Entreprise | Pays | Métrique clé | Rôle |
```

- Plafonner les tableaux à **7 lignes** — diviser sur 2 slides si nécessaire
- Inclure les drapeaux de pays pour un scan visuel rapide
- Mettre en valeur les entreprises EU avec du **bold** ou une note

### Depuis les profils JSON → slides spotlight

Utiliser le layout `_class: cols`. Colonne gauche = faits, colonne droite = analyse.

```markdown
<div class="left">

- Métriques financières clés (CA, valorisation, croissance)
- Produits/services (2–3 bullets)

</div>
<div class="right">

- Moats compétitifs / ce qui les distingue
- Leçon pour entrepreneurs
- Angle EU/souveraineté (si applicable)

</div>
```

Respecter le budget cols : ~9 lignes de contenu réel (voir `slide-creation-standards.md` §2).

### Depuis les sections d'analyse du rapport → slides de synthèse

- Extraire les thèmes clés, patterns et contrastes
- Cadrer pour la prise de décision entrepreneuriale
- Inclure une slide "Key Takeaways" en fin (5 points numérotés max)

### Gestion des données incertaines

- Si un champ JSON est marqué `uncertain` ou `estimated`, soit le sauter, soit ajouter le qualificatif `(est.)`
- Ne jamais présenter des données incertaines comme définitives

## 4. Discussion

Chaque slide de discussion suit le template de `slide-creation-standards.md` §3.3 (slide de discussion).

## 5. Rédaction

Appliquer toutes les conventions de `slide-creation-standards.md` :
- Front matter avec le footer "Recherche [Topic] 2024–2026 · Données publiques" (§3.1)
- ABOUTME (§3.2), numérotation (§3.4), langue (§4), citations (§6.4)
- Utiliser des **subagents** pour lire les fichiers volumineux (`report.md`, JSONs). Ne jamais lire de gros fichiers directement dans le contexte principal — risque de compaction du contexte.

## 6. Vérification

Appliquer la checklist de `slide-creation-standards.md` §9, plus :

- [ ] Tous les chiffres financiers correspondent aux données de `report.md`
- [ ] Les entreprises EU sont intégrées tout au long (pas isolées sur une slide)
- [ ] Pas de subheaders `###` à l'intérieur des layouts `cols`

---

# Annexes

## Annexe A : Exemple détaillé — "Explainability in AI"

Déroulé complet pour 5 slides ajoutées à `session-05/A-regulation-ethique.md`.

### Phase 1 — Cadrage

- **Objectif** : "Évaluer si l'Explainability est un levier de conformité ou un avantage compétitif pour leur projet IA"
- **Estimation** : concept technique + implications business → **5 slides**
- **Format** : nouvelle section dans le deck existant `session-05/A-regulation-ethique.md`

### Phase 2 — Recherche

Sources ciblées (5 slides → 5–8 sources visées) :
1. Tavily Search : `"explainable AI market size 2025 2026"` → Gartner/MarketsAndMarkets
2. Tavily Search : `"EU AI Act transparency obligation Article 13"` → EUR-Lex
3. Tavily Search : `"SHAP LIME explainability benchmark 2024"` → arXiv
4. Tavily Search : `"explainable AI enterprise adoption 2025"` → McKinsey/Deloitte
5. Tavily Extract : vérifier les chiffres sur chaque page source

Résultat : 6 sources validées, 1 exemple français (BNP Paribas).

### Phase 3 — Conception narrative

| Slide | Étape narrative | Type | Contenu |
|-------|----------------|------|---------|
| Section | — | `section` | "Explainability : obligation ou opportunité ?" |
| 15 | Accroche | Standard | Stat marché XAI + obligation EU AI Act Art. 13 |
| 16 | Le savoir | Standard + infographie | Taxonomie des méthodes (SHAP, LIME, Attention Maps) |
| 17 | Exemples | `cols` | BNP Paribas (EU) vs Stripe (US) — approches comparées |
| 18 | Implications | Standard | Trade-off performance vs interprétabilité |
| 19 | Discussion | Discussion | "Votre startup de scoring RH doit expliquer ses décisions..." |

Décision PaperBanana : **OUI** pour slide 16 — taxonomie avec 5+ méthodes et hiérarchie.

### Phase 5 — PaperBanana

Input (300+ mots) décrivant la taxonomie XAI. Caption : "Visualize the taxonomy of explainability methods organized by scope (local vs global) and technique (perturbation, gradient, attention), with enterprise adoption levels annotated."

Commande : `uvx paperbanana generate -i /tmp/xai-taxonomy.txt -c "..." -n 5`

### Phase 6 — Vérification

```bash
make check    # Confirmer 0 overflow sur les nouvelles slides
make html     # Build propre
```

Inspection visuelle des 5 slides dans le navigateur.

---

## Annexe B : Carte de référence rapide

```
┌─────────────────────────────────────────────────────────┐
│  CADRAGE                                                │
│  1. Objectif : étudiants sauront FAIRE quoi ?           │
│  2. Slides : cas 2-3 / concept 3-5 / framework 4-6 /   │
│             marché 5-8 / panorama 7-10                  │
│  3. Format : section existante / mini-deck / discussion │
├─────────────────────────────────────────────────────────┤
│  RECHERCHE                                              │
│  Sources : 3-5 (petit) → 8-12 (grand)                  │
│  Outils : Tavily Search + Extract, Context7             │
│  Validation : slide-creation-standards.md §6.2-6.3      │
├─────────────────────────────────────────────────────────┤
│  NARRATIF                                               │
│  1. Accroche  2. Pourquoi  3. Savoir                    │
│  4. Exemples  5. Synthèse (si 5+ slides)                │
├─────────────────────────────────────────────────────────┤
│  TYPES DE SLIDES                                        │
│  Voir slide-creation-standards.md §2-3                  │
│  Standard : ~13 lignes effectives                       │
│  Cols : ~9 lignes contenu réel, pas de ### dans cols    │
│  Discussion : scénario + 2-3 questions trade-off        │
│  Infographie : bg right:50%, ~8-9 lignes de texte       │
├─────────────────────────────────────────────────────────┤
│  PAPERBANANA                                            │
│  Décision : slide-creation-standards.md §7              │
│  Input : 300+ mots, caption = intention communicative   │
│  CLI : uvx paperbanana generate -i <f> -c "<c>" -n 5   │
├─────────────────────────────────────────────────────────┤
│  VÉRIFICATION                                           │
│  make check → make html → checklist manuelle            │
│  Détails : slide-creation-standards.md §9               │
└─────────────────────────────────────────────────────────┘
```

---

## Annexe C : Pièges courants

Voir la liste complète dans `slide-creation-standards.md` §8. Les pièges les plus fréquents en workflow :

| Piège | Solution |
|-------|----------|
| **Trop de slides** — le sujet explose au-delà du budget | Revenir au §1.2, se rappeler que 2–3 slides bien sourcées > 8 slides superficielles |
| **Recherche sans fin** — 45 min passées sans avoir écrit une ligne | Appliquer le checkpoint §2.5 à 30 min max, passer à la rédaction même si imparfait |
| **Sources snippet-only** — un chiffre repris d'un snippet sans vérifier la page | Toujours Tavily Extract pour lire la page réelle avant de citer |
| **Pas de discussion** — slides purement magistrales sur 7+ slides | Ajouter au moins 1 question de discussion par section de 3–5 slides |

---

## Annexe D : Prompt autonome pour nouvelle session

Ce prompt permet de lancer une conversion de rapport de recherche dans une session Claude indépendante.

### Votre tâche

Convertir un topic de recherche complété en un deck Marp pour le cours M2 IMT&E à Paris 1 Panthéon-Sorbonne.

**Vous recevrez** : un chemin vers un répertoire de recherche (ex : `docs/research/ai-market-intelligence/`) contenant `report.md` et `results/*.json`.

### Processus

1. **Lire les références** :
   - `docs/references/slide-creation-standards.md` — toutes les conventions
   - `docs/references/workflow-new-slides.md` — ce fichier, Partie B
   - `CLAUDE.md` — conventions globales du projet

2. **Analyser le matériel source** :
   - **Utiliser un subagent** pour lire `report.md` et extraire les données structurées (catégories, items, tables par catégorie, items EU/français)
   - **Utiliser un subagent** pour lire 4–6 spotlight JSONs depuis `results/*.json` (diversifiés, au moins 1 EU, 1 leader, 1 underdog)
   - **NE PAS lire de gros fichiers directement dans le contexte principal** — risque de compaction

3. **Planifier le deck** : suivre la Partie B §1–2

4. **Rédiger le deck** : suivre la Partie B §3–5 et les standards

5. **Vérifier** :
   - `sed -i 's/\r$//' <fichier>` (corriger les fins de ligne CRLF)
   - `make check` — 0 overflow
   - `make check-citations` — toutes les slides de données ont des sources
   - `make html` — build propre
   - Rapporter : nombre de slides, liste des spotlights, questions de discussion, nombre de citations

### Checklist qualité

- [ ] `make check` passe (0 avertissements overflow)
- [ ] `make check-citations` passe
- [ ] `make html` build sans erreurs
- [ ] ABOUTME présents
- [ ] Numérotation correcte (01–XX continu, titre/section non numérotés)
- [ ] Français + termes techniques anglais (pas de traductions parenthétiques)
- [ ] Entreprises EU intégrées tout au long
- [ ] Questions de discussion = scénarios entrepreneuriaux concrets
- [ ] Chiffres financiers correspondent aux données de report.md
- [ ] Pas de `###` à l'intérieur des layouts cols
