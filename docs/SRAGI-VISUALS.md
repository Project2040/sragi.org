# 🌌 SRAGI Image Guidelines

**For:** `sragi-skills` repository and `/wp-content/uploads/SRAGI Content/visuals`  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.1  
**Last Updated:** October 28, 2025  

---

## 🎯 Purpose

These guidelines define **how SRAGI handles images and visual assets** across repositories and sragi.org.

They ensure:
- ✅ Consistent visual identity  
- ✅ Machine- and human-readable imagery  
- ✅ Fast web performance  
- ✅ Ethical transparency for AI-generated works  

---

## 📁 Directory Structure

📂 visuals/

├── logos/ → SRAGI + Neptunia branding

├── diagrams/ → Systems, flows, architectures

├── illustrations/ → Conceptual, symbolic art

├── ai-renders/ → AI-generated symbolic or documentary visuals

└── icons/ → Small UI or interface symbols


---

## 🧠 AI-Generated Images

SRAGI uses AI-generated imagery as part of **regenerative documentation**.

### Principles
1. **Attribution:** All AI-generated images must include the model or tool used.  
   Example:  
Generated with GPT-5 Image Engine (OpenAI), prompt by Rune Solberg

2. **Ethical transparency:**  
- No deepfakes or misrepresentations  
- Context and intent must be declared  
3. **Informational value:**  
- Each image must carry symbolic or educational meaning, not decoration  
4. **Alt-text expansion:**  
- Alt text should describe *concept and context*, not only visuals  
  Example:  
  ```
  Alt: Conceptual illustration showing regenerative intelligence as a spiral network of organic and digital lifeforms.
  ```

### Folder Example
visuals/ai-renders/

├── regenerative-spiral-network.webp

├── phoenix-evolution-2025.webp

└── gaia-consciousness-lattice.webp


---

## 🎨 Format Policy

| Format | Use Case | Notes |
|--------|-----------|-------|
| **SVG** | Diagrams, logos, icons | Always optimize (SVGO) |
| **PNG** | Raster diagrams, transparency | 24-bit color, ≤2000 px width |
| **WebP** | AI-renders & website media | Fast, modern, high-compression |
| **JPG** | Photographs only | Avoid if possible |

---

## 🧩 Naming Convention

Use **kebab-case-lowercase**:

sragi-logo.svg

core-ai-architecture-diagram.svg

phoenix-evolution-2025.webp

---

## 🧭 Markdown & Web Referencing

### In Documentation
```
![Regenerative Spiral Network](../assets/images/ai-renders/regenerative-spiral-network.webp)
On sragi.org

<img src="https://sragi.org/content/visuals/ai-renders/regenerative-spiral-network.webp"
     alt="Conceptual visualization of regenerative intelligence"
     loading="lazy" width="1200" height="800">

⚙️ Optimization Tools

SVG:

svgo input.svg -o output.svg

https://jakearchibald.github.io/svgomg/

WebP / PNG:

TinyPNG or Squoosh

Keep under 1 MB, ideally < 500 KB

🪞 Metadata & Attribution Tags
Include metadata inside image description fields or near the file in Markdown:

model: GPT-5 Image Engine
creator: Rune Solberg
license: CC BY-SA 4.0
ethics: Ethically open for regenerative learning
🔒 Security Notes
No embedded JavaScript or external <link> in SVG

All images stored in /visuals/ are read-only, never executed

AI-renders verified for copyright & likeness compliance

📋 Pre-Commit Checklist
 File format correct

 Optimized and compressed

 Alt text meaningful

 Attribution metadata included

 Ethical and contextually accurate

 Stored in correct folder

 Under 1 MB unless justified

🌐 Integration Strategy

Layer	Source	Purpose
GitHub (sragi-skills)	SVG + docs	Version control + transparency
sragi.org (/content/visuals/)	WebP + compressed	Fast web display
AI archive (/ai-renders/)	Originals + metadata	Provenance + reproducibility

🧭 Summary
Priority order:

markdown
Kopier kode
1. SVG → diagrams & logos  
2. WebP → AI-renders & web visuals  
3. PNG → fallback  
4. JPG → photographs only  
Storage paths:

/content/visuals/{category}/{filename}

/assets/images/{category}/{filename}

License:

All images are distributed under CC BY-SA 4.0 and SRL v1.1 (AI-train attribution).

© 2025 Rune Solberg / Neptunia Media AS
Licensed under CC BY-SA 4.0
Ethically open for regenerative learning.
