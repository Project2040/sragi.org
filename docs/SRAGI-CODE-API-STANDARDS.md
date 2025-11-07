# 💻 SRAGI Code & API Standards

**File:** `/docs/SRAGI-CODE-API-STANDARDS.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.0
**Last Updated:** October 2025

---

## 🧭 Purpose

This document defines **code formatting, YAML/JSON structure, API conventions, and integration patterns** for the SRAGI.org ecosystem.
It ensures consistency between configuration, PHP logic, frontend code, and AI data interfaces (Elantrix, Muse, SureCart, WPCodeBox, etc.).

---

## ⚙️ YAML Formatting Standards

| Rule            | Description                                           | Example                 |
| --------------- | ----------------------------------------------------- | ----------------------- |
| **Indentation** | 2 spaces (no tabs)                                    | `meta:\n  version: 1.0` |
| **Quotes**      | Only when needed (for special chars or leading zeros) | `'01'`                  |
| **Lists**       | Hyphen + space (`- item`)                             | `- version: 1.0`        |
| **Comments**    | Begin with `#`, aligned to left margin                | `# Example of comment`  |
| **Line width**  | Max 100 chars                                         | —                       |

Example:

```yaml
meta:
  version: 1.01
  license: CC-BY-4.0
permissions:
  - usage: all
  - modification: allowed
```

**Validation:**

* Use `yamllint` or VSCode YAML plugin for schema validation.
* Avoid inline YAML in Markdown except for front-matter.

---

## 🧩 JSON Structure Standards

| Rule                | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **Indentation**     | 2 spaces                                                                |
| **Quotes**          | Double quotes only                                                      |
| **Keys**            | Use `snake_case` for API responses, `camelCase` for JS internal objects |
| **Trailing commas** | Never allowed                                                           |
| **Top-level type**  | Must be object `{}` not array `[]` for consistency                      |

Example:

```json
{
  "version": "1.0",
  "license": "CC-BY-4.0",
  "author": {
    "name": "Rune Solberg",
    "organization": "Neptunia Media AS"
  }
}
```

---

## 🧱 PHP Code Standards

| Aspect          | Standard                                                         | Example |
| --------------- | ---------------------------------------------------------------- | ------- |
| **Indentation** | 4 spaces                                                         |         |
| **Braces**      | K&R style (open on same line)                                    |         |
| **Naming**      | `snake_case` for functions, `SCREAMING_SNAKE_CASE` for constants |         |
| **Functions**   | One purpose per function; max 30 lines                           |         |
| **Docblocks**   | Required for all public functions                                |         |

Example:

```php
/**
 * Generate SRAGI license XML from YAML.
 * @param string $yaml_file Path to YAML file.
 * @return string XML string.
 */
function generate_license_xml($yaml_file) {
    $data = yaml_parse_file($yaml_file);
    return array_to_xml($data);
}
```

---

## ⚡ JavaScript Standards

| Aspect       | Standard                                          |
| ------------ | ------------------------------------------------- |
| **Syntax**   | ES6+ with `const`/`let`                           |
| **Naming**   | `camelCase` for variables and functions           |
| **Imports**  | Group external imports first, internal last       |
| **Comments** | Use `//` for short notes, `/** ... */` for blocks |
| **Async**    | Prefer async/await over promises                  |

Example:

```js
import { fetchLicense } from './utils/license.js';

async function updateLicenseView() {
  const data = await fetchLicense('/api/license.json');
  document.querySelector('#license').innerHTML = data.license;
}
```

---

## 🎨 CSS Standards

| Aspect        | Standard                                                          |
| ------------- | ----------------------------------------------------------------- |
| **Naming**    | BEM (`block__element--modifier`)                                  |
| **Units**     | `rem` for spacing, `em` for typography, `%` for responsive widths |
| **Variables** | Use CSS custom properties for color + spacing                     |
| **Comments**  | Group sections clearly                                            |

Example:

```css
:root {
  --color-primary: #14854f;
  --spacing-md: 1.5rem;
}

.header__nav--active {
  color: var(--color-primary);
  margin-top: var(--spacing-md);
}
```

---

## 🌐 API Design Standards

SRAGI APIs are designed to be **REST-like** with structured JSON responses and clear versioning.

### Base Format

```
/api/v1/{resource}/{id?}
```

### Example Endpoint

```
GET /api/v1/license
```

Response:

```json
{
  "status": "success",
  "data": {
    "license": "CC-BY-4.0",
    "source": "https://sragi.org/license"
  }
}
```

### Response Rules

| Rule         | Description                                    |
| ------------ | ---------------------------------------------- |
| `status`     | Always include (`success`, `error`, `warning`) |
| `data`       | Primary payload container                      |
| `message`    | Human-readable explanation                     |
| `error_code` | Optional integer for automation                |
| `timestamp`  | ISO 8601 UTC timestamp                         |

### Error Example

```json
{
  "status": "error",
  "message": "License file not found.",
  "error_code": 404,
  "timestamp": "2025-10-24T12:05:32Z"
}
```

---

## 🧠 AI Integration Guidelines

SRAGI’s APIs are designed to be parsed by AI (Elantrix Core, Muse API, external LLMs).
Therefore:

* Include explicit metadata fields (`version`, `license`, `author`)
* Prefer JSON over XML for AI consumption
* YAML → JSON conversion handled in workflows
* Keep consistent key naming (lowercase, underscores)

---

## 🧩 API Documentation Template

Each API should have a companion Markdown document in `/docs/api/`:

```markdown
# GET /api/v1/license

**Purpose:** Return the current SRL license metadata.

## Request
```

GET /api/v1/license

````

## Response
```json
{
  "status": "success",
  "data": { ... }
}
````

## Notes

* Requires no authentication.
* Cached for 5 minutes.

```

---

## 🔒 Security & Validation

| Area | Standard |
|------|-----------|
| **Input Validation** | Sanitize all user input, even internal APIs |
| **Authentication** | Use HMAC or token-based verification for internal sync |
| **Rate Limiting** | Protect endpoints with request caps (if public) |
| **CORS** | Restrict origins to trusted domains |

---

## 📦 File & Folder Structure

```

/wordpress/wpcodebox/
├── sragi_api_license.php
├── sragi_api_status.php
├── sragi_helpers.php
└── sragi_security.php

```

All API endpoints:
- Start with `sragi_api_`
- Return valid JSON (`application/json` header)
- Include version metadata in the response

---

## 🪄 Summary

The **SRAGI Code & API Standards** unify all development efforts under one consistent, safe, and machine-friendly framework:

- Consistent formatting across YAML, JSON, PHP, JS, CSS  
- REST-like, AI-parseable API structures  
- Safe security patterns and validation flows  
- Predictable conventions for WordPress and Bricks integration

> “Code is the architecture of consciousness — let it be clean.”  
> — SRAGI Engineering Philosophy

---

**© 2025 Rune Solberg / Neptunia Media AS**  
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.

```
