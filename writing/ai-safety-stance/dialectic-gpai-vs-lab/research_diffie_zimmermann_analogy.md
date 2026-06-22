# Research — The Diffie/Zimmermann Analogy: Stress-test for Louis's 2026 GPAI move

**Written:** 2026-04-13
**Frame:** Monk A argued Louis's GPAI/ZKP positioning is in the reference class of Diffie/Hellman (1976) and Zimmermann (1991) — "first serious technical voices inside an emerging governance fight" who produced decades of outsized policy influence. This report stress-tests that analogy with historical evidence and 2026 institutional reality.

---

## 1. What was 1970s–1990s crypto governance actually like?

### 1.1 The institutional void

- **NSA monopoly.** Before 1976, cryptography was effectively classified. Hellman's peers discouraged him: "You're wasting your time... NSA has such a huge budget and a several-decades head start." ([Stanford Magazine](https://stanfordmag.org/contents/keeping-secrets))
- **Essentially no academic field.** "Little serious academic scholarship on cryptography existed outside classified research." Only **one** nongovernmental research group (IBM Yorktown) is named in the histories. Diffie and Hellman effectively **constituted** the non-classified research community when they started. ([NYU Tandon](https://engineering.nyu.edu/news/co-inventor-public-key-cryptography-turing-award-winner-alum))
- **No intermediaries.** No standards bodies, no AISIs, no industry consortia, no congressional committees with permanent crypto jurisdiction, no EFF (founded 1990), no civil society layer. The pipeline was: individual researcher → direct confrontation with NSA/Commerce → direct press/congressional escalation.

### 1.2 The actors

- **NSA** (monopoly incumbent), **NBS/NIST** (standards — then weak relative to NSA), **Commerce Department** (ITAR export controls), **Congress** (retroactively), **White House** (Clipper 1993).
- Civil society emerged **in response** to this specific fight: EFF (1990), EPIC (1994), Cypherpunks mailing list (1992).
- **Total headcount of the "relevant expert community" was maybe 50–200 people** in the late 1970s, and still a few thousand globally by the mid-1990s.

### 1.3 Bureaucratization: near zero

There was effectively **one layer of bureaucracy** between a technical contributor and a policy outcome: the research paper → public press → directly-convened congressional hearing → legislative/regulatory response. Diffie gave Senate testimony on Clipper in 1993 **as a Sun Microsystems distinguished engineer**, not as part of a standards body review cycle. ([EPIC archive](https://archive.epic.org/crypto/clipper/diffie_testimony.html))

---

## 2. How did Diffie/Hellman and Zimmermann actually translate technical work into policy?

### 2.1 Mechanisms that actually worked

| Actor | Mechanism | Effect |
|---|---|---|
| **Diffie/Hellman** | Direct public campaigning against DES weakening (mid-1970s); Diffie's Senate testimony on Clipper (1993); Sun Microsystems policy role (1991–); expert witness **Bernstein v. DoJ** | Shaped US export control debate; provided the technical credibility the EFF/industry campaigns leaned on |
| **Zimmermann** | Released PGP (1991); 3-year criminal investigation; published **PGP: Source Code and Internals** as a **book** via MIT Press (1995) to force First Amendment adjudication — government declined to prosecute rather than test the constitutional question | Dropped prosecution (1996); set de facto precedent that code-as-speech was too dangerous for the state to test. Reason.com ([When Encryption Was a Crime](https://reason.com/video/2020/10/21/cryptowars-gilmore-zimmermann-cryptography/)) preserves the detailed account. |
| **Matt Blaze** | Technical demonstration of Clipper LEAF protocol flaw (1994) | **Single technical paper killed Clipper.** Darknet Diaries: "That was the first nail in the coffin of the government's crypto policy." ([Darknet Diaries ep. 12](https://darknetdiaries.com/transcript/12/)) |

### 2.2 What the mechanisms share

1. **Small direct distance to policy.** Technical work → public dissemination → policy recoil, with minimal institutional relay.
2. **Individual visibility.** Each of these names is inseparable from the technical artifact (the 1976 paper, PGP source, the LEAF break). There was no "lead author of the committee draft."
3. **Adversarial dynamics.** Policy influence came from **defeating** a state proposal (DES, Clipper, ITAR), not from contributing to a harmonized standard.
4. **Legal/constitutional leverage** (PGP-as-book, Bernstein). The First Amendment was an **external lever** that technical contributors could pull because the regulated artifact (source code) had a constitutional shadow.

---

## 3. The 2026 AI governance structure — by contrast

The contrast is stark. List of institutional relays between a technical contributor and a policy outcome on frontier AI training verification:

**Active regulators/enforcers:** EU AI Office (140 staff, €46.5M), US **CAISI** (renamed from AISI June 2025 under Lutnick — explicitly shifted from "safety" to "innovation" framing ([Commerce statement](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai))), UK AISI (£100M), Singapore IDA, Japan AISI, Canada AISI, China CAC. ([OECD.AI overview](https://oecd.ai/en/wonk/ai-safety-institutes-challenge))

**Standards bodies:** NIST (AI RMF, Zero Drafts), **CEN-CENELEC JTC 21** (the body actually writing EU harmonized standards — 5 working groups, hundreds of contributors), ISO/IEC JTC 1/SC 42 (ISO 42001), IEEE P2894 and the P7000 family. ([JTC21 overview](https://jtc21.eu/))

**Code-of-Practice process:** The **GPAI Code of Practice** (Article 53/55 compliance bridge, published July 2025) was authored by **~1000 stakeholders in 4 working groups** over 9 months — hundreds of experts, industry reps, civil society. ([Code of Practice](https://code-of-practice.ai/))

**Policy think tanks & intermediaries:** GovAI (Oxford), CSET (Georgetown), CAIS, MIRI, METR, FAR.AI, Ada Lovelace, AI Now, Apollo, RAND, CNAS, Mozilla, Partnership on AI.

**Frontier-lab internal teams:** Anthropic Policy, OpenAI Policy (post-Brundage diaspora), Google DeepMind Responsible AI, Meta.

**New verification-specific entrants:** AVERI (Brundage, Jan 2026 — **funded by Coefficient Giving**, same funder as Louis's grant — with a published "AI Assurance Levels" framework aiming at treaty-grade attestation). ([DeepLearning.AI](https://www.deeplearning.ai/the-batch/openai-alumni-found-averi-to-set-standards-for-ai-model-audits/))

**Layers between Louis and a policy outcome:** at minimum 3–4. A GPAI Policy Lab paper feeds into → JTC 21 working-group draft → harmonized standard → EU AI Office enforcement. Every relay attenuates individual authorship.

---

## 4. Contemporary counter-examples: technical voices absorbed rather than shaping

### 4.1 The FLI "Pause" letter (2023)

30,000 signatures, Bengio + Russell + Tegmark + Musk. Concrete policy effect: **none of the stated goals achieved**. No lab paused. Did accelerate EU AI Act completion and White House meetings — diffusely. ([MIT Tech Review 6-months-on](https://www.technologyreview.com/2023/09/26/1080299/six-months-on-from-the-pause-letter/)) This is a famous-voices-absorbed-into-discourse pattern, not a Clipper-kill pattern.

### 4.2 Gary Marcus testimony (May 2023)

Marcus testified alongside Altman before the Senate Judiciary Subcommittee. Proposed FDA-style AI agency. Reception bipartisan and enthusiastic. **Actual legislation passed since: zero.** Marcus himself: "Congress has failed to pass any meaningful AI regulation... Republicans... far more resistant to AI regulation now than they were in 2023." ([Marcus substack 2025](https://garymarcus.substack.com/p/two-years-ago-today-in-ai-history))

### 4.3 Dan Hendrycks + CAIS + SB 1047 (2024)

Technical credibility (GELU, MMLU, robustness), direct co-sponsorship of a named bill. **Governor Newsom vetoed.** Hendrycks's Gray Swan conflict-of-interest became a talking point that weakened his voice. This is the closest-to-Diffie attempt in 2024 — and it failed at the final policy step despite technical-voice legitimacy. ([Pirate Wires](https://www.piratewires.com/p/sb-1047-dan-hendrycks-conflict-of-interest))

### 4.4 Bengio and the Singapore Consensus (2025)

Bengio led IAISR (33 governments) + the Singapore Consensus expert committee. This is **consensus-generating, not policy-kill**. It is the modern analog of writing a UNESCO report, not of publishing PGP. Influence is real and diffuse — exactly Monk B's "structurally capped" governance career pattern. ([arXiv 2506.20702](https://arxiv.org/abs/2506.20702))

### 4.5 Paul Christiano at AISI → CAISI (2024–2025)

The closest contemporary "technical authority → direct policy role" path. RLHF authorship → AISI Head of AI Safety (April 2024). Rebranded to CAISI under Trump admin (June 2025). Christiano still holds the role, but the **mandate shifted from safety to innovation/standards**. ([NIST staff page](https://www.nist.gov/people/paul-christiano)) A cautionary tale: political administrations can redirect the mandate underneath you faster than you can build policy permanence.

### 4.6 Miles Brundage / AVERI (Jan 2026)

Most directly parallel to Louis's case. Left OpenAI, raised $7.5M of $13M target, published **AI Assurance Levels** framework. **Funded by Coefficient Giving — the same funder as Louis's grant.** Brundage's AVERI is the US-based, better-funded, already-launched institution working the exact adjacent problem. ([Fortune](https://fortune.com/2026/01/15/former-openai-policy-chief-creates-nonprofit-institute-calls-for-independent-safety-audits-of-frontier-ai-models/)) AVERI's existence fundamentally changes the question "who will be the first reference voice on AI auditing" — **Brundage already is**, with OpenAI insider credibility Louis does not have.

---

## 5. Is the Diffie/Zimmermann pattern reproducible today?

**No — at least not via the Diffie/Zimmermann mechanism.** The specific conditions that enabled it:

1. **Small field, direct channel to power.** In 1976 the non-classified crypto community was ~100 people. In 2026 the AI governance expert community is **tens of thousands**.
2. **Adversarial state proposal to defeat.** Clipper, ITAR, DES weakening were specific, dateable artifacts a single technical demonstration could break. 2026 AI governance is diffuse, multilateral, and standards-based — built for durability against single-paper attacks.
3. **Constitutional shadow.** Code-as-speech gave crypto a legal lever. ZKP-of-training has no equivalent constitutional footing.
4. **Pre-bureaucratic window.** Crypto policy got codified 1993–2000; after that the Wassenaar Arrangement, BIS export controls, NIST FIPS processes turned it into standards-bureaucracy like everything else. **AI governance has been bureaucratized since ~2023.** The window Monk A describes — "inside an emerging governance fight" — **closed about 36 months before Louis's decision**, not 36 months after.

---

## 6. Is 2026 ZKP-of-training more like 1976 or more like 2024-era AI safety advocacy?

Honest answer: **neither cleanly.** The field-specific facts:

### 6.1 ZKP-of-training as a research field

- Published state-of-art: **zkLLM** (2024, 13B params, inference only, proof gen ~15 min, 2500%+ overhead on training). ([arXiv 2404.16109](https://arxiv.org/pdf/2404.16109))
- **zkGPT** (USENIX Security 2025, GPT-2 inference <25s, orders-of-magnitude improvement). ([eprint 2025/1184](https://eprint.iacr.org/2025/1184))
- Kaizen (2024), Gensyn publicly pivoted away from pure ZKP, flexHEG targeting 2027.
- This is **not** an empty field. The small-community-with-direct-policy-line analogy does not hold — cryptographers (Sun, Zhang, Abbaszadeh, Qu et al.) are actively publishing, conferences are running tracks, and the engineering bottlenecks are published.

### 6.2 The institutional context

- Compute governance has an **established literature cohort**: Shavit ("Catch a Chinchilla", 2023), Sastry/Heim/Anderljung/Trager ([arXiv 2402.08797](https://arxiv.org/abs/2402.08797)), Institute for Law & AI, GovAI, RAND compute team. Verification fits *inside* this cohort, not outside it.
- AVERI is already the nonprofit institutional home for "AI assurance levels." Coefficient Giving funded both AVERI and GPAI Policy Lab. Louis's work at GPAI is **not** the only or first serious technical voice; it's one credible European-side voice inside a maturing cohort.

### 6.3 So which analogy?

Closer to **2024 AI safety advocacy than to 1976 crypto**, on the institutional-structure axis. The field is populated, bureaucratized, and policy-translation runs through standards bodies and multi-stakeholder processes. **But** — importantly — it is still early enough that a first-of-kind working multi-GPU demonstration has rarity value, *because the engineering is hard*. That rarity is a real asset even without the Diffie-era mechanism translating it into personal policy influence.

---

## 7. Verdict

**The Diffie/Zimmermann analogy does not hold for Louis's 2026 GPAI move.** It breaks on three structural load-bearing points:

1. **Institutional structure (decisive).** 2026 AI governance has 3–4 bureaucratic relays between technical contributor and policy outcome. 1976 crypto had zero-to-one. The mechanism by which Diffie's 1976 paper became 2010s US crypto policy — direct adversarial confrontation with a state proposal, amplified by a small community with press access and constitutional shadow — is structurally unavailable in 2026 AI governance.
2. **Field maturity.** ZKP-of-training has active academic literature (zkLLM, zkGPT, Kaizen), a cryptography cohort publishing at top venues, and a compute-governance intellectual community already occupied (Shavit, Heim, Anderljung, Trager, GovAI, Institute for Law & AI, AVERI). "First serious technical voice" is not an accurate characterization of a Louis-at-GPAI position in 2026.
3. **Policy-translation mechanism.** The live 2026 mechanisms are **JTC 21 working groups, GPAI Code of Practice revisions, NIST Zero Drafts, AISI/CAISI evaluation frameworks, and Code-of-Practice signatory negotiations** — all multi-stakeholder, committee-authored, consensus-diluted processes. These do not produce Diffie-style individually-attached authority. They produce Bengio-Singapore-Consensus-style diffuse influence, which **every individual technical voice of the last 3 years has ended up inside**.

**If Louis's case held the analogy, the closest real-world fit is Brundage/AVERI** — who already did the move (left a frontier lab, launched a nonprofit on AI assurance, wrote the framework document) with OpenAI-insider credibility Louis doesn't have and $7.5M in committed funding. Brundage is a more accurate forward projection of Louis's best-case GPAI outcome than Diffie is — and Brundage's influence, while real, is structurally capped in exactly the way Monk B argued Leung's and Toner's are.

**Where the analogy partially survives.** A working multi-GPU ZKP-of-training demonstration has genuine rarity, and Louis co-authored would produce a cited artifact. That artifact has real value **inside the standards-body route** (JTC 21 verification annex, CAISI evaluation protocol references, EU harmonized standard footnotes). But this is **technical-contributor-inside-institution value**, which is exactly the Bengio/Christiano/Leung reference class — not the Diffie/Zimmermann reference class. Monk A has the reference class wrong by approximately one generation of governance bureaucratization.

**If the analogy holds anywhere, it holds for Matt Blaze's Clipper break** (one paper, specific technical demonstration, direct policy recoil), not for the broader Diffie positioning. A demonstrative "your proposed verification scheme is broken" technical result can still move policy fast. A "I helped co-author one of many technical inputs to the JTC 21 harmonized standard on training verification" outcome is real but generational-scale policy influence is not the likely result.

---

## 8. Implication for the dialectic

Monk A's **neglected-infrastructure** argument partially survives (rare credential, hard problem, real deliverable). Monk A's **Diffie-Zimmermann reference class** does not. Louis's GPAI outcome, even brilliantly executed, is more accurately projected as a **Brundage/Christiano/Leung-class career** — senior governance-technical role, structurally influential but bureaucratically mediated, not "decades of Diffie-grade individual policy authorship." That is not a small career. It is a different career than Monk A named.

If the decision is being made on expected personal policy influence over 20 years, **Monk A's reference class overstates the influence mechanism by roughly one order of magnitude.** If the decision is being made on neglected-technical-contribution terms, the argument survives on its own merits without the historical analogy.

---

## Sources and references

1. [Stanford Magazine: Keeping Secrets (Diffie/Hellman)](https://stanfordmag.org/contents/keeping-secrets)
2. [NYU Tandon: Co-Inventor of Public Key Cryptography profile](https://engineering.nyu.edu/news/co-inventor-public-key-cryptography-turing-award-winner-alum)
3. [EPIC archive: Diffie's Clipper testimony (1993)](https://archive.epic.org/crypto/clipper/diffie_testimony.html)
4. [Reason: When Encryption Was a Crime (Zimmermann documentary)](https://reason.com/video/2020/10/21/cryptowars-gilmore-zimmermann-cryptography/)
5. [Wikipedia: Phil Zimmermann](https://en.wikipedia.org/wiki/Phil_Zimmermann)
6. [Darknet Diaries ep. 12: Crypto Wars (Matt Blaze Clipper break)](https://darknetdiaries.com/transcript/12/)
7. [Wikipedia: Crypto Wars](https://en.wikipedia.org/wiki/Crypto_Wars)
8. [OECD.AI: AI Safety Institutes — Can countries meet the challenge?](https://oecd.ai/en/wonk/ai-safety-institutes-challenge)
9. [Commerce Dept: AISI → CAISI rebrand (June 2025)](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai)
10. [NIST: Paul Christiano staff page](https://www.nist.gov/people/paul-christiano)
11. [CEN-CENELEC JTC 21 overview](https://jtc21.eu/)
12. [EU AI Act Code of Practice (final, July 2025)](https://code-of-practice.ai/)
13. [EU AI Act Article 53](https://artificialintelligenceact.eu/article/53/)
14. [Marcus Senate testimony (May 2023)](https://www.judiciary.senate.gov/imo/media/doc/2023-05-16%20-%20Testimony%20-%20Marcus.pdf)
15. [Gary Marcus: "Two Years Ago Today" on failure of AI legislation](https://garymarcus.substack.com/p/two-years-ago-today-in-ai-history)
16. [MIT Tech Review: six months after the pause letter](https://www.technologyreview.com/2023/09/26/1080299/six-months-on-from-the-pause-letter/)
17. [FLI pause letter Wikipedia](https://en.wikipedia.org/wiki/Pause_Giant_AI_Experiments:_An_Open_Letter)
18. [Singapore Consensus on AI Safety Research (arXiv)](https://arxiv.org/abs/2506.20702)
19. [Wikipedia: SB 1047 / Hendrycks CAIS](https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act)
20. [Pirate Wires: Hendrycks / SB 1047 conflict of interest](https://www.piratewires.com/p/sb-1047-dan-hendrycks-conflict-of-interest)
21. [Fortune: Brundage launches AVERI (Jan 2026)](https://fortune.com/2026/01/15/former-openai-policy-chief-creates-nonprofit-institute-calls-for-independent-safety-audits-of-frontier-ai-models/)
22. [DeepLearning.AI: OpenAI Alumni Found Averi](https://www.deeplearning.ai/the-batch/openai-alumni-found-averi-to-set-standards-for-ai-model-audits/)
23. [AVERI work page](https://www.averi.org/ourwork)
24. [zkLLM paper (arXiv 2404.16109)](https://arxiv.org/pdf/2404.16109)
25. [zkGPT (USENIX Security 2025)](https://eprint.iacr.org/2025/1184)
26. [Sastry/Heim/Anderljung/Trager et al. — Computing Power and the Governance of AI (arXiv 2402.08797)](https://arxiv.org/abs/2402.08797)
27. [Institute for Law & AI: Computing Power and the Governance of AI](https://law-ai.org/computing-power-and-the-governance-of-artificial-intelligence/)
28. [Wikipedia: Jade Leung](https://en.wikipedia.org/wiki/Jade_Leung_(engineer))
29. [ACM Turing Award: Diffie & Hellman 2015](https://amturing.acm.org/award_winners/diffie_8371646.cfm)
30. [GPAI Policy Lab site](https://gpaipolicylab.org/)
