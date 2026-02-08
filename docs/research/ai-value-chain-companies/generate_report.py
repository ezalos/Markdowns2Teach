# ABOUTME: Generates a markdown report from AI Value Chain Companies research JSON files.
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

# TOC summary fields selected by user
TOC_FIELDS = [
    "headquarters_region",
    "role_in_value_chain",
    "revenue_or_valuation",
    "open_vs_closed_spectrum",
]

# Category mapping: fields.yaml category -> possible JSON keys
CATEGORY_MAPPING = {
    "identity": ["identity", "Identity"],
    "value_chain": ["value_chain", "Value Chain", "value_chain_position"],
    "products": ["products", "Products"],
    "business": ["business", "Business"],
    "openness": ["openness", "Openness"],
    "startup_relevance": ["startup_relevance", "Startup Relevance"],
    "ecosystem": ["ecosystem", "Ecosystem"],
    "regulatory": ["regulatory", "Regulatory"],
}

# Internal fields to skip
INTERNAL_FIELDS = {"_source_file", "uncertain"}


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def slugify(name):
    """Convert company name to anchor-friendly slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def get_field_value(data, field_name):
    """Look up a field in nested JSON structure."""
    # Direct top-level lookup
    if field_name in data:
        return data[field_name]
    # Search in nested categories
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


def truncate_for_toc(value, max_len=80):
    """Truncate a value for TOC display."""
    if value is None:
        return "—"
    s = str(value)
    if isinstance(value, list):
        s = ", ".join(str(v) for v in value)
    # Take first sentence or truncate
    if len(s) > max_len:
        # Try to cut at a period or comma
        cut = s[:max_len].rfind(".")
        if cut > 30:
            s = s[: cut + 1]
        else:
            cut = s[:max_len].rfind(",")
            if cut > 30:
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
        # List of dicts
        if isinstance(value[0], dict):
            lines = []
            for item in value:
                parts = [f"**{k}**: {v}" for k, v in item.items() if v]
                lines.append(f"{prefix}- " + " | ".join(parts))
            return "\n".join(lines)
        # List of strings
        if all(isinstance(v, str) and len(v) < 80 for v in value):
            return ", ".join(str(v) for v in value)
        # Long list items
        lines = []
        for item in value:
            s = str(item)
            if len(s) > 120:
                lines.append(f"{prefix}- {s}")
            else:
                lines.append(f"{prefix}- {s}")
        return "\n".join(lines)

    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            lines.append(f"{prefix}- **{k}**: {v}")
        return "\n".join(lines)

    s = str(value)
    # Long text: use blockquote for readability
    if len(s) > 300:
        return s
    return s


def get_fields_for_category(fields_yaml, category_name):
    """Get the field definitions for a category from fields.yaml."""
    cat_data = fields_yaml.get(category_name, {})
    if isinstance(cat_data, dict):
        return {k: v for k, v in cat_data.items()
                if isinstance(v, dict) and "description" in v}
    return {}


def get_json_category_data(data, category_name):
    """Get category data from JSON, trying multiple key variants."""
    variants = CATEGORY_MAPPING.get(category_name, [category_name])
    for variant in variants:
        if variant in data and isinstance(data[variant], dict):
            return data[variant]
    return {}


def build_item_order(outline):
    """Build ordered list of items grouped by layer from outline.yaml."""
    items = outline.get("items", [])
    layers = []
    layer_items = {}
    layer_names = {
        "energy_infrastructure": "Layer 0 — Energy & Power Infrastructure",
        "hardware": "Layer 1 — Semiconductor / Hardware",
        "cloud": "Layer 2 — Cloud Infrastructure / Compute",
        "data_infrastructure": "Layer 2.5 — Data Infrastructure & Labeling",
        "model_creator": "Layer 3 — Foundation Model Creators",
        "model_hub": "Layer 4 — Model Hubs & Communities",
        "api_provider": "Layer 5a — API Providers / Routers",
        "orchestration": "Layer 5b — Orchestration",
        "vector_db": "Layer 5c — Vector Databases",
        "evaluation": "Layer 6a — Evaluation & Benchmarking",
        "safety": "Layer 6b — AI Safety",
        "mlops": "Layer 6c — MLOps",
        "application": "Layer 7 — AI-Native Applications",
    }
    for item in items:
        layer = item.get("layer", "other")
        if layer not in layer_items:
            layers.append(layer)
            layer_items[layer] = []
        layer_items[layer].append(item)

    return layers, layer_items, layer_names


def find_json_for_item(item_name, json_files):
    """Find the matching JSON file(s) for an outline item."""
    slug = re.sub(r"[^a-zA-Z0-9]", "_", item_name)
    slug = re.sub(r"_+", "_", slug).strip("_")
    matches = []
    for jf in json_files:
        basename = os.path.splitext(os.path.basename(jf))[0]
        # Exact match
        if basename == slug:
            matches.append(jf)
        # Partial match (e.g., xAI_Colossus and xAI_Grok both match "xAI")
        elif slug.lower().replace("_", "") in basename.lower().replace("_", ""):
            matches.append(jf)
        elif basename.lower().replace("_", "") in slug.lower().replace("_", ""):
            matches.append(jf)
    return matches


def generate_report():
    fields_yaml = load_yaml(FIELDS_PATH)
    outline = load_yaml(OUTLINE_PATH)
    topic = outline.get("topic", "Research Report")

    # Get all JSON files
    json_files = sorted(
        [os.path.join(RESULTS_DIR, f) for f in os.listdir(RESULTS_DIR)
         if f.endswith(".json")]
    )

    # Load all JSON data keyed by filename
    all_data = {}
    for jf in json_files:
        basename = os.path.splitext(os.path.basename(jf))[0]
        all_data[basename] = load_json(jf)

    layers, layer_items, layer_names = build_item_order(outline)

    # Get field categories (excluding 'uncertain' which is a reserved key)
    categories = [k for k in fields_yaml.keys() if k != "uncertain"]

    lines = []

    # Header
    lines.append(f"# {topic}\n")
    lines.append(f"> Generated from {len(all_data)} company research files.\n")
    lines.append("---\n")

    # Table of Contents grouped by layer
    lines.append("## Table of Contents\n")
    item_num = 0
    for layer in layers:
        layer_label = layer_names.get(layer, layer)
        lines.append(f"\n### {layer_label}\n")
        lines.append("| # | Company | Region | Role | Revenue / Valuation | Openness |")
        lines.append("|---|---------|--------|------|---------------------|----------|")

        for item in layer_items[layer]:
            item_num += 1
            name = item["name"]
            slug = slugify(name)
            matches = find_json_for_item(name, json_files)

            if matches:
                data = load_json(matches[0])
                region = get_field_value(data, "headquarters_region") or "—"
                role = get_field_value(data, "role_in_value_chain") or "—"
                rev = truncate_for_toc(
                    get_field_value(data, "revenue_or_valuation"), 60
                )
                openness = truncate_for_toc(
                    get_field_value(data, "open_vs_closed_spectrum"), 50
                )
            else:
                region = role = rev = openness = "—"

            lines.append(
                f"| {item_num} | [{name}](#{slug}) | {region} | {role} | {rev} | {openness} |"
            )

    lines.append("\n---\n")

    # Detailed sections per company
    lines.append("## Company Profiles\n")

    item_num = 0
    for layer in layers:
        layer_label = layer_names.get(layer, layer)
        lines.append(f"\n---\n\n## {layer_label}\n")

        for item in layer_items[layer]:
            item_num += 1
            name = item["name"]
            slug = slugify(name)
            matches = find_json_for_item(name, json_files)

            if not matches:
                lines.append(f"\n### {item_num}. {name}\n")
                lines.append("*No research data found.*\n")
                continue

            # If multiple JSON files match (e.g., xAI has Colossus + Grok),
            # merge them
            merged_data = {}
            for m in matches:
                data = load_json(m)
                for cat_key in data:
                    if cat_key == "uncertain":
                        existing = merged_data.get("uncertain", [])
                        merged_data["uncertain"] = list(
                            set(existing + data.get("uncertain", []))
                        )
                    elif cat_key not in merged_data:
                        merged_data[cat_key] = data[cat_key]
                    elif isinstance(data[cat_key], dict):
                        if not isinstance(merged_data[cat_key], dict):
                            merged_data[cat_key] = data[cat_key]
                        else:
                            # Merge dict fields, preferring longer values
                            for fk, fv in data[cat_key].items():
                                existing_val = merged_data[cat_key].get(fk)
                                if existing_val is None or (
                                    isinstance(fv, str) and isinstance(existing_val, str)
                                    and len(fv) > len(existing_val)
                                ):
                                    merged_data[cat_key][fk] = fv

            data = merged_data
            source_files = [os.path.basename(m) for m in matches]

            lines.append(f"\n### {item_num}. {name}\n")
            lines.append(
                f"*Source: {', '.join(source_files)}*\n"
            )

            # Iterate through each field category
            for category in categories:
                cat_fields = get_fields_for_category(fields_yaml, category)
                cat_data = get_json_category_data(data, category)

                if not cat_fields and not cat_data:
                    continue

                cat_label = category.replace("_", " ").title()
                lines.append(f"\n#### {cat_label}\n")

                # Use fields from fields.yaml as the canonical list
                for field_name, field_def in cat_fields.items():
                    value = cat_data.get(field_name)
                    if value is None:
                        value = get_field_value(data, field_name)

                    if is_uncertain(data, field_name, value):
                        continue

                    desc = field_def.get("description", "")
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
            for category in categories:
                known_fields.update(get_fields_for_category(fields_yaml, category).keys())
            known_categories = set(categories) | set(INTERNAL_FIELDS)
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
    print(f"Companies: {len(all_data)}")
    print(f"Layers: {len(layers)}")


if __name__ == "__main__":
    generate_report()
