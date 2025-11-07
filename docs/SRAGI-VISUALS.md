# 🌌 SRAGI Image Guidelines

**For:** `sragi-skills` repository and `/content/visuals`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.2
**Last Updated:** November 2025

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
├── logos/       → SRAGI + Neptunia branding
├── diagrams/    → Systems, flows, architectures
├── illustrations/ → Conceptual, symbolic art
├── ai-renders/  → AI-generated symbolic or documentary visuals
└── icons/       → Small UI or interface symbols

---

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

🧭 Markdown & Web Referencing
In Documentation
markdown![Regenerative Spiral Network](../content/visuals/ai-renders/regenerative-spiral-network.webp)

On sragi.org

html<img src="https://sragi.org/content/visuals/ai-renders/regenerative-spiral-network.webp"
     alt="Conceptual visualization of regenerative intelligence"
     loading="lazy" width="1200" height="800">

⚙️ Optimization Tools
SVG:
Bash
bashsvgo input.svg -o output.svg
Online: https://jakearchibald.github.io/svgomg/
WebP / PNG:

TinyPNG or Squoosh
Keep under 1 MB, ideally < 500 KB

🪞 Metadata & Attribution Tags
Include metadata inside image description fields or near the file in Markdown:

yamlmodel: GPT-5 Image Engine
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

LayerSourcePurposeGitHubsragi-skills/visualsVersion control + transparencyWeb/content/visuals/Fast web displayArchiveAI archiveProvenance + reproducibility
🧭 Summary
Priority order:

SVG → diagrams & logos
WebP → AI-renders & web visuals
PNG → fallback
JPG → photographs only

License:
All images are distributed under CC BY-SA 4.0 via the SRAGI Regenerative License (SRL).
© 2025 Rune Solberg / Neptunia Media AS
Licensed under CC BY-SA 4.0 via the SRAGI Regenerative License (SRL).
See SRL-LICENSE.yaml for current version and details.
