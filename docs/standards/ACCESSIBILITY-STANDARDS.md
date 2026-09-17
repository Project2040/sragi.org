# ♿ SRAGI Accessibility & Testing Standards

**File:** `/docs/SRAGI-ACCESSIBILITY-TESTING-STANDARDS.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.1c
**Last Updated:** December 2025

**This standard need a quality evaluation to make it coherent in the SRAGI doc ecosystem
---

## 🧭 Purpose

This document defines the **accessibility, validation, and automated testing standards** for SRAGI.org and associated systems (Neptunia Media, SRAGI Elantrix, Muse API).
Its purpose is to ensure that SRAGI’s digital products are **inclusive, compliant, and maintain technical integrity** across codebases and platforms.

---

## 🌍 Accessibility Principles

SRAGI adopts **WCAG 2.2 AA** as a minimum standard for accessibility and emphasizes regenerative design that enhances usability for all.

### Core Principles

| Principle          | Description                                                           |
| ------------------ | --------------------------------------------------------------------- |
| **Perceivable**    | Information and UI must be visible and understandable to all users    |
| **Operable**       | All functionality must be accessible via keyboard and assistive tools |
| **Understandable** | Interfaces should follow predictable, consistent patterns             |
| **Robust**         | Compatible with modern browsers and assistive technologies            |

---

## 🪶 Content Accessibility Guidelines

### 1. Alt Text & Media

* All images must include descriptive `alt` attributes.
* Decorative images may use empty `alt=""`.
* Avoid generic descriptions like “image” or “photo.”
* Prefer context-aware descriptions: “Diagram of SRAGI Sync Loop architecture.”

### 2. ARIA Labels

* Use ARIA labels only when native HTML semantics are insufficient.
* Example:

  ```html
  <button aria-label="Open SRAGI license details">
    <svg>...</svg>
  </button>
  ```

### 3. Color Contrast

| Level          | Ratio | Recommendation                   |
| -------------- | ----- | -------------------------------- |
| **Minimum**    | 4.5:1 | Standard text                    |
| **Enhanced**   | 7:1   | Important content or UI elements |
| **Large Text** | 3:1   | Font size ≥ 18pt or 14pt bold    |

Use tools like **Contrast Checker** or **axe-core** to verify compliance.

### 4. Typography

* Base font size: `16px` (1rem)
* Use relative units (`em`, `rem`) for scalability.
* Maintain consistent line-height (1.5–1.7 for readability).

### 5. Semantic HTML

* Use `<main>`, `<header>`, `<footer>`, `<nav>` appropriately.
* Avoid `<div>` or `<span>` where semantic tags exist.
* Tables must have headers (`<th>`) and captions.

---

## 🧩 Keyboard Navigation

All interactive elements must:

* Be reachable via `Tab` navigation.
* Show visible focus indicators.
* Support `Enter` and `Space` actions.

**Tip:** Use `:focus-visible` in CSS for accessible focus styling.

Example:

```css
button:focus-visible {
  outline: 2px solid var(--color-primary);
  outline-offset: 3px;
}
```

---

## 🔍 Testing Standards Overview

SRAGI maintains a **test-first philosophy** — validation and linting are part of every CI workflow.

| Category                | Tool / Method            | Purpose                                               |
| ----------------------- | ------------------------ | ----------------------------------------------------- |
| **Markdown Linting**    | `markdownlint`           | Ensures consistent heading and code block structure   |
| **YAML Validation**     | `yamllint`               | Checks schema consistency and indentation             |
| **JSON Schema**         | `jsonlint` or `ajv`      | Validates API responses and configs                   |
| **SVG Optimization**    | `svgo`                   | Removes unnecessary metadata and ensures clean markup |
| **Link Checking**       | `markdown-link-check`    | Detects broken internal/external links                |
| **Accessibility Audit** | `axe-core`, `lighthouse` | Evaluates WCAG compliance                             |

---

## 🧪 Planned Feature: Automated Testing Workflow

GitHub Actions run tests automatically on push and pull requests:

```
.github/workflows/VALIDATE-DOCS.yaml
```

### Example Workflow

```yaml
name: Validate Docs and Accessibility
on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main, dev]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Lint Markdown
        run: npx markdownlint '**/*.md'
      - name: Validate YAML
        run: yamllint .
      - name: Validate JSON
        run: npx jsonlint-cli '**/*.json'
      - name: Optimize SVG
        run: npx svgo -f assets/images/
```

---

## 🧱 Accessibility Checklist (Manual Review)

| Area     | Check                                      |
| -------- | ------------------------------------------ |
| Images   | All include meaningful `alt` text          |
| Links    | Descriptive text, no bare URLs             |
| Headings | Logical hierarchy, no skipped levels       |
| Forms    | Labeled inputs, keyboard accessible        |
| Media    | Captions and transcripts provided          |
| Contrast | Meets 4.5:1 minimum                        |
| Motion   | Avoid autoplay animations without controls |

---

## 🧰 Developer Tools

| Purpose             | Tool                                         |
| ------------------- | -------------------------------------------- |
| Browser Testing     | Chrome DevTools / Firefox Accessibility Pane |
| Color Contrast      | WebAIM Contrast Checker                      |
| Screen Reader       | NVDA (Windows), VoiceOver (macOS)            |
| Keyboard Simulation | Accessibility Insights / TabNav              |

---

## 🌐 Internationalization & RTL Support

* Language codes must be included in `<html lang="en">` or `<html lang="no">`.
* Translation strategy follows the SRAGI Content Sync Protocol. Language variants are stored as suffix-files (e.g., page-nb.md) or within SSOT YAML nodes (title_no), synchronized to WordPress via WPML.
* Ensure UI mirrors correctly in RTL (if implemented).
* Use ISO 639-1 codes only.

---

## 🔒 Continuous Validation Philosophy

> “Validation is not about perfection — it’s about integrity.”

SRAGI’s continuous integration enforces validation in all commits:

* Every push triggers **linting**, **schema validation**, and **link checking**.
* Broken links or YAML errors block merges.
* Accessibility reports are attached to PR summaries.

---

## 🪄 Summary

The **SRAGI Accessibility & Testing Standards** ensure that all products and documentation are:

* **Inclusive** – accessible to everyone
* **Validated** – syntactically and semantically correct
* **Resilient** – continuously checked for errors
* **Aligned** – with regenerative design ethics

> “Accessibility is regeneration made visible.”
> — SRAGI Human-Centered Design Philosophy

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC-BY-4.0.
The stated artifact license applies to this document. Framework: https://sragi.org/licensing/.
