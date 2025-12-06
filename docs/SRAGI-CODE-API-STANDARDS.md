# 💻 SRAGI Code & API Standards

**File:** `/docs/SRAGI-CODE-API-STANDARDS.md`

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.1

**Last Updated:** December 2025

---

## 🧭 Purpose

This document defines **code formatting, YAML/JSON structure, API conventions, and integration patterns** for the SRAGI.org ecosystem.
It serves as both an internal standard for development and a **roadmap for our public API**, ensuring consistency, security, and AI-interoperability.

---

## ⚙️ YAML Formatting Standards (SSOT)

YAML is our "Source of Truth". It must be human-readable and machine-parseable.

| Rule            | Description                                           | Example                 |
| --------------- | ----------------------------------------------------- | ----------------------- |
| **Indentation** | 2 spaces (no tabs)                                    | `meta:\n  version: 1.0` |
| **Quotes** | Only when needed (for special chars or leading zeros) | `'01'`                  |
| **Lists** | Hyphen + space (`- item`)                             | `- version: 1.0`        |
| **Line width** | Max 100 chars                                         | —                       |

**Validation:**
* Use `yamllint` or VSCode YAML plugin.
* **Principle:** YAML updates trigger automated builds (e.g., License XML).

---

## 🧩 JSON Structure Standards (The Output)

JSON is our "Delivery Format" for APIs and AI consumption.

| Rule                | Description                                                             |
| ------------------- | ----------------------------------------------------------------------- |
| **Indentation** | 2 spaces                                                                |
| **Quotes** | Double quotes only                                                      |
| **Keys** | Use `snake_case` for API responses                                      |
| **Trailing commas** | Never allowed                                                           |
| **Top-level type** | Must be object `{}` not array `[]` for extensibility                    |

Example:

```json
{
  "meta": {
    "version": "1.0",
    "generated_at": "2025-12-06T12:00:00Z"
  },
  "data": {
    "license": "CC-BY-4.0",
    "author": "Rune Solberg"
  }
}
```
---
# 💻 SRAGI Code & API Standards

**File:** `/docs/SRAGI-CODE-API-STANDARDS.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.1
**Last Updated:** December 2025

---

## 🧭 Purpose

This document defines **code formatting, YAML/JSON structure, API conventions, and integration patterns** for the SRAGI.org ecosystem.
It ensures consistency between configuration, PHP logic (WPCodeBox), frontend code, and AI data interfaces.
It serves as both an internal standard and a **roadmap for our public API**.

---

## ⚙️ YAML Formatting Standards (SSOT)

YAML is our "Source of Truth". It must be human-readable and machine-parseable.

| Rule            | Description                                           | Example                 |
| --------------- | ----------------------------------------------------- | ----------------------- |
| **Indentation** | 2 spaces (no tabs)                                    | `meta:\n  version: 1.0` |
| **Quotes** | Only when needed (for special chars or leading zeros) | `'01'`                  |
| **Lists** | Hyphen + space (`- item`)                             | `- version: 1.0`        |
| **Line width** | Max 100 chars                                         | —                       |

**Validation:**
* Use `yamllint` or VSCode YAML plugin.
* **SSOT Principle:** YAML files in GitHub are the Single Source of Truth.

## **🌐 API Design Standards (The Roadmap)**

This section defines how we expose SRAGI to the world. We build on the **WordPress REST API** infrastructure but enforce strictness for AI-readability.

### **Base Namespace**

All SRAGI endpoints live here:

```
[https://sragi.org/wp-json/sragi/v1/](https://sragi.org/wp-json/sragi/v1/){resource}
```

*(Note: Matches definition in SRAGI-WEB-BIOS-v2.1.yaml)*

### **Core Endpoints (Vision)**

| Method | Endpoint | Purpose |
| :---- | :---- | :---- |
| GET | /license | Returns current SRL metadata (XML/JSON links) |
| GET | /ontology | Returns the Knowledge Graph (Pillars, Domains) |
| GET | /token/{id} | Returns metadata for a specific Visual Token |

### **Response Format (Envelope)**

Every response must follow this envelope to be predictable for AI agents:

JSON

```
{
  "status": "success",
  "meta": {
    "api_version": "1.0",
    "timestamp": "2025-12-06T12:00:00Z"
  },
  "data": { ... }
}
```

---

## **🧠 AI Integration Guidelines**

SRAGI APIs are designed to be consumed by Elantrix, Muse, and external LLMs.

1. **Self-Describing:** API responses should include context (what is this data?).  
2. **Metadata Keys:** Use consistent keys defined in BIOS (e.g., knowledge\_graph, actor\_types).  
3. **Hypermedia:** Where possible, link to related resources (e.g., original\_link for images).

---

## **🧩 Documentation Template**

Every public endpoint needs a Markdown definition in /docs/api/:

Markdown

````
# GET /wp-json/sragi/v1/license

**Purpose:** Return the current SRL license metadata for automated compliance checks.

## Response Example
```json
{
  "status": "success",
  "data": {
    "license": "CC-BY-4.0",
    "source": "https://sragi.org/license"
  }
}
````

---

## **🔒 Security & Validation**

| Area | Standard |
| :---- | :---- |
| **Public Read** | GET requests for content/license are open (CORS enabled) |
| **Private Write** | POST/PUT requires Bearer Token or Nonce (Admin only) |
| **Input Validation** | Sanitize all user input, even internal APIs |
| **Rate Limiting** | Protect endpoints with request caps |

---

## **🪄 Summary**

The **SRAGI Code & API Standards** unify development under a **WordPress-Native** but **System-Agnostic** philosophy:

* **YAML** is the Brain (SSOT).  
* **PHP** is the Muscle (Sync Engine).  
* **JSON** is the Voice (Public API).

“Code is the architecture of consciousness — let it be clean, open, and regenerative.”

— SRAGI Engineering Philosophy

---

© 2025 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).

See SRL-LICENSE.yaml for details.






