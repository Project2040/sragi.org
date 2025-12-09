# 📚 SRAGI Documentation Standards (The Regelbok)

**Version:** 1.0  
**Status:** PRODUCTION READY (SSOT)  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Last Updated:** 2025-12-09

---

## 🧭 Welcome to the Regelbok

This is the **Single Source of Truth** for all SRAGI standards, protocols, and system documentation.

> **"Documentation is not bureaucracy — it's the living memory of the system."**

### 📖 How to Navigate

The documentation library is organized into four distinct layers of abstraction, ranging from eternal principles to machine-executable rules:

| Layer | Folder | Purpose |
| :--- | :--- | :--- |
| **1. PHILOSOPHY** | [`core/`](core/) | **WHY.** The soul and intent. Rarely changes. |
| **2. STANDARDS** | [`standards/`](standards/) | **WHAT.** Hard rules humans must follow. |
| **3. ARCHITECTURE** | [`architecture/`](architecture/) | **HOW.** Technical maps of machinery & data flows. |
| **4. LAW (DATA)** | [`_CONFIG/`](_CONFIG/) | **THE CODE.** Machine-readable SSOT files. |

---

## 🏛️ 1. Core Philosophy
*The eternal principles. Read these first to understand the intent.*

| Document | Purpose |
| :--- | :--- |
| [**MERKUR-TQM-PHILOSOPHY.md**](core/MERKUR-TQM-PHILOSOPHY.md) | Quality doctrine: Human-in-the-Loop, SSOT, Kaizen, R>1. |
| [**SSOT-POLICY.md**](core/SSOT-POLICY.md) | The law of Single Source of Truth. |
| [**VISUAL-PHILOSOPHY.md**](core/VISUAL-PHILOSOPHY.md) | Ethics of visual creation & latent space tokens. |
| [**ETHICAL-CONTACT-PROTOCOL.md**](core/ETHICAL-CONTACT-PROTOCOL.md) | Data minimalism, consent, and transparency. |

**Key Concepts:**
* **R>1:** Regenerative Ratio (give more than you take).
* **Kairos over Chronos:** Right timing over deadlines.
* **Fitness for Future:** Build for evolution, not just "good enough".

---

## 📏 2. Standards & Protocols
*The rules humans must follow when creating content.*

| Document | Governs |
| :--- | :--- |
| [**VISUAL-PROTOCOL.md**](standards/VISUAL-PROTOCOL.md) | 6 sacred ratios, image pipeline, file naming. |
| [**SEO-PROTOCOL.md**](standards/SEO-PROTOCOL.md) | Title length, meta desc, slug formats. |
| [**DOCUMENTATION-STANDARDS.md**](standards/DOCUMENTATION-STANDARDS.md) | Markdown structure, H1 rules, frontmatter. |
| [**CODE-API-STANDARDS.md**](standards/CODE-API-STANDARDS.md) | YAML/JSON formatting, API design patterns. |
| [**ACCESSIBILITY-STANDARDS.md**](standards/ACCESSIBILITY-STANDARDS.md) | WCAG 2.2 AA, alt text, contrast requirements. |
| [**GIT-STANDARDS.md**](standards/GIT-STANDARDS.md) | Commit messages, branching, versioning. |
| [**SRAGI-CSS.md**](standards/SRAGI-CSS.md) | White paper aesthetics & Bricks implementation. |

---

## ⚙️ 3. Architecture & Systems
*How the machinery works.*

| Document | Describes |
| :--- | :--- |
| [**WEB-BIOS.yaml**](architecture/WEB-BIOS.yaml) | System definition, actor types, knowledge graph. |
| [**SYNC-LOOP-ARCHITECTURE.md**](architecture/SYNC-LOOP-ARCHITECTURE.md) | The flow from Git to WordPress (The Factory). |
| [**HAPPYFILES-STRUCTURE.md**](architecture/HAPPYFILES-STRUCTURE.md) | WordPress media library organization. |
| [**TSF-INTEGRATION.md**](architecture/TSF-INTEGRATION.md) | The SEO Framework headless setup. |
| [**BUNNY-CDN-INTEGRATION.md**](architecture/BUNNY-CDN-INTEGRATION.md) | Edge caching & asset delivery. |
| [**FILE-STRUCTURE-OVERVIEW.md**](architecture/FILE-STRUCTURE-OVERVIEW.md) | Map of the root filesystem. |

---

## 🤖 4. Configuration (SSOT)
*Machine-readable law. Validators read directly from here.*

| File | Contains |
| :--- | :--- |
| [**TAXONOMY_GRAPH.yaml**](_CONFIG/TAXONOMY_GRAPH.yaml) | 9 taxonomies, 89 terms (The Ontology). |
| [**VALIDATION_RULES.yaml**](_CONFIG/VALIDATION_RULES.yaml) | Logic for SEO, markdown, media & accessibility. |
| [**CONTENT-TEMPLATE.yaml**](_CONFIG/CONTENT-TEMPLATE.yaml) | Master content specification (The Mold). |

> **Critical Principle:** These files are the Single Source of Truth. All documentation mirrors these. Never hardcode rules; always reference `_CONFIG`.

---

## 🎯 Common Workflows

### I want to create an article
1. **Read:** [`SEO-PROTOCOL.md`](standards/SEO-PROTOCOL.md) & [`DOCUMENTATION-STANDARDS.md`](standards/DOCUMENTATION-STANDARDS.md).
2. **Use:** **Mission Control v5.0** (enforces `VALIDATION_RULES.yaml`).
3. **Check:** [`CONTENT-TEMPLATE.yaml`](_CONFIG/CONTENT-TEMPLATE.yaml) for required fields.

### I want to add an image
1. **Read:** [`VISUAL-PROTOCOL.md`](standards/VISUAL-PROTOCOL.md).
2. **Use:** `SRAGI-IMAGE-PIPELINE-v2_1.bat` (generates all sizes).
3. **Upload:** To HappyFiles per [`HAPPYFILES-STRUCTURE.md`](architecture/HAPPYFILES-STRUCTURE.md).

### I want to build a validator
1. **Read:** [`MERKUR-TQM-PHILOSOPHY.md`](core/MERKUR-TQM-PHILOSOPHY.md) (principles).
2. **Load:** [`VALIDATION_RULES.yaml`](_CONFIG/VALIDATION_RULES.yaml) (rules).
3. **Follow:** [`CODE-API-STANDARDS.md`](standards/CODE-API-STANDARDS.md) (formatting).

---

## 🔍 Quick Reference Card

| Need | Look Here | Standard |
| :--- | :--- | :--- |
| **SEO Title** | [`SEO-PROTOCOL.md`](standards/SEO-PROTOCOL.md) | 45-60 chars |
| **Image Sizes** | [`VISUAL-PROTOCOL.md`](standards/VISUAL-PROTOCOL.md) | 6 ratios (3:2, 16:9...) |
| **Taxonomy** | [`TAXONOMY_GRAPH.yaml`](_CONFIG/TAXONOMY_GRAPH.yaml) | 89 valid terms |
| **H1 Rules** | [`DOCUMENTATION-STANDARDS.md`](standards/DOCUMENTATION-STANDARDS.md) | One per file |
| **Alt Text** | [`ACCESSIBILITY-STANDARDS.md`](standards/ACCESSIBILITY-STANDARDS.md) | Required, max 125 chars |
| **Commits** | [`GIT-STANDARDS.md`](standards/GIT-STANDARDS.md) | Conventional Commits |

---

## 🌀 The SRAGI Principles

Every standard in this documentation embodies these core principles:

1.  **R>1 (Regenerative Ratio):** Give more than you take.
2.  **SSOT:** One canonical source for every piece of data.
3.  **Human-in-the-Loop:** AI suggests, humans decide.
4.  **Kaizen:** When we find an error, we update the system.
5.  **Fitness for Future:** Build for evolution.

---

**© 2025 Rune Solberg / Neptunia Media AS** License: CC BY-SA 4.0 via SRAGI Regenerative License (SRL)  
Repository: [https://github.com/Project2040/sragi.org](https://github.com/Project2040/sragi.org)

*"Quality is not an act, it is a habit."* — Aristotle (Merkur paraphrase)

**🌀 Welcome to the Regelbok. May it serve regeneration.**
