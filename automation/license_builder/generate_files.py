# ===========================================================
#  SRAGI LICENSE GENERATORS — v2.2 (content/license/)
#  © 2025 Rune Solberg / Neptunia Media AS
#  Generates all SRAGI license artifacts from SRL-LICENSE.yaml
#  All files go to: content/license/
# ===========================================================

import os
from jinja2 import Template
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")
LICENSE_DIR = os.path.join(BASE_DIR, "content", "license")  # ✅ All files here

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
# 1. LICENSE-RSL.xml (using inline template from YAML)
# -----------------------------------------------------------
def generate_rsl_xml(data):
    """Generate machine-readable RSL XML license from YAML inline template."""
    # Use the inline template from machine_format.template
    template_str = data.get("machine_format", {}).get("template", "")
    
    if not template_str:
        raise ValueError("No machine_format.template found in YAML file!")
    
    # Render the inline template with Jinja2
    template = Template(template_str)
    content = template.render(**data)
    
    return write_output(os.path.join(LICENSE_DIR, "LICENSE-RSL.xml"), content)

# -----------------------------------------------------------
# 2. REGENERATIVE_LICENSE.md — Human-readable version
# -----------------------------------------------------------
def generate_human_license(data):
    """Generate human-readable Markdown license."""
    # Try to use template first, fallback to inline generation
    try:
        content = render_template("regenerative_license.md.j2", data)
        return write_output(os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"), content)
    except FileNotFoundError:
        # Fallback: generate inline
        meta = data.get("meta", {})
        org = data.get("organization", {})
        ethics = data.get("ethics", {}).get("framework", {})
        reqs = data.get("requirements", {})
        perms = data.get("permissions", {}).get("usage", [])
        attrib = data.get("attribution", {})
        
        perms_str = ", ".join(perms) if perms else "No permissions defined"
        
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
        
        return write_output(os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"), content)

# -----------------------------------------------------------
# 3. ai-policy.xml
# -----------------------------------------------------------
def generate_ai_policy_xml(data):
    """Generate machine-readable AI policy XML."""
    content = render_template("ai_policy.xml.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.xml"), content)

# -----------------------------------------------------------
# 4. ai-policy.txt
# -----------------------------------------------------------
def generate_ai_policy_txt(data):
    """Generate human-readable AI policy text file."""
    content = render_template("ai_policy.txt.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.txt"), content)

# -----------------------------------------------------------
# 5. robots.txt
# -----------------------------------------------------------
def generate_robots(data):
    """Generate robots.txt with license and AI policy directives."""
    content = render_template("robots.txt.j2", data)
    return write_output(os.path.join(LICENSE_DIR, "robots.txt"), content)

# -----------------------------------------------------------
# 6. sitemap.xml (dynamic from YAML linked_files)
# -----------------------------------------------------------
def generate_sitemap(data):
    """ Generate XML sitemap for license and documentation pages."""
    meta = data.get("meta", {})
    linked = data.get("linked_files", {})
    base_url = meta.get("source_url", "https://sragi.org")
    last_updated = meta.get("last_updated", datetime.utcnow().strftime('%Y-%m-%d'))
    
    # Start XML
    urls = ["<?xml version='1.0' encoding='UTF-8'?>",
            "<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"]
    
    # Add main license page
    urls.append(f"  <url><loc>{base_url}/license</loc><lastmod>{last_updated}</lastmod></url>")
    
    # Add linked files from YAML
    for format_type, path in linked.items():
        if not path.startswith('http'):  # Skip external URLs
            full_url = f"{base_url}/{path}"
            urls.append(f"  <url><loc>{full_url}</loc><lastmod>{last_updated}</lastmod></url>")
    
    # Add generated files explicitly (in case not in linked_files)
    for generated in ['LICENSE-RSL.xml', 'REGENERATIVE_LICENSE.md', 
                      'ai-policy.xml', 'ai-policy.txt', 'robots.txt']:
        full_url = f"{base_url}/content/license/{generated}"
        # Only add if not already added from linked_files
        url_entry = f"  <url><loc>{full_url}</loc><lastmod>{last_updated}</lastmod></url>"
        if url_entry not in urls:
            urls.append(url_entry)
    
    urls.append("</urlset>")
    
    content = "\n".join(urls)
    return write_output(os.path.join(LICENSE_DIR, "sitemap.xml"), content)
