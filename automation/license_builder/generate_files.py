# ===========================================================
#  SRAGI LICENSE GENERATORS — v3.0 (Kairos Edition)
#  © 2025 Rune Solberg / Neptunia Media AS
#  Generates all SRAGI license artifacts from SRL-LICENSE.yaml
#  All files go to: content/license/
# ===========================================================

import os
import json
from jinja2 import Template
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")
LICENSE_DIR = os.path.join(BASE_DIR, "content", "license")

def write_output(path, content):
    """Write content to file and create directories if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated {os.path.relpath(path, BASE_DIR)}")
    return {"file": path, "status": "ok"}

def render_template(filename, data):
    """Render a Jinja2 template with data."""
    template_path = os.path.join(TPL_DIR, filename)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"CRITICAL: Template not found: {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
        return tpl.render(**data)

# -----------------------------------------------------------
# 1. LICENSE-RSL.xml (using inline template from YAML SSOT)
# -----------------------------------------------------------
def generate_rsl_xml(data):
    template_str = data.get("machine_format", {}).get("template", "")
    if not template_str:
        raise ValueError("SSOT Error: No machine_format.template found in YAML!")

    template = Template(template_str)
    content = template.render(**data)
    return write_output(os.path.join(LICENSE_DIR, "LICENSE-RSL.xml"), content)

# -----------------------------------------------------------
# 2. REGENERATIVE_LICENSE.md (Human-readable)
# -----------------------------------------------------------
def generate_human_license(data):
    content = render_template("regenerative_license.md.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"), content)

# -----------------------------------------------------------
# 3. license.html (Web-ready version) -- NEW!
# -----------------------------------------------------------
def generate_license_html(data):
    content = render_template("license.html.j2", data)
    # Saves as index.html in a subfolder for clean URL /content/license/
    return write_output(os.path.join(LICENSE_DIR, "index.html"), content)

# -----------------------------------------------------------
# 4. AI Policy Files (TXT & XML)
# -----------------------------------------------------------
def generate_ai_policy_xml(data):
    content = render_template("ai_policy.xml.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.xml"), content)

def generate_ai_policy_txt(data):
    content = render_template("ai_policy.txt.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.txt"), content)

# -----------------------------------------------------------
# 5. robots.txt
# -----------------------------------------------------------
def generate_robots(data):
    content = render_template("robots.txt.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "robots.txt"), content)

# -----------------------------------------------------------
# 6. license.json (Full API Response)
# -----------------------------------------------------------
def generate_license_json(data):
    meta = data.get("meta", {})
    linked = data.get("linked_files", {}).copy()
    linked.pop("source_map", None) # Remove internal build data

    # SIKKERHETSFIKS: Tving 'last_updated' til string for å unngå JSON-krasj
    updated_date = str(meta.get("last_updated", ""))

    json_data = {
        "meta": {
            "id": meta.get("id"),
            "version": meta.get("version"),
            "updated": updated_date,  # <-- Nå trygg for JSON
            "strategy": meta.get("license_strategy", {}),
            "source": meta.get("source_url")
        },
        "organization": data.get("organization", {}),
        "permissions": data.get("permissions", {}),
        "requirements": data.get("requirements", {}),
        "ethics": data.get("ethics", {}),
        "links": linked
    }

    return write_output(os.path.join(LICENSE_DIR, "license.json"),
                       json.dumps(json_data, indent=2, ensure_ascii=False))

# -----------------------------------------------------------
# 7. sitemap.xml
# -----------------------------------------------------------
def generate_sitemap(data):
    # Uses the specialized Jinja2 template for full control
    content = render_template("sitemap.xml.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "sitemap.xml"), content)
