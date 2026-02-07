#!/usr/bin/env bash
# ABOUTME: Linter that warns about slides likely to overflow the viewport.
# ABOUTME: Splits markdown on '---' separators and counts content lines per slide.

set -euo pipefail

THRESHOLD="${1:-15}"
SLIDES_DIR="${2:-slides}"
EXIT_CODE=0

for file in $(find "$SLIDES_DIR" -name '*.md' -type f | sort); do
  slide_num=0
  line_count=0

  while IFS= read -r line; do
    # Slide separator
    if [[ "$line" == "---" ]]; then
      if (( slide_num > 0 && line_count > THRESHOLD )); then
        echo "WARNING: $file slide $slide_num has $line_count content lines (threshold: $THRESHOLD)"
        EXIT_CODE=1
      fi
      slide_num=$((slide_num + 1))
      line_count=0
      continue
    fi

    # Skip empty lines
    [[ -z "${line// /}" ]] && continue
    # Skip HTML comments (directives)
    [[ "$line" =~ ^[[:space:]]*\<\!-- ]] && continue
    # Skip front matter markers (already handled by ---)
    # Count this as a content line
    line_count=$((line_count + 1))
  done < "$file"

  # Check the last slide (no trailing ---)
  if (( slide_num > 0 && line_count > THRESHOLD )); then
    echo "WARNING: $file slide $slide_num has $line_count content lines (threshold: $THRESHOLD)"
    EXIT_CODE=1
  fi
done

if (( EXIT_CODE == 0 )); then
  echo "OK: No overflow warnings (threshold: $THRESHOLD lines)."
fi

exit $EXIT_CODE
