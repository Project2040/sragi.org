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


class LicensingTests(unittest.TestCase):
    def setUp(self):
        self.data = builder.load_yaml(ROOT / 'SRL-LICENSE.yaml')

    def test_machine_access_cannot_become_a_grant(self):
        for path, value in [
            (('rights', 'ecosystem_default_license'), 'CC-BY-4.0'),
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
        outputs = render(self.data)
        builder.verify_output(outputs, self.data)
        self.assertNotIn('Give more than you take', outputs['ai-policy.txt'])
        for path in ('content/license/ai-policy.xml', 'content/license/LICENSE-RSL.xml'):
            root = ET.fromstring(outputs[path])
            self.assertEqual(root.get('legal-license-grant'), 'false')
            self.assertEqual(root.find('preferred-machine-attribution').get('binding'), 'false')
            self.assertIn('does not determine', root.findtext('ai-training-and-adaptation'))
            self.assertEqual(root.findtext('machine-access/agents'), '*')
            self.assertIn('applicable', root.findtext('commercial-grant-rule'))
        self.assertNotIn('License:', outputs['robots.txt'])
        self.assertNotIn('CC-BY', outputs['robots.txt'])

    def test_master_changes_propagate_and_markup_is_escaped(self):
        data = copy.deepcopy(self.data)
        name = 'Project <demo> & "quoted"'
        data['meta']['name'] = name
        data['organization']['licensing_email'] = 'test@example.invalid'
        data['attribution']['preferred_machine_attribution']['value'] = name
        outputs = render(data)
        root = ET.fromstring(outputs['content/license/ai-policy.xml'])
        self.assertEqual(root.findtext('framework'), name)
        self.assertEqual(root.findtext('preferred-machine-attribution'), name)
        self.assertIn('test@example.invalid', outputs['ai-policy.txt'])
        self.assertIn('&lt;demo&gt;', outputs['content/license/index.html'])
        self.assertNotIn('<demo>', outputs['content/license/index.html'])

    def test_render_is_deterministic_and_json_retains_all_master_sections(self):
        self.assertEqual(render(self.data), render(copy.deepcopy(self.data)))
        data = copy.deepcopy(self.data)
        data['future_extension'] = {'example': 'preserved'}
        result = json.loads(render(data)['content/license/license.json'])
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
            for name, content in render(self.data).items():
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


if __name__ == '__main__':
    unittest.main()
