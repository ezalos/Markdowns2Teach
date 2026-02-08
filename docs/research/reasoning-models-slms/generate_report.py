# ABOUTME: Generates a markdown report from Reasoning Models & SLMs research JSON files.
# ABOUTME: Reads fields.yaml for structure and all results/*.json for data, outputs report.md.

import json
import os
import re
import yaml


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIELDS_PATH = os.path.join(SCRIPT_DIR, "fields.yaml")
OUTLINE_PATH = os.path.join(SCRIPT_DIR, "outline.yaml")
RESULTS_DIR = os.path.join(SCRIPT_DIR, "results")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "report.md")

# TOC summary fields
TOC_FIELDS = [
    "parameter_count",
    "open_or_closed",
    "pricing_per_1M_tokens",
    "context_window",
]

# Category mapping: fields.yaml category -> possible JSON keys
CATEGORY_MAPPING = {
    "identity": ["identity", "Identity"],
    "architecture": ["architecture", "Architecture"],
    "capabilities": ["capabilities", "Capabilities"],
    "benchmarks": ["benchmarks", "Benchmarks"],
    "pricing": ["pricing", "Pricing"],
    "deployment": ["deployment", "Deployment"],
    "business": ["business", "Business"],
}

# Internal fields to skip
INTERNAL_FIELDS = {"_source_file", "uncertain"}

# Category display order and labels (from outline.yaml categories)
CATEGORY_LABELS = {
    "reasoning": "Reasoning Models (Chain-of-Thought / Extended Thinking)",
    "frontier": "Frontier General-Purpose Models",
    "slm": "Small Language Models (SLMs) — Compact & Edge",
    "coding": "Specialized / Coding Models",
}


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        data = data[0]
    return data


def slugify(name):
    """Convert item name to anchor-friendly slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def get_field_value(data, field_name):
    """Look up a field in nested JSON structure."""
    if field_name in data:
        return data[field_name]
    for key, val in data.items():
        if isinstance(val, dict) and field_name in val:
            return val[field_name]
    return None


def is_uncertain(data, field_name, value):
    """Check if a field value should be skipped due to uncertainty."""
    if value is None or value == "":
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    uncertain_list = data.get("uncertain", [])
    if field_name in uncertain_list:
        return True
    return False


def truncate_for_toc(value, max_len=50):
    """Truncate a value for TOC display."""
    if value is None:
        return "—"
    s = str(value)
    if isinstance(value, list):
        s = ", ".join(str(v) for v in value)
    if len(s) > max_len:
        cut = s[:max_len].rfind(",")
        if cut > 15:
            s = s[:cut]
        else:
            s = s[:max_len] + "…"
    return s


def format_value(value, indent=0):
    """Format a field value for markdown display."""
    if value is None or value == "":
        return "—"

    prefix = "  " * indent

    if isinstance(value, list):
        if len(value) == 0:
            return "—"
        if isinstance(value[0], dict):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items() if v]
                lines.append(f"{prefix}- " + " | ".join(parts))
            return "\n".join(lines)
        if all(isinstance(v, str) and len(v) < 80 for v in value):
            return ", ".join(str(v) for v in value)
        lines = []
        for item in value:
            lines.append(f"{prefix}- {item}")
        return "\n".join(lines)

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{prefix}- **{k}**: {v}")
        return "\n".join(lines)

    return str(value)


def get_fields_for_category(fields_yaml, category_name):
    """Get the field definitions for a category from fields.yaml."""
    cat_data = fields_yaml.get(category_name, {})
    if isinstance(cat_data, dict):
        return {
            k: v
            for k, v in cat_data.items()
            if isinstance(v, dict) and "description" in v
        }
    return {}


def get_json_category_data(data, category_name):
    """Get category data from JSON, trying multiple key variants."""
    variants = CATEGORY_MAPPING.get(category_name, [category_name])
    for variant in variants:
        if variant in data and isinstance(data[variant], dict):
            return data[variant]
    return {}


def build_item_order(outline):
    """Build ordered list of items grouped by category from outline.yaml."""
    items = outline.get("items", [])
    categories = []
    category_items = {}
    for item in items:
        cat = item.get("category", "other")
        if cat not in category_items:
            categories.append(cat)
            category_items[cat] = []
        category_items[cat].append(item)
    return categories, category_items


def normalize(s):
    """Normalize a string for matching by removing non-alphanumeric chars."""
    return re.sub(r"[^a-z0-9]", "", s.lower())


def find_json_for_item(item_name, json_files):
    """Find the matching JSON file for an outline item."""
    slug = re.sub(r"[^a-zA-Z0-9]", "_", item_name)
    slug = re.sub(r"_+", "_", slug).strip("_")
    norm_slug = normalize(slug)
    matches = []
    for jf in json_files:
        basename = os.path.splitext(os.path.basename(jf))[0]
        norm_base = normalize(basename)
        if basename == slug:
            matches.append(jf)
        elif norm_slug in norm_base:
            matches.append(jf)
        elif norm_base in norm_slug:
            matches.append(jf)
    return matches


def generate_report():
    fields_yaml = load_yaml(FIELDS_PATH)
    outline = load_yaml(OUTLINE_PATH)
    topic = outline.get("topic", "Research Report")

    json_files = sorted(
        [
            os.path.join(RESULTS_DIR, f)
            for f in os.listdir(RESULTS_DIR)
            if f.endswith(".json")
        ]
    )

    all_data = {}
    for jf in json_files:
        basename = os.path.splitext(os.path.basename(jf))[0]
        all_data[basename] = load_json(jf)

    categories, category_items = build_item_order(outline)

    field_categories = [k for k in fields_yaml.keys() if k != "uncertain"]

    lines = []

    # Header
    lines.append(f"# {topic}\n")
    lines.append(f"> Generated from {len(all_data)} research files.\n")
    lines.append("---\n")

    # Table of Contents grouped by category
    lines.append("## Table of Contents\n")
    item_num = 0
    for cat in categories:
        cat_label = CATEGORY_LABELS.get(cat, cat.replace("_", " ").title())
        lines.append(f"\n### {cat_label}\n")
        lines.append(
            "| # | Model | Params | Open/Closed | Pricing (in/out 1M) | Context |"
        )
        lines.append(
            "|---|-------|--------|-------------|---------------------|---------|"
        )

        for item in category_items[cat]:
            item_num += 1
            name = item["name"]
            slug = slugify(name)
            matches = find_json_for_item(name, json_files)

            if matches:
                data = load_json(matches[0])
                params = truncate_for_toc(
                    get_field_value(data, "parameter_count"), 30
                )
                openness = truncate_for_toc(
                    get_field_value(data, "open_or_closed"), 30
                )
                pricing = truncate_for_toc(
                    get_field_value(data, "pricing_per_1M_tokens"), 40
                )
                context = truncate_for_toc(
                    get_field_value(data, "context_window"), 20
                )
            else:
                params = openness = pricing = context = "—"

            lines.append(
                f"| {item_num} | [{name}](#{slug}) | {params} | {openness} | {pricing} | {context} |"
            )

    lines.append("\n---\n")

    # Detailed sections per item
    lines.append("## Detailed Models\n")

    item_num = 0
    for cat in categories:
        cat_label = CATEGORY_LABELS.get(cat, cat.replace("_", " ").title())
        lines.append(f"\n---\n\n## {cat_label}\n")

        for item in category_items[cat]:
            item_num += 1
            name = item["name"]
            slug = slugify(name)
            matches = find_json_for_item(name, json_files)

            if not matches:
                lines.append(f"\n### {item_num}. {name}\n")
                lines.append("*No research data found.*\n")
                continue

            data = load_json(matches[0])
            source_file = os.path.basename(matches[0])

            lines.append(f"\n### {item_num}. {name}\n")
            lines.append(f"*Source: {source_file}*\n")

            for fc in field_categories:
                cat_fields = get_fields_for_category(fields_yaml, fc)
                cat_data = get_json_category_data(data, fc)

                if not cat_fields and not cat_data:
                    continue

                fc_label = fc.replace("_", " ").title()
                lines.append(f"\n#### {fc_label}\n")

                for field_name, field_def in cat_fields.items():
                    value = cat_data.get(field_name)
                    if value is None:
                        value = get_field_value(data, field_name)

                    if is_uncertain(data, field_name, value):
                        continue

                    label = field_name.replace("_", " ").title()
                    formatted = format_value(value)

                    if isinstance(value, (list, dict)) or (
                        isinstance(value, str) and len(value) > 200
                    ):
                        lines.append(f"**{label}**:\n{formatted}\n")
                    else:
                        lines.append(f"**{label}**: {formatted}\n")

            # Collect extra fields not in fields.yaml
            known_fields = set()
            for fc in field_categories:
                known_fields.update(
                    get_fields_for_category(fields_yaml, fc).keys()
                )
            known_categories = set(field_categories) | set(INTERNAL_FIELDS)
            for variants in CATEGORY_MAPPING.values():
                known_categories.update(variants)

            extra_fields = {}
            for key, val in data.items():
                if key in known_categories or key in INTERNAL_FIELDS:
                    continue
                if isinstance(val, dict):
                    for fk, fv in val.items():
                        if fk not in known_fields and fk not in INTERNAL_FIELDS:
                            if not is_uncertain(data, fk, fv):
                                extra_fields[fk] = fv
                elif key not in known_fields:
                    if not is_uncertain(data, key, val):
                        extra_fields[key] = val

            if extra_fields:
                lines.append("\n#### Other Info\n")
                for fk, fv in extra_fields.items():
                    label = fk.replace("_", " ").title()
                    formatted = format_value(fv)
                    if isinstance(fv, str) and len(fv) > 200:
                        lines.append(f"**{label}**:\n{formatted}\n")
                    else:
                        lines.append(f"**{label}**: {formatted}\n")

    # Write report
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Report generated: {OUTPUT_PATH}")
    print(f"Models: {len(all_data)}")
    print(f"Categories: {len(categories)}")


if __name__ == "__main__":
    generate_report()
