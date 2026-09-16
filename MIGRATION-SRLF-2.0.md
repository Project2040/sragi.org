# SRLF 2.0 Migration Checklist

## Completed on migration branch

- [x] Replace legacy ecosystem-default model with artifact-level rights authority.
- [x] Set `ecosystem_default_license: null`.
- [x] Set unspecified-artifact rule: no license grant should be inferred.
- [x] Normalize `SRL-LICENSE.yaml` to pure YAML.
- [x] Complete repository map and 2026–2036+ evolution policy.
- [x] Separate maximally open machine access from legal license grants.
- [x] Replace legacy `ai-policy.txt` grants with rights-discovery semantics.
- [x] Simplify `robots.txt` to technical access/discovery.
- [x] Add `LicenseRef-SRAGI-Commercial.txt`.
- [x] Add contributor-rights framework.
- [x] Rewrite license builder for SRLF 2.0 fields.
- [x] Add validation for core SRLF invariants and required license files.
- [x] Replace legacy default-license enforcement script.
- [x] Rewrite repository README and documentation licensing standard.
- [x] Replace legacy `_CONFIG` redirect semantics.
- [x] Add SPDX standard-license synchronization tool.

## Required before merge

- [ ] Materialize the five canonical standard SPDX license texts under `LICENSES/` by running `python tools/sync_spdx_license_texts.py`.
- [ ] Run `python automation/license_builder/build_licenses.py` and commit regenerated outputs.
- [ ] Run `python tools/enforce_version_refs.py` and resolve remaining live-document legacy grants.
- [ ] Validate generated YAML/JSON/XML outputs.
- [ ] Review remaining live documentation for obsolete SRL 1.x terminology.
- [ ] Review `LicenseRef-SRAGI-Commercial.txt` and contributor-rights language before production publication.
- [ ] Confirm canonical web endpoint `/licensing/` exists before merge/deployment.

## Core invariant

**Framework describes; artifact grants.**

Machine access is maximally open. Rights remain artifact-specific.
