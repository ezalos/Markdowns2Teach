
https://x.com/TaylorPearsonMe/status/2029996204306866585

See new posts
Conversation
Taylor Pearson
@TaylorPearsonMe
I've been working on a longer piece about how Claude Code is changing knowledge work — an "As We May Work" riff on Vannevar Bush's 1945 essay.

In the process I've been trying to visualize how all the pieces fit together. This is my favorite attempt so far — the Knowledge Work Stack:

Five layers, bottom to top:

The Model. The big blob of compute. Claude, GPT, whatever. Powerful but shapeless — it doesn't know your files, your preferences, or your Tuesday meeting schedule.

The Harness. Claude Code, Codex, etc. This gives the model hands — filesystem access, terminal commands, the ability to read and write files. Without it, the model is a chatbot. With it, the model can actually do things on your computer.

Personal Scaffolding. Your CLAUDE dot md files, skills, hooks, memory logs, folder conventions. Everything that makes the model work like your assistant, not a generic one. Everyone has access to the same models. The scaffolding is where differentiation happens — (h/t 
@DanielMiessler
)

Utilities + Materials. APIs, MCPs, and CLIs that connect to external services — email, calendar, CRM, documents. When an email comes in requesting a meeting, the model checks my calendar, drafts a reply, creates the event. I never open a browser. Markdown files plus Unix plus an LLM is a surprisingly general-purpose system — once you have ways of connecting to external applications, the model can basically do anything on a computer.

Agents. Once the infrastructure is in place, you deploy agents that use it autonomously. An agent is just a Claude Code session running on its own — you define the goal, it executes using the same tools and context it would if you were sitting there.

You stand on the scaffolding layer like a general contractor — directing the agents, inspecting work, occasionally grabbing a hammer yourself. The job is the same one the freestyle chess amateurs had: understanding what the machine is good at, designing process around its strengths, and applying your own judgment where it falls short.


slides/sorbonne-m2-2026/session-03/assets/agent_stack-claude_code.jpeg



