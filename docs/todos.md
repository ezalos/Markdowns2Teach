
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



## Course content

I would like to change the course order a bit : 
Deck-A : First I would like to define AI, 
and then make a general slide about approach the different ways to categorize AI : 
- By their algorithm type (stat/ml/dl/gen-ai)
- By their label type (supervise/unsup/rl)
- By their data type (tabulaire/text/image/...)
- task type (classif / regression / summarization / object detection) -> should be with a hf screenshot of all the possible task that can be selected

And then we go through each to give details with 1-3 slides 

- Algo type for dl give hte keras link : https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.20188&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false
- In supervised learning -> give an example with LR

I need to prepare the g-sheet

I should make sur S2 has evaluation in it.

## Nice things which could be added



- [ ] Difference between the different type of training done (pretrianing + instruct + thinking + ...) and then what can be done later : finetuning + LoRA

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