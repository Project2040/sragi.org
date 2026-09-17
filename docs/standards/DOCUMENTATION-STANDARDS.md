# 📝 SRAGI Markdown & Documentation Standards

**File:** `/docs/standards/DOCUMENTATION-STANDARDS.md`

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 2.0

**Last Updated:** September 2026

---

## 🧭 Purpose

This document defines Markdown, formatting, documentation metadata and licensing-reference standards for SRAGI.org.

---

## 🧩 Core Markdown Structure

### 1. Heading Levels

| Level | Usage | Example |
| --- | --- | --- |
| `#` | Page Title (H1) | `# What is SRAGI?` |
| `##` | Major Section (H2) | `## Core principles` |
| `###` | Subsection (H3) | `### The fractal nature` |
| `####` | Detail (H4) | `#### Implementation` |

**Strict rules:**
- One H1 per file.
- Do not skip heading levels.
- Use sentence case unless a proper name requires otherwise.

---

## ⚙️ Frontmatter

Content files should carry machine-readable identity metadata where the publishing pipeline uses it. Use the applicable content schema rather than inventing file-specific fields.

### Licensing metadata

SRLF 2.0 has **no ecosystem-wide default license**. Every publishable SRAGI artifact should identify its applicable license, SPDX expression, rights statement or governing terms.

For dual-licensed SRAGI instruction YAML, the canonical expression is:

```text
CC-BY-SA-4.0 OR LicenseRef-SRAGI-Commercial
```

For other artifacts, select the license appropriate to that artifact. Do not copy the instruction-framework expression onto software, articles, schemas or third-party material unless it actually applies.

Eligible public sragi.org content without a different notice inherits the explicit website license defined in `SRL-LICENSE.yaml → website_licensing`. A specific artifact notice takes precedence, and third-party rights are preserved. Outside that website scope, **no license grant should be inferred**. Content templates reference the master policy; separately licensed products require explicit terms. See `CONTENT-TEMPLATES.md` for the working generation and licensing-validation commands.

Canonical licensing portal: https://sragi.org/licensing/

---

## 🌐 Language & File Structure

Where sibling language files are used, keep their semantic structure aligned while allowing natural translation.

| Language | Filename Pattern | Example |
| --- | --- | --- |
| English | `[slug].md` | `what-is-sragi.md` |
| Norwegian | `[slug]-nb.md` | `what-is-sragi-nb.md` |
| YAML controller | `[slug].yaml` | `what-is-sragi.yaml` |

---

## 🎨 Text Formatting

- **Bold:** concepts and UI elements.
- *Italic:* emphasis or foreign words.
- `Code`: file paths, variables, identifiers and technical terms.
- Use `-` for unordered lists and `1.` for ordered lists.

### Callouts

```markdown
> **Note:** General information.

> **Warning:** A material risk or constraint.

> **Tip:** Practical guidance.
```

---

## 🖼️ Visuals & Media

- Alt text is mandatory where meaningful.
- Prefer efficient modern formats such as AVIF or WebP where supported.
- Preserve provenance and applicable rights information for third-party media.

---

## 🔗 Links

- Repository documentation: prefer stable relative links where appropriate.
- Site links: use canonical SRAGI URLs.
- External sources: use full canonical URLs.

---

## 🪄 Summary

- YAML carries structured context.
- Markdown carries human-readable content.
- Git carries version history.
- The artifact carries its rights.
- SRLF describes the licensing architecture; it does not silently license every artifact.

> Documentation is not bureaucracy — it is the living memory of the system.

---

© 2024-2026 Neptunia Media AS

License: see the artifact-specific SPDX identifier, license expression or rights statement.  
Licensing framework: https://sragi.org/licensing/
