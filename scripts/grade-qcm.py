# ABOUTME: Parses hand-filled answers.md files, grades QCM with 3 scoring modes, generates histograms.
# ABOUTME: Reads from .private/qcm-exam/students/<name>/answers.md, outputs CSV + PNG.

"""
QCM Grading Pipeline
====================
1. Parses answers.md in each student directory
2. Generates student_answers.csv
3. Grades with 3 scoring modes
4. Produces histogram comparison

Usage:
    uv run --with matplotlib scripts/grade-qcm.py
"""

import csv
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PROJECT = Path(__file__).resolve().parent.parent
EXAM_DIR = PROJECT / ".private" / "qcm-exam"
STUDENTS_DIR = EXAM_DIR / "students"
ANSWER_KEY = PROJECT / "docs" / "qcm" / "qcm-answer-key.csv"
ANSWERS_CSV = EXAM_DIR / "student_answers.csv"
GRADES_CSV = EXAM_DIR / "grades.csv"
HISTOGRAM_PNG = EXAM_DIR / "grades_histogram.png"

ALL_QIDS = [
    "QVNL", "QBKN", "QWMN", "QTEV", "QCYM", "QFJT", "QAAF", "QTXV",
    "QTKF", "QBMP", "QJLW", "QCXX", "QNBR", "QZYU", "QSVG", "QHAR",
    "QUHB", "QEAS", "QKDV", "QZSE",
]


# ---------------------------------------------------------------------------
# Parse answers.md files
# ---------------------------------------------------------------------------

def parse_answers_md(path: Path) -> dict[str, dict[str, int]]:
    """Parse a student's answers.md. Returns {qid: {A:0/1, B:0/1, ...}}."""
    text = path.read_text(encoding="utf-8")
    answers = {}

    # Split by question headers (QXXX: Title)
    blocks = re.split(r"\n(?=Q[A-Z]{3,4}:)", text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        lines = block.split("\n")
        header = lines[0].strip()
        qid_match = re.match(r"^(Q[A-Z]{3,4}):", header)
        if not qid_match:
            continue
        qid = qid_match.group(1)

        # Answer is on the next non-empty line
        answer_letters = ""
        for line in lines[1:]:
            line = line.strip()
            if line and not line.startswith("Q"):
                answer_letters = line.upper()
                break

        answers[qid] = {
            "A": 1 if "A" in answer_letters else 0,
            "B": 1 if "B" in answer_letters else 0,
            "C": 1 if "C" in answer_letters else 0,
            "D": 1 if "D" in answer_letters else 0,
            "E": 1 if "E" in answer_letters else 0,
        }

    return answers


def load_all_students() -> list[dict]:
    """Load answers from all student directories. Skip absent students (empty answers)."""
    students = []
    absent = []

    for d in sorted(STUDENTS_DIR.iterdir()):
        if not d.is_dir():
            continue
        md = d / "answers.md"
        if not md.exists():
            continue

        name = d.name.replace("_", " ")
        answers = parse_answers_md(md)

        # Check if student is absent (no answers filled)
        has_answers = any(
            any(v == 1 for v in ans.values())
            for ans in answers.values()
        )
        if not has_answers:
            absent.append(name)
            continue

        students.append({"name": name, "dir": d.name, "answers": answers})

    return students, absent


# ---------------------------------------------------------------------------
# Answer key
# ---------------------------------------------------------------------------

def load_answer_key(path: Path) -> dict[str, dict[str, int]]:
    """Load answer key: {qid: {A: 0/1, B: 0/1, ...}}."""
    key = {}
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key[row["q_id"]] = {
                letter: 1 if row[letter] == "VRAI" else 0
                for letter in "ABCDE"
            }
    return key


# ---------------------------------------------------------------------------
# CSV output
# ---------------------------------------------------------------------------

def write_answers_csv(students: list[dict], path: Path):
    """Write student_answers.csv."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "q_id", "A", "B", "C", "D", "E"])
        for s in students:
            for qid in ALL_QIDS:
                ans = s["answers"].get(qid, {l: 0 for l in "ABCDE"})
                writer.writerow([s["name"], qid, ans["A"], ans["B"], ans["C"], ans["D"], ans["E"]])
    n = len(students)
    print(f"  Wrote {n * 20} rows ({n} students x 20 questions)")


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

def score_question(student: dict[str, int], correct: dict[str, int], mode: str) -> float:
    """Score one question."""
    errors = sum(1 for l in "ABCDE" if student[l] != correct[l])
    if mode == "strict":
        return 1.0 if errors == 0 else 0.0
    elif mode == "half":
        return {0: 1.0, 1: 0.5}.get(errors, 0.0)
    elif mode == "quarter":
        return max(0.0, 1.0 - errors * 0.25)
    raise ValueError(mode)


def grade_all(students: list[dict], key: dict) -> list[dict]:
    """Grade every student under all 3 modes."""
    results = []
    for s in students:
        g = {"name": s["name"]}
        for mode in ("strict", "half", "quarter"):
            total = sum(
                score_question(
                    s["answers"].get(qid, {l: 0 for l in "ABCDE"}),
                    key[qid],
                    mode,
                )
                for qid in ALL_QIDS
            )
            g[mode] = round(total, 2)
        results.append(g)
    return results


def write_grades_csv(grades: list[dict], path: Path):
    """Write grades.csv."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "strict", "half", "quarter"])
        for g in sorted(grades, key=lambda x: -x["strict"]):
            writer.writerow([g["name"], g["strict"], g["half"], g["quarter"]])


# ---------------------------------------------------------------------------
# Histogram
# ---------------------------------------------------------------------------

def generate_histogram(grades: list[dict], path: Path):
    """3 side-by-side histograms."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    modes = [
        ("strict", "Tout ou rien", "#2196F3"),
        ("half", "1 erreur = ½ pt", "#4CAF50"),
        ("quarter", "-¼ pt par erreur", "#FF9800"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
    fig.suptitle("QCM Deep Tech & ML — Distribution des notes", fontsize=14, fontweight="bold")

    bins = np.arange(0, 21.5, 1)
    n = len(grades)

    for ax, (key, label, color) in zip(axes, modes):
        scores = [g[key] for g in grades]
        avg = sum(scores) / len(scores)
        failing = sum(1 for s in scores if s < 10)
        perfect = sum(1 for s in scores if s == 20)

        ax.hist(scores, bins=bins, color=color, edgecolor="white", alpha=0.85)
        ax.axvline(avg, color="red", linestyle="--", linewidth=1.5, label=f"Moyenne: {avg:.1f}")
        ax.axvline(10, color="black", linestyle=":", linewidth=1, alpha=0.5)

        ax.set_title(label, fontsize=11, fontweight="bold")
        ax.set_xlabel("Note /20")
        ax.set_xlim(0, 20)
        ax.legend(fontsize=9)

        stats = f"Moy: {avg:.1f}\n< 10: {failing}/{n}\n= 20: {perfect}/{n}\nMin: {min(scores):.1f}\nMax: {max(scores):.1f}"
        ax.text(0.97, 0.97, stats, transform=ax.transAxes, fontsize=8,
                verticalalignment="top", horizontalalignment="right",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

    axes[0].set_ylabel("Nombre d'étudiants")
    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("QCM GRADING")
    print("=" * 60)

    # Load
    students, absent = load_all_students()
    key = load_answer_key(ANSWER_KEY)
    print(f"\n  Present: {len(students)} students")
    print(f"  Absent:  {len(absent)} — {', '.join(absent)}")

    # Validate
    for s in students:
        missing = [q for q in ALL_QIDS if q not in s["answers"]]
        if missing:
            print(f"  ⚠ {s['name']}: missing {missing}")

    # CSV
    print(f"\nStudent answers → {ANSWERS_CSV.name}")
    write_answers_csv(students, ANSWERS_CSV)

    # Grade
    grades = grade_all(students, key)
    write_grades_csv(grades, GRADES_CSV)

    # Summary
    for mode_key, mode_label in [("strict", "Tout ou rien"),
                                  ("half", "1 erreur = ½ pt"),
                                  ("quarter", "-¼ pt / erreur")]:
        scores = [g[mode_key] for g in grades]
        avg = sum(scores) / len(scores)
        failing = sum(1 for s in scores if s < 10)
        perfect = sum(1 for s in scores if s == 20)
        print(f"\n  {mode_label}:")
        print(f"    Moyenne: {avg:.1f}/20  |  < 10: {failing}/{len(scores)}  |  = 20: {perfect}/{len(scores)}")

    # Per-student table
    print(f"\n{'Nom':<35} {'Strict':>6} {'½ err':>6} {'-¼pt':>6}")
    print("-" * 60)
    for g in sorted(grades, key=lambda x: -x["strict"]):
        print(f"{g['name']:<35} {g['strict']:>6.1f} {g['half']:>6.1f} {g['quarter']:>6.1f}")

    # Histogram
    print(f"\nHistogram → {HISTOGRAM_PNG.name}")
    generate_histogram(grades, HISTOGRAM_PNG)
    print("Done.")


if __name__ == "__main__":
    main()
