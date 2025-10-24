#!/usr/bin/env python3
# ===========================================================
#  SRAGI LICENSE BUILDER — v1.2
#  © 2025 Rune Solberg / Neptunia Media AS
#  Reads SRL-LICENSE.yaml and generates all license artifacts
#  All files output to: content/license/
# ===========================================================

import os
import sys
import yaml
import json
from datetime import datetime
from generate_files import *

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
YAML_FILE = os.path.join(BASE_DIR, "SRL-LICENSE.yaml")
LOG_FILE = os.path.join(BASE_DIR, "sync/sync-log.json")
LICENSE_DIR = os.path.join(BASE_DIR, "content", "license")

def load_yaml(path):
    """Load and parse YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def log_event(result):
    """Append build result to sync log."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
        f.write("\n")

def show_debug_info(data):
    """Show debug information if DEBUG env var is set."""
    if not os.getenv("DEBUG"):
        return
    
    print("\n🔍 DEBUG MODE\n")
    print(f"📋 YAML Structure:")
    print(f"  - Version: {data.get('meta', {}).get('version')}")
    print(f"  - License: {data.get('meta', {}).get('base_license')}")
    print(f"  - Permissions: {len(data.get('permissions', {}).get('usage', []))} items")
    print(f"  - Organization: {data.get('organization', {}).get('organization')}")
    
    if data.get('content'):
        print(f"  - Content sections: {', '.join(data['content'].keys())}")
    
    print()

def verify_output():
    """Verify that all expected files were created."""
    expected_files = [
        "LICENSE-RSL.xml",
        "REGENERATIVE_LICENSE.md",
        "ai-policy.xml",
        "ai-policy.txt",
        "robots.txt",
        "sitemap.xml"
    ]
    
    missing = []
    for filename in expected_files:
        filepath = os.path.join(LICENSE_DIR, filename)
        if not os.path.exists(filepath):
            missing.append(filename)
    
    if missing:
        print(f"\n⚠️  WARNING: Missing files: {', '.join(missing)}\n")
        return False
    
    print(f"\n✅ All {len(expected_files)} files verified in {os.path.relpath(LICENSE_DIR, BASE_DIR)}/\n")
    return True

def main():
    """Main build function."""
    # Load YAML
    try:
        data = load_yaml(YAML_FILE)
        print(f"📖 Loaded {os.path.relpath(YAML_FILE, BASE_DIR)}")
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find {YAML_FILE}")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ ERROR: Invalid YAML syntax:\n{e}")
        sys.exit(1)
    
    # Show debug info if enabled
    show_debug_info(data)
    
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    results = {}
    
    print(f"\n🧩 Building SRAGI License Files — {timestamp}\n")
    
    # Generate all files
    try:
        results["LICENSE-RSL.xml"] = generate_rsl_xml(data)
        results["REGENERATIVE_LICENSE.md"] = generate_human_license(data)
        results["ai-policy.xml"] = generate_ai_policy_xml(data)
        results["ai-policy.txt"] = generate_ai_policy_txt(data)
        results["robots.txt"] = generate_robots(data)
        results["sitemap.xml"] = generate_sitemap(data)
        
        # Log success
        log_event({
            "timestamp": timestamp,
            "status": "success",
            "version": data.get("meta", {}).get("version"),
            "results": results
        })
        
        # Verify output
        verify_output()
        
        print("✅ All license files generated successfully!\n")
        
    except FileNotFoundError as e:
        error_msg = f"Template file not found: {e}"
        print(f"❌ ERROR: {error_msg}")
        log_event({
            "timestamp": timestamp,
            "status": "error",
            "error": error_msg
        })
        sys.exit(1)
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ ERROR during build: {error_msg}")
        log_event({
            "timestamp": timestamp,
            "status": "error",
            "error": error_msg
        })
        sys.exit(1)

if __name__ == "__main__":
    main()
