"""Regression tests for legal/access boundaries and release validation."""
import copy
import contextlib
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'automation/license_builder'))
sys.path.insert(0, str(ROOT / 'tools'))
import build_licenses as builder
import enforce_version_refs as guard
from generate_files import render
from rsl import NS, RSL, SRAGI, select_records, validate_projection


class LicensingTests(unittest.TestCase):
    def setUp(self):
        self.data = builder.load_yaml(ROOT / 'SRL-LICENSE.yaml')
        self.manifest = builder.load_yaml(ROOT / self.data['machine_readable']['rsl']['manifest'])
        self.records = select_records(ROOT, self.manifest, self.data)

    def test_machine_access_cannot_become_a_grant(self):
        for path, value in [
            (('rights', 'ecosystem_default_license'), 'CC-BY-4.0'),
            (('machine_readable', 'rsl', 'protocol_version'), '2.0'),
            (('machine_readable', 'rsl', 'enabled'), False),
            (('machine_access', 'ai_policy', 'legal_license_grant'), True),
            (('machine_access', 'robots', 'legal_license_grant'), True),
            (('machine_access', 'agents', 'default'), 'GPTBot'),
            (('machine_access', 'discovery', 'allow_indexing'), False),
            (('attribution', 'preferred_machine_attribution', 'binding'), True),
            (('contributions', 'commercial_relicensing', 'requirement'), 'none'),
            (('publication', 'generated_formats', 'robots', 'path'), '../robots.txt'),
        ]:
            with self.subTest(path=path):
                data = copy.deepcopy(self.data)
                parent = data
                for part in path[:-1]:
                    parent = parent[part]
                parent[path[-1]] = value
                with self.assertRaises(ValueError):
                    builder.validate_v2(data)

    def test_machine_output_preserves_rights_and_unresolved_ai_interpretation(self):
        outputs = render(self.data, self.records)
        builder.verify_output(outputs, self.data, self.records)
        self.assertNotIn('Give more than you take', outputs['ai-policy.txt'])
        for path in ('content/license/ai-policy.xml',):
            root = ET.fromstring(outputs[path])
            self.assertEqual(root.get('legal-license-grant'), 'false')
            self.assertEqual(root.find('preferred-machine-attribution').get('binding'), 'false')
            self.assertIn('does not determine', root.findtext('ai-training-and-adaptation'))
            self.assertEqual(root.findtext('machine-access/agents'), '*')
            self.assertIn('applicable', root.findtext('commercial-grant-rule'))
        self.assertIn('License: https://sragi.org/content/license/LICENSE-RSL.xml', outputs['robots.txt'])
        rsl = ET.fromstring(outputs['content/license/LICENSE-RSL.xml'])
        self.assertIn('does not determine', rsl.findtext('s:framework/s:ai-training-and-adaptation', namespaces=NS))
        self.assertEqual(rsl.find('s:framework', NS).get('version'), '2.0')
        self.assertIsNone(rsl.get('version'))
        self.assertNotIn('CC-BY', outputs['robots.txt'])

    def test_master_changes_propagate_and_markup_is_escaped(self):
        data = copy.deepcopy(self.data)
        name = 'Project <demo> & "quoted"'
        data['meta']['name'] = name
        data['organization']['licensing_email'] = 'test@example.invalid'
        data['attribution']['preferred_machine_attribution']['value'] = name
        outputs = render(data, self.records)
        root = ET.fromstring(outputs['content/license/ai-policy.xml'])
        self.assertEqual(root.findtext('framework'), name)
        self.assertEqual(root.findtext('preferred-machine-attribution'), name)
        self.assertIn('test@example.invalid', outputs['ai-policy.txt'])
        self.assertIn('&lt;demo&gt;', outputs['content/license/index.html'])
        self.assertNotIn('<demo>', outputs['content/license/index.html'])

    def test_render_is_deterministic_and_json_retains_all_master_sections(self):
        self.assertEqual(render(self.data, self.records), render(copy.deepcopy(self.data), self.records))
        data = copy.deepcopy(self.data)
        data['future_extension'] = {'example': 'preserved'}
        result = json.loads(render(data, self.records)['content/license/license.json'])
        self.assertEqual(result['future_extension'], data['future_extension'])
        self.assertIn('machine_readable', result)

    def test_fenced_and_duplicate_yaml_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'input.yaml'
            for content in ['```yaml\nrights: {}\n```\n', 'rights: {}\nrights: {}\n']:
                p.write_text(content)
                with self.assertRaises(ValueError):
                    builder.load_yaml(p)

    def test_missing_or_modified_license_text_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / 'LICENSES', root / 'LICENSES')
            builder.verify_license_files(root, self.data)
            p = root / 'LICENSES/CC-BY-4.0.txt'
            p.write_text('altered legal text')
            with self.assertRaisesRegex(ValueError, 'checksum'):
                builder.verify_license_files(root, self.data)
            p.unlink()
            with self.assertRaisesRegex(ValueError, 'Missing'):
                builder.verify_license_files(root, self.data)

    def test_check_mode_detects_drift_without_rewriting_it(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            shutil.copytree(ROOT / 'LICENSES', root / 'LICENSES')
            shutil.copyfile(ROOT / 'SRL-LICENSE.yaml', root / 'SRL-LICENSE.yaml')
            for name in [self.data['machine_readable']['rsl']['manifest']] + [r['path'] for r in self.records] + [s['path'] for s in self.data['content_templates'].values()]:
                destination = root / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, destination)
            for name, content in render(self.data, self.records).items():
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content.encode())
            p = root / 'ai-policy.txt'
            p.write_text('stale policy\n')
            with patch.object(builder, 'ROOT', root), patch.object(sys, 'argv', ['builder', '--check']), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(builder.main(), 1)
            self.assertEqual(p.read_text(), 'stale policy\n')

    def test_guard_rejects_blanket_claims_but_preserves_explicit_artifact_licenses(self):
        forbidden = ['All SRAGI content is licensed under **CC BY-SA 4.0**.', 'Alt SRAGI-innhold er lisensiert under CC BY-SA 4.0.', 'Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL)', 'license: SRL-1.12 (CC BY 4.0)']
        for text in forbidden:
            with self.subTest(text=text):
                self.assertTrue(any(p.search(text) for p in guard.BAD_PATTERNS.values()))
        valid = 'Private by default.\n\nLicensed under CC-BY-4.0.'
        self.assertFalse(any(p.search(valid) for p in guard.BAD_PATTERNS.values()))

    def test_rsl_core_has_exact_scopes_and_standard_licenses_without_extensions(self):
        root = ET.fromstring(render(self.data, self.records)['content/license/LICENSE-RSL.xml'])
        self.assertEqual(root.tag, '{https://rslstandard.org/rsl}rsl')
        contents = [c for c in root.findall('r:content', NS) if c.get('url') != '/']
        self.assertEqual(len(contents), 2)
        for content in contents:
            self.assertTrue(content.get('url').endswith('.md$'))
            self.assertIsNone(content.get('server'))
            # Core-only processors retain the complete CC standard reference.
            for extension in list(content):
                if extension.tag.startswith('{' + SRAGI + '}'):
                    content.remove(extension)
            self.assertEqual(content.findtext('r:license/r:payment/r:standard', namespaces=NS),
                             'https://creativecommons.org/licenses/by/4.0/')
            self.assertEqual(content.find('r:license/r:payment', NS).get('type'), 'attribution')
        self.assertFalse(root.findall('.//r:permits', NS))
        self.assertFalse(root.findall('.//r:prohibits', NS))

    def test_rsl_regressions_fail_even_when_xml_parses(self):
        text = render(self.data, self.records)['content/license/LICENSE-RSL.xml']
        mutations = [
            text.replace('xmlns="https://rslstandard.org/rsl"', 'xmlns="urn:custom"'),
            text.replace('<rsl ', '<rsl version="2.0" ', 1),
            text.replace('<license>', '<license><permits type="usage">all</permits>', 1),
            text.replace('by/4.0/', 'by-sa/4.0/', 1),
            text.replace(self.records[0]['rsl_path'], '/', 1),
            text.replace('<standard>', '<made-up-standard>', 1).replace('</standard>', '</made-up-standard>', 1),
        ]
        for changed in mutations:
            with self.subTest(changed=changed[:100]):
                ET.fromstring(changed)
                with self.assertRaises(ValueError):
                    validate_projection(changed, self.records, self.data)
        outputs = render(self.data, self.records)
        outputs['robots.txt'] = '\n'.join(line for line in outputs['robots.txt'].splitlines() if not line.startswith('License:'))
        with self.assertRaisesRegex(ValueError, 'RSL discovery'):
            builder.verify_output(outputs, self.data, self.records)

    def test_rsl_manifest_requires_evidence_and_rejects_unresolved_or_broad_scope(self):
        for key, value in [('source_sha256', '0' * 64), ('status', 'needs_rights_review'),
                           ('rsl_path', '/'), ('license_expression', 'CC-BY-SA-4.0')]:
            manifest = copy.deepcopy(self.manifest)
            record = next(r for r in manifest['artifacts'] if 'rsl_path' in r)
            record[key] = value
            with self.subTest(key=key), self.assertRaises(ValueError):
                select_records(ROOT, manifest, self.data)

    def test_dual_license_preserves_open_path_and_requires_commercial_provenance(self):
        import hashlib
        DUAL = self.data['dual_licensing']['canonical_instruction_expression']
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = ('SPDX-License-Identifier: ' + DUAL + '\n').encode()
            (root / 'example.txt').write_bytes(source)
            record = {'path': 'example.txt', 'rsl_path': '/example.txt$',
                      'status': 'explicit_license_verified', 'license_expression': DUAL,
                      'source_sha256': hashlib.sha256(source).hexdigest(),
                      'commercial_relicensing_verified': False}
            manifest = {'authority': 'artifact', 'meta': {'legal_license_grant': False}, 'artifacts': [record]}
            with self.assertRaisesRegex(ValueError, 'commercial rights'):
                select_records(root, manifest, self.data)
            record['commercial_relicensing_verified'] = True
            records = select_records(root, manifest, self.data)
            text = render(self.data, records)['content/license/LICENSE-RSL.xml']
            validate_projection(text, records, self.data)
            node = ET.fromstring(text)
            node = next(c for c in node.findall('r:content', NS) if c.get('url') == '/example.txt$')
            self.assertEqual(len(node.findall('r:license', NS)), 1)
            self.assertEqual(node.findtext('r:license/r:payment/r:standard', namespaces=NS),
                             'https://creativecommons.org/licenses/by-sa/4.0/')
            self.assertEqual(node.findtext('s:license-expression', namespaces=NS), DUAL)


if __name__ == '__main__':
    unittest.main()
