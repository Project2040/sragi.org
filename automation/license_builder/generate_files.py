# ===========================================================
#  SRAGI LICENSE GENERATORS — v3.1 (Hybrid-Kairos Edition)
#  © 2025 Rune Solberg / Neptunia Media AS
#  Generates all SRAGI license artifacts from SRL-LICENSE.yaml
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
# 1. LICENSE-RSL.xml
# -----------------------------------------------------------
def generate_rsl_xml(data):
    template_str = data.get("machine_format", {}).get("template", "")
    if not template_str:
        raise ValueError("SSOT Error: No machine_format.template found in YAML!")
    template = Template(template_str)
    return write_output(os.path.join(LICENSE_DIR, "LICENSE-RSL.xml"), template.render(**data))

# -----------------------------------------------------------
# 2. REGENERATIVE_LICENSE.md
# -----------------------------------------------------------
def generate_human_license(data):
    return write_output(os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"), render_template("regenerative_license.md.j2", data))

# -----------------------------------------------------------
# 3. license.html
# -----------------------------------------------------------
def generate_license_html(data):
    return write_output(os.path.join(LICENSE_DIR, "index.html"), render_template("license.html.j2", data))

# -----------------------------------------------------------
# 4. AI Policy Files (TXT in ROOT, XML in folder)
# -----------------------------------------------------------
def generate_ai_policy_xml(data):
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.xml"), render_template("ai_policy.xml.j2", data))

def generate_ai_policy_txt(data):
    # ✅ ENDRING: Lagres nå i roten (BASE_DIR)
    return write_output(os.path.join(BASE_DIR, "ai-policy.txt"), render_template("ai_policy.txt.j2", data))

# -----------------------------------------------------------
# 5. robots.txt (in ROOT)
# -----------------------------------------------------------
def generate_robots(data):
    # ✅ ENDRING: Lagres nå i roten (BASE_DIR)
    return write_output(os.path.join(BASE_DIR, "robots.txt"), render_template("robots.txt.j2", data))

# -----------------------------------------------------------
# 6. license.json
# -----------------------------------------------------------
def generate_license_json(data):
    meta = data.get("meta", {})
    linked = data.get("linked_files", {}).copy()
    linked.pop("source_map", None)
    updated_date = str(meta.get("last_updated", ""))

    json_data = {
        "meta": {
            "id": meta.get("id"),
            "version": meta.get("version"),
            "updated": updated_date,
            "strategy": meta.get("license_strategy", {}),
            "source": meta.get("source_url")
        },
        "organization": data.get("organization", {}),
        "permissions": data.get("permissions", {}),
        "requirements": data.get("requirements", {}),
        "ethics": data.get("ethics", {}),
        "links": linked
    }
    return write_output(os.path.join(LICENSE_DIR, "license.json"), json.dumps(json_data, indent=2, ensure_ascii=False))

# -----------------------------------------------------------
# 7. sitemap.xml (in ROOT)
# -----------------------------------------------------------
def generate_sitemap(data):
    # ✅ ENDRING: Lagres nå i roten (BASE_DIR)
    return write_output(os.path.join(BASE_DIR, "sitemap.xml"), render_template("sitemap.xml.j2", data))
