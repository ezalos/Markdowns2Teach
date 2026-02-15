
# Engineering

- [x] Updated the directory structure (session-based layout under `slides/session-XX/`)
- [x] Dist split by file type (`dist/html/`, `dist/pptx/`)
- [x] GDrive sync via rclone (`make sync` → `gdrive:Travail/Formations/Sorbonne/AutoDecks`)
- [x] Commit the changes to the repo (still ignoring large files / pdf / ...)

Also please reorganize dist to be split by file type :
  - dist
    - html
      - xxxx.html
    - pptx
      - xxxx.pptx


Please create a sync of the local slides to GDrive easily (you can use uvx if it helps)
  - Make sync : dist/pptx -> MonDrive/Travail/Formations/Sorbonne/AutoDecks


# Content

## No-code tools

- Some n8n video ? Will need to show what's a JSON, and the javascript notation to select a variable
- Explain what is an API and a WebHook
- Show the HF interface
- Show some architecture diagrams (n8n workflows ?)




## Nice things which could be added

- [x] Make sure RAG is explained in architecture term
- [ ] Nvidia Moat and CUDA, get back this : https://newsletter.semianalysis.com/p/nvidiaopenaitritonpytorch
- [ ] Nvidia Moat and in light of Google TPU move
- [ ] NVIDIA moat deep research — semianalysis article is 2023, needs update for Blackwell/ROCm/TPU v5 era

- [ ] Add State of AI report to it !!!!
- [ ] Speak about Claude Code revolutionnizing the way we code + OpenClaw

- [ ] Book from Chip Huyen : ML-OPs & ML-Engineering
- [ ] LLM Evaluation chapter — needs research (Chip Huyen AIE Ch 3-4 as starting point)
- [ ] Regression metrics slides (MAE, MSE, RMSE) — add to Session 3A




# Things to research

- [ ] DO a N8N tutorial with hf usage
- [ ] Prepare a N8N course with hf usage
- [ ]


Huggingface spaces :
- Interesting I would like to show it to them


Pour la veille techno :
- AI News is sooo good
- https://www.wizwand.com/




## Evaluation

### QCM

Preparer les QCMs
- [x] Session 1 QCM (`docs/qcm/session-01-qcm.md`)
- [x] Session 3 QCM (`docs/qcm/session-03-qcm.md`)
- [ ] QCMs for Sessions 2, 4, 5

Preparer un deck pour me presenter et presenter:
- [x] Intro deck (`slides/session-01/0-intro-cours.md`)
- le cours complet dans ses grandes lignes
- les evaluations qu'il y aura
- les projets qu'il y aura



Error metrcis (great qcm for a given pbm) :
- Classification
- Regression


Tasks types (great qcm for a given pbm) :
- Classification
- Regression
- Computer vision types



Preparer des quesitons a ajouter au cours




![bg right:45%](assets/) [1]

<small>Sources : [1] [Gartner](link) </small>


# CORRECTIONS : 

Ma slide d'intro, j'enseigne a  Master 2 Innovation Management des Technologies et Entrepreneuriat (IMT&E) à Paris 1 Panthéon-Sorbonne (et non juste Sorbonne). Et mon cours est bien Deep Tech & Machine Learning (UE3)


### Comments on : session-01/A-genai-fondamentaux.md

Slides numbers should be corrected

After : 

# 09 — Les grandes familles de l'IA

the big paragraph should become a little sheet

It would be a great occasion to introduce the content about the different types of ML models 

.

Also there is a bunch of informations said which do not have rigourous source. I would really like you to go find them all and update them.

Also I sometimes put multiple images by slide,. i would love you to either fit them all on a same slide, or to duplicate the slides.