# What is the real state of company-memory systems for agents in September 2026?

## Decision this feeds

**S52 "The company brain"** in the 2026-09-02 Station F founders' talk — one of two slides
on economic opportunity. It is also the most likely conversation topic in the room: the
incubator hosting the talk has a team building exactly this (an internal-memory agent built
from a team's Claude sessions). The current source is a vendor infographic from a
note-taking company's growth marketing (nine systems, four shared parts, an unaudited
149-team survey, and an ebook whose body is JavaScript-gated). The decision: **which
systems get named on the slide, with one defensible number each, and what the honest
architecture story is** — including whether written memory measurably beats long context.

## Must answer

- **Per-system primaries** for the systems worth naming: mem0, Letta (the MemGPT lineage), Zep and its Graphiti temporal-graph layer, and any first-party engineering write-up of a production company-memory system. For each: what it actually stores and retrieves, its architecture in one sentence, adoption evidence (repository stars with a date, funding with a date, named production users), and its own claimed benchmark with the caveat that it is self-published.
- **Does written memory beat long context?** The measured evidence: memory benchmarks such as LoCoMo and LongMemEval or their 2026 successors, and any study comparing a retrieval-plus-memory system against simply putting everything in a large context window. Report the numbers and the experimental setup, and state plainly where the evidence is thin.
- **The academic bridge**: Google's WikiSkill paper (arXiv 2608.27454) reports that a persistent wiki plus executable skills lets a 9-billion-parameter model with skills beat a 27-billion-parameter model without them. Verify those numbers against the paper, and establish whether any independent work replicates the finding that written, accumulated knowledge carries the gain.
- **The do-it-yourself pattern**: what is published about using plain files plus version control as an agent's company memory — the pattern the speaker actually teaches. Anthropic engineering posts, practitioner write-ups, and any measurement of how it compares to a dedicated memory product.
- **Market signal**: funding rounds, launches and acquisitions in agent-memory infrastructure during 2026, with amounts and dates from primary announcements or reputable financial press. Test the marketing claim that the category is less than six months old.
- **Failure modes with sources**: memory poisoning, stale facts that outlive their truth, retrieval precision collapse as the store grows, and privacy exposure when a team's sessions become a shared corpus. One citable source per mode, plus any documented mitigation.
- **The build-versus-buy read for a small team**: at what point does a plain-files approach stop working, on evidence rather than opinion?

## Source bar

tier: Primary repositories, papers and first-party engineering posts first. Funding and adoption facts from company announcements or reputable financial press. Vendor benchmark claims are usable only when labelled self-published and paired with their methodology. Growth-marketing content and unaudited vendor surveys may be cited for framing only, never for a number on a slide.

recency: 2026 state of play. Repository and funding figures carry their retrieval date. Papers may be older when they remain the reference, and must be dated.

## Deliverable

A Markdown report with: a table of named systems — system · what it stores · architecture in one sentence · one defensible number with its date · exact clickable URL · verbatim quote · self-reported yes/no. Then a verdict section on written memory versus long context, stating the strength of the evidence. Then a failure-mode table. Then a two-line read on build versus buy for a five-person team.

## Out of scope

- Retrieval-augmented-generation tutorials and vector-database comparisons as such.
- Any product recommendation.
- Consumer personal-memory assistants.
