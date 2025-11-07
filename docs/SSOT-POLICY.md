# 🧭 SRAGI SSOT Policy

**File:** `/docs/SSOT-POLICY.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.1
**Last Updated:** November 2025

---

## 🌱 Purpose

This document defines how version control and licensing are handled inside the SRAGI repositories.
All versioned and licensed materials must point to a **single source of truth (SSOT)** — the canonical YAML file that defines the SRL system.

---

## 🧩 SSOT Hierarchy

| Layer | File | Description |
|-------|------|--------------|
| **Primary Source (SSOT)** | `SRL-LICENSE.yaml` | Defines active version, metadata, license text, and full changelog history. |
| **Generated Artifacts** | `LICENSE-RSL.xml`, `license.json`, `index.html`, etc. | Built automatically from the SSOT file by CI/CD pipelines. |
| **Human Docs** | `README.md`, `/docs/*.md` | Must never contain hard-coded version numbers — only point back to the SSOT. |

---

## ⚙️ Enforcement

The following tools ensure permanent alignment:

| Tool | Path | Function |
|------|------|-----------|
| `tools/enforce_version_refs.py` | Repository root | Scans and auto-fixes any outdated SRL references. |
| `.github/workflows/ssot-guard.yml` | GitHub Actions | CI guard that blocks commits or PRs with hard-coded versions. |

All repositories under the SRAGI ecosystem **must include both**.

---

## 🔒 Rules

1. **Never** write `SRL v1.0`, `v1.1`, etc. directly in documentation headers or footers.
2. Always use the timeless reference:
   > Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
   > See SRL-LICENSE.yaml for current version and details.
3. Files under `/content/visuals/` or `sragi-skills/` fall under the **Secondary Scope** and may use **CC BY-SA 4.0**.
4. Any script introducing version text must read it dynamically from `SRL-LICENSE.yaml`.
5. Merging to `main` requires the **SSOT Guard** workflow to pass.

---

## 🕰 Kairos vs Chronos

| Chronos | Kairos |
|----------|--------|
| Manual versioning | Living license reference |
| Fragmented updates | Centralized truth |
| Reactive maintenance | Regenerative evolution |

SRAGI maintains **Kairos versioning** — a living, self-healing documentation structure that evolves in sync with its license source.

---

## 📘 Compliance Status

| Area | Required | Enforced by |
|------|-----------|-------------|
| License references | ✅ | `enforce_version_refs.py` |
| Version history | ✅ | `SRL-LICENSE.yaml` (history block) |
| CI validation | ✅ | `.github/workflows/ssot-guard.yml` |
| Local pre-commit | Optional | Manual `python tools/enforce_version_refs.py` |

---

**Maintained by:** Neptunia Media AS / SRAGI Core
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.
**“One source for all time — Kairos over Chronos.”**
