# SRLF 2.0 Migration Checklist

## Completed on migration branch

- [x] Replace ecosystem-default licensing with artifact-level rights authority.
- [x] Set `ecosystem_default_license: null` and `No license grant should be inferred.`
- [x] Normalize and complete `SRL-LICENSE.yaml` as pure YAML.
- [x] Add 2026–2036+ evolution and repository-file policies.
- [x] Separate maximally open machine access from legal license grants.
- [x] Replace legacy TXT/XML machine policies and universal license XML semantics.
- [x] Simplify `robots.txt` to technical access/discovery.
- [x] Add `LicenseRef-SRAGI-Commercial.txt` and contributor-rights framework.
- [x] Rewrite builder/generators for SRLF 2.0 and add invariant validation.
- [x] Replace legacy default-license enforcement script.
- [x] Rewrite repository README and documentation licensing standard.
- [x] Replace legacy `_CONFIG` redirect semantics.
- [x] Add SPDX standard-license synchronization tool and license-directory provenance README.
- [x] Align generated human-readable, XML, HTML, TXT and sitemap outputs with the v2 generator.

## Required before merge

- [ ] Materialize canonical standard SPDX license texts under `LICENSES/` by running `python tools/sync_spdx_license_texts.py` in a checkout with network access.
- [ ] Run `python automation/license_builder/build_licenses.py` after the standard texts exist and commit deterministic output changes.
- [ ] Run `python tools/enforce_version_refs.py` and resolve remaining live-document legacy grants.
- [ ] Validate YAML, JSON and XML in CI/local checkout.
- [ ] Review remaining live documentation for obsolete SRL 1.x terminology.
- [ ] Legal review of `LicenseRef-SRAGI-Commercial.txt` and contributor-rights language before production publication.
- [ ] Confirm canonical web endpoint `/licensing/` exists before deployment.

## Branch state

Migration branch is intentionally ahead of `main` and PR #9 remains draft. Do not merge until the release gates above pass.

## Core invariant

**Framework describes; artifact grants.**

Machine access is maximally open. Rights remain artifact-specific.
