#!/usr/bin/env python3
# ABOUTME: Generates dist/html/index.html from slides/index.manifest.yml — groups decks,
# ABOUTME: dates them, and orders newest-first; titles come from each deck's source .md.

import html
import sys
from pathlib import Path

import yaml

GENERIC_H1 = "Deep Tech & Machine Learning"


def get_title(srcfile: Path) -> str:
    """First H1, falling back to first H2 when the H1 is the generic course title."""
    first_h1 = None
    first_h2 = None
    try:
        for line in srcfile.read_text(encoding="utf-8", errors="replace").splitlines():
            if first_h1 is None and line.startswith("# "):
                first_h1 = line[2:].strip()
            elif first_h2 is None and line.startswith("## "):
                first_h2 = line[3:].strip()
            if first_h1 and first_h2:
                break
    except OSError:
        return ""
    if first_h1 and first_h1 != GENERIC_H1:
        return first_h1
    if first_h2:
        return first_h2
    return first_h1 or ""


def deslugify(stem: str) -> str:
    out = stem
    if "-" in out and out.split("-", 1)[0].isdigit():
        out = out.split("-", 1)[1]
    return out.replace("-", " ").strip()


def html_name(md_path: Path, slides_dir: Path) -> str:
    """Mirror the Makefile flat-output naming: <parent-rel-with-dashes>-<stem>.html"""
    rel = md_path.relative_to(slides_dir)
    slug = str(rel.parent).replace("/", "-")
    return f"{slug}-{md_path.stem}.html"


def decks_in(dir_path: Path, slides_dir: Path, html_dir: Path):
    """Return (title, html_filename) for each .md in dir_path with built HTML, sorted."""
    out = []
    if not dir_path.is_dir():
        return out
    for md in sorted(dir_path.glob("*.md")):
        hname = html_name(md, slides_dir)
        if not (html_dir / hname).is_file():
            continue
        title = get_title(md) or deslugify(md.stem)
        out.append((title, hname))
    return out


def li(title: str, hname: str) -> str:
    return (
        f'<li><a href="{html.escape(hname)}">{html.escape(title)}</a>'
        f'<span class="deck-file">{html.escape(hname)}</span></li>'
    )


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: generate-index.py SLIDES_DIR HTML_DIR")
    slides_dir = Path(sys.argv[1])
    html_dir = Path(sys.argv[2])
    manifest_path = slides_dir / "index.manifest.yml"
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))

    page_title = manifest.get("title", "Slide Decks")
    subtitle = manifest.get("subtitle", "")
    groups = manifest.get("groups", [])
    # Newest first; groups without a date sort last.
    groups = sorted(groups, key=lambda g: g.get("date", "0000-00-00"), reverse=True)

    covered_ids = {g["id"] for g in groups}
    body = []

    for g in groups:
        gid = g["id"]
        label = g.get("label", gid)
        date_disp = g.get("date_display") or g.get("date", "")
        gdir = slides_dir / gid

        section_blocks = []  # (subheading_html_or_None, [li, ...])

        if g.get("prebuilt_html"):
            hname = g["prebuilt_html"]
            if (html_dir / hname).is_file():
                title = g.get("deck_title", label)
                section_blocks.append((None, [li(title, hname)]))
        elif g.get("subgroups"):
            for sg in g["subgroups"]:
                decks = decks_in(gdir / sg["id"], slides_dir, html_dir)
                if decks:
                    # Manifest labels are trusted pre-formatted HTML (may contain &amp; etc).
                    sub = f'<h3>{sg.get("label", sg["id"])}</h3>'
                    section_blocks.append((sub, [li(t, h) for t, h in decks]))
        else:
            decks = decks_in(gdir, slides_dir, html_dir)
            if decks:
                section_blocks.append((None, [li(t, h) for t, h in decks]))

        if not section_blocks:
            continue  # nothing built for this group → skip

        date_html = f'<span class="group-date">{date_disp}</span>' if date_disp else ""
        # label/date_disp come from the manifest and are trusted HTML.
        body.append(f"<h2><span>{label}</span>{date_html}</h2>")
        for sub, items in section_blocks:
            if sub:
                body.append(sub)
            body.append("<ul>")
            body.extend(items)
            body.append("</ul>")

    # Safety net: any top-level slides dir not in the manifest, with built HTML.
    extra = []
    for d in sorted(p for p in slides_dir.iterdir() if p.is_dir()):
        if d.name in covered_ids:
            continue
        # Scan recursively for any .md whose HTML was built.
        decks = []
        for md in sorted(d.rglob("*.md")):
            hname = html_name(md, slides_dir)
            if (html_dir / hname).is_file():
                decks.append((get_title(md) or deslugify(md.stem), hname))
        if decks:
            extra.append((d.name, decks))
    if extra:
        body.append('<h2>Not in manifest <span class="group-date">add to index.manifest.yml</span></h2>')
        for name, decks in extra:
            body.append(f"<h3>{html.escape(name)}</h3><ul>")
            body.extend(li(t, h) for t, h in decks)
            body.append("</ul>")

    out = f"""<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page_title} — Louis Develle</title>
<style>
  *{{margin:0;padding:0;box-sizing:border-box}}
  body{{font-family:system-ui,-apple-system,sans-serif;max-width:820px;margin:0 auto;padding:2rem;background:#fafbfc;color:#1a1a2e}}
  h1{{font-size:1.8rem;margin-bottom:.3rem}}
  .subtitle{{color:#666;margin-bottom:2rem;font-size:.95rem}}
  h2{{font-size:1.2rem;margin:1.8rem 0 .5rem;padding-bottom:.3rem;border-bottom:2px solid #16213e;color:#16213e;display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:.5rem}}
  h3{{font-size:.98rem;margin:1rem 0 .25rem;color:#0f3460;font-weight:600}}
  .group-date{{color:#8892a4;font-size:.78rem;font-weight:400}}
  ul{{list-style:none;padding:0}}
  li{{margin:.35rem 0}}
  a{{color:#0f3460;text-decoration:none;padding:.25rem .5rem;border-radius:4px;display:inline-block}}
  a:hover{{background:#e2e8f0;color:#16213e}}
  .deck-file{{color:#aab2c0;font-size:.8rem;margin-left:.5rem}}
</style>
</head><body>
<h1>{page_title}</h1>
<p class="subtitle">{subtitle}</p>
{chr(10).join(body)}
</body></html>
"""
    (html_dir / "index.html").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
