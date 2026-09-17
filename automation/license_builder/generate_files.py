#!/usr/bin/env python3
"""Deterministic SRLF representations. Render first; the builder owns file I/O."""
import html
import json
from pathlib import Path
from string import Template
from xml.etree import ElementTree as ET
from rsl import render_rsl


def compact(value):
    return ' '.join(str(value).split())


def xml_text(root):
    ET.indent(root, space='  ')
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding='unicode') + '\n'


def field(parent, name, value, **attributes):
    node = ET.SubElement(parent, name, attributes)
    node.text = compact(value)
    return node


def text_template(data, name, values):
    root = Path(__file__).resolve().parents[2]
    path = (root / data['publication']['templates'][name]).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Output template must stay in the repository')
    return Template(path.read_text(encoding='utf-8')).substitute(values)


def website_grant(data):
    site = data['website_licensing']
    return (
        f"Unless otherwise indicated, public content on sragi.org that Neptunia "
        f"Media AS owns or is authorized to license is made available under "
        f"{site['default_spdx']} at {site['default_license_url']}."
    )


def human_sections(data):
    """Both human formats carry the same substantive source statements."""
    commercial = data['commercial']
    sections = [
        ('Rights authority', [data['rights']['principle'], data['rights']['unspecified_artifact_policy'], data['rights']['non_override_rule']]),
        ('Website default license', [website_grant(data), data['website_licensing']['exceptions'], data['website_licensing']['machine_use'], data['website_licensing']['scope_rule']]),
        ('Licensing paths', [data['licensing']['rule'], data['dual_licensing']['interpretation']]),
        ('Commercial licensing', [commercial['grant_rule'], commercial['sharealike_exception']['rule'], commercial['profiles']['principle'], 'Commercial reference: ' + commercial['identifier']]),
        ('Machine access', [data['machine_access']['access_policy'], data['machine_access']['rights_rule']]),
        ('Really Simple Licensing (RSL)', [data['machine_readable']['rsl']['rule'], data['machine_readable']['rsl']['url']]),
        ('AI training', [data['machine_access']['ai_training']['rule'], data['machine_access']['interpretation']['ai_training_and_adaptation']]),
        ('Attribution', [data['attribution']['rule'], data['attribution']['preferred_machine_attribution']['value'], data['attribution']['preferred_machine_attribution']['note']]),
        ('Regenerative invitation', [data['regenerative']['open_license_layer']['principle'], data['regenerative']['open_license_layer']['invitation'], data['regenerative']['commercial_covenant']['rule']]),
        ('Contributor rights', [data['contributions']['principle'], data['contributions']['sufficient_rights_definition'], data['contributions']['commercial_relicensing']['rule'], data['contributions']['fallback'], data['contributions']['contributor_rights']['principle']]),
        ('Third-party rights', [data['third_party']['rule']]),
        ('Trademark and certification', [data['trademark']['principle'], 'Commercial brand licensing is separate from copyright licensing and requires an express agreement.']),
        ('Evolution', [data['evolution']['rule']]),
    ]
    classes = []
    for name, record in data['license_classes'].items():
        choices = record.get('possible_licenses') or [record.get('preferred_expression') or record.get('identifier') or 'future artifact-specific selection']
        classes.append(f"{name}: {', '.join(choices)}. {compact(record['description'])}")
    sections.insert(2, ('Available license classes (not grants)', classes))
    sections.append(('Canonical information', [data['publication']['canonical_licensing_portal'], data['organization']['licensing_email'], 'Source: SRL-LICENSE.yaml. The website policy and artifact-specific terms define their respective scopes.']))
    return sections


def render(data, rsl_records):
    """Return repository-relative output paths and UTF-8 text, without side effects."""
    meta = data['meta']
    rights = data['rights']
    machine = data['machine_access']
    attribution = data['attribution']['preferred_machine_attribution']
    publication = data['publication']
    formats = publication['generated_formats']
    portal = publication['canonical_licensing_portal']
    contact = data['organization']['licensing_email']
    website = data['organization']['website'].rstrip('/')
    manifest = meta['repository'].rstrip('/') + '/blob/main/content/license/RESOURCE_LICENSE_MANIFEST.yaml'
    outputs = {}

    def put(kind, text):
        outputs[formats[kind]['path']] = text.rstrip() + '\n'

    put('json', json.dumps(data, indent=2, ensure_ascii=False, default=str))
    put('xml', xml_text(render_rsl(data, rsl_records)))
    for kind, tag in [('ai_policy_xml', 'sragi-ai-policy')]:
        root = ET.Element(tag, {'version': str(meta['version']), 'function': 'rights-discovery', 'legal-license-grant': 'false'})
        field(root, 'framework', meta['name'])
        field(root, 'canonical', portal)
        field(root, 'rights-authority', rights['authority'])
        field(root, 'rights-rule', rights['principle'])
        field(root, 'ecosystem-default-license', 'none')
        site = ET.SubElement(root, 'website-license-policy')
        field(site, 'default-spdx', data['website_licensing']['default_spdx'])
        field(site, 'policy-url', data['website_licensing']['policy_url'])
        field(site, 'scope', data['website_licensing']['default_scope'])
        field(site, 'exceptions', data['website_licensing']['exceptions'])
        field(site, 'machine-use', data['website_licensing']['machine_use'])
        field(root, 'unspecified-artifact-policy', rights['unspecified_artifact_policy'])
        access = ET.SubElement(root, 'machine-access', {'posture': machine['posture'], 'legal-license-grant': 'false'})
        field(access, 'agents', machine['agents']['default'])
        for name in machine['agents']['named']:
            field(access, 'named-agent', name)
        field(access, 'scope', 'publicly accessible resources')
        for activity in ('crawling', 'indexing', 'retrieval', 'search_discovery'):
            field(access, activity.replace('_', '-'), 'allow-by-default')
        field(access, 'rights-rule', machine['rights_rule'])
        field(root, 'ai-training-rights', machine['ai_training']['rule'], policy=machine['ai_training']['policy'])
        field(root, 'ai-training-and-adaptation', machine['interpretation']['ai_training_and_adaptation'])
        field(root, 'preferred-machine-attribution', attribution['value'], binding='false')
        field(root, 'attribution-note', attribution['note'])
        field(root, 'artifact-manifest', manifest)
        field(root, 'commercial-grant-rule', data['commercial']['grant_rule'])
        field(root, 'commercial-sharealike-exception', data['commercial']['sharealike_exception']['rule'])
        field(root, 'third-party-rights', data['third_party']['rule'])
        field(root, 'rsl-license-document', data['machine_readable']['rsl']['url'])
        field(root, 'licensing-contact', contact)
        put(kind, xml_text(root))

    lines = [
        f"# {meta['name']} {meta['version']} — AI & machine rights discovery",
        'Function: rights-discovery', 'Legal-License-Grant: false',
        'Access-Posture: ' + machine['posture'], 'Access-Scope: publicly accessible resources',
        'Machine-Agents: ' + machine['agents']['default'],
        'Named-Machine-Agents: ' + ', '.join(machine['agents']['named']),
        'Named-Agent-List-Exhaustive: false',
        'Discovery: allowed-by-default', 'Crawling: allowed-by-default',
        'Indexing: allowed-by-default', 'Retrieval: allowed-by-default',
        'Rights-Authority: ' + rights['authority'], 'Ecosystem-Default-License: none',
        'Website-Default-License: ' + data['website_licensing']['default_spdx'],
        'Website-License-Policy: ' + data['website_licensing']['policy_url'],
        'Website-License-Scope: ' + data['website_licensing']['default_scope'],
        'Website-License-Exceptions: ' + compact(data['website_licensing']['exceptions']),
        'Website-Machine-Use: ' + compact(data['website_licensing']['machine_use']),
        'Rights-Rule: ' + compact(rights['principle']),
        'Access-Rights-Rule: ' + compact(machine['rights_rule']),
        'Unspecified-Artifact-Policy: ' + compact(rights['unspecified_artifact_policy']),
        'AI-Training-Policy: ' + machine['ai_training']['policy'],
        'AI-Training-Rights: ' + compact(machine['ai_training']['rule']),
        'AI-Training-And-Adaptation: ' + compact(machine['interpretation']['ai_training_and_adaptation']),
        'Preferred-Machine-Attribution: ' + attribution['value'],
        'Preferred-Machine-Attribution-Binding: false',
        'Attribution-Note: ' + compact(attribution['note']),
        'Commercial-Grant-Rule: ' + compact(data['commercial']['grant_rule']),
        'Commercial-Primary-Function: ' + data['commercial']['primary_function'],
        'Commercial-ShareAlike-Exception: ' + compact(data['commercial']['sharealike_exception']['rule']),
        'Third-Party-Rights: ' + compact(data['third_party']['rule']),
        'Artifact-Manifest: ' + manifest, 'RSL-License-Document: ' + data['machine_readable']['rsl']['url'],
        'Licensing: ' + portal, 'Licensing-Contact: ' + contact,
    ]
    put('ai_policy_txt', '\n'.join(lines))

    put('robots', text_template(data, 'robots', {
        'rsl_url': data['machine_readable']['rsl']['url'],
        'user_agent': machine['agents']['default'],
        'sitemap_url': website + '/sitemap.xml',
    }))

    site = data['website_licensing']
    values = {
        'title': site['title'],
        'policy_url': site['policy_url'],
        'grant': website_grant(data),
        'license_url': site['default_license_url'],
        'license_identifier': site['default_spdx'],
        'exceptions': site['exceptions'],
        'machine_use': site['machine_use'],
        'ai_interpretation': machine['interpretation']['ai_training_and_adaptation'],
        'scope_rule': site['scope_rule'],
        'attribution': data['attribution']['minimal'],
        'framework_version': str(meta['version']),
        'effective_date': str(meta['last_updated']),
        'contact': contact,
    }
    put('website_policy', text_template(data, 'website_policy', {
        key: html.escape(compact(value), quote=True) for key, value in values.items()
    }))

    title = f"{meta['name']} v{meta['version']}"
    sections = human_sections(data)
    markdown = ['# ' + title, '', '<!-- Generated from SRL-LICENSE.yaml; edit the source, then rebuild. -->', '']
    for heading, paragraphs in sections:
        markdown.extend(['## ' + heading, ''])
        for paragraph in paragraphs:
            markdown.extend([compact(paragraph), ''])
    put('markdown', '\n'.join(markdown))
    esc = html.escape
    html_lines = ['<!doctype html>', '<html lang="en">', '<head>', '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">', f'<title>{esc(title)}</title>', f'<link rel="canonical" href="{esc(portal, quote=True)}">', '</head>', '<body><main>', f'<h1>{esc(title)}</h1>']
    for heading, paragraphs in sections:
        html_lines.append(f'<section><h2>{esc(heading)}</h2>')
        html_lines.extend(f'<p>{esc(compact(p))}</p>' for p in paragraphs)
        html_lines.append('</section>')
    html_lines.extend(['</main></body>', '</html>'])
    put('html', '\n'.join(html_lines))
    root = ET.Element('urlset', {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})
    for url in publication['sitemap_urls']:
        field(ET.SubElement(root, 'url'), 'loc', url)
    put('sitemap', xml_text(root))
    return outputs
