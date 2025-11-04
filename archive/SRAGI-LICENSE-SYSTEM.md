# NOT IN USE! 💤💤💤

# 🌍 SRAGI License System Overview

**File:** `/docs/licensing/SRAGI-LICENSE-SYSTEM.md`
**Version:** 1.0
**Maintainer:** Rune Solberg / Neptunia Media AS
**Last Updated:** October 2025

---

## 🧭 Purpose

The **SRAGI License System** defines how regenerative content, AI models, and documentation are licensed, generated, and distributed within the SRAGI.org ecosystem.
It ensures alignment between **legal**, **machine-readable**, and **human-readable** layers while maintaining a single source of truth (SSOT) through YAML-based configuration.

---

## ⚙️ Core Architecture

```
YAML → XML → Markdown → WPCodeBox → Bricks → Web / API
```

Each layer derives directly from the YAML master file (`SRL-LICENSE.yaml`) ensuring no duplicated data and full synchronization between systems.

| Layer       | File                        | Purpose                                                                |
| ----------- | --------------------------- | ---------------------------------------------------------------------- |
| Source      | `SRL-LICENSE.yaml`          | Master file (SSOT) containing meta, permissions, ethics, and templates |
| Machine     | `LICENSE-RSL.xml`           | Machine-readable RSL license file for AI and crawlers                  |
| Human       | `REGENERATIVE_LICENSE.md`   | Public-facing readable license for SRAGI.org                           |
| Integration | `sync-license.yml`          | GitHub workflow that regenerates and validates files automatically     |
| Display     | `sragi_license_display.php` | WordPress snippet that injects license dynamically                     |

---

## 📜 Legal Foundation

The **SRAGI Regenerative License (SRL)** is built on **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
This guarantees:

* ✅ Legal simplicity — one minimal requirement (attribution)
* ✅ Compatibility — works with all open and proprietary licenses
* ✅ Transparency — explicit credit to original creators
* ✅ Freedom — commercial and closed-source use permitted

---

## 🧩 Core License Components

### 1. SRL-LICENSE.yaml (Master File)

**Role:** Defines all metadata, rules, and templates.

Key blocks:

* `meta`: version, SPDX, base license
* `organization`: author and contact info
* `permissions`: AI and user usage rights
* `requirements`: legal mandates (only attribution)
* `ethics`: aspirational regenerative framework
* `attribution`: credit formats
* `machine_format`: RSL XML template
* `linked_files`: cross-file references
* `history`: changelog

---

### 2. LICENSE-RSL.xml (Machine-Readable)

**Purpose:** Enables AI training platforms, crawlers, and compliance bots to automatically parse the license.

**Standard:** [Really Simple Licensing (RSL)](https://rslstandard.org/)

**Example Output:**

```xml
<rsl xmlns="https://rslstandard.org/rsl" version="1.0">
  <content url="https://github.com/Project2040/sragi.org">
    <license type="permissive">
      <standard>https://creativecommons.org/licenses/by/4.0/</standard>
      <permits type="usage">all</permits>
      <payment type="attribution">
        <required>true</required>
        <format><![CDATA[
SRAGI by Rune Solberg, Neptunia Media AS
Source: https://sragi.org
]]></format>
      </payment>
    </license>
  </content>
</rsl>
```

---

### 3. REGENERATIVE_LICENSE.md (Human-Readable)

The Markdown version of the license, combining legal, philosophical, and practical guidance:

* Overview and philosophy (radical openness)
* Legal base (CC BY 4.0)
* RSL XML snippet for transparency
* Regenerative Principles (aspirational ethics)
* Attribution formats and examples

**Public path:** `/content/license/REGENERATIVE_LICENSE.md`

---

## 🔁 Workflow Integration

### GitHub → WordPress → Bricks Sync Loop

1. **Edit:** Update `SRL-LICENSE.yaml`
2. **Generate:** GitHub Action runs `/automation/.github/workflows/sync-license.yml`
3. **Render:** Creates updated `LICENSE-RSL.xml` + `REGENERATIVE_LICENSE.md`
4. **Deploy:** Secure webhook posts to WordPress via `sragi_github_sync_secure.php`
5. **Display:** Bricks builder automatically updates license page

**Security:**

* HMAC signature check in permission_callback (prevents DoS)
* No `__return_true` callbacks
* SHA256 secret verification

---

## 🧱 File Locations

```
sragi.org/
├── SRL-LICENSE.yaml
├── LICENSE-RSL.xml
├── /content/license/
│   ├── REGENERATIVE_LICENSE.md
│   ├── LEGAL_SUMMARY.md
│   └── HUMAN_READABLE.md
└── /automation/.github/workflows/sync-license.yml
```

---

## 🧠 Version Management

Versions are tracked inside the YAML file under the `history` block.
Each update triggers automatic regeneration.

Example:

```yaml
history:
  - version: 1.01
    date: 2025-10-24
    summary: Minor update – clarified design philosophy.
```

Version identifiers should increment as follows:

* `1.0` → Stable foundation release
* `1.01` → Minor clarifications
* `1.1` → Structural improvements
* `2.0` → Major philosophical or legal change

---

## 🤖 AI and Crawler Visibility

Ensure the following supporting files exist in root:

| File                     | Purpose                                     |
| ------------------------ | ------------------------------------------- |
| `/robots.txt`            | Points to license files and sitemap         |
| `/sitemap.xml`           | Lists license and documentation URLs        |
| `/api/license.json`      | JSON response for API and AI access         |
| `/ai-training-data.yaml` | Training data declaration for Elantrix/Muse |

---

## 🌱 Regenerative Principles (Aspirational)

These are **cultural invitations**, not legal obligations:

1. **Give More Than You Take** – Reciprocity builds resilience.
2. **Validate Triadically** – Mind, Heart, Soul alignment.
3. **Honor the Whole** – Maintain source integrity.
4. **Be Transparent** – Share learning and context.
5. **Do No Harm** – Avoid extractive or exploitative use.

---

## 🧩 Linked Components

| Component        | Description              | File                                                |
| ---------------- | ------------------------ | --------------------------------------------------- |
| SRL YAML Master  | Single Source of Truth   | `/SRL-LICENSE.yaml`                                 |
| RSL XML Output   | Machine-readable license | `/LICENSE-RSL.xml`                                  |
| Markdown License | Human-readable license   | `/content/license/REGENERATIVE_LICENSE.md`          |
| Workflow         | License generator        | `/automation/.github/workflows/sync-license.yml`    |
| Webhook          | WordPress sync           | `/wordpress/wpcodebox/sragi_github_sync_secure.php` |
| Display Snippet  | Dynamic shortcode        | `/wordpress/wpcodebox/sragi_license_display.php`    |

---

## 🪄 Design Philosophy

```yaml
design_philosophy:
  must_language: false
  rationale: |
    The SRL framework intentionally avoids formal "MUST/SHALL" language.
    It relies on trust-based reciprocity instead of enforcement.
    The single legal mandate—attribution—comes from CC BY 4.0.
```

This philosophy keeps SRAGI **regenerative, flexible, and non-punitive**, aligning with the project’s moral and technical integrity.

---

## 🧭 Summary

The SRAGI License System:

* Defines a **regenerative, permissive framework** built on CC BY 4.0
* Bridges legal, ethical, and AI-readable dimensions
* Enables automatic generation and synchronization
* Embodies SRAGI’s guiding ethos: **“Culture, not control.”**

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0
**Source:** [https://sragi.org/license](https://sragi.org/license)
