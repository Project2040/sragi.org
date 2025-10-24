# ===========================================================
#  SRAGI LICENSE GENERATORS — v2.1 (Fixed)
#  © 2025 Rune Solberg / Neptunia Media AS
#  Generates all SRAGI license artifacts from SRL-LICENSE.yaml
# ===========================================================

import os
from jinja2 import Template
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")

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
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    with open(template_path, "r", encoding="utf-8") as f:
        tpl = Template(f.read())
        return tpl.render(**data)

# -----------------------------------------------------------
# 1. LICENSE-RSL.xml
# -----------------------------------------------------------
def generate_rsl_xml(data):
    """Generate machine-readable RSL XML license."""
    content = render_template("license_rsl.xml.j2", data)
    return write_output(os.path.join(BASE_DIR, "LICENSE-RSL.xml"), content)

# -----------------------------------------------------------
# 2. REGENERATIVE_LICENSE.md — Human-readable version
# -----------------------------------------------------------
def generate_human_license(data):
    """Generate human-readable Markdown license."""
    meta = data.get("meta", {})
    org = data.get("organization", {})
    ethics = data.get("ethics", {}).get("framework", {})
    reqs = data.get("requirements", {})
    perms = data.get("permissions", {}).get("usage", [])
    attrib = data.get("attribution", {})
    
    # Format permissions as comma-separated string
    perms_str = ", ".join(perms) if perms else "No permissions defined"
    
    # Build the content
    content = f"""# 🌱 SRAGI Regenerative License (SRL) v{meta.get('version', '1.0')}

Based on **{meta.get('base_license', 'CC-BY-4.0')}**

**Maintainer:** {org.get('author', 'Rune Solberg')} / {org.get('organization', 'SRAGI.org')}  
**Last updated:** {meta.get('last_updated', datetime.utcnow().strftime('%Y-%m-%d'))}

---

## ✅ Permissions
{perms_str}

## ⚠️ Requirements
Attribution required: {reqs.get('attribution', True)}  
Share-alike required: {reqs.get('share-alike', False)}

---

## 🌿 Ethics
{ethics.get('encouragement', 'We invite alignment with regenerative principles.')}

See: {ethics.get('url', 'https://sragi.org/regenerative-principles')}

---

## 🧾 Attribution Format

{attrib.get('standard', attrib.get('minimal', 'SRAGI by Rune Solberg / Neptunia Media AS'))}

---

**© {org.get('author', 'Rune Solberg')} / {org.get('rights_holder', 'Neptunia Media AS')} — {meta.get('last_updated', datetime.utcnow().strftime('%Y-%m-%d'))}**

**Source:** {meta.get('source_url', 'https://sragi.org/license')}  
**Repository:** {meta.get('repository', 'https://github.com/Project2040/sragi.org')}
"""
    
    output_path = os.path.join(BASE_DIR, "content", "license", "REGENERATIVE_LICENSE.md")
    return write_output(output_path, content)

# -----------------------------------------------------------
# 3. ai-policy.xml
# -----------------------------------------------------------
def generate_ai_policy_xml(data):
    """Generate machine-readable AI policy XML."""
    content = render_template("ai_policy.xml.j2", data)
    return write_output(os.path.join(BASE_DIR, "ai-policy.xml"), content)

# -----------------------------------------------------------
# 4. ai-policy.txt
# -----------------------------------------------------------
def generate_ai_policy_txt(data):
    """Generate human-readable AI policy text file."""
    content = render_template("ai_policy.txt.j2", data)
    return write_output(os.path.join(BASE_DIR, "ai-policy.txt"), content)

# -----------------------------------------------------------
# 5. robots.txt
# -----------------------------------------------------------
def generate_robots(data):
    """Generate robots.txt with license and AI policy directives."""
    content = render_template("robots.txt.j2", data)
    return write_output(os.path.join(BASE_DIR, "robots.txt"), content)

# -----------------------------------------------------------
# 6. sitemap.xml
# -----------------------------------------------------------
def generate_sitemap(data):
    """Generate XML sitemap for license and documentation pages."""
    meta = data.get("meta", {})
    last_updated = meta.get("last_updated", datetime.utcnow().strftime('%Y-%m-%d'))
    
    content = f"""<?xml version='1.0' encoding='UTF-8'?>
<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
  <url><loc>https://sragi.org/license</loc><lastmod>{last_updated}</lastmod></url>
  <url><loc>https://sragi.org/ai-policy.xml</loc><lastmod>{last_updated}</lastmod></url>
  <url><loc>https://sragi.org/ai-policy.txt</loc><lastmod>{last_updated}</lastmod></url>
  <url><loc>https://sragi.org/content/license/REGENERATIVE_LICENSE.md</loc><lastmod>{last_updated}</lastmod></url>
</urlset>"""
    
    return write_output(os.path.join(BASE_DIR, "sitemap.xml"), content)
