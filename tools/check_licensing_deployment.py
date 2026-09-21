#!/usr/bin/env python3
"""Read-only HTTP verification of the SRLF release. Never deploys or purges caches."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'automation/license_builder'))
from build_licenses import load_yaml, validate_v2, verify_license_files, verify_output
from generate_files import render
from rsl import select_records


class PageText(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.parts = []
        self.ignored = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.ignored = True

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.ignored = False

    def handle_data(self, value):
        if not self.ignored:
            self.parts.append(value)


def targets(data, outputs, records):
    items = []
    for path, content in outputs.items():
        if path in {data['publication']['generated_formats'][kind]['path']
                    for kind in ('config_pointer', 'commercial_reference')}:
            continue  # Repository resources without a required public file URL.
        suffix = Path(path).suffix
        types = {'.html': ['text/html'], '.json': ['application/json'],
                 '.xml': ['application/xml', 'text/xml'], '.md': ['text/markdown', 'text/plain'],
                 '.txt': ['text/plain']}[suffix]
        if path == data['publication']['generated_formats']['xml']['path']:
            types = [data['machine_readable']['rsl']['media_type']]
        items.append({'url': data['organization']['website'].rstrip('/') + '/' + path,
                      'sha256': hashlib.sha256(content.encode()).hexdigest(), 'media_types': types})
    for record in records:
        items.append({'url': data['organization']['website'].rstrip('/') + '/' + record['path'],
                      'sha256': record['source_sha256'], 'media_types': ['text/markdown', 'text/plain']})
    for old_path, kind in [('/LICENSE-RSL.xml', 'xml'), ('/ai-policy.xml', 'ai_policy_xml')]:
        canonical = next(item for item in items if item['url'].endswith('/' + data['publication']['generated_formats'][kind]['path']))
        items.append(dict(canonical, url=data['organization']['website'].rstrip('/') + old_path))
    for key in ('canonical_licensing_portal', 'commercial_licensing_portal'):
        items.append({'url': data['publication'][key], 'media_types': ['text/html'],
                      'markers': [data['commercial']['license_name'],
                                  data['publication']['contact_roles']['commercial']['email']]})
    return items


def inspect_response(target, status, headers, body, effective_url):
    issues = []
    media_type = headers.get('content-type', '').split(';', 1)[0].strip().lower()
    digest = hashlib.sha256(body).hexdigest()
    if status != 200:
        issues.append(f'HTTP {status}; expected 200')
    if media_type not in target['media_types']:
        issues.append(f'Content-Type {media_type!r}; expected {target["media_types"]}')
    if 'sha256' in target and digest != target['sha256']:
        issues.append('Served bytes do not match the reviewed release')
    if 'markers' in target:
        parser = PageText(body.decode('utf-8', errors='replace'))
        text = ' '.join(' '.join(parser.parts).split())
        for marker in target['markers']:
            if marker not in text:
                issues.append(f'Public page missing expected content: {marker}')
    return {'url': target['url'], 'effective_url': effective_url, 'http_status': status,
            'content_type': media_type, 'sha256': digest,
            'expected_sha256': target.get('sha256'), 'expected_media_types': target['media_types'],
            'headers': {key: value for key, value in headers.items()
                        if key in {'cache-control', 'age', 'last-modified', 'etag', 'x-license', 'x-license-url', 'x-ai-policy', 'link'}},
            'status': 'pass' if not issues else 'fail', 'issues': issues}


def probe(target, timeout):
    request = Request(target['url'], headers={'User-Agent': 'SRAGI-Licensing-QA/1.0', 'Cache-Control': 'no-cache'})
    try:
        try:
            response = urlopen(request, timeout=timeout)
        except HTTPError as error:
            response = error
        with response:
            body = response.read(8 * 1024 * 1024 + 1)
            if len(body) > 8 * 1024 * 1024:
                raise ValueError('Response exceeds 8 MiB inspection limit')
            return inspect_response(target, response.status,
                                    {key.lower(): value for key, value in response.headers.items()},
                                    body, response.geturl())
    except (URLError, OSError, ValueError) as error:
        return {'url': target['url'], 'status': 'unverified', 'issues': [str(error)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='Optional JSON evidence file')
    parser.add_argument('--timeout', type=float, default=15)
    args = parser.parse_args()
    data = load_yaml(ROOT / 'SRL-LICENSE.yaml')
    validate_v2(data)
    verify_license_files(ROOT, data)
    records = select_records(ROOT, load_yaml(ROOT / data['machine_readable']['rsl']['manifest']), data)
    outputs = render(data, records)
    verify_output(outputs, data, records)
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda item: probe(item, args.timeout), targets(data, outputs, records)))
    report = {'checked_at_utc': datetime.now(timezone.utc).isoformat(),
              'framework_version': data['meta']['version'],
              'all_passed': all(item['status'] == 'pass' for item in results), 'checks': results}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    for result in results:
        print(f"{result['status'].upper()}: {result['url']}" + (' — ' + '; '.join(result['issues']) if result['issues'] else ''))
    return 0 if report['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
