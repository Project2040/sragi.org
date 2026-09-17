"""Website inheritance, scoped licensing and non-exclusive crawler declarations."""
import copy
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree as ET
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'automation/license_builder'))
import build_licenses as builder
from generate_files import render
from policy import render_content, resolve_license, validate_content_templates
from rsl import NS, select_records, validate_projection


class WebsitePolicyTests(unittest.TestCase):
    def setUp(self):
        self.data = builder.load_yaml(ROOT / 'SRL-LICENSE.yaml')
        self.context = {'url': 'https://sragi.org/article/', 'public': True, 'rights_verified': True}
        self.records = select_records(ROOT, builder.load_yaml(ROOT / self.data['machine_readable']['rsl']['manifest']), self.data)

    def test_website_default_and_explicit_diamonds_have_distinct_scopes(self):
        value = resolve_license(self.data, {}, 'website_content', self.context, True)
        self.assertEqual(value['spdx'], 'CC-BY-4.0')
        self.assertEqual(value['resolved_from'], 'website_licensing')
        diamond = self.data['dual_licensing']['canonical_instruction_expression']
        for profile in ['website_content', 'explicit_artifact']:
            value = resolve_license(self.data, {'spdx': diamond}, profile, self.context, True)
            self.assertEqual(value['spdx'], diamond)
            self.assertEqual(value['resolved_from'], 'artifact')
        with self.assertRaises(ValueError):
            resolve_license(self.data, {}, 'explicit_artifact', self.context, True)

    def test_default_cannot_relicense_external_private_or_third_party_material(self):
        for override in [{'url': 'https://other.example/article/'}, {'public': False},
                         {'rights_verified': False}, {'third_party': True},
                         {'url': 'https://sragi.org.attacker.example/a/'}]:
            context = dict(self.context, **override)
            with self.subTest(override=override), self.assertRaises(ValueError):
                resolve_license(self.data, {}, 'website_content', context, True)
        with self.assertRaisesRegex(ValueError, 'Conflicting'):
            resolve_license(self.data, {'spdx': 'CC-BY-4.0', 'type': 'CC-BY-SA-4.0'}, 'website_content', self.context, True)
        third_party = resolve_license(self.data, {'rights_statement': 'Third-party terms at https://example.org/terms'}, 'website_content', dict(self.context, third_party=True), True)
        self.assertIsNone(third_party['spdx'])
        self.assertEqual(third_party['status'], 'explicit')
        self.assertEqual(self.data['website_licensing']['precedence'][0], 'third_party_terms')

    def test_every_registered_template_renders_real_yaml_and_preserves_explicit_license(self):
        validate_content_templates(ROOT, self.data)
        for name, spec in self.data['content_templates'].items():
            raw = (ROOT / spec['path']).read_text()
            inputs = {key: 'Demo "quoted"\nsecond line: safe' for key in re.findall(r'{{\s*input\.(\w+)\s*}}', raw)}
            inputs['publication_context'] = self.context
            inputs['license'] = {'spdx': 'CC-BY-SA-4.0'}
            with self.subTest(template=name):
                output = render_content(ROOT, self.data, name, inputs, True)
                parsed = yaml.safe_load(output)
                self.assertEqual(parsed['license']['spdx'], 'CC-BY-SA-4.0')
                self.assertNotIn('{{', output)
                if name == 'editorial':
                    self.assertEqual(parsed['authors']['primary'], inputs['author_id'])
                else:
                    self.assertIn(self.data['organization']['creator'], output)
        with self.assertRaisesRegex(ValueError, 'Missing template value'):
            render_content(ROOT, self.data, 'basic', {}, True)

    def test_policy_and_crawler_signals_propagate_without_changing_robots_mechanism(self):
        data = copy.deepcopy(self.data)
        data['website_licensing']['default_spdx'] = 'CC-BY-SA-4.0'
        data['website_licensing']['default_license_url'] = 'https://creativecommons.org/licenses/by-sa/4.0/'
        data['machine_access']['agents']['named'].append('FutureBot')
        data['organization']['creator'] = 'New author from master'
        builder.validate_v2(data)
        values = {'title': 'A title', 'slug': 'a-title', 'date': '2026-09-17', 'publication_context': self.context}
        result = yaml.safe_load(render_content(ROOT, data, 'basic', values, True))
        self.assertEqual(result['meta']['author'], 'New author from master')
        self.assertEqual(result['license']['spdx'], 'CC-BY-SA-4.0')
        outputs = render(data, self.records)
        self.assertNotIn('User-agent: FutureBot', outputs['robots.txt'])
        self.assertIn('FutureBot', outputs['ai-policy.txt'])
        self.assertIn('Website-Default-License: CC-BY-SA-4.0', outputs['ai-policy.txt'])
        self.assertIn('made available under CC-BY-SA-4.0', outputs['content/license/WEBSITE-LICENSE.html'])

    def test_named_and_unknown_crawlers_follow_single_wildcard_group(self):
        outputs = render(self.data, self.records)
        robots = outputs['robots.txt']
        self.assertEqual(robots.count('User-agent:'), 1)
        self.assertIn('User-agent: *', robots)
        parser = RobotFileParser()
        parser.parse(robots.splitlines())
        for agent in self.data['machine_access']['agents']['named'] + ['UnlistedFutureCrawler']:
            self.assertTrue(parser.can_fetch(agent, 'https://sragi.org/any/path'))

        restricted = robots.replace('Disallow:\n', 'Disallow: /private/\n', 1)
        parser = RobotFileParser()
        parser.parse(restricted.splitlines())
        for agent in ['GPTBot', 'ClaudeBot', 'CCBot', 'UnlistedFutureCrawler']:
            self.assertFalse(parser.can_fetch(agent, 'https://sragi.org/private/data'))

        data = copy.deepcopy(self.data)
        data['machine_access']['agents']['named'].append('BadBot\nDisallow: /')
        with self.assertRaises(ValueError):
            builder.validate_v2(data)

    def test_generated_outputs_have_no_unresolved_policy_placeholders(self):
        outputs = render(self.data, self.records)
        for path, text in outputs.items():
            with self.subTest(path=path):
                self.assertNotIn('{{', text)
                self.assertNotIn('}}', text)

    def test_website_policy_is_self_describing_and_machine_linked(self):
        policy = render(self.data, self.records)['content/license/WEBSITE-LICENSE.html']
        self.assertIn('rel="license"', policy)
        self.assertIn(str(self.data['meta']['version']), policy)
        self.assertIn(str(self.data['meta']['last_updated']), policy)
        self.assertIn(self.data['attribution']['minimal'], policy)
        self.assertIn('Adapted Material', policy)

    def test_rsl_site_reference_keeps_exceptions_in_core_terms_without_fees(self):
        outputs = render(self.data, self.records)
        text = outputs['content/license/LICENSE-RSL.xml']
        root = ET.fromstring(text)
        site = next(node for node in root.findall('r:content', NS) if node.get('url') == '/')
        self.assertIsNone(site.get('server'))
        payment = site.find('r:license/r:payment', NS)
        self.assertEqual(payment.get('type'), 'attribution')
        self.assertEqual(payment.findtext('r:standard', namespaces=NS), self.data['website_licensing']['policy_url'])
        self.assertEqual(site.findtext('r:terms', namespaces=NS), self.data['website_licensing']['policy_url'])
        self.assertFalse(root.findall('.//r:permits', NS))
        self.assertIn('CC-BY-4.0', outputs['content/license/WEBSITE-LICENSE.html'])
        self.assertIn('takes precedence', outputs['content/license/WEBSITE-LICENSE.html'])
        for invalid_type in ('free', 'subscription'):
            with self.subTest(payment=invalid_type), self.assertRaises(ValueError):
                validate_projection(text.replace('type="attribution"', f'type="{invalid_type}"', 1), self.records, self.data)

    def test_content_cli_creates_and_refuses_to_overwrite_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            values, output = Path(directory) / 'values.yaml', Path(directory) / 'article.yaml'
            values.write_text(yaml.safe_dump({'title': 'Example', 'slug': 'example', 'date': '2026-09-17', 'publication_context': self.context}))
            cmd = [sys.executable, str(ROOT / 'tools/new_content.py'), '--template', 'basic', '--values', str(values), '--output', str(output), '--for-publication']
            first = subprocess.run(cmd, capture_output=True, text=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            original = output.read_bytes()
            self.assertEqual(yaml.safe_load(original)['license']['spdx'], 'CC-BY-4.0')
            second = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(output.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
