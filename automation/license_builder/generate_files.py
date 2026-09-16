#!/usr/bin/env python3
"""Deterministic SRLF representations. Render first; the builder owns file I/O."""
import html
import json
from xml.etree import ElementTree as ET


def compact(value):
    return ' '.join(str(value).split())


def xml_text(root):
    ET.indent(root, space='  ')
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding='unicode') + '\n'


def field(parent, name, value, **attributes):
    node = ET.SubElement(parent, name, attributes)
    node.text = compact(value)
    return node


def human_sections(data):
    """Both human formats carry the same substantive source statements."""
    sections = [
        ('Rights authority', [data['rights']['principle'], data['rights']['unspecified_artifact_policy'], data['rights']['non_override_rule']]),
        ('Licensing paths', [data['licensing']['rule'], data['dual_licensing']['interpretation']]),
        ('Commercial licensing', [data['commercial']['grant_rule'], 'Commercial reference: ' + data['commercial']['identifier']]),
        ('Machine access', [data['machine_access']['access_policy'], data['machine_access']['rights_rule']]),
        ('AI training', [data['machine_access']['ai_training']['rule'], data['machine_access']['interpretation']['ai_training_and_adaptation']]),
        ('Attribution', [data['attribution']['rule'], data['attribution']['preferred_machine_attribution']['value'], data['attribution']['preferred_machine_attribution']['note']]),
        ('Regenerative invitation', [data['regenerative']['open_license_layer']['principle'], data['regenerative']['open_license_layer']['invitation'], data['regenerative']['commercial_covenant']['rule']]),
        ('Contributor rights', [data['contributions']['principle'], data['contributions']['commercial_relicensing']['rule'], data['contributions']['fallback'], data['contributions']['contributor_rights']['principle']]),
        ('Third-party rights', [data['third_party']['rule']]),
        ('Trademark and certification', [data['trademark']['principle']]),
        ('Evolution', [data['evolution']['rule']]),
    ]
    classes = []
    for name, record in data['license_classes'].items():
        choices = record.get('possible_licenses') or [record.get('preferred_expression') or record.get('identifier') or 'future artifact-specific selection']
        classes.append(f"{name}: {', '.join(choices)}. {compact(record['description'])}")
    sections.insert(2, ('Available license classes (not grants)', classes))
    sections.append(('Canonical information', [data['publication']['canonical_licensing_portal'], data['organization']['licensing_email'], 'Source: SRL-LICENSE.yaml. This generated representation does not independently license any artifact.']))
    return sections


def render(data):
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
    for kind, tag in [('xml', 'sragi-rights-discovery'), ('ai_policy_xml', 'sragi-ai-policy')]:
        root = ET.Element(tag, {'version': str(meta['version']), 'function': 'rights-discovery', 'legal-license-grant': 'false'})
        field(root, 'framework', meta['name'])
        field(root, 'canonical', portal)
        field(root, 'rights-authority', rights['authority'])
        field(root, 'rights-rule', rights['principle'])
        field(root, 'ecosystem-default-license', 'none')
        field(root, 'unspecified-artifact-policy', rights['unspecified_artifact_policy'])
        access = ET.SubElement(root, 'machine-access', {'posture': machine['posture'], 'legal-license-grant': 'false'})
        field(access, 'agents', machine['agents']['default'])
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
        field(root, 'third-party-rights', data['third_party']['rule'])
        if kind == 'xml':
            example = ET.SubElement(root, 'instruction-license-example', {'scope': 'only-where-attached-to-an-artifact', 'legal-license-grant': 'false'})
            field(example, 'expression', data['dual_licensing']['canonical_instruction_expression'])
            field(example, 'interpretation', data['dual_licensing']['interpretation'])
        field(root, 'licensing-contact', contact)
        put(kind, xml_text(root))

    lines = [
        f"# {meta['name']} {meta['version']} — AI & machine rights discovery",
        'Function: rights-discovery', 'Legal-License-Grant: false',
        'Access-Posture: ' + machine['posture'], 'Access-Scope: publicly accessible resources',
        'Machine-Agents: ' + machine['agents']['default'],
        'Discovery: allowed-by-default', 'Crawling: allowed-by-default',
        'Indexing: allowed-by-default', 'Retrieval: allowed-by-default',
        'Rights-Authority: ' + rights['authority'], 'Ecosystem-Default-License: none',
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
        'Third-Party-Rights: ' + compact(data['third_party']['rule']),
        'Artifact-Manifest: ' + manifest, 'Licensing: ' + portal, 'Licensing-Contact: ' + contact,
    ]
    put('ai_policy_txt', '\n'.join(lines))
    put('robots', f"# Technical crawler access to public resources\nUser-agent: {machine['agents']['default']}\nDisallow:\n\nSitemap: {website}/sitemap.xml\n")
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
