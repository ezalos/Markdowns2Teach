
# Engineering 

You need to commit the changes to the repo (still ignoring large files / pdf / ...)

I notably updated the directory structre (you should update readme as well): 
  - docs 
    - sources
      - courses (was previously ./refecences)
        - AndrewNg
        - KevinVU
    - research
    - plans 
  - slides 
  - dist

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

- 

## Nice things which could be added

- [ ] Make sure RAG is explained in architecture term
- [ ] Nvidia Moat and CUDA, get back this : https://newsletter.semianalysis.com/p/nvidiaopenaitritonpytorch 
- [ ] Nvidia Moat and in light of Google TPU move

- [ ] Add State of AI report to it !!!!
- [ ] Speak about Claude Code revolutionnizing the way we code + OpenClaw


- [ ] Book from Chip Huyen : ML-OPs & ML-Engineering

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
Preparer un deck pour me presenter et presenter:
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


# Course plan again

What seems good : 

3 hours = 
- Section A (Slide deck) - 45 mins + 15 mins break
- Section B (Slide deck) - 45 mins + 15 mins break
- Section C (Either Practice | QCMs | Intervenant externe |  ) 45 mins + 15 mins bonus


## 1 - Course Intro AI : 

15 min intro about : 
- Who I Am
- The course plan
- The rules and QCM + Housework

- A : What's AI ?
  - Not AI
  - Rule based
  - Pure stats
  - ML algorithms
    - My special Notebooks about Linear Regression
  - DL
    - Showcase of different models : 
      - Text classif 
      - Computer Vision
      - 
  - GenAI
    - Text
    - Image
    - Sound
    - Video
    - Robot
- B : Dive on examples
  - Linear Regression
  - Random Forest
- C : How to evaluate AI ?
  - We evaluate differently depending on the system
    - Classification
    - Regression
    - Computer Vision tasks
    - LLM evaluations
  - Cost
  - legale
  - acccessibilite technique
  - Open-Source or as-a-service


Let's make together : 
- An N8n takes input send it to more


## 2 - Course Deeper in AI : 

- ML systems 
  - API / Local or Cloud deployment / Database or S3 / Monitoring
  - Showing : 
    - Mail spam filter
    - RAG : 
      - Must explain what are embeddings !!!
    - Video Search Engine
    - Fashion online watcher
    - CodeAgent

- Dive on LLMs : 
  - key players
  - how to evaluate LLMs
  - OSS vs closed API
  - Dive RAG
  - Dive finetuning
  - Dive Agentic AI

- Tech watch ?

## 3 - Others
- AI project management
- AI regulation + AI Safety
- Entrepreunership YC rules


## 4 - Business AI
- AI Value Chain 
- AI Market 
- AI Business models

## 5 - 
Group projects showcase ? 
QCM 


The course would have to be restructured in the following manner : 
  - docs 
    - slides 
      - assets
      - Session${SESSION_NB}-Deck${DECK_NB}-Title.md
  - dist
    - html
      - Session${SESSION_NB}-Deck${DECK_NB}-Title.html
    - pptx
      - Session${SESSION_NB}-Deck${DECK_NB}-Title.pptx 
