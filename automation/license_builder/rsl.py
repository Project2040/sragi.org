"""SRAGI's narrow RSL 1.0 standard-license projection, not a general RSL validator.

Based on https://rslstandard.org/rsl sections 1.2, 2.2, 3 and 4.4 and
https://rslstandard.org/guide/standard-licenses (checked 2026-09-16).
The website fallback points to its scoped policy, including exceptions.
Explicit artifact standards and expression mappings are configured in the master.
"""
import hashlib
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET

RSL = 'https://rslstandard.org/rsl'
SRAGI = 'https://sragi.org/ns/licensing'
NS = {'r': RSL, 's': SRAGI}
def standard_for(data, expression):
    config = data['machine_readable']['rsl']
    mapping = config['expression_mappings'].get(expression, {})
    identifier = mapping.get('open_license', expression)
    if identifier not in config['standard_licenses']:
        raise ValueError(f'No reviewed RSL mapping for {expression!r}')
    return config['standard_licenses'][identifier]


def select_records(root, manifest, data):
    if manifest.get('authority') != 'artifact' or manifest.get('meta', {}).get('legal_license_grant') is not False:
        raise ValueError('RSL manifest must preserve artifact authority')
    records, scopes = [], set()
    for record in manifest['artifacts']:
        if 'rsl_path' not in record:
            continue
        if record.get('status') != 'explicit_license_verified':
            raise ValueError('Unresolved artifact cannot be exported to RSL')
        path = Path(record['path'])
        if path.is_absolute() or '..' in path.parts or not (root / path).resolve().is_relative_to(root.resolve()):
            raise ValueError('RSL evidence path must stay in the repository')
        # This initial profile maps static repository files only. Publishing a
        # WordPress route requires a separately reviewed mapping, not a guess.
        scope = '/' + quote(path.as_posix(), safe='/') + '$'
        if record['rsl_path'] != scope or scope in scopes or '*' in scope:
            raise ValueError('RSL scope must uniquely match the exact source path')
        source = (root / path).read_bytes()
        if hashlib.sha256(source).hexdigest() != record.get('source_sha256'):
            raise ValueError(f'RSL license evidence changed: {path}')
        expression = record['license_expression']
        notices = {'**License:** ' + expression, '**Lisens:** ' + expression,
                   'SPDX-License-Identifier: ' + expression}
        if not notices.intersection(line.strip() for line in source.decode('utf-8').splitlines()):
            raise ValueError(f'RSL expression lacks an explicit source notice: {path}')
        standard_for(data, expression)
        mapping = data['machine_readable']['rsl']['expression_mappings'].get(expression, {})
        if mapping.get('requires_commercial_provenance') and record.get('commercial_relicensing_verified') is not True:
            raise ValueError('Dual-license RSL metadata requires verified commercial rights')
        records.append(record)
        scopes.add(scope)
    if not records:
        raise ValueError('RSL requires at least one explicitly licensed artifact')
    return sorted(records, key=lambda item: item['rsl_path'])


def render_rsl(data, records):
    ET.register_namespace('', RSL)
    ET.register_namespace('sragi', SRAGI)
    root = ET.Element(f'{{{RSL}}}rsl')
    site = data['website_licensing']
    default = ET.SubElement(root, f'{{{RSL}}}content', {'url': site['rsl_path']})
    license_node = ET.SubElement(default, f'{{{RSL}}}license')
    payment_type = standard_for(data, site['default_spdx'])['payment_type']
    payment = ET.SubElement(license_node, f'{{{RSL}}}payment', {'type': payment_type})
    # This URI identifies the conditional website policy, not an unconditional
    # CC grant to every resource beneath '/'. Core readers see its full terms.
    ET.SubElement(payment, f'{{{RSL}}}standard').text = site['policy_url']
    ET.SubElement(default, f'{{{RSL}}}terms').text = site['policy_url']
    ET.SubElement(default, f'{{{SRAGI}}}default-spdx').text = site['default_spdx']
    ET.SubElement(default, f'{{{SRAGI}}}scope').text = site['default_scope']
    ET.SubElement(default, f'{{{SRAGI}}}exceptions').text = ' '.join(site['exceptions'].split())
    for record in records:
        content = ET.SubElement(root, f'{{{RSL}}}content', {'url': record['rsl_path']})
        license_node = ET.SubElement(content, f'{{{RSL}}}license')
        standard = standard_for(data, record['license_expression'])
        payment = ET.SubElement(license_node, f'{{{RSL}}}payment', {'type': standard['payment_type']})
        ET.SubElement(payment, f'{{{RSL}}}standard').text = standard['url']
        ET.SubElement(content, f'{{{SRAGI}}}license-expression').text = record['license_expression']
        ET.SubElement(content, f'{{{SRAGI}}}source-sha256').text = record['source_sha256']
    metadata = ET.SubElement(root, f'{{{SRAGI}}}framework', {'version': str(data['meta']['version']), 'legal-license-grant': 'false'})
    values = {
        'rights-authority': data['rights']['authority'],
        'rights-rule': data['rights']['principle'],
        'unspecified-artifact-policy': data['rights']['unspecified_artifact_policy'],
        'ai-training-and-adaptation': data['machine_access']['interpretation']['ai_training_and_adaptation'],
        'commercial-grant-rule': data['commercial']['grant_rule'],
    }
    for name, value in values.items():
        ET.SubElement(metadata, f'{{{SRAGI}}}{name}').text = ' '.join(value.split())
    return root


def validate_projection(text, records, data):
    """Reject deviations from our reviewed subset, including valid-but-broader RSL.

    This is a project conformance check, not official RSL certification.
    Core license meaning must stand on its own if extensions are ignored.
    """
    root = ET.fromstring(text)
    if root.tag != f'{{{RSL}}}rsl' or root.attrib:
        raise ValueError('Expected RSL 1.0 root/namespace; SRLF version is not an RSL version')
    structure = {'rsl': ({'content'}, set()), 'content': ({'license', 'terms'}, {'url'}),
                 'license': ({'payment'}, set()), 'payment': ({'standard'}, {'type'}),
                 'standard': (set(), set()), 'terms': (set(), set())}
    def visit(node):
        if node.tag.startswith(f'{{{SRAGI}}}'):
            return
        if not node.tag.startswith(f'{{{RSL}}}'):
            raise ValueError('Unexpected namespace in RSL projection')
        name = node.tag.split('}', 1)[1]
        if name not in structure:
            raise ValueError(f'Unsupported RSL element: {name}')
        children, attributes = structure[name]
        if set(node.attrib) != attributes:
            raise ValueError(f'Unexpected attributes on RSL {name}')
        for child in node:
            if child.tag.startswith(f'{{{RSL}}}') and child.tag.split('}', 1)[1] not in children:
                raise ValueError(f'Invalid RSL child under {name}')
            visit(child)
    visit(root)
    contents = root.findall('r:content', NS)
    expected = {r['rsl_path']: r for r in records}
    site = data['website_licensing']
    if site['rsl_path'] in expected:
        raise ValueError('Artifact record collides with website fallback')
    expected[site['rsl_path']] = None
    if not expected or len(contents) != len(expected) or {c.get('url') for c in contents} != set(expected):
        raise ValueError('RSL content scope differs from verified manifest')
    for content in contents:
        record = expected[content.get('url')]
        licenses = content.findall('r:license', NS)
        if len(licenses) != 1 or len(licenses[0]) != 1:
            raise ValueError('RSL projection must preserve a single open path')
        payment = licenses[0].find('r:payment', NS)
        spec = standard_for(data, record['license_expression']) if record else {
            'url': site['policy_url'],
            'payment_type': standard_for(data, site['default_spdx'])['payment_type'],
        }
        if payment is None or payment.attrib != {'type': spec['payment_type']} or len(payment) != 1:
            raise ValueError('Expected the reviewed RSL attribution standard form')
        standard = payment.find('r:standard', NS)
        if standard is None or standard.text != spec['url']:
            raise ValueError('RSL standard license differs from source artifact')
        if record is None:
            if content.findtext('r:terms', namespaces=NS) != site['policy_url']:
                raise ValueError('Website fallback lost its exception-bearing terms')
            continue
        if content.findtext('s:license-expression', namespaces=NS) != record['license_expression']:
            raise ValueError('RSL metadata lost the artifact license expression')
    metadata = root.find('s:framework', NS)
    if metadata is None or metadata.get('legal-license-grant') != 'false' or metadata.findtext('s:rights-authority', namespaces=NS) != 'artifact':
        raise ValueError('RSL extension must preserve artifact authority')
