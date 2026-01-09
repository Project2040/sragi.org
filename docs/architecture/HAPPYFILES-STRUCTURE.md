# 🌿 SRAGI HappyFiles Guide

**File:** `/docs/architecture/HAPPYFILES-STRUCTURE.md`

**Status:** PRODUCTION STANDARD

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 2.2 (Dual-Core Aligned)

**Last Updated:** January 2026

## ⚠️ Note: This guide is synchronized with SRAGI Visual Factory v5.5
---

## 🧭 Purpose
This guide defines how to reorganize the WordPress Media Library and HappyFiles folders to match the official SRAGI architecture and **Visual Protocol v1.1**.

We are moving from fragmented “Chronos” folders to a single, timeless **Kairos content structure**.

---

## 📁 Target Structure (SSOT)
All uploaded and curated assets live under **one root folder** in HappyFiles:

`/content/`

Within that root, create these top-level folders:

| Folder | Purpose |
|---------|----------|
| `visuals/` | All images, icons, and visual tokens (See structure below) |
| `docs/` | PDFs, Markdown exports, and reference material |
| `license/` | Public copies of license, AI-policy, and compliance artifacts |
| `media/` | Audio/video clips (MP4, MP3) |

### 🎨 The Visuals Sub-structure (Crucial!)
This MUST match the **SRAGI Visual Factory** output targets:

```text
/content/visuals/
├── hero/           (For *-hero.avif files)
├── content/        (For *-content.avif and *-content.jpg files)
├── tokens/         (For *-token.avif and *-tiny.avif files)
├── social/         (For *-og.jpg files)
├── diagrams/       (For SVG system diagrams)
├── icons/          (For SVG UI icons/logos)
└── video/          (For MP4 background loops)

