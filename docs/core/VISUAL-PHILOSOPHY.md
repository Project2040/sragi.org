# **🌌 SRAGI Image Guidelines (UPDATED)**  need quality control

**For:** sragi-skills repository and /content/visuals

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.5 (Dual Core Aligned)

**Last Updated:** 09.01.2026

**Coordination:** Technical specs are governed by SRAGI-VISUAL-SYSTEM-v1.0.md (SSOT)

**Note:** This document governs *meaning, ethics, and handling*.

**SRAGI-VISUAL-SYSTEM-v1.0.md governs pixels, sizes, and export rules.**



## **🎯 Purpose**

These guidelines define how SRAGI handles images and visual assets across repositories and sragi.org.

They ensure:

✅ **Consistent visual identity** (mytopoetic, fractal-inspired)

✅ **Machine- and human-readable imagery** (alt text \+ Dual Core metadata)

✅ **Fast web performance** (AVIF-first, JPG-fallback)

✅ **Ethical transparency for AI-generated works** (disclose origins, avoid misrepresentation)

---

## **📁 Directory Structure**

In the GitHub repository (/content/visuals/), we use a flat structure for raw assets, but logically we categorize them:

* logos/ → SRAGI \+ Neptunia branding (vectors)  
* diagrams/ → Systems, flows, architectures  
* illustrations/ → Conceptual, symbolic art  
* ai-renders/ → AI-generated symbolic/documentary visuals (with disclosure)  
* icons/ → Small UI/interface symbols

### **Folder Example with Previews (GitHub Source)**

Plaintext

```

/content/visuals/
├── nanobanana-architect-2026-16x9.yaml       (METADATA SSOT)
├── nanobanana-architect-2026-16x9-hero.avif  (1920px)
├── nanobanana-architect-2026-16x9-content.avif (1200px)
├── nanobanana-architect-2026-16x9-content.jpg  (FALLBACK)
└── nanobanana-architect-2026-16x9-token.avif   (600px)

```

---

## **🎨 Format Policy (AVIF-first)**

| Format | Use Case | Notes | Best Practice |
| :---- | :---- | :---- | :---- |
| **SVG** | Diagrams, logos, icons | Optimize \+ strip scripts | Best for UI \+ structure; scalable and small |
| **PNG** | Master/originals | Lossless | Keep as archival source of truth (GitHub only, not WP) |
| **AVIF** | Website media (primary) | Best compression/quality | Default for web delivery |
| **JPG** | Website fallback \+ OG | Max compatibility | Always paired with AVIF as fallback |

Rule:

For every published raster image: AVIF is primary and JPG is fallback.

Masters (when needed) stay **PNG** and live in assets/originals/ or GitHub.

---

## **🖼️ Size & Resolution Guidelines (LEAN Protocol)**

See SRAGI-VISUAL-SYSTEM-v1.0.md for exact pixel dimensions.

| Variant | Suffix | Use Case |
| :---- | :---- | :---- |
| **Hero** | \-hero | Frontpage/landing/roadmaps |
| **Content** | \-content | Articles/blog (Primary & Fallback) |
| **Token** | \-token | Cards/previews |
| **Tiny** | \-tiny | Thumbnails/LCP |
| **OG** | \-og | Social Sharing (Open Graph) |
| **Diagram** | .svg | Architecture/flows |

---

## **🧩 Naming Convention**

Use **kebab-case-lowercase**.

**Format:** \[project\]-\[description\]-\[year\]-\[ratio\]-\[suffix\].\[ext\]

**Examples:**

* sragi-logo.svg  
* nanobanana-architect-2026-16x9-hero.avif  
* nanobanana-architect-2026-16x9-content.jpg  
* sragi-os-interface-v2-token.avif

**Length rule:** Keep meaningful but concise (\~50 chars if possible).

---

## **🧭 Markdown & Web Referencing (Smart Shortcode)**

On sragi.org (WordPress):

Use the smart shortcode which handles Dual Core languages automatically.

HTML

```

[sragi_picture name="nanobanana-architect-2026-16x9" size="content"]

```

In documentation (Markdown):

Link to the raw GitHub AVIF for preview.

\!\[Nano Banana Architect\](../content/visuals/nanobanana-architect-2026-16x9-content.avif)

---

## **⚙️ Optimization Tools**

The **SRAGI-STD-FACTORY.bat** handles all optimization automatically using ImageMagick.

* **AVIF:** Quality 63, Speed 4  
* **JPG:** Quality 82, Progressive  
* **SVG:** Manual optimization via SVGO required.

---

## **🪞 Metadata & Attribution (Dual Core YAML)**

All images must have a corresponding .yaml file.

YAML

```

meta:
  id: "nanobanana-architect-2026-16x9"
display:
  title_en: "Nano Banana: The Architect"
  title_no: "Nano Banana: Arkitekten"
origin:
  tool: "Midjourney v6"
  license: "CC-BY-SA-4.0"
ethics:
  disclosure: true

```

---

## **🔒 Security Notes**

* ❌ No embedded JavaScript in SVG (XSS prevention)  
* ✅ Images are static assets only (never executed)  
* ✅ Avoid sensitive data in visuals  
* ✅ AI renders: disclose tool \+ prompt; avoid deceptive depictions

---

## **📋 Pre-Commit Checklist**

* \[ \] Processed via SRAGI-STD-FACTORY.bat?  
* \[ \] 6 files generated (Hero, Content, Fallback, Token, Tiny, OG)?  
* \[ \] YAML file created with Dual Core (NO+EN) data?  
* \[ \] Committed to /content/visuals/?

---

## **🌐 Integration Strategy**

| Layer | Source | Purpose |
| :---- | :---- | :---- |
| **GitHub** | /content/visuals/ | Version control \+ SSOT Metadata |
| **Web** | WP Uploads | Fast delivery (AVIF \+ JPG fallback) |
| **Archive** | /assets/originals/ | Master PNGs (Token seeds) |

---

## **📜 License**

Each image must carry its own license or rights statement. Many existing image records specify CC-BY-SA-4.0; that choice is not a default for every image. Third-party rights and source provenance remain applicable.

**© 2026 Rune Solberg / Neptunia Media AS**



