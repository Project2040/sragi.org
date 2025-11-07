# 🧬 SRAGI Git & Version Control Conventions

**File:** `/docs/SRAGI-GIT-STANDARDS.md`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.1
**Last Updated:** November 2025

---

## 🧭 Purpose

This document defines the **Git, branching, and commit message conventions** for the SRAGI.org ecosystem.
It ensures clarity, traceability, and automation compatibility across GitHub workflows, WordPress synchronization, and AI-integrated documentation pipelines.

---

## 🧱 Repository Principles

SRAGI repositories follow these principles:

* **Single Source of Truth (SSOT)** for each data type (e.g., YAML → XML → MD)
* **Readable history** – commits tell a clear story
* **Minimal merge friction** – consistent branch naming
* **Automated compliance** – commits trigger workflows via keywords

---

## 🌿 Branch Naming Convention

| Type                  | Prefix  | Example                   | Purpose                         |
| --------------------- | ------- | ------------------------- | ------------------------------- |
| Main / Production     | `main`  | `main`                    | Stable, deployable branch       |
| Development           | `dev`   | `dev`                     | Consolidated testing branch     |
| Feature               | `feat/` | `feat/license-generator`  | New features or modules         |
| Fix / Patch           | `fix/`  | `fix/yaml-parser-bug`     | Bug or regression fix           |
| Documentation         | `docs/` | `docs/conventions-update` | Documentation-only changes      |
| Experiment / Research | `exp/`  | `exp/elantrix-ai-agent`   | Prototyping, not for production |

**Rules:**

* Use lowercase + hyphens.
* Branch names must be short, descriptive, and actionable.
* Avoid personal names; use purpose-driven identifiers.

---

## ✍️ Commit Message Standard

All commits follow the **Conventional Commit** style adapted for SRAGI:

### Format

<type>(<scope>): <short summary>[optional body][optional footer]
### Example

feat(licensing): add automated sync workflow for SRL YAML → XMLAdded new GitHub Action (build-license.yml) to regenerate XML + MD.Includes validation step and webhook notification to WordPress.
### Accepted Commit Types

| Type       | Description                                            |
| ---------- | ------------------------------------------------------ |
| `feat`     | New feature or functionality                           |
| `fix`      | Bug fix or patch                                       |
| `docs`     | Documentation updates                                  |
| `style`    | Code style or formatting only (no logic changes)       |
| `refactor` | Internal restructuring without behavior change         |
| `test`     | New or updated test cases                              |
| `chore`    | Maintenance tasks (dependency updates, config changes) |
| `perf`     | Performance improvements                               |

---

### Commit Body Guidelines

* Use present tense (“add”, not “added”).
* Limit first line to **72 characters**.
* Reference issues or PRs in the footer (`Refs #42`).
* Include rationale for non-obvious changes.
* Separate paragraphs with a blank line.

Example:

fix(yaml): correct indentation in generated SRL-LICENSE.yamlCaused by mixed tab/space alignment during build.Refs #134.
---

## 🏷️ Tagging and Releases

SRAGI uses semantic versioning-like tags:

v1.0.0   = major releasev1.0.1   = minor fix / patchv1.1.0   = feature releasev2.0.0   = major architecture or license change
### Tag Naming Rules

* Must start with `v` (e.g., `v1.01`).
* Should match the version inside `SRL-LICENSE.yaml` (meta.version).
* Tags may trigger specific deployment workflows.

### Release Notes

* Automatically generated from commit messages using keywords.
* Each release should include:

  * Summary of major changes
  * Updated license or docs references
  * Link to relevant discussions (if any)

---

## 🔁 Pull Request (PR) Conventions

Each PR must:

* Reference related issue(s) or discussion threads.
* Include a descriptive title (`feat:`, `fix:`, `docs:` prefix).
* Contain a summary checklist in the body:

  ```markdown
  ## Summary
  - [x] Implemented new SRL license workflow
  - [x] Verified against SRL-LICENSE.yaml SSOT
  - [x] Added documentation in /docs/licensing/

**Review Rules:**

* At least one reviewer (for all non-doc PRs)
* No direct commits to `main` unless automated
* Squash merge recommended to maintain clean history

---

## 🧩 Automation Keywords (Workflow Triggers)

Workflows can be triggered automatically using commit message keywords:

| Keyword          | Triggered Action                             |
| ---------------- | -------------------------------------------- |
| `[skip ci]`      | Prevents GitHub Actions from running         |
| `[deploy-wp]`    | Pushes updates to WordPress via webhook      |
| `[docs-rebuild]` | Rebuilds documentation index in GitHub Pages |

*(Note: License regeneration happens automatically on every push to `SRL-LICENSE.yaml`, no keyword needed.)*

Example:

chore(docs): update typo in readme [skip ci]


---

## 🌐 Branch Protection & Security

**Protected Branches:**

* `main` → requires review, no force-push
* `dev` → requires successful checks before merge

**Workflow Secrets:**

* Store sensitive keys (e.g., `WP_SYNC_SECRET`) in GitHub Actions secrets
* Never commit tokens or API keys directly

**Commit Signing:**

* GPG-signed commits recommended for all maintainers
* Bots (SRAGI Automation) use verified `bot@sragi.org` identity

---

## 📦 Repository Structure for Git Configs

.github/
├── workflows/
│   ├── build-license.yml    # Core SSOT generator
│   ├── ssot-guard.yml       # Version enforcement
│   └── ...
├── ISSUE_TEMPLATE.md
├── PULL_REQUEST_TEMPLATE.md
└── CODEOWNERS

CODEOWNERS Example:

/docs/           @runesolberg
/wordpress/      @runesolberg
/automation/     @runesolberg

---

## 🧠 Commit Message AI Integration

SRAGI Elantrix Core will parse commit messages for metadata enrichment.
Therefore, consistency in message structure is essential for:

* Documentation auto-generation
* Version sync
* Contributor recognition
* AI learning corpus attribution

---

## 🪄 Summary

The **SRAGI Git & Version Control Standards** ensure that all repositories remain:

* Predictable in structure
* Transparent in purpose
* Ready for automation and AI indexing
* Human-readable and regenerative in ethos

> “A clean Git history is a mirror of collective clarity.”
> — SRAGI Engineering Philosophy

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.
