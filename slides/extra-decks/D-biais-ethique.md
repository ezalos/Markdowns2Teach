---
marp: true
theme: sorbonne
paginate: true
header: "Deep Tech & ML (UE3) — Extra · M2 IMT&E · Paris 1 Panthéon-Sorbonne"
footer: "Sources multiples"
---

<!-- ABOUTME: Introduction aux biais et à l'éthique dans l'IA — biais de genre, toxicité, responsabilité légale. -->
<!-- ABOUTME: Module court optionnel pour sensibiliser dès le jour 1, approfondi en Session 5. -->

<!-- _class: title -->
<!-- _paginate: skip -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Biais et éthique : introduction

## Extra — L'IA responsable dès le jour 1

M2 IMT&E · Paris 1 Panthéon-Sorbonne · 2026

---

<!-- _class: section -->

# Biais, éthique et IA responsable

## Ethics and Responsible AI

---

# 01 — Biais et toxicité dans les LLMs

Les LLMs *reflètent les biais* présents dans leurs données d'entraînement :

*Exemple de biais de genre* :
- "The surgeon walked to the parking lot and took out *his* car keys."
- "The nurse walked to the parking lot and took out *her* phone."

| Enjeu | Question clé | Exemple |
|---|---|---|
| *Fairness* | Les données sont-elles représentatives ? | Biais de genre dans le recrutement |
| *Vie privée* | Quelles données collecte-t-on ? | RGPD et droit à l'oubli |
| *Contrôle* | Qui est responsable des décisions ? | Le chatbot Tay de Microsoft (2016) [1] |

> *Pour les entrepreneurs* : l'éthique n'est pas un frein — c'est un *avantage compétitif*. Les entreprises qui intègrent la responsabilité IA dès le départ sont mieux positionnées face au EU AI Act.

<small>Sources : [1] [The Verge](https://www.theverge.com/2016/3/24/11297050/microsoft-tay-ai-chatbot-racist)</small>

---

# 02 — Discussion : biais et responsabilité

<!-- INSTRUCTOR: Réponses aux questions de discussion :

Q1 — Responsabilité légale : responsabilité PARTAGÉE sous le EU AI Act.
- Le FOURNISSEUR (provider) doit : évaluation de conformité, documentation technique, surveillance post-marché (Art. 16-22)
- Le DÉPLOYEUR (employer/startup) doit : utiliser selon les instructions, assurer la supervision humaine, surveiller les performances, suspendre en cas de risque (Art. 26)
- En pratique : l'employeur est responsable du CHOIX du système et de son absence de tests. Le fournisseur est responsable des biais connus non documentés.
- La Directive Responsabilité IA (proposée 2022, retirée pour révision) prévoyait une présomption réfutable de causalité — la charge de la preuve passerait au provider/deployer.

Q2 — Tester le biais avant déploiement :
- Parité démographique : comparer les taux de sélection par groupe (ex : % femmes vs % hommes shortlistés)
- Règle des 4/5 : si un groupe est sélectionné à moins de 80% du taux du groupe le plus favorisé → impact disparate
- Equalized Odds : vérifier que les taux de vrais positifs ET faux positifs sont égaux entre groupes
- Test contrefactuel : soumettre des CV identiques en changeant uniquement le nom ("Jean Dupont" vs "Fatima Benali") — les scores changent-ils ?
- Outils : Microsoft Fairlearn (open source), IBM AI Fairness 360
- Le EU AI Act exige ces tests dans l'évaluation de conformité pour les systèmes à haut risque

Q3 — Obligations haut risque (EU AI Act, Annexe III point 4a) :
- Le recrutement IA est EXPLICITEMENT listé comme haut risque (Art. 6(2) + Annexe III)
- Provider : évaluation de conformité, système de gestion des risques, gouvernance des données, documentation technique, marquage CE
- Deployer : supervision humaine par personnel compétent, surveillance des performances, qualité des données d'entrée, informer les candidats qu'ils sont soumis à une décision IA, conserver les logs ≥ 6 mois
- Échéance : obligations applicables à partir du 2 août 2026
- Sources : artificialintelligenceact.eu/article/6/ et /annex/3/
-->

> *Scénario* : votre startup utilise un LLM pour présélectionner des CV. Vous découvrez que le modèle favorise systématiquement les candidats masculins pour les postes techniques.

*Questions pour la classe* :

- Qui est légalement responsable ? Vous ? Le fournisseur du modèle ? Les deux ?
- Comment tester le biais *avant* de déployer en production ?
- Le EU AI Act classe le recrutement IA en « haut risque » — quelles obligations en découlent ?

> L'éthique de l'IA sera approfondie en Session 5. Mais dès aujourd'hui, retenez : *tester le biais avant de déployer, pas après*.

---

# 03 — Rendez-vous en Session 5

Ce module d'introduction sera approfondi lors de la *Session 5 — Régulation & IA responsable* :

- **EU AI Act** : les 4 niveaux de risque, le calendrier, les coûts de conformité
- **RGPD et IA** : interaction entre les deux cadres réglementaires
- **Cas de biais réels** : Amazon (recrutement), COMPAS (justice), banques (crédit)
- **Impact environnemental** : le coût carbone de l'entraînement des LLMs
- **Frameworks d'IA responsable** : comment intégrer l'éthique dans votre projet

> *D'ici là* : à chaque fois que vous utilisez un LLM pour prendre une décision, demandez-vous : "Si cette décision était prise par un humain, serait-elle défendable ?"
