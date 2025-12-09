# 🧭 SRAGI SSOT Policy

**File:** `/docs/core/SSOT-POLICY.md`

**Status:** CORE DOCTRINE

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 2.0 (System-Wide Expansion)

**Last Updated:** 2025-12-09

---

## 🌱 Purpose

This document defines the **Single Source of Truth (SSOT)** architecture for the SRAGI ecosystem.
It establishes the absolute rule that **data defines the system**, not code.

**Core Principle:** Every piece of logic has ONE canonical source. Everything else references or generates from it.

---

## 🧩 The SSOT Hierarchy

The system is controlled by four specific files in `_CONFIG/` and root. All documentation (`standards/`), code (`backend/`), and validation logic must derive from these.

| Domain | File Location (The Truth) | Enforced By |
| :--- | :--- | :--- |
| **Ontology** | `/_CONFIG/TAXONOMY_GRAPH.yaml` | `config_bridge.py` |
| **Quality** | `/_CONFIG/VALIDATION_RULES.yaml` | `validate.php`, `qa_engine.py` |
| **Structure**| `/_CONFIG/CONTENT-TEMPLATE.yaml` | `process.php` |
| **Legal** | `/SRL-LICENSE.yaml` | `license_builder.py` |

> **Rule:** If documentation in `/docs/standards/` contradicts a file in `/_CONFIG/`, the documentation is wrong. The Config is the Law.

---

## 🔒 The 5 Immutable Rules

### 1. Never Hardcode Rules
* ❌ **Bad:** Writing `if (strlen($title) > 60)` inside PHP.
* ✅ **Good:** Writing `if (strlen($title) > $config['seo']['max_title'])`.

### 2. No Duplicate Truths
Do not define "SEO Title Length" in both `seo.md` and `validate.php`. Define it in `VALIDATION_RULES.yaml`, and let both the doc and the code reference that.

### 3. Generate, Don't Duplicate
We do not manually copy taxonomy terms into WordPress. The Sync Engine reads `TAXONOMY_GRAPH.yaml` and creates them.

### 4. Version in Metadata
Do not put version numbers in filenames (e.g., `BIOS-v2.1.yaml`). Put them inside the file content (`version: 2.1`). This keeps Git history clean (Kairos).

### 5. Reference Dynamically
Never write "Licensed under SRL v1.12" in a footer. Write "See SRL-LICENSE.yaml". This ensures old files remain valid when the license evolves.

---

## ⚙️ Enforcement

This policy is not just a wish; it is enforced by code.

1.  **License Integrity:** `tools/enforce_version_refs.py` scans for hardcoded versions.
2.  **Content Validation:** `modules/qa_engine.py` reads `VALIDATION_RULES.yaml` to reject non-compliant content.
3.  **Interface Sync:** `modules/config_bridge.py` generates menus in Mission Control directly from `TAXONOMY_GRAPH.yaml`.

---

## 🕰 Kairos vs Chronos

| Chronos (Old Way) | Kairos (SRAGI Way) |
| :--- | :--- |
| Hardcoded rules scattered in code | Centralized YAML rules |
| Manual updates across 10 files | Update 1 file, regen everything |
| "Documentation rot" | Documentation as Code |

SRAGI maintains **Kairos Architecture** — a living, breathing system where the map *is* the territory.

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.

**“One source for all time.”**
