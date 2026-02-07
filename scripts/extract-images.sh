#!/usr/bin/env bash
# ABOUTME: Extracts embedded images from a PDF using pdfimages.
# ABOUTME: Filters out small images (<200px wide) and renames sequentially.

set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <input.pdf> <output-dir>"
  echo "  Extracts PNG images from a PDF, filtering out small ones."
  exit 1
fi

INPUT_PDF="$1"
OUTPUT_DIR="$2"
MIN_WIDTH="${3:-200}"

if [[ ! -f "$INPUT_PDF" ]]; then
  echo "ERROR: File not found: $INPUT_PDF"
  exit 1
fi

TMPDIR=$(mktemp -d)
trap 'rm -rf "$TMPDIR"' EXIT

echo "Extracting images from: $INPUT_PDF"
pdfimages -png "$INPUT_PDF" "$TMPDIR/raw"

mkdir -p "$OUTPUT_DIR"

counter=1
for img in "$TMPDIR"/raw-*.png; do
  [[ -f "$img" ]] || continue

  # Get image width using identify (ImageMagick) or file
  width=$(identify -format "%w" "$img" 2>/dev/null || echo "0")

  if (( width < MIN_WIDTH )); then
    echo "  SKIP (${width}px wide): $(basename "$img")"
    continue
  fi

  dest=$(printf "%s/img-%03d.png" "$OUTPUT_DIR" "$counter")
  cp "$img" "$dest"
  echo "  KEEP (${width}px wide): $(basename "$img") -> $(basename "$dest")"
  counter=$((counter + 1))
done

total=$((counter - 1))
echo "Done: $total images extracted to $OUTPUT_DIR"
