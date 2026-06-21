# How to Write a Great ML Technical Blog Article

**A Research-Backed Reference Guide for ML Engineers Writing on Medium**

*Compiled from 40+ sources spanning data-driven content analysis (100M articles), academic writing guidelines (CMU ML Blog), practitioner advice (ProBlogger, Draft.dev, Dev.to), and ML-specific references (Sebastian Raschka, Google Research Tuning Playbook).*

---

# PART I: Universal Principles

What makes technical articles succeed with ML engineering audiences — transferable to any article you write.

---

## 1. Headlines & First Impressions

### Why This Matters Most

Headlines are the single most important element of your article. Research consistently shows that **~40% of your article's success is determined before anyone reads a single paragraph**. Your title is your article competing against every other link in someone's feed.

### The Data

- Headlines with **numbers** get 36% more clicks (e.g., "5 Techniques That..." vs "Techniques That...")
- Adding **brackets** to numbered headlines increases clicks another 38% (e.g., "5 Techniques [With Code]")
- Curiosity-driven questions outperform declarative statements
- Articles with poorly formatted titles are **ineligible for Medium curation** — the algorithm literally won't promote them

### Title Formulas That Work for ML Content

| Formula | Example |
|---------|---------|
| **Number + Outcome** | "7 PyTorch Training Optimizations That Cut Our Training Time by 8x" |
| **How To + Specific Result** | "How to Systematically Tune Deep Learning Models (Instead of Guessing)" |
| **Problem + Promise** | "Why Your PyTorch Model Trains Slower Than TensorFlow — And How to Fix It" |
| **Counterintuitive Claim** | "The Hyperparameter You're Tuning Is Probably the Wrong One" |
| **X Mistakes** | "5 Mistakes ML Engineers Make When Migrating to PyTorch" |

### Actionable Recommendations

1. **Write 5-10 title variations** before choosing. Don't settle for your first instinct.
2. **Keep titles under 60 characters** to avoid truncation in search results and Medium feeds.
3. **Front-load keywords**: "PyTorch Training Optimization: 7 Techniques..." beats "7 Techniques for Optimizing Your PyTorch Training..."
4. **Use a strong subtitle** (Medium displays it below the title). This is your second hook — expand on the promise without repeating the title. Example: Title = "How to Systematically Tune Deep Learning Models" → Subtitle = "A battle-tested methodology from migrating 50k lines of TF to PyTorch."
5. **Choose a preview image that signals technical depth** — architecture diagrams, training curves, or annotated code screenshots outperform stock photos for ML audiences. This image appears in feeds and notifications.

### Power Words for ML Titles

Use sparingly but effectively: *systematic, battle-tested, from scratch, step-by-step, practical, production-ready, reproducible, under the hood, deep dive, lessons learned.*

**Avoid**: *ultimate, hack, secret, revolutionary* — ML engineers are allergic to hype.

*Sources: Noah Kagan (100M article analysis), Medium Help Center, Scalenut SEO research, Matt Giaro (Medium virality)*

---

## 2. The Opening Hook

### The 15-Second Rule

Most readers decide within **15 seconds** whether to keep reading or bounce. Your opening paragraph is not a summary — it's a sales pitch for the rest of your article.

### 7 Proven Hook Techniques for Technical Content

**1. Problem-Focused Opening** (Most reliable for ML content)
> "You've run 47 hyperparameter sweeps. Each one takes 6 hours on 4 GPUs. Your validation accuracy hasn't budged in two weeks. Sound familiar?"

Why it works: Immediately builds connection — "this person understands my pain."

**2. Compelling Statistic**
> "Only 6% of algorithm presenters at top ML conferences share their code. Over 70% of researchers report failing to reproduce published experiments."

Why it works: Quantifies a problem readers intuitively feel, lending urgency to your solution.

**3. Curiosity Gap**
> "There's one step in systematic hyperparameter tuning that most engineers skip — and it costs them weeks of wasted compute."

Why it works: Withheld information creates cognitive tension that demands resolution.

**4. Scenario / Drop Into Action**
> "It's 2am. The training run you launched 18 hours ago just diverged. You check the config — learning rate 3e-4, same as always. Except this time, you're on PyTorch, and 'same as always' doesn't mean what you think."

Why it works: Places the reader in a vivid, recognizable moment. Emotional engagement before intellectual engagement.

**5. Unexpected Insight**
> "Adam in PyTorch and Adam in TensorFlow are not the same optimizer. The epsilon placement is different, and it changes convergence behavior."

Why it works: Signals "I know something you probably don't" — the reader's curiosity is hooked.

**6. Engaging Question**
> "What if the reason your PyTorch model underperforms your TensorFlow baseline has nothing to do with the model — and everything to do with how the framework handles convolutions?"

Why it works: Invites the reader to think, making them an active participant.

**7. Active / Bold Statement**
> "We migrated 50,000 lines of deep learning code from TensorFlow to PyTorch. It broke everything. Here's the systematic methodology we built to fix it."

Why it works: Establishes authority and scope immediately. The reader knows this will be substantive.

### What to Avoid in Openings

- "In this article, we will explore..." — Generic, passive, signals nothing unique
- Starting with definitions — "Deep learning is a subset of machine learning..." — Your audience knows this
- Lengthy personal introductions — Get to the problem first, establish credentials through the content itself
- Disclaimers — "I'm not an expert but..." — Either you have something valuable to say or you don't

### Actionable Recommendation

**Combine techniques.** Your strongest opening will likely merge 2-3 hooks. Example: Problem-focused + Bold statement:

> "We migrated 50,000 lines of TensorFlow training code to PyTorch. Within a week, every model performed worse. Not slightly worse — measurably, consistently, inexplicably worse. This article is about the systematic methodology we built to not only match TensorFlow performance, but exceed it."

*Sources: ProBlogger (11 opening strategies), TechFinitive (10 hook techniques), Doppler (writing for engineers)*

---

## 3. Narrative Architecture

### Three Frameworks That Combine

The most effective ML technical articles don't just dump information — they take the reader on a journey. Three narrative frameworks work particularly well for technical content, and they **layer on top of each other**.

### Framework 1: The Story Spine

Originally from improvisational theater, adapted for technical writing by Use Anvil:

```
Once upon a time...     → [Your context / starting point]
Every day...            → [The recurring problem]
One day...              → [The specific challenge that forced change]
Because of that...      → [Consequences, escalation]
Because of that...      → [Further consequences]
Until finally...        → [The solution / resolution]
And ever since...       → [The new reality + what readers can do]
```

**Adapted for ML content (Author as Character):**
1. Here's what we were doing (TF training pipeline, working well)
2. Then we encountered this problem (need for modern architectures, PyTorch ecosystem)
3. Why the problem mattered (falling behind SOTA, can't use DINOv3, multi-GPU, mixed precision)
4. What solutions we tried (direct translation — failed)
5. What we learned from failure (frameworks differ at fundamental level)
6. The methodology we built (systematic approach)
7. The results we achieved (matching then exceeding TF)
8. How readers can apply this (transferable methodology)

**Why it works:** The narrative structure triggers oxytocin release, improving understanding and long-term recall. Readers follow the "man in hole" arc — the most engaging story shape.

### Framework 2: Progressive Disclosure

From UX design (Nielsen Norman Group). Reveal information in layers:

- **Layer 1**: High-level concept (what and why)
- **Layer 2**: How it works (methodology overview)
- **Layer 3**: Detailed implementation (code, configs, specific numbers)
- **Layer 4**: Edge cases, pitfalls, advanced considerations

**Applied to technical articles:** Don't front-load every detail. Introduce a concept simply, let it breathe, then deepen. Readers who want the overview can stop; readers who want depth keep going.

**Key insight from the research:** Progressive disclosure improves three usability dimensions simultaneously — learnability, efficiency, and error reduction. People understand systems better when you help them prioritize.

### Framework 3: Gradual Discovery (Your Proposed Pattern)

A cycle that repeats for each major topic:

```
Problem to Solve → Method Introduced → Concrete Example → Pitfalls & Limits → (Next Problem)
```

This is particularly powerful because:
- Each cycle is **self-contained** — the reader gets value even if they stop
- The pitfalls/limits section **creates natural tension** that pulls the reader into the next cycle
- Each cycle **builds on the previous one** — compound understanding
- It mirrors the **scientific method** — hypothesis, experiment, results, limitations

### How They Combine

Use the **Story Spine** as your macro-level narrative arc (the article's overall journey). Use **Progressive Disclosure** within each section (simple first, then deep). Use **Gradual Discovery** as the repeating unit structure.

```
ARTICLE-LEVEL: Story Spine (setup → problem → escalation → resolution)
  └── SECTION-LEVEL: Gradual Discovery cycles
        └── WITHIN SECTIONS: Progressive Disclosure (concept → detail)
```

*Sources: Use Anvil (story spine for tech posts), Nielsen Norman Group (progressive disclosure), IxDF (progressive disclosure theory)*

---

## 4. Structure & Formatting for Readability

### How Readers Actually Behave

Readers **scan before they read**. Eye-tracking studies show an F-pattern: readers scan headings, first sentences, and bold text, then decide whether to read in detail. Your formatting is the roadmap that makes scanning productive.

### The Rules

**Paragraphs:** Keep to **2-3 sentences maximum**. In technical content, one idea per paragraph. White space is your friend — it gives the reader's brain room to process.

**Headings:** Use a clear hierarchy.
- **H2** = Major sections ("chapters"). Each H2 should answer one main question an engineer might search for.
- **H3** = Sub-topics within a section.
- **H4** = Specific details or examples within sub-topics (use sparingly).

**Lists:** Use bulleted lists for unordered items, numbered lists for sequential steps or ranked items. Lists break visual monotony and make information scannable.

**Tables:** Use for comparisons, parameter summaries, or any side-by-side data. ML audiences love tables — they're information-dense and scannable.

**Bold text:** Bold **key terms and important conclusions**. These are anchor points for scanning readers. Don't bold entire sentences — bold the 2-3 words that carry the meaning.

**Code blocks:** Use fenced code blocks with language tags for syntax highlighting. Keep code snippets **focused and short** (10-30 lines). If longer code is needed, show the critical section inline and link to the full version.

### Medium-Specific Formatting

- Use Medium's **T dropdown** to set proper heading hierarchy (Title, Subtitle, Section headings)
- **Title Case** for H2 headings, **Sentence case** for H3 and below — maintain consistency throughout
- Use `backtick` formatting for inline code, parameter names, and file paths
- Medium renders code blocks well but doesn't support syntax highlighting natively — consider using GitHub Gists for complex code
- Use **separator lines** (---) between major sections for visual breathing room
- Pull quotes (Medium's quote formatting) work well for key takeaways — readers highlight these

### Structural Principle: MECE

Organize main sections using the **MECE principle** (Mutually Exclusive, Collectively Exhaustive). Each H2 section should cover a distinct topic without overlapping other H2 sections. Together, they should cover the entire subject. No more than **3-4 major points per section** — beyond that, break into sub-sections.

*Sources: Nielsen Norman Group (formatting long-form content), WriteTech Hub (long-form structure), Linkible (structuring articles)*

---

## 5. Depth, Clarity & Technical Credibility

### The Long-Form Paradox

Counterintuitive finding from the 100M article analysis: **articles of 3,000-10,000 words received the most social shares** (averaging 8,859 shares). Short attention spans are real, but there's far less competition in deep content. Your long, thorough article will get shared precisely *because* it's the definitive resource.

**The key:** Long does not mean padded. Every paragraph must earn its place. Length should come from genuine depth — multiple perspectives, real data, concrete examples — not from throat-clearing or repetition.

### Jargon Calibration for ML Peers

Your audience is ML Research Engineers. They know what a learning rate is. They know what Adam is. **Do not define fundamentals.** This is the #1 sign of a junior writer — wasting your expert reader's time explaining things they already know.

However:
- **Do define** non-obvious terms specific to your methodology (e.g., "scientific parameters" vs "nuisance parameters" in the Tuning Playbook sense — this isn't standard ML terminology)
- **Do clarify** when you use a term in a specific way that might differ from common usage
- **Use consistent terminology.** Pick "hyperparameter sweep" or "hyperparameter search" and stick with it throughout

### The No-Hand-Waving Principle

ML engineers have finely tuned BS detectors. Every claim should be backed by:
- **Your own experimental data** (best — shows you actually did the work)
- **Published papers or benchmarks** (strong — establishes credibility by association)
- **Reasoning from first principles** (acceptable — shows deep understanding)

**Never:** "It's well-known that..." / "Experts agree..." / "Research shows..." without a specific citation or your own data.

### Active Voice & Directness

| Weak | Strong |
|------|--------|
| "It was observed that the learning rate schedule impacts convergence" | "We found that the learning rate schedule directly impacts convergence" |
| "The model can be trained using mixed precision" | "Train your model with mixed precision — it halves memory usage with negligible accuracy impact" |
| "Consideration should be given to..." | "Consider..." |

### Acknowledging Limitations

Paradoxically, **acknowledging what you don't know increases credibility**. The Google Research Tuning Playbook does this brilliantly — it flags areas where more research is needed rather than pretending to have all answers. Your readers are sophisticated enough to know that no methodology is universal. Transparency about limitations builds trust.

*Sources: CMU ML Blog guidelines, Noah Kagan (100M article analysis), Doppler (writing for engineers), Google Research Tuning Playbook (stylistic model)*

---

## 6. Visual Strategy

### When to Use What

| Visual Type | Use For | Example in ML Context |
|-------------|---------|----------------------|
| **Architecture diagrams** | System overviews, data flow | Training pipeline diagram, model architecture |
| **Flowcharts** | Decision processes, methodology steps | "Which optimizer to use" decision tree, experiment workflow |
| **Tables** | Precise numerical comparisons | Hyperparameter configs → metrics, framework feature comparison |
| **Line charts** | Trends over time/iterations | Training curves, learning rate schedules, convergence plots |
| **Bar charts** | Comparing discrete categories | Model A vs B vs C accuracy, speedup per optimization technique |
| **Heat maps** | Multi-dimensional parameter interactions | Hyperparameter grid search results |
| **Code snippets** | Implementation details | Key config differences, code changes per optimization |
| **Before/After** | Impact demonstration | TF code vs PyTorch code, training curves before/after optimization |

### The 75-100 Word Rule

Research shows articles with a visual element every **75-100 words** receive **2x more shares** than text-only articles. For a 4,000-word article, that means roughly **40-50 visual break points**. This doesn't mean 50 images — it includes code blocks, tables, diagrams, pull quotes, and formatted callouts.

### Presenting Experimental Results

This is where ML articles succeed or fail. Your audience is trained to read results critically.

**Do:**
- Show **error bars / variance** across multiple runs — point estimates are suspicious
- Include **wall-clock time AND accuracy together** — speed without quality context is meaningless
- Specify **hardware** (GPU model, count, VRAM) — results aren't reproducible without this
- Use **progressive results tables** that show cumulative impact: "baseline → +technique A → +technique B → all combined"
- Show **training curves**, not just final numbers — the trajectory reveals more than the endpoint

**Don't:**
- Show results without context on why they matter
- Present untuned baselines as fair comparisons
- Include raw training logs (summarize instead)
- Use pie charts for anything (ML audiences find them imprecise)

### Color and Design

- Use color purposefully, not decoratively — color should encode information
- Maintain consistent color coding across all figures (e.g., always blue for PyTorch, always orange for TF)
- Ensure figures are readable on both light and dark backgrounds (Medium supports dark mode)
- Label axes clearly — unlabeled axes are a cardinal sin in ML visualization

*Sources: Noah Kagan (visual frequency analysis), CMU ML Blog guidelines, Sebastian Raschka (PyTorch training blog as exemplar), Comet ML (communicating data science results)*

---

## 7. Storytelling in Technical Content

### The 22x Retention Factor

Research in cognitive science shows that humans retain stories **22 times better** than facts presented in isolation. Stories activate multiple brain regions simultaneously — language, motor, sensory, and emotional centers — creating richer memory encoding.

This doesn't mean your article should read like a novel. It means **wrapping technical insights in narrative context** dramatically increases what your reader retains and applies.

### The "Author as Character" Technique

The most effective ML blog posts position the author as a character in the story:

- **You faced a real challenge** (migrating 50k LOC from TF to PyTorch)
- **You made mistakes** (direct translation failed, models performed worse)
- **You iterated toward a solution** (built systematic methodology)
- **You achieved measurable results** (matched then exceeded TF performance)
- **You share what you learned** (so the reader can skip the mistakes)

This structure is powerful because it's **authentic** — ML engineers can tell when someone actually did the work versus when someone is writing from theory.

### The Context → Story → Results Arc

For each major section of your article:

1. **Context:** Why this matters, what problem you faced
2. **Story:** What you tried, what failed, what worked (include the messy middle)
3. **Results:** What you achieved, with data

The messy middle is the most valuable part. ML engineers are buying your failure stories, not your success stories. The failures are where the transferable knowledge lives.

### Second Person for Reader as Protagonist

Strategically use second person ("you") to make the reader feel like they're doing the work:

> "When you first compare training curves between your TF and PyTorch models, you'll likely see the PyTorch version converge slower. Your instinct will be to adjust the learning rate. Resist that instinct — the problem is almost certainly in the optimizer defaults."

This technique transforms passive reading into active engagement.

### Humor and Personality

ML engineers appreciate **dry wit** and **self-deprecating honesty** about the messiness of real research. A well-placed joke about GPU costs or the 47th failed hyperparameter sweep creates rapport. But humor should never interrupt the technical flow — it should punctuate it.

**Good:** "After three weeks of debugging, I discovered the issue was a single missing `model.train()` call. I briefly considered a career in carpentry."

**Bad:** "LOL training neural networks is so hard am I right? 😂" — Don't.

*Sources: Use Anvil (story spine for tech), ClickHelp (storytelling in technical writing), Kittelson (elevating technical reports through storytelling)*

---

## 8. Reproducibility & Code

### What ML Engineers Value Most

From CMU's research on reproducibility in ML:
- Only **6% of algorithm presenters** at top conferences share their code
- Over **70% of researchers** report failure to reproduce others' experiments
- This is your opportunity — **reproducible content is rare and therefore extremely valued**

### The Reproducibility Checklist for Blog Posts

Every ML article should include (inline or linked):

| Element | Where | Why |
|---------|-------|-----|
| **Hyperparameter values** (all of them) | Table in results section | Readers need exact configs to reproduce |
| **Hardware specs** | Footnote or dedicated section | GPU model, count, VRAM, CPU, RAM — performance is hardware-dependent |
| **Software versions** | Top of article or prerequisites section | PyTorch version, CUDA version, key library versions |
| **Code** (working, tested) | Inline snippets + linked repo | Readers WILL try to run your code — it must work |
| **Random seeds** | In code or config | Reproducibility requires determinism |
| **Dataset details** | Method section | Size, splits, preprocessing, any filtering |
| **Training time** | Results table | Wall-clock time calibrates reader expectations |
| **Statistical reporting** | Results | Variance across seeds/runs, not just best result |

### Code Quality in Blog Posts

- **Working code only.** No pseudocode, no "the rest is left as an exercise." ML engineers will copy-paste and run your code. If it doesn't work, you lose all credibility instantly.
- **Short, focused snippets.** Show the critical 10-30 lines inline. Link to the full implementation in a repo.
- **Annotate tensor dimensions.** This is the most common confusion point when reading others' code.
- **Show the diff.** When presenting an optimization, show what changed, not the entire file. Before/after is more instructive than the final version alone.

### Template for Presenting Code

```
[Brief description of what this code does and why]

[Code block — 10-30 lines, focused on the key change]

[1-2 sentences explaining the non-obvious parts]

[Metrics: what this change achieved]
```

*Sources: CMU ML Blog (reproducibility research), Sebastian Raschka (PyTorch optimization blog structure), Google Research Tuning Playbook*

---

## 9. Engagement, CTAs & Community

### The Science of Sharing

From the analysis of 100 million articles:
- **Awe** is the #1 emotion driving shares (25% of viral technical content)
- "Aha moment" content — where readers gain a new mental model — generates the most engagement
- Content that challenges conventional wisdom gets shared because people share to signal insight

### Creating "Aha Moments"

In ML technical content, aha moments come from:
- **Revealing hidden mechanisms:** "Adam in PyTorch places epsilon inside the square root; TensorFlow places it outside. This changes convergence behavior on sparse gradients."
- **Connecting disparate concepts:** "The reason your PyTorch model trains slower isn't the optimizer — it's the convolution padding. TF uses 'SAME' padding which maps to a different implementation than PyTorch's zero-padding."
- **Quantifying intuition:** "We tested 200 configurations. Label smoothing improved accuracy in 83% of experiments, but only when dropout was below 0.2."

### Strategic CTAs (Calls to Action)

Research shows **mid-content CTAs convert 121% higher** than end-of-article CTAs alone. Best practice is to include CTAs at three points:

**Beginning (soft):**
> "By the end of this article, you'll have a systematic framework for tuning any PyTorch model — no more guessing."

**Mid-content (contextual):**
> "Try this on your own model before reading the next section — seeing the difference firsthand is more convincing than any chart I can show you."

**End (direct):**
> "If this methodology saved you time, share it with your team. And comment below — what's the most surprising hyperparameter interaction you've discovered?"

### Quotable Sentences

Medium readers can **highlight** text, and highlights are weighted heavily by the algorithm. Deliberately craft sentences that readers will want to highlight:

- "The hyperparameter you spend the most time tuning is rarely the one that matters most."
- "A systematic methodology beats intuition not because intuition is wrong, but because it doesn't scale."
- "The cost of a bad hyperparameter search isn't just compute — it's the conclusions you draw from biased results."

These sentences should be **insight-dense, concise, and standalone** — they should make sense even without the surrounding paragraphs.

### Comment Engagement Strategy

- Ask **specific, answerable questions** at the end (not vague "what do you think?")
- Example: "What's the biggest surprise you encountered migrating frameworks? I'd bet money it was related to default numerical precision."
- Respond to comments promptly in the first 48 hours — active discussion signals to Medium's algorithm that the content is engaging

*Sources: Noah Kagan (100M article analysis), Crazy Egg (CTA strategies), MetroQuest (community engagement), Medium Help Center*

---

## 10. Two-Part Series Strategy

### Why Series Work for Deep Technical Content

- Shows deep expertise (not surface coverage)
- Creates natural return visits (built-in audience retention)
- Internal linking between parts boosts SEO
- Generates bookmark-worthy reference material
- Can later become a workshop, talk, or course

### Critical Rule: Standalone Value Per Part

**Each part must be valuable on its own.** Readers arriving via search may find Part 2 first. Part 1 should not be a teaser — it should be a complete, valuable article that also sets up Part 2.

### Linking Strategy

Place navigation links at **both the top and bottom** of each article:

**Part 1 top:** *(No link needed — it's the first part)*
**Part 1 bottom:** "Continue to Part 2: [Title] →"

**Part 2 top:** "This builds on Part 1: [Title]. Key concepts: [2-3 sentence summary of what Part 1 established]"
**Part 2 bottom:** "← Back to Part 1: [Title]"

Use **keyword-rich anchor text**, not "click here" or "Part 2."

### Publication Timing

- Publish Part 2 within **1-2 weeks** of Part 1 — long enough for Part 1 to gain traction, short enough that readers remember it
- If the gap is longer, include a brief recap in Part 2's introduction
- Promote both parts when Part 2 launches (Part 1 gets a second wave of traffic)

### Cross-Referencing

- In Part 1, naturally mention what Part 2 will cover at relevant moments (not forced — organic teases)
- In Part 2, reference specific results or concepts from Part 1 (this rewards readers who read both)
- Use consistent formatting, visual style, and tone across both parts

### The Transition Between Parts

The end of Part 1 should create **constructive tension** — a question that Part 2 answers:

> "We've now matched TensorFlow performance in PyTorch. But matching isn't enough — the whole point of migrating was to access capabilities TF couldn't offer. Part 2 covers the systematic methodology we built to not just match, but surpass our previous results."

This is not a cliffhanger (Part 1 stands alone). It's a promise that there's more valuable content ahead.

*Sources: ProBlogger (blog series strategy), ProBlogger (10 steps for successful series)*

---

## 11. Medium Platform Optimization

### How Medium's Algorithm Works

Medium's algorithm surfaces content based on:

1. **Read time** — Calculated at ~265 words/minute, adjusted for images and code complexity. Longer read times signal depth.
2. **Read ratio** — What percentage of people who start your article finish it. A high read ratio signals quality.
3. **Claps** — Medium's engagement metric (readers can clap up to 50 times). More claps = more visibility.
4. **Highlights** — When readers highlight text, it signals high-quality, quotable content.
5. **Responses** — Active discussion boosts visibility.
6. **Followers gained** — If reading your article causes people to follow you, the algorithm treats this as a strong quality signal.

### Practical Optimization

**Tags:** Use 3-5 tags for discoverability. For ML content, mix broad and specific:
- Broad: `Machine Learning`, `Deep Learning`, `Data Science`
- Specific: `PyTorch`, `Hyperparameter Tuning`, `MLOps`

**Meta description:** Keep under 160 characters. This appears in search results and should complement (not repeat) the title.

**Publication timing:**
- Tuesday is the highest-engagement day on Medium overall
- Morning (8-10am) in your target audience's timezone
- For ML content, consider Monday-Wednesday when engineers are in work/learning mode

**Read time sweet spot:** For in-depth technical content targeting ML engineers, aim for **8-15 minute read time** (roughly 2,000-4,000 words). Under 3 minutes signals shallow content. Over 20 minutes risks losing readers unless the content is exceptional.

### Distribution After Publishing

Shares drop **96% after 3 days.** Content can be revived by resharing a week later.

1. **Day 0:** Publish. Share on Twitter/X and LinkedIn with a hook (not just the title — write a thread or mini-insight)
2. **Day 0-2:** Engage with every comment. Post in relevant communities: Reddit r/MachineLearning, Hacker News, ML Discord servers
3. **Day 7:** Reshare to different audiences. Frame it differently for each platform.
4. **Ongoing:** Link to it from future articles. Update it if you get new results.

**Influencer effect:** Research shows one influencer sharing your article increases total shares by 31.8%. Five influencers sharing = nearly 4x shares. Identify 3-5 people in the ML community whose audience would benefit, and share your article directly with them (with a personalized note about why their audience would care).

*Sources: Medium Help Center (read time), Medium Course (algorithm mechanics), Noah Kagan (distribution timing), Matt Giaro (Medium virality)*

---

# PART II: Your Article Blueprint

Applying the principles above to your specific two-part article on TF→PyTorch migration and systematic tuning methodology.

---

## 12. Article Series Overview

### The Two-Part Arc

| | Part 1 | Part 2 |
|---|--------|--------|
| **Topic** | TF→PyTorch Migration | Systematic Tuning Methodology |
| **Reader Journey** | "This is harder than I thought" → "There's a systematic way" | "Guessing isn't enough" → "Here's a rigorous framework" |
| **Emotional Arc** | Empathy → Competence | Curiosity → Mastery |
| **Standalone Value** | How to migrate and verify correctness | How to systematically tune any DL model |
| **Target Length** | ~3,000-4,000 words (10-15 min read) | ~4,000-5,000 words (15-20 min read) |

### The Narrative Thread

The migration story (Part 1) naturally creates the need for the tuning methodology (Part 2). The connection: migrating frameworks reveals that "same configuration" doesn't mean "same behavior" — which forces you to develop a principled approach to finding the right configuration in the new framework. This insight bridges the two parts seamlessly.

### Audience Journey

```
Part 1: "I need to migrate" or "I'm curious about framework differences"
    → Discovers: Migration is non-trivial, frameworks differ fundamentally
    → Learns: Systematic verification methodology (dummy model → overfit → validate)
    → Takes away: Confidence to attempt their own migration

Part 2: "I need to tune my model" or "My PyTorch model underperforms"
    → Discovers: Tuning is a science, not an art
    → Learns: Scientific vs nuisance parameters, quasi-random search, phased experiments
    → Takes away: A complete methodology they can apply immediately
```

---

## 13. Part 1 Blueprint: TF→PyTorch Migration

### Suggested Title Options

1. "We Migrated 50K Lines of Deep Learning from TensorFlow to PyTorch. Here's What Broke (And How We Fixed It)"
2. "The Hidden Differences Between TensorFlow and PyTorch That No One Warns You About"
3. "From TF to PyTorch: A Systematic Migration Methodology for Production ML Systems"

### Opening Hook (Recommended: Combine Bold Statement + Unexpected Insight)

> "We migrated 50,000 lines of deep learning code from TensorFlow to PyTorch. Within a week, every model performed worse — not because our code was wrong, but because the two frameworks fundamentally disagree on how convolutions, optimizers, and even image resizing should work. This article is about the systematic methodology we built to find and fix every one of these differences."

### Suggested Section Flow (Gradual Discovery Pattern)

**Section 1: Why Migrate?** (Problem → Method intro)
- The growing gap: PyTorch's dominance in research (cite adoption numbers, HuggingFace ecosystem, paper implementations)
- What you couldn't do on TF: DINOv3, multi-GPU training, mixed precision, latest architectures
- Frame it as a forced move, not a preference — this builds empathy

**Section 2: Why It's Harder Than You Think** (Deeper problem → Method detail)
- Scale of the challenge: 50k LOC of DL, 15k LOC of TF-specific code
- No unit tests in the original — can't regression-test the migration
- The fundamental differences:
  - Convolution padding: TF's SAME vs PyTorch's explicit padding (link to SO reference)
  - Adam optimizer: epsilon placement differs (cite PyTorch forums discussion)
  - Data format: NCHW vs NHWC
  - Image resizing: different interpolation implementations
  - Pretrained weight formats differ
- Even loading an image and resizing gives different tensors — you must work with raw tensors directly
- *Pitfall:* Direct translation is a trap. "Same code" ≠ "same behavior"

**Section 3: The Verification Ladder** (Method → Concrete example)
- **Step 1: Dummy model equivalence.** Build a minimal model (dense layers only — no conv strides). Load identical weights in both frameworks. Compare inputs, outputs at each layer, loss, and gradients. Allow small relative tolerance for backend matmul differences.
- **Step 2: Overfit the dummy.** If you can't memorize 2 batches of random data, something is fundamentally broken. This is the sanity check that catches framework-level bugs.
- **Step 3: Overfit the real model.** Same test with Xception/DINOv3 — overfit on 2 batches. If this works, the model+training loop is correct.
- **Step 4: Validate on production data.** Run on real datasets, compare metrics to TF baseline.

Include code snippets for the verification at each step. Show the actual test file structure.

**Section 4: Lessons Learned** (Pitfalls → Transition to Part 2)
- Test as early as possible
- Build minimal dummy versions first
- Lost knowledge in the codebase (undocumented decisions) — you can only test with and without
- Even "matching" TF isn't enough — the optimal configuration for PyTorch is different
- *Transition:* "We matched TF performance. But that was just the starting point. The real gains came from developing a systematic tuning methodology — which is Part 2 of this series."

### Visual Elements for Part 1

- Architecture diagram of the training pipeline (before/after migration)
- Side-by-side code comparison: TF vs PyTorch for a key operation (conv, optimizer setup)
- Table: Framework differences inventory (operation, TF behavior, PyTorch behavior, impact)
- Training curves: TF baseline vs naive PyTorch port vs verified PyTorch
- The verification ladder as a flowchart

---

## 14. Part 2 Blueprint: Systematic Tuning Methodology

### Suggested Title Options

1. "A Systematic Methodology for Tuning Deep Learning Models (Based on the Google Research Tuning Playbook)"
2. "Stop Guessing: How We Systematically Tuned PyTorch Training to Beat Our TensorFlow Baseline"
3. "The 5-Phase Experiment Workflow That Turned Hyperparameter Tuning From Art Into Science"

### Opening Hook (Recommended: Problem-Focused + Curiosity Gap)

> "Most hyperparameter tuning looks like this: change the learning rate, run for 6 hours, check the result, repeat. After migrating to PyTorch, we had hundreds of knobs to tune and no systematic way to turn them. So we built one — a 5-phase methodology based on the Google Research Tuning Playbook that turned guesswork into science. The first thing it taught us: the parameter you think matters most probably doesn't."

### Suggested Section Flow (Gradual Discovery Pattern)

**Cycle 1: The Problem With Ad-Hoc Tuning**
- *Problem:* After migration, "same hyperparameters" gives different results. Need to find PyTorch-optimal configuration.
- *Method:* Introduce the Google Research Tuning Playbook framework — separate scientific parameters (what you're studying) from nuisance parameters (what you must control)
- *Example:* "We wanted to know if TrivialAugment helps. But comparing it fairly requires tuning its sub-parameters (magnitude bins, probability) for each augmentation type. Without this separation, you're comparing tuned-A vs untuned-B."
- *Pitfall:* Most engineers conflate scientific and nuisance parameters → biased conclusions

**Cycle 2: Designing Rigorous Experiments**
- *Problem:* Even with the right framework, how do you efficiently explore the search space?
- *Method:* Quasi-random sampling (Halton sequences) over grid search or random search — better coverage with fewer trials
- *Example:* Show a concrete experiment design: "Label smoothing study: scientific param = label_smoothing (0.0-0.2, uniform), nuisance params = dropout (0.1-0.3), image_size ([224, 256]). 15 configs via Halton sequence."
- *Pitfall:* Grid search wastes compute on correlated dimensions. Random search is better but not optimal. Quasi-random is the sweet spot.

**Cycle 3: The 5-Phase Experiment Workflow**
- *Problem:* Even well-designed experiments fail in practice — wrong YAML configs, unlogged parameters, GPU crashes
- *Method:* The phased approach: Design → Generate → Verify → Document → Launch
- *Example:* Walk through a real experiment from research question to results:
  1. Phase 1: Collaborative design (research question, parameter selection, ranges from literature)
  2. Phase 2: YAML generation (Halton sequences, TEST config for validation)
  3. Phase 3: Pre-launch verification (hparam logging check, git state, server availability, TEST yaml run)
  4. Phase 4: Documentation (hypothesis before results — prevents post-hoc rationalization)
  5. Phase 5: Full deployment and monitoring
- *Pitfall:* Skipping the TEST yaml phase → discovering config errors after 30 experiments have run for 6 hours each

**Cycle 4: Reading Results and Iterating**
- *Problem:* You have 30 experiment results. How do you actually interpret them?
- *Method:* Systematic analysis — best per scientific parameter value, interaction effects, convergence analysis
- *Example:* Show a real results table and walk through the analysis. "Label smoothing of 0.1 outperformed in 83% of configs, but only when combined with dropout < 0.2. This interaction would have been invisible in a one-at-a-time search."
- *Pitfall:* Drawing conclusions from single runs without considering variance across nuisance parameters

**Cycle 5: The Compound Effect**
- *Problem:* Individual improvements are modest. How do they stack?
- *Method:* Cumulative optimization — apply discoveries sequentially, re-verify at each step
- *Example:* Progressive results table showing cumulative impact: baseline → +correct optimizer → +tuned augmentation → +regularization → final. Show the total improvement from TF baseline to fully optimized PyTorch.
- *Pitfall:* Assuming optimizations are independent — interaction effects can make the sum less (or more) than the parts

### Closing Section: Making It Your Own

- The methodology is framework-agnostic — works for JAX, TF, PyTorch, anything
- Open-source the experiment generation tools if possible
- Key principle: "Systematic methodology beats intuition not because intuition is wrong, but because it doesn't scale"
- CTA: "What's your tuning methodology? Comment below with the most surprising hyperparameter interaction you've discovered."

### Visual Elements for Part 2

- Flowchart: 5-phase experiment workflow (the core visual, reference repeatedly)
- Table: Scientific vs nuisance parameter examples across common experiment types
- Diagram: Halton sequence sampling vs grid vs random (2D parameter space visualization)
- Results table: Real experiment showing progressive improvement
- Training curves: Best configs compared across different experiments
- Heat map: Parameter interaction effects (if data available)

---

## 15. Common Pitfalls to Avoid

The research identified 10 engagement killers. Here's how each maps to risks in your specific content:

### 1. Jargon Overload (HIGH RISK)
Your content is dense with ML-specific terms. While your audience knows the basics, terms like "nuisance parameters" (in the Tuning Playbook sense), "Halton sequences", and "scientific parameters" need explicit definition on first use. **Calibrate:** define methodology-specific terms, skip explaining SGD.

### 2. No Visuals (MEDIUM RISK)
Training methodology articles risk becoming walls of text and tables. **Counter:** include training curve comparisons, workflow diagrams, parameter space visualizations. Aim for a visual element every 100-150 words.

### 3. Weak Headline (HIGH RISK)
Technical authors often default to descriptive-but-boring titles. "A Methodology for Hyperparameter Tuning" will get zero clicks. **Counter:** use the formulas from Section 1. Include a concrete result in the title if possible.

### 4. Missing CTAs (MEDIUM RISK)
Technical authors often end abruptly after the last result. **Counter:** end each part with a specific, engaging CTA. Ask a concrete question, not "what do you think?"

### 5. No Narrative (HIGH RISK)
The temptation is to present the methodology as a reference manual. **Counter:** tell the story of how you developed it. The failures and iterations are the most valuable content.

### 6. Padding Without Depth (LOW RISK)
You have genuine depth — this is not a risk for the content, but watch for padding in the TF→PyTorch section if you're uncertain about audience interest. **Counter:** keep Part 1 tighter and more focused than Part 2.

### 7. Unverifiable Claims (LOW RISK)
You have real experimental data. **Counter:** show it. Include the actual numbers, not "significant improvement."

### 8. Poor Code Quality (MEDIUM RISK)
Inline code snippets that don't run, or that assume context the reader doesn't have. **Counter:** test every code block. Include necessary imports. Annotate tensor dimensions.

### 9. Ignoring Distribution (HIGH RISK)
Even great articles get zero views without promotion. **Counter:** follow the distribution strategy in Section 11. Share on Reddit r/MachineLearning, Twitter/X, LinkedIn. Tag relevant people.

### 10. Inconsistent Series Quality (MEDIUM RISK)
Part 2 is the meat — risk is that Part 1 feels like "just the setup." **Counter:** make Part 1 genuinely valuable on its own. The verification ladder methodology is interesting independent of Part 2.

---

# APPENDICES

---

## Appendix A: Source Bibliography

### Content Strategy & Virality
- Noah Kagan — "How to Create Viral Content: 10 Insights from 100 Million Articles" (noahkagan.com) — Data-driven analysis of what makes content go viral
- Matt Giaro — "How To Go Viral On Medium & Get 1 Million Views" (mattgiaro.com) — Medium-specific virality strategies
- ContentStudio — "A Comprehensive Guide to Create Engaging Content in 2025" (contentstudio.io) — Engagement optimization
- Ocoya — "Creating Viral Content: Essential Strategies for Maximum Impact" (blog.ocoya.com) — Distribution and amplification
- OutreachZ — "Viral Content: What Makes Posts Go Viral" (outreachz.com) — Emotional triggers in sharing
- GreenGeeks — "How to Help Make Content Go Viral" (greengeeks.com) — Content lifecycle management

### Technical Writing
- MDN Blog — "Creating Effective Technical Documentation" (developer.mozilla.org) — Technical documentation best practices
- Nitor Infotech — "5 Best Practices for Technical Writing" (nitorinfotech.com) — Clarity and accessibility
- ProEdit — "Technical Writing: 6 Best Practices" (proedit.com) — Professional technical writing standards
- Document360 — "Top 11 Essential Tips to Improve Technical Writing" (document360.com) — Readability optimization
- Archbee — "10 Tips for Writing Effective Technical Documentation" (archbee.com) — Documentation structure

### Storytelling in Technical Content
- Use Anvil — "Writing Technical Blog Posts with the Story Spine" (useanvil.com) — Story spine framework adapted for tech
- ClickHelp — "Storytelling in Technical Writing" (clickhelp.com) — Narrative techniques
- Kittelson & Associates — "Elevating Technical Reports Through Storytelling" (kittelson.com) — Story arc in reports
- TechWriters Substack — "The Different Flavours of Narrative Technical Writing" (techwriters.substack.com) — Narrative styles

### Article Structure
- Nielsen Norman Group — "Progressive Disclosure" (nngroup.com/articles/progressive-disclosure) — Information layering theory
- IxDF — "Progressive Disclosure" (ixdf.org) — Design pattern theory
- WriteTech Hub — "Planning and Structuring Long-Form Technical Content" (writetechhub.org) — Long-form structure
- Linkible — "How to Structure Long-Form Articles" (linkible.io) — Article organization
- NN/G — "Formatting Long-Form Content" (nngroup.com/articles/formatting-long-form-content) — Readability formatting
- DEV Community — "How to Structure a Perfect Technical Tutorial" (dev.to) — Tutorial template
- Draft.dev — "Technical Tutorials" (draft.dev/learn/technical-tutorials) — Tutorial best practices
- freeCodeCamp — "How to Write a Good Technical Tutorial" (freecodecamp.news) — Tutorial writing

### ML-Specific
- CMU ML Blog — "Submission Guidelines" (blog.ml.cmu.edu/submissions) — ML blog writing standards
- CMU ML Blog — "Reproducibility in ML Research" (blog.ml.cmu.edu/2020/08/31/5-reproducibility) — Reproducibility crisis data
- Sebastian Raschka — "PyTorch Models Train (Much) Faster" (sebastianraschka.com) — Exemplar ML optimization blog
- Google — "Deep Learning Tuning Playbook" (developers.google.com/machine-learning/guides/deep-learning-tuning-playbook) — Tuning methodology reference
- Alluxio — "Top Tips for PyTorch Model Training Performance Tuning" (alluxio.io) — PyTorch optimization
- Ali Shafique — "PyTorch Training Optimizations: Throughput with GPU Profiling" (medium.com/@alishafique3) — GPU optimization
- Comet ML — "A Data Scientist Guide to Communicating Results" (medium.com/comet-ml) — ML result presentation
- TraininData — "The Ultimate Guide to Deep Learning Hyperparameter Tuning" (blog.trainindata.com) — HP tuning overview

### Medium Platform
- Medium Help Center — "Read Time" (help.medium.com) — How read time is calculated
- Medium Help Center — "Using the Story Editor" (help.medium.com) — Formatting guide
- Medium Blog — "Improvements to Titles, Subtitles, and Headings" (blog.medium.com) — Title formatting
- Medium Course — "How Medium Calculates Read Time" (mediumcourse.com) — Algorithm details
- Saifullah Ghanghro — "How Medium Pays Writers" (medium.com/@Saifullah-Ghanghro) — Monetization mechanics
- Artistic Hive — "Writing for Medium - Complete Guide" (artistichive.com) — Platform best practices
- The Side Blogger — "A Guide to Writing on Medium in 2025" (thesideblogger.com) — Updated Medium guide

### Engagement & CTAs
- ProBlogger — "11 Ways to Open a Post and Get Reader Engagement" (problogger.com) — Hook techniques
- ProBlogger — "Blog Post Series" (problogger.com) — Series strategy
- ProBlogger — "10 Steps to Writing a Successful Series" (problogger.com) — Series planning
- TechFinitive — "10 Hook Techniques Every Tech Content Creator Should Use" (techfinitive.com) — Tech-specific hooks
- Crazy Egg — "6 Powerful Blog CTAs" (crazyegg.com) — CTA placement and design
- MetroQuest — "Drive Engagement Using Powerful Calls to Action" (metroquest.com) — Community CTAs
- Doppler — "Writing Better Blog Content for Software Engineers" (doppler.com) — Engineer-focused writing

### SEO & Distribution
- Scalenut — "Meta Title Length Best Practices, 2026" (scalenut.com) — Title optimization
- Zyppy — "The Best Title Tag Length for SEO" (zyppy.com) — Character limits
- BigRedSEO — "Article Writing For SEO In 2026" (bigredseo.com) — SEO best practices
- Straight North — "How to Optimize Title Tags & Meta Descriptions in 2026" (straightnorth.com) — Meta optimization

### Blogging Mistakes
- Husam Jandal — "10 Common Blog Mistakes Driving Your Readers Away" (husamjandal.com) — Engagement killers
- Feather — "31 Common Blogging Mistakes And How To Fix Them" (feather.so) — Comprehensive mistake list
- Pixel2Pixel — "12 Blogging Mistakes Costing You Readers" (pixel2pixeldesign.com) — Reader retention

---

## Appendix B: Headline Formula Cheat Sheet

### Quick-Reference Formulas for ML Content

| # | Formula | Template | Example |
|---|---------|----------|---------|
| 1 | Number + Outcome | "N [Things] That [Result]" | "7 PyTorch Optimizations That Cut Training Time by 8x" |
| 2 | How-To + Specific | "How to [Action] [Specific Thing]" | "How to Systematically Tune Any Deep Learning Model" |
| 3 | Problem + Fix | "Why [Problem] — And How to Fix It" | "Why Your PyTorch Model Trains Slower Than TF — And How to Fix It" |
| 4 | Counterintuitive | "[Surprising Claim About Known Topic]" | "The Hyperparameter You Tune Most Is Probably the Wrong One" |
| 5 | Mistakes | "N Mistakes [Audience] Make When [Activity]" | "5 Mistakes ML Engineers Make When Tuning Hyperparameters" |
| 6 | Story + Scale | "We [Did X]. Here's What [Happened/Learned]" | "We Migrated 50K Lines from TF to PyTorch. Here's What Broke" |
| 7 | Framework + Audience | "A [Adjective] [Framework] for [Audience Activity]" | "A Systematic Methodology for Tuning Production DL Models" |
| 8 | Comparison | "[A] vs [B]: [What You Need to Know]" | "Grid Search vs Quasi-Random Sampling: What 200 Experiments Taught Us" |

### Power Words (Use These)
*systematic, battle-tested, reproducible, step-by-step, practical, production-ready, from scratch, under the hood, deep dive, lessons learned, what we learned, comprehensive*

### Avoid (ML Audience Red Flags)
*ultimate, revolutionary, game-changing, hack, secret, insane, mind-blowing, you won't believe*

### Title Length Rules
- Main title: **50-60 characters** (avoids search truncation)
- Subtitle: **Up to 120 characters** (expand the promise, don't repeat)
- Combined: should convey topic + value + audience

---

## Appendix C: Pre-Publish Checklist

### Before Publishing — Verify Each Item

**Content Quality**
- [ ] Title is under 60 characters and uses a proven formula
- [ ] Subtitle expands on the title's promise without repeating it
- [ ] Opening hook grabs attention within 15 seconds (read it out loud)
- [ ] Every section follows the Gradual Discovery pattern (problem → method → example → pitfall)
- [ ] No undefined jargon — methodology-specific terms are explained on first use
- [ ] All claims are backed by data, citations, or first-principles reasoning
- [ ] Limitations and caveats are explicitly acknowledged
- [ ] The article has standalone value (doesn't require reading another article to be useful)

**Structure & Formatting**
- [ ] Paragraphs are 2-3 sentences maximum
- [ ] H2/H3 headings create a scannable table of contents
- [ ] Bold text highlights key terms and conclusions
- [ ] Code blocks have language tags for syntax highlighting
- [ ] Tables are used for comparisons and parameter summaries
- [ ] Visual element every 100-150 words (image, diagram, table, code block, or pull quote)

**Visuals**
- [ ] All figures have clear labels, titles, and legends
- [ ] Color is used consistently across all charts (same color = same thing)
- [ ] Error bars / variance are shown where applicable
- [ ] Hardware specs are noted alongside performance claims
- [ ] Training curves are included (not just final metrics)

**Code & Reproducibility**
- [ ] Every code snippet has been tested and runs
- [ ] Tensor dimensions are annotated in code comments
- [ ] Hyperparameter values are listed explicitly (in tables, not buried in text)
- [ ] Software versions are specified (PyTorch, CUDA, key libraries)
- [ ] Random seeds are documented
- [ ] Link to full code repository is included

**Engagement**
- [ ] Beginning CTA sets expectation of value
- [ ] Mid-content CTA encourages the reader to try something
- [ ] End CTA asks a specific, answerable question
- [ ] At least 3-5 "highlightable" standalone insight sentences
- [ ] For series: navigation links at top AND bottom

**Medium-Specific**
- [ ] Title formatted using Medium's T dropdown (not manually bolded)
- [ ] Tags: 3-5 relevant tags selected (mix of broad and specific)
- [ ] Preview image is set and looks good in feed format
- [ ] Read time is 8-15 minutes (check after publishing)
- [ ] Meta description is under 160 characters

**Distribution Plan**
- [ ] Twitter/X thread or hook prepared
- [ ] LinkedIn post prepared (different framing than Twitter)
- [ ] Reddit communities identified (r/MachineLearning, r/pytorch)
- [ ] 3-5 people in ML community to share with personally
- [ ] Day-7 reshare reminder set

