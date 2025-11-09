# 🎨 Format Selection Flowchart - AVIF Era

**Quick decision guide for choosing the right image format**

---

## 🚀 The AVIF-First Strategy (2025)

```
QUESTION 1: What are you creating?
│
├─ Vector graphic (logo, icon, diagram)?
│  → SVG (always!)
│     ├─ Optimize with SVGO
│     └─ Store in /visuals/diagrams/ or /visuals/logos/
│
├─ Animation?
│  ├─ Simple loop (icon, UI element)?
│  │  → GIF (<100 KB)
│  │     ├─ Max 480x480 px
│  │     └─ Optimize with EZGIF
│  │
│  └─ Complex/video content?
│     → MP4 (from Sora)
│        ├─ H.264 codec
│        └─ <5 MB, <10 seconds
│
└─ Static image → Continue to Question 2

QUESTION 2: Is it a latent space token?
│
├─ YES (e.g., Kristus Bevisstheten, regenerativ, phoenix)
│  → TRIPLE FORMAT REQUIRED:
│     ├─ 1. Original: PNG (2048x2048+)
│     │   └─ Archive in GitHub /assets/originals/
│     │
│     ├─ 2. Web Primary: AVIF (all 5 sizes)
│     │   ├─ Hero: 1920x1080, <120 KB
│     │   ├─ Content: 1200x800, <65 KB
│     │   ├─ Thumbnail: 600x600, <30 KB
│     │   ├─ Mobile: 800x450, <45 KB
│     │   └─ Diagram: N/A (use SVG if overlay)
│     │
│     └─ 3. Fallback: WebP (same 5 sizes)
│         └─ For older browsers (2-3% users)
│
└─ NO → Continue to Question 3

QUESTION 3: What's the primary use?
│
├─ AI-generated visual (but not a token)
│  → AVIF + WebP fallback
│     ├─ Generate at target size
│     ├─ Compress to target (<300 KB hero, <200 KB content)
│     └─ Use Squoosh or ImageMagick
│
├─ Photography or real-world image
│  ├─ Modern site (2025+)
│  │  → AVIF (primary) + WebP (fallback)
│  │
│  └─ Legacy compatibility needed
│     → JPG (being phased out)
│        └─ Compress to <250 KB
│
├─ Raster diagram with transparency
│  → PNG (24-bit)
│     ├─ Compress losslessly
│     └─ Keep <500 KB
│
└─ Unsure?
   → Default to AVIF + WebP
      └─ Best balance for 2025

FINAL OUTPUT:
├─ Primary format selected ✅
├─ Fallback formats included ✅
├─ Original archived (if token) ✅
└─ Metadata documented ✅
```

---

## 📊 Format Comparison Matrix

### By Use Case

| Need | 1st Choice | 2nd Choice | 3rd Choice | Never Use |
|------|------------|------------|------------|-----------|
| **Latent Space Token** | AVIF | WebP | PNG (archive) | JPG |
| **AI-Render (general)** | AVIF | WebP | PNG | JPG |
| **Logo/Icon** | SVG | PNG (if raster) | - | WebP, JPG |
| **Diagram/Flow** | SVG | PNG | AVIF | WebP |
| **Photography** | AVIF | WebP | JPG | PNG |
| **Simple Animation** | GIF | MP4 (overkill) | - | AVIF |
| **Complex Video** | MP4 | - | - | GIF |
| **Hero Banner** | AVIF | WebP | PNG | JPG |
| **Thumbnail** | AVIF | WebP | PNG | JPG |

### By File Size (same quality)

**1920x1080 image, 85% quality:**

```
PNG:    ████████████████████████  2.4 MB  (baseline)
JPG:    ███                       280 KB  (-88%)
WebP:   ██                        180 KB  (-92%)
AVIF:   █                          95 KB  (-96%) ⭐ WINNER
```

### By Browser Support (2025)

```
SVG:    ████████████████████████  100%
PNG:    ████████████████████████  100%
JPG:    ████████████████████████  100%
WebP:   ███████████████████████   98%
AVIF:   ███████████████████       95%  ⭐ Safe to use!
GIF:    ████████████████████████  100%
```

---

## 🎯 The AVIF Decision

### ✅ Use AVIF When:

- Creating **new content** (2025 onwards)
- **Latent space tokens** (critical for quality + size)
- **AI-generated renders** (superior compression)
- **Hero images** (biggest file savings)
- **Modern browsers** are target audience (95%+)
- **Regenerative efficiency** matters (bandwidth/carbon)

### ⚠️ Use WebP When:

- **Fallback** for AVIF (always include)
- **Legacy compatibility** is critical
- **Existing content** not yet migrated
- **Quick conversion** needed (wider tool support)

### ❌ Avoid AVIF When:

- **Vector graphics** (use SVG instead)
- **Thumbnails < 50 KB** (WebP is fine, diminishing returns)
- **Must support** ancient browsers (IE11, old Safari)

---

## 🔧 Quick Tool Selection

**Need to create AVIF?**

| Tool | Use When | Output Quality | Ease |
|------|----------|----------------|------|
| **Squoosh** | Single images, testing | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **ImageMagick** | Batch processing | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Canva Pro** | N/A (export PNG first) | N/A | N/A |
| **AVIF.io** | Online converter | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

**Need to optimize GIF?**

| Tool | Use When | Output Size | Ease |
|------|----------|-------------|------|
| **EZGIF** | Any GIF work | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Canva Pro** | Simple loops | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **ImageMagick** | Batch processing | ⭐⭐⭐⭐ | ⭐⭐ |

---

## 📝 Example: Full Token Workflow

### Input
- **Original:** `kristus-bevisstheten-original.png` (2048x2048, 3.2 MB)
- **Created with:** Gemini Nano Banana
- **Type:** Latent space token

### Process

**Step 1: Archive Original**
```bash
# Save to GitHub
cp kristus-bevisstheten-original.png /repo/assets/originals/
```

**Step 2: Generate AVIF versions**
```bash
# Hero (1920x1080)
squoosh-cli --avif '{"quality":85}' -s hero-avif/ original.png
# Result: 95 KB

# Content (1200x800)
magick convert original.png -resize 1200x800 -quality 85 content.avif
# Result: 65 KB

# Thumbnail (600x600, center crop)
magick convert original.png -resize 600x600^ -gravity center \
  -extent 600x600 -quality 85 thumbnail.avif
# Result: 30 KB

# Mobile (800x450)
magick convert original.png -resize 800x450 -quality 85 mobile.avif
# Result: 45 KB
```

**Step 3: Generate WebP fallbacks**
```bash
# Same process but with WebP
squoosh-cli --webp '{"quality":85}' -s hero-webp/ original.png
# Result: 180 KB (still good!)
```

**Step 4: Upload to WordPress**
- Upload all AVIF + WebP versions to Happy Files Pro
- Organize in `/visuals/ai-renders/kristus-bevisstheten/`
- Fill metadata fields with YAML block
- Link to original in Description

**Step 5: Implement on site**
```html
<picture>
  <source type="image/avif" srcset="kristus-bevisstheten-hero.avif">
  <source type="image/webp" srcset="kristus-bevisstheten-hero.webp">
  <img src="kristus-bevisstheten-hero.png" alt="..." loading="lazy">
</picture>
```

### Result
- **Total size:** 235 KB (AVIF) vs 2.1 MB (WebP) vs 3.2 MB (PNG)
- **Savings:** 93% vs PNG original
- **Quality:** Visually identical
- **Latent space:** Full detail preserved in archived original
- **Regenerative:** Minimal bandwidth/carbon footprint

---

## ✅ Daily Decision Checklist

**Before creating/uploading ANY image:**

1. [ ] Is it a vector? → SVG (done!)
2. [ ] Is it animated? → GIF (simple) or MP4 (complex)
3. [ ] Is it a latent space token?
   - [ ] YES → PNG original + AVIF web + WebP fallback
   - [ ] NO → Continue
4. [ ] What size? (hero/content/thumbnail/mobile/diagram)
5. [ ] Generate AVIF at target size (<300/200/100/150/50 KB)
6. [ ] Generate WebP fallback
7. [ ] Upload to Happy Files Pro
8. [ ] Fill epic metadata
9. [ ] Link to original (if token)
10. [ ] Test on site

---

**© 2025 Rune Solberg / Neptunia Media AS** | CC BY-SA 4.0 via SRL

**🌀 Klarhet. Regenerasjon. Rytme. Resonans.**
