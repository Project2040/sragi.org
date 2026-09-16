# SRAGI.org — Regenerative AI Framework

> **Documentation is not bureaucracy — it is living architecture.**

This repository contains public SRAGI.org content, licensing infrastructure, documentation architecture and automation.

## Licensing architecture

SRAGI uses **artifact-level licensing** under the **SRAGI® Regenerative Licensing Framework (SRLF) 2.0**.

There is **no ecosystem-wide default license**. The license identifier, SPDX expression, rights statement or applicable agreement attached to an individual artifact determines the rights for that artifact.

**Core rule:** `No license grant should be inferred.`

SRAGI instruction frameworks may use the dual-license expression:

```text
CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial
```

Commercial activity alone does not require the commercial path. The **SRAGI® Commercial Suite License** provides an alternative path where different or additional terms or rights are required.

Canonical licensing portal: https://sragi.org/licensing/

## Machine access

Public SRAGI resources are **maximally open for technical discovery** by search engines, AI systems, research crawlers and other machine agents.

```text
Machine access: *
Rights authority: artifact
```

Technical crawling, indexing, retrieval or discovery does not independently grant copyright or other intellectual-property rights. Machine policy files exist for access and rights discovery; they are not universal license grants.

See [`ai-policy.txt`](ai-policy.txt) and [`robots.txt`](robots.txt).

## Repository map

```text
sragi.org/
├── SRL-LICENSE.yaml                 # SRLF 2.0 licensing architecture
├── LICENSES/                        # Standard license texts + SRAGI LicenseRef
├── ai-policy.txt                    # Machine rights discovery
├── robots.txt                       # Technical crawler access
├── content/license/                 # Generated/human-readable licensing material
├── docs/                            # Documentation and architecture
├── automation/license_builder/      # SRLF artifact generators
└── tools/                           # Validation and enforcement
```

## Rights chain

Third-party rights are preserved. Neptunia Media AS can grant only rights it owns, controls or is authorized to license. Contributions intended for commercially dual-licensed artifacts require sufficient rights for that commercial path.

See [`content/license/SRAGI_CLA.md`](content/license/SRAGI_CLA.md).

## Regenerative layer

**Give more than you take.**

For open-license artifacts this is a regenerative invitation, not an additional restriction imposed on the open license. A separate commercial agreement may expressly define binding regenerative commitments.

## Automation

The license builder reads [`SRL-LICENSE.yaml`](SRL-LICENSE.yaml) and generates machine-readable and human-readable rights-discovery artifacts. Generated files must preserve the distinction between:

1. technical access;
2. rights discovery; and
3. legal license grants.

Run `python automation/license_builder/build_licenses.py` to rebuild, and add `--check` to verify checked-in output without writing files. CI runs the check and regression tests on pull requests and branch pushes; it does not commit generated changes automatically. See [CONTRIBUTING.md](CONTRIBUTING.md) for commands.

[`LICENSE-RSL.xml`](content/license/LICENSE-RSL.xml) uses **Really Simple Licensing 1.0**, with the standard `https://rslstandard.org/rsl` namespace. `robots.txt` advertises it through the RSL `License:` directive while retaining open crawler access. SPDX identifies licenses; RSL represents and exposes artifact-specific terms; SRLF 2.0 describes the framework. These are separate roles and version numbers.

The initial RSL projection covers the two explicitly CC-BY-4.0-licensed Regenerative Principles source documents at their exact static repository paths. It does not license the entire domain or assume that WordPress pages contain the same material. Source hashes and explicit notices are checked before export. Unresolved entries are excluded; unsupported license mappings fail instead of selecting a default. SRAGI metadata lives in its own XML namespace. A future verified dual-license entry exports its open standard-license path and preserves its full SPDX expression as metadata; it does not turn a commercial reference into a grant.

The builder validates this limited RSL profile against the [RSL 1.0 specification](https://rslstandard.org/rsl) and its [standard-license form](https://rslstandard.org/guide/standard-licenses). These project checks are not official RSL certification. See [RSL deployment](content/license/RSL_DEPLOYMENT.md) for HTTP requirements and the remaining live-site verification.

The [resource manifest](content/license/RESOURCE_LICENSE_MANIFEST.yaml) records two pre-existing conflicting document notices requiring review. It does not silently resolve or relicense them. Unchanged historical license grants are not revoked by this migration.

## Contributing

Before contributing, review the documentation standards and contributor-rights framework. Every publishable artifact should carry its applicable license expression or rights statement; do not assume a repository-wide license.

## Organization

SRAGI® is developed and stewarded by **Neptunia Media AS**.

Licensing: licensing@sragi.org  
Website: https://sragi.org/  
Repository: https://github.com/Project2040/sragi.org

© 2024-2026 Neptunia Media AS
