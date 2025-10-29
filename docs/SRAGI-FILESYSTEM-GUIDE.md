# 🗂️ SRAGI Filesystem Guide

**File:** `/docs/SRAGI-FILESYSTEM-GUIDE.md`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0  
**Last Updated:** October 28, 2025  

---

## 🌍 Purpose

This document defines the **content structure** and **storage conventions** for [SRAGI.org](https://sragi.org).  
It ensures a clean, logical hierarchy that works seamlessly with **Bricks Builder**, **HappyFiles Pro**, and **WordPress Core**,  
without breaking update compatibility or GDPR compliance.

---

## 🧱 Directory Structure

SRAGI.org uses [HappyFiles Pro](https://happyfiles.io) to organize uploaded content inside the native WordPress directory:

/wp-content/uploads/SRAGI Content/

csharp
Kopier kode

The internal folder hierarchy mirrors the logical structure of the SRAGI project:

📁 SRAGI Content
├── forms/ → Contact forms, ethical form templates
├── license/ → SRAGI-RSL, SRL, and AI-policy files
├── docs/ → Documentation, Markdown content, guides
└── visuals/ → Logos, diagrams, and concept illustrations

yaml
Kopier kode

---

## ⚙️ HappyFiles Configuration (Recommended)

| Setting | Status | Description |
|----------|--------|-------------|
| **Enforce loading → wp-admin** | ✅ Enabled | Ensures HappyFiles loads in the admin panel. |
| **Enforce loading → Frontend** | 🔲 Disabled | Avoids unnecessary script loading for visitors. |
| **Assign multiple folders** | 🔲 Disabled | Keeps each file in one logical location. |
| **Remove from all folders** | ✅ Enabled | Maintains clean folder relations. |
| **Infinite scrolling** | ✅ Enabled | Improves usability for large media libraries. |
| **Sort by file size** | ✅ Enabled | Helps manage large diagram and media files. |

---

## 🔗 Accessing Files Publicly

Each file inside `/wp-content/uploads/SRAGI Content/` can be accessed directly via URL, for example:

https://sragi.org/wp-content/uploads/SRAGI%20Content/forms/contact.md
https://sragi.org/wp-content/uploads/SRAGI%20Content/license/LICENSE-RSL.xml
https://sragi.org/wp-content/uploads/SRAGI%20Content/docs/SRAGI-INTEGRATION-MAP.md

yaml
Kopier kode

*(The space between “SRAGI” and “Content” is URL-encoded as `%20`.)*

---

## ✨ Optional: Clean “/content/” URL Mapping

For a human-readable structure without modifying WordPress core paths,  
add this safe rewrite rule to `.htaccess` at the root of your WordPress installation:

```apache
# 🔹 SRAGI Custom Content Mapping
RewriteEngine On
RewriteRule ^content/(.*)$ wp-content/uploads/SRAGI%20Content/$1 [L,QSA]
You can then use simplified URLs like:

ruby
Kopier kode
https://sragi.org/content/forms/contact.md
https://sragi.org/content/license/LICENSE-RSL.xml
✅ Safe: Does not interfere with Bricks, ACF, or media uploads
✅ SEO-friendly: Search engines index /content/*
✅ Reversible: Remove the rule anytime without affecting files

📚 Example Integration (Bricks + ACF)
When referencing these files dynamically in Bricks Builder or ACF fields:

text
Kopier kode
<a href="{acf:license_link}" target="_blank">View License</a>
Example ACF field value:

ruby
Kopier kode
https://sragi.org/content/license/LICENSE-RSL.xml
🧩 Version Control
All non-binary documents (.md, .xml, .txt, .json) should also be mirrored to GitHub for full transparency and backup.

Repository:
https://github.com/Project2040/sragi.org

Recommended GitHub mirrors:

bash
Kopier kode
/docs/         → /wp-content/uploads/SRAGI Content/docs/
/license/      → /wp-content/uploads/SRAGI Content/license/
/forms/        → /wp-content/uploads/SRAGI Content/forms/
🔒 Security Notes
No executable files (.php, .js) are stored in /SRAGI Content/

All Markdown and XML files are safe for public read access

Personal data (from forms) is never stored unless explicit consent is given

Backups are handled at the hosting level via One.com

🌱 Why This Approach Works
Principle	Explanation
Regenerative Structure	Every file serves both human and machine readability.
Compatibility	Works natively with Bricks, ACF, and SureCart.
Transparency	Public access via /content/ mirrors the open-source spirit of SRAGI.
Simplicity	No plugin conflicts, no broken paths, no custom code in PHP.

© 2025 Rune Solberg / Neptunia Media AS
Licensed under CC BY-SA 4.0
Part of the SRAGI Regenerative Source License (RSL)
