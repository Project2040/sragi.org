# 🌿 SRAGI HappyFiles Refactor Guide (v2.0)
**File:** `/docs/HappyFiles-Refactor-Guide.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 2.0 (Synced with Visual Protocol v1.1)  
**Last Updated:** December 2025  
**License:** CC BY 4.0 via SRL  

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
This MUST match the **SRAGI Visual Protocol** output targets:

```text
/content/visuals/
├── hero/           (For *-large.avif files)
├── content/        (For *-medium.avif files)
├── tokens/         (For *-small.avif and *-tiny.avif files)
├── social/         (For *-social.jpg and *-og.jpg files)
├── diagrams/       (For SVG system diagrams)
├── icons/          (For SVG UI icons/logos)
└── video/          (For MP4 background loops)
