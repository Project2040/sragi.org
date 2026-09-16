# RSL 1.0 deployment

Repository generation and live deployment are separate checks. PR #9 restores the repository implementation; it does not deploy WordPress or establish live RSL conformance.

## Publish together

- Serve the generated `content/license/LICENSE-RSL.xml` at `https://sragi.org/content/license/LICENSE-RSL.xml` with `Content-Type: application/rsl+xml` (an optional charset is fine).
- Publish the generated root `robots.txt`, including its global `License:` URL, `User-agent: *`, and empty `Disallow:`.
- Serve the two licensed source files at the exact paths recorded in `RESOURCE_LICENSE_MANIFEST.yaml`. The `$` in RSL means an exact path match; it is not part of the HTTP URL.
- On Apache, deploy the adjacent `.htaccess` with the XML file. Its `ForceType` rule targets only `LICENSE-RSL.xml`. If overrides are disabled, or another server/CDN serves the file, configure the equivalent response header there. A filename or XML declaration cannot set the HTTP media type.

Do not attach a site-wide HTTP/HTML `rel="license"` association to unreviewed resources. WordPress pages, translations, downloads and embedded third-party material need verified URL and license mappings before adding them to the manifest. The initial two RSL entries apply to static Markdown source documents, not automatically to their rendered website counterparts.

## Verify after an approved deployment

1. Request `/robots.txt` and confirm the generated `License:` URL and open access directives.
2. Request the RSL URL: confirm HTTP 200, `application/rsl+xml`, the RSL namespace and the expected two content records. Check the response through the actual public CDN as well as the origin configuration.
3. Request both source URLs and compare their SHA-256 hashes with the manifest. Confirm that the actual served files contain the license notices used by the generator.
4. Run the [official RSL validator](https://rslstandard.org/validate) against the published URL and review any findings. The local project validator covers our narrow standard-license profile; it is not the official validator or a certification service.

The build checks file structure, evidence, scope and discovery configuration offline. Live HTTP status, headers, CDN behavior and WordPress mappings remain unverified until this deployment check is completed.

References: [RSL specification, including sections 2.2 and 4.4](https://rslstandard.org/rsl), [standard licenses](https://rslstandard.org/guide/standard-licenses).
