# 🧬 SRAGI Git & Version Control Conventions

**File:** `/docs/standards/GIT-STANDARDS.md`

**Status:** PRODUCTION STANDARD

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.3 (Expanded with Multi-Repo & Flagging)

**Last Updated:** December 2025

---

## 🧭 Purpose

This document defines the **Git, branching, and commit message conventions** for the entire Neptunia Media ecosystem (sragi.org, lurevalg.no, merkur-consulting.com).
It ensures clarity, traceability, and automation compatibility across GitHub workflows, WordPress synchronization, and AI-integrated documentation pipelines.

---

## 🧱 Repository Principles

All Neptunia repositories follow these principles:

* **Single Source of Truth (SSOT)** for each data type (e.g., YAML → XML → MD)
* **Readable history** – commits tell a clear story
* **Minimal merge friction** – consistent branch naming
* **Automated compliance** – commits trigger workflows via keywords

> *These standards apply to all Neptunia repositories unless a repo has an explicit override documented in its own `/docs/`.*

---

## 🌿 Branch Naming Convention

| Type | Prefix | Example | Purpose |
| :--- | :--- | :--- | :--- |
| Main / Production | `main` | `main` | Stable, deployable branch |
| Development | `dev` | `dev` | Consolidated testing branch |
| Feature | `feat/` | `feat/license-generator` | New features or modules |
| Fix / Patch | `fix/` | `fix/yaml-parser-bug` | Bug or regression fix |
| Documentation | `docs/` | `docs/conventions-update` | Documentation-only changes |
| Experiment | `exp/` | `exp/elantrix-ai-agent` | Prototyping, not for production |

**Rules:**
* Use lowercase + hyphens.
* Branch names must be short, descriptive, and actionable.

---

## ✍️ Commit Message Standard

All commits follow the **Conventional Commit** style adapted for SRAGI:

### Format
`<type>(<scope>): <short summary>`
`[optional body]`
`[optional footer]`

### Example
```text
feat(licensing): add automated sync workflow for SRL YAML → XML

Added new GitHub Action (build-license.yml) to regenerate XML + MD.
Includes validation step and webhook notification to WordPress.
````

### **Accepted Commit Types**

| Type | Description |
| :---- | :---- |
| feat | New feature or functionality |
| fix | Bug fix or patch |
| docs | Documentation updates |
| style | Code style or formatting only (no logic changes) |
| refactor | Internal restructuring without behavior change |
| test | New or updated test cases |
| chore | Maintenance tasks (dependency updates, config changes) |

---

## **🏷️ Tagging and Releases**

SRAGI uses semantic versioning-like tags:

* v1.0.0 \= major release  
* v1.0.1 \= minor fix / patch  
* v1.1.0 \= feature release

### **Tag Naming Rules**

* Must start with v (e.g., v1.0.1).  
* Should match the version inside SRL-LICENSE.yaml (meta.version).  
* Tags may trigger specific deployment workflows.

---

## **📄 File-Level Versioning (The Flags)**

We use specific suffixes in file headers to signal review status without breaking production.

### **1\. Change Required (c)**

Use when a file works but **must be changed** to meet new standards.

* **Suffix:** v1.0c  
* **Example:** Version: 1.0c  
* **Comment:** \> \*\*⚠️ CHANGE REQUIRED:\*\* Needs updated logo path per Visual Protocol v1.1.

### **2\. Revision Needed (r)**

Use when content is technically valid but needs **editorial or strategic review**.

* **Suffix:** v1.0r  
* **Example:** Version: 1.0r  
* **Comment:** \> \*\*⚠️ REVISION NEEDED:\*\* Tone of voice check required before launch.

**Why flags?** They allow the system (Loom/Code) to continue using the file as valid asset, while signaling to humans (and AI agents) that attention is needed.

---

## **🛡️ History & Force Push**

* **Never** git push \--force to main or dev.  
* git push \--force-with-lease is allowed on your own feature branches **before** opening a PR.  
* Once a branch is under review, treat its history as shared.

---

## **🔁 Pull Request (PR) Conventions**

Each PR must:

* Include a descriptive title (feat:, fix:, docs: prefix).  
* Contain a summary checklist.  
* **Squash merge** is recommended to maintain clean history.

---

## **🧩 Automation Keywords**

These keywords only work if matching GitHub Actions are configured in .github/workflows/.

| Keyword | Triggered Action |
| :---- | :---- |
| \[skip ci\] | Prevents GitHub Actions from running |
| \[deploy-wp\] | Pushes updates to WordPress via webhook |
| \[docs-rebuild\] | Rebuilds documentation index |

---

## **📦 Repository Structure for Git Configs**

Plaintext

```
.github/
├── workflows/
│   ├── build-license.yml    # Core SSOT generator
│   ├── ssot-guard.yml       # Version enforcement
└── ...
CODEOWNERS                   # Defines responsibility
```

---

## **🪄 Summary**

The **SRAGI Git & Version Control Standards** ensure that all repositories remain:

* Predictable in structure  
* Transparent in purpose  
* Ready for automation

“A clean Git history is a mirror of collective clarity.”

---

© 2025 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).

See SRL-LICENSE.yaml for details.

