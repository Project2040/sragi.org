# ===========================================================
#  SRAGI LICENSE GENERATORS — helper module
# ===========================================================

import os
from jinja2 import Template
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
TPL_DIR = os.path.join(os.path.dirname(__file__), "templates")

def write_output(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"✅ Generated {path}")
    return {"file": path, "status": "ok"}

def render_template(filename, data):
    with open(os.path.join(TPL_DIR, filename), "r", encoding="utf-8") as f:
        tpl = Template(f.read())
        return tpl.render(**data)

# 1. LICENSE-RSL.xml
def generate_rsl_xml(data):
    content = render_template("license_rsl.xml.j2", data)
    return write_output(os.path.join(BASE_DIR, "LICENSE-RSL.xml"), content)

# 2. REGENERATIVE_LICENSE.md
def generate_human_license(data):
    content = render_template("regenerative_license.md.j2", data)
    return write_output(os.path.join(BASE_DIR, "content/license/REGENERATIVE_LICENSE.md"), content)

# 3. AI policy XML
def generate_ai_policy_xml(data):
    content = render_template("ai_policy.xml.j2", data)
    return write_output(os.path.join(BASE_DIR, "ai-policy.xml"), content)

# 4. AI policy TXT
def generate_ai_policy_txt(data):
    content = render_template("ai_policy.txt.j2", data)
    return write_output(os.path.join(BASE_DIR, "ai-policy.txt"), content)

# 5. robots.txt
def generate_robots(data):
    content = render_template("robots.txt.j2", data)
    return write_output(os.path.join(BASE_DIR, "robots.txt"), content)

# 6. sitemap.xml
def generate_sitemap(data):
    urls = [
        "https://sragi.org/license",
        "https://sragi.org/ai-policy.xml",
        "https://sragi.org/ai-policy.txt",
        "https://sragi.org/content/license/REGENERATIVE_LICENSE.md"
    ]
    sitemap = "<?xml version='1.0' encoding='UTF-8'?>\n<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>\n"
    for url in urls:
        sitemap += f"  <url><loc>{url}</loc><lastmod>{datetime.utcnow().date()}</lastmod></url>\n"
    sitemap += "</urlset>"
    return write_output(os.path.join(BASE_DIR, "sitemap.xml"), sitemap)
