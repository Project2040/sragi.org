# Working content templates

`SRL-LICENSE.yaml` registers the templates, website licensing policy, organization and crawler configuration. Template files contain placeholders and layout; they do not select an open license independently. The builder checks this separation, and the regression suite renders every registered template.

## Create website content

Save author-supplied values in a YAML file, for example `values.yaml`:

```yaml
title: Example article
slug: example-article
date: "2026-09-16"
publication_context:
  url: https://sragi.org/example-article/
  public: true
  rights_verified: true
  third_party: false
```

`rights_verified` records the author's confirmation that SRAGI owns or has sufficient rights to apply the website policy. Do not set it merely because a resource is publicly accessible.

```sh
python tools/new_content.py --template basic --values values.yaml --output content/pages/example-article.yaml --for-publication
```

With no separate artifact terms, eligible public website content inherits the license configured in `website_licensing.default_spdx`. The output records the selected SPDX identifier, `status: inherited`, the policy URL and `resolved_from: website_licensing`. The template itself contains no fixed SPDX choice.

Supply `license.spdx` or `license.rights_statement` in the values file when an artifact has separate terms. Those terms take precedence. Third-party material, private resources and other domains do not inherit the website default through this tool. Conflicting legacy `license.type` and `license.spdx` values fail validation.

## Create separately licensed products

Use `--template product` with `id`, `title`, `version` and explicit license metadata. For an artifact actually offered through the dual-license path, values can include:

```yaml
id: example-framework
title: Example framework
version: "1.0"
license:
  spdx: CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial
```

The product profile never inherits website licensing. Choose the expression appropriate to that artifact and verify the commercial rights chain before offering the commercial alternative. Rendering metadata neither grants missing contributor rights nor executes a commercial agreement.

## Template inputs and validation

The registered names are `basic`, `editorial`, `visual` and `product`. Each `{{ input.NAME }}` placeholder requires that exact key in the values file; the editorial template retains its uppercase field names and takes an explicit `author_id`. Organization and policy placeholders resolve from the master. YAML values retain their types, and quoted or multiline text is serialized safely.

Without `--for-publication`, unresolved licensing can remain in a draft. With it, missing artifact terms and missing website eligibility stop creation. Existing output files are never overwritten.

This command creates YAML metadata. It does not create article prose or images, validate every editorial/SEO field, publish to WordPress, or establish indexing. The CMS/Loom publication integration must call the same resolution/validation logic before publication; repository CI alone cannot inspect every live website resource.

Change policy in the master, then rebuild with `python automation/license_builder/build_licenses.py`. Edit layout in the registered template files. The generator's robots and website-policy templates are likewise registered under `publication.templates`.
