# RSL 1.0 deployment

Repository generation and live deployment are separate checks. The SRLF 2.0.1 migration is merged through PR #10, including PR #9; this does not deploy WordPress or establish live RSL conformance.

## Publish together

- Serve the generated `content/license/LICENSE-RSL.xml` at `https://sragi.org/content/license/LICENSE-RSL.xml` with `Content-Type: application/rsl+xml` (an optional charset is fine).
- Serve the generated `content/license/WEBSITE-LICENSE.html` at the policy URL configured in the master. The root RSL record refers to this conditional CC-BY website policy, including artifact-specific and third-party exceptions.
- Publish the generated root `robots.txt`, including its global `License:` URL and one `User-agent: *` group with an empty `Disallow:` directive. Named crawlers belong in AI/machine policy only; do not add separate robots groups.
- Publish the remaining public generated outputs: `ai-policy.txt`, `content/license/ai-policy.xml`, `content/license/license.json`, `content/license/index.html`, `content/license/REGENERATIVE_LICENSE.md` and the reviewed sitemap. Make the commercial reference available through its commercial information route and repository/package; the master does not require a separate public `/LICENSES/` file URL. The generated `docs/_CONFIG/SRL-LICENSE.yaml` is repository compatibility metadata, not a required website endpoint.
- Map `/licensing/` to the current overview and make `/commercial-licensing/` serve the current commercial information and contact. These WordPress routes are not created by the repository generator. Preserve the CMS's other sitemap entries when integrating licensing discovery.
- Redirect the legacy `/LICENSE-RSL.xml` and `/ai-policy.xml` routes to their current `/content/license/` counterparts, or serve exactly the same current bytes and media types there. Do not leave an older licensing policy reachable through these aliases.
- Serve the two licensed source files at the exact paths recorded in `RESOURCE_LICENSE_MANIFEST.yaml`. The `$` in RSL means an exact path match; it is not part of the HTTP URL.
- On Apache, deploy the adjacent `.htaccess` with the XML file. Its `ForceType` rule targets only `LICENSE-RSL.xml`. If overrides are disabled, or another server/CDN serves the file, configure the equivalent response header there. A filename or XML declaration cannot set the HTTP media type.

The root RSL record uses `payment type="attribution"` and references the exception-bearing website policy in both `standard` and `terms`. This preserves CC-BY credit requirements without monetary payment. RSL's `free` token would also remove attribution requirements. The root record does not point the whole domain directly at the CC-BY legal code. No license server, registration, token or crawler fee is required. The two additional RSL entries apply to static Markdown source documents at exact paths. They do not assert that their WordPress counterparts contain identical material.

Preserve visible artifact-specific notices on products, downloads and third-party components. Confirm URL and license mappings before adding individual WordPress resources to the manifest. A site-wide discovery link must point to the conditional website policy/RSL file; do not label every resource unconditionally CC-BY when exceptions exist.

Review server/CDN-injected `X-License`, `X-License-URL`, `X-AI-Policy`, `Link` and HTML license links. Remove or qualify unconditional site-wide CC-BY claims; each assertion must respect artifact and third-party exceptions. Canonical discovery URLs must reference the current files. Existing live headers may be configured outside this repository.

Stage the complete release first. At cutover, update policy files, source documents, aliases, WordPress routes and headers as one coordinated release, then purge the affected origin/CDN caches. The observed legacy TXT/Markdown responses can retain a 30-day cache lifetime; uploading a file alone does not clear those cached copies. Keep a restorable copy of the prior site configuration and files.

## Verify after an approved deployment

1. Request `/robots.txt` and confirm the generated global `License:` URL and one open wildcard group, which covers named and unknown crawlers. Check whether origin/CDN access controls permit these requests too.
2. Request the RSL URL: confirm HTTP 200, `application/rsl+xml`, the RSL namespace and the expected three content records: one website-policy fallback and two exact artifact records. Request the policy URL and confirm that its CC-BY default and exceptions are served together. Check through the actual public CDN as well as the origin configuration.
3. Request both source URLs and compare their SHA-256 hashes with the manifest. Confirm that the actual served files contain the license notices used by the generator.
4. Run the [official RSL validator](https://rslstandard.org/validate) against the published URL and review any findings. The local project validator covers our narrow standard-license profile; it is not the official validator or a certification service.
5. Check representative website pages and separately licensed products for the correct visible notices. Inspect indexing controls, canonical URLs and sitemap discovery, then verify actual search-engine indexing separately. Open robots directives express permission; they do not establish that indexing has occurred.

The build checks file structure, evidence, scope and discovery configuration offline. Live HTTP status, headers, CDN behavior and WordPress mappings remain unverified until this deployment check is completed.

Run the read-only release probe before and after cutover:

```sh
python tools/check_licensing_deployment.py --output /tmp/sragi-licensing-http-check.json
```

It checks public generated files, manifest source hashes, legacy aliases, HTTP status, media types and basic content on the two licensing portals. Network failures are reported as unverified. It does not send email, publish files, purge caches, prove mailbox delivery, inspect private origin settings or replace the official RSL validator. HTML/Markdown on WordPress requires its own visual and content review. The static sitemap byte check assumes that the repository sitemap is deployed as-is; if the CMS integrates the same URLs into a larger sitemap, review that intentional difference separately rather than discarding the rest of the CMS sitemap.

References: [RSL specification, including sections 2.2 and 4.4](https://rslstandard.org/rsl), [standard licenses](https://rslstandard.org/guide/standard-licenses).
