#!/usr/bin/env bash
# ABOUTME: Linter that warns when numbered data slides lack source citations.
# ABOUTME: Detects slides with financial/statistical figures ($, €, %) missing a <small>Sources line.

set -euo pipefail

SLIDES_DIR="${1:-slides}"
EXIT_CODE=0

for file in $(find "$SLIDES_DIR" -name '*.md' -type f | sort); do
  slide_num=0
  has_data=false
  has_sources=false
  is_discussion=false
  is_section=false
  is_numbered=false
  slide_title=""

  while IFS= read -r line; do
    # Slide separator
    if [[ "$line" == "---" ]]; then
      if (( slide_num > 0 )) && $is_numbered && $has_data && ! $has_sources && ! $is_discussion && ! $is_section; then
        echo "WARNING: $file slide $slide_num ($slide_title) has data but no Sources line"
        EXIT_CODE=1
      fi
      slide_num=$((slide_num + 1))
      has_data=false
      has_sources=false
      is_discussion=false
      is_section=false
      is_numbered=false
      slide_title=""
      continue
    fi

    # Detect section dividers
    [[ "$line" =~ _class:\ *section ]] && is_section=true

    # Detect numbered slides (# 01 — Title)
    if [[ "$line" =~ ^#\ [0-9]{2}\ —\  ]]; then
      is_numbered=true
      slide_title="$line"
    fi

    # Detect discussion slides
    [[ "$line" =~ Discussion ]] && is_discussion=true
    [[ "$line" =~ "Key Takeaways" ]] && is_discussion=true

    # Detect data claims (currency symbols, percentages, large numbers)
    if [[ "$line" =~ [\$€£] ]] || [[ "$line" =~ [0-9]+% ]] || [[ "$line" =~ [0-9]+[[:space:]]*(Mds|Md|M\ |B\ |Mrd) ]]; then
      has_data=true
    fi

    # Detect sources line
    [[ "$line" =~ \<small\>Sources ]] && has_sources=true

  done < "$file"

  # Check the last slide
  if (( slide_num > 0 )) && $is_numbered && $has_data && ! $has_sources && ! $is_discussion && ! $is_section; then
    echo "WARNING: $file slide $slide_num ($slide_title) has data but no Sources line"
    EXIT_CODE=1
  fi
done

if (( EXIT_CODE == 0 )); then
  echo "OK: All data slides have source citations."
fi

exit $EXIT_CODE
