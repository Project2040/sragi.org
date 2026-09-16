# SRAGI® License Files

This directory contains license texts referenced by SRAGI artifacts.

## Standard SPDX licenses

The canonical text files for these standard identifiers are synchronized from the public `spdx/license-list-data` repository using `tools/sync_spdx_license_texts.py`:

- `CC-BY-4.0.txt`
- `CC-BY-SA-4.0.txt`
- `AGPL-3.0-only.txt`
- `Apache-2.0.txt`
- `CC0-1.0.txt`

Do not hand-edit synchronized standard license texts. The SRLF 2.0 builder intentionally fails release validation if any required standard text is missing.

## SRAGI custom reference

`LicenseRef-SRAGI-Commercial.txt` is maintained by Neptunia Media AS. It identifies the alternative SRAGI® Commercial Suite licensing path. Its presence does not itself grant commercial-license rights.

## Release preparation

Run from repository root:

```bash
python tools/sync_spdx_license_texts.py
python automation/license_builder/build_licenses.py
python tools/enforce_version_refs.py
```

Then review and commit the generated diff before merging a licensing release.

Canonical licensing portal: https://sragi.org/licensing/
