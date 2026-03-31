---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---
<!-- ABOUTME: Context Engineering avancé — niveaux de réponse d'outil, Peripheral Vision, Form Factors, Composabilité. -->
<!-- ABOUTME: Deck de référence (extra) pour étudiants M2 IMT&E Paris 1 souhaitant approfondir le Context Engineering. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Context Engineering : approfondissement

## Deck complémentaire — Session 3B

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: img-right -->

# 01 — Les 4 niveaux de réponse d'outil

**4 niveaux** de maturité pour les réponses d'outils [1] :

- **L1** — Chunks bruts (texte sans metadata)
- **L2** — Metadata source (document, page, URL)
- **L3** — Multi-modal (tableaux HTML, images + OCR)
- **L4** — Facets (agrégations, comptages, catégories)

> "Les réponses d'outils enseignent à l'agent **comment penser les données**." C'est du meilleur formatage, pas de la reconstruction [1].

![bg right:55% contain](../session-03/assets/infographics/tool-response-levels.png)

<small>Sources : [1] [Jason Liu — Beyond Chunks](https://jxnl.co/writing/2025/08/27/facets-context-engineering/)</small>

---

<!-- _class: img-right -->

# 02 — Peripheral Vision : voir au-delà du top-K

Le RAG renvoie les **top-K chunks**. Mais l'agent ne voit pas ce qu'il manque.

**Faceted Search** = agrégations metadata en plus des résultats [1] :
- "API timeout" → 5 résultats "Done"
- Facets : **15 tickets "Open"** masqués
- L'agent filtre → couverture complète

> L'agent utilise les facets pour **construire un plan d'exploration** stratégique [1].

![bg right:55% contain](../session-03/assets/infographics/peripheral-vision.png)

<small>Sources : [1] [Jason Liu — Beyond Chunks](https://jxnl.co/writing/2025/08/27/facets-context-engineering/)</small>

---

# 03 — 3 Form Factors : quel agent construire ?

Avant l'architecture technique, choisissez votre **Form Factor** [1] :

| Form Factor | Ce que c'est | KPI |
|---|---|---|
| **Chatbot** | Conversation + outils. L'humain supervise | Satisfaction, résolution |
| **Workflow** | Moteur side-effect, pas d'UI. Contrats, tickets, factures | Complétion, précision |
| **Research Artifact** | Rapports, tableaux, résumés structurés | Précision, exploitabilité |

> **"Toutes les autres décisions techniques — design des outils, prompts, orchestration — dépendent de ce choix."** Choisissez le Form Factor AVANT de coder [1].

<small>Sources : [1] [Jason Liu — Form Factors](https://jxnl.co/writing/2025/09/04/context-engineering-agent-frameworks-and-form-factors/)</small>

---

<!-- _class: compact-table -->

# 04 — Composabilité : chaque niveau est un outil

**5 niveaux d'autonomie** — chaque niveau devient un outil pour les niveaux supérieurs [1] :

| Niveau | Quoi | Exemple |
|---|---|---|
| **L0 — Deterministic** | Code classique (if/else) | Validation, formatage |
| **L1 — AI Function** | 1 appel LLM, 1 tâche | Extraction, classification |
| **L2 — Prompt Chain** | Appels séquentiels, ordre fixe | Rédiger → Critiquer → Réviser |
| **L3 — Graph State Machine** | Branches conditionnelles | L'IA choisit le chemin |
| **L4 — Tool-Calling Loop** | Boucle agent classique | Réservé aux cas imprévisibles |

> **L'insight clé** : un script L0 → outil pour L1 → outil pour L2 → outil pour L4. C'est **pourquoi** l'échelle Anthropic dit "commencez simple" [1].

<small>Sources : [1] [Jason Liu — Form Factors](https://jxnl.co/writing/2025/09/04/context-engineering-agent-frameworks-and-form-factors/)</small>

---

# 05 — Discussion : Context Engineering en action

> Vous construisez un **agent de veille réglementaire** pour des cabinets d'avocats. Il doit scanner les nouvelles lois, les comparer aux dossiers clients, et produire un résumé hebdomadaire.

**Questions pour la classe** :

- Quel **Form Factor** choisissez-vous ? (Chatbot, Workflow, ou Research Artifact ?)
- À quel **niveau de composabilité** commencez-vous ? Que mettez-vous en L0 (deterministic) ?
- Comment structureriez-vous les réponses des outils pour donner de la **Peripheral Vision** à l'agent ?
