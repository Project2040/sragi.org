# RSL 1.0 deployment

Repository generation and live deployment are separate checks. PR #9 restores the repository implementation; it does not deploy WordPress or establish live RSL conformance.

## Publish together

- Serve the generated `content/license/LICENSE-RSL.xml` at `https://sragi.org/content/license/LICENSE-RSL.xml` with `Content-Type: application/rsl+xml` (an optional charset is fine).
- Serve the generated `content/license/WEBSITE-LICENSE.html` at the policy URL configured in the master. The root RSL record refers to this conditional CC-BY website policy, including artifact-specific and third-party exceptions.
- Publish the generated root `robots.txt`, including its global `License:` URL, `User-agent: *`, the named crawler groups and their empty `Disallow:` directives.
- Serve the two licensed source files at the exact paths recorded in `RESOURCE_LICENSE_MANIFEST.yaml`. The `$` in RSL means an exact path match; it is not part of the HTTP URL.
- On Apache, deploy the adjacent `.htaccess` with the XML file. Its `ForceType` rule targets only `LICENSE-RSL.xml`. If overrides are disabled, or another server/CDN serves the file, configure the equivalent response header there. A filename or XML declaration cannot set the HTTP media type.

The root RSL record uses `payment type="attribution"` and references the exception-bearing website policy in both `standard` and `terms`. This preserves CC-BY credit requirements without monetary payment. RSL's `free` token would also remove attribution requirements. The root record does not point the whole domain directly at the CC-BY legal code. No license server, registration, token or crawler fee is required. The two additional RSL entries apply to static Markdown source documents at exact paths. They do not assert that their WordPress counterparts contain identical material.

Preserve visible artifact-specific notices on products, downloads and third-party components. Confirm URL and license mappings before adding individual WordPress resources to the manifest. A site-wide discovery link must point to the conditional website policy/RSL file; do not label every resource unconditionally CC-BY when exceptions exist.

## Verify after an approved deployment

1. Request `/robots.txt` and confirm the generated `License:` URL and open directives for the wildcard and all named crawlers. Check whether origin/CDN access controls permit these requests too.
2. Request the RSL URL: confirm HTTP 200, `application/rsl+xml`, the RSL namespace and the expected three content records: one website-policy fallback and two exact artifact records. Request the policy URL and confirm that its CC-BY default and exceptions are served together. Check through the actual public CDN as well as the origin configuration.
3. Request both source URLs and compare their SHA-256 hashes with the manifest. Confirm that the actual served files contain the license notices used by the generator.
4. Run the [official RSL validator](https://rslstandard.org/validate) against the published URL and review any findings. The local project validator covers our narrow standard-license profile; it is not the official validator or a certification service.
5. Check representative website pages and separately licensed products for the correct visible notices. Inspect indexing controls, canonical URLs and sitemap discovery, then verify actual search-engine indexing separately. Open robots directives express permission; they do not establish that indexing has occurred.

The build checks file structure, evidence, scope and discovery configuration offline. Live HTTP status, headers, CDN behavior and WordPress mappings remain unverified until this deployment check is completed.

References: [RSL specification, including sections 2.2 and 4.4](https://rslstandard.org/rsl), [standard licenses](https://rslstandard.org/guide/standard-licenses).
