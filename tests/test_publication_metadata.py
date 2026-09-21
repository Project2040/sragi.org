"""Public routing and instruction metadata must follow the same master."""
import copy
from html.parser import HTMLParser
from pathlib import Path
import sys
import unittest
from xml.etree import ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'automation/license_builder'))
import build_licenses as builder
from generate_files import render
from rsl import select_records


class OverviewParser(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.tables, self.headers = [], 0, []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a':
            self.links.append(attrs.get('href'))
        if tag == 'table':
            self.tables += 1
        if tag == 'th':
            self.headers.append(attrs.get('scope'))


class PublicationMetadataTests(unittest.TestCase):
    def setUp(self):
        self.data = builder.load_yaml(ROOT / 'SRL-LICENSE.yaml')
        manifest = builder.load_yaml(ROOT / self.data['machine_readable']['rsl']['manifest'])
        self.records = select_records(ROOT, manifest, self.data)

    def test_configured_contacts_and_portals_propagate_without_literal_defaults(self):
        source = (ROOT / 'SRL-LICENSE.yaml').read_text()
        replacements = {
            'contact@sragi.org': 'hello@example.test',
            'licensing@sragi.org': 'rights@example.test',
            'commercial@sragi.org': 'sales@example.test',
            'https://sragi.org/licensing/': 'https://example.test/rights/',
            'https://sragi.org/commercial-licensing/': 'https://example.test/agreements/',
            'SRAGI® Commercial Suite License': 'Future Commercial License',
        }
        for old, new in replacements.items():
            source = source.replace(old, new)
        data = yaml.load(source, Loader=builder.UniqueKeyLoader)
        builder.validate_v2(data)
        outputs = render(data, self.records)
        builder.verify_output(outputs, data, self.records)
        for path in ('content/license/REGENERATIVE_LICENSE.md', 'content/license/index.html', 'ai-policy.txt', 'content/license/ai-policy.xml', 'content/license/license.json'):
            for old, new in replacements.items():
                with self.subTest(path=path, setting=old):
                    self.assertIn(new, outputs[path])
                    self.assertNotIn(old, outputs[path])
        reference = outputs['LICENSES/LicenseRef-SRAGI-Commercial.txt']
        for value in ('rights@example.test', 'sales@example.test', 'https://example.test/agreements/', 'Future Commercial License'):
            self.assertIn(value, reference)
        ai = ET.fromstring(outputs['content/license/ai-policy.xml'])
        self.assertEqual(ai.findtext('general-contact'), 'hello@example.test')
        self.assertEqual(ai.findtext('licensing-contact'), 'rights@example.test')
        self.assertEqual(ai.findtext('commercial-contact'), 'sales@example.test')

    def test_instruction_alias_drift_and_swapped_url_roles_are_rejected(self):
        changes = [
            ('license.spdx', 'CC-BY-4.0'),
            ('license.commercial_license', 'Old name'),
            ('license.licensing_url', 'https://sragi.org/commercial-licensing/'),
            ('license_url', 'https://sragi.org/licensing/'),
            ('commercial_licensing.url', 'https://sragi.org/licensing/'),
            ('commercial_licensing.contact', 'licensing@sragi.org'),
            ('commercial_licensing.basis', 'metadata_only'),
            ('commercial_licensing.available', False),
            ('contact', 'commercial@sragi.org'),
        ]
        for path, value in changes:
            data = copy.deepcopy(self.data)
            target = data['machine_readable']['instruction_frontmatter']
            parts = path.split('.')
            for part in parts[:-1]:
                target = target[part]
            target[parts[-1]] = value
            with self.subTest(path=path), self.assertRaises(ValueError):
                builder.validate_v2(data)

    def test_overview_tables_and_clickable_role_links(self):
        outputs = render(self.data, self.records)
        parsed = OverviewParser(outputs['content/license/index.html'])
        markdown = outputs['content/license/REGENERATIVE_LICENSE.md']
        self.assertEqual(parsed.tables, 3)
        self.assertEqual(parsed.headers, ['col'] * 9)
        self.assertIn('| Class | Available licenses / expression | Description |', markdown)
        for role, spec in self.data['publication']['contact_roles'].items():
            uri = 'mailto:' + spec['email']
            with self.subTest(role=role):
                self.assertIn(uri, parsed.links)
                self.assertIn('](<' + uri + '>)', markdown)
        self.assertNotIn('mailto\\:', markdown)
        for key in ('canonical_licensing_portal', 'commercial_licensing_portal'):
            self.assertIn(self.data['publication'][key], parsed.links)
        self.assertIn('license.commercial_license', outputs['content/license/index.html'])
        self.assertIn('commercial_licensing.basis', outputs['content/license/index.html'])

    def test_table_values_escape_markup_and_do_not_split_markdown_rows(self):
        data = copy.deepcopy(self.data)
        data['license_classes']['open_knowledge']['description'] = 'A | B <script>alert(1)</script>'
        outputs = render(data, self.records)
        self.assertIn('A \\| B &lt;script&gt;', outputs['content/license/REGENERATIVE_LICENSE.md'])
        self.assertIn('A | B &lt;script&gt;', outputs['content/license/index.html'])
        self.assertNotIn('<script>', outputs['content/license/index.html'])

    def test_commercial_reference_preserves_scope_and_agreement_boundaries(self):
        data = copy.deepcopy(self.data)
        data['commercial']['sharealike_exception']['limits'] += '\nAdditional scope statement from master.'
        outputs = render(data, self.records)
        reference = outputs['LICENSES/LicenseRef-SRAGI-Commercial.txt']
        for required in ('Private modification alone does not trigger', 'Additional scope statement from master.', 'separate_written_agreement', 'does not itself constitute an agreement or grant rights'):
            self.assertIn(required, reference)
        self.assertIn('Additional scope statement from master.', outputs['content/license/REGENERATIVE_LICENSE.md'])
        self.assertIn('Commercial activity alone does not imply', reference)

    def test_publication_configurations_are_parseable_yaml_mappings(self):
        for path in (ROOT / 'docs/_CONFIG').glob('*.yaml'):
            with self.subTest(path=path.name):
                self.assertIsInstance(yaml.safe_load(path.read_text()), dict)


if __name__ == '__main__':
    unittest.main()
