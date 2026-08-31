<!-- ABOUTME: Deep-research brief — does Claude watermark its output, and what should founders know about AI provenance? -->
<!-- ABOUTME: Louis's list has "Claude watermarking?" with no source at all — pure research gap. -->

# Research brief — Claude watermarking & AI provenance, for founders

## Question
Does Claude (text or artifacts) carry any watermark or provenance signal in 2026 — and what is the actual state of AI-output provenance (text watermarking, C2PA, SynthID, detector reliability) that a founder shipping AI-generated content should understand?

## Why it matters for the talk
Louis flagged "Claude watermarking?" with zero sources. Founders in the room ship AI-written code, marketing copy, and images daily; "can anyone tell?" and "will this be detectable/regulated?" are questions they will ask in the conversation half. High leverage: nobody in the room has researched this, and confident wrong answers circulate widely.

## What we already have
Nothing collected. Adjacent context: Louis maintains a multi-vendor AI-provenance-mark removal skill, so he has practitioner priors on what marks exist (invisible Unicode classes, statistical text watermarks, C2PA/EXIF/XMP metadata) — the research must confirm/refute against public primary sources, not fold in private knowledge without citations.

## What to find
1. **Anthropic specifically**: any official statement/docs on watermarking Claude text output; what metadata Claude-generated artifacts/files actually carry; anything in Anthropic's usage policies or transparency reports about provenance.
2. **Text watermarking state of the art**: Google SynthID-Text (deployed where?), OpenAI's stance (they built one, chose not to deploy — verify + date), academic consensus on robustness (paraphrase attacks).
3. **Detector reality**: published false-positive/negative rates of AI-text detectors in 2026; the documented harms (student false accusations) — one citable study.
4. **Regulatory hooks**: EU AI Act Article 50 transparency obligations (machine-readable marking of synthetic content) — what actually applies to a startup and WHEN; China's labeling rules as contrast.
5. **Images/media**: C2PA adoption status (which cameras/tools/platforms), SynthID for images — is provenance becoming default in any pipeline founders use?

## Acceptance
A clear yes/no/nuanced answer on Claude with primary citations; a founder-legible 4-row summary (text/code/images/regulation) each with exact clickable primary URL + verbatim quote. Distinguish "technically possible" from "actually deployed".

## Method
One deep-research run; primary sources: anthropic.com docs/policies, deepmind.google (SynthID), eur-lex (AI Act art. 50), peer-reviewed detector studies.
