<!-- ABOUTME: QCM d'évaluation pour la Session 1 — IA Générative, taxonomie IA, architectures, LLMs. -->
<!-- ABOUTME: 12 questions à choix multiples avec réponses détaillées et explications en français. -->

# QCM — Session 1 : Comprendre l'IA en 2026

## IA Générative · Taxonomie IA · Architectures · Reasoning Models · Éthique

---

### Q1 — Generative AI vs Discriminative AI

Quelle est la différence fondamentale entre une IA **générative** et une IA **discriminative** ?

- A) L'IA générative est plus récente, l'IA discriminative est obsolète
- B) L'IA générative crée du contenu nouveau, l'IA discriminative classe ou prédit à partir de données existantes
- C) L'IA générative utilise des GPUs, l'IA discriminative fonctionne sur CPU
- D) L'IA générative est toujours plus performante que l'IA discriminative

<details><summary>Réponse</summary>

**B)** — L'IA **générative** (GPT, Claude, DALL-E) produit du contenu nouveau : texte, images, code, audio. L'IA **discriminative** (Supervised Learning classique) prend une entrée et produit une classification ou prédiction : email → spam/pas spam, image → chat/chien. Les deux coexistent — le Supervised Learning reste la technologie IA la plus déployée et la plus rentable en entreprise.

</details>

---

### Q2 — Les 3 familles de tâches LLM

Un LLM excelle dans trois grandes familles de tâches. Lesquelles ?

- A) Calcul, stockage, réseau
- B) Writing (écriture), Reading (analyse), Chatting (conversation)
- C) Classification, regression, clustering
- D) Entraînement, inférence, fine-tuning

<details><summary>Réponse</summary>

**B) Writing, Reading, Chatting** — **Writing** : brainstorming, rédaction, traduction, génération de code. **Reading** : résumé, extraction d'information, sentiment analysis, relecture. **Chatting** : chatbot client, assistant interne, tuteur pédagogique. Cette classification aide l'entrepreneur à identifier les use cases LLM pertinents pour son business.

</details>

---

### Q3 — Hallucination

Un avocat utilise ChatGPT pour rédiger un mémoire juridique. Le LLM cite l'arrêt "Varghese v. China Southern Airlines" avec numéro de dossier et date. Que s'est-il probablement passé ?

- A) Le LLM a trouvé l'arrêt dans sa base de données juridique
- B) Le LLM a effectué une recherche web en temps réel
- C) Le LLM a "halluciné" — il a inventé une référence qui n'existe pas, avec une grande confiance
- D) L'arrêt existe mais dans une autre juridiction

<details><summary>Réponse</summary>

**C)** — C'est un cas réel : un avocat new-yorkais a soumis un mémoire contenant 6 arrêts inventés par ChatGPT, avec des numéros de dossier fictifs. Le LLM ne "sait" pas ce qu'il ne sait pas — il génère du texte statistiquement plausible. L'hallucination est un risque majeur : le LLM peut inventer des faits, des citations, des chiffres avec une apparence de certitude totale.

</details>

---

### Q4 — Knowledge Cutoff

Un utilisateur demande à un LLM : "Quel est le cours de l'action Tesla aujourd'hui ?" Le modèle répond avec un chiffre précis. Que faut-il en penser ?

- A) Le chiffre est fiable car les LLMs sont connectés aux marchés financiers
- B) Le chiffre est probablement inventé — le LLM a un Knowledge Cutoff et ne connaît pas les données en temps réel
- C) Le chiffre est correct si le modèle a été mis à jour récemment
- D) Le chiffre est correct car les LLMs ont accès à Internet par défaut

<details><summary>Réponse</summary>

**B)** — Les LLMs ont un **Knowledge Cutoff** : leur connaissance est figée à la date de fin d'entraînement. Sans accès web explicite (browsing activé), ils ne connaissent pas les événements récents, les cours de bourse actuels, ni les dernières actualités. Un LLM qui donne un cours de bourse "aujourd'hui" l'invente en se basant sur des patterns statistiques.

</details>

---

### Q5 — Taxonomie IA

Quelle est la relation correcte entre ces concepts ?

- A) AI ⊃ GenAI ⊃ Deep Learning ⊃ Machine Learning
- B) Machine Learning ⊃ Deep Learning ⊃ AI ⊃ GenAI
- C) AI ⊃ Machine Learning ⊃ Deep Learning ⊃ GenAI
- D) GenAI ⊃ AI ⊃ Machine Learning ⊃ Deep Learning

<details><summary>Réponse</summary>

**C) AI ⊃ Machine Learning ⊃ Deep Learning ⊃ GenAI** — L'Intelligence Artificielle est le domaine le plus large. Le Machine Learning est un sous-ensemble de l'IA (apprentissage par les données). Le Deep Learning est un sous-ensemble du ML (réseaux de neurones profonds). La Generative AI est un sous-ensemble du Deep Learning (génération de contenu). Chaque niveau imbrique le précédent.

</details>

---

### Q6 — AI Winters

Qu'est-ce qui a causé les "AI Winters" (périodes de désillusion et de chute des investissements en IA) ?

- A) Les ordinateurs n'étaient pas assez puissants et les résultats ne correspondaient pas aux promesses
- B) L'IA a été déclarée dangereuse et interdite par les gouvernements
- C) Les chercheurs en IA ont tous changé de domaine
- D) Les entreprises ont trouvé que l'IA était trop bon marché pour être rentable

<details><summary>Réponse</summary>

**A)** — Les AI Winters (années 1970-80, puis 1990s) ont été causés par un décalage entre les **promesses** (machines pensantes) et les **résultats** (capacités très limitées). En 1969, Minsky & Papert ont montré les limites du Perceptron. Les financements ont chuté, la recherche a stagné. La renaissance est venue en 2012 avec AlexNet qui a écrasé la compétition ImageNet, prouvant que le Deep Learning fonctionnait — grâce aux GPUs et aux grandes quantités de données.

</details>

---

### Q7 — Architecture matching

Vous devez choisir une architecture pour chacun de ces cas. Quel matching est **correct** ?

- A) CNN → texte, RNN → images, Transformer → audio uniquement
- B) CNN → images/vidéo, RNN → séquences temporelles, Transformer → multi-modal (texte, image, audio)
- C) CNN → données tabulaires, RNN → images, Transformer → texte uniquement
- D) Toutes les architectures sont interchangeables, seul le volume de données compte

<details><summary>Réponse</summary>

**B)** — Le **CNN** (Convolutional Neural Network) excelle sur les images et vidéos : il détecte des patterns visuels hiérarchiques (bords → formes → objets). Le **RNN/LSTM** est spécialisé dans les séquences (texte, audio, séries temporelles) grâce à sa mémoire temporelle — mais il a été largement remplacé par le Transformer pour le texte depuis 2017. Le **Transformer** est l'architecture la plus polyvalente : texte, image, audio, multi-modal.

</details>

---

### Q8 — Transformer

Qu'est-ce qui a rendu l'architecture **Transformer** révolutionnaire par rapport aux architectures précédentes ?

- A) Elle utilise moins de données d'entraînement
- B) Le mécanisme d'**Attention** permet de traiter tous les éléments d'une séquence en parallèle
- C) Elle ne nécessite pas de GPU
- D) Elle a été inventée par OpenAI

<details><summary>Réponse</summary>

**B)** — Le papier "Attention Is All You Need" (Google, 2017) a introduit le mécanisme d'**Attention** : au lieu de traiter une séquence mot par mot (comme les RNN), le Transformer peut "regarder" tous les mots simultanément et pondérer leur importance relative. Cela permet la parallélisation massive sur GPU et la capture de dépendances à longue distance. C'est la base de GPT, Claude, Mistral et de tous les LLMs modernes.

</details>

---

### Q9 — Principes de Prompting

Lequel de ces deux prompts est le **meilleur** pour obtenir un résumé d'article ?

**Prompt A** : "Résume cet article."

**Prompt B** : "Résume cet article en 5 bullet points maximum, en français, en gardant uniquement les faits chiffrés et les conclusions principales. Format : une phrase par point."

- A) Prompt A — plus court, donc plus efficace
- B) Prompt B — plus spécifique, donc le résultat sera plus prévisible et utile
- C) Les deux sont équivalents — le LLM comprend l'intention
- D) Prompt A — le LLM doit être libre de choisir le format

<details><summary>Réponse</summary>

**B) Prompt B** — Le premier principe du Prompting est d'être **détaillé et spécifique**. Le Prompt B précise : le format (bullet points), la longueur (5 max), la langue (français), le focus (faits chiffrés + conclusions), et la structure (une phrase par point). Le LLM a des instructions claires et produira un résultat prévisible. Le Prompt A laisse trop de place à l'interprétation.

</details>

---

### Q10 — Diffusion Models

Comment fonctionnent conceptuellement les **Diffusion Models** (DALL-E, Midjourney, Stable Diffusion) pour générer des images ?

- A) Ils recherchent et assemblent des morceaux d'images existantes
- B) Ils partent d'une image de bruit aléatoire et apprennent à la "débruiter" progressivement pour créer l'image souhaitée
- C) Ils dessinent pixel par pixel de gauche à droite, comme un scanner
- D) Ils copient des images d'Internet et les modifient légèrement

<details><summary>Réponse</summary>

**B)** — Les Diffusion Models fonctionnent en deux phases. **Entraînement** : on prend une image, on ajoute du bruit progressivement jusqu'à obtenir du bruit pur, et le modèle apprend à inverser ce processus. **Génération** : on part de bruit aléatoire et on applique le processus inverse de débruitage, guidé par le prompt textuel. Ce n'est pas du collage ni de la copie — le modèle génère des pixels originaux.

</details>

---

### Q11 — Reasoning Models

Quelle est la différence principale entre un **Reasoning Model** (o3, o4-mini) et un LLM standard (GPT-4o) ?

- A) Les Reasoning Models sont plus rapides et moins chers
- B) Les Reasoning Models génèrent une chaîne de raisonnement interne (Extended Thinking) avant de répondre, ce qui réduit les erreurs
- C) Les Reasoning Models n'ont pas de Knowledge Cutoff
- D) Les Reasoning Models remplacent totalement les LLMs standards

<details><summary>Réponse</summary>

**B)** — Les Reasoning Models utilisent l'**Extended Thinking** : avant de donner une réponse finale, ils génèrent une chaîne de raisonnement étape par étape (Chain-of-Thought) et vérifient leur propre logique. Cela réduit les hallucinations et améliore les performances sur les tâches complexes (mathématiques, logique, code). En contrepartie, ils sont plus lents et plus coûteux. Sur AIME 2024 (mathématiques olympiade) : GPT-4o ≈ 26%, o1 = 74%, o3 = 92%.

</details>

---

### Q12 — Limites des LLMs

Parmi ces affirmations, lesquelles sont des **vraies limitations** des LLMs ? (plusieurs réponses possibles)

- A) Ils ne peuvent pas accéder à des données postérieures à leur Knowledge Cutoff
- B) Ils peuvent inventer des faits avec une grande confiance (hallucinations)
- C) Ils ne savent pas faire de calcul mathématique exact de manière fiable
- D) Toutes les réponses ci-dessus

<details><summary>Réponse</summary>

**D) Toutes les réponses ci-dessus** — Les trois sont de vraies limitations. **A)** Knowledge Cutoff : sans accès web, le LLM ne connaît pas les événements récents. **B)** Hallucinations : le LLM génère du texte statistiquement plausible, pas factuellement vérifié — il peut inventer des références, des chiffres, des noms. **C)** Calcul : les LLMs sont des modèles de langage, pas des calculatrices — ils peuvent se tromper sur des multiplications simples (les Reasoning Models améliorent ce point mais ne l'éliminent pas complètement).

</details>
