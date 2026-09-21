#!/usr/bin/env python3
"""Instantiate a registered YAML template using master data and explicit inputs.

--for-publication validates licensing metadata; it never publishes to a CMS.
"""
import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'automation/license_builder'))
from build_licenses import load_yaml, validate_v2
from policy import render_content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template', required=True)
    parser.add_argument('--values', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--for-publication', action='store_true')
    args = parser.parse_args()
    try:
        data = load_yaml(ROOT / 'SRL-LICENSE.yaml')
        validate_v2(data)
        rendered = render_content(ROOT, data, args.template, load_yaml(args.values), args.for_publication)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        # Never overwrite an existing artifact or its license notice.
        with args.output.open('x', encoding='utf-8') as handle:
            handle.write(rendered)
        print(f'Created {args.output}; no website deployment performed.')
        return 0
    except (ValueError, KeyError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
