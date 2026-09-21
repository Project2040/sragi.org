"""Deployment checks distinguish a matching release from merely HTTP 200."""
import hashlib
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from check_licensing_deployment import inspect_response


class DeploymentChecks(unittest.TestCase):
    def test_static_release_checks_bytes_and_required_media_type(self):
        body = b'<rsl/>'
        target = {'url': 'https://example.test/license.xml', 'media_types': ['application/rsl+xml'],
                  'sha256': hashlib.sha256(body).hexdigest()}
        self.assertEqual(inspect_response(target, 200, {'content-type': 'application/rsl+xml; charset=utf-8'}, body, target['url'])['status'], 'pass')
        for status, kind, payload in [(404, 'application/rsl+xml', body), (200, 'application/xml', body),
                                     (200, 'application/rsl+xml', b'old release')]:
            with self.subTest(status=status, kind=kind, payload=payload):
                self.assertEqual(inspect_response(target, status, {'content-type': kind}, payload, target['url'])['status'], 'fail')

    def test_soft_200_does_not_pass_as_a_commercial_page(self):
        target = {'url': 'https://example.test/commercial/', 'media_types': ['text/html'],
                  'markers': ['Commercial Suite License', 'sales@example.test']}
        for body in (b'<h1>Page not found</h1>', b'<script>Commercial Suite License sales@example.test</script>'):
            self.assertEqual(inspect_response(target, 200, {'content-type': 'text/html'}, body, target['url'])['status'], 'fail')
        body = b'<h1>Commercial <b>Suite</b> License</h1><p>sales@example.test</p>'
        self.assertEqual(inspect_response(target, 200, {'content-type': 'text/html'}, body, target['url'])['status'], 'pass')


if __name__ == '__main__':
    unittest.main()
