# SRLF 2.0 migration review

## Technical implementation

- Pure YAML master with artifact rights authority, an explicit conditional CC-BY website default and no ecosystem-wide default.
- Five canonical SPDX license texts materialized from pinned revision `16f3aa6c3bdd62e50f8b1cf618f32d2a510250ee`, with SHA-256 verification.
- Deterministic generator for nine Markdown, HTML, JSON, XML, TXT and sitemap outputs, including the exception-bearing website license policy.
- Non-mutating `--check` detects stale output. YAML duplicate keys and fences, missing/altered texts and broken licensing invariants fail validation.
- Complete JSON master representation, including SPDX machine-readable settings and future fields.
- Open crawler access retained; AI policy preserves artifact authority, attribution guidance and the neutral position on AI training and adaptation.
- Old unused v1 templates removed; Git history retains them.
- Explicit existing CC-BY and CC-BY-SA notices retained at artifact level; old SRL wrappers and blanket claims removed from live documents and metadata.
- Source and output checks run in GitHub Actions on Node 24 actions. CI is read-only and no longer auto-commits generated changes.
- Nineteen regression tests cover grant boundaries, propagation/escaping, determinism, duplicate YAML, license integrity, drift detection, guard false positives, the RSL standard-license profile, website inheritance, named/wildcard crawler access and working content templates.

## Website openness clarification

The owner confirmed that public sragi.org content is CC-BY-4.0 by default unless otherwise marked, within Neptunia Media AS's rights. This is an express website grant; it is not an ecosystem-wide license for all SRAGI products or repositories. Specific artifact terms, existing grants and third-party rights remain authoritative.

- RSL includes a root record pointing to the conditional website policy, with attribution and no monetary fee. Its core `standard` and `terms` references carry the exceptions even when a client ignores SRAGI extensions. The two verified source-document records remain available separately. RSL payment semantics are derived from the configured license mapping; CC BY uses `attribution`, since `free` would also waive attribution.
- Named crawler groups are generated from the master alongside `*`; the list is not exclusive. AI/search access has no crawler fee, registration or token requirement. Content use follows the applicable open or artifact-specific license.
- Content templates are registered in the master and rendered by `tools/new_content.py`. Eligible website content inherits the configured default; explicit terms win, and the product profile requires explicit terms. Missing licensing information stops the tool's publication-validation mode.
- Business policy values and crawler names reside in the master. Generator presentation uses registered templates; tests exercise configuration changes without editing Python code. Protocol syntax and validation constraints remain in code.
- CMS publication and indexing verification remain separate integration/deployment work, as described in the [deployment check](content/license/RSL_DEPLOYMENT.md).

## RSL regression corrected

The earlier migration replaced Really Simple Licensing with custom XML while retaining the `LICENSE-RSL.xml` filename and removed the robots `License:` directive. The previous eight tests missed that interoperability regression; one even prohibited the discovery directive. That check has been replaced.

- RSL 1.0 root and namespace restored, separately versioned from SRLF 2.0.
- Global `License:` discovery restored without changing open crawling.
- The first repair projected two explicitly licensed source documents using the official standard-license form, exact paths and verified SHA-256 evidence. The subsequent owner clarification adds the conditional website fallback described above.
- SRAGI metadata separated into its own namespace. Open-license terms remain intelligible to a core-only RSL reader. No AI-use permission tokens or commercial acquisition requirements are invented.
- Regression tests reject custom/wrong namespaces, incorrect RSL versions, unsupported core elements, added broad permissions, license substitutions, lost discovery, broad scopes and unresolved/changed source evidence. Dual-license mapping preserves the open path and requires commercial provenance.
- Apache MIME configuration and a [deployment check](content/license/RSL_DEPLOYMENT.md) added. The public server/CDN and official online validator remain deployment checks, not claims established by local tests.

## Local validation

The source was read through the GitHub connector at commit `529b9a5e3964f10fe1464dbe817ab51913c4ae47`. All 115 text files were retrieved; existing binary assets were left unchanged in the remote base tree.

- Builder and `--check`: passed for all nine generated outputs after the website-policy clarification.
- SPDX checksums: all five standard texts passed.
- Legacy-reference guard: passed.
- Regression suite: 19/19 passed after the website-policy clarification (12 tests at the earlier RSL correction).
- At the earlier RSL repair, 37 YAML/workflow files, 2 JSON files and 3 XML files parsed successfully. Current checks also render all four registered content templates and validate the generated XML/JSON.

## Required review before merge

1. **Conflicting existing notices:** `docs/core/ETHICAL-CONTACT-PROTOCOL.md` and `docs/standards/VISUAL-PROTOCOL.md` each carried CC-BY-SA-4.0 in the header and CC-BY-4.0 in the footer. Both were preserved and registered; no OR expression or new license choice was invented.
2. **Different scoped notices:** The PHP snippet in `BUNNY-CDN-INTEGRATION.md` carries CC-BY-SA-4.0, while the surrounding document carries CC-BY-4.0. These scopes remain separate.
3. **Commercial/contributor instruments:** The commercial LicenseRef is a routing/reference document, not an executed commercial agreement. The CLA file is a contributor-rights notice, not evidence that a contributor has signed. Review these alongside the intended agreements and provenance records.
4. **Output and deployment review:** Confirm wording and the actual serving of `/licensing/`, policy files and licensing contact before website deployment. Repository changes do not establish WordPress routes or email mailboxes.

PR #9 remains draft for this review. No merge or WordPress deployment is performed by this migration.
