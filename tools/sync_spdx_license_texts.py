#!/usr/bin/env python3
"""Download canonical standard license texts used by SRLF 2.0.

Source: SPDX license-list-data. The custom SRAGI commercial LicenseRef is
maintained locally and is intentionally not overwritten by this tool.
"""

import hashlib
import json
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
LICENSES = ROOT / "LICENSES"
LOCK_FILE = LICENSES / "SPDX-SOURCES.json"

IDENTIFIERS = [
    "CC-BY-4.0",
    "CC-BY-SA-4.0",
    "AGPL-3.0-only",
    "Apache-2.0",
    "CC0-1.0",
]


def main() -> int:
    lock = json.loads(LOCK_FILE.read_text(encoding="utf-8"))
    LICENSES.mkdir(parents=True, exist_ok=True)
    downloaded = {}
    for identifier in IDENTIFIERS:
        record = lock['licenses'][identifier]
        url = record['url']
        print(f"Fetching {identifier} from SPDX license-list-data...")
        with urlopen(url, timeout=30) as response:
            content = response.read()
        if hashlib.sha256(content).hexdigest() != record['sha256']:
            raise SystemExit(f"Checksum mismatch for {identifier}; no texts were changed")
        downloaded[identifier] = content

    custom = LICENSES / "LicenseRef-SRAGI-Commercial.txt"
    if not custom.exists():
        raise SystemExit("Missing custom license reference: LICENSES/LicenseRef-SRAGI-Commercial.txt")

    # Replace only after every pinned download has been verified.
    for identifier, content in downloaded.items():
        target = LICENSES / f"{identifier}.txt"
        target.write_bytes(content)
        print(f"  wrote {target.relative_to(ROOT)}")

    print("Standard license texts synchronized. Custom LicenseRef preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
