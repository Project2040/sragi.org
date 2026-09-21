#!/usr/bin/env python3
"""Build SRLF outputs or check them without changing the checkout."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import re
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET
import yaml
from generate_files import render
from rsl import select_records, validate_projection
from policy import validate_content_templates

ROOT = Path(__file__).resolve().parents[2]
STANDARD_LICENSES = {'CC-BY-4.0', 'CC-BY-SA-4.0', 'AGPL-3.0-only', 'Apache-2.0', 'CC0-1.0'}
EXPECTED_OUTPUTS = {
    'content/license/LICENSE-RSL.xml', 'content/license/REGENERATIVE_LICENSE.md',
    'content/license/index.html', 'content/license/license.json',
    'content/license/ai-policy.xml', 'ai-policy.txt', 'robots.txt', 'sitemap.xml',
    'content/license/WEBSITE-LICENSE.html',
    'LICENSES/LicenseRef-SRAGI-Commercial.txt',
    'docs/_CONFIG/SRL-LICENSE.yaml',
}
PLACEHOLDER_RE = re.compile(r'\{\{[^{}]+\}\}')


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate keys instead of silently losing policy statements."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f'Duplicate YAML key: {key}')
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def load_yaml(path):
    raw = Path(path).read_text(encoding='utf-8')
    if raw.lstrip().startswith(chr(96) * 3) or raw.rstrip().endswith(chr(96) * 3):
        raise ValueError(f'{path} must be pure YAML, without Markdown fences')
    data = yaml.load(raw, Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise ValueError(f'{path} must contain a mapping')
    return data


def validate_v2(data):
    expected = {
        'rights.authority': 'artifact',
        'rights.ecosystem_default_license': None, 'rights.artifact_license_authoritative': True,
        'machine_access.posture': 'maximally_open', 'machine_access.agents.default': '*',
        'machine_access.robots.posture': 'allow_by_default',
        'machine_access.robots.function': 'technical_access',
        'machine_access.robots.legal_license_grant': False,
        'machine_access.ai_policy.function': 'rights_discovery',
        'machine_access.ai_policy.legal_license_grant': False,
        'machine_access.ai_training.policy': 'artifact_license',
        'attribution.preferred_machine_attribution.binding': False,
        'regenerative.open_license_layer.binding': False,
        'third_party.override_third_party_rights': False,
        'contributions.commercial_relicensing.requirement': 'sufficient_rights',
        'dual_licensing.commercial_grant_by_reference': False,
        'dual_licensing.canonical_instruction_expression': 'CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial',
        'commercial.primary_function': 'sharealike_exception_within_licensed_scope',
        'commercial.agreement_basis': 'separate_written_agreement',
        'machine_readable.instruction_frontmatter.commercial_licensing.available': True,
        'machine_readable.custom_license_references.LicenseRef-SRAGI-Commercial.url_role': 'commercial_licensing_information',
        'evolution.retroactive_relicensing': False,
        'machine_readable.rsl.enabled': True,
        'machine_readable.rsl.protocol_version': '1.0',
        'machine_readable.rsl.namespace': 'https://rslstandard.org/rsl',
        'machine_readable.rsl.media_type': 'application/rsl+xml',
        'machine_readable.rsl.scope': 'website_policy_with_artifact_overrides',
        'machine_readable.rsl.manifest': 'content/license/RESOURCE_LICENSE_MANIFEST.yaml',
        'publication.generated_formats.xml.standard': 'RSL',
        'publication.generated_formats.xml.protocol_version': '1.0',
        'publication.generated_formats.xml.media_type': 'application/rsl+xml',
        'website_licensing.explicit_artifact_terms_override': True,
        'website_licensing.third_party_rights_preserved': True,
        'machine_access.agents.list_is_exhaustive': False,
    }
    for activity in ('allow_by_default', 'allow_crawling', 'allow_indexing', 'allow_retrieval', 'allow_search_discovery'):
        expected['machine_access.discovery.' + activity] = True
    for kind in ('ai_policy_txt', 'ai_policy_xml', 'robots', 'commercial_reference', 'config_pointer'):
        expected[f'publication.generated_formats.{kind}.legal_license_grant'] = False
    errors = []
    version = data.get('meta', {}).get('version')
    if not isinstance(version, str) or not re.fullmatch(r'2\.0(?:\.(?:0|[1-9][0-9]*))?', version):
        errors.append('meta.version must be a released SRLF 2.0 maintenance version')
    for dotted, value in expected.items():
        actual = data
        for part in dotted.split('.'):
            actual = actual.get(part, object()) if isinstance(actual, dict) else object()
        if actual != value or type(actual) is not type(value):
            errors.append(f'{dotted} must be {value!r}')
    site = data['website_licensing']
    if site.get('precedence') != ['third_party_terms', 'artifact_terms', 'website_default']:
        errors.append('Website precedence must preserve third-party terms as the overriding boundary')
    config = data['machine_readable']['rsl']
    selected = config['standard_licenses'].get(site['default_spdx'], {})
    if selected.get('url') != site['default_license_url']:
        errors.append('Website default license must match the configured standard URL')
    for key, output in [('policy_url', 'website_policy'), ('rsl_url', 'xml')]:
        url = site['policy_url'] if key == 'policy_url' else config['url']
        parsed = urlsplit(url)
        if f'{parsed.scheme}://{parsed.netloc}' not in site['origins'] or parsed.path != '/' + data['publication']['generated_formats'][output]['path'] or parsed.query or parsed.fragment:
            errors.append('Policy/RSL URL must match its generated file on a configured website origin')
    if site['rsl_path'] != '/':
        errors.append('Website policy must cover the site; artifact exceptions live in its terms')
    names = data['machine_access']['agents']['named']
    if not isinstance(names, list) or len({n.casefold() for n in names}) != len(names) or any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9_-]*', n) for n in names):
        errors.append('Named agents must be unique product tokens without directives or whitespace')
    custom = data['machine_readable']['custom_license_references']
    if custom.get('LicenseRef-SRAGI-Commercial', {}).get('file') != 'LICENSES/LicenseRef-SRAGI-Commercial.txt':
        errors.append('The commercial LicenseRef must point to its local text')
    declared = set(data['machine_readable']['license_files']['expected'])
    required = {x + '.txt' for x in STANDARD_LICENSES} | {'LicenseRef-SRAGI-Commercial.txt'}
    if not required.issubset(declared):
        errors.append('All five standard texts and the commercial reference are required')
    for spec in data['publication']['generated_formats'].values():
        p = Path(spec['path'])
        if p.is_absolute() or '..' in p.parts:
            errors.append('Generated output paths must remain in the repository')
    serialized = json.dumps(data, ensure_ascii=False, default=str)
    if PLACEHOLDER_RE.search(serialized):
        errors.append('Master policy data must not contain unresolved presentation placeholders')
    validate_metadata_consistency(data, errors)
    if errors:
        raise ValueError('SRLF validation failed:\n- ' + '\n- '.join(errors))


def validate_metadata_consistency(data, errors):
    """Check duplicated public metadata against its configured source, not literals."""
    def value(path):
        result = data
        for part in path.split('.'):
            if not isinstance(result, dict) or part not in result:
                return None
            result = result[part]
        return result

    groups = [
        ('publication.canonical_licensing_portal', 'meta.canonical_url', 'machine_readable.instruction_frontmatter.license.licensing_url'),
        ('publication.commercial_licensing_portal', 'licensing.commercial_path.url', 'commercial.licensing_url', 'license_classes.commercial.licensing_url', 'machine_readable.instruction_frontmatter.commercial_licensing.url', 'machine_readable.custom_license_references.LicenseRef-SRAGI-Commercial.url'),
        ('commercial.license_name', 'license_classes.commercial.name', 'machine_readable.instruction_frontmatter.license.commercial_license', 'machine_readable.custom_license_references.LicenseRef-SRAGI-Commercial.name'),
        ('commercial.identifier', 'licensing.commercial_path.identifier', 'license_classes.commercial.identifier'),
        ('dual_licensing.canonical_instruction_expression', 'license_classes.open_frameworks.preferred_expression', 'machine_readable.instruction_frontmatter.license.spdx'),
        ('commercial.agreement_basis', 'machine_readable.instruction_frontmatter.commercial_licensing.basis', 'machine_readable.custom_license_references.LicenseRef-SRAGI-Commercial.grant_basis'),
        ('publication.contact_roles.general.email', 'organization.contact_email', 'machine_readable.instruction_frontmatter.contact'),
        ('publication.contact_roles.licensing.email', 'organization.licensing_email', 'machine_readable.instruction_frontmatter.licensing_contact', 'trademark.licensing_contact'),
        ('publication.contact_roles.commercial.email', 'organization.commercial_email', 'commercial.licensing_email', 'machine_readable.instruction_frontmatter.commercial_licensing.contact'),
        ('publication.generated_formats.commercial_reference.path', 'machine_readable.custom_license_references.LicenseRef-SRAGI-Commercial.file'),
    ]
    for source, *aliases in groups:
        expected = value(source)
        if not isinstance(expected, str) or not expected.strip():
            errors.append(f'Missing metadata source: {source}')
        for alias in aliases:
            if value(alias) != expected:
                errors.append(f'Metadata mismatch: {alias} must match {source}')
    front = data['machine_readable']['instruction_frontmatter']
    expression = data['dual_licensing']['canonical_instruction_expression']
    if data['machine_readable']['instruction_header']['license'] != 'SPDX-License-Identifier: ' + expression:
        errors.append('Instruction header must match the canonical instruction expression')
    config = data['machine_readable']['rsl']
    identifier = config['expression_mappings'][expression]['open_license']
    if front.get('license_url') != config['standard_licenses'][identifier]['url']:
        errors.append('Instruction license_url must identify the open path, not the commercial portal')
    for key in ('canonical_licensing_portal', 'commercial_licensing_portal'):
        url = data['publication'].get(key)
        parsed = urlsplit(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != 'https' or not parsed.netloc or any(c.isspace() or c in '<>"' for c in url):
            errors.append(f'Invalid publication URL: {key}')
    for role in ('general', 'licensing', 'commercial'):
        spec = data['publication'].get('contact_roles', {}).get(role, {})
        if not re.fullmatch(r"[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", str(spec.get('email', ''))):
            errors.append(f'Invalid contact email: {role}')
        if not isinstance(spec.get('purpose'), str) or not spec['purpose'].strip():
            errors.append(f'Missing contact purpose: {role}')


def verify_license_files(root, data):
    for name in data['machine_readable']['license_files']['expected']:
        if Path(name).name != name:
            raise ValueError('License text names must be plain filenames')
        p = root / 'LICENSES' / name
        if p.relative_to(root).as_posix() == data['publication']['generated_formats']['commercial_reference']['path']:
            # This is generated output. --check detects a missing/stale reference;
            # an ordinary build must be able to recreate it from the sources.
            continue
        if not p.is_file() or not p.stat().st_size:
            raise ValueError(f'Missing or empty license text: {name}')
    lock = json.loads((root / 'LICENSES/SPDX-SOURCES.json').read_text(encoding='utf-8'))
    if set(lock['licenses']) != STANDARD_LICENSES:
        raise ValueError('SPDX source lock must cover all five standard licenses')
    for identifier, item in lock['licenses'].items():
        actual = hashlib.sha256((root / 'LICENSES' / (identifier + '.txt')).read_bytes()).hexdigest()
        if actual != item['sha256']:
            raise ValueError(f'Canonical license text checksum mismatch: {identifier}')


def verify_output(outputs, data, rsl_records):
    if set(outputs) != EXPECTED_OUTPUTS:
        raise ValueError('Generated output set changed; update publication and validation together')
    for path, content in outputs.items():
        if PLACEHOLDER_RE.search(content):
            raise ValueError(f'Unresolved presentation placeholder in generated output: {path}')
        if path.endswith('.xml'):
            ET.fromstring(content)
        if path.endswith('.json'):
            json.loads(content)
        if path.endswith('.yaml'):
            yaml.load(content, Loader=UniqueKeyLoader)
    exported = json.loads(outputs['content/license/license.json'])
    if exported != json.loads(json.dumps(data, default=str)):
        raise ValueError('JSON representation differs from the master')
    pointer = yaml.load(outputs['docs/_CONFIG/SRL-LICENSE.yaml'], Loader=UniqueKeyLoader)
    if (pointer['meta']['framework_version'] != data['meta']['version']
            or pointer['source']['canonical_url'] != data['publication']['canonical_licensing_portal']):
        raise ValueError('Compatibility pointer differs from the master')
    validate_projection(outputs['content/license/LICENSE-RSL.xml'], rsl_records, data)
    for path in ('content/license/ai-policy.xml',):
        root = ET.fromstring(outputs[path])
        if root.get('legal-license-grant') != 'false' or root.findtext('rights-authority') != 'artifact':
            raise ValueError(f'Unexpected rights grant in {path}')
        if not root.findtext('ai-training-and-adaptation'):
            raise ValueError(f'Missing AI interpretation statement in {path}')
    robots = [line for line in outputs['robots.txt'].splitlines() if line and not line.startswith('#')]
    expected = [
        'License: ' + data['machine_readable']['rsl']['url'],
        'User-agent: ' + data['machine_access']['agents']['default'],
        'Disallow:',
        'Sitemap: ' + data['organization']['website'].rstrip('/') + '/sitemap.xml',
    ]
    if robots != expected:
        raise ValueError('robots.txt must use one wildcard group while preserving RSL discovery and open technical access')
    policy = outputs['content/license/WEBSITE-LICENSE.html']
    for required in ('rel="license"', str(data['meta']['version']), str(data['meta']['last_updated']), data['attribution']['minimal']):
        if required not in policy:
            raise ValueError(f'Website policy missing required publication metadata: {required}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Fail on stale output without modifying any files')
    args = parser.parse_args()
    try:
        data = load_yaml(ROOT / 'SRL-LICENSE.yaml')
        validate_v2(data)
        verify_license_files(ROOT, data)
        validate_content_templates(ROOT, data)
        manifest = load_yaml(ROOT / data['machine_readable']['rsl']['manifest'])
        rsl_records = select_records(ROOT, manifest, data)
        outputs = render(data, rsl_records)
        verify_output(outputs, data, rsl_records)
        stale = [name for name, content in outputs.items() if not (ROOT / name).is_file() or (ROOT / name).read_bytes() != content.encode('utf-8')]
        if args.check and stale:
            raise ValueError('Stale generated files (rebuild and commit): ' + ', '.join(stale))
        if not args.check:
            for name, content in outputs.items():
                path = ROOT / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode('utf-8'))
        print(f"SRLF {data['meta']['version']}: {len(outputs)} outputs validated; {len(rsl_records)} explicit RSL {data['machine_readable']['rsl']['protocol_version']} records; canonical license checksums verified.")
        return 0
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
