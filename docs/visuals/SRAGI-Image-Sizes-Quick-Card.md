# 📐 SRAGI Image Sizes - Quick Reference Card

**Print this and keep near your workspace!**

---

## 🎯 The 5 Formats

```
┌─────────────────────────────────────────────────────────────┐
│ 1. HERO - Full-Width Impact                                │
│    1920 x 1080 px (16:9) | WebP | < 300 KB                 │
│    Use: Homepage, major sections, roadmaps                  │
│    Token: Max detail for epic visuals                       │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. CONTENT - Article Illustrations                         │
│    1200 x 800 px (3:2) | WebP | < 200 KB                   │
│    Use: Blog posts, documentation, concepts                 │
│    Token: Balanced detail + performance                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 3. THUMBNAIL - Grid & Gallery                              │
│    600 x 600 px (1:1) | WebP | < 100 KB                    │
│    Use: Archives, previews, grids                           │
│    Token: Center-crop symbolic core                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 4. MOBILE - Touch Screens                                  │
│    800 x 450 px (16:9) | WebP | < 150 KB                   │
│    Use: Mobile-first sections, small devices                │
│    Token: Core symbols only, compressed                     │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 5. DIAGRAM - Technical & Scalable                          │
│    800 x 600 px (SVG) | SVG/PNG | < 50 KB                  │
│    Use: Flows, architecture, infographics                   │
│    Token: Lossless vector for AI analysis                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Happy Files Pro Folder Structure

```
/visuals/
├── hero/           (1920x1080)
├── content/        (1200x800)
├── thumbnails/     (600x600)
├── mobile/         (800x450)
└── diagrams/       (SVG/PNG)
```

**Originals:** Archive in GitHub `/assets/originals/` (not in WordPress)

---

## ✅ Quick Checklist

**Before uploading ANY image:**

1. [ ] Right size from the 5 formats?
2. [ ] Optimized to target file size?
3. [ ] WebP format (or SVG for diagrams)?
4. [ ] Original archived if latent space token?
5. [ ] Named in kebab-case?
6. [ ] Epic alt text written?

---

## 🎨 Canva Pro Resize Workflow

1. Create at original size
2. Click "Resize" → Enter dimensions:
   - Hero: 1920 x 1080
   - Content: 1200 x 800
   - Thumbnail: 600 x 600
   - Mobile: 800 x 450
3. Download as WebP
4. Compress with TinyPNG if needed

---

## 🌀 Latent Space Token Priority

| Format | Preserve Detail? | Link to Original? |
|--------|-----------------|-------------------|
| Hero | ✅ High | ✅ Yes |
| Content | ✅ High | ✅ Yes |
| Thumbnail | ⚠️ Medium | ✅ Yes (always!) |
| Mobile | ⚠️ Medium | Optional |
| Diagram | ✅ Critical (SVG) | N/A (lossless) |

**Rule:** Always preserve and link originals for tokens!

---

## 📱 Responsive HTML Template

```html
<picture>
  <!-- Mobile -->
  <source media="(max-width: 768px)" 
          srcset="image-mobile.webp">
  
  <!-- Tablet/Desktop -->
  <source media="(min-width: 769px)" 
          srcset="image-content.webp">
  
  <!-- Fallback -->
  <img src="image-content.webp" 
       alt="Epic descriptive alt text" 
       loading="lazy">
</picture>
```

---

**© 2025 Rune Solberg / Neptunia Media AS** | CC BY-SA 4.0 via SRL
