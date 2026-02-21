
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


CORRECTIONS : 


We have some corrections to do in Session 1. For them you will need : 
@docs/references/topic-exploration-guide.md when researching new topics
@docs/references/source-guidelines.md to find relevant sources
@docs/references/paperbanana-guide.md
And to update after @docs/references/course-architecture.md and other relevant documents

Session 01-A: 
- Missing recap slides at the end
- Tasks type : add images for CV slides/session-01/assets/object-detection.png slides/session-01/assets/object-detection.png and add tasks from HF (learning about task names is important bc it allows them to knopw what they can build, and with the vocab search hf efficiently) https://huggingface.co/models slides/session-01/assets/hf_tasks.png ? Also all task names should be in english
- Architectures : Let's put in a separate Deck

Then we will move stuff 
-> all the extra deck (architecture now but also slides/session-01/D-biais-ethique.md) should be put in slides/extra-decks (and still be compiled, think to move the resources linked)


We will change Session 01-B (you can move this deck in the session2 directory, it will be reused later). For the updates you should cut slides from S01-B, S02-A and S02-B, once you read the new plan, do a full search of slides to see which slides you should move to be re-used in S01-B. If the deck is a bit too big it's not a huge pbm, we will tackle it after (but no need to have 2 slides saying the same thing with different words oibsiouly). If a slide is reused in the new S1B no need to let in the orignal deck you took it fdrom

So here's the content for the Session 01-B : LLMs

- First an introduciton to their high impact, and how they enable 
- Then a what is a LLM and how it works
- We then go through a Glossary with one or multiple slides by concept : 
  - Tokens
  - Context Window
  - Mixture of Expert (must tbe researched)
- Then we explain that different types of LLM exists depending on which training steps have been coompleted (first a PaperBabnan graph on the first slide, and then at least a slide each to explain why what, how much it cost (data & dollar), and examples)
  - Pre-Train
  - Instruct
  - Thinking (thinking we want to add https://substackcdn.com/image/fetch/$s_!pgyl!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png and dl it locally)
  - Finetuning
- Then we go through access :
  - Through Web interface (like ChatGPT)
  - Through API (like openai api / openrouter / anthropic)
  - open-weights (hugging-face)
  - open-source (and we cite the main licences ok commercially)
- Their size : 
  - What are B ? How to go from B to vRAM Go ? What's vRAM ? MacBook MPS ?
  - If a MoE , he Active B is also important (but still we explain that eventhough it's faster, you still have to have enoiugh ram to fit, or long time to offload reload model). (topic must tbe researched)
  - we show graph that smarter model are lareger but larger model are slower / more resource hungry (topic must tbe researched)
- We wrap-up a resume about everything we said in S1-B

With so many changes, DeepLearning AI as no big connections anymore to the S1, good time to change footer.




We have some corrections to do in Session 1 and Session 2. For them you will need : 
@docs/references/topic-exploration-guide.md when researching new topics
@docs/references/source-guidelines.md to find relevant sources
@docs/references/paperbanana-guide.md
And to update after @docs/references/course-architecture.md and other relevant documents

Are the corrections:

# New course architecture for S1, After Slide 7 : 

[New SLIDE] : Mais pas que la GenAI : (should be researched how much value is produced today by ML vs Gen-AI and/or how many ML models are deployed compared to GenAI)

[New Slide] : Many AI types : There are many ways we can categorize AI, here are some usefull ones 
By : 
the technique (or approach/method) -> Stats / ML / DL / GenAI
the learning paradigm -> Supervised / Unsupervised / RL 
the task -> Classification, Regression, Object Detection, ...


[NEWSLIDE] For the technique one global slide, then we will see a couple an example (one slide each, with a definition, a nice visual, and some example of applications): 
Stats -> you need to think about it
ML -> Linear Regression (I got something ready)
DL -> NeuralNetwork : https://playground.tensorflow.org
GenAI -> Transformers : https://poloclub.github.io/transformer-explainer/ x https://bbycroft.net/llm x  https://colab.research.google.com/github/davidarps/2022_course_embeddings_and_transformers/blob/main/Visualizing_Attention_with_BertViz.ipynb#scrollTo=dpX4plGXdr8o

[NEWSLIDES] For the learning paradigm, one global slide, then one slide each, with a definition, a nice visual, and some example of applications
Supervised : we mention LR is one, we also show Random Forest slides/session-01/assets/random_forest.png
Un-Supervised : KNN, I have a Gif here slides/session-01/assets/KNN_decision_surface_animation.gif 
Self-Supervised : Gen-AI : LLM pre-training on text (like transformer) or image generation  slides/session-01/assets/A/diffusion_model.gif / 
RL -> AlphaGo -> chess + other for Finance or LLM thinking training



[NEWSLIDES] For the Tasks we will see quite a bunch of them : 
Classification / Regression
Object-Detection / Segmentation 
Text generation : translate / question-answering / summarization / coding / ...

You can then insert the slides from Architectures NeuralNetworks from the S2-B

Then we get back around the slide 14 for which you will generate nice timelines : 

- Chronology : 
--> TimeLine for ML : 
Linear Regression — The earliest form traces back to 1805 (Legendre) and 1809 (Gauss) with the method of least squares. It's arguably the oldest ML algorithm, born out of astronomy (predicting planetary orbits).
K-Nearest Neighbors (KNN) — The algorithm was introduced by Fix and Hodges in 1951 in an unpublished US Air Force technical report. It was later formalized and popularized by Cover and Hart in 1967 with their landmark paper on nearest neighbor pattern classification. It saw early practical use in pattern recognition tasks like handwriting and image classification through the 60s–70s.
Logistic Regression — Introduced by Cox in 1958, though the logistic function itself was described by Verhulst in the 1840s for population modeling. It became a workhorse in epidemiology and social sciences through the 1960s–70s.
SVM (Support Vector Machines) — The theoretical foundations were laid by Vapnik and Chervonenkis in 1963 (linear classifier), but the modern soft-margin SVM with the kernel trick was formalized by Vapnik et al. in 1992–1995. It dominated ML competitions and real-world applications (text classification, bioinformatics) through the late 90s and 2000s.
Random Forest — Formalized by Leo Breiman in 2001, building on earlier ensemble and bagging ideas (Breiman's bagging paper was 1996, and Ho's random subspace method was 1995). It quickly became a go-to for tabular data in both industry and Kaggle-style competitions.
XGBoost — Created by Tianqi Chen in 2014 (paper published 2016). It exploded in popularity almost immediately, becoming the dominant algorithm on Kaggle and in industry for structured/tabular data. It built on gradient boosting ideas from Friedman (2001).
timeline: linear regression (1805) → KNN (1951) → logistic regression (1958) → SVM foundations (1963, modern form 1995) → random forest (2001) → XGBoost (2014).
--> TimeLine for deeplearning : 
Hinton backprop
LeCunn MNIST (CNN works)
AlexNet (CNN Generalize)
Transformers 
--> LiTimeLinene for GenAI
Bert + Bert google at scale
ChatGPT
DALLE
Deepseek
Vision LLM (Gpt4v ?)
O1
Claude Code
OpenClaw

Then we cut the rest of the slides to put in S1-B, you can join this partial deck with the prompting slides from S1-B beginning. and then also add th elsides for reasonning models and onward.

Keep separate in a new deck the part on bias / ethics (25-27 ?) ( (it can be 4 decks for session 1 at the moment, we will arrange it later))


Now new corrections for the Session 2 slides :  

# Corrections for : session-02-A-prompt-au-produit

S2 all images should be 'contain' (it seems like none are in S2-A)
S2-A-01 -> missing coding AI (like in S1)
S2-A-02 -> for the deployment add link to https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf and image slides/session-02/assets/hidden-technical-debt.png 
s2-a-3,6 -> image is not contained

Aussi -> Il faudrait que tu reparcours le cours et a chaque fois qu'il y a une "Question pour la classe" je veux que tu me mettes des axes de reponses en commantaire / notes de slide

s2-a-7 Scope -> mesurer le succes. P-E show eval metrics ?

s2-a-13 : should be 2 slides !
Tokens add image : "slides/session-02/assets/6630e466c569a5f73cd81c9e_Understanding LLM Billing_ From Characters to Tokens-p-1080.jpg"  + explain that the tokens is the vocabulary of the LLM, with last Qwen Models ~200k (checks for citations online)
Fot the context window, you need to make a full slide for it, use 
Paper banana to show the context window, and especially the context window being increased turn by turn in a conversation (with thinking part being stripped of, but output beoing conserved, also find citations for this (for example in claude code doc)) https://platform.claude.com/docs/en/build-with-claude/context-windows found image here slides/session-02/assets/context-window-thinking.svg 

For Deck-B I would love to have a page explaining the differneces between an only pre-trained LLM, instruct LLM and thinking LLM. Each time tell what's training step is added, what is the use case of the end model, and when this step appeared (pretraining it's BERT, thinking it's O1)



S1 missing : 
- Examples of model (Stat model + LR OK RandomForest + NeuralNetwork OK)


S2 missing : 
- Different kind of LLMs
- Evaluation 

S2-B : 
RAG IS BAD
s2 is missing a PaperBanana diagram
s3 should be zooming on the search engine part, explaining it uses embeddings
THEN embeddings slide with image
VectorDB missing image / schema  slides/session-02/assets/vecotr-database.png
s8 -> cerveau is not a perfect analogy, makes LLm seems smarter thant they are
s9 -> finetuning image from https://www.sciencedirect.com/science/article/abs/pii/S0262885624001161 slides/session-02/assets/finetuning.jpg
s12 -> nano banana distillation 


WE ARE MISSING EVALUATION CHAPTER, will do later


Image taxonomie sous l'angle du type de data 

Image taxonomie sous l'angle de la tache realise

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
-> also I need to formalize that they must use an LLM
-> amin comment on ngrok for security reasons
Bolt.new ok for front, or Lovable

I should make sur S2 has evaluation in it.


# Corrections for : session-02-A-prompt-au-produit

S2 all images should be 'contain' (it seems like none are in S2-A)
S2-A-01 -> missing coding AI (like in S1)
S2-A-02 -> for the deployment add link to https://proceedings.neurips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf and image slides/session-02/assets/hidden-technical-debt.png 
s2-a-3,6 -> image is not contained

Il faudrait que tu reparcours le cours et a chaque fois qu'il y a une "Question pour la classe" je veux que tu me mettes des axes de reponses en commantaire / notes de slide

s2-a-7 Scope -> mesurer le succes. P-E show eval metrics ?

s2-a-13 : should be 2 slides !
Tokens add image : slides/session-02/assets/6630e466c569a5f73cd81c9e_Understanding LLM Billing_ From Characters to Tokens-p-1080.jpg  + explain that the tokens is the vocabulary of the LLM, with last Qwen Models ~200k (checks for citations online)
Fot the context window, you need to make a full slide for it, use 
Paper banana to show the context window, and especially the context window being increased turn by turn in a conversation (with thinking part being stripped of, but output beoing conserved, also find citations for this (for example in claude code doc)) https://platform.claude.com/docs/en/build-with-claude/context-windows found image here slides/session-02/assets/context-window-thinking.svg 

For Deck-B I would love to have a page explaining the differneces between an only pre-trained LLM, instruct LLM and thinking LLM.

WE ARE MISSING EVALUATION CHAPTER 

S1 missing : 
- Examples of model (Stat model + LR OK RandomForest + NeuralNetwork OK)


S2 missing : 
- Different kind of LLMs
- Evaluation 

S2-B : 
RAG IS BAD
s2 is missing a PaperBanana diagram
s3 should be zooming on the search engine part, explaining it uses embeddings
THEN embeddings slide with image
VectorDB missing image / schema  slides/session-02/assets/vecotr-database.png
s8 -> cerveau is not a perfect analogy, makes LLm seems smarter thant they are
s9 -> finetuning image from https://www.sciencedirect.com/science/article/abs/pii/S0262885624001161 slides/session-02/assets/finetuning.jpg
s12 -> nano banana distillation 


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