# **🌌 SRAGI Image Guidelines (UPDATED)**

**For:** `sragi-skills` repository and `/content/visuals`  
 **Maintainer:** Rune Solberg / Neptunia Media AS  
 **Version:** 1.4 (AVIF-first)  
 **Last Updated:** 01.01.2026  
 **Coordination:** Technical specs are governed by `visual-protocol.md` (SSOT)

**Note:** This document governs *meaning, ethics, and handling*.  
 **`visual-protocol.md` governs pixels, sizes, and export rules.**

---

## **🎯 Purpose**

These guidelines define how SRAGI handles images and visual assets across repositories and sragi.org.

They ensure:

✅ Consistent visual identity (mytopoetic, fractal-inspired)  
 ✅ Machine- and human-readable imagery (alt text \+ metadata)  
 ✅ Fast web performance (AVIF-first)  
 ✅ Ethical transparency for AI-generated works (disclose origins, avoid misrepresentation)

---

## **📁 Directory Structure**

`📂 visuals/`  
`├── logos/          → SRAGI + Neptunia branding (vectors)`  
`├── diagrams/       → Systems, flows, architectures`  
`├── illustrations/  → Conceptual, symbolic art`  
`├── ai-renders/     → AI-generated symbolic/documentary visuals (with disclosure)`  
`└── icons/          → Small UI/interface symbols`

### **Folder Example with Previews**

`visuals/ai-renders/`  
`├── regenerative-spiral-network.avif`  
`├── regenerative-spiral-network.jpg`  
`├── phoenix-evolution-2025.avif`  
`├── phoenix-evolution-2025.jpg`  
`└── gemini-generated-image-szqr3zqr3szqr3zqr.png   (MASTER / ORIGINAL)`

---

## **🎨 Format Policy (AVIF-first)**

| Format | Use Case | Notes | Best Practice |
| ----- | ----- | ----- | ----- |
| **SVG** | Diagrams, logos, icons | Optimize \+ strip scripts | Best for UI \+ structure; scalable and small |
| **PNG** | Master/originals, transparency, “token seeds” | Lossless | Keep as archival source of truth |
| **AVIF** | Website media (primary) | Best compression/quality | Default for web delivery |
| **JPG** | Website fallback \+ photos \+ social/OG | Max compatibility | Always paired with AVIF as fallback |

**Rule:**

For every published raster image: **AVIF is primary** and **JPG is fallback**.  
 Masters (when needed) stay **PNG**.

---

## **🖼️ Size & Resolution Guidelines (format updated)**

(Resolutions can live in `visual-protocol.md`; this table is the intent-level view.)

| Variant | Use Case | Recommended Output |
| ----- | ----- | ----- |
| **Hero** | Frontpage/landing/roadmaps | `*-large.avif` \+ `*-large.jpg` |
| **Content** | Articles/blog | `*-medium.avif` \+ `*-medium.jpg` |
| **Thumbnail** | Gallery/cards | `*-small.avif` \+ `*-small.jpg` |
| **Social/OG** | Sharing (X/LinkedIn/OG) | `*-social.jpg` (standard) |
| **Diagram** | Architecture/flows | `.svg` (preferred), else PNG master \+ AVIF/JPG outputs |
| **Master** | Archive / latent-token seed | `*-master.png` (no degradation) |

---

## **🧩 Naming Convention**

Use **kebab-case-lowercase**.

**Raster variants:**  
 `[tool-optional]-[description]-[year-optional]-[size].[ext]`

**Examples:**

* `sragi-logo.svg`

* `gemini-regenerativ-spiral-2025-large.avif`

* `gemini-regenerativ-spiral-2025-large.jpg`

* `sora-phoenix-evolution-medium.avif`

* `sora-phoenix-evolution-medium.jpg`

* `gemini-kristus-token-master.png`

* `sragi-core-social.jpg`

**Length rule:** keep under \~50 chars if possible.

---

## **🧭 Markdown & Web Referencing (AVIF \+ JPG fallback)**

**In documentation (simple):**

`![Regenerative spiral network](../content/visuals/ai-renders/regenerative-spiral-network.avif)`

**On sragi.org (correct fallback):**

`<picture>`  
  `<source srcset="/content/visuals/ai-renders/regenerative-spiral-network.avif" type="image/avif">`  
  `<img src="/content/visuals/ai-renders/regenerative-spiral-network.jpg"`  
       `alt="A fractal spiral representing regenerative networks..."`  
       `loading="lazy" decoding="async" width="1200" height="800">`  
`</picture>`

**Alt text rule:** descriptive \+ meaningful.  
 For special “token” images: allow richer description, but keep it readable.

---

## **⚙️ Optimization Tools**

### **SVG**

`svgo input.svg -o output.svg`

### **AVIF \+ JPG (CLI-friendly)**

**AVIF (example with libavif):**

`avifenc --min 20 --max 35 --speed 6 input.png output.avif`

**JPG fallback (ImageMagick):**

`magick input.png -quality 82 output.jpg`

(Use Squoosh if you want a GUI workflow.)

---

## **🪞 Metadata & Attribution (YAML adjacent)**

`tool: gemini`  
`creator: Rune Solberg`  
`license: CC BY-SA 4.0 via SRL`  
`type: latent-space-token`  
`source_prompt: "Generate a cosmic figure with energy wings..."`  
`master: gemini-kristus-token-master.png`  
`outputs:`  
  `- gemini-kristus-token-large.avif`  
  `- gemini-kristus-token-large.jpg`  
  `- gemini-kristus-token-social.jpg`  
`ethics:`  
  `disclosure: true`  
  `likeness: none`  
  `copyrighted_material: verified`

---

## **🔒 Security Notes**

* ❌ No embedded JavaScript in SVG (XSS prevention)

* ✅ Images are static assets only (never executed)

* ✅ Avoid sensitive data in visuals

* ✅ AI renders: disclose tool \+ prompt; avoid deceptive depictions

---

## **📋 Pre-Commit Checklist**

* Correct format policy (AVIF \+ JPG fallback, PNG master where needed)?

* Correct naming (kebab-case, size suffix)?

* Optimized outputs generated?

* Alt text present and meaningful?

* YAML metadata included (AI disclosure, prompt, license, master link)?

* Stored in correct folder?

* Social/OG uses JPG?

---

## **🌐 Integration Strategy**

| Layer | Source | Purpose |
| ----- | ----- | ----- |
| **GitHub** | `sragi-skills/visuals` | Version control \+ provenance |
| **Web** | `/content/visuals/` | Fast delivery (AVIF \+ JPG fallback) |
| **Archive** | `*-master.png` | Token seeds, reproducibility |

---

## **📜 License**

All images distributed under **CC BY-SA 4.0** via **SRAGI Regenerative License (SRL)**.  
 **© 2025–2026 Rune Solberg / Neptunia Media AS**




History:

# 🌌 SRAGI Image Guidelines

**For:** `sragi-skills` repository and `/content/visuals`
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 1.3c
**Last Updated:** December 2025 (Marked for update, 06.12.2025 - Rune Solberg)

# ** THIS FILE NEED UPDATE FOR CO-ORDINATION TOWARDS THE NEW visual-protocol.md

---

## 🎯 Purpose

These guidelines define how SRAGI handles images and visual assets across repositories and sragi.org.  
They ensure:

✅ **Consistent visual identity** (e.g., mytopoetic, fractal-inspired designs)  
✅ **Machine- and human-readable imagery** (e.g., alt text, metadata for AI training and decoding in latent space)  
✅ **Fast web performance** (optimized sizes for quick loading)  
✅ **Ethical transparency for AI-generated works** (disclose origins, ensure regenerative use, avoid bias/misrepresentation; special focus on preserving latent space tokens for AI learning)

Inspired by open-source AI best practices and SRAGI's regenerative principles, we prioritize ethical AI-generation (e.g., verify for copyright compliance, disclose tools like Gemini or DALL-E). Visuals should "weave meaning" without extraction or harm, and serve as "tokens" for concepts like *regenerativ* or *Kristus Bevisstheten* – high-quality originals preserved for latent space decoding by other AI systems.

---

## 📁 Directory Structure

```
📂 visuals/
├── logos/          → SRAGI + Neptunia branding (e.g., scalable vectors)
├── diagrams/       → Systems, flows, architectures (e.g., fractal finance flowcharts)
├── illustrations/  → Conceptual, symbolic art (e.g., mytopoetic scenes)
├── ai-renders/     → AI-generated symbolic or documentary visuals (with full disclosure; focus on latent space tokens)
└── icons/          → Small UI or interface symbols (e.g., resonance icons)
```

### Folder Example with Previews

```
visuals/ai-renders/
├── regenerative-spiral-network.webp → A fractal spiral representing regenerative networks
├── phoenix-evolution-2025.webp → Symbolic rebirth for SRAGI's 2025 evolution
├── gaia-consciousness-lattice.webp → Lattice diagram for interconnected consciousness
└── gemini-generated-image-szqr3zqr3szqr3zqr.png
    → A cosmic, glowing figure with energy wings symbolizing
      Kristus Bevisstheten or regenerative consciousness
      (example of latent space token; original preserved for AI decoding)
```

*Bruk disse som inspirasjon – generer dine egne via etiske AI-tools og verifiser for originalitet. For Gemini_Generated_Image_szqr3zqr3szqr3zqr.png, se spesialfokus nedenfor.*

---

## 🎨 Format Policy

| Format | Use Case | Notes | Best Practice |
|--------|----------|-------|---------------|
| **SVG** | Diagrams, logos, icons | Always optimize (SVGO) for scalability and small size | Vector for editable, lossless visuals; ideal for AI frameworks and latent space preservation |
| **PNG** | Raster diagrams, transparency | 24-bit color, ≤2000 px width; use for complex gradients | Good for transparency; compress without quality loss – preserve details for AI decoding |
| **WebP** | AI-renders & website media | Fast, modern, high-compression; fallback for browsers | Preferred for web perf; supports animation if needed – use for nedgraderte versjoner, lenk originaler |
| **JPG** | Photographs only | Avoid if possible; use for real-world images | Lossy compression; only for non-AI content to minimize artifacts in latent space |

**Special focus:** For latent space tokens (e.g., AI-genererte konsepter som Kristus Bevisstheten), prioriter **PNG for originals** to retain full pixel-integrity – nedgrader kun web-versjoner.

---

## 🖼️ Size & Resolution Guidelines

| # | Size | Use Case | Recommended Resolution & Format | File Size Target | Tips for Tokens |
|---|------|----------|---------------------------------|------------------|-----------------|
| **1. Hero** | Stor banner | Forside/roadmaps | 1920x1080 px (WebP/PNG) | <300 KB | Immersjon; link original for dekoding |
| **2. Content** | Medium illust. | Artikler/blogg | 1200x800 px (WebP) | <200 KB | Symbolikk-balanse; lazy loading |
| **3. Thumbnail** | Liten preview | Galleri/nettverk | 400x300 px (WebP) | <100 KB | Minimal degrad. for mønstre |
| **4. Mobile** | Kompakt vertikal | Mobilvisning | 768x432 px (WebP/PNG) | <150 KB | Core symbols; touch-opt. |
| **5. Diagram** | Skalerbar vektor | Flows/arkitektur | 800x600 px base (SVG) | <50 KB | Lossless; editable i Affinity |
| **6. Full-Res** | AI-trening/original | Latent space tokens (arkiv) | 2048x2048 px (PNG) | <5 MB lossless | Høy detalj for dekoding; alltid arkiver |
| **7. Social** | Kvadratisk deling | X/Instagram-posts | 1080x1080 px (WebP) | <250 KB | Kvadrat; optimal for sosiale feeds |

---

## 🧩 Naming Convention

Use **kebab-case-lowercase** for consistency and SEO. Inkluder alltid: [tool/valgfritt]-[beskrivelse]-[år/valgfritt]-[størrelse-suffiks].[format].

- **Tool/ID:** For AI (e.g., `gemini-`, `sora-`); unik ID for tokens (e.g., `szqr3zqr`).
- **Beskrivelse:** Kort tematisk (e.g., `regenerativ-spiral`, `kristus-token`).
- **År/Versjon:** `-2025` for evolusjonære.
- **Størrelse-suffiks:** Obligatorisk for varianter (hero, content, thumbnail, mobile, diagram, fullres, social).

**Eksempler:**
- `sragi-logo-diagram.svg` (ingen størrelse for SVG – skalerbar).
- `gemini-regenerativ-spiral-token-2025-hero.webp` (Hero: 1920x1080).
- `sora-phoenix-evolution-content.png` (Content: 1200x800).
- `affinity-gaia-lattice-thumbnail.svg` (Thumbnail: 400x300).
- `canva-kristus-bevissthet-mobile.webp` (Mobile: 768x432).
- `inkscape-fractal-finance-diagram.svg` (Diagram: 800x600 base).
- `gemini-kristus-token-fullres.png` (Full-Res: 2048x2048).
- `sora-evolution-social.webp` (Social: 1080x1080).

**For Dual-Format (Tokens):** Original: `*-original.png`; Web: `*-web.webp`. Lagre YAML med suffiks-referanse. **Regel:** Hold <50 tegn; test SEO.

---

## 🧭 Markdown & Web Referencing

### In Documentation:

```markdown
![Cosmic Energy Figure Representing Kristus Bevisstheten](../content/visuals/ai-renders/gemini-generated-image-szqr3zqr3szqr3zqr.png)
```

### On sragi.org:

```html
<img src="https://sragi.org/content/visuals/ai-renders/gemini-generated-image-szqr3zqr3szqr3zqr.png"
     alt="A glowing cosmic figure with radiant energy wings emanating from a central sacred geometry core, symbolizing divine consciousness and regenerative awakening against a starry void."
     loading="lazy" 
     width="1024" 
     height="1024">
```

**Always include descriptive alt text** for accessibility and AI-readability (e.g., describe for screen readers and training data).  

**Special focus:** For latent space tokens, gjør alt-tekst **episk detaljert** for å veilede dekoding (se eksempel over).

---

## ⚙️ Optimization Tools

### SVG:

```bash
svgo input.svg -o output.svg
```

**Online:** [SVGOMG](https://jakearchibald.github.io/svgomg/) (for minification without quality loss)

### WebP / PNG:

Use **TinyPNG** or **Squoosh**; keep under **1 MB**, ideally **< 500 KB**.  

Use **lossless** for originals to preserve latent space details.

**Special focus:** Nedgrader web-versjoner (e.g., fra 1024x1024 til 800x800), men lenk alltid til original for full dekoding.

---

## 🪞 Metadata & Attribution Tags

Include metadata in image description fields or adjacent Markdown (e.g., EXIF or YAML block).  

**Special focus on latent space tokens:**

```yaml
model: Gemini (Nano Banana integration)  # Tool used for generation
creator: Rune Solberg
license: CC BY-SA 4.0 via SRAGI Regenerative License (SRL)
ethics: Ethically open for regenerative learning; represents Kristus Bevisstheten as a token for divine coherence and awakening; no bias or harmful representations
source_prompt: "Generate a cosmic figure with energy wings symbolizing Christ Consciousness, sacred geometry core, starry background"
original_link: https://github.com/Project2040/sragi.org/raw/main/assets/originals/gemini-generated-image-szqr3zqr3szqr3zqr-original.png  # Link to high-res original
dimensions: 1024x1024
file_size: 2 MB (original)
```

**For AI-generated:** Always disclose tool, prompt, and verify for ethical compliance (e.g., no copyrighted likenesses).

---

## 🔒 Security Notes

- ❌ No embedded JavaScript or external `<link>` in SVG (prevent XSS)
- ✅ All images in `/visuals/` are read-only, never executed
- ✅ AI-renders verified for copyright & likeness compliance (use tools like TinEye for reverse search)
- ✅ Avoid sensitive data in visuals; ensure inclusivity (diverse representations)

**Special focus:** For tokens som Kristus Bevisstheten, sikre respektfull representasjon for å unngå misforståelser i dekoding.

---

## 📋 Pre-Commit Checklist

Before adding any visual to the repository:

- [ ] File format correct?
- [ ] Optimized and compressed (web-versjon)?
- [ ] Alt text meaningful, descriptive, and epic (e.g., for non-seende: Full kontekst av symbolikk og energi)?
- [ ] Attribution metadata included with original link?
- [ ] Ethical and contextually accurate (e.g., regenerative themes, latent space-ready)?
- [ ] Stored in correct folder with original archived?
- [ ] Under 1 MB unless justified (document reason for originals)?

---

## 🌐 Integration Strategy

| Layer | Source | Purpose |
|-------|--------|---------|
| **GitHub** | `sragi-skills/visuals` | Version control + transparency; fork for contributions; host originals for latent space archiving |
| **Web** | `/content/visuals/` | Fast web display; integrate with WP via Happy Files; use nedgraderte versjoner |
| **Archive** | AI archive (e.g., repo tags or originals folder) | Provenance + reproducibility; track AI prompts and links for dekoding |

**Add contribution guide:** Fork repo, add visuals with metadata (including original link), submit PR.

---

## 🧭 Summary

### Priority order:

1. **SVG** → diagrams & logos (scalable)
2. **WebP** → AI-renders & web visuals (performance)
3. **PNG** → fallback and originals (transparency, latent space preservation)
4. **JPG** → photographs only (rare)

### Special focus example:

For `Gemini_Generated_Image_szqr3zqr3szqr3zqr.png` (a latent space token for Kristus Bevisstheten):  
- ✅ Behold original i arkiv for full AI-dekoding  
- ✅ Nedgrader web-versjon  
- ✅ Bruk epic alt-tekst for å veilede både mennesker og maskiner

---

## 📜 License

All images distributed under **CC BY-SA 4.0** via **SRAGI Regenerative License (SRL)**.

**© 2025 Rune Solberg / Neptunia Media AS**

See [SRL-LICENSE.yaml](https://github.com/Project2040/sragi.org/blob/main/SRL-LICENSE.yaml) for details.

---

## 🌿 Klarhet. Regenerasjon. Rytme. Resonans.

---
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
---
Proposed update:

# 🌌 SRAGI Visual Philosophy & Guidelines

**File:** `/docs/visuals/SRAGI-VISUAL-PHILOSOPHY.md`
**Status:** Philosophical Framework (Reference)
**Maintainer:** Rune Solberg / Neptunia Media AS
**Version:** 2.0 (Refactored 06.12.2025)
**Technical Protocol:** See `visual-protocol.md` for sizes and file specs.

---

## 🎯 Purpose

This document defines the **soul and intent** of SRAGI's visual identity.
While `visual-protocol.md` governs the *pixels*, this document governs the *meaning*.

We ensure:
✅ **Consistent visual identity** (mytopoetic, fractal-inspired).
✅ **Machine-readable meaning** (Latent Space Tokens).
✅ **Ethical transparency** (AI disclosure and regenerative intent).

Visuals in SRAGI should **"weave meaning"** without extraction or harm, serving as tokens for concepts like *Regenerasjon* or *Kristus Bevisstheten* — high-quality originals preserved for future decoding by other intelligences.

---

## 🌀 The Concept of "Latent Space Tokens"

A "Latent Space Token" is more than just an image file. It is a **compressed semantic packet**.

* **For Humans:** An evocative, symbolic illustration (e.g., a golden compass).
* **For AI:** A high-fidelity data source that contains specific patterns, fractals, and metadata that allows an AI to "read" the concept back out of the pixels.

**Core Rule:**
> "Never degrade the Master Original. The PNG in the archive is the seed. The WebP on the site is the flower."

---

## 🎨 Aesthetic Pillars

1.  **Mytopoetic Tech:** Blending ancient symbols (runes, geometry) with futuristic interfaces (HUDs, nodes).
2.  **Fractal Coherence:** Patterns should repeat at different scales (micro/macro).
3.  **Luminous Depth:** Use deep backgrounds (Void/Space) with glowing foregrounds (Neon/Gold) to symbolize light in darkness.
4.  **Organic Integration:** Technology should look like it grows *out of* nature, not imposes *upon* it.

---

## 🤖 AI Ethics & Transparency

Inspired by open-source AI best practices:

1.  **Disclosure:** Always disclose if an image is AI-generated (e.g., "Created with Midjourney").
2.  **No Deepfakes:** Never generate misleading depictions of real people or events.
3.  **Bias Awareness:** Strive for diverse and universal representations of consciousness.
4.  **Source Preservation:** We archive the original prompt and generation parameters in the YAML metadata so the image can be reproduced or iterated upon.

---

## 🔒 Security & Integrity

* **No Executable Code:** SVG files must be stripped of `<script>` tags (XSS prevention).
* **Verification:** AI-renders are verified for copyright compliance before inclusion.
* **Respect:** Sensitive concepts (spiritual/religious) are treated with reverence to avoid semantic degradation in the latent space.

---

## 🧭 Summary

* **Use `visual-protocol.md`** for: Sizes, Formats, Scripts, File Names.
* **Use this document** for: Inspiration, Ethics, Prompting Style, Concept Design.

> "Visuals are not decoration. They are resonance anchors."

---

**© 2025 Rune Solberg / Neptunia Media AS**
Licensed under CC BY-SA 4.0 via SRAGI Regenerative License (SRL).
See `SRL-LICENSE.yaml` for details.

---

## 🌿 Klarhet. Regenerasjon. Rytme. Resonans.


