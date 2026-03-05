Corrections of the course : 
- slides should fit in screen, MUST FIX, maybe screenshot it ?
- context window, wrong diagram, and false "noting is deleted"
- 


# Research TODOs — Course Restructuring (2026-03-01)

These topics need deeper research before their new decks can be finalized:

- [ ] **MCP protocol deep dive** — for S3-A agents section. What MCP is, how it works, the protocol spec, real-world examples
- [ ] **Skills concept** — for S3-A agents section. What Skills are in agent development, how they compose with MCP
- [ ] **Agent development methodology** — for S3-A agents section. Best practices, common patterns, failure modes
- [ ] **RAG expansion** — for S3-A. Hybrid search, advanced chunking strategies, reranking, production patterns
- [ ] **N8N OpenRouter integration** — for S2-C. Step-by-step structured output generation tutorial
- [ ] **Agent demo design** — for S3-C. What specific MCP tool / agent workflow to demo live

# Engineering

# Content

## No-code tools

- Some n8n video ? Will need to show what's a JSON, and the javascript notation to select a variable
- Explain what is an API and a WebHook


CORRECTIONS : 
Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md


Session 01-A: 
- Slide 8 : missing the value produced in 2025, see docs/sources/ml_dl-market_value.md  also the trillions/an prediciton should come with a date if appropriate
- slide 11, say it's not AI
- For the other slides let's break it down THIS_FORMAT : 
  - Why & What : why it matters & field definition with a PaperBanana diagram or an image
  - A couple of examples Business use cases with this tech 
  - 1 or 2 algo example, with a given image or PaperBanana diagram

So for ML definition  fill THIS_FORMAT with : 
definiton """
Machine learning is an approach to (1) learn (2) complex patterns from (3) existing
data and use these patterns to make (4) predictions on (5) unseen data.
""" cite Chip Huyen, and read the page 3-6 (not pdf page, but book pages) docs/sources/books/designing-machine-learning-systems-an-iterative (1).pdf to say why each is important (1: Database, 2: Zip Code, ...)

For the deeplearning add neuralnetwork drawing and perceptron, put the keras link on it's own diapo (even if quite empty)

For the GenAI transformers fill THIS_FORMAT : 
The why : Explain the limitation for translating before attention , make a nice PaperBanana
```
The “Bottleneck” Problem
Imagine trying to describe the entire plot of a three-hour movie in a single sentence. You’d lose a ton of important details, right?

That’s exactly what older translation models, which used an encoder-decoder architecture, did. The encoder network would read the source text and compress it into a single, fixed-length summary (a ‘vector’). Then, a decoder network had to use that one, tiny summary to generate a full translation.

This worked okay for short sentences, but for anything long or complex, it was a disaster. The model would forget key details, lose track of the context, and produce translations that were clunky and inaccurate.
```

Then the what : 
slides/session-01/assets/Transformer-model-architecture-described-in-Attention-Is-All-You-Need-6.ppm 

+
"""
The Library Analogy: You ask a question
Books have spine labels: Renaissance, Medieval, Modern Art. 
These are the Keys (K) They tell you what each book contains without opening it.

"What caused the Renaissance?" This is your Query (Q) what you're trying to understand.

Attention compares and selects

Inside each book: actual content

Compare your question to all labels, calculate relevance, then extract information from the most relevant books—all simultaneously.

Detailed information you need. These are the Values (V) The knowledge you want to retrieve.
"""
and add the links to the resources

For the Supervised / Unsupervised / RL : 
- The starter sldde (15) should just list the 3 names, and then we follow for each THIS_FORMAT we spoke (2 slides in supervised for the algos, one random forest, other KNN)

For the tasks, why is because it will allow them to explain what they wan t to build or allow them to search for models. And then please break regression / classification in a slide each and do some paper banana for visual

For the timelines : 
It will be better if the image is just aftyer title centered, then the table.





CORRECTIONS : 
Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md


# Session 01-B: 
- Slide 1 : METR reference will be put later for thew introduction of agents after the RAG, it's not the right time to show it, for the size of LLMs it should be said before we speak about the the pre-training. For this introduction I would like to speak about how LLM are making large advances, and especially saturating benchmarks, You should research it slides/session-01/assets/epoch_ai_llm_saturation_benchmarks.jpeg  
- Slide 3 : It could be interesting toi exchange it for a paper banana diagram : 
"I learn AI and I " -> Tokens -> LLM -> Logits (show a couple only) -> sample "love "
"I learn AI and I love " -> Tokens -> LLM -> Logits (show a couple only) -> sample "it!"
"I learn AI and I love it!" -> Tokens -> LLM -> Logits (show a couple only) -> sample "<eos>"
- Slide 4 : Tokens add image : "slides/session-02/assets/6630e466c569a5f73cd81c9e_Understanding LLM Billing_ From Characters to Tokens-p-1080.jpg"  + explain that the tokens is the vocabulary of the LLM, with last Qwen Models ~200k (checks for citations online) (you can keep llama citations here)
- Slide 5: add slides/session-01/assets/context-window.svg 
- New slide after the context window you should say that  it's increasing shjowing this https://substackcdn.com/image/fetch/$s_!FCO4!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F59c172a0-213b-43ec-94d1-e163623706bb_1600x1027.png (dl it)
- Slide 06: Adding a LLM vs MoE PaperBanana diagram would make it more visual (should show router pred + experts in MoE, but it doesnt have to show details masked self-attention / layer norm ...)
- Slide 07 : image should be put center after title, I love the image but remove the cost (use the run cache still available to leverage the work)
- Slide 08: please also cite the exact name of the different variant for a qwen3 model on openrouter or hugging face
- Slide 15 : should be broken down 1 slide explain float/int  using https://medium.com/@aquaone/what-are-tops-flops-int4-float-32-854cc79de75d slides/session-01/assets/int_floats.webp and what is quantization, it's impact on Memory / SPeed / Intelligence (source). Then second slide is how to compute the vram need
- Slide 17 addimage fromhttps://cjtrowbridge.com/ai/mmlu-params/graph.svg and cite https://cjtrowbridge.com/ai/mmlu-params/ update the numbers to use the one from the article (I prefer to use Qwen than to use llama as example)

For the API costs I would like to re-use : http://77.134.130.112:3901/session-02-A-prompt-au-produit#18

Should add the limitations (Knowledge Cutoff + Hallucinations) : 
- http://77.134.130.112:3901/session-02-B-au-dela-des-llms#22 
- http://77.134.130.112:3901/session-02-B-au-dela-des-llms#23

Should be researched and added a slides on structured output : 
- The problem it solves 
- What is it
Should be researched and added a slides on LLM multimodality : 
- Images / Videos / Sound + give examples


CORRECTIONS : 
Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md

Session01-A:
Change 15 image, it should be https://www.researchgate.net/publication/334609713/figure/fig1/AS:11431281369606220@1744317990799/Multi-Layer-Perceptron-MLP-diagram-with-four-hidden-layers-and-a-collection-of-single.tif (download it)
Change 22 to Decision tree! 

Session01-B:
Corrections to the slides : 
- Slide 03 : not the right Infography. They current one is OK, but i would like it to be duplicated vertically, so we can see the progression of the text being generated. Also there should be a bit more details, for example at the sampling step, show like the top 2-3 tokens and highlight the one sleected by sampling (and which we can see in the "duplicated version under" having one more token added to the LLM input)
- Slide 07 : Infography ok but not perfect, please refetch the work you did to not start from scratch, but a couple of modifications : the router arrrow should pass to the experts, and not the same expert should be activated at each layer. For the Normal LLM side, the schema should be a similar to MoE but no router, only one Expert and bigger (should not be called an expert).
- Slide 08 : you didnt modified the paperbanana grpahic to remove the cost, please do it. Also I liked a lot the details you were giving on how much data (in Tokens) is roughly need at each step, cna you search them again to add them ? cite your sources
- Slide 09, remove the end stuff about qwen, and add this link https://huggingface.co/collections/Qwen/qwen3 please also add the link in the slide about quantization and model size, so I can reference it later 
to show realworld example.
- SLide 16: I'm really surprised by the small loss. Can you do more research about it ? It seems cherry picked. Also remove the image
- Slide 17 : needs to start by saying that model uses gpu, and in the gpu there is a quantity of vram GB. If a model is larger than your vram you cant use it in a practical way
- Slide 20 : We lost content can you check the git history ? Your left table do not mean anything without input tokens. Also I would prefere samll qwen3 or deepseek as price example
- Slide 26 should arrive just after slide 20
- Slide 27 has a formatting problem
Also you are missing a lot of sources and citations

New Slides to add : 
For structured outputs I want you to stress out how cool it is! 
Make some slide example usages : 
- Simple classifier
- Data extraction in a book (charcter names / age / profession )
- Or even tool usage (like tool calling or filling a json input of a n8n node)
For the LLMs we need ot add : 
- Sampling :  Temperature & Top-p & Top-k. You should add it to the beginning after context-window, make a special slide and use paper banana to make it crystal clear


We have some corrections to do, for them you will need :
@docs/references/workflow-new-slides.md when researching new topics or creating slides
@docs/references/slide-creation-standards.md for all slide conventions and sourcing rules
And to update after @docs/references/course-architecture.md and other relevant documents


We need to update the students project ! 
@docs/references/slide-creation-standards.md
You have to update the deck slides/session-01/C-premier-projet-ia.md and maybe some of docs/references/n8n-student-guide.md

At the end the slides are here for the presentation, the md.guide will be sent to them by email (so thay have access to all the technical details). Can you convert it to like a simple formatted pdf (or anything easily readable for them, like a word doc), and add make command ?

You must also prepare me a google sheet I can upload with : 
One sheet with colunm group (G1, G2, G3,...) and then 4 columns Student 1, Student 2, Student 3, ... They should fill before the end of session
And then a second sheet with Project Title, Project Description, Group
In the project description, do not speak about the right error metric, and avoid technical terms like saying the exact "ml task name" as it's part of the evaluation.
All the groups should formed before the end of the session, and the project chosen and filled before Friday the 06 march


Remove mention of my IP (77.134.130.112) and put https://7b97-77-134-130-112.ngrok-free.app

They can either do the project using an hugging face model or an LLm through API (like open-router) with structured outputs.

The example workflow is now "TEACHER_EXAMPLE-Prod-HuggingFace" and "TEACHER_EXAMPLE-Prod-OpenRouter"

The dataset they have to provide must have at least 20 examples, spanning easy to hard use-case, and be close to the future prod data.
They must evaluate at least 2 different models on their dataset, see the example Eval.


They must not spend money on this work (open-router has some free-tier models with 50 message / day (or if they charge 10$ they can have 1k msg /day for free-tier models), and hugging face also have generous freetier fo HF-APi-inference (check how much))


At the end of the presentation, make it clear that learning to use a specific tool is less important than learning to learn. That's why this n8n course is minimal and do not cover everything they will need, because I want them to research as a group how to use it and create what they have in mind. They should not hesitate to use AI to build it (but they are responsible of the quality of what is produced and should understand it)


For the notation, here's what I have in mind (so they must do 1 presentation and a demo in 4 minutes total).
Do not give the precise nb of points, but tell them about what matters, and a rough idea of how much a part will contribute to the notation (we can see it's heavy on the evluation and demo, but the aesthetics do not matter that much)
- Presentation : 
  - the presentation + demo fits in 4 minutes : 2 point
  - Explain the product clearly : 1 point
  - Demo and it works in live : 3 points
  - I can start interacting with it in less than a minute (not counting the workflow time), and it works : 5 points
  - Model evaluation : 
    - correct ML task said : 1 point
    - Using the good metric : 1 point
    - Dataset, showing 2-3 examples : 3 points
    - at least 2 Models tested : 2 points
    - motivation for the right model choice : 1 point
- Any of these bonus 5 points (up to 2)
  - extensive testing across +10 models, and clear reports of results
  - having a website interface (lovable | blot.new | ...) I cna interact with
  - managing complex input types (image / video / audio)
  - having some database / corpus of data (like for RAG, or a system with some memory)


We need to update the presentation slides/session-01/0-intro-cours.md 
The course objective should add : 
- Giving them good fundamentals in AI
- Learning how to choose and use the system they could start a company with

Plan du cours : ne le lie pas au dates de session : 
  - Les types d'IA 
  - Les LLMS
  - Evaluer l'IA
  - RAG & Agent
  - and then the rest we already have

Slide sur les dates de session et :
Les dates de session et attention previent les que la session 4 pour accomoder un intervenant en fauteil roulant devrait se faire a l'ecole 42, 96 Bd Bessières, 75017 Paris. Accessible depuis ici en 35 minutes par RER B + métro 14, ou métro 4 + 14 (depuis le 14 rue Cujas), pour accomoder tout le monde ce court demarrerait 30 min plus tard (donc 18h)

SLide 04: retire la colonne format et le bloc de fin.
Slide 07: simplify (and update it because it's not exact anymore : slides/session-01/C-premier-projet-ia.md)


Context window : slides/session-02/assets/context-window-thinking.svg

Fot the context window, you need to make a full slide for it, use 


WE ARE MISSING EVALUATION CHAPTER, will do later


I need to prepare the g-sheet
-> also I need to formalize that they must use an LLM
-> amin comment on ngrok for security reasons
Bolt.new ok for front, or Lovable

I should make sure S2 has evaluation in it.


# Corrections for : session-02-A-prompt-au-produit


Il faudrait que tu reparcours le cours et a chaque fois qu'il y a une "Question pour la classe" je veux que tu me mettes des axes de reponses en commantaire / notes de slide




## Nice things which could be added

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




