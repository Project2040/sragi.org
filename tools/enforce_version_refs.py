#!/usr/bin/env python3
"""SRAGI® SRLF 2.0 rights-reference enforcement.

The repository has no ecosystem-wide default license. This check prevents
legacy statements from silently reintroducing one and prevents hard-coded
SRLF version grants from being used as artifact licenses.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILETYPES = {".md", ".css", ".yaml", ".yml", ".xml", ".txt", ".py", ".json"}
SKIP_DIRS = {".git", "archive", "node_modules", "vendor"}

# Legacy claims that conflict with SRLF 2.0 artifact-level authority.
BAD_PATTERNS = {
    "ecosystem CC BY default": re.compile(
        r"(?:all content|everything|ecosystem|default(?:_license)?)"
        r".{0,100}CC[ -]?BY[ -]?4\.0",
        re.I | re.S,
    ),
    "legacy SRL license grant": re.compile(
        r"Licensed under CC BY 4\.0 via (?:the )?SRAGI Regenerative License",
        re.I,
    ),
    "versioned SRL grant": re.compile(
        r"(?:SRL|SRAGI Regenerative License)\s+v\d+(?:\.\d+)*",
        re.I,
    ),
}

ALLOWED_CONTEXT_FILES = {
    "SRL-LICENSE.yaml",  # may mention historical versions in history
}


def skipped(path: pathlib.Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def main() -> int:
    print("Scanning repository for legacy ecosystem-wide license grants...\n")
    hits = []
    checked = 0

    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in FILETYPES or skipped(path):
            continue
        checked += 1
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            print(f"WARNING: could not read {path}: {exc}")
            continue

        if path.name in ALLOWED_CONTEXT_FILES:
            continue

        for label, pattern in BAD_PATTERNS.items():
            if pattern.search(text):
                hits.append((str(path.relative_to(ROOT)), label))

    print(f"Files checked: {checked}")
    if hits:
        print("\nERROR: legacy licensing claims found:")
        for path, label in sorted(set(hits)):
            print(f"  - {path}: {label}")
        print(
            "\nSRLF 2.0 rule: the framework describes; the artifact grants. "
            "Attach an SPDX identifier/expression or rights statement to the artifact."
        )
        return 1

    print("\nOK: no legacy ecosystem-wide license grants detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
