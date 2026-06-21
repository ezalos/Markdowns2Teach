# ABOUTME: Generates report.md from individual JSON prompt engineering research files.
# ABOUTME: Reads fields.yaml for structure, outputs TOC + detailed profiles per technique.

import json
import glob
import os
import re
import yaml

# --- Configuration ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(SCRIPT_DIR, "results")
FIELDS_PATH = os.path.join(SCRIPT_DIR, "fields.yaml")
OUTLINE_PATH = os.path.join(SCRIPT_DIR, "outline.yaml")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "report.md")

# TOC summary fields (user-selected)
TOC_FIELDS = ["category_type", "difficulty_level"]
TOC_LABELS = ["Type", "Difficulty"]

# Internal fields to skip
SKIP_FIELDS = {"uncertain", "_source_file"}


def load_yaml(path):
    """Load a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def find_field(data, key):
    """Recursively search for a field in nested dict structure."""
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for v in data.values():
            result = find_field(v, key)
            if result is not None:
                return result
    return None


def get_uncertain_fields(data):
    """Get set of uncertain field names from JSON data."""
    uncertain = set()
    unc_list = find_field(data, "uncertain")
    if isinstance(unc_list, list):
        uncertain.update(unc_list)
    return uncertain


def is_uncertain_value(value):
    """Check if a value contains [uncertain] marker."""
    if isinstance(value, str) and "[uncertain]" in value:
        return True
    return False


def should_skip_field(field_name, value, uncertain_fields):
    """Determine if a field should be skipped in output."""
    if field_name in SKIP_FIELDS:
        return True
    if field_name in uncertain_fields:
        return True
    if is_uncertain_value(value):
        return True
    if value is None or value == "":
        return True
    return False


def format_value(value, indent=0):
    """Format a field value for markdown output."""
    prefix = "  " * indent

    if isinstance(value, list):
        if not value:
            return "None"
        # List of dicts
        if isinstance(value[0], dict):
            lines = []
            for item in value:
                parts = [f"{k}: {v}" for k, v in item.items() if v]
                lines.append(f"{prefix}- {' | '.join(parts)}")
            return "\n".join(lines)
        # Simple list
        if len(value) <= 3 and all(len(str(v)) < 60 for v in value):
            return ", ".join(str(v) for v in value)
        lines = [f"{prefix}- {v}" for v in value]
        return "\n".join(lines)

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if v is not None and v != "":
                formatted = format_value(v, indent + 1)
                if "\n" in formatted:
                    lines.append(f"{prefix}- **{k}**:\n{formatted}")
                else:
                    lines.append(f"{prefix}- **{k}**: {formatted}")
        return "\n".join(lines)

    # String value
    text = str(value)
    return text


def slugify(name):
    """Create a markdown anchor slug from a name."""
    slug = name.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')


def parse_field_categories(fields_yaml):
    """Parse fields.yaml into ordered list of (category_name, [field_names])."""
    categories = []
    for cat in fields_yaml.get("field_categories", []):
        cat_name = cat.get("name", cat.get("category", "Unknown"))
        field_names = [f["name"] for f in cat.get("fields", [])]
        categories.append((cat_name, field_names))
    return categories


def get_category_order(outline_yaml):
    """Get the category display order and item ordering from outline.yaml."""
    cat_order = [c["name"] for c in outline_yaml.get("categories", [])]
    # Build item order: list of (item_name, category)
    items_order = []
    for item in outline_yaml.get("items", []):
        items_order.append((item["name"], item.get("category", "")))
    return cat_order, items_order


def main():
    # Load config files
    fields_yaml = load_yaml(FIELDS_PATH)
    outline_yaml = load_yaml(OUTLINE_PATH)
    field_categories = parse_field_categories(fields_yaml)
    cat_order, items_order = get_category_order(outline_yaml)

    # Collect all field names from fields.yaml
    all_defined_fields = set()
    for _, field_names in field_categories:
        all_defined_fields.update(field_names)

    # Load all JSON results
    json_files = sorted(glob.glob(os.path.join(RESULTS_DIR, "*.json")))
    techniques = {}
    for jf in json_files:
        data = load_json(jf)
        name = find_field(data, "technique_name")
        if not name:
            name = os.path.basename(jf).replace(".json", "").replace("_", " ")
        techniques[os.path.basename(jf)] = {
            "name": name,
            "data": data,
            "file": os.path.basename(jf),
        }

    # Map outline item names to JSON files
    json_lookup = {}
    for fname, tech in techniques.items():
        json_lookup[tech["name"].lower()] = fname
        # Also index by filename stem
        stem = fname.replace(".json", "").replace("_", " ").lower()
        json_lookup[stem] = fname

    # Order techniques by outline order
    ordered_techniques = []
    used_files = set()
    for item_name, item_cat in items_order:
        # Try to find matching JSON
        match = None
        item_lower = item_name.lower()
        for key, fname in json_lookup.items():
            if item_lower in key or key in item_lower:
                match = fname
                break
        if not match:
            # Fuzzy: try first word
            first_word = item_lower.split()[0]
            for key, fname in json_lookup.items():
                if first_word in key:
                    match = fname
                    break
        if match and match not in used_files:
            ordered_techniques.append((item_name, item_cat, techniques[match]))
            used_files.add(match)

    # Add any unmatched JSON files at the end
    for fname, tech in techniques.items():
        if fname not in used_files:
            ordered_techniques.append((tech["name"], "Other", tech))

    # --- Generate Report ---
    lines = []
    topic = outline_yaml.get("topic", "Research Report")

    # Header
    lines.append(f"# {topic}")
    lines.append("")
    lines.append(f"*Generated from {len(ordered_techniques)} technique research files.*")
    lines.append("")
    lines.append("---")
    lines.append("")

    # Table of Contents — grouped by category
    lines.append("## Table of Contents")
    lines.append("")

    current_cat = None
    tech_num = 0
    for item_name, item_cat, tech in ordered_techniques:
        if item_cat != current_cat:
            current_cat = item_cat
            lines.append(f"### {current_cat}")
            lines.append("")
            lines.append(f"| # | Technique | {' | '.join(TOC_LABELS)} |")
            lines.append(f"|---|-----------|{'|'.join(['---'] * len(TOC_LABELS))}|")

        tech_num += 1
        data = tech["data"]
        uncertain = get_uncertain_fields(data)
        slug = slugify(tech["name"])
        link = f"[{tech['name']}](#{slug})"

        # Extract TOC field values
        toc_vals = []
        for field in TOC_FIELDS:
            val = find_field(data, field)
            if val and not should_skip_field(field, val, uncertain):
                text = str(val)
                if len(text) > 80:
                    text = text[:77] + "..."
                toc_vals.append(text)
            else:
                toc_vals.append("—")

        lines.append(f"| {tech_num} | {link} | {' | '.join(toc_vals)} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Detailed profiles
    lines.append("## Detailed Techniques")
    lines.append("")

    current_cat = None
    for item_name, item_cat, tech in ordered_techniques:
        if item_cat != current_cat:
            current_cat = item_cat
            lines.append(f"## {current_cat}")
            lines.append("")

        data = tech["data"]
        uncertain = get_uncertain_fields(data)

        lines.append(f"### {tech['name']}")
        lines.append("")

        # Output fields by category
        for cat_name, field_names in field_categories:
            cat_has_content = False
            cat_lines = []
            cat_lines.append(f"**{cat_name}**")
            cat_lines.append("")

            for field in field_names:
                value = find_field(data, field)
                if should_skip_field(field, value, uncertain):
                    continue
                cat_has_content = True
                formatted = format_value(value)
                display_name = field.replace("_", " ").title()

                if "\n" in formatted:
                    cat_lines.append(f"- **{display_name}**:")
                    cat_lines.append(formatted)
                else:
                    cat_lines.append(f"- **{display_name}**: {formatted}")

            cat_lines.append("")

            if cat_has_content:
                lines.extend(cat_lines)

        # Extra fields not in fields.yaml
        extra_fields = []
        all_keys = set()

        def collect_keys(d, prefix=""):
            if isinstance(d, dict):
                for k, v in d.items():
                    if isinstance(v, dict):
                        collect_keys(v, f"{prefix}{k}.")
                    else:
                        all_keys.add(k)

        collect_keys(data)
        # Filter out category top-level keys and internal fields
        category_top_keys = set()
        for cat in fields_yaml.get("field_categories", []):
            cat_name_lower = cat.get("name", "").lower().replace(" ", "_").replace("&", "and")
            category_top_keys.add(cat_name_lower)
        # Common nested structure top-level keys
        category_top_keys.update({
            "identity", "technical_description", "business_value",
            "implementation", "effectiveness", "security",
            "teaching_relevance",
        })

        for key in sorted(all_keys):
            if key not in all_defined_fields and key not in SKIP_FIELDS and key not in category_top_keys:
                value = find_field(data, key)
                if value and not is_uncertain_value(value):
                    extra_fields.append((key, value))

        if extra_fields:
            lines.append("**Other Info**")
            lines.append("")
            for key, value in extra_fields:
                display = key.replace("_", " ").title()
                formatted = format_value(value)
                if "\n" in formatted:
                    lines.append(f"- **{display}**:")
                    lines.append(formatted)
                else:
                    lines.append(f"- **{display}**: {formatted}")
            lines.append("")

        # Uncertain fields list
        if uncertain:
            lines.append("**Uncertain Fields**")
            lines.append("")
            for uf in sorted(uncertain):
                lines.append(f"- {uf}")
            lines.append("")

        lines.append("---")
        lines.append("")

    # Write report
    report = "\n".join(lines)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Report generated: {OUTPUT_PATH}")
    print(f"  Techniques: {len(ordered_techniques)}")
    print(f"  Lines: {len(lines)}")
    print(f"  Size: {len(report):,} bytes")


if __name__ == "__main__":
    main()
