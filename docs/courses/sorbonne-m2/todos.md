Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md

===========================================
https://slides.develle.fr/session-04-C-business-models.html#4


remove the slides : 1, 3, 14, 16

===========================================
Could be interesting to copy pasting the couple of last SemiAnalysis newsletters to see if intersting things

https://slides.develle.fr/session-04-B-ecosysteme-ia.html#3

1: add as reference that total world gdp is around 100 Trillion
https://en.wikipedia.org/wiki/Gross_world_product
also, where is the pitchbook source link ?

3 & 6: sources are wrapped on the left

For the 9 layers: please take in account "docs/sources/The AI Value Chain in 2025_ Nine Layers, One Trillion-Dollar Stack.pdf" to add a bit more narrative to the current raw numbers/company names. You may add 1 slide if needed (and up to 2 exceptionnally). Make sure to use and keep the sources cited in the pdf.
I'm really looking to keep the 20% of the content which is the 80% most interesting (paretto), the point is not to double in size the deck. You should reshape what was here originally, especially if less interesting (just a bunch of numbers dont tell a lot), but keep the couple of company being cited so it at least ggive a clear picture to the students.
Also, make sure to generate visuals for each individual layer, putting if needed graph or company logo. Take the time to brainstorm yourself. Also remember, the infography are here for the highlevel understanding, not stuffing paragraph of text.


6 : it's a bit all over the place, the message is not really clear, it's hard to know what to keep from it.
-> make me some propositions.

7: we miss the revenue of scaleway

11: remove

For the slides 14-18. I'm curious if they wouldnt be better integrated in the layers directly. IF so they  do not count in the 1-2 extra slide by layer (but can still be reshaoed with the new content, but keep the images, they are great)

On the previous deck on methodo, add theses sources in the mvp slide :
- https://www.youtube.com/watch?v=0kARDVL2nZg 
- https://www.youtube.com/watch?v=1hHMwLxN6EM
also, we may need a new slide to explain what is needed for mvp

On the next deck the data moat source is wrong, maybe it should be this link ? https://a16z.com/services-led-growth/ 
update content if doesnt reflect it's resources (verify the other)
===========================================

https://slides.develle.fr/session-03-D-methodologie-projet.html
-> should be moved to session 4

Under is change of the order for the things in this deck, removing of slides, and new slides.


NEWSLIDE : begin with the Bitter lesson from Richard Sutton.
http://www.incompleteideas.net/IncIdeas/BitterLesson.html
--> How AI get's 'simpler' with time, and is in the end just Moores Law

Then NEWSLIDE on how it was really complex to do some CV task before : 
https://www.youtube.com/watch?v=c3zw6KI6dLc&list=PLkDaE6sCZn6Gl29AoE31iwdVwSG-KnDzF&index=22
Example, before for gender detection : training model, having dataset, 2 step process with one first model for bbox face & second for classif. both trained, so needed data
- now just: image in VLM -> structured output out, no training needed and competitive in performance 
This will require a paperbanana diagram showing the 2 different options 

Then slide 01

Then slides [03-07] how to build tech

NEW SLIDE:  Add at the end that the first iteration is a bit different, the original build to :
AI toy model first: majority class if classif, mean value if regression
Evaluate having a small dataset at the beginning (~20 examples)

NEW SLIDE: Then iterate on this baseline : 
- Build / evaluate loop : keep changes if it improves your score. Complexity should be added only if it is useful
- add examples in your dataset as you cross problems in production (something missed ? something incorrect being not predict), or if you want a better coverage.

Slides 12-14

Slide 22 — Progression : Prompting

Slide 16 MVP Building GMAIL story : https://www.ycombinator.com/library/Jc-paul-buchheit-creator-of-gmail 


Slides to remove : 2, 8-11, 15, 17, 18-21, 23-24
 


https://slides.develle.fr/session-05-A-regulation-ethique.html#4

02 — EU AI Act : les 4 niveaux de risque
-> what are these 4 levels ? How do I know in which I am ? I'm ok with a simplification if really complex, but it should be clearly stated

===========================================

Feedback RAGs : 

S02: should be moved just after "Le Pipeline RAG en détail" 
Replace with a simple diagram, a RAG is just an LLM plugged on a search engine. 
We can either feed the search engine new documents, or ask questions to the LLM which uses the search engine to answer.

S03: great
And after put directly the slide 17 with the concrete example!


Let's move the embeddings deck outside the RAG one ! 
Put it before A=Embedding, B=RAG, C=Agents, D=Methodo


S13: great
s14: we need to reformulate :
-> We introduce the search engine part, which can be tfidf or bm25 or embeddings
then we should present TF-IDF, then BM25 (we can just ay it's tfidf on bigrams and trigrams), then embeddings, then hybrid search

===========================================

Feedback Embeddings : 

Add MTEB link !! But in the end we must test on our own data to be sure

===========================================

S01: Ok
S03 should be next 
S02: Multi-Step Agent and Multi-Agent are both 3 stars, not 4. THe diagram has the same pbm (but otherwise is beautifull, it's the only change needed).
S04: ok

Tools, Skills & produits agents S19-S21
S20 : a full concrete example is better of a skills.md would be great something simple and visual (like a skill to translate a document, or somehting else, short that the text can be shown easily)


Then explain that MCP is a particular type of tools, and go on with MCP chapter: 
MCP S13-S18
MCP : should be after the introduction of tools
S13: please do a vertical stack of these diagrams : 
- https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1.png 
- https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1a.png 
- https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/2.png
S15: concrete example missing of host/client/server, do it with an n8n server and wiki search mcp
S16 : https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/8.png

Also, in MCP, it's missing the CLI controversy (like would the abstraction still be necessary in the future ?)
 

Memory stuff S25-S30
S26 types of memories : might be bullshit (it's human centered here). Let's stay LLM centered? Like: prompt / history conversation / memory.md / outside database 

Context-Engineering: S36-S43
-> it's way too much content, you need to only keep the most import  20% (like 2-4 slides) and put the rest in an extradeck


S05 
S06-S12 Agents work flows : should be later and should have diagrams (just fetch from anthropic, they are great)
- prompt chaining https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75 
- routing https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75 
- parallelizzaion https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75 
- orchestrator https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75 
- evaluator https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75


Agent in production : S31-S35


S22 - S23
Open claw et Claude code should be way later in the course
For the open claw : explain pulse files?

AutoResearch : S44-S45

S46 until the end needs to be custom made again




===========================================



Pour les rags, quoi  dire : 
- expliquer le fondamental pareto (chnunking + bm25) 
- la method (noisy signal for llm pred, follow recall on search engine, for this synthetic dat generation is great, juges can be cheaper)

Pour les agents, some notes : 
Mais un agent IA c'est quoi ?
Un agent c'est un systeme qui agit en autonomie pour accomplir un objectif a l'aide d'outils !
Par exemple si tu demandes a un agent de te trouver un bon resto asiat a paris pour diner mardi prochain, c'est son objectif !
Peut-etre que les outils qu'il a disposition c'est :
recherche google
lire un site web
google maps
Il va commencer par une recherche Google :
"Meilleurs restaurant asiatiques Paris"
Il va voir les 5 premiers resultats, et ca tombe le 2eme c'est un top 10.
Il va recuperer le contenu du siteweb.
Et apres pour chaque restaurant il va verifier avec l'outil google maps que le restaurant est bien ouvert mardi prochain.





Corrections of the course : 
- Benchmark satures, but it's possible to see beyon (make new slide after), progress is constant
- context window, wrong diagram, and false "noting is deleted"


CORRECTIONS : 
Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md

Corrections session 2-A LLM : 
- SLide context window, you need ot change the image for https://platform.claude.com/docs/images/context-window-thinking.svg + and do not say that "noting is deleted" 
- Mixture of expert use this image : https://media.licdn.com/dms/image/v2/D5612AQGOYM7pxovxYQ/article-cover_image-shrink_720_1280/B56ZWbBoLeHEAI-/0/1742062650873?e=1774483200&v=beta&t=rb092P1wag2hNnKPSwRPQwCqFkzGAEBllcNou8ImLvk 
- Finetuning add image : https://miro.medium.com/v2/resize:fit:1400/format:webp/1*y9mXfWfxvqHk55TNrP2CXg.png 
- Slide 15 : cost for GPT  2 is now around 60$ (2hours of 8xh100) https://x.com/karpathy/status/2029701092347630069?s=20 
- Slide 20 : please capture the plot from epoch ai and add it
- slide 21: you cna remove
- Slide 23 : please add an exemple of open-weight model, but not open-source commercial. Like YOLO (if you got an llm example it's best)
-for quantization please add this image  : https://miro.medium.com/v2/resize:fit:1400/1*5IdTuemsFlNSkLfOtcOR2g.png 
- for moe & vram add this image  https://substackcdn.com/image/fetch/$s_!bmV0!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fce63e5cc-9b82-45b4-b3dc-9db0cac47da3_880x748.png 
- slide 29: missing new line on right side
- slide 30: behind the token nb  put the multiplication in paranthesis : ~670 tokens (= 500 mots * 4/3 tokens/words)
- slide 33 : remove the table and merge with the next slide diagrams
- slide 35: remove
- slide 37: remove
- slide 39: remove
- slide 40: add image https://substackcdn.com/image/fetch/$s_!Pq2z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d76dab1-362f-45b6-9b12-a12ac131edc5_1600x944.png 
- slide 42: put the example on 2 lines, more readable
- slide 43: put the example on 3 lines, more readable

CORRECTIONS : 
Here are some corrections to on the slides.
@docs/references/slide-creation-standards.md
@docs/references/workflow-new-slides.md
@docs/references/course-architecture.md

Add these images to the slides on evaluation : 
- confusion matrix : https://stratusdata.io/wp-content/uploads/Blank.png 
- Accuracy : https://stratusdata.io/wp-content/uploads/1-%E2%80%93-2.png 
- Recall : https://stratusdata.io/wp-content/uploads/2-%E2%80%93-2.png
- Precision : https://stratusdata.io/wp-content/uploads/4-%E2%80%93-2.png
If not enough space on precison / recall slides and you have to make 2 slides, it's ok
- Slide 8 IoU stack 2 images veritcally
- for mae add this https://miro.medium.com/v2/resize:fit:1200/0*s6YGm5hBneEVNc7U.jpg and change rmse to MSE and add this https://byam.github.io/assets/img/model-eval-val/mean-squared-error.png . Also add hte formulas (simple for 1 example)

Slides Evaluation corrections :
- 01 confusion matrix add https://stratusdata.io/gone-fishing-4-metrics-for-evaluating-binary-classifiers/
- 02 make one slide for accuracy, and then a slide for the "piege". No need to tell it in one slide. For the piege slide explain that airport scanner which needs to find 10 bags out of 10k can have 99.9% accuracy while missing everything.
- For precision / recall, I have a live demonstration I will show. If it fits, cool to add : https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Precisionrecall.svg/1280px-Precisionrecall.svg.png but if dont fit, its ok without
- Slide 8 : stack 2 images veritcally
- Slide 9 can be removed
- Slide 10, must modify (too much saturation). We can keep MMLU + SWE-bench (give the current rating for frontier clowsed source). Change GSM8K & HumanEval, for ARC-AGI 2 & Humanity's Last Exam. Give numbers for frontier AI.
- For chatbot arena, add a word of caution, and this source https://www.hackster.io/news/chatbot-arena-shenanigans-09bd3fa3e6fa
- GDP val add source https://evals.openai.com/gdpval/leaderboard 


Interesting stuff to use : 


LLM : 
- Training costs https://epoch.ai/blog/how-much-does-it-cost-to-train-frontier-ai-models
- LLM running out of data : https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data BUT MUST BE BALNCED BY : https://vintagedata.org/blog/posts/synthetic-pretraining 
- Open-source is only small lag : https://epoch.ai/blog/open-models-report 


Eval : 
- Great resource : https://lmcouncil.ai/benchmarks
- https://epoch.ai/benchmarks/eci


RAG : 
- BM25 deepmind : https://arxiv.org/html/2508.21038v1
- https://jxnl.co/writing/category/rag/#why-cognition-does-not-use-multi-agent-systems 
- https://jxnl.co/writing/2025/08/28/context-engineering-index/

Engineering / build : 
- https://huyenchip.com/2025/01/16/ai-engineering-pitfalls.html


Ethics : 
- https://www.darioamodei.com/essay/the-adolescence-of-technology
- Anthropic critic : https://www.lesswrong.com/posts/5aKRshJzhojqfbRyo/unless-its-governance-changes-anthropic-is-untrustworthy#1__In_private__Dario_frequently_said_he_won_t_push_the_frontier_of_AI_capabilities__later__Anthropic_pushed_the_frontier 
- https://www.anthropic.com/news/claudes-constitution & https://www.anthropic.com/constitution


Agents : 
- https://arxiv.org/pdf/2601.10825


Ecosystem AI, where it's heading : 
- https://epoch.ai/blog/inference-economics-of-language-models
- https://epoch.ai/blog/can-ai-scaling-continue-through-2030  
- https://epoch.ai/blog/what-will-ai-look-like-in-2030
- https://epoch.ai/blog/what-do-economic-value-benchmarks-tell-us


# Research TODOs — Course Restructuring (2026-03-01)

These topics need deeper research before their new decks can be finalized:

- [x] **MCP protocol deep dive** — DONE (S3-B slides 13-18). M×N problem, M+N solution, Host/Client/Server, 4 capabilities, ecosystem, security risks
- [x] **Skills concept** — DONE (S3-B slides 20-21). Tool vs Skill, SKILL.md standard, 26+ platforms, composition patterns
- [x] **Agent development methodology** — DONE (S3-B slides 22-24). Claude Code, OpenClaw, Knowledge Work Stack, product comparison
- [x] **RAG expansion** — already covered in S3-A (hybrid search, chunking, reranking, production patterns)
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




