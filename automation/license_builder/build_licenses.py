#!/usr/bin/env python3
"""Build and validate SRLF 2.0 licensing/discovery artifacts."""

import json
import os
import sys
import traceback
from datetime import datetime, timezone

import yaml
from generate_files import (
    generate_ai_policy_txt,
    generate_ai_policy_xml,
    generate_human_license,
    generate_license_html,
    generate_license_json,
    generate_robots,
    generate_rsl_xml,
    generate_sitemap,
)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
YAML_FILE = os.path.join(BASE_DIR, "SRL-LICENSE.yaml")
LOG_FILE = os.path.join(BASE_DIR, "sync", "sync-log.json")
LICENSE_DIR = os.path.join(BASE_DIR, "content", "license")


def load_yaml(path):
    raw = open(path, "r", encoding="utf-8").read()
    if raw.lstrip().startswith("```") or raw.rstrip().endswith("```"):
        raise ValueError("SRL-LICENSE.yaml must be pure YAML, not a Markdown code fence")
    data = yaml.safe_load(raw)
    if not isinstance(data, dict):
        raise ValueError("SRL-LICENSE.yaml must contain a YAML mapping at document root")
    return data


def validate_v2(data):
    errors = []
    meta = data.get("meta", {})
    rights = data.get("rights", {})
    machine = data.get("machine_access", {})
    dual = data.get("dual_licensing", {})
    custom = data.get("machine_readable", {}).get("custom_license_references", {})

    checks = [
        (str(meta.get("version")) == "2.0", "meta.version must be 2.0"),
        (rights.get("authority") == "artifact", "rights.authority must be artifact"),
        (rights.get("ecosystem_default_license", "sentinel") is None, "rights.ecosystem_default_license must be null"),
        (machine.get("agents", {}).get("default") == "*", "machine_access.agents.default must be '*'"),
        (machine.get("robots", {}).get("legal_license_grant") is False, "robots must not be a legal license grant"),
        (machine.get("ai_policy", {}).get("legal_license_grant") is False, "ai_policy must not be a legal license grant"),
        (dual.get("canonical_instruction_expression") == "CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial", "canonical instruction SPDX expression mismatch"),
        ("LicenseRef-SRAGI-Commercial" in custom, "custom commercial LicenseRef must be defined"),
    ]
    errors.extend(message for ok, message in checks if not ok)
    if errors:
        raise ValueError("SRLF 2.0 validation failed:\n- " + "\n- ".join(errors))


def verify_license_files(data):
    expected = data.get("machine_readable", {}).get("license_files", {}).get("expected", [])
    missing = [name for name in expected if not os.path.exists(os.path.join(BASE_DIR, "LICENSES", name))]
    if missing:
        raise RuntimeError(
            "Missing canonical license files: " + ", ".join(missing) +
            ". Run tools/sync_spdx_license_texts.py for standard SPDX texts."
        )


def log_event(result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, default=str)
        f.write("\n")


def verify_output():
    expected = [
        os.path.join(LICENSE_DIR, "LICENSE-RSL.xml"),
        os.path.join(LICENSE_DIR, "REGENERATIVE_LICENSE.md"),
        os.path.join(LICENSE_DIR, "index.html"),
        os.path.join(LICENSE_DIR, "license.json"),
        os.path.join(LICENSE_DIR, "ai-policy.xml"),
        os.path.join(BASE_DIR, "ai-policy.txt"),
        os.path.join(BASE_DIR, "robots.txt"),
        os.path.join(BASE_DIR, "sitemap.xml"),
    ]
    missing = [os.path.relpath(p, BASE_DIR) for p in expected if not os.path.exists(p)]
    if missing:
        raise RuntimeError("Missing generated files: " + ", ".join(missing))


def main():
    try:
        data = load_yaml(YAML_FILE)
        validate_v2(data)
        verify_license_files(data)
        print("Loaded SRL-LICENSE.yaml — SRLF 2.0 validated")

        results = {
            "LICENSE-RSL.xml": generate_rsl_xml(data),
            "REGENERATIVE_LICENSE.md": generate_human_license(data),
            "index.html": generate_license_html(data),
            "license.json": generate_license_json(data),
            "ai-policy.xml": generate_ai_policy_xml(data),
            "ai-policy.txt": generate_ai_policy_txt(data),
            "robots.txt": generate_robots(data),
            "sitemap.xml": generate_sitemap(data),
        }
        verify_output()
        log_event({
            "build_time": datetime.now(timezone.utc).isoformat(),
            "framework_version": str(data.get("meta", {}).get("version")),
            "framework_date": str(data.get("meta", {}).get("last_updated", "")),
            "status": "success",
            "results": results,
        })
        print("SRLF 2.0 build complete and verified.")
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
