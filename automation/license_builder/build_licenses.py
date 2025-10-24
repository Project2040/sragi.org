#!/usr/bin/env python3
# ===========================================================
#  SRAGI LICENSE BUILDER — v1.1
#  © 2025 Rune Solberg / Neptunia Media AS
#  Reads SRL-LICENSE.yaml and generates all license artifacts
# ===========================================================

import os
import yaml
import json
from datetime import datetime
from generate_files import *

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
YAML_FILE = os.path.join(BASE_DIR, "SRL-LICENSE.yaml")
LOG_FILE = os.path.join(BASE_DIR, "sync/sync-log.json")

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def log_event(result):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)
        f.write("\n")

def main():
    try:
        data = load_yaml(YAML_FILE)
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find {YAML_FILE}")
        return

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    results = {}

    print(f"\n🧩 Building SRAGI License Files — {timestamp}\n")

    try:
        results["LICENSE-RSL.xml"] = generate_rsl_xml(data)
        results["REGENERATIVE_LICENSE.md"] = generate_human_license(data)
        results["ai-policy.xml"] = generate_ai_policy_xml(data)
        results["ai-policy.txt"] = generate_ai_policy_txt(data)
        results["robots.txt"] = generate_robots(data)
        results["sitemap.xml"] = generate_sitemap(data)

        log_event({
            "timestamp": timestamp,
            "results": results
        })

        print("✅ All license files generated successfully!\n")

    except Exception as e:
        print(f"❌ ERROR during build: {e}")
        log_event({
            "timestamp": timestamp,
            "error": str(e)
        })

if __name__ == "__main__":
    main()
