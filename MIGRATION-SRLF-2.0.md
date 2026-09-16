# SRLF 2.0 migration review

## Technical implementation

- Pure YAML master with artifact rights authority and no ecosystem-wide default.
- Five canonical SPDX license texts materialized from pinned revision `16f3aa6c3bdd62e50f8b1cf618f32d2a510250ee`, with SHA-256 verification.
- Deterministic generator for eight Markdown, HTML, JSON, XML, TXT and sitemap outputs.
- Non-mutating `--check` detects stale output. YAML duplicate keys and fences, missing/altered texts and broken licensing invariants fail validation.
- Complete JSON master representation, including SPDX machine-readable settings and future fields.
- Open crawler access retained; AI policy preserves artifact authority, attribution guidance and the neutral position on AI training and adaptation.
- Old unused v1 templates removed; Git history retains them.
- Explicit existing CC-BY and CC-BY-SA notices retained at artifact level; old SRL wrappers and blanket claims removed from live documents and metadata.
- Source and output checks run in GitHub Actions on Node 24 actions. CI is read-only and no longer auto-commits generated changes.
- Eight regression tests cover grant boundaries, propagation/escaping, determinism, duplicate YAML, license integrity, drift detection and guard false positives.

## Local validation

The source was read through the GitHub connector at commit `529b9a5e3964f10fe1464dbe817ab51913c4ae47`. All 115 text files were retrieved; existing binary assets were left unchanged in the remote base tree.

- Builder and `--check`: passed for all eight generated outputs.
- SPDX checksums: all five standard texts passed.
- Legacy-reference guard: passed.
- Regression suite: 8/8 passed.
- Changed/new structured files at validation: 37 YAML/workflow files, 2 JSON files and 3 XML files parsed successfully.

## Required review before merge

1. **Conflicting existing notices:** `docs/core/ETHICAL-CONTACT-PROTOCOL.md` and `docs/standards/VISUAL-PROTOCOL.md` each carried CC-BY-SA-4.0 in the header and CC-BY-4.0 in the footer. Both were preserved and registered; no OR expression or new license choice was invented.
2. **Different scoped notices:** The PHP snippet in `BUNNY-CDN-INTEGRATION.md` carries CC-BY-SA-4.0, while the surrounding document carries CC-BY-4.0. These scopes remain separate.
3. **Commercial/contributor instruments:** The commercial LicenseRef is a routing/reference document, not an executed commercial agreement. The CLA file is a contributor-rights notice, not evidence that a contributor has signed. Review these alongside the intended agreements and provenance records.
4. **Output and deployment review:** Confirm wording and the actual serving of `/licensing/`, policy files and licensing contact before website deployment. Repository changes do not establish WordPress routes or email mailboxes.

PR #9 remains draft for this review. No merge or WordPress deployment is performed by this migration.
