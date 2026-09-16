#!/usr/bin/env python3
"""Download canonical standard license texts used by SRLF 2.0.

Source: SPDX license-list-data. The custom SRAGI commercial LicenseRef is
maintained locally and is intentionally not overwritten by this tool.
"""

from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent.parent
LICENSES = ROOT / "LICENSES"
BASE = "https://raw.githubusercontent.com/spdx/license-list-data/main/text"

IDENTIFIERS = [
    "CC-BY-4.0",
    "CC-BY-SA-4.0",
    "AGPL-3.0-only",
    "Apache-2.0",
    "CC0-1.0",
]


def main() -> int:
    LICENSES.mkdir(parents=True, exist_ok=True)
    for identifier in IDENTIFIERS:
        url = f"{BASE}/{identifier}.txt"
        target = LICENSES / f"{identifier}.txt"
        print(f"Fetching {identifier} from SPDX license-list-data...")
        with urlopen(url, timeout=30) as response:
            content = response.read()
        target.write_bytes(content)
        print(f"  wrote {target.relative_to(ROOT)}")

    custom = LICENSES / "LicenseRef-SRAGI-Commercial.txt"
    if not custom.exists():
        raise SystemExit("Missing custom license reference: LICENSES/LicenseRef-SRAGI-Commercial.txt")

    print("Standard license texts synchronized. Custom LicenseRef preserved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
