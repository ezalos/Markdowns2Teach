---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Session 3 · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: ""
---

<!-- ABOUTME: Informations pratiques pour les sessions 4 et 5 — logistique 42, intervenants, QCM et rappels projet. -->
<!-- ABOUTME: Deck d'ouverture de la Session 3, avant les decks thématiques A et B. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->

# Deep Tech & Machine Learning

## Informations pratiques — Sessions 4 & 5

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

# 01 — Prochaine séance : École 42

**Lundi 23 mars** · **18h00–21h00** (30 min plus tard que d'habitude)

**Adresse** : 96 boulevard Bessières, 75017 Paris

Pourquoi 42 ? Pour accueillir un intervenant en fauteuil roulant dans un lieu accessible.

L'**École 42** est une école d'informatique fondée en 2013, reconnue pour sa pédagogie par projets et son campus ouvert 24/7. C'est là que votre enseignant a fait ses études et dirigé le laboratoire d'intelligence artificielle.

---

# 02 — Comment venir à 42

**Depuis le 14 rue Cujas** (~35 min) :

- **Option 1** : RER B → métro 14
- **Option 2** : Métro 4 → métro 14

**Pièce d'identité obligatoire** pour accéder au campus.

**Accueil** : des personnes seront à l'entrée de **17h30 à 18h15** pour vous guider jusqu'à l'amphi. Évitez d'arriver en retard !

**Visite du campus** : profitez d'une pause pour découvrir 42, guidés par des bénévoles de l'école.

> Le cours démarre à **18h00** (pas 17h30) pour vous laisser le temps d'arriver.

---

# 03 — Intervenant S4 : Maxime Jégat

![bg right:30% contain](assets/Maxime_Jegat.jpeg)

**Founder @ Hoox** · AI UGC for e-commerce

Hoox aide les acteurs e-commerce à mieux convertir grâce à l'IA :

- Vidéos avec des **avatars IA ultra-réalistes**, sans tournage ni acteurs
- **Coût réduit de 40 à 60%** par rapport à un UGC traditionnel
- Test A/B à une échelle impossible en production classique
- **100+ clients** : Smartbox, Snapchat, Cheerz…

hoox.video · [LinkedIn](https://www.linkedin.com/in/maximejegat/)

> Préparez vos questions sur l'AI UGC, la conversion e-commerce, ou l'entrepreneuriat dans l'IA.

---

# 04 — Intervenant S4 : Tanguy Auffret

![bg right:30% contain](assets/Tanguy_Auffret.jpeg)

**Business Partner for Early-Stage Entrepreneurs** · HEC Paris

Au service des entrepreneurs et de l'écosystème startup depuis près de 10 ans :

- Accompagnement de **100+ startups** depuis 2017
- Spécialiste en **stratégie, finance et opérations**
- Programmes de soutien aux startups pour fonds d'investissement et incubateurs
- Conviction : **l'IA va changer les règles du jeu**

[LinkedIn](https://www.linkedin.com/in/tanguy-auffret-strategy-finance-startups/)

> Préparez vos questions sur le lancement de startup, la levée de fonds, ou la stratégie business dans l'IA.

---

<!-- _class: compact -->

# 05 — Intervenante S5 : Juliette Lefay

![bg right:30% contain](assets/Juliette_Lefay.jpeg)

**Fondatrice & Productrice** · Phygital Studio · Super Organique

Ingénieure de formation, elle entreprend à la croisée de l'Art, la Nature et la Technologie :

- **Phygital Studio** : art numérique interactif et immersif
- Clients : Yves Rocher, La Seine Musicale, Centquatre, Min. de la Culture
- **Super Organique** : événements de transmission art-science
- **Plant Being** : installation traduisant les signaux des plantes en sons et lumières

phygital-studio.fr · [LinkedIn](https://www.linkedin.com/in/juliette-lefay-phygital-studio/)

> Préparez vos questions sur l'entrepreneuriat tech-art ou la création d'un studio créatif.

---

# 06 — Rappel : QCM final (Session 5)

Le QCM aura lieu en **Session 5** (30 mars), couvrant l'ensemble du cours.

| | |
|---|---|
| **Questions** | 20 questions à choix multiples |
| **Propositions** | 5 choix par question |
| **Durée** | 30 minutes |
| **Supports** | Aucun document autorisé, aucun téléphone |
| **Matériel** | **Apportez un stylo !** Calculatrice basique OK (+-×÷) |

Le QCM évalue la **compréhension**. Les éventuels calculs seront simples.

> Révisez les concepts clés de chaque session, pas les détails techniques.

---

<!-- _class: cols -->

# 07 — Rappel : Présentations projet (Session 5)

<div class="left">

**Poids fort**

- La démo fonctionne en live
- Je peux interagir avec votre système rapidement
- Dataset de test solide (20+ exemples)
- Au moins 2 modèles comparés

</div>
<div class="right">

**Poids modéré**

- Présentation + démo tient en 4 min
- Produit expliqué clairement
- Choix du modèle justifié

**Soumission** : workflow + dataset le vendredi 28 mars, présentation avant le cours → develle.louis@gmail.com

</div>

---

# 08 — Question S2 : Tokens en chinois vs anglais

**Votre question** : un LLM consomme-t-il plus ou moins de tokens en chinois qu'en anglais ?

Le chinois est **logographique** — chaque caractère (我, 爱) porte un sens complet. En anglais, un mot peut coûter plusieurs tokens ("un-believ-able" → 3 tokens).

| Modèle | Chinois vs Anglais |
|---|---|
| **Qwen 3** (151K vocab, optimisé CJK) | Chinois ~30–50% **moins cher** |
| **Llama 1–2** (32K vocab, anglais) | Chinois ~2–4× **plus cher** (UTF-8 fallback) |
| **Llama 3** (128K vocab) | Comparable, léger désavantage chinois |
| **GPT-4 / Claude** | Chinois légèrement moins cher |

> **Impact business** : un prompt chinois coûte 500 tokens sur Qwen mais 1 500–2 000 sur Llama 2. Le choix du modèle change le coût pour les apps non-anglophones.

---

<!-- _class: section -->

# Passons au contenu

## Session 3A — RAG & Agents IA
