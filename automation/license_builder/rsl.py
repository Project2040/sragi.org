"""SRAGI's narrow RSL 1.0 standard-license projection, not a general RSL validator.

Based on https://rslstandard.org/rsl sections 1.2, 2.2, 3 and 4.4 and
https://rslstandard.org/guide/standard-licenses (checked 2026-09-16).
Only explicitly evidenced CC licenses are currently projected. Other license
classes require a reviewed mapping; there is no fallback license.
"""
import hashlib
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET

RSL = 'https://rslstandard.org/rsl'
SRAGI = 'https://sragi.org/ns/licensing'
NS = {'r': RSL, 's': SRAGI}
STANDARDS = {
    'CC-BY-4.0': 'https://creativecommons.org/licenses/by/4.0/',
    'CC-BY-SA-4.0': 'https://creativecommons.org/licenses/by-sa/4.0/',
}
DUAL = 'CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial'


def standard_for(expression):
    # The open path is represented in RSL Core. Two RSL licenses would combine
    # obligations, not express SPDX OR. The complete expression stays metadata.
    identifier = 'CC-BY-SA-4.0' if expression == DUAL else expression
    if identifier not in STANDARDS:
        raise ValueError(f'No reviewed RSL mapping for {expression!r}')
    return STANDARDS[identifier]


def select_records(root, manifest):
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
        standard_for(expression)
        if expression == DUAL and record.get('commercial_relicensing_verified') is not True:
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
    for record in records:
        content = ET.SubElement(root, f'{{{RSL}}}content', {'url': record['rsl_path']})
        license_node = ET.SubElement(content, f'{{{RSL}}}license')
        payment = ET.SubElement(license_node, f'{{{RSL}}}payment', {'type': 'attribution'})
        ET.SubElement(payment, f'{{{RSL}}}standard').text = standard_for(record['license_expression'])
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


def validate_projection(text, records):
    """Reject deviations from our reviewed subset, including valid-but-broader RSL.

    This is a project conformance check, not official RSL certification.
    Core license meaning must stand on its own if extensions are ignored.
    """
    root = ET.fromstring(text)
    if root.tag != f'{{{RSL}}}rsl' or root.attrib:
        raise ValueError('Expected RSL 1.0 root/namespace; SRLF version is not an RSL version')
    structure = {'rsl': ({'content'}, set()), 'content': ({'license'}, {'url'}),
                 'license': ({'payment'}, set()), 'payment': ({'standard'}, {'type'}),
                 'standard': (set(), set())}
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
    if not expected or len(contents) != len(expected) or {c.get('url') for c in contents} != set(expected):
        raise ValueError('RSL content scope differs from verified manifest')
    for content in contents:
        record = expected[content.get('url')]
        licenses = content.findall('r:license', NS)
        if len(licenses) != 1 or len(licenses[0]) != 1:
            raise ValueError('RSL projection must preserve a single open path')
        payment = licenses[0].find('r:payment', NS)
        if payment is None or payment.attrib != {'type': 'attribution'} or len(payment) != 1:
            raise ValueError('Expected the reviewed RSL attribution standard form')
        standard = payment.find('r:standard', NS)
        if standard is None or standard.text != standard_for(record['license_expression']):
            raise ValueError('RSL standard license differs from source artifact')
        if content.findtext('s:license-expression', namespaces=NS) != record['license_expression']:
            raise ValueError('RSL metadata lost the artifact license expression')
    metadata = root.find('s:framework', NS)
    if metadata is None or metadata.get('legal-license-grant') != 'false' or metadata.findtext('s:rights-authority', namespaces=NS) != 'artifact':
        raise ValueError('RSL extension must preserve artifact authority')
