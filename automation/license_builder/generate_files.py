#!/usr/bin/env python3
"""Generate SRLF 2.0 rights-discovery artifacts from SRL-LICENSE.yaml."""

import json
import os
from xml.sax.saxutils import escape

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
LICENSE_DIR = os.path.join(BASE_DIR, "content", "license")


def write_output(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Generated {os.path.relpath(path, BASE_DIR)}")
    return {"file": path, "status": "ok"}


def _meta(data): return data.get("meta", {})
def _portal(data): return data.get("publication", {}).get("canonical_licensing_portal", _meta(data).get("canonical_url", "https://sragi.org/licensing/"))
def _contact(data): return data.get("organization", {}).get("licensing_email", "licensing@sragi.org")


def generate_rsl_xml(data):
    meta, rights, machine = _meta(data), data.get("rights", {}), data.get("machine_access", {})
    expression = data.get("dual_licensing", {}).get("canonical_instruction_expression", "")
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<sragi-rights-discovery version="{escape(str(meta.get('version', '2.0')))}">
  <framework>{escape(str(meta.get('name', 'SRAGI® Regenerative Licensing Framework')))}</framework>
  <canonical>{escape(_portal(data))}</canonical>
  <rights-authority>{escape(str(rights.get('authority', 'artifact')))}</rights-authority>
  <ecosystem-default-license>none</ecosystem-default-license>
  <unspecified-artifact-policy>No license grant should be inferred.</unspecified-artifact-policy>
  <machine-access posture="{escape(str(machine.get('posture', 'maximally_open')))}" legal-license-grant="false">
    <agents>*</agents><crawling>allow-by-default</crawling><indexing>allow-by-default</indexing><retrieval>allow-by-default</retrieval>
  </machine-access>
  <canonical-instruction-expression>{escape(expression)}</canonical-instruction-expression>
  <commercial-license-ref>LicenseRef-SRAGI-Commercial</commercial-license-ref>
  <licensing-contact>{escape(_contact(data))}</licensing-contact>
</sragi-rights-discovery>'''
    return write_output(os.path.join(LICENSE_DIR, "LICENSE-RSL.xml"), xml)


def generate_human_license(data):
    meta = _meta(data)
    text = f'''# {meta.get("name", "SRAGI® Regenerative Licensing Framework")} v{meta.get("version", "2.0")}

## Open by design. Licensed at artifact level.

SRAGI does not use one ecosystem-wide default license. The license identifier, SPDX expression, rights statement or applicable agreement attached to an artifact determines its rights.

> **No license grant should be inferred for an unspecified artifact.**

SRAGI instruction frameworks may use `CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial`. Commercial activity alone does not require the commercial path; it provides alternative terms where different or additional rights are required.

Public SRAGI resources are maximally open for technical discovery by search engines, AI systems, research crawlers and other machine agents. Technical access does not independently grant intellectual-property rights.

Rights relating to AI training are determined by the artifact license, rights statement, contract and applicable law. SRLF does not determine whether AI training or related activity constitutes Adapted Material.

**Give more than you take.** For open-license artifacts this is an invitation, not an additional restriction. A separate commercial agreement may expressly define regenerative commitments.

Canonical licensing portal: {_portal(data)}  
Licensing contact: {_contact(data)}
'''
    return write_output(os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"), text)


def generate_license_html(data):
    meta = _meta(data)
    html = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{meta.get('name', 'SRAGI Licensing')}</title></head><body><main>
<h1>{meta.get('name', 'SRAGI® Regenerative Licensing Framework')} v{meta.get('version', '2.0')}</h1>
<p>SRAGI is open by design and licensed at artifact level.</p><p><strong>No license grant should be inferred for an unspecified artifact.</strong></p>
<p>Canonical licensing portal: <a href="{_portal(data)}">{_portal(data)}</a></p></main></body></html>'''
    return write_output(os.path.join(LICENSE_DIR, "index.html"), html)


def generate_ai_policy_xml(data):
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<sragi-ai-policy version="2.0" function="rights-discovery" legal-license-grant="false">
  <access posture="maximally-open"><agents>*</agents><crawling>allow-by-default</crawling><indexing>allow-by-default</indexing><retrieval>allow-by-default</retrieval></access>
  <rights-authority>artifact</rights-authority><ecosystem-default-license>none</ecosystem-default-license>
  <unspecified-artifact-policy>No license grant should be inferred.</unspecified-artifact-policy>
  <ai-training-rights>artifact-license</ai-training-rights>
  <preferred-machine-attribution binding="false">SRAGI® — Neptunia Media AS — https://sragi.org/</preferred-machine-attribution>
  <licensing>{escape(_portal(data))}</licensing><licensing-contact>{escape(_contact(data))}</licensing-contact>
</sragi-ai-policy>'''
    return write_output(os.path.join(LICENSE_DIR, "ai-policy.xml"), xml)


def generate_ai_policy_txt(data):
    text = f'''# SRAGI® — AI & MACHINE RIGHTS DISCOVERY
# SRLF 2.0 | Function: rights discovery | Legal license grant: false
Access-Posture: maximally-open
Machine-Agents: *
Discovery: allowed-by-default
Crawling: allowed-by-default
Indexing: allowed-by-default
Retrieval: allowed-by-default
Rights-Authority: artifact
Ecosystem-Default-License: none
Unspecified-Artifact-Policy: No license grant should be inferred.
AI-Training-Rights: artifact-license
Preferred-Machine-Attribution: SRAGI® — Neptunia Media AS — https://sragi.org/
Preferred-Machine-Attribution-Binding: false
Licensing: {_portal(data)}
Licensing-Contact: {_contact(data)}'''
    return write_output(os.path.join(BASE_DIR, "ai-policy.txt"), text)


def generate_robots(data):
    text = f'''# SRAGI® — TECHNICAL ACCESS POLICY
# SRLF 2.0 | Posture: maximally open | Legal license grant: false
User-agent: *
Disallow:

Sitemap: https://sragi.org/sitemap.xml
# Rights discovery: https://sragi.org/ai-policy.txt
# Licensing: {_portal(data)}
# Licensing contact: {_contact(data)}'''
    return write_output(os.path.join(BASE_DIR, "robots.txt"), text)


def generate_license_json(data):
    payload = {key: data.get(key, {}) for key in (
        "meta", "rights", "licensing", "license_classes", "dual_licensing", "commercial",
        "machine_access", "attribution", "regenerative", "contributions", "trademark",
        "third_party", "organization", "publication", "evolution"
    )}
    return write_output(os.path.join(LICENSE_DIR, "license.json"), json.dumps(payload, indent=2, ensure_ascii=False, default=str))


def generate_sitemap(data):
    urls = [
        "https://sragi.org/", _portal(data), "https://sragi.org/ai-policy.txt",
        "https://sragi.org/robots.txt", "https://sragi.org/regenerative-principles/",
        "https://sragi.org/content/license/LICENSE-RSL.xml",
        "https://sragi.org/content/license/ai-policy.xml",
        "https://sragi.org/content/license/license.json",
        "https://sragi.org/content/license/REGENERATIVE_LICENSE.md",
    ]
    body = "\n".join(f"  <url><loc>{escape(url)}</loc></url>" for url in urls)
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}\n</urlset>'''
    return write_output(os.path.join(BASE_DIR, "sitemap.xml"), xml)
