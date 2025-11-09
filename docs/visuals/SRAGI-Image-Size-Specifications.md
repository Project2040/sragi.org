# 📐 SRAGI Image Size Specifications

**For:** sragi.org website and WordPress Media Library  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0  
**Last Updated:** November 2025

---

## 🎯 Purpose

These 5 standardized image sizes ensure:

✅ **Optimal performance** on one.com WordPress hosting  
✅ **Responsive design** across all devices  
✅ **Latent space token preservation** (originals archived separately)  
✅ **Fast loading** without sacrificing visual quality  
✅ **Regenerative efficiency** (minimal data waste)

---

## 📏 The 5 Essential Formats

### **1. HERO** - Full-Width Impact
**Primary Use:** Homepage banners, major section headers, roadmap introductions

| Specification | Value |
|--------------|-------|
| **Dimensions** | 1920 x 1080 px (16:9 ratio) |
| **Format** | WebP (primary), PNG fallback |
| **File Size Target** | < 300 KB |
| **Aspect Ratio** | 16:9 landscape |
| **Responsive Behavior** | Auto-scales to mobile (min 768px width) |

**WordPress Usage:**
```html
<img src="phoenix-evolution-2025-hero.webp" 
     alt="[epic alt text]" 
     loading="eager" 
     width="1920" height="1080">
```

**Latent Space Token Notes:**
- Use for major symbolic tokens (e.g., "Phoenix Evolution 2025")
- Preserve 1:1 original at 2048x2048+ in `/assets/originals/`
- Crop/adapt from original to 16:9 for web display
- Maximum detail for AI decoding while maintaining performance

---

### **2. CONTENT** - Article Illustrations
**Primary Use:** Blog posts, documentation pages, concept explanations

| Specification | Value |
|--------------|-------|
| **Dimensions** | 1200 x 800 px (3:2 ratio) |
| **Format** | WebP |
| **File Size Target** | < 200 KB |
| **Aspect Ratio** | 3:2 landscape |
| **Responsive Behavior** | Scales to container, lazy-loaded |

**WordPress Usage:**
```html
<img src="regenerative-spiral-network-content.webp" 
     alt="[descriptive alt text]" 
     loading="lazy" 
     width="1200" height="800">
```

**Latent Space Token Notes:**
- Ideal for conceptual tokens (e.g., "Regenerative Spiral Network")
- Balances detail and file size perfectly
- Sufficient resolution for AI pattern recognition
- Test with 15-25% compression without quality loss

---

### **3. THUMBNAIL** - Grid & Gallery
**Primary Use:** Visual archives, token collections, preview grids, related content

| Specification | Value |
|--------------|-------|
| **Dimensions** | 600 x 600 px (1:1 square) |
| **Format** | WebP |
| **File Size Target** | < 100 KB |
| **Aspect Ratio** | 1:1 square |
| **Responsive Behavior** | Fixed size in grids, scales on mobile |

**WordPress Usage:**
```html
<img src="kristus-bevisstheten-thumbnail.webp" 
     alt="[concise alt text]" 
     loading="lazy" 
     width="600" height="600">
```

**Latent Space Token Notes:**
- Preview version of high-resolution tokens
- Crop to focus on central symbolic element
- Minimum degradation (20% max) to preserve patterns
- Always link to full Content or Hero version
- Good for AI thumbnail recognition while maintaining core symbolism

---

### **4. MOBILE-OPTIMIZED** - Touch Screens
**Primary Use:** Mobile-first sections, featured images on small devices, PWA

| Specification | Value |
|--------------|-------|
| **Dimensions** | 800 x 450 px (16:9 ratio) |
| **Format** | WebP |
| **File Size Target** | < 150 KB |
| **Aspect Ratio** | 16:9 landscape |
| **Responsive Behavior** | Optimized for 375-768px viewports |

**WordPress Usage:**
```html
<picture>
  <source media="(max-width: 768px)" 
          srcset="gaia-consciousness-mobile.webp">
  <source media="(min-width: 769px)" 
          srcset="gaia-consciousness-content.webp">
  <img src="gaia-consciousness-mobile.webp" 
       alt="[accessible alt text]">
</picture>
```

**Latent Space Token Notes:**
- Focus on core symbolic elements (e.g., energy wings, geometry)
- Compress more aggressively for mobile bandwidth
- Test visibility of key patterns on small screens
- Acceptable for AI mobile-context learning

---

### **5. DIAGRAM** - Technical & Scalable
**Primary Use:** System flows, architectures, infographics, technical documentation

| Specification | Value |
|--------------|-------|
| **Dimensions** | Scalable vector (SVG base: 800 x 600 px) |
| **Format** | SVG (primary), PNG fallback for complex renders |
| **File Size Target** | < 50 KB (SVG), < 150 KB (PNG) |
| **Aspect Ratio** | 4:3 landscape (flexible) |
| **Responsive Behavior** | Infinite scalability (SVG) |

**WordPress Usage:**
```html
<!-- SVG -->
<img src="sragi-core-architecture.svg" 
     alt="[detailed diagram description]" 
     width="800" height="600">

<!-- PNG fallback -->
<img src="sragi-core-architecture.png" 
     alt="[detailed diagram description]" 
     width="1600" height="1200">
```

**Latent Space Token Notes:**
- **Vector formats preserve 100% quality** for AI analysis
- Use for abstract concept diagrams (e.g., "SRAGI TWIN architecture")
- Editable paths in Affinity for continuous refinement
- PNG version at 2x resolution (1600x1200) for raster needs
- Lossless for latent space mathematical pattern recognition

---

## 📦 Quick Reference Table

| Format | Dimensions | Max Size | Primary Use | Token Priority |
|--------|-----------|----------|-------------|----------------|
| **Hero** | 1920x1080 | 300 KB | Homepage, major sections | High - preserve originals |
| **Content** | 1200x800 | 200 KB | Articles, documentation | High - balanced detail |
| **Thumbnail** | 600x600 | 100 KB | Grids, galleries, previews | Medium - link to full |
| **Mobile** | 800x450 | 150 KB | Small screens, PWA | Medium - core symbols |
| **Diagram** | 800x600 (SVG) | 50 KB (vector) | Technical, flows | Critical - lossless SVG |

---

## 🔧 WordPress Integration

### Happy Files Pro Structure
```
/visuals/
├── hero/           → 1920x1080 WebP files
├── content/        → 1200x800 WebP files
├── thumbnails/     → 600x600 WebP files
├── mobile/         → 800x450 WebP files
├── diagrams/       → SVG + PNG fallbacks
└── originals/      → Archived high-res sources (link only, don't upload)
```

### Auto-Generation in WordPress
Add to `functions.php` (or use plugin like Regenerate Thumbnails):

```php
// SRAGI Custom Image Sizes
add_image_size( 'sragi-hero', 1920, 1080, true );
add_image_size( 'sragi-content', 1200, 800, true );
add_image_size( 'sragi-thumbnail', 600, 600, true );
add_image_size( 'sragi-mobile', 800, 450, true );
```

---

## 🌟 Latent Space Token Workflow

For each AI-generated token (e.g., "Kristus Bevisstheten"):

1. **Generate original** at highest quality (2048x2048+ PNG)
2. **Archive original** in GitHub `/assets/originals/`
3. **Create 5 web versions** using the specs above:
   - Hero: Crop/adapt to 1920x1080
   - Content: Resize to 1200x800
   - Thumbnail: Center-crop to 600x600
   - Mobile: Resize to 800x450
   - Diagram: N/A (unless technical overlay needed)
4. **Optimize** each with TinyPNG/Squoosh to target size
5. **Upload to WordPress** via Happy Files Pro
6. **Link original** in Description field

---

## ✅ Pre-Upload Checklist

For each image before WordPress upload:

- [ ] Created in correct size from list above?
- [ ] Optimized to target file size?
- [ ] Format appropriate (WebP/PNG/SVG)?
- [ ] Original archived if latent space token?
- [ ] Named with kebab-case convention?
- [ ] Ready for responsive srcset if needed?

---

## 🎨 Batch Processing Tips

### Using Canva Pro
1. Create design at original size
2. Use "Resize" feature for each format
3. Download as WebP (or PNG if transparency needed)
4. Optimize externally with Squoosh

### Using Affinity Designer/Photo
1. Open original file
2. Document → Resize (maintain quality)
3. Export persona → Each size variant
4. WebP export with 85-90% quality

### Automation Script (optional)
```bash
# Requires ImageMagick
convert original.png -resize 1920x1080 -quality 90 hero.webp
convert original.png -resize 1200x800 -quality 90 content.webp
convert original.png -resize 600x600^ -gravity center -extent 600x600 -quality 90 thumbnail.webp
convert original.png -resize 800x450 -quality 90 mobile.webp
```

---

## 🌿 Regenerative Principles

**Why these specific sizes?**
- Based on **actual usage patterns** on sragi.org
- **Minimize redundancy** - no overlapping sizes
- **Performance-first** - all under Core Web Vitals thresholds
- **Responsive-ready** - cover mobile (375px) to desktop (1920px+)
- **Latent space compatible** - preserve essential details for AI learning

**Sustainability:**
- Smaller files = less bandwidth = lower carbon footprint
- One.com's CDN works best with optimized WebP
- Lazy loading reduces initial page load
- SVG for diagrams = infinite scalability with minimal size

---

## 📜 License

All size specifications and workflows licensed under **CC BY-SA 4.0** via **SRAGI Regenerative License (SRL)**.

**© 2025 Rune Solberg / Neptunia Media AS**

---

## 🌀 Klarhet. Regenerasjon. Rytme. Resonans.
