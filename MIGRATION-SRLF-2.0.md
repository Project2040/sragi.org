# SRLF 2.0 Migration Checklist

## Completed on migration branch

- [x] Replace ecosystem-default licensing with artifact-level rights authority.
- [x] Set `ecosystem_default_license: null`.
- [x] Set `No license grant should be inferred.`
- [x] Normalize and complete `SRL-LICENSE.yaml` as pure YAML.
- [x] Add 2026–2036+ evolution and repository-file policies.
- [x] Separate maximally open machine access from legal license grants.
- [x] Replace legacy `ai-policy.txt` with rights-discovery semantics.
- [x] Replace legacy AI-policy XML and universal license XML semantics.
- [x] Simplify `robots.txt` to technical access/discovery.
- [x] Add `LicenseRef-SRAGI-Commercial.txt`.
- [x] Add contributor-rights framework.
- [x] Rewrite license builder/generators for SRLF 2.0.
- [x] Add validation for core SRLF invariants and required license files.
- [x] Replace legacy default-license enforcement script.
- [x] Rewrite repository README and documentation licensing standard.
- [x] Replace legacy `_CONFIG` redirect semantics.
- [x] Add SPDX standard-license synchronization tool.
- [x] Regenerate human-readable framework, JSON, XML and HTML summaries on branch.

## Required before merge

- [ ] Materialize canonical standard SPDX license texts under `LICENSES/` by running `python tools/sync_spdx_license_texts.py` in a checkout with network access.
- [ ] Run `python automation/license_builder/build_licenses.py` after the standard texts exist and commit any deterministic output changes.
- [ ] Run `python tools/enforce_version_refs.py` and resolve remaining live-document legacy grants.
- [ ] Validate YAML, JSON and XML in CI/local checkout.
- [ ] Review remaining live documentation for obsolete SRL 1.x terminology.
- [ ] Legal review of `LicenseRef-SRAGI-Commercial.txt` and contributor-rights language before production publication.
- [ ] Confirm canonical web endpoint `/licensing/` exists before deployment.

## Core invariant

**Framework describes; artifact grants.**

Machine access is maximally open. Rights remain artifact-specific.
