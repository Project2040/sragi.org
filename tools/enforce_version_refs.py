#!/usr/bin/env python3
# ===========================================================
#  SRAGI SSOT Version Enforcement Script
#  tools/enforce_version_refs.py
#
#  Ensures all repository files reference the SRAGI License
#  (SRL) dynamically — never with hardcoded version numbers.
#
#  Author: Rune Solberg / Neptunia Media AS
#  License: CC BY 4.0 via the SRAGI Regenerative License (SRL)
#  -----------------------------------------------------------
#  ✅ Purpose:
#     - Scan repository for invalid SRL version strings
#     - Auto-clean old references where safe
#     - Exit non-zero if violations persist (CI enforcement)
#
#  🧭 Kairos Principle:
#     Chronos updates break continuity.
#     Kairos pointers align all documents to the living SSOT.
# ===========================================================

import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILETYPES = {".md", ".css", ".yaml", ".yml", ".xml", ".txt", ".py"}

# Canonical footer patterns
CANONICAL_BY = (
    "Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL). "
    "See SRL-LICENSE.yaml for current version and details."
)
CANONICAL_BYSA = (
    "Licensed under CC BY-SA 4.0 via the SRAGI Regenerative License (SRL). "
    "See SRL-LICENSE.yaml for current version and details."
)

# Regex patterns that represent bad / legacy references
BAD_PATTERNS = [
    r"SRL v\d+(\.\d+)*",  # e.g., SRL v1.0, SRL v1.1, etc.
    r"CC BY[- ]?SA 4\.0.*SRL v\d+(\.\d+)*",
    r"CC BY 4\.0.*SRL v\d+(\.\d+)*",
]

# Directories that are allowed to use CC BY-SA (visuals etc.)
BYSA_DIRS = {"assets", "visuals", "sragi-skills"}


def clean_text(text: str, is_bysa_area: bool) -> str:
    """Replace outdated license strings with canonical references."""
    # Normalize CRLF → LF
    text = text.replace("\r\n", "\n")

    # Always strip version numbers
    text = re.sub(r"SRL v\d+(\.\d+)*", "SRL", text, flags=re.I)

    if is_bysa_area:
        # Replace BY-SA references with canonical BY-SA form (no version)
        text = re.sub(
            r"Licensed under CC BY[- ]?SA 4\.0.*SRL.*",
            CANONICAL_BYSA,
            text,
            flags=re.I,
        )
    else:
        # Replace any BY or BY-SA pattern with canonical BY form
        text = re.sub(
            r"Licensed under CC BY(?:-SA)? 4\.0.*SRL.*",
            CANONICAL_BY,
            text,
            flags=re.I,
        )
    return text


def main() -> int:
    print("🔍 Scanning repository for hardcoded SRL version references...\n")

    bad_hits = []
    files_checked = 0

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in FILETYPES:
            files_checked += 1
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception as e:
                print(f"⚠️  Could not read {path}: {e}")
                continue

            original = text
            is_bysa_area = any(part in BYSA_DIRS for part in path.parts)
            text = clean_text(text, is_bysa_area=is_bysa_area)

            if text != original:
                path.write_text(text, encoding="utf-8")

            for pat in BAD_PATTERNS:
                if re.search(pat, text, flags=re.I):
                    bad_hits.append(str(path))
                    break

    print(f"🧩 Files checked: {files_checked}")

    if bad_hits:
        print("\n❌ Found hardcoded SRL versions in:")
        for f in sorted(set(bad_hits)):
            print(f"  - {f}")
        print(
            "\n🛑 Fix or remove these references. "
            "All files must point to SRL-LICENSE.yaml as SSOT.\n"
        )
        return 1

    print("\n✅ All version references are clean and SSOT-compliant.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
