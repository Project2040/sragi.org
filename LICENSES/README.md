# SRAGI® License Files

This directory contains license texts referenced by SRAGI artifacts.

## Standard SPDX licenses

The canonical text files for these standard identifiers are synchronized from the public `spdx/license-list-data` repository using `tools/sync_spdx_license_texts.py`:

- `CC-BY-4.0.txt`
- `CC-BY-SA-4.0.txt`
- `AGPL-3.0-only.txt`
- `Apache-2.0.txt`
- `CC0-1.0.txt`

The exact upstream revision and SHA-256 checksums are recorded in `SPDX-SOURCES.json`. Do not hand-edit standard license texts. The builder fails if a required text is missing, empty or changed. The sync tool downloads that pinned revision and verifies every text before replacing files.

## SRAGI custom reference

`LicenseRef-SRAGI-Commercial.txt` is maintained by Neptunia Media AS. It identifies the alternative SRAGI® Commercial Suite licensing path. Its presence does not itself grant commercial-license rights.

## Release preparation

Run from repository root:

```bash
python -m pip install -r automation/license_builder/requirements.txt
python automation/license_builder/build_licenses.py
python automation/license_builder/build_licenses.py --check
python tools/enforce_version_refs.py
python -m unittest discover -s tests
```

Then review and commit the generated diff before merging a licensing release.

Standard license texts are checked in; ordinary builds do not fetch them from the network. Run `python tools/sync_spdx_license_texts.py` only to restore the pinned copies.

Canonical licensing portal: https://sragi.org/licensing/
