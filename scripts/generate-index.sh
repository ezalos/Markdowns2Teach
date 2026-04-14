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
<p class="subtitle">Deep Tech &amp; ML (UE3) — M2 IMT&amp;E · Paris 1 Panthéon-Sorbonne</p>
HEADER

# Source-driven grouping: walk slides/<SUBDIR>/*.md and render the matching HTML
# (named "<subdir>-<deck>.html" by the Makefile's flat-output convention).
# This grounds the grouping in the directory layout so any subdir works — no
# regex updates needed when a new deck dir (station-f, extra-decks, ...) is added.

label_for_slug() {
    case "$1" in
        session-01)  echo "Session 1 — Comprendre l'IA en 2026" ;;
        session-02)  echo "Session 2 — Construire avec l'IA" ;;
        session-03)  echo "Session 3 — Cadrer un projet IA" ;;
        session-04)  echo "Session 4 — Le business de l'IA" ;;
        session-05)  echo "Session 5 — Éthique, gouvernance & clôture" ;;
        evaluation)  echo "Evaluation reference decks" ;;
        station-f)   echo "Station F — Building With AI (EN)" ;;
        extra-decks) echo "Archived / extra decks" ;;
        *)           echo "$1" ;;
    esac
}

# Deterministic order: most-recent work first (station-f), then sessions
# in course order (sorted), then evaluation, anything else alphabetically,
# then extra-decks (archive) last. Update the leading group when newer work
# supersedes station-f as the freshest deck set.
all_slugs=""
for subdir in "$SLIDES_DIR"/*/; do
    [ -d "$subdir" ] || continue
    all_slugs+="$(basename "$subdir")"$'\n'
done

sessions=$(echo "$all_slugs" | grep -E '^session-' | sort || true)
has_eval=$(echo "$all_slugs" | grep -Fx 'evaluation' || true)
has_stationf=$(echo "$all_slugs" | grep -Fx 'station-f' || true)
has_extra=$(echo "$all_slugs" | grep -Fx 'extra-decks' || true)
others=$(echo "$all_slugs" | grep -vE '^(session-|evaluation$|station-f$|extra-decks$)' | grep -v '^$' | sort || true)

ordered_slugs=$(printf "%s\n%s\n%s\n%s\n%s\n" "$has_stationf" "$sessions" "$has_eval" "$others" "$has_extra" | grep -v '^$' || true)

while IFS= read -r slug; do
    [ -z "$slug" ] && continue
    subdir="$SLIDES_DIR/$slug"
    # Collect source .md files in this subdir (sorted)
    mds=$(find "$subdir" -maxdepth 1 -name '*.md' -type f 2>/dev/null | sort)
    [ -z "$mds" ] && continue

    header_emitted=false
    while IFS= read -r src; do
        [ -f "$src" ] || continue
        deck_base=$(basename "$src" .md)
        htmlfile="$slug-$deck_base.html"
        [ -f "$HTML_DIR/$htmlfile" ] || continue

        if ! $header_emitted; then
            label=$(label_for_slug "$slug")
            echo "<h2>$label</h2>" >> "$OUTPUT"
            echo '<ul>' >> "$OUTPUT"
            header_emitted=true
        fi

        title=$(get_title "$src")
        if [ -z "$title" ]; then
            title=$(echo "$deck_base" | sed 's/^[0-9]*-//;s/-/ /g')
        fi
        echo "<li><a href=\"$htmlfile\">$title</a><span class=\"deck-file\">$htmlfile</span></li>" >> "$OUTPUT"
    done <<< "$mds"

    $header_emitted && echo '</ul>' >> "$OUTPUT"
done <<< "$ordered_slugs"

echo '</body></html>' >> "$OUTPUT"
