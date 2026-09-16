# Resource license manifest

The manifest is a scoped discovery and review register, not a repository-wide license grant. Each entry identifies an exact repository path. Omission does not assign a license; the express website policy independently supplies the fallback for eligible public sragi.org content without another notice.

- `license_expression`: an explicitly verified SPDX expression, or `null` when unresolved. Never infer `OR` or `AND` from conflicting notices.
- `observed_notices`: identifiers and locations already present on the artifact; these are evidence, not a new license choice.
- `status`: `needs_rights_review`, `scoped_notices_preserved`, or `explicit_license_verified`.
- `commercial_relicensing_verified`: `false` until a sufficient rights chain is documented. Open licensing alone does not establish authority to offer alternative commercial terms.
- `reviewed_source_commit`: fixes the evidence snapshot so later edits cannot erase its context.

Additional fields and artifact classes are permitted. An approved license decision should record its authority, scope and affected version. Keep historical grants and third-party rights intact.

## RSL export

The master additionally generates one site-level `/` record pointing to `website_licensing.policy_url`. This record has a free access policy, without a license server. Its standard and terms URL identifies the conditional website policy, including the CC BY default and all artifact/third-party exceptions. It does not directly assign CC BY to every URL. Artifact records below remain independently verified overrides; unmatched website content follows the website policy rather than the manifest's completeness.

Only records with an explicit `rsl_path` are selected for RSL export. They must have `status: explicit_license_verified`, a full-file `source_sha256`, and an exact license notice matching `license_expression` in the source. Changes to the source require renewed review of the evidence hash. An unresolved record with an export path fails the build.

The initial profile supports exact static file paths: `rsl_path` is `/` plus the URL-encoded repository path plus a terminal `$`. Directory scopes, wildcards, duplicate scopes and guessed WordPress routes are rejected. The two initial entries describe existing CC-BY-4.0 notices; they do not select new licenses. Their HTTP availability is a deployment check.

The reviewed mappings are CC-BY-4.0 and CC-BY-SA-4.0 to their canonical Creative Commons URLs, using RSL's standard-license attribution form. The canonical instruction dual expression can also be represented when commercial relicensing rights are verified: RSL Core carries the CC-BY-SA-4.0 path, and a SRAGI extension preserves the complete SPDX expression. No second core license or payment requirement is added, because RSL combines applicable terms rather than expressing SPDX `OR`. Commercial rights still require an applicable agreement.

Other expressions fail export until an appropriate mapping is reviewed. This is an implementation limit, not a restriction on the framework's future artifact classes or licensing options. Entries without `rsl_path` retain their existing review-only role.

Contact: licensing@sragi.org. Framework: https://sragi.org/licensing/.
