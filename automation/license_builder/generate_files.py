# ===========================================================
#  SRAGI LICENSE GENERATORS — v2.0
#  © 2025 Rune Solberg / Neptunia Media AS
#  Generates all SRAGI license artifacts from SRL-LICENSE.yaml
# ===========================================================

import os
from jinja2 import Template
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")

def write_output(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated {os.path.relpath(path, BASE_DIR)}")
    return {"file": path, "status": "ok"}

def render_template(filename, data):
    with open(os.path.join(TPL_DIR, filename), "r", encoding="utf-8") as f:
        tpl = Template(f.read())
        return tpl.render(**data)

# -----------------------------------------------------------
# 1. LICENSE-RSL.xml
# -----------------------------------------------------------
def generate_rsl_xml(data):
    content = render_template("license_rsl.xml.j2", data)
    return write_output(os.path.join(BASE_DIR, "LICENSE-RSL.xml"), content)

# -----------------------------------------------------------
# 2. REGENERATIVE_LICENSE.md — Human-readable version
# -----------------------------------------------------------
def generate_human_license(data):
    meta = data.get("meta", {})
    org = data.get("organization", {})
    ethics = data.get("ethics", {}).get("framework", {})
    perms = ", ".join(data.get("permissions", {}).get("usage", []))
    attrib = data.get("attribution", {}).get("standard", "").strip()
    today = datetime.utcnow().strftime("%Y-%m-%d")

    content = f"""# 🌱 SRAGI Regenerative License (SRL) v{meta.get('version', '1.0')}

Based on **{meta.get('base_license', 'CC-BY-4.0')}**

**Maintainer:** {org.get('author', 'Rune Solberg')} / {org.get('organization', 'SRAGI.org')}  
**Last updated:** {meta.get('last_updated', today)}

---

## ✅ Permissions
{perms or 'No permissions defined.'}

## ⚠️ Requirements
Attribution required: {data.get('requirements', {}).get('attribution', True)}  
Share-alike required: {data.get('requirements', {}).get('share-alike', False)}

---

## 🌿 Ethics
{ethics.get('encouragement', 'We invite alignment with regenerative principles.')}  
See: {ethics.get('url', 'https://sragi.org/regenerative-principles')}

---

## 🧾 Attribution Format
"""

