<!-- ABOUTME: Real transcript of the Grill Me demo, captured 2026-09-01 in stage conditions (opus, in-repo, 3m51s). -->
<!-- ABOUTME: Fallback slide content if the live demo cannot run. Unedited apart from this header. -->

# Grill Me — captured run, 2026-09-01

> Command: `claude --model opus --permission-mode plan` in `slides/station-f-claude-code/demo/`,
> prompt: *"Use the grilling skill. I want to build the agent described in README.md."*
> Time to this output: **3 min 51 s**. Unedited.

Facts first, then questions.

**What I found** (`docs/talks/station-f-claude-code/`): the talk is tomorrow, 2026-09-02 14h, Station F / Incubateur 42 — 40 min + 20 min conversation, English, founders who already use Claude daily. Its thesis: *"what compounds is what you build around the model: the harness, the written memory, the loop, the evaluation."* Slide 15 is **"Reach shared understanding before you build — the Grill Me pattern"**, marked **"Live-demo candidate"**, ~3 min, and still listed under Open decisions as *"In or out?"*.

Two things the docs do **not** say: Support Signal appears nowhere in the talk plan, and `slides/station-f-claude-code/` contains no deck — only this untracked README, created today at 15:39. So I'm not going to guess which of those is the real job.

---

❓ **Q1** — **What is actually being delivered here?** Three readings fit the evidence. (a) **Stage prop**: this README is the input to the slide-15 Grill Me live demo — what ships is a rehearsed, legible interview, and Support Signal never has to run. (b) **Real tool**: a working weekly agent you'll actually operate. (c) **Reference implementation**: it really runs, and the talk shows its output as proof the method works.

➡️ **(c), weighted toward (a).** Build a genuinely runnable Support Signal, but treat the *interview transcript and the plan it produces* as the primary artifact, because that's what slide 15 needs. A demo of a method that produced nothing runnable is a weaker demo than one where you can say "and here's Monday's memo." But if the code slips, the demo still lands.

❓ **Q2** — **Is "we" real?** Is there an actual 6-person B2B SaaS with an Intercom inbox behind this — a portfolio company, a client, a friend's startup — or is the persona invented so the brief has teeth? This changes whether "customer names and account IDs" is a compliance problem or a realism detail.

➡️ **Invented, but honor it as if real.** Nothing in the repo hints at a support-data integration or an Intercom key, and inventing a sharp constraint set is exactly how you write a good demo brief. If it *is* real, say so now — it moves the PII question from "nice touch" to "hard gate" and I'll plan differently.

❓ **Q3** — **Where does this sit against the talk?** You have roughly 22 hours and the deck for tomorrow does not exist as a file yet. Support Signal can absorb an afternoon or a strict box.

➡️ **Strict box: ~90 minutes, and the deck takes everything else.** I'd rather hand you a working thin agent and a clean transcript than a beautiful agent and no slides. If you tell me the deck is further along than `slides/` suggests — drafted elsewhere, or you're building it from the talk plan live — I'll widen this.

❓ **Q4** — **Is this session itself the demo?** You invoked the Grill Me skill on the Support Signal brief, which is precisely the slide-15 pattern. Are you (i) rehearsing the demo now, so this transcript wants to be short, punchy and screenshot-legible, (ii) generating a canned transcript to show on a slide as a fallback if the live demo is cut, or (iii) just genuinely building the thing and the resemblance is incidental?

➡️ **(i) — rehearsing.** I'll keep rounds tight, questions numbered and quotable, and recommendations opinionated enough to be interesting on a projector. Tell me if you'd rather I optimise for depth over legibility; they pull in different directions and I can only serve one.
