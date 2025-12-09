# 📝 SRAGI Markdown & Documentation Standards

**File:** `/docs/SRAGI-DOCUMENTATION-STANDARDS.md`

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.2

**Last Updated:** December 2025

---

## 🧭 Purpose

This document defines the **Markdown, formatting, and documentation structure standards** for SRAGI.org.
It ensures consistency between GitHub (Kairos) and WordPress (Chronos) via the **Content Sync Engine**.

---

## 🧩 Core Markdown Structure

### 1. Heading Levels

| Level  | Usage                   | Example                   |
| ------ | ----------------------- | ------------------------- |
| `#`    | **Page Title (H1)** | `# What is SRAGI?`        |
| `##`   | **Major Section (H2)** | `## Core Principles`      |
| `###`  | **Subsection (H3)** | `### The Fractal Nature`  |
| `####` | **Detail (H4)** | `#### Implementation`     |

**Strict Rules:**
* **One H1 per file:** The `# Title` must match `title_en` in the YAML frontmatter.
* **No skipping:** Do not jump from H2 to H4.
* **Sentence Case:** Use "Core principles", not "CORE PRINCIPLES".

---

## ⚙️ Frontmatter (The Brain)

Every content file (`.md`) **MUST** have a YAML frontmatter block defining its identity.
This is the source code for the Sync Engine.

```yaml
---
meta:
  type: documentation
  title: "Page Title"
  slug: "page-slug"
ia:
  pillar: "sragi-os"
  parent: "about"
sync:
  auto_publish: true
```
*See content-template.md.yaml for the full schema.*

---

## **🌐 Language & File Structure (Twin-File Strategy)**

We use a **Sibling File** approach for multilingual content to ensure clean git diffs.

| Language | Filename Pattern | Example |
| :---- | :---- | :---- |
| **English (Master)** | \[slug\].md | what-is-sragi.md |
| **Norwegian** | \[slug\]-nb.md | what-is-sragi-nb.md |
| **YAML Controller** | \[slug\].yaml | what-is-sragi.yaml |

**Rule:** The English file is the structure master. The Norwegian file mirrors the structure (headings) of the English file exactly.

---

## **🎨 Text Formatting**

### **Emphasis**

* **Bold:** \*\*text\*\* for concepts and UI elements.  
* *Italic:* \_text\_ for emphasis or foreign words.  
* Code: \`text\` for file paths, variables, or technical terms.

### **Admonitions (Callouts)**

Use blockquotes with specific prefixes to create styled boxes in Bricks:

Markdown

```
> **Note:** This is a general note.

> **Warning:** Be careful with this setting.

> **Tip:** Try using the CLI for speed.
```

### **Lists**

* Use \- for unordered lists.  
* Use 1\. for ordered lists.

---

## **🖼️ Visuals & Media**

Refer to **SRAGI Visual Protocol v1.1** for full details.

In Markdown:

Always use the relative path from the content root, or the absolute path for stability.

Markdown

```
![Epic alt text describing the latent space](../assets/images/visuals/hero/gemini-nebula-2025-16x9-content.avif)
```

*   
  **Alt Text:** Mandatory. Must describe the concept, not just the pixels.  
* **Format:** Prefer .avif or .webp.

---

## **🔗 Links**

* **Internal (Docs):** Relative links (../setup/install.md).  
* **Internal (Site):** Absolute paths (/about/what-is-sragi).  
* **External:** Full URL (https://example.com).

---

## **🪄 Summary**

* **YAML** defines the context.  
* **Markdown** defines the content.  
* **Git** tracks the truth.

“Documentation is not bureaucracy — it’s the living memory of the system.”

---

© 2025 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL).

See SRL-LICENSE.yaml for details.
