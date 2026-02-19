# Guide d'exploration de sujet — De l'idée aux slides

<!-- ABOUTME: Workflow en une session pour explorer un sujet et produire 2-10 slides sourcées avec infographies optionnelles. -->
<!-- ABOUTME: Guide autonome couvrant cadrage, recherche ciblée, arc narratif, rédaction et vérification. -->

## Quand utiliser ce guide

| Situation | Outil |
|-----------|-------|
| Ajouter 2-10 slides sur un sujet précis | **Ce guide** |
| Produire un deck complet (25-30 slides) depuis un rapport de recherche existant | `research-to-slides-template.md` + `convert-research-to-slides.prompt.md` |
| Lancer une recherche multi-agents exhaustive (25-60 items) | Pipeline `/research` → `/research-deep` → `/research-report` |

Ce guide couvre tout en une session : cadrage, recherche, conception narrative, rédaction et vérification. Pas besoin de rapport préexistant.

---

## Phase 1 : Cadrage (~10 min)

### 1.1 Définir l'objectif d'apprentissage

Répondre en une phrase : **qu'est-ce que les étudiants sauront FAIRE après ces slides ?**

Exemples :
- "Évaluer si l'Explainability est un risque ou un avantage pour leur projet IA"
- "Choisir entre 3 stratégies de pricing API pour leur startup"
- "Identifier les étapes clés d'une due diligence IA"

### 1.2 Estimer le nombre de slides

| Type de sujet | Slides | Raison |
|---------------|--------|--------|
| **Cas d'étude** (1 entreprise) | 2–3 | Contexte + analyse + leçon |
| **Concept technique** (ex : Quantization) | 3–5 | Définition + mécanisme + exemples + implications business |
| **Framework / méthodologie** (ex : AI Canvas) | 4–6 | Cadre + composants + exemples + exercice |
| **Tendance marché** (ex : AI Agents en 2026) | 5–8 | Chiffres + taxonomie + acteurs + cas + implications |
| **Panorama** (ex : outils no-code IA) | 7–10 | Vue d'ensemble + catégories + spotlights + discussion |

### 1.3 Choisir le format d'intégration

| Format | Quand |
|--------|-------|
| **Nouvelle section dans un deck existant** | Le sujet enrichit un thème déjà couvert (ex : ajouter un cas dans session-04/B) |
| **Mini-deck autonome** | Le sujet justifie un bloc indépendant (ex : supplément pour le Bloc C pratique) |
| **Supplément discussion** | 1-2 slides de contexte + 1 slide discussion pour animer un échange |

---

## Phase 2 : Recherche ciblée (~30-45 min)

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

Appliquer la hiérarchie d'autorité :

| Rang | Type de source | Exemples |
|------|---------------|----------|
| 1 | IR d'entreprise / SEC filings | Rapports annuels, documents investors |
| 2 | Publications peer-reviewed | arXiv, NeurIPS, ICML |
| 3 | Recherche Tier-1 | Gartner, McKinsey, Stanford HAI, OECD |
| 4 | Presse Tier-1 | Bloomberg, Reuters, CNBC, Financial Times |
| 5 | Presse Tier-2 | TechCrunch, The Verge, Ars Technica |
| 6 | Bases de données startups | Crunchbase, Sacra, PitchBook |

**Filtre de récence** :
- **Rejet dur** : source > 2 ans pour tout claim sur le marché/adoption IA
- **Exception** : faits historiques (AlexNet 2012, Flash Crash 2010) et jurisprudence
- **Préférence** : source < 6 mois quand disponible
- **Conflit** : le plus récent gagne, sauf si la source plus ancienne est nettement plus autoritaire

**Vérification** : utiliser Tavily Extract pour lire la page réelle et confirmer que le chiffre correspond. Ne pas se fier aux snippets de recherche.

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
| **4. Exemples concrets** | Entreprises réelles 2024-2026, EU/France intégrés | Mistral AI, Klarna, L'Oréal, Doctolib |
| **5. Synthèse** | Si 5+ slides : takeaways en 3-5 points | Points clés numérotés |

Pour 2-3 slides, condenser : accroche + savoir sur slide 1, exemples sur slide 2, leçon/discussion sur slide 3.

### 3.2 Allocation des types de slides

| Contenu | Type de slide | Quand |
|---------|---------------|-------|
| Accroche avec stat forte | Standard | Toujours pour la première slide |
| Comparaison deux options (Build vs Buy, etc.) | `cols` | Quand 2 alternatives sont directement comparées |
| Spotlight entreprise (faits + analyse) | `cols` | Gauche = faits/métriques, Droite = analyse/leçons |
| Concept illustré par un diagramme | Standard + `![bg right:50%]` | Quand un visuel clarifie mieux que du texte |
| Échange avec la classe | Discussion | 1 par section majeure (groupe de 3-5 slides) |
| Transition entre sous-thèmes | `section` | Uniquement si 7+ slides avec 2+ sous-thèmes |

### 3.3 Décision PaperBanana

**OUI — générer une infographie** quand :
- Framework avec **4+ composants** (ex : AI Canvas, CRISP-DM)
- Processus avec **3+ branches** ou embranchements (ex : arbre de décision Build vs Buy)
- Taxonomie avec **hiérarchie** (ex : types d'IA, niveaux de risque EU AI Act)
- Concept nécessitant **10+ bullets** si présenté en texte seul

**NON — rester en texte** quand :
- Comparaison simple de 2-3 items → utiliser `cols`
- Statistiques pures → utiliser un tableau ou des bullets avec **bold**
- Séquence linéaire < 4 étapes → numéroter en bullets
- Spotlight entreprise → utiliser `cols` (faits | analyse)

---

## Phase 4 : Rédaction des slides

### 4.1 Template — Slide standard

```markdown
# XX — Titre de la slide

- Premier point avec donnée sourcée [1]
- Deuxième point
- Troisième point

> Callout ou insight clé pour les entrepreneurs

<small>Sources : [1] [Autorité](https://url-complète)</small>
```

**Budget** : ~13 lignes de contenu effectif (seuil linter = 15, la ligne de sources coûte ~1).

### 4.2 Template — Slide cols (spotlight)

```markdown
<!-- _class: cols -->

# XX — Nom de l'entreprise

<div class="left">

- **Fondation** : 2023, Paris
- **Valorisation** : $6 Mds [1]
- **Produit** : Mistral Large, Le Chat

</div>
<div class="right">

- **Moat** : souveraineté EU, open-weight
- **Leçon** : le timing réglementaire crée des opportunités
- Pour un entrepreneur : alternative crédible aux US

</div>

<small>Sources : [1] [Mistral AI](https://mistral.ai)</small>
```

**Budget** : ~8-9 lignes de contenu réel par colonne. Les tags `<div>` comptent comme lignes de contenu pour le linter. Éviter les `###` à l'intérieur des colonnes.

### 4.3 Template — Slide discussion

```markdown
# XX — Discussion : [Sujet]

> [Scénario concret — mettre les étudiants dans la peau de l'entrepreneur.
> Ex : "Vous développez une app de recrutement. Un candidat vous demande
> pourquoi l'IA a rejeté son CV. Que répondez-vous ?"]

**Questions pour la classe** :
- [Question spécifique avec un vrai trade-off]
- [Question qui se connecte au contexte entrepreneurial]
```

Bonnes questions :
- Présentent un vrai trade-off (coût vs souveraineté, vitesse vs contrôle)
- Référencent des entreprises vues dans les slides précédentes
- N'ont pas de réponse unique "correcte"

### 4.4 Template — Slide avec infographie

```markdown
# XX — Titre de la slide

- Point clé condensé
- Deuxième point

> Callout ou insight

![bg right:50%](assets/infographics/nom-descriptif_run_YYYYMMDD_HHMMSS_hash.png)

<small>Sources : [1] [Autorité](https://url)</small>
```

**Budget** : ~8-9 lignes de texte (même budget qu'une slide `cols`). L'image occupe 50% de la slide.

### 4.5 Conventions de rédaction

| Convention | Règle |
|------------|-------|
| **Langue** | Corps en français, termes techniques en anglais directement |
| | ✅ "Le Fine-tuning permet d'adapter..." |
| | ❌ "Le réglage fin *(Fine-tuning)* permet..." |
| **Numérotation** | `# 01 — Titre` (2 chiffres, tiret cadratin, redémarre par fichier) |
| **Titre/section** | NON numérotés |
| **Bullets** | Concis, pas de longs paragraphes |
| **Tableaux** | Max 7 lignes — diviser sur 2 slides si nécessaire |
| **Citations** | `[1]` in-text + `<small>Sources : [1] [Autorité](url)</small>` en bas |
| **Blockquotes** | `>` pour callouts, tips et takeaways |

### 4.6 Front matter

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session N · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0"
---
```

Adapter le footer selon les sources :
- Multi-sources (recherche + Andrew Ng) : `"Sources multiples · DeepLearning.AI CC BY-SA 2.0"`
- Recherche originale uniquement : `"Recherche [Topic] 2024–2026 · Données publiques"`
- Principalement Andrew Ng : `"Adapté de Generative AI for Everyone par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"`

### 4.7 Commentaires ABOUTME

Chaque fichier `.md` commence (après le front matter) par deux commentaires :

```markdown
<!-- ABOUTME: Description brève du contenu du deck. -->
<!-- ABOUTME: Public visé et approche pédagogique. -->
```

---

## Phase 5 : Génération PaperBanana (si applicable, ~15-30 min)

Ne lancer cette phase que si la décision PaperBanana (§3.3) est positive.

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
[... au moins 4-5 composants]

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

| Itérations | Usage |
|-----------|-------|
| 5 | **Standard pour les slides** — publication-ready |
| 7 | Diagrammes complexes (10+ composants) |

Résultat dans `outputs/run_<timestamp>_<hash>/final_output.png`.

### 5.4 Ranger et intégrer

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

---

## Phase 6 : Vérification (~10 min)

### 6.1 Checks automatiques

```bash
make check    # Linter overflow (seuil 15 lignes par slide)
make html     # Build propre, pas d'erreurs
```

### 6.2 Checklist manuelle

- [ ] **ABOUTME** : deux commentaires présents après le front matter
- [ ] **Front matter** : `marp: true`, `theme: sorbonne`, `paginate: true`, header avec session, footer avec attribution
- [ ] **Numérotation** : `# 01 — Titre` continu, titre/section non numérotés
- [ ] **Langue** : français + termes techniques en anglais directement (pas de traductions parenthétiques)
- [ ] **Citations** : chaque claim chiffré a un `[1]` in-text + `<small>Sources</small>` en bas de slide
- [ ] **Budget de lignes** : ~13 effectives par slide standard, ~8-9 par colonne pour `cols`
- [ ] **Sources vérifiées** : chaque URL pointe vers la donnée citée (pas un snippet)
- [ ] **Contexte EU/France** : au moins 1 exemple européen intégré (pas isolé)
- [ ] **Discussion** : si 5+ slides, au moins 1 question de discussion
- [ ] **Infographie** : si générée, lisible à taille demi-slide, éléments clés labelés

---

## Annexe A : Exemple détaillé — "Explainability in AI"

Déroulé complet pour 5 slides ajoutées à `session-05/A-regulation-ethique.md`.

### Phase 1 — Cadrage

- **Objectif** : "Évaluer si l'Explainability est un levier de conformité ou un avantage compétitif pour leur projet IA"
- **Estimation** : concept technique + implications business → **5 slides**
- **Format** : nouvelle section dans le deck existant `session-05/A-regulation-ethique.md`

### Phase 2 — Recherche

Sources ciblées (5 slides → 5-8 sources visées) :
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

### Phase 4 — Rédaction

*(Appliquer les templates de la Phase 4 pour chaque slide.)*

### Phase 5 — PaperBanana

Input (300+ mots) décrivant la taxonomie XAI, caption : "Visualize the taxonomy of explainability methods organized by scope (local vs global) and technique (perturbation, gradient, attention), with enterprise adoption levels annotated."

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
│  Hiérarchie : IR > papers > Tier-1 research > Tier-1    │
│  press > Tier-2 > Crunchbase                            │
│  Récence : <6 mois préféré, >2 ans rejet dur            │
├─────────────────────────────────────────────────────────┤
│  NARRATIF                                               │
│  1. Accroche  2. Pourquoi  3. Savoir                    │
│  4. Exemples  5. Synthèse (si 5+ slides)                │
├─────────────────────────────────────────────────────────┤
│  TYPES DE SLIDES                                        │
│  Standard : 13 lignes effectives                        │
│  Cols : 8-9 lignes/colonne, pas de ### dans cols        │
│  Discussion : scénario + 2-3 questions trade-off        │
│  Infographie : bg right:50%, 8-9 lignes de texte        │
├─────────────────────────────────────────────────────────┤
│  PAPERBANANA                                            │
│  OUI : framework 4+, process 3+ branches, taxonomie     │
│  NON : 2-3 items, stats pures, séquence <4 étapes       │
│  Input : 300+ mots, caption = intention communicative   │
│  CLI : uvx paperbanana generate -i <f> -c "<c>" -n 5   │
├─────────────────────────────────────────────────────────┤
│  VÉRIFICATION                                           │
│  make check → make html → checklist manuelle            │
└─────────────────────────────────────────────────────────┘
```

---

## Annexe C : Pièges courants

| Piège | Solution |
|-------|----------|
| **Trop de slides** — le sujet explose au-delà du budget | Revenir au §1.2, se rappeler que 2-3 slides bien sourcées > 8 slides superficielles |
| **Recherche sans fin** — 45 min passées sans avoir écrit une ligne | Appliquer le checkpoint §2.5 à 30 min max, passer à la rédaction même si imparfait |
| **Sources snippet-only** — un chiffre repris d'un snippet sans vérifier la page | Toujours Tavily Extract pour lire la page réelle avant de citer |
| **Input PaperBanana trop court** — résultat générique | Minimum 300 mots, structurer avec les 5 sections du template (§5.1) |
| **Caption PaperBanana = titre** — résultat plat | La caption est une intention communicative, pas un nom (§5.2) |
| **Overflow cols** — le linter signale >15 lignes | Les tags `<div>` comptent — budgeter seulement 10 lignes de contenu réel |
| **Termes techniques traduits** — "le réglage fin (Fine-tuning)" | Utiliser le terme anglais directement : "le Fine-tuning" |
| **Claim non sourcé** — chiffre sans `[1]` ni `<small>Sources</small>` | Adoucir ("environ", "de l'ordre de") ou sourcer. Jamais inventer une source |
| **Tous les exemples EU sur une seule slide** | Intégrer les exemples français/européens tout au long, synthétiser en fin |
| **Pas de discussion** — slides purement magistrales sur 7+ slides | Ajouter au moins 1 question de discussion par section de 3-5 slides |
