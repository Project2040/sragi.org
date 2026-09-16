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
FILETYPES = {".md", ".css", ".yaml", ".yml", ".xml", ".txt", ".py", ".json", ".html", ".j2"}
# Historical records and test fixtures are not live policy. Standard license
# texts are checked separately against their pinned SPDX checksums.
SKIP_DIRS = {".git", "archive", "node_modules", "vendor", "__pycache__", "tests"}

# Legacy claims that conflict with SRLF 2.0 artifact-level authority.
BAD_PATTERNS = {
    "ecosystem CC BY default": re.compile(
        r"(?:all(?: SRAGI)? content|everything|all images|alt SRAGI-innhold)"
        r"[^\n]{0,150}(?:licens|lisens|distribut)[^\n]{0,80}CC[ -]?BY(?:[ -]?SA)?[ -]?4\.0"
        r"|(?:ecosystem[- ]wide default license|default_license)\s*[:=]\s*[\"']?CC[ -]?BY(?:[ -]?SA)?[ -]?4\.0",
        re.I,
    ),
    "legacy SRL license grant": re.compile(
        r"CC[ -]?BY(?:[ -]?SA)?[ -]?4\.0[^\n]{0,20}(?:via|\+)\s*(?:the )?(?:SRAGI Regenerative (?:Source )?License|SRL\b|SRAGI RSL)",
        re.I,
    ),
    "versioned SRL grant": re.compile(
        r"(?:SRL|SRAGI Regenerative License)[ -]*v?\d+(?:\.\d+)+",
        re.I,
    ),
}

ALLOWED_CONTEXT_FILES = {
    "SRL-LICENSE.yaml",  # may mention historical versions in history
}


def skipped(path: pathlib.Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)


def main() -> int:
    print("Scanning repository for legacy ecosystem-wide license grants...\n")
    hits = []
    checked = 0

    for path in ROOT.rglob("*"):
        if not path.is_file() or (path.suffix.lower() not in FILETYPES and path.name not in {"makefile", "gemini-sragi-bios-2025-1x1"}) or skipped(path):
            continue
        checked += 1
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:
            print(f"WARNING: could not read {path}: {exc}")
            continue

        if path.relative_to(ROOT).as_posix() in ALLOWED_CONTEXT_FILES:
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
