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

```
## ⚙️ Refactor Steps (Kairos Order)

### 1. Create the New Structure
1. Open **HappyFiles → Folders → Add New**.
2. Create the root folder **`content`**.
3. Inside it, create subfolders: `visuals`, `docs`, `license`, `media`.
4. Inside `visuals`, create the subfolders listed above (`hero`, `content`, `tokens`, etc.).
5. Add one temporary folder: **`_to-sort`** (buffer).

### 2. Move Files Safely
1. **Identify:** Use the filename suffix to guide you.
   - Has `-hero`? 👉 Move to `/visuals/hero/`
   - Has `-token`? 👉 Move to `/visuals/tokens/`
   - Is it a Logo? 👉 Move to `/visuals/icons/`
2. **Uncertain?** 👉 Move to `_to-sort`.
3. **Verify:** Check frontend to ensure images still load correctly.

### 3. Cleanup Old Structure
After verifying functionality:
1. Delete obsolete folders (e.g., `Bilder SRAGI`, `Branding`, `Photos`).
2. Empty `_to-sort` gradually as you identify proper homes for the files.

---

## 🧩 Verification Checklist

| Step | Status |
| :--- | :--- |
| Root folder `content/` exists | ☐ |
| Visual sub-folders match Protocol v1.1 | ☐ |
| Old folders deleted | ☐ |
| All images verified on frontend | ☐ |

---

**Maintained by:** Neptunia Media AS / SRAGI Core  
**License:** CC BY 4.0 via SRL

