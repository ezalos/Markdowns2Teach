# ABOUTME: Generates a consolidated markdown report from individual JSON research results for AI Business Models.
# ABOUTME: Reads fields.yaml for structure, processes all JSONs, outputs report.md with TOC and detailed sections.

import json
import os
import glob
import re
import yaml


# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FIELDS_PATH = os.path.join(SCRIPT_DIR, "fields.yaml")
RESULTS_DIR = os.path.join(SCRIPT_DIR, "results")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "report.md")
TOC_SUMMARY_FIELDS = [
    "type",
    "target_customer",
    "data_quality",
]

# Category mapping: fields.yaml key -> possible JSON keys
CATEGORY_MAPPING = {
    "basic_information": [
        "basic_information",
        "Basic Information",
        "basic_info",
    ],
    "business_model_structure": [
        "business_model_structure",
        "Business Model Structure",
        "business_model",
    ],
    "financial_metrics": [
        "financial_metrics",
        "Financial Metrics",
        "financials",
    ],
    "market_positioning": [
        "market_positioning",
        "Market Positioning",
        "market",
    ],
    "ai_specific_economics": [
        "ai_specific_economics",
        "AI Specific Economics",
        "ai_economics",
    ],
    "scaling_and_growth": [
        "scaling_and_growth",
        "Scaling and Growth",
        "scaling_growth",
        "scaling",
    ],
    "risk_and_challenges": [
        "risk_and_challenges",
        "Risk and Challenges",
        "risks",
    ],
    "entrepreneurial_relevance": [
        "entrepreneurial_relevance",
        "Entrepreneurial Relevance",
        "entrepreneurial",
    ],
    "confidence": [
        "confidence",
        "Confidence",
        "data_confidence",
    ],
}

# Internal/meta fields to skip
INTERNAL_FIELDS = {"_source_file", "uncertain"}
CATEGORY_KEYS = set()
for variants in CATEGORY_MAPPING.values():
    CATEGORY_KEYS.update(variants)


def load_fields_yaml(path):
    """Load fields.yaml and return ordered list of (category, [(field_name, description)])."""
    with open(path, "r") as f:
        data = yaml.safe_load(f)

    categories = []
    for cat_key, cat_value in data.items():
        if cat_key in ("uncertain",):
            continue
        if isinstance(cat_value, dict):
            fields = []
            for field_name, field_def in cat_value.items():
                desc = ""
                if isinstance(field_def, dict):
                    desc = field_def.get("description", "")
                fields.append((field_name, desc))
            categories.append((cat_key, fields))
    return categories


def find_field_value(data, field_name, category_key):
    """Look up a field value in JSON data, trying multiple strategies."""
    # Strategy 1: Top-level
    if field_name in data:
        return data[field_name]

    # Strategy 2: Under the category key (exact match)
    if category_key in data and isinstance(data[category_key], dict):
        if field_name in data[category_key]:
            return data[category_key][field_name]

    # Strategy 3: Under any variant of the category key
    variants = CATEGORY_MAPPING.get(category_key, [category_key])
    for variant in variants:
        if variant in data and isinstance(data[variant], dict):
            if field_name in data[variant]:
                return data[variant][field_name]

    # Strategy 4: Traverse all nested dicts
    for key, value in data.items():
        if isinstance(value, dict) and field_name in value:
            return value[field_name]

    return None


def is_uncertain(value, field_name, uncertain_list):
    """Check if a field value should be skipped as uncertain."""
    if field_name in uncertain_list:
        return True
    if value is None or value == "":
        return True
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    return False


def format_value(value, indent=0):
    """Format a complex value for markdown display."""
    if value is None or value == "":
        return "_N/A_"

    if isinstance(value, list):
        if len(value) == 0:
            return "_None_"
        # List of dicts
        if isinstance(value[0], dict):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items() if v]
                lines.append("  " * indent + "- " + " | ".join(parts))
            return "\n".join(lines)
        # List of strings
        if len(value) <= 3 and all(isinstance(v, str) and len(v) < 60 for v in value):
            return ", ".join(str(v) for v in value)
        else:
            lines = []
            for item in value:
                lines.append("  " * indent + "- " + str(item))
            return "\n".join(lines)

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if isinstance(v, (dict, list)):
                formatted = format_value(v, indent + 1)
                lines.append(f"  " * indent + f"- **{k}**:\n{formatted}")
            else:
                lines.append(f"  " * indent + f"- **{k}**: {v}")
        return "\n".join(lines)

    # String value
    s = str(value)
    if len(s) > 200:
        return s
    return s


def slugify(name):
    """Create an anchor-friendly slug from a name."""
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def get_toc_field_value(data, field_name):
    """Get a short summary value for TOC display."""
    value = find_field_value(data, field_name, "basic_information")
    if value is None:
        # Try all categories
        for cat_key in CATEGORY_MAPPING:
            value = find_field_value(data, field_name, cat_key)
            if value is not None:
                break

    if value is None:
        return "N/A"

    s = str(value)
    # Truncate for TOC display
    if len(s) > 60:
        s = s[:57] + "..."
    return s


def main():
    # Load field definitions
    categories = load_fields_yaml(FIELDS_PATH)
    all_defined_fields = set()
    for _, fields in categories:
        for field_name, _ in fields:
            all_defined_fields.add(field_name)

    # Load all JSON results
    json_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "*.json")))
    if not json_files:
        print("No JSON files found in results directory!")
        return

    items = []
    for jf in json_files:
        with open(jf, "r") as f:
            data = json.load(f)
        # Get item name
        name = find_field_value(data, "name", "basic_information") or os.path.basename(
            jf
        ).replace(".json", "").replace("_", " ")
        items.append({"name": name, "data": data, "file": os.path.basename(jf)})

    print(f"Loaded {len(items)} items from {RESULTS_DIR}")

    # Build report
    lines = []
    lines.append(
        "# AI Business Models & Strategy 2024-2026 — Research Report\n"
    )
    lines.append(
        "> Comprehensive mapping of AI business models — revenue patterns, pricing strategies, "
        "unit economics, investment dynamics, competitive moats, and case studies. Emphasis on "
        "entrepreneurial decision-making for AI-native startups and AI adoption in traditional businesses.\n"
    )
    lines.append(f"**Items covered:** {len(items)}  ")
    lines.append(f"**Generated from:** `{RESULTS_DIR}`\n")

    # --- Table of Contents ---
    lines.append("---\n")
    lines.append("## Table of Contents\n")
    lines.append(
        "| # | Item | Type | Target Customer | Data Quality |"
    )
    lines.append("|---|------|------|-----------------|--------------|")

    for i, item in enumerate(items, 1):
        slug = slugify(item["name"])
        name_link = f"[{item['name']}](#{slug})"
        type_val = get_toc_field_value(item["data"], "type")
        target_val = get_toc_field_value(item["data"], "target_customer")
        quality_val = get_toc_field_value(item["data"], "data_quality")
        lines.append(
            f"| {i} | {name_link} | {type_val} | {target_val} | {quality_val} |"
        )

    lines.append("")

    # --- Detailed Sections ---
    lines.append("---\n")
    lines.append("## Detailed Research Results\n")

    for i, item in enumerate(items, 1):
        data = item["data"]
        uncertain_list = data.get("uncertain", [])
        if isinstance(uncertain_list, str):
            uncertain_list = [uncertain_list]

        lines.append(f"### {i}. {item['name']}\n")
        lines.append(f"_Source: `{item['file']}`_\n")

        # Process each category from fields.yaml
        for cat_key, fields in categories:
            cat_display = cat_key.replace("_", " ").title()
            cat_lines = []

            for field_name, field_desc in fields:
                value = find_field_value(data, field_name, cat_key)
                if is_uncertain(value, field_name, uncertain_list):
                    continue

                field_display = field_name.replace("_", " ").title()
                formatted = format_value(value)

                # Decide inline vs block display
                if "\n" in formatted:
                    cat_lines.append(f"**{field_display}:**\n\n{formatted}\n")
                else:
                    cat_lines.append(f"**{field_display}:** {formatted}\n")

            if cat_lines:
                lines.append(f"#### {cat_display}\n")
                lines.extend(cat_lines)

        # Extra fields (in JSON but not in fields.yaml)
        extra_lines = []
        all_json_fields = set()

        def collect_fields(d, prefix=""):
            for k, v in d.items():
                if k in INTERNAL_FIELDS or k in CATEGORY_KEYS:
                    if isinstance(v, dict):
                        collect_fields(v, prefix)
                    continue
                all_json_fields.add(k)

        collect_fields(data)
        extra_fields = all_json_fields - all_defined_fields
        if extra_fields:
            for ef in sorted(extra_fields):
                value = find_field_value(data, ef, "")
                if value is not None and value != "" and not is_uncertain(
                    value, ef, uncertain_list
                ):
                    formatted = format_value(value)
                    ef_display = ef.replace("_", " ").title()
                    if "\n" in formatted:
                        extra_lines.append(f"**{ef_display}:**\n\n{formatted}\n")
                    else:
                        extra_lines.append(f"**{ef_display}:** {formatted}\n")

        if extra_lines:
            lines.append("#### Other Info\n")
            lines.extend(extra_lines)

        # Uncertain fields summary
        if uncertain_list:
            lines.append("#### Uncertain Fields\n")
            for uf in uncertain_list:
                lines.append(f"- {uf}")
            lines.append("")

        lines.append("---\n")

    # Write report
    report = "\n".join(lines)
    with open(OUTPUT_PATH, "w") as f:
        f.write(report)

    print(f"Report written to {OUTPUT_PATH}")
    print(f"Total items: {len(items)}")
    print(f"Total categories: {len(categories)}")


if __name__ == "__main__":
    main()
