# 💻 SRAGI Code & API Standards

**File:** `/docs/standards/CODE-API-STANDARDS.md`

**Status:** PRODUCTION STANDARD

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.2 (Ecosystem-Ready)

**Last Updated:** December 2025

---

## 🧭 Purpose

This document defines **code formatting, YAML/JSON structure, API conventions, and integration patterns** for the entire SRAGI & Neptunia ecosystem.

It ensures consistency between:
* **SSOT Files** (`_CONFIG/*.yaml`)
* **Backend Logic** (Python Loom / PHP Refinery)
* **Public Interfaces** (REST APIs / AI Feeds)

**Core Philosophy:** "Code is the architecture of consciousness — let it be clean, open, and regenerative."

---

## ⚙️ 1. YAML Formatting (The Brain)
*YAML is our Source of Truth. All configuration lives here.*

| Rule | Standard | Example |
| :--- | :--- | :--- |
| **Indentation** | 2 spaces (NO tabs) | `meta:\n  version: 1.0` |
| **Keys** | `snake_case` mandatory | `qa_status`, `published_at` |
| **Quotes** | Only when needed (special chars/zeros) | `'01'`, `"2025-12-08"` |
| **Lists** | Hyphen + space | `- item` |
| **Validation** | `yamllint` / VSCode plugin | — |

**Normative Sources:**
* `TAXONOMY_GRAPH.yaml` (The Ontology)
* `VALIDATION_RULES.yaml` (The Logic)
* `CONTENT-TEMPLATE.yaml` (The Structure)
* `SRL-LICENSE.yaml` (The Law)

> **Rule:** Code reads YAML. Code never hardcodes rules.

---

## 🐍 2. Python Standards (The Logic)
*Python scripts (Loom Engine, Bridges, Validators) must be robust.*

| Area | Standard |
| :--- | :--- |
| **Version** | Python 3.10+ |
| **Formatting** | **Black** (Line length 88). No debates. |
| **Type Hinting** | **Mandatory** (`def func(a: int) -> bool:`). |
| **Docstrings** | Google Style. Readable by AI. |
| **Imports** | Sorted: StdLib → Third Party → Local. |

---

## 🐘 3. PHP Standards (The Muscle)
*PHP scripts (WordPress, Mission Control) handle data transport.*

| Area | Standard |
| :--- | :--- |
| **Style** | **PSR-12**. |
| **Security** | Always verify `nonce`. Sanitize input, escape output. |
| **Naming** | `camelCase` for internal logic, `snake_case` for DB keys. |

---

## 🧩 4. JSON & Data Transport (The Voice)
*JSON is our delivery format for APIs and AI consumption.*

* **Top Level:** Always Object `{}` (never Array `[]`).
* **Keys:** `snake_case`.
* **No Trailing Commas.**

### Standard Envelopes

✅ **Success Response:**
```json
{
  "status": "success",
  "meta": {
    "api_version": "1.0",
    "timestamp": "2025-12-09T12:00:00Z",
    "source": "SRAGI OS"
  },
  "data": {
    "id": "system-thinking",
    "type": "pillar",
    "content": "..."
  }
}
````

❌ **Error Response:**

JSON

```
{
  "status": "error",
  "meta": { "api_version": "1.0", "timestamp": "..." },
  "error": {
    "code": "invalid_taxonomy",
    "message": "The term 'magic' does not exist in 'sragi_pillars'.",
    "details": { "field": "pillar", "expected_source": "TAXONOMY_GRAPH.yaml" }
  }
}
```

---

## **🌐 5\. API Design Architecture**

*How the Neptunia Ecosystem talks to the world.*

### **Namespaces**

Each product has its own namespace, following the same pattern:

* https://sragi.org/wp-json/sragi/v1/{resource}  
* https://lurevalg.no/wp-json/lurevalg/v1/{resource}

### **Core Endpoints (Vision)**

| Method | Endpoint | Purpose |
| :---- | :---- | :---- |
| GET | /license | Returns current SRL metadata. |
| GET | /ontology | Returns the Knowledge Graph (Pillars). |
| GET | /token/{id} | Returns metadata for a Visual Token. |

### **AI Integration**

* **Self-Describing:** Responses include context (meta block).  
* **Stable IDs:** Slugs (system-thinking) never change.  
* **Hypermedia:** Include original\_link for images and related for content.

---

## **🔒 6\. Security & Integrity**

1. **Public Read:** GET requests for content/license are open (CORS enabled).  
2. **Private Write:** POST/PUT requires **Application Passwords** or **Bearer Token**.  
3. **Rate Limiting:** Protect endpoints against scraping abuse.  
4. **SSOT Validation:** All input payloads must pass VALIDATION\_RULES.yaml.

---

© 2025 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).

See SRL-LICENSE.yaml for details.


