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


What should be checked