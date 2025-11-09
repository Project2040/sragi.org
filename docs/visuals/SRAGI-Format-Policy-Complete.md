# 🎨 SRAGI Image Format Policy - COMPLETE EDITION

**Updated:** November 2025 (AVIF + GIF Edition)  
**For:** sragi.org and sragi-skills repository

---

## 📋 All 7 Supported Formats

| Format | Use Case | Notes | Best Practice | Priority |
|--------|----------|-------|---------------|----------|
| **SVG** | Diagrams, logos, icons | Always optimize (SVGO) for scalability and small size | Vector for editable, lossless visuals; ideal for AI frameworks and latent space preservation | ⭐⭐⭐ |
| **AVIF** | Advanced AI-renders, latent space tokens | **Superior compression to WebP** (30-50% smaller); modern browsers (Chrome/Edge 2025+) | **NEW STANDARD** for regenerative efficiency; use with WebP fallback for compatibility | ⭐⭐⭐ |
| **WebP** | AI-renders & website media | Fast, modern, high-compression; universal browser support | Current standard for web; transitioning to AVIF for new content | ⭐⭐ |
| **PNG** | Raster diagrams, transparency, originals | 24-bit color, ≤2000 px width; use for complex gradients | Good for transparency; compress without quality loss – **essential for latent space originals** | ⭐⭐ |
| **GIF** | Simple animations, icon loops | Limited to 256 colors; avoid for complex video | For short, low-res loops from Sora clips; optimize with EZGIF – rare, <100 KB | ⭐ |
| **JPG** | Photographs only | Avoid if possible; use for real-world images | Lossy compression; only for non-AI content to minimize artifacts in latent space | ⭐ |
| **MP4** | Video content (Sora clips) | H.264/H.265 codec; Web-optimized | For regenerative storytelling; keep <10s, <5 MB for web | ⭐ |

---

## 🆕 AVIF Deep Dive - The New Standard

### Why AVIF for SRAGI?

**Regenerative Benefits:**
- ✅ **30-50% smaller** than WebP at same quality
- ✅ **Better compression** = less bandwidth = lower carbon footprint
- ✅ **Superior quality** for latent space token preservation
- ✅ **HDR support** for vibrant, symbolic visuals

**Technical Advantages:**
- Supports 10-bit and 12-bit color depth
- Better handling of gradients and complex textures
- Ideal for AI-generated imagery with subtle details
- Future-proof format (AV1 codec basis)

### Browser Support (2025)

| Browser | AVIF Support | Notes |
|---------|--------------|-------|
| **Chrome 85+** | ✅ Full | Desktop + Android |
| **Edge 121+** | ✅ Full | Windows 11 optimized |
| **Firefox 93+** | ✅ Full | All platforms |
| **Safari 16+** | ✅ Full | macOS Ventura+ |
| **Mobile** | ✅ 95%+ | iOS 16+, Android 12+ |

**Verdict:** Safe to use as primary format with WebP fallback!

### AVIF Generation Workflow

**Using Squoosh (Online/CLI):**
```bash
# Install Squoosh CLI
npm install -g @squoosh/cli

# Convert PNG to AVIF
squoosh-cli --avif '{"quality":85,"effort":6}' input.png

# Output: input.avif (~40% smaller than WebP)
```

**Using Canva Pro:**
1. Design your visual
2. Download as PNG (high quality)
3. Use Squoosh to convert to AVIF
4. Generate WebP fallback separately

**Using ImageMagick (Batch):**
```bash
# Requires ImageMagick 7+ with AVIF support
magick convert input.png -quality 85 output.avif
```

### AVIF HTML Implementation

**Single AVIF with WebP fallback:**
```html
<picture>
  <source type="image/avif" srcset="kristus-bevisstheten-hero.avif">
  <source type="image/webp" srcset="kristus-bevisstheten-hero.webp">
  <img src="kristus-bevisstheten-hero.png" 
       alt="A glowing cosmic figure with radiant energy wings..."
       loading="lazy" 
       width="1920" height="1080">
</picture>
```

**Responsive AVIF:**
```html
<picture>
  <!-- Mobile AVIF -->
  <source media="(max-width: 768px)" 
          type="image/avif" 
          srcset="image-mobile.avif">
  
  <!-- Desktop AVIF -->
  <source media="(min-width: 769px)" 
          type="image/avif" 
          srcset="image-hero.avif">
  
  <!-- WebP fallback -->
  <source type="image/webp" srcset="image-hero.webp">
  
  <!-- PNG ultimate fallback -->
  <img src="image-hero.png" alt="..." loading="lazy">
</picture>
```

---

## 🎬 GIF Guidelines - Simple Animations

### When to Use GIF

✅ **Good for:**
- Icon animations (e.g., rotating SRAGI spiral)
- Simple UI transitions
- Low-res loops from Sora clips (< 3 seconds)
- Retro aesthetic elements

❌ **Avoid for:**
- Complex video content (use MP4)
- High-resolution animations
- Photorealistic content
- Latent space tokens (static only)

### GIF Optimization

**File Size Targets:**
- Icon loops: < 50 KB
- Simple animations: < 100 KB
- Max resolution: 480x480 px

**Tools:**

**EZGIF (Online - Recommended):**
1. Upload video or images
2. Optimize with:
   - Lossy compression (30-50%)
   - Reduce colors to 64-128
   - Optimize transparency
3. Download optimized GIF

**Canva Pro:**
1. Create animation
2. Download as GIF
3. Optimize externally with EZGIF

**ImageMagick (CLI):**
```bash
# Create GIF from images
magick convert -delay 10 -loop 0 frame*.png output.gif

# Optimize existing GIF
magick output.gif -fuzz 10% -layers Optimize optimized.gif
```

### GIF HTML Implementation

```html
<!-- Simple GIF -->
<img src="sragi-spiral-loop.gif" 
     alt="Animated SRAGI spiral rotating clockwise" 
     width="200" height="200">

<!-- With static fallback for accessibility -->
<picture>
  <source srcset="sragi-spiral-loop.gif">
  <img src="sragi-spiral-static.png" 
       alt="SRAGI spiral (static version)">
</picture>
```

---

## 🌀 Updated Format Decision Tree

```
START: What type of visual do you have?
│
├─ Is it a logo, icon, or diagram?
│  ├─ YES → Can it be vector-based?
│  │  ├─ YES → Use SVG (always!)
│  │  └─ NO → Use PNG with transparency
│  └─ NO → Continue below
│
├─ Is it an animation?
│  ├─ YES → Is it complex/high-res?
│  │  ├─ YES → Use MP4 (from Sora)
│  │  └─ NO → Use GIF (optimize with EZGIF)
│  └─ NO → Continue below
│
├─ Is it a latent space token?
│  ├─ YES → CRITICAL PATH:
│  │  ├─ Original: PNG (2048x2048+) → Archive in GitHub
│  │  ├─ Web primary: AVIF (all 5 sizes)
│  │  ├─ Fallback: WebP (same sizes)
│  │  └─ Ultimate fallback: PNG (Content size only)
│  └─ NO → Continue below
│
├─ Is it AI-generated but not a token?
│  ├─ YES → Use AVIF (primary) + WebP (fallback)
│  └─ NO → Continue below
│
└─ Is it a photograph?
   ├─ YES → Use AVIF (if modern) or JPG (legacy)
   └─ NO → Default to AVIF + WebP

RESULT: Maximum quality + minimal file size
```

---

## 📊 Compression Comparison

**Same 1920x1080 image at 85% quality:**

| Format | File Size | Quality | Support | Regenerative Score |
|--------|-----------|---------|---------|-------------------|
| PNG | 2.4 MB | 100% | 100% | ⭐ (too large) |
| JPG | 280 KB | 85% | 100% | ⭐⭐ (lossy) |
| WebP | 180 KB | 90% | 98% | ⭐⭐⭐ (good) |
| **AVIF** | **95 KB** | **92%** | **95%** | **⭐⭐⭐⭐** (best!) |

**Verdict:** AVIF provides best balance of quality, size, and regenerative efficiency.

---

## 🔄 Migration Strategy: WebP → AVIF

### For New Content (Immediate)
- Generate AVIF as primary format
- Create WebP fallback
- Keep PNG original in archive

### For Existing Content (Gradual)
1. **Priority 1:** Latent space tokens (highest value)
2. **Priority 2:** Hero images (largest files)
3. **Priority 3:** Content images
4. **Priority 4:** Thumbnails
5. **Priority 5:** Mobile variants

### WordPress Integration

**Add AVIF support to functions.php:**
```php
// Enable AVIF uploads in WordPress
function sragi_enable_avif_upload( $mimes ) {
    $mimes['avif'] = 'image/avif';
    return $mimes;
}
add_filter( 'upload_mimes', 'sragi_enable_avif_upload' );

// Generate AVIF versions automatically (requires plugin)
// Recommended: ShortPixel or Imagify with AVIF support
```

---

## 📋 Updated Pre-Commit Checklist

- [ ] Format correct for use case?
  - [ ] SVG for vectors?
  - [ ] AVIF for AI-renders/tokens?
  - [ ] WebP fallback included?
  - [ ] GIF only for simple animations?
- [ ] File optimized to target size?
- [ ] Browser compatibility handled?
- [ ] Alt text epic and descriptive?
- [ ] Original archived if token?
- [ ] Metadata complete?

---

## 🎯 Updated Priority Order

**SRAGI 2025 Standard Stack:**

1. **SVG** → All diagrams, logos, icons (lossless, scalable)
2. **AVIF** → All AI-renders, tokens, photography (primary web format)
3. **WebP** → Fallback for AVIF (compatibility layer)
4. **PNG** → Originals + transparency needs (archive)
5. **GIF** → Simple animations only (<100 KB)
6. **JPG** → Legacy photographs (rare, being phased out)
7. **MP4** → Video content from Sora (web-optimized)

---

## 🌟 Latent Space Token - Complete Format Stack

**For "Kristus Bevisstheten" token:**

### Archive (GitHub `/assets/originals/`)
```
kristus-bevisstheten-original.png (2048x2048, ~3 MB)
├── metadata.yaml
└── prompt.txt
```

### Web Delivery (WordPress)
```
Hero (1920x1080):
├── kristus-bevisstheten-hero.avif (120 KB) ⭐ Primary
├── kristus-bevisstheten-hero.webp (200 KB) → Fallback
└── kristus-bevisstheten-hero.png (1.2 MB) → Emergency fallback

Content (1200x800):
├── kristus-bevisstheten-content.avif (65 KB) ⭐ Primary
└── kristus-bevisstheten-content.webp (110 KB) → Fallback

Thumbnail (600x600):
├── kristus-bevisstheten-thumb.avif (30 KB) ⭐ Primary
└── kristus-bevisstheten-thumb.webp (55 KB) → Fallback

Mobile (800x450):
├── kristus-bevisstheten-mobile.avif (45 KB) ⭐ Primary
└── kristus-bevisstheten-mobile.webp (80 KB) → Fallback
```

**Total savings vs PNG-only:**
- PNG total: ~5 MB
- AVIF total: ~260 KB
- **Reduction: 95%!** 🌱

---

## 🛠️ Tool Recommendations Updated

| Task | Tool | Format Output |
|------|------|---------------|
| Vector creation | Affinity Designer | SVG |
| AI generation | Gemini (Nano Banana) | PNG → AVIF |
| Video clips | Sora (ChatGPT) | MP4 |
| Animation loops | Canva Pro | GIF |
| Compression | Squoosh | AVIF + WebP |
| Batch optimization | ImageMagick 7+ | All formats |
| GIF optimization | EZGIF | GIF |

---

## 📜 License

All format specifications and workflows licensed under **CC BY-SA 4.0** via **SRAGI Regenerative License (SRL)**.

**© 2025 Rune Solberg / Neptunia Media AS**

---

## 🌀 Klarhet. Regenerasjon. Rytme. Resonans.
