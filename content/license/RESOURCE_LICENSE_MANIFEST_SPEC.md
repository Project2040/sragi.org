# Resource license manifest

The manifest is a scoped discovery and review register, not a repository-wide license grant. Each entry identifies an exact repository path. Omission has no licensing effect.

- `license_expression`: an explicitly verified SPDX expression, or `null` when unresolved. Never infer `OR` or `AND` from conflicting notices.
- `observed_notices`: identifiers and locations already present on the artifact; these are evidence, not a new license choice.
- `status`: `needs_rights_review` or `scoped_notices_preserved` in the initial register.
- `commercial_relicensing_verified`: `false` until a sufficient rights chain is documented. Open licensing alone does not establish authority to offer alternative commercial terms.
- `reviewed_source_commit`: fixes the evidence snapshot so later edits cannot erase its context.

Additional fields and artifact classes are permitted. An approved license decision should record its authority, scope and affected version. Keep historical grants and third-party rights intact.

Contact: licensing@sragi.org. Framework: https://sragi.org/licensing/.
