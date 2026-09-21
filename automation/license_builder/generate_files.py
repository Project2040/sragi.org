#!/usr/bin/env python3
"""Deterministic SRLF representations. Render first; the builder owns file I/O."""
import html
import json
from pathlib import Path
from string import Template
from xml.etree import ElementTree as ET
import yaml
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
        ('Commercial licensing', [commercial['license_name'], commercial['grant_rule'], commercial['sharealike_exception']['rule'], commercial['sharealike_exception']['limits'], commercial['profiles']['principle'], 'Commercial reference: ' + commercial['identifier']]),
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
    sections.insert(2, ('Available license classes (not grants)', ['These are available choices. The applicable license is selected for each artifact.']))
    sections.insert(5, ('Instruction metadata', ['These fields describe eligible dual-licensed instructions. The information URLs and metadata do not themselves grant commercial rights.']))
    sections.append(('Canonical information', ['Source: SRL-LICENSE.yaml. The website policy and artifact-specific terms define their respective scopes.']))
    return sections


def link(label, url):
    return {'label': label, 'url': url}


def markdown_value(value):
    if isinstance(value, dict):
        # Angle-delimited destinations preserve URI punctuation, including mailto:.
        return f"[{markdown_value(value['label'])}](<{value['url']}>)"
    text = html.escape(compact(value), quote=False)
    for char in ('\\', '|', '[', ']', '*', '_', '`'):
        text = text.replace(char, '\\' + char)
    return text


def html_value(value):
    if isinstance(value, dict):
        return f'<a href="{html.escape(value["url"], quote=True)}">{html_value(value["label"])}</a>'
    return html.escape(compact(value))


def human_tables(data):
    classes = []
    for name, record in data['license_classes'].items():
        choices = record.get('possible_licenses') or [record.get('preferred_expression') or record.get('identifier') or 'future artifact-specific selection']
        classes.append([name.replace('_', ' '), ', '.join(choices), record['description']])
    front = data['machine_readable']['instruction_frontmatter']
    metadata = [
        ['license.spdx', front['license']['spdx'], 'Alternative license paths for the artifact.'],
        ['license.commercial_license', front['license']['commercial_license'], 'Name of the commercial license.'],
        ['license.licensing_url', link(front['license']['licensing_url'], front['license']['licensing_url']), 'General licensing overview.'],
        ['license_url', link(front['license_url'], front['license_url']), 'Terms of the open license path.'],
        ['commercial_licensing.available', str(front['commercial_licensing']['available']).lower(), 'Availability of a commercial path; not a rights grant.'],
        ['commercial_licensing.url', link(front['commercial_licensing']['url'], front['commercial_licensing']['url']), 'Commercial licensing information.'],
        ['commercial_licensing.basis', front['commercial_licensing']['basis'], 'Basis required for commercial rights.'],
    ]
    for field_name, email in [('contact', front['contact']), ('licensing_contact', front['licensing_contact']), ('commercial_licensing.contact', front['commercial_licensing']['contact'])]:
        metadata.append([field_name, link(email, 'mailto:' + email), 'Contact for this role.'])
    contacts = [[role.capitalize(), link(spec['email'], 'mailto:' + spec['email']), spec['purpose']]
                for role, spec in data['publication']['contact_roles'].items()]
    return {
        'Available license classes (not grants)': (['Class', 'Available licenses / expression', 'Description'], classes),
        'Instruction metadata': (['Field', 'Configured value', 'Meaning'], metadata),
        'Canonical information': (['Contact role', 'Email', 'Purpose'], contacts),
    }


def human_links(data):
    publication = data['publication']
    email = publication['contact_roles']['commercial']['email']
    return {
        'Commercial licensing': [link('Commercial licensing information', publication['commercial_licensing_portal']), link(email, 'mailto:' + email)],
        'Canonical information': [link('Licensing overview', publication['canonical_licensing_portal']), link('Commercial licensing', publication['commercial_licensing_portal'])],
    }


def render(data, rsl_records):
    """Return repository-relative output paths and UTF-8 text, without side effects."""
    meta = data['meta']
    rights = data['rights']
    machine = data['machine_access']
    attribution = data['attribution']['preferred_machine_attribution']
    publication = data['publication']
    formats = publication['generated_formats']
    portal = publication['canonical_licensing_portal']
    roles = publication['contact_roles']
    contact = roles['licensing']['email']
    commercial_portal = publication['commercial_licensing_portal']
    commercial_contact = roles['commercial']['email']
    website = data['organization']['website'].rstrip('/')
    manifest = meta['repository'].rstrip('/') + '/blob/main/content/license/RESOURCE_LICENSE_MANIFEST.yaml'
    outputs = {}

    def put(kind, text):
        outputs[formats[kind]['path']] = text.rstrip() + '\n'

    put('json', json.dumps(data, indent=2, ensure_ascii=False, default=str))
    put('config_pointer', '# Generated from SRL-LICENSE.yaml; edit the master and rebuild.\n' + yaml.safe_dump({
        'meta': {'status': 'compatibility_pointer', 'framework': meta['id'],
                 'framework_version': meta['version'], 'updated': str(meta['last_updated'])},
        'source': {'authority': 'framework_architecture', 'path': '/SRL-LICENSE.yaml', 'canonical_url': portal},
        'rights': {'authority': rights['authority'], 'rule_ref': '/SRL-LICENSE.yaml#/rights',
                   'website_policy_ref': '/SRL-LICENSE.yaml#/website_licensing'},
        'note': 'This compatibility pointer does not grant rights and is not a second licensing master. The root SRL-LICENSE.yaml defines the framework; artifact terms remain authoritative.',
    }, sort_keys=False, allow_unicode=True))
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
        field(root, 'general-contact', roles['general']['email'])
        field(root, 'licensing-contact', contact)
        field(root, 'commercial-license-name', data['commercial']['license_name'])
        field(root, 'commercial-licensing', commercial_portal)
        field(root, 'commercial-contact', commercial_contact)
        field(root, 'commercial-agreement-basis', data['commercial']['agreement_basis'])
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
        'Licensing: ' + portal, 'General-Contact: ' + roles['general']['email'],
        'Licensing-Contact: ' + contact,
        'Commercial-License-Name: ' + data['commercial']['license_name'],
        'Commercial-Licensing: ' + commercial_portal,
        'Commercial-Contact: ' + commercial_contact,
        'Commercial-Agreement-Basis: ' + data['commercial']['agreement_basis'],
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
        'portal': portal,
        'commercial_portal': commercial_portal,
        'commercial_contact': commercial_contact,
    }
    put('website_policy', text_template(data, 'website_policy', {
        key: html.escape(compact(value), quote=True) for key, value in values.items()
    }))

    commercial = data['commercial']
    put('commercial_reference', text_template(data, 'commercial_reference', {
        'license_name': commercial['license_name'],
        'identifier': commercial['identifier'],
        'rights_holder': data['organization']['rights_holder'],
        'portal': portal,
        'commercial_portal': commercial_portal,
        'contact': contact,
        'commercial_contact': commercial_contact,
        'website': data['organization']['website'],
        'repository': meta['repository'],
        'expression': data['dual_licensing']['canonical_instruction_expression'],
        'sharealike_rule': compact(commercial['sharealike_exception']['rule']),
        'sharealike_limits': compact(commercial['sharealike_exception']['limits']),
        'grant_rule': compact(commercial['grant_rule']),
        'agreement_basis': commercial['agreement_basis'],
        'profiles': compact(commercial['profiles']['principle']),
    }))

    title = f"{meta['name']} v{meta['version']}"
    sections = human_sections(data)
    tables = human_tables(data)
    links = human_links(data)
    markdown = ['# ' + title, '', '<!-- Generated from SRL-LICENSE.yaml; edit the source, then rebuild. -->', '']
    for heading, paragraphs in sections:
        markdown.extend(['## ' + heading, ''])
        for paragraph in paragraphs:
            markdown.extend([compact(paragraph), ''])
        if heading in tables:
            columns, rows = tables[heading]
            markdown.append('| ' + ' | '.join(columns) + ' |')
            markdown.append('| ' + ' | '.join(['---'] * len(columns)) + ' |')
            markdown.extend('| ' + ' | '.join(markdown_value(cell) for cell in row) + ' |' for row in rows)
            markdown.append('')
        for value in links.get(heading, []):
            markdown.extend([markdown_value(value), ''])
    put('markdown', '\n'.join(markdown))
    esc = html.escape
    html_lines = ['<!doctype html>', '<html lang="en">', '<head>', '<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1">', f'<title>{esc(title)}</title>', f'<link rel="canonical" href="{esc(portal, quote=True)}">', '</head>', '<body><main>', f'<h1>{esc(title)}</h1>']
    for heading, paragraphs in sections:
        html_lines.append(f'<section><h2>{esc(heading)}</h2>')
        html_lines.extend(f'<p>{esc(compact(p))}</p>' for p in paragraphs)
        if heading in tables:
            columns, rows = tables[heading]
            html_lines.append('<table><thead><tr>' + ''.join(f'<th scope="col">{esc(col)}</th>' for col in columns) + '</tr></thead><tbody>')
            html_lines.extend('<tr>' + ''.join(f'<td>{html_value(cell)}</td>' for cell in row) + '</tr>' for row in rows)
            html_lines.append('</tbody></table>')
        html_lines.extend(f'<p>{html_value(value)}</p>' for value in links.get(heading, []))
        html_lines.append('</section>')
    html_lines.extend(['</main></body>', '</html>'])
    put('html', '\n'.join(html_lines))
    root = ET.Element('urlset', {'xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9'})
    for url in publication['sitemap_urls']:
        field(ET.SubElement(root, 'url'), 'loc', url)
    put('sitemap', xml_text(root))
    return outputs
