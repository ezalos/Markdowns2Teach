# ABOUTME: Generates index.html with links to all built slide decks.
# ABOUTME: Extracts deck titles from source .md files for human-readable names.

set -euo pipefail

SLIDES_DIR="${1:?Usage: generate-index.sh SLIDES_DIR HTML_DIR}"
HTML_DIR="${2:?Usage: generate-index.sh SLIDES_DIR HTML_DIR}"

OUTPUT="$HTML_DIR/index.html"

# Extract a display title from a slide source file.
# Uses first H1 heading, falling back to first H2 if H1 is the generic course title.
get_title() {
    local srcfile="$1"
    local first_h1
    first_h1=$(grep -m1 '^# ' "$srcfile" | sed 's/^# //;s/\r$//')
    if [ "$first_h1" = "Deep Tech & Machine Learning" ]; then
        grep -m1 '^## ' "$srcfile" | sed 's/^## //;s/\r$//'
    else
        echo "$first_h1"
    fi
}

# Write HTML header
cat > "$OUTPUT" <<'HEADER'
<!DOCTYPE html>
<html lang="fr"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Slide Decks — Deep Tech &amp; ML</title>
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  body{font-family:system-ui,-apple-system,sans-serif;max-width:800px;margin:0 auto;padding:2rem;background:#fafbfc;color:#1a1a2e}
  h1{font-size:1.8rem;margin-bottom:.3rem}
  .subtitle{color:#666;margin-bottom:2rem;font-size:.95rem}
  h2{font-size:1.15rem;margin:1.5rem 0 .5rem;padding-bottom:.3rem;border-bottom:2px solid #16213e;color:#16213e}
  ul{list-style:none;padding:0}
  li{margin:.35rem 0}
  a{color:#0f3460;text-decoration:none;padding:.25rem .5rem;border-radius:4px;display:inline-block}
  a:hover{background:#e2e8f0;color:#16213e}
  .deck-file{color:#888;font-size:.85rem;margin-left:.5rem}
</style>
</head><body>
<h1>Slide Decks</h1>
<p class="subtitle">Deep Tech &amp; ML — M2 Entrepreneuriat Sorbonne</p>
HEADER

# Build a sorted list of "slug\tfilename" pairs for proper grouping.
# HTML files are named <slug>-<deck>.html (e.g. session-01-A-genai-fondamentaux.html).
# Extract slug by matching the session-XX prefix.
sorted_entries=""
for f in $(find "$HTML_DIR" -maxdepth 1 -name '*.html' ! -name 'index.html'); do
    filename=$(basename "$f")
    base="${filename%.html}"
    # Extract session slug (session-XX) from the filename prefix
    if [[ "$base" =~ ^(session-[0-9]+)- ]]; then
        slug="${BASH_REMATCH[1]}"
    else
        slug="unknown"
    fi
    sorted_entries+="$slug	$filename"$'\n'
done
sorted_entries=$(echo "$sorted_entries" | sort)

# Group HTML files by session slug
current_group=""
while IFS=$'\t' read -r slug filename; do
    [ -z "$slug" ] && continue
    base="${filename%.html}"

    # Resolve title from source .md — strip slug prefix to get deck basename
    deck_base="${base#"$slug"-}"
    srcfile="$SLIDES_DIR/$slug/$deck_base.md"
    title=""
    if [ -f "$srcfile" ]; then
        title=$(get_title "$srcfile")
    fi
    if [ -z "$title" ]; then
        title=$(echo "$deck_base" | sed 's/^[0-9]*-//;s/-/ /g')
    fi

    # Start new group if needed
    if [ "$slug" != "$current_group" ]; then
        if [ -n "$current_group" ]; then
            echo '</ul>' >> "$OUTPUT"
        fi
        current_group="$slug"
        # Map session directories to human-readable labels
        group_label="$slug"
        case "$slug" in
            session-01) group_label="Session 1 — Comprendre l'IA en 2026" ;;
            session-02) group_label="Session 2 — Construire avec l'IA" ;;
            session-03) group_label="Session 3 — Cadrer un projet IA" ;;
            session-04) group_label="Session 4 — Le business de l'IA" ;;
            session-05) group_label="Session 5 — Éthique, gouvernance & clôture" ;;
        esac
        echo "<h2>$group_label</h2>" >> "$OUTPUT"
        echo '<ul>' >> "$OUTPUT"
    fi

    echo "<li><a href=\"$filename\">$title</a><span class=\"deck-file\">$filename</span></li>" >> "$OUTPUT"
done <<< "$sorted_entries"

# Close last group
if [ -n "$current_group" ]; then
    echo '</ul>' >> "$OUTPUT"
fi

echo '</body></html>' >> "$OUTPUT"
