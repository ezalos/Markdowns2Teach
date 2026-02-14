# Guide de création de decks

<!-- ABOUTME: Conventions et bonnes pratiques pour construire un deck pédagogique Marp. -->
<!-- ABOUTME: Couvre la structure, les conventions Marp, les règles de contenu et la vérification. -->

## Formule de structure

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

## Budget de contenu par slide

| Type de slide | Lignes de contenu max | Notes |
|---------------|----------------------|-------|
| Slide standard | **15 lignes** | Seuil du linter `make check` |
| Slide avec sources | **~13 lignes** | La ligne `<small>Sources</small>` coûte ~1 ligne |
| Slide `cols` | **~8–9 lignes par colonne** | Les tags `<div>` comptent comme lignes de contenu |

## Front matter Marp

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
- Le footer liste les attributions :
  - Multi-sources : `"Sources multiples · DeepLearning.AI CC BY-SA 2.0"`
  - Principalement Andrew Ng : `"Adapté de Generative AI for Everyone par Andrew Ng · DeepLearning.AI · CC BY-SA 2.0"`
  - Recherche originale : `"Recherche [Topic] 2024–2026 · Données publiques"`

## Commentaires ABOUTME

Chaque fichier `.md` commence (après le front matter) par deux commentaires :

```markdown
<!-- ABOUTME: Description brève du contenu du deck. -->
<!-- ABOUTME: Public visé et approche pédagogique. -->
```

## Types de slides

### Slide titre

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

### Séparateur de section

```markdown
<!-- _class: section -->

# Nom de la section
```

### Slide à deux colonnes

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

Attention : éviter les `###` à l'intérieur des colonnes — ils consomment une ligne sans apport visuel à cette densité.

### Slide de discussion

```markdown
# XX — Discussion : [Sujet]

> [Scénario concret — mettre les étudiants dans la peau de l'entrepreneur]

**Questions pour la classe** :
- [Question spécifique 1]
- [Question spécifique 2]
```

Bonnes questions de discussion :
- Présentent un vrai trade-off (coût vs souveraineté, vitesse vs contrôle)
- Référencent des entreprises vues dans les slides précédentes
- N'ont pas de réponse unique "correcte"
- Se connectent au contexte entrepreneurial des étudiants

## Numérotation

- Slides de contenu : `# 01 — Titre` (2 chiffres, tiret cadratin, redémarre par fichier)
- Slides titre et séparateurs de section : **NON numérotés**
- Permet de référencer facilement : "déplace la slide 03 après la 05"

## Règles linguistiques

- **Corps de texte** : français
- **Termes techniques** : anglais, utilisés directement sans traduction
  - ✅ "Le Supervised Learning est la technique la plus déployée..."
  - ❌ "L'apprentissage supervisé *(Supervised Learning)*"
- Bullet points concis, pas de longs paragraphes
- Tableaux pour les comparaisons (input/output, outils)
- Blockquotes (`>`) pour les callouts, tips et takeaways

## Cadrage du contenu

- **Business-first** : cadrer les concepts pour des entrepreneurs, pas des chercheurs
- **Questions d'engagement** : 1–2 questions de discussion par section majeure
- **Cas réels 2024–2026** : éviter les exemples datés
- **Contexte EU/France** : intégrer les entreprises françaises et européennes tout au long du deck (pas isolées sur une seule slide)

## Pièges courants

| Piège | Solution |
|-------|----------|
| Overflow `cols` | Le linter compte les tags `<div>` comme lignes — ne budgeter que 10 lignes de contenu réel |
| Fins de ligne CRLF | L'outil Write peut produire du CRLF — lancer `sed -i 's/\r$//' <fichier>` avant `make check` |
| Tableau trop long | Max 7 lignes par tableau — diviser sur 2 slides si nécessaire ("1/2" et "2/2") |
| Trop de spotlights | Plus de 6–7 spotlights dans un deck de 30 slides rend le rythme monotone |
| Slide EU isolée | Ne pas regrouper toutes les entreprises EU sur une slide — les distribuer par couche puis synthétiser |

## Checklist de vérification

Avant de considérer un deck comme terminé :

```bash
make check            # Linter overflow (seuil 15 lignes)
make check-citations  # Toutes les slides de données ont des sources
make html             # Build propre, pas d'erreurs
```

Vérifications visuelles :
- [ ] La slide titre s'affiche avec le fond bleu foncé
- [ ] Les séparateurs de section s'affichent avec le fond bleu clair
- [ ] Les layouts `cols` se divisent correctement (gauche/droite)
- [ ] Les chiffres financiers correspondent aux données source
- [ ] Commentaires ABOUTME présents après le front matter
- [ ] Numérotation correcte (01–XX, titre/section non numérotés)
- [ ] Corps en français + termes techniques en anglais
- [ ] Attribution footer appropriée pour les sources
- [ ] Questions de discussion = scénarios concrets, pas abstraits
