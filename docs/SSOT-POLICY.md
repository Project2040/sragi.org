# 🧭 SRAGI SSOT Policy  
**File:** `/docs/SSOT-POLICY.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0  
**Last Updated:** 2025-11-02  
**License:** CC BY 4.0 via the SRAGI Regenerative License (SRL)

---

## 🌱 Purpose
This document defines how version control and licensing are handled inside the SRAGI repositories.  
All versioned and licensed materials must point to a **single source of truth (SSOT)** — the canonical YAML files that define the SRL system.

---

## 🧩 SSOT Hierarchy

| Layer | File | Description |
|-------|------|--------------|
| **Primary Source (SSOT)** | `SRL-LICENSE.yaml` | Defines the active SRL version, metadata, and canonical license text. |
| **Version History (SSOT)** | `SRL-VERSIONS.yaml` | Stores the changelog and previous SRL versions. |
| **Generated Artifacts** | `LICENSE-RSL.xml`, `ai-policy.xml`, etc. | Built automatically from the above SSOT files. |
| **Human Docs** | `README.md`, `/docs/*.md`, etc. | Must never contain hard-coded version numbers — only point back to the SSOT. |

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

1. **Never** write `SRL v1.0`, `v1.1`, etc. directly in docs.  
2. Always use the timeless reference:  
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.

yaml
Kopier kode
3. Files under `/visuals/`, `/assets/`, or `sragi-skills/` may use  
**CC BY-SA 4.0** — all others use **CC BY 4.0**.
4. Any script or documentation introducing version text must read it dynamically from `SRL-LICENSE.yaml`.
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
| Version history | ✅ | `SRL-VERSIONS.yaml` |
| CI validation | ✅ | `.github/workflows/ssot-guard.yml` |
| Local pre-commit | Optional | Manual `python tools/enforce_version_refs.py` |

---

**Maintained by:** Neptunia Media AS / SRAGI Core  
**License:** CC BY 4.0 via SRL  
**“One source for all time — Kairos over Chronos.”**
