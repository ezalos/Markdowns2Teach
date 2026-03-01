# Course Outline — Deep Tech & Machine Learning

M2 Entrepreneuriat · Sorbonne · 2026
5 sessions x 3h · Mon 17h30–20h30 · ~28 students (7 teams of 4)

## Session Format

Each 3h session follows:
- **Deck A** (45 min) → 15 min break
- **Deck B** (45 min) → 15 min break
- **Block C** (45 min) — practice / QCM / external speaker + 15 min buffer

---

## Session 1 — Comprendre l'IA en 2026

**A — L'IA Générative : ce qu'elle sait faire** (`session-01/A-genai-fondamentaux.md`, 29 slides)
- GenAI intro, capabilities, market impact
- AI taxonomy: by technique (Stats→ML→DL→GenAI), by paradigm (Supervised/Unsupervised/Self-Supervised/RL), by task (Classification/Detection/Generation)
- Architecture tour: CNN, RNN, GAN, Transformer
- Three timelines: ML, Deep Learning, Generative AI (incl. OpenClaw)

**B — L'IA au-delà des LLMs** (`session-01/B-au-dela-des-llms.md`, 23 slides)
- 3 prompting principles (specific, iterative, context)
- LLM mechanics: data trends, next-token prediction, LLMs as thought partners
- Application families: Writing / Reading / Chatting / Coding
- Image generation with Diffusion Models, No-Code spectrum
- Capabilities & limitations, hallucinations, knowledge cutoffs
- Reasoning models, SLMs, decision matrix

**D — Biais et éthique : introduction** (`session-01/D-biais-ethique.md`, 3 slides)
- Gender bias in LLMs, toxicity
- Discussion: legal responsibility, bias testing, EU AI Act
- Teaser for Session 5

**C — Votre premier projet IA** (`session-01/C-premier-projet-ia.md`, 22 slides)
- Toolbox intro: JSON, API, HuggingFace, n8n
- Live demo: 3-node Sentiment Analysis workflow (Chat Trigger → HTTP Request → Format Response)
- Project assignment: 7 teams, 10 pre-built projects, evaluation criteria
- Homework: form teams, create HF account, pick project via Google Sheet

---

## Session 2 — Construire avec l'IA

**A — Du Prompt au Produit** (`session-02/A-prompt-au-produit.md`, 20 slides)
- 4 app categories (Writing, Reading, Chatting, Coding)
- Prompt-based development lifecycle
- Scope → Build → Evaluate → Deploy (with evaluation metrics)
- Tokens, vocabulary sizes, context windows, costs

**B — L'Ingénierie IA** (`session-02/B-ingenierie-ia.md`, 23 slides)
- RAG pipeline: 5 steps (chunk→embed→index→retrieve→generate), hybrid search, reranking
- 3 LLM generations: Base → Instruct → Thinking
- Fine-tuning: LoRA, QLoRA, distillation
- Agentic AI: ReAct, Tool Use, MCP protocol
- RAG vs Fine-tuning decision matrix

**C — Classification par LLM avec OpenRouter** (`session-02/C-n8n-openrouter.md`, 16 slides)
- OpenRouter intro (free tier, API key setup)
- Structured Output in practice (prompt, field ordering, confidence)
- Demo: n8n workflow Chat Trigger → HTTP Request → Code → Response
- Hands-on: implement OpenRouter approach for team project

---

## Session 3 — Cadrer un projet IA

**A — RAG & Agents IA** (`session-03/A-rag-agents.md`, 30 slides)
- RAG pipeline (chunking, embeddings, vector DB, hybrid search, reranking)
- RAG advanced (Contextual Retrieval, Agentic/Self/Corrective RAG)
- Agents (ReAct, Tool Use, MCP protocol deep dive, MCP security)
- Skills (SKILL.md standard, Skills vs Tools)
- Agent methodology (Anthropic progression, compound errors, failure modes)
- Toolbox synthesis, key takeaways

**B — Méthodologie projet IA** (`session-03/B-methodologie-projet.md`, 17 slides)
- CRISP-DM 6 phases, LLMOps 9 phases
- AI Canvas tool
- Open Source vs API vs Self-hosted
- Case studies: Klarna, L'Oréal, Schneider, Doctolib, Alan
- Failure analysis patterns

**C — Agents en action** (`session-03/C-demo-agents.md`, 11 slides)
- Live demo: n8n AI Agent with ReAct loop, Calculator + HTTP tools
- MCP teaser: Claude Desktop + filesystem MCP
- Project check-in: team status, presentation prep, checklist

---

## Session 4 — Le business de l'IA

**A — L'écosystème IA** (`session-04/A-ecosysteme-ia.md`, 18 slides)
- 9-layer AI value chain
- Key players: NVIDIA, cloud providers, model labs
- Market size and investment trends
- French/EU positioning, Mistral AI spotlight
- Open vs closed ecosystem dynamics

**B — Business Models & Cas Réels** (`session-04/B-business-models.md`, 17 slides)
- 7 business model patterns
- Cost deflation, pricing evolution, moats
- Data flywheel and network effects
- Case studies: Klarna, L'Oréal, Cursor, French champions
- 5 structural trends for entrepreneurs

**C — Intervenant externe** (~1h)

---

## Session 5 — Éthique, gouvernance & clôture

**A — Régulation & IA responsable** (`session-05/A-regulation-ethique.md`, 23 slides)
- EU AI Act: 4 risk levels, timeline, compliance costs
- GDPR interaction, global regulatory comparison
- AI bias cases, copyright issues, environmental impact
- Job displacement vs augmentation
- Responsible AI frameworks
- Tech watch resources, course recap

**B — Présentations finales**
- 7 teams x 5 min + feedback (~40 min)

**C — QCM & clôture**
- Final evaluation + wrap-up

---

## Content Not Yet Designed

- **Practice thread**: N8N workshop progression — S1-C done, S2-C done, S3-C done
- **Prompt engineering competition**: timing, dataset design
- **Presentation logistics**: 28 students, team composition
