# ABOUTME: Generates print-ready QCM PDFs from markdown source with 4 shuffled versions.
# ABOUTME: Designed for VLM-based automatic grading with prominent Q-IDs and inline checkboxes.

"""
QCM PDF Generator
==================
Parses docs/courses/sorbonne-m2/qcm/qcm-sessions-1-4.md and generates 4 shuffled
PDF versions for automatic VLM-based grading.

Usage:
    uv run --with reportlab scripts/generate-qcm-pdf.py

Output:
    docs/courses/sorbonne-m2/qcm/qcm-v1.pdf ... qcm-v4.pdf
    docs/courses/sorbonne-m2/qcm/qcm-answer-key.csv
    docs/courses/sorbonne-m2/qcm/qcm-version-orders.csv
"""

import csv
import random
import re
import string
import sys
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

QCM_MD = Path(__file__).resolve().parent.parent / "docs" / "courses" / "sorbonne-m2" / "qcm" / "qcm-sessions-1-4.md"
OUT_DIR = QCM_MD.parent

PAGE_W, PAGE_H = A4  # 210 x 297 mm
MARGIN_LEFT = 15 * mm
MARGIN_RIGHT = 15 * mm
MARGIN_TOP = 15 * mm
MARGIN_BOTTOM = 12 * mm
USABLE_W = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

# Font sizes
FONT_TITLE = 13
FONT_VERSION = 16
FONT_INSTRUCTIONS = 8
FONT_QID = 11
FONT_QTITLE = 8.5
FONT_PROP = 7.5

# Checkbox dimensions
BOX_SIZE = 3.2 * mm

# Vertical spacing
LINE_HEIGHT_PROP = 9.5  # points between proposition lines
QUESTION_GAP = 5  # extra points between questions

# Seeds for deterministic shuffles
SHUFFLE_SEEDS = [None, 42, 137, 2026]  # None = no shuffle (V1 = original order)

# Seed for generating Q-IDs (deterministic 3-letter codes)
QID_SEED = 7777


# ---------------------------------------------------------------------------
# Q-ID generation (3 random uppercase letters, no duplicates)
# ---------------------------------------------------------------------------

def generate_qids(n: int, seed: int) -> list[str]:
    """Generate n unique 3-letter Q-IDs like QABC, QXYZ, etc."""
    rng = random.Random(seed)
    used = set()
    qids = []
    # Use only easily distinguishable uppercase letters (drop I, O, Q to avoid
    # confusion with 1, 0, Q-prefix itself)
    alphabet = [c for c in string.ascii_uppercase if c not in "IOQ"]
    while len(qids) < n:
        code = "".join(rng.choices(alphabet, k=3))
        if code not in used:
            used.add(code)
            qids.append(f"Q{code}")
    return qids


# ---------------------------------------------------------------------------
# Markdown parser
# ---------------------------------------------------------------------------

def parse_qcm_markdown(path: Path) -> list[dict]:
    """Parse the QCM markdown and return a list of question dicts."""
    text = path.read_text(encoding="utf-8")

    # Extract only Partie 1 (between "# Partie 1" and "# Partie 2")
    part1_match = re.search(
        r"# Partie 1 — Questions\s*\n(.*?)(?=\n# Partie 2|\Z)",
        text,
        re.DOTALL,
    )
    if not part1_match:
        sys.exit("ERROR: Could not find '# Partie 1 — Questions' in markdown.")
    part1 = part1_match.group(1)

    # Find all questions
    question_pattern = re.compile(
        r"###\s*Question\s+(\d+)\s*—\s*(.+?)\s*\n"
        r"(.*?)(?=\n###\s*Question|\n---\s*\n---|\Z)",
        re.DOTALL,
    )

    questions = []
    for m in question_pattern.finditer(part1):
        q_num = int(m.group(1))
        q_title = m.group(2).strip()
        q_body = m.group(3)

        # Extract propositions (lines starting with "- A)" through "- E)")
        props = []
        for line in q_body.split("\n"):
            line = line.strip()
            prop_match = re.match(r"^-\s*([A-E])\)\s*(.+)$", line)
            if prop_match:
                props.append((prop_match.group(1), prop_match.group(2).strip()))

        questions.append({
            "num": q_num,
            "title": q_title,
            "props": props,
        })

    return questions


def validate_questions(questions: list[dict]):
    """Validate parsed questions."""
    assert len(questions) == 20, f"Expected 20 questions, got {len(questions)}"
    for q in questions:
        assert len(q["props"]) == 5, (
            f"Q{q['num']:02d} has {len(q['props'])} propositions (expected 5): "
            f"{[p[0] for p in q['props']]}"
        )
        letters = [p[0] for p in q["props"]]
        assert letters == ["A", "B", "C", "D", "E"], (
            f"Q{q['num']:02d} propositions are {letters}, expected A-E"
        )
    print(f"✓ Parsed {len(questions)} questions, all with 5 propositions (A–E)")


# ---------------------------------------------------------------------------
# PDF generation
# ---------------------------------------------------------------------------

def draw_inline_checkbox(c: canvas.Canvas, x: float, y: float, label: str):
    """Draw a checkbox with the letter label printed right next to it."""
    # Draw the box
    c.setLineWidth(1.2)
    c.setStrokeColorRGB(0, 0, 0)
    c.setFillColorRGB(1, 1, 1)
    c.rect(x, y, BOX_SIZE, BOX_SIZE, fill=1, stroke=1)
    # Draw letter immediately after the box, same size as proposition text
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", FONT_PROP)
    c.drawString(x + BOX_SIZE + 1 * mm, y + 0.3 * mm, label)


def draw_header(c: canvas.Canvas, version: str, page_num: int):
    """Draw header on the page."""
    y = PAGE_H - MARGIN_TOP

    if page_num == 1:
        # Title
        c.setFont("Helvetica-Bold", FONT_TITLE)
        c.drawString(MARGIN_LEFT, y, "QCM — Deep Tech & ML (UE3)")

        # Version tag (top-right, prominent)
        c.setFont("Helvetica-Bold", FONT_VERSION)
        c.drawRightString(PAGE_W - MARGIN_RIGHT, y, f"Version {version}")

        # Subtitle
        y -= 14
        c.setFont("Helvetica", 8)
        c.drawString(MARGIN_LEFT, y, "M2 IMT&E — Paris 1 Panthéon-Sorbonne — 30 mars 2026")

        # Name fields
        y -= 18
        c.setFont("Helvetica-Bold", 9)
        c.drawString(MARGIN_LEFT, y, "Prénom : ")
        c.setLineWidth(0.5)
        name_start = MARGIN_LEFT + 42
        c.line(name_start, y - 1, name_start + 120, y - 1)

        c.drawString(name_start + 140, y, "Nom : ")
        c.line(name_start + 170, y - 1, name_start + 310, y - 1)

        # Instructions
        y -= 16
        c.setFont("Helvetica-Bold", FONT_INSTRUCTIONS)
        c.drawString(
            MARGIN_LEFT,
            y,
            "Noircissez les cases des affirmations VRAIES. "
            "Plusieurs réponses possibles par question. Correction automatique.",
        )
        y -= 10
        c.setFont("Helvetica-Bold", FONT_INSTRUCTIONS)
        c.drawString(
            MARGIN_LEFT,
            y,
            "IMPORTANT : Remplissez votre nom et prénom sur les DEUX pages (recto et verso).",
        )

        # Separator line
        y -= 6
        c.setLineWidth(0.8)
        c.line(MARGIN_LEFT, y, PAGE_W - MARGIN_RIGHT, y)

        return y - 10

    else:
        # Page 2+: header with name fields
        c.setFont("Helvetica-Bold", 9)
        c.drawString(MARGIN_LEFT, y, f"QCM — Deep Tech & ML — Version {version} — Page {page_num}")

        # Name fields on page 2
        y -= 14
        c.drawString(MARGIN_LEFT, y, "Prénom : ")
        c.setLineWidth(0.5)
        name_start = MARGIN_LEFT + 42
        c.line(name_start, y - 1, name_start + 120, y - 1)

        c.drawString(name_start + 140, y, "Nom : ")
        c.line(name_start + 170, y - 1, name_start + 310, y - 1)

        y -= 6
        c.setLineWidth(0.5)
        c.line(MARGIN_LEFT, y, PAGE_W - MARGIN_RIGHT, y)
        return y - 12


def truncate_text(text: str, font_name: str, font_size: float, max_width: float) -> str:
    """Truncate text to fit within max_width, adding ellipsis if needed."""
    if stringWidth(text, font_name, font_size) <= max_width:
        return text
    while len(text) > 0 and stringWidth(text + "…", font_name, font_size) > max_width:
        text = text[:-1]
    return text + "…"


def generate_pdf(questions: list[dict], version: str, order: list[int], output_path: Path):
    """Generate a single QCM PDF with inline checkboxes per proposition."""
    c = canvas.Canvas(str(output_path), pagesize=A4)
    c.setTitle(f"QCM Deep Tech & ML — Version {version}")

    page_num = 1
    y = draw_header(c, version, page_num)

    # Layout constants for inline checkboxes
    qid_x = MARGIN_LEFT
    checkbox_x = MARGIN_LEFT + 6 * mm  # checkbox column for propositions
    # Box + 1mm gap + bold letter (e.g. "A") + 1.5mm gap + text
    letter_w = stringWidth("A", "Helvetica-Bold", FONT_PROP)
    text_x = checkbox_x + BOX_SIZE + 1 * mm + letter_w + 2 * mm
    max_text_w = PAGE_W - MARGIN_RIGHT - text_x

    for idx, q_idx in enumerate(order):
        q = questions[q_idx]

        # Estimate space needed: title line + 5 proposition lines + gap
        needed = FONT_QID + 2 + len(q["props"]) * LINE_HEIGHT_PROP + QUESTION_GAP

        # New page if needed
        if y - needed < MARGIN_BOTTOM:
            c.showPage()
            page_num += 1
            y = draw_header(c, version, page_num)

        # --- Q-ID + title line ---
        c.setFont("Helvetica-Bold", FONT_QID)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(qid_x, y, q["qid"])

        qid_end = qid_x + stringWidth(q["qid"], "Helvetica-Bold", FONT_QID) + 3 * mm
        c.setFont("Helvetica-Bold", FONT_QTITLE)
        max_title_w = PAGE_W - MARGIN_RIGHT - qid_end
        title_text = truncate_text(q["title"], "Helvetica-Bold", FONT_QTITLE, max_title_w)
        c.drawString(qid_end, y, title_text)

        y -= FONT_QID + 2

        # --- Propositions with inline checkboxes ---
        for letter, text in q["props"]:
            # Checkbox with letter label right next to it
            draw_inline_checkbox(c, checkbox_x, y - 0.5 * mm, letter)

            # Proposition text (without letter prefix, since it's on the box)
            prop_text = truncate_text(text, "Helvetica", FONT_PROP, max_text_w)
            c.setFont("Helvetica", FONT_PROP)
            c.drawString(text_x, y, prop_text)

            y -= LINE_HEIGHT_PROP

        y -= QUESTION_GAP

    c.save()
    print(f"  → {output_path.name} ({page_num} pages)")


# ---------------------------------------------------------------------------
# Answer key CSV
# ---------------------------------------------------------------------------

def parse_answer_key(path: Path) -> dict[int, dict[str, bool]]:
    """Parse the Partie 2 answer key from markdown. Returns {q_num: {letter: bool}}."""
    text = path.read_text(encoding="utf-8")
    part2_match = re.search(r"# Partie 2 — Corrigé\s*\n(.*)", text, re.DOTALL)
    if not part2_match:
        sys.exit("ERROR: Could not find '# Partie 2 — Corrigé'")
    part2 = part2_match.group(1)

    answers = {}
    current_q = None

    for line in part2.split("\n"):
        q_header = re.match(r"###\s*Question\s+(\d+)", line)
        if q_header:
            current_q = int(q_header.group(1))
            answers[current_q] = {}
            continue

        row_match = re.match(
            r"\|\s*([A-E])\s*\|\s*\*\*(\w+)\*\*\s*\|", line
        )
        if row_match and current_q is not None:
            letter = row_match.group(1)
            verdict = row_match.group(2).upper()
            answers[current_q][letter] = (verdict == "VRAI")

    return answers


def write_answer_key_csv(questions: list[dict], answers: dict[int, dict[str, bool]], output_path: Path):
    """Write answer key CSV: qid (3-letter), A, B, C, D, E."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["q_id", "q_num", "title", "A", "B", "C", "D", "E"])
        for q in questions:
            ans = answers.get(q["num"], {})
            row = [q["qid"], q["num"], q["title"]]
            for letter in "ABCDE":
                row.append("VRAI" if ans.get(letter, False) else "FAUX")
            writer.writerow(row)
    print(f"  → {output_path.name}")


def write_version_orders_csv(questions: list[dict], all_orders: dict[str, list[int]], output_path: Path):
    """Write CSV mapping version → position → q_id."""
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["version", "position", "q_id", "q_num", "title"])
        for version, order in sorted(all_orders.items()):
            for pos, q_idx in enumerate(order, 1):
                q = questions[q_idx]
                writer.writerow([version, pos, q["qid"], q["num"], q["title"]])
    print(f"  → {output_path.name}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print(f"Parsing {QCM_MD}...")
    questions = parse_qcm_markdown(QCM_MD)
    validate_questions(questions)

    # Assign 3-letter Q-IDs
    qids = generate_qids(20, QID_SEED)
    for i, q in enumerate(questions):
        q["qid"] = qids[i]
    print(f"✓ Assigned Q-IDs: {', '.join(q['qid'] for q in questions)}")

    # Validate no duplicate Q-IDs
    assert len(set(qids)) == 20, "Duplicate Q-IDs detected!"

    # Generate 4 versions with different question orders
    all_orders = {}
    versions = ["V1", "V2", "V3", "V4"]

    print("\nGenerating PDFs...")
    for i, version in enumerate(versions):
        order = list(range(20))
        seed = SHUFFLE_SEEDS[i]
        if seed is not None:
            rng = random.Random(seed)
            rng.shuffle(order)
        all_orders[version] = order

        output_path = OUT_DIR / f"qcm-{version.lower()}.pdf"
        generate_pdf(questions, version, order, output_path)

        # Validation: every Q-ID appears exactly once
        qids_in_order = [questions[idx]["qid"] for idx in order]
        assert len(set(qids_in_order)) == 20, f"{version}: duplicate or missing Q-IDs!"

    # Parse answer key and generate CSV
    print("\nGenerating answer key...")
    answers = parse_answer_key(QCM_MD)
    assert len(answers) == 20, f"Expected 20 answer entries, got {len(answers)}"
    for q_num, ans in answers.items():
        assert len(ans) == 5, f"Q{q_num} has {len(ans)} answers (expected 5)"
    write_answer_key_csv(questions, answers, OUT_DIR / "qcm-answer-key.csv")

    # Generate version orders CSV
    print("\nGenerating version orders...")
    write_version_orders_csv(questions, all_orders, OUT_DIR / "qcm-version-orders.csv")

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for version, order in all_orders.items():
        qids = [questions[idx]["qid"] for idx in order]
        print(f"  {version}: {', '.join(qids)}")
    print(f"\nAnswer key:")
    for q in questions:
        ans = answers.get(q["num"], {})
        vrai_letters = [l for l in "ABCDE" if ans.get(l, False)]
        print(f"  {q['qid']} (Q{q['num']:02d} {q['title'][:30]}): {', '.join(vrai_letters)}")


if __name__ == "__main__":
    main()
