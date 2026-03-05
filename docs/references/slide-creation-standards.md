# Standards de création de slides

<!-- ABOUTME: Source unique de vérité pour toutes les règles de construction de slides Marp du cours. -->
<!-- ABOUTME: Couvre structure, budget de contenu, conventions Marp, langue, citations, sourcing et vérification. -->

---

## 1. Formule de structure

Chaque deck couvre **45 minutes** de présentation et vise **25–30 slides**.

| Section | Slides | Contenu |
|---------|--------|---------|
| Titre | 1 | `_class: title`, titre du deck, sous-titre, info du cours |
| Introduction | 1–2 | Pourquoi ce sujet, périmètre, questions récurrentes |
| Vue d'ensemble | 1 | Tableau récapitulatif des catégories/couches |
| Blocs thématiques | 1–2 par catégorie | Tableau d'items + 1 spotlight par 8–10 items |
| Questions de discussion | 1 par section | Scénario + 2–3 questions pour la classe |
| Synthèse | 2–3 | Points clés, angle EU, takeaways |

**Ratio spotlights** : ~1 spotlight pour 8–10 items dans le rapport source.

**Ratio discussions** : ~1 discussion par section majeure (groupe de 2–4 slides thématiques).

Pour les ensembles de 2–10 slides (ajout ponctuel à un deck existant), adapter proportionnellement :

| Type de sujet | Slides | Raison |
|---------------|--------|--------|
| Cas d'étude (1 entreprise) | 2–3 | Contexte + analyse + leçon |
| Concept technique | 3–5 | Définition + mécanisme + exemples + implications business |
| Framework / méthodologie | 4–6 | Cadre + composants + exemples + exercice |
| Tendance marché | 5–8 | Chiffres + taxonomie + acteurs + cas + implications |
| Panorama | 7–10 | Vue d'ensemble + catégories + spotlights + discussion |

---

## 2. Budget de contenu par slide

Le linter (`make check`) détecte le **overflow pixel-accurate** en rendant les slides via Marp + Puppeteer (headless Chrome) et en comparant `scrollHeight` vs `clientHeight` sur chaque `<section>`. Les budgets ci-dessous restent de bons repères pour l'écriture, mais la vérification définitive est le rendu réel.

| Type de slide | Lignes linter max | Lignes de contenu effectif | Notes |
|---------------|-------------------|---------------------------|-------|
| Standard | 15 | **~13** | La ligne `<small>Sources</small>` coûte ~1 ligne |
| Cols | 15 | **~10 réparties sur 2 colonnes** | 1 titre + 4 tags `<div>` = 5 lignes d'overhead → reste 10 pour le contenu réel (~5 par colonne) |
| Infographie (`bg right:50%`) | 15 | **~8–9 lignes de texte** | L'image occupe 50% de la slide |

**Détail du budget cols** :

```
# XX — Titre                    ← 1 ligne (heading)
<div class="left">              ← 1 ligne (div tag)
- Bullet 1                      ← contenu
- Bullet 2                      ← contenu
</div>                          ← 1 ligne (div tag)
<div class="right">             ← 1 ligne (div tag)
- Bullet 3                      ← contenu
- Bullet 4                      ← contenu
</div>                          ← 1 ligne (div tag)
<small>Sources : ...</small>    ← ~1 ligne
```

Total overhead : 1 (titre) + 4 (divs) + 1 (sources) = 6 → **reste ~9 lignes de contenu réel** réparties entre les deux colonnes.

Éviter les `###` à l'intérieur des colonnes — ils consomment une ligne sans apport visuel à cette densité.

---

## 3. Conventions Marp

### 3.1 Front matter

```yaml
---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session N · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples · DeepLearning.AI CC BY-SA 2.0"
---
```

- Le header inclut le numéro de session
- Le footer liste les attributions. Trois options selon les sources :

| Cas | Footer |
|-----|--------|
| Multi-sources (recherche + Andrew Ng) | `"Sources multiples · DeepLearning.AI CC BY-SA 2.0"` |
| Principalement Andrew Ng | `"Adapté de Generative AI for Everyone par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"` |
| Recherche originale uniquement | `"Recherche [Topic] 2024–2026 · Données publiques"` |

### 3.2 Commentaires ABOUTME

Chaque fichier `.md` commence (après le front matter) par deux commentaires :

```markdown
<!-- ABOUTME: Description brève du contenu du deck. -->
<!-- ABOUTME: Public visé et approche pédagogique. -->
```

### 3.3 Types de slides

#### Slide titre

```markdown
<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Titre du deck

## Sous-titre

Deep Tech & ML (UE3) · Session N
M2 IMT&E · Paris 1 Panthéon-Sorbonne
```

#### Séparateur de section

```markdown
<!-- _class: section -->

# Nom de la section
```

#### Slide à deux colonnes

```markdown
<!-- _class: cols -->

# XX — Titre

<div class="left">

- Faits, métriques
- Produits/services

</div>
<div class="right">

- Analyse, moats
- Leçon pour entrepreneurs

</div>
```

#### Slide de discussion

```markdown
# XX — Discussion : [Sujet]

> [Scénario concret — mettre les étudiants dans la peau de l'entrepreneur.
> Ex : "Vous développez une app de recrutement. Un candidat vous demande
> pourquoi l'IA a rejeté son CV. Que répondez-vous ?"]

**Questions pour la classe** :
- [Question spécifique avec un vrai trade-off]
- [Question qui se connecte au contexte entrepreneurial]
```

Bonnes questions de discussion :
- Présentent un vrai trade-off (coût vs souveraineté, vitesse vs contrôle)
- Référencent des entreprises vues dans les slides précédentes
- N'ont pas de réponse unique "correcte"
- Se connectent au contexte entrepreneurial des étudiants

#### Slide avec infographie

```markdown
# XX — Titre de la slide

- Point clé condensé
- Deuxième point

> Callout ou insight

![bg right:50%](assets/infographics/nom-descriptif_run_YYYYMMDD_HHMMSS_hash.png)

<small>Sources : [1] [Autorité](https://url)</small>
```

### 3.4 Numérotation

- Slides de contenu : `# 01 — Titre` (2 chiffres, tiret cadratin, redémarre par fichier)
- Slides titre et séparateurs de section : **NON numérotés**
- Permet de référencer facilement : "déplace la slide 03 après la 05"

---

## 4. Règles linguistiques

- **Corps de texte** : français
- **Termes techniques** : anglais, utilisés directement sans traduction
  - ✅ "Le Supervised Learning est la technique la plus déployée..."
  - ❌ "L'apprentissage supervisé *(Supervised Learning)*"
- Bullet points concis, pas de longs paragraphes
- Tableaux pour les comparaisons (input/output, outils) — max **7 lignes** par tableau, diviser sur 2 slides si nécessaire
- Blockquotes (`>`) pour les callouts, tips et takeaways

---

## 5. Cadrage du contenu

- **Business-first** : cadrer les concepts pour des entrepreneurs, pas des chercheurs
- **Questions d'engagement** : 1–2 questions de discussion par section majeure
- **Cas réels 2024–2026** : éviter les exemples datés
- **Contexte EU/France** : intégrer les entreprises françaises et européennes tout au long du deck (pas isolées sur une seule slide)

---

## 6. Citations et sourcing

### 6.1 Classification des claims

**Nécessite une source** (`[1]` + `<small>Sources</small>`) :
- Tout **chiffre** : montants en dollars, pourcentages, taux de croissance, tailles de marché, effectifs
- Toute **statistique nommée** : "X% des entreprises font Y"
- Tout **fait spécifique à une entreprise** : chiffre d'affaires, valorisation, levée de fonds, nombre d'utilisateurs
- Tout **résultat de benchmark** : scores de précision, taux d'erreur, comparaisons de performance
- Toute **donnée de pricing** : coûts API, tarifs d'abonnement, fourchettes de prix
- Toute **prédiction/prévision** : "le marché atteindra $X en 2030"

**Ne nécessite PAS de source** :
- **Déductions logiques** : raisonnements, pas de claims factuels
- **Définitions** : explications de concepts niveau manuel
- **Cadrage pédagogique** : métaphores, analogies d'enseignement
- **Descriptions d'outils** (sans statistiques) : ce qu'un outil fait, pas combien d'utilisateurs il a
- **Questions de discussion** : pas de claim factuel

**Zone grise** — résoudre vers le sourçage :
- "Andrew Ng dit X" → Trouver d'où Ng tire l'info. Citer la source amont, pas Ng.
- "Il est bien connu que..." → S'il y a un chiffre, sourcer.
- "Estimations sectorielles" ou "Estimations développeurs" → **Pas des vraies sources**. Remplacer par un vrai rapport/enquête ou adoucir le langage.

### 6.2 Hiérarchie d'autorité des sources

| Rang | Type de source | Exemples |
|------|---------------|----------|
| 1 | **IR d'entreprise / SEC filings** | Rapports annuels, documents investors — chiffres audités |
| 2 | **Publications peer-reviewed** | arXiv, NeurIPS, ICML — benchmarks et claims techniques |
| 3 | **Recherche Tier-1** | Gartner, McKinsey, Stanford HAI, OECD — données marché/adoption |
| 4 | **Presse Tier-1** | Bloomberg, Reuters, CNBC, Financial Times — news/funding/events |
| 5 | **Presse Tier-2** | TechCrunch, The Verge, Ars Technica — quand Tier-1 indisponible |
| 6 | **Bases de données startups** | Crunchbase, Sacra, PitchBook — valorisations/funding sans couverture presse |

### 6.3 Filtre de récence

| Règle | Détail |
|-------|--------|
| **Rejet dur** | Source > 2 ans pour tout claim sur le marché/adoption IA |
| **Exception** | Faits historiques (AlexNet 2012, Flash Crash 2010) et jurisprudence |
| **Préférence** | Source < 6 mois quand disponible |
| **Conflit** | Le plus récent gagne, sauf si la source plus ancienne est nettement plus autoritaire |

### 6.4 Format de citation

**Marqueurs in-text** : `[1]`, `[2]` placés directement après chaque claim chiffré.

**Footer de slide** :

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

**Exemple complet** :

```markdown
- Le marché atteint **$2 527 Mds** en 2026 [1]
- L'adoption passe de 55% à **88%** en deux ans [2]

<small>Sources : [1] [Gartner](https://www.gartner.com/...) · [2] [McKinsey](https://www.mckinsey.com/...)</small>
```

Les slides de discussion et séparateurs de section peuvent omettre les citations s'il n'y a pas de claim factuel.

### 6.5 Protocole de recherche par type de claim

| Type de claim | Sources primaires | Stratégie de recherche |
|--------------|-------------------|----------------------|
| Taille de marché / prévision | Gartner, IDC, Statista, McKinsey, CB Insights | `"[sujet] market size 2025" site:gartner.com OR site:statista.com` |
| Financiers d'entreprise | Pages IR, SEC filings, Bloomberg | `"[entreprise] revenue 2024" site:investor.[entreprise].com` |
| Stats d'adoption / enquêtes | McKinsey, Deloitte, Stanford HAI AI Index | `"[stat]" survey 2024 2025` |
| Résultats de benchmarks | Papiers originaux (arXiv), HuggingFace | `"[modèle] [benchmark]" site:arxiv.org` |
| Pricing API | Pages pricing des fournisseurs directement | Aller sur openai.com/pricing, anthropic.com/pricing, etc. |
| Événements historiques | Reuters, Bloomberg, NYT, archives judiciaires | `"[événement]" [année] site:reuters.com OR site:nytimes.com` |
| Régulation EU | EUR-Lex, Parlement Européen, CEPS | `"EU AI Act [disposition spécifique]"` |

### 6.6 Vérification des sources

Utiliser Tavily Extract pour lire la page réelle et confirmer que le chiffre correspond. Ne pas se fier aux snippets de recherche.

### 6.7 Claims non sourçables

Si un claim ne peut pas être sourcé après un effort de recherche raisonnable :

| Action | Quand |
|--------|-------|
| **Adoucir** | Remplacer le chiffre exact par "environ", "de l'ordre de", "plusieurs" |
| **Retirer** | Supprimer la stat spécifique si la slide fonctionne sans |
| **Signaler** | Marquer avec `<!-- TODO: source needed for [claim] -->` pour décision |
| **Jamais** | Inventer une source ou citer une source secondaire qui ne contient pas la donnée réelle |

### 6.8 Résolution de conflits

Quand les sources se contredisent, préférer la donnée la plus récente provenant de la source la plus réputée :

**company IR > Bloomberg/CNBC > TechCrunch > Crunchbase**

Si une source contredit le chiffre dans la slide, mettre à jour la slide pour correspondre à la meilleure source.

---

## 7. Décision PaperBanana (infographies)

**OUI — générer une infographie** quand :
- Framework avec **4+ composants** (ex : AI Canvas, CRISP-DM)
- Processus avec **3+ branches** ou embranchements (ex : arbre de décision Build vs Buy)
- Taxonomie avec **hiérarchie** (ex : types d'IA, niveaux de risque EU AI Act)
- Concept nécessitant **10+ bullets** si présenté en texte seul

**NON — rester en texte** quand :
- Comparaison simple de 2–3 items → utiliser `cols`
- Statistiques pures → utiliser un tableau ou des bullets avec **bold**
- Séquence linéaire < 4 étapes → numéroter en bullets
- Spotlight entreprise → utiliser `cols` (faits | analyse)

Détails d'utilisation de PaperBanana : voir `workflow-new-slides.md` Phase 5.

---

## 8. Pièges courants

| Piège | Solution |
|-------|----------|
| **Overflow cols** | Le linter compte les tags `<div>` — budgeter ~9 lignes de contenu réel (voir §2) |
| **Fins de ligne CRLF** | L'outil Write peut produire du CRLF — lancer `sed -i 's/\r$//' <fichier>` avant `make check` |
| **Tableau trop long** | Max 7 lignes par tableau — diviser sur 2 slides si nécessaire ("1/2" et "2/2") |
| **Trop de spotlights** | Plus de 6–7 spotlights dans un deck de 30 slides rend le rythme monotone |
| **Slide EU isolée** | Ne pas regrouper toutes les entreprises EU sur une slide — les distribuer par couche puis synthétiser |
| **Termes techniques traduits** | Utiliser le terme anglais directement : "le Fine-tuning", pas "le réglage fin *(Fine-tuning)*" |
| **Claim non sourcé** | Adoucir ("environ", "de l'ordre de") ou sourcer. Jamais inventer une source |
| **Sources snippet-only** | Toujours vérifier avec Tavily Extract la page réelle avant de citer |
| **Trop de slides** | Se rappeler que 2–3 slides bien sourcées > 8 slides superficielles |
| **Recherche sans fin** | Limiter à 30–45 min max, passer à la rédaction même si imparfait |
| **Input PaperBanana trop court** | Minimum 300 mots, structurer en 5 sections (voir workflow-new-slides.md §5.1) |
| **Caption PaperBanana = titre** | La caption est une intention communicative, pas un nom |
| **Tous les exemples EU sur une slide** | Intégrer tout au long, synthétiser en fin |
| **Pas de discussion** | Sur 7+ slides, au moins 1 question de discussion par section de 3–5 slides |

---

## 9. Checklist de vérification

### Checks automatiques

```bash
npm install           # Installer Puppeteer (une seule fois)
make check            # Overflow pixel-accurate (Puppeteer + headless Chrome)
make check-citations  # Toutes les slides de données ont des sources
make html             # Build propre, pas d'erreurs
```

### Vérifications visuelles

- [ ] La slide titre s'affiche avec le fond bleu foncé
- [ ] Les séparateurs de section s'affichent avec le fond bleu clair
- [ ] Les layouts `cols` se divisent correctement (gauche/droite)
- [ ] Les chiffres financiers correspondent aux données source

### Vérifications de conformité

- [ ] Commentaires ABOUTME présents après le front matter
- [ ] Numérotation correcte (01–XX, titre/section non numérotés)
- [ ] Corps en français + termes techniques en anglais
- [ ] Attribution footer appropriée pour les sources (§3.1)
- [ ] Citations `[N]` + `<small>Sources</small>` sur chaque slide de données (§6.4)
- [ ] Sources vérifiées : chaque URL pointe vers la donnée citée
- [ ] Contexte EU/France : au moins 1 exemple européen intégré (pas isolé)
- [ ] Questions de discussion = scénarios concrets, pas abstraits
- [ ] Infographies lisibles à taille demi-slide, éléments clés labelés
