#!/usr/bin/env python3
# ABOUTME: Removes duplicate and near-duplicate images from an assets directory.
# ABOUTME: Uses MD5 for exact matches and average perceptual hash for near-duplicates.

"""
Usage: python3 scripts/dedup-images.py <assets_dir> [--threshold N] [--dry-run]

Deduplicates images in two passes:
  1. Exact duplicates: same MD5 hash → keep first, remove rest
  2. Near-duplicates: perceptual hash (aHash) within threshold → keep first, remove rest

After dedup, remaining images are renumbered sequentially (img-001.png, img-002.png, ...).

Options:
  --threshold N   Max Hamming distance for near-duplicate detection (default: 5)
                  0 = only exact perceptual matches, 10+ = aggressive grouping
  --dry-run       Show what would be removed without actually deleting
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

from PIL import Image


def md5_hash(filepath):
    """Compute MD5 hash of a file."""
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def average_hash(filepath, hash_size=8):
    """Compute average perceptual hash (aHash) of an image.

    Resizes to hash_size x hash_size, converts to grayscale,
    returns a binary hash based on whether each pixel is above the mean.
    """
    try:
        img = Image.open(filepath).resize((hash_size, hash_size)).convert("L")
    except Exception:
        return None
    pixels = list(img.getdata())
    mean = sum(pixels) / len(pixels)
    return tuple(1 if p > mean else 0 for p in pixels)


def hamming_distance(hash1, hash2):
    """Count differing bits between two hashes."""
    if hash1 is None or hash2 is None:
        return float("inf")
    return sum(a != b for a, b in zip(hash1, hash2))


def dedup_images(assets_dir, threshold=5, dry_run=False):
    """Remove duplicate and near-duplicate images, renumber survivors."""
    assets_path = Path(assets_dir)
    if not assets_path.is_dir():
        print(f"Error: {assets_dir} is not a directory")
        sys.exit(1)

    images = sorted(assets_path.glob("img-*.png"))
    if not images:
        print(f"No img-*.png files found in {assets_dir}")
        return

    print(f"Scanning {len(images)} images in {assets_dir}...")

    # Pass 1: Exact duplicates (MD5)
    md5_map = {}
    exact_dupes = []
    for img in images:
        h = md5_hash(img)
        if h in md5_map:
            exact_dupes.append(img)
        else:
            md5_map[h] = img

    survivors_after_exact = [img for img in images if img not in exact_dupes]
    print(f"  Pass 1 (exact MD5): {len(exact_dupes)} duplicates found, "
          f"{len(survivors_after_exact)} unique")

    # Pass 2: Near-duplicates (perceptual hash)
    phashes = {}
    for img in survivors_after_exact:
        phashes[img] = average_hash(img)

    near_dupes = set()
    survivors = []
    for img in survivors_after_exact:
        if img in near_dupes:
            continue
        # Check against all already-accepted survivors
        is_near_dupe = False
        for kept in survivors:
            dist = hamming_distance(phashes[img], phashes[kept])
            if dist <= threshold:
                near_dupes.add(img)
                is_near_dupe = True
                break
        if not is_near_dupe:
            survivors.append(img)

    print(f"  Pass 2 (perceptual, threshold={threshold}): "
          f"{len(near_dupes)} near-duplicates found, "
          f"{len(survivors)} survivors")

    to_remove = exact_dupes + list(near_dupes)
    print(f"\n  Total: {len(images)} → {len(survivors)} "
          f"({len(to_remove)} removed)")

    if dry_run:
        print("\n  [DRY RUN] Would remove:")
        for img in sorted(to_remove):
            print(f"    {img.name}")
        print(f"\n  [DRY RUN] Would keep {len(survivors)} images:")
        for img in survivors:
            print(f"    {img.name}")
        return

    # Delete duplicates
    for img in to_remove:
        img.unlink()

    # Renumber survivors sequentially
    for i, img in enumerate(sorted(survivors), start=1):
        new_name = assets_path / f"img-{i:03d}.png"
        if img != new_name:
            # Avoid collision by using temp name first
            temp_name = assets_path / f"_tmp_rename_{i:03d}.png"
            img.rename(temp_name)

    # Second pass to finalize names (temp → final)
    temps = sorted(assets_path.glob("_tmp_rename_*.png"))
    for temp in temps:
        num = temp.stem.split("_")[-1]
        final_name = assets_path / f"img-{num}.png"
        temp.rename(final_name)

    # Also rename any survivors that didn't need temp renaming
    remaining = sorted(assets_path.glob("img-*.png"))
    print(f"\n  Renumbered to img-001.png through img-{len(remaining):03d}.png")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    assets_dir = sys.argv[1]
    threshold = 5
    dry_run = False

    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--threshold" and i + 1 < len(args):
            threshold = int(args[i + 1])
            i += 2
        elif args[i] == "--dry-run":
            dry_run = True
            i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            sys.exit(1)

    dedup_images(assets_dir, threshold=threshold, dry_run=dry_run)


if __name__ == "__main__":
    main()
