# 🌿 SRAGI HappyFiles Refactor Guide
**File:** `/docs/HappyFiles-Refactor-Guide.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.1  
**Last Updated:** 2025-11-04  
**License:** CC BY 4.0 via SRL  

---

## 🧭 Purpose
This guide defines how to reorganize the WordPress Media Library and HappyFiles folders so that they match the official SRAGI architecture and repository layout.

We are moving from fragmented “Chronos” folders to a single, timeless **Kairos content structure**.

---

## 📁 Target Structure
All uploaded and curated assets live under **one root folder**:

/wp-content/uploads/content/

javascript
Kopier kode

Within that root you create these top-level folders:

| Folder | Purpose |
|---------|----------|
| `visuals/` | Images, illustrations, icons, and concept art used on the site |
| `docs/` | PDFs, Markdown exports, and reference material displayed or linked on the site |
| `forms/` | Uploaded form data, e.g., contact confirmations (if stored) |
| `license/` | Public copies of license, AI-policy, and compliance artifacts |
| `media/` | Audio/video clips, promotional or explanatory media |

Optional specialized sub-folders under `visuals/`:

visuals/
├── branding/ # Logos, wordmarks, symbols
├── ui-elements/ # Icons, interface graphics
├── regenerative/ # Conceptual & philosophical visuals
├── diagrams/ # System & architecture diagrams
└── photos/ # Real-world imagery

yaml
Kopier kode

---

## ⚙️ Refactor Steps (Kairos Order)

### 1. Create the New Structure
1. Open **HappyFiles → Folders → Add New**  
2. Create the root folder **`content`**.  
3. Inside it, create the subfolders shown above.  
4. Add one temporary folder: **`_to-sort`** (acts as a buffer).

---

### 2. Move Files Safely
1. Move assets you are **certain** of (e.g., logos → `visuals/branding/`).  
2. Everything uncertain → move to `_to-sort`.  
3. Do **not delete** any old folders yet.  
4. Verify on the front-end that moved assets load correctly.

---

### 3. Fonts and Code Assets
- `.woff`, `.woff2`, `.ttf`, etc. **must not** remain in the Media Library.  
- Move them to:  
/wp-content/themes/bricks-child/fonts/

yaml
Kopier kode
- Reference them in `sragi.css` using `@font-face`.

---

### 4. Backup Checkpoint
Before deleting anything:
1. In **One.com File Manager**, zip-download  
 `/wp-content/uploads/content/`
2. Keep that archive as your *Kairos snapshot.*

---

### 5. Cleanup Old Structure
After verifying the new structure:
1. Delete obsolete HappyFiles folders (`Bilder SRAGI`, `Hero Sections`, `ICO128`, etc.).  
2. Delete stray `.woff2` files from the Media Library.  
3. Remove any leftover “Uncategorized” assets or move them into the correct folder.

---

### 6. GitHub Sync (Optional but Recommended)
Mirror the same structure inside the repository:

/content/
├── visuals/
├── docs/
├── forms/
├── license/
└── media/

sql
Kopier kode

Commit with message:
chore(content): align HappyFiles structure with SRAGI content architecture v1.1

yaml
Kopier kode

---

## 🧩 Verification Checklist

| Step | Status |
|------|--------|
| Root folder `content/` exists | ☐ |
| Sub-folders match table above | ☐ |
| Fonts removed from Media Library | ☐ |
| All images correctly visible | ☐ |
| Backup ZIP created | ☐ |
| Old folders deleted | ☐ |
| Repo structure mirrored | ☐ |

---

### 🕰 Kairos Principle
> **Build first → move safely → verify → delete last.**

No stress, no loss — each move refines the living structure.

---

**Maintained by:** Neptunia Media AS / SRAGI Core  
**License:** CC BY 4.0 via SRL  
**Tagline:** “One structure, many lives — Kairos over Chronos.”
