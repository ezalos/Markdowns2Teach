# ABOUTME: Generates report.md from individual JSON research files for AI Project Frameworks & Methodologies.
# ABOUTME: Reads fields.yaml for structure, processes 24 JSONs from results/, outputs a categorized markdown report.

import json
import os
import re
import yaml

TOPIC_DIR = os.path.dirname(os.path.abspath(__file__))
FIELDS_PATH = os.path.join(TOPIC_DIR, "fields.yaml")
OUTLINE_PATH = os.path.join(TOPIC_DIR, "outline.yaml")
RESULTS_DIR = os.path.join(TOPIC_DIR, "results")
OUTPUT_PATH = os.path.join(TOPIC_DIR, "report.md")

# TOC summary fields (user-selected)
TOC_FIELDS = [
    "framework_type",
    "free_or_paid",
    "session_mapping",
]

# Category mapping: fields.yaml key -> possible JSON keys
CATEGORY_MAPPING = {
    "identity": ["identity"],
    "framework_profile": ["framework_profile"],
    "accessibility_and_adoption": ["accessibility_and_adoption"],
    "entrepreneurial_relevance": ["entrepreneurial_relevance"],
    "practical_application": ["practical_application"],
}

# Internal/meta fields to skip in "Other Info"
SKIP_FIELDS = {"_source_file", "uncertain"}


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def slugify(name):
    """Create markdown anchor from resource name."""
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def get_field_value(data, field_name):
    """Look up a field value in flat or nested JSON."""
    # Flat lookup first
    if field_name in data:
        return data[field_name]
    # Nested lookup: search all dict values
    for key, val in data.items():
        if isinstance(val, dict) and field_name in val:
            return val[field_name]
    return None


def is_uncertain(data, field_name):
    """Check if a field is marked as uncertain."""
    uncertain_list = data.get("uncertain", [])
    if field_name in uncertain_list:
        return True
    val = get_field_value(data, field_name)
    if isinstance(val, str) and "[uncertain]" in val:
        return True
    return False


def format_value(val):
    """Format a value for markdown display."""
    if val is None or val == "":
        return "*N/A*"
    if isinstance(val, list):
        if len(val) == 0:
            return "*N/A*"
        if all(isinstance(item, dict) for item in val):
            lines = []
            for item in val:
                parts = [f"**{k}**: {v}" for k, v in item.items()]
                lines.append(" | ".join(parts))
            return "\n".join(f"- {line}" for line in lines)
        if len(val) <= 5 and all(isinstance(item, str) and len(item) < 50 for item in val):
            return ", ".join(str(v) for v in val)
        return "\n".join(f"- {v}" for v in val)
    if isinstance(val, dict):
        parts = []
        for k, v in val.items():
            parts.append(f"**{k}**: {v}")
        return "; ".join(parts)
    val_str = str(val)
    return val_str


def extract_short_value(val, max_len=30):
    """Extract a short summary from a potentially long field value.

    Many Research 5 fields include explanations after a core value
    (e.g., 'Free — Published as an open...'). This extracts just the
    core value before the explanation.
    """
    if val is None or val == "":
        return "—"
    val_str = str(val)
    # Try splitting on common separators to get the core value
    for sep in [" — ", " -- ", " - ", ". ", "; "]:
        if sep in val_str:
            short = val_str.split(sep)[0].strip()
            if len(short) <= max_len:
                return short
    # Truncate if still too long
    if len(val_str) > max_len:
        return val_str[:max_len - 3] + "..."
    return val_str


def format_toc_value(val, max_len=30):
    """Format a value for compact TOC display."""
    return extract_short_value(val, max_len)


def get_all_defined_fields(fields_yaml):
    """Extract all field names from fields.yaml."""
    defined = {}
    categories = fields_yaml.get("field_categories", {})
    for cat_key, cat_val in categories.items():
        if cat_key == "uncertain":
            continue
        if not isinstance(cat_val, dict):
            continue
        fields = cat_val.get("fields", {})
        if not isinstance(fields, dict):
            continue
        for field_name, field_def in fields.items():
            desc = field_def.get("description", "") if isinstance(field_def, dict) else ""
            defined[field_name] = {"category": cat_key, "description": desc}
    return defined


def get_category_display_name(cat_key, fields_yaml):
    """Get human-readable category name."""
    categories = fields_yaml.get("field_categories", {})
    cat_val = categories.get(cat_key, {})
    desc = cat_val.get("description", "")
    # Convert snake_case to Title Case
    display = cat_key.replace("_", " ").title()
    return display


def build_category_order(fields_yaml):
    """Get ordered list of categories from fields.yaml."""
    categories = fields_yaml.get("field_categories", {})
    return [k for k in categories.keys() if k != "uncertain"]


def build_fields_by_category(fields_yaml):
    """Build {category: [field_names]} mapping."""
    result = {}
    categories = fields_yaml.get("field_categories", {})
    for cat_key, cat_val in categories.items():
        if cat_key == "uncertain":
            continue
        if not isinstance(cat_val, dict):
            continue
        fields = cat_val.get("fields", {})
        if not isinstance(fields, dict):
            continue
        result[cat_key] = list(fields.keys())
    return result


def normalize(s):
    """Strip punctuation, @, parens content, lowercase for matching."""
    s = s.lower().strip()
    s = re.sub(r"@", "", s)
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthetical
    s = re.sub(r"[^\w\s]", " ", s)  # punctuation to space
    s = re.sub(r"\s+", " ", s).strip()
    return s


def outline_name_to_slug(name):
    """Convert outline item name to the expected filename slug."""
    slug = name.strip()
    slug = re.sub(r"[^\w\s\-]", "", slug)  # remove special chars but keep hyphens
    slug = re.sub(r"\s+", "_", slug)
    return slug


def main():
    # Load config
    fields_yaml = load_yaml(FIELDS_PATH)
    outline = load_yaml(OUTLINE_PATH)

    # Get category order from outline
    outline_categories = [c["name"] for c in outline.get("categories", [])]

    # Build item -> category mapping from outline
    item_categories = {}
    for item in outline.get("items", []):
        item_categories[item["name"]] = item.get("category", "Uncategorized")

    # Load all JSONs
    json_files = sorted(
        [f for f in os.listdir(RESULTS_DIR) if f.endswith(".json")]
    )
    resources = []
    for jf in json_files:
        data = load_json(os.path.join(RESULTS_DIR, jf))
        data["_source_file"] = jf
        resources.append(data)

    # Pre-build filename -> outline mapping
    filename_to_outline = {}
    for item in outline.get("items", []):
        slug = outline_name_to_slug(item["name"])
        filename_to_outline[slug + ".json"] = item["name"]
        # Also try common variations
        filename_to_outline[slug.replace("__", "_") + ".json"] = item["name"]

    categorized = {cat: [] for cat in outline_categories}
    unmatched = []
    for res in resources:
        name = res.get("framework_name", res["_source_file"])
        source_file = res.get("_source_file", "")
        matched = False

        # Method 1: Direct filename match via slug mapping
        if source_file in filename_to_outline:
            outline_name = filename_to_outline[source_file]
            outline_cat = item_categories[outline_name]
            if outline_cat in categorized:
                categorized[outline_cat].append(res)
                matched = True

        # Method 2: Normalized name matching with best-match scoring
        if not matched:
            best_match = None
            best_score = 0
            for outline_name, outline_cat in item_categories.items():
                jn_norm = normalize(name)
                on_norm = normalize(outline_name)
                # Exact normalized match
                if jn_norm == on_norm:
                    best_match = (outline_name, outline_cat)
                    best_score = 100
                    break
                # One contains the other (prefer longer overlap)
                if on_norm in jn_norm or jn_norm in on_norm:
                    overlap_len = min(len(jn_norm), len(on_norm))
                    if overlap_len > best_score:
                        best_match = (outline_name, outline_cat)
                        best_score = overlap_len
                # Word overlap with first-word match
                jn_words = jn_norm.split()
                on_words = on_norm.split()
                if jn_words and on_words:
                    overlap = set(jn_words) & set(on_words)
                    if len(overlap) >= 2 and jn_words[0] == on_words[0]:
                        score = len(overlap) * 10
                        if score > best_score:
                            best_match = (outline_name, outline_cat)
                            best_score = score

            if best_match:
                outline_cat = best_match[1]
                if outline_cat in categorized:
                    categorized[outline_cat].append(res)
                    matched = True

        # Method 3: Fallback by source filename words
        if not matched:
            file_stem = source_file.replace(".json", "").replace("_", " ").lower()
            best_match = None
            best_score = 0
            for outline_name, outline_cat in item_categories.items():
                on_norm = normalize(outline_name)
                if file_stem == on_norm:
                    best_match = (outline_name, outline_cat)
                    best_score = 100
                    break
                if on_norm in file_stem or file_stem in on_norm:
                    overlap_len = min(len(file_stem), len(on_norm))
                    if overlap_len > best_score:
                        best_match = (outline_name, outline_cat)
                        best_score = overlap_len
            if best_match:
                outline_cat = best_match[1]
                if outline_cat in categorized:
                    categorized[outline_cat].append(res)
                    matched = True

        if not matched:
            unmatched.append(res)

    # Get field structure
    defined_fields = get_all_defined_fields(fields_yaml)
    cat_order = build_category_order(fields_yaml)
    fields_by_cat = build_fields_by_category(fields_yaml)

    # Build report
    lines = []
    lines.append("# AI Project Frameworks & Methodologies 2024-2026")
    lines.append("")
    lines.append("> Practical frameworks and methodologies for framing, planning, and managing AI projects.")
    lines.append("> 24 frameworks across 10 categories. Targeted at M2 Entrepreneurship students (Sorbonne).")
    lines.append("> Business-oriented, actionable, current as of February 2026.")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === TABLE OF CONTENTS ===
    lines.append("## Table of Contents")
    lines.append("")

    global_idx = 0
    for cat_name in outline_categories:
        cat_resources = categorized.get(cat_name, [])
        if not cat_resources:
            continue
        cat_slug = slugify(cat_name)
        lines.append(f"### [{cat_name}](#{cat_slug})")
        lines.append("")
        lines.append("| # | Framework | Type | Access | Sessions |")
        lines.append("|---|-----------|------|--------|----------|")

        for res in cat_resources:
            global_idx += 1
            name = res.get("framework_name", "Unknown")
            anchor = slugify(name)
            f_type = format_toc_value(get_field_value(res, "framework_type"), 30)
            access = format_toc_value(get_field_value(res, "free_or_paid"), 25)
            sessions = format_toc_value(get_field_value(res, "session_mapping"), 30)
            lines.append(
                f"| {global_idx} | [{name}](#{anchor}) | {f_type} | {access} | {sessions} |"
            )

        lines.append("")

    lines.append("---")
    lines.append("")

    # === DETAILED PROFILES ===
    global_idx = 0
    for cat_name in outline_categories:
        cat_resources = categorized.get(cat_name, [])
        if not cat_resources:
            continue

        lines.append(f"## {cat_name}")
        lines.append("")

        for res in cat_resources:
            global_idx += 1
            name = res.get("framework_name", "Unknown")
            lines.append(f"### {name}")
            lines.append("")

            # Render fields by category
            for cat_key in cat_order:
                cat_fields = fields_by_cat.get(cat_key, [])
                if not cat_fields:
                    continue

                cat_display = get_category_display_name(cat_key, fields_yaml)
                has_content = False
                cat_lines = []

                for field_name in cat_fields:
                    if is_uncertain(res, field_name):
                        continue
                    val = get_field_value(res, field_name)
                    if val is None or val == "":
                        continue
                    formatted = format_value(val)
                    field_display = field_name.replace("_", " ").title()
                    cat_lines.append(f"- **{field_display}**: {formatted}")
                    has_content = True

                if has_content:
                    lines.append(f"**{cat_display}**")
                    lines.append("")
                    lines.extend(cat_lines)
                    lines.append("")

            # Uncertain fields
            uncertain = res.get("uncertain", [])
            if uncertain:
                lines.append("**Uncertain Fields**")
                lines.append("")
                for uf in uncertain:
                    lines.append(f"- {uf}")
                lines.append("")

            # Extra fields not in fields.yaml
            all_json_fields = set()
            for k, v in res.items():
                if isinstance(v, dict):
                    all_json_fields.update(v.keys())
                else:
                    all_json_fields.add(k)

            extra = all_json_fields - set(defined_fields.keys()) - SKIP_FIELDS
            # Remove top-level category keys
            for cat_key in CATEGORY_MAPPING:
                extra.discard(cat_key)

            if extra:
                lines.append("**Other Info**")
                lines.append("")
                for ef in sorted(extra):
                    val = get_field_value(res, ef)
                    if val is not None and val != "":
                        formatted = format_value(val)
                        field_display = ef.replace("_", " ").title()
                        lines.append(f"- **{field_display}**: {formatted}")
                lines.append("")

            lines.append("---")
            lines.append("")

    # Handle unmatched resources
    if unmatched:
        lines.append("## Uncategorized Frameworks")
        lines.append("")
        for res in unmatched:
            name = res.get("framework_name", res.get("_source_file", "Unknown"))
            lines.append(f"### {name}")
            lines.append("")
            lines.append(f"*Source file: {res.get('_source_file', 'unknown')}*")
            lines.append("")
            for field_name in sorted(defined_fields.keys()):
                if is_uncertain(res, field_name):
                    continue
                val = get_field_value(res, field_name)
                if val is not None and val != "":
                    formatted = format_value(val)
                    field_display = field_name.replace("_", " ").title()
                    lines.append(f"- **{field_display}**: {formatted}")
            lines.append("")
            lines.append("---")
            lines.append("")

    # Write report
    report = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report generated: {OUTPUT_PATH}")
    print(f"Total frameworks: {len(resources)}")
    print(f"Categorized: {sum(len(v) for v in categorized.values())}")
    print(f"Unmatched: {len(unmatched)}")
    for cat_name in outline_categories:
        count = len(categorized.get(cat_name, []))
        if count > 0:
            print(f"  {cat_name}: {count}")
    print(f"Report length: {len(report):,} characters, {report.count(chr(10)):,} lines")


if __name__ == "__main__":
    main()
