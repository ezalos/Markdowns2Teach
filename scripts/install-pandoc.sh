#!/usr/bin/env bash
# ABOUTME: Downloads pandoc binary if not already installed.
# ABOUTME: Used by 'make guide' to convert Markdown to DOCX.

set -euo pipefail

PANDOC_VERSION="3.6.4"
INSTALL_DIR="${HOME}/.local/bin"
PANDOC_BIN="${INSTALL_DIR}/pandoc"

if command -v pandoc &>/dev/null; then
    echo "  pandoc already available: $(pandoc --version | head -1)"
    exit 0
fi

if [[ -x "${PANDOC_BIN}" ]]; then
    echo "  pandoc already installed at ${PANDOC_BIN}"
    exit 0
fi

echo "  Downloading pandoc ${PANDOC_VERSION}..."
mkdir -p "${INSTALL_DIR}"

TMPDIR=$(mktemp -d)
trap 'rm -rf "${TMPDIR}"' EXIT

curl -sL "https://github.com/jgm/pandoc/releases/download/${PANDOC_VERSION}/pandoc-${PANDOC_VERSION}-linux-amd64.tar.gz" \
    | tar xz -C "${TMPDIR}"

cp "${TMPDIR}/pandoc-${PANDOC_VERSION}/bin/pandoc" "${PANDOC_BIN}"
chmod +x "${PANDOC_BIN}"

echo "  pandoc ${PANDOC_VERSION} installed to ${PANDOC_BIN}"
echo "  Make sure ${INSTALL_DIR} is in your PATH"
