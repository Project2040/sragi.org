# 📝 SRAGI Markdown & Documentation Standards

**File:** `/docs/SRAGI-DOCUMENTATION-STANDARDS.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.0
**Last Updated:** October 2025

---

## 🧭 Purpose

This document defines the **Markdown, formatting, and documentation structure standards** for SRAGI.org and associated repositories.
It ensures consistency, clarity, and interoperability across GitHub, WordPress (Bricks Builder), and AI-integrated systems.

---

## 🧩 Markdown Structure

### 1. Heading Levels

| Level  | Usage                   | Example                   |
| ------ | ----------------------- | ------------------------- |
| `#`    | Document title          | `# SRAGI License System`  |
| `##`   | Major section           | `## Purpose`              |
| `###`  | Subsection              | `### Workflow Steps`      |
| `####` | Minor detail (optional) | `#### Inline SVG example` |

**Rules:**

* Start all documents with a single `#` H1 title.
* Do **not** skip heading levels (no jumping from H2 → H4).
* Each section must have a **unique, descriptive** title.

---

### 2. Text Emphasis

* Use `**bold**` for key terms, commands, and warnings.
* Use `_italic_` for emphasis, quotes, or external titles.
* Use blockquotes `>` for contextual commentary or philosophy notes.

Example:

```markdown
> “Give more than you take.” — SRAGI Principle #1
```

---

### 3. Code Blocks

Use **fenced code blocks** with language identifiers:

````markdown
```yaml
meta:
  version: 1.0
  license: CC-BY-4.0
````

````

✅ Preferred: triple backticks + language tag (yaml, json, php, html, md)  
❌ Avoid: indented code blocks (breaks in WordPress & AI renderers)

Inline code should use single backticks: `` `like_this` ``.

---

### 4. Links & References

Use **relative links** within the repository, and **absolute links** externally.

Examples:
```markdown
[SRAGI License System](../licensing/SRAGI-LICENSE-SYSTEM.md)
[Neptunia Media AS](https://neptuniamedia.org)
````

**Guidelines:**

* Use descriptive link text (no “click here”).
* Always verify internal links after restructuring.
* Avoid trailing slashes for GitHub markdown links.

---

### 5. Lists & Tables

* Use hyphens (`-`) for unordered lists.
* Use `1.` for ordered lists.
* Tables should include header separators (`|---|`).

Example:

```markdown
| File | Purpose |
|------|----------|
| SRL-LICENSE.yaml | Source of truth for license metadata |
| LICENSE-RSL.xml | Machine-readable output |
```

---

## 🧾 License Headers (All Files)

Every file in SRAGI repositories should begin with a **license header**:

### Markdown / YAML Example:

```yaml
# ===========================================================
#  SRAGI PROJECT — Regenerative AI Framework
#  © 2025 Rune Solberg / Neptunia Media AS
#  Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0
#  Source: https://sragi.org/license
# ===========================================================
```

### PHP / JS / CSS Example:

```php
/* ===========================================================
 *  SRAGI PROJECT — Regenerative AI Framework
 *  © 2025 Rune Solberg / Neptunia Media AS
 *  Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0
 *  Source: https://sragi.org/license
 * =========================================================== */
```

**Rules:**

* Must appear at the top of every source or documentation file.
* Use consistent version tag (e.g., SRL v1.0).
* Always include project name, copyright, and license link.

---

## 📚 Documentation Structure

Each document should follow a consistent logical order:

```
# Title

**File / Maintainer / Version / Date**

---

## Purpose

## Architecture / Process / Concept

## Implementation / Workflow

## Related Files / References

## License Footer
```

### Example Layout

```markdown
# SRAGI Elantrix Core

**File:** `/docs/ELANTRIX-CORE.md`  
**Maintainer:** Rune Solberg  
**Version:** 1.0  
**Updated:** October 2025

---

## Purpose
Define the internal AI orchestration layer for SRAGI Elantrix Core.

## Architecture
Explain Elantrix-Core modules and Muse API integration.

## References
[SRAGI-CONVENTIONS.md](../SRAGI-CONVENTIONS.md)
```

---

## 🔗 Cross-Referencing & Navigation

* Use relative links between documents: `../folder/filename.md`.
* Add a **Back to Index** link at the bottom of long documents.
* Use consistent anchors for major sections: `(#purpose)`, `(#workflow)`.
* Interlink related docs using a “See Also” section.

Example:

```markdown
### See Also
- [SRAGI-CONVENTIONS.md](../SRAGI-CONVENTIONS.md)
- [SRAGI-LICENSE-SYSTEM.md](../licensing/SRAGI-LICENSE-SYSTEM.md)
```

---

## 📖 README Template

Each directory should have a simple `README.md` file with:

1. **Title + short description**
2. **File list (with links)**
3. **Purpose of the folder**
4. **Link back to root documentation**

Example:

```markdown
# SRAGI Licensing Documentation

This folder contains all documents related to SRL and licensing workflows.

## Files
- [SRAGI-LICENSE-SYSTEM.md](SRAGI-LICENSE-SYSTEM.md)
- [SRL-VERSIONS.yaml](SRL-VERSIONS.yaml)

---
[← Back to /docs/](../README.md)
```

---

## 🧠 Version Indicators in Docs

Every major document includes version metadata in the header block:

```markdown
**Version:** 1.0  
**Last Updated:** 2025-10-24
```

Minor edits that do not change the meaning do **not** require a new version number — only an updated date.

---

## 🧩 File Cross-Linking & Front-Matter (Optional)

Some documents may include YAML front-matter for AI processing:

```yaml
---
version: 1.0
author: Rune Solberg
date: 2025-10-24
license: CC-BY-4.0
related:
  - SRAGI-CONVENTIONS.md
  - SRAGI-LICENSE-SYSTEM.md
---
```

This allows future automation (e.g., building docs indexes, AI summarization, or WP integration).

---

## 🌊 Summary

The **SRAGI Markdown & Documentation Standards** ensure that all written content is:

* **Readable and structured** across all platforms
* **Legally consistent** through uniform headers
* **Machine-interpretable** for future AI workflows
* **Visually coherent** across SRAGI.org and Neptunia Media

> “Documentation is not bureaucracy — it’s living architecture.”
> — SRAGI Documentation Philosophy

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0
