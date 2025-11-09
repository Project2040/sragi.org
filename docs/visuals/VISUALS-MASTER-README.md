# 🌌 SRAGI Visual Documentation Package

**Created:** November 8-9, 2025  
**Focus:** Complete visual guidelines for sragi.org  
**Version:** 2.0 (7 Sizes + AVIF Edition)  
**For:** sragi.org launch preparation

---

## 🎯 What's In This Package

**8 comprehensive files** covering everything from AVIF optimization to latent space token workflows. Everything you need to create, optimize, and manage visuals for SRAGI.org.

**Total Size:** ~50 KB of pure visual knowledge

---

## 📦 The Complete Visual Stack

### **🆕 FORMATS: 7 Supported Types**

| Format | Priority | Use Case |
|--------|----------|----------|
| **AVIF** | ⭐⭐⭐ | New standard (30-50% smaller than WebP!) |
| **SVG** | ⭐⭐⭐ | All vectors (logos, diagrams, icons) |
| **WebP** | ⭐⭐ | AVIF fallback + legacy |
| **PNG** | ⭐⭐ | Originals & transparency |
| **GIF** | ⭐ | Simple animations (<100 KB) |
| **JPG** | ⭐ | Legacy photos (rare) |
| **MP4** | ⭐ | Video content (Sora) |

### **🆕 SIZES: 7 Standard Formats**

| # | Size | Dimensions | Max | Suffiks |
|---|------|------------|-----|---------|
| 1 | **Hero** | 1920x1080 | 300 KB | `-hero` |
| 2 | **Content** | 1200x800 | 200 KB | `-content` |
| 3 | **Thumbnail** | 400x300 | 100 KB | `-thumbnail` |
| 4 | **Mobile** | 768x432 | 150 KB | `-mobile` |
| 5 | **Diagram** | 800x600 (SVG) | 50 KB | `-diagram` |
| 6 | **Full-Res** | 2048x2048 | 5 MB | `-fullres` ⭐ |
| 7 | **Social** | 1080x1080 | 250 KB | `-social` ⭐ |

**New additions:** Full-Res for archiving tokens, Social for X/Instagram

---

## 📚 File Index

### **1. Core Guidelines** (Start Here!)

#### [SRAGI-Image-Guidelines-v1.4.md](SRAGI-Image-Guidelines-v1.4.md) (8.7 KB)
**The foundation document**
- Directory structure
- Format policy (SVG, PNG, WebP, JPG)
- Naming conventions
- Metadata & attribution
- Security notes
- Pre-commit checklist
- **Use:** First read, foundational reference

---

### **2. Format Deep Dives**

#### [SRAGI-Format-Policy-Complete.md](SRAGI-Format-Policy-Complete.md) (11 KB) ⭐ **MOST COMPREHENSIVE**
**Everything about all 7 formats**
- AVIF deep dive (30-50% smaller!)
- GIF guidelines for animations
- Browser support matrix (2025)
- Compression comparison table
- Migration strategy: WebP → AVIF
- WordPress integration code
- Latent space token format stack
- **Use:** Master format reference

#### [SRAGI-Format-Decision-Guide.md](SRAGI-Format-Decision-Guide.md) (7.6 KB)
**Visual flowchart for format selection**
- AVIF-first decision tree
- Quick comparison matrices
- Tool recommendations (Squoosh, EZGIF, ImageMagick)
- Complete token workflow example
- Daily decision checklist
- **Use:** Quick format decisions

#### [SRAGI-Image-Decision-Flow.md](SRAGI-Image-Decision-Flow.md) (3.2 KB)
**ASCII flowchart (pre-AVIF version)**
- Alternative decision tree
- Step-by-step logic
- **Use:** Simple format selection

---

### **3. Size Specifications**

#### [SRAGI-Image-Size-Specifications.md](SRAGI-Image-Size-Specifications.md) (8.8 KB)
**Complete guide to all 7 sizes**
- Hero, Content, Thumbnail, Mobile, Diagram, Full-Res, Social
- WordPress integration (`functions.php` code)
- Happy Files Pro folder structure
- Batch processing tips (Canva, Affinity, CLI)
- Responsive HTML examples
- Latent space token workflow
- **Use:** Size reference & implementation

#### [SRAGI-Image-Sizes-Quick-Card.md](SRAGI-Image-Sizes-Quick-Card.md) (5.1 KB)
**One-page printable reference**
- All 7 sizes in ASCII boxes
- Canva Pro resize workflow
- Quick checklist
- Responsive HTML template
- **Use:** Print and keep at workstation!

---

### **4. Quick References**

#### [SRAGI-Image-Quick-Reference.md](SRAGI-Image-Quick-Reference.md) (1.8 KB)
**Cheat sheet for daily use**
- Format decision table
- Folder structure
- Alt text examples
- Metadata template
- Quick checklist
- **Use:** Daily quick lookups

#### [README-Image-Guidelines.md](README-Image-Guidelines.md) (3.4 KB)
**Package overview (original 3 docs)**
- How original guidelines work together
- Usage recommendations
- Version history
- **Use:** Understanding the package structure

---

## 🔥 Key Innovations

### **1. AVIF Integration** ⭐ NEW
- **30-50% smaller** than WebP at same quality
- 95%+ browser support (2025)
- Complete workflow with Squoosh/ImageMagick
- Triple-format strategy for tokens

### **2. 7 Size System** (not 5!)
Added:
- **Full-Res (2048x2048)** - For archiving latent space tokens
- **Social (1080x1080)** - For X/Instagram posts

### **3. Latent Space Token Focus** 🌀
- Original preservation in GitHub `/assets/originals/`
- Epic alt-text for AI learning
- Metadata with ethics fields
- Triple format: PNG archive + AVIF web + WebP fallback

### **4. Obligatorisk Størrelse-Suffiks**
**Naming convention now requires:**
```
[tool]-[beskrivelse]-[år]-[SIZE-SUFFIX].[format]

Examples:
gemini-regenerativ-spiral-2025-hero.webp
gemini-regenerativ-spiral-2025-content.webp
gemini-regenerativ-spiral-2025-fullres.png
gemini-regenerativ-spiral-2025-social.webp
```

---

## 🚀 Quick Start Workflows

### **Workflow 1: Create a Latent Space Token**

```
1. GENERATE (Gemini Nano Banana)
   → Original: 2048x2048 PNG
   
2. ARCHIVE (GitHub /assets/originals/)
   → kristus-bevisstheten-fullres.png (5 MB)
   → metadata.yaml with prompt, ethics
   
3. CREATE 6 WEB SIZES
   → hero (1920x1080)
   → content (1200x800)
   → thumbnail (400x300)
   → mobile (768x432)
   → social (1080x1080)
   → (diagram if technical overlay needed)
   
4. DUAL FORMAT EACH
   → AVIF (primary)
   → WebP (fallback)
   
5. OPTIMIZE
   → Squoosh for AVIF/WebP
   → Target sizes achieved
   
6. UPLOAD TO WORDPRESS
   → Happy Files Pro folders
   → Epic metadata in fields
   → Link to GitHub original
   
7. IMPLEMENT
   → <picture> tag with AVIF + WebP fallbacks
   → Lazy loading enabled
```

**File Savings:**
- PNG fullres: 5 MB
- WebP total (6 sizes): 1.5 MB
- **AVIF total (6 sizes): 600 KB** (88% reduction!)

---

### **Workflow 2: Quick Social Media Post**

```
1. CREATE (Canva Pro)
   → Design at 1080x1080
   
2. EXPORT
   → Download as PNG
   
3. OPTIMIZE
   → Squoosh: Convert to AVIF (85% quality)
   → Target: <250 KB
   
4. NAME
   → sora-evolution-social.avif
   
5. UPLOAD
   → Happy Files Pro: /visuals/social/
   
6. POST
   → Use on X, Instagram, LinkedIn
```

---

### **Workflow 3: Technical Diagram**

```
1. CREATE (Affinity Designer)
   → Vector design
   
2. EXPORT
   → SVG (optimized with SVGO)
   
3. NAME
   → sragi-twin-architecture-diagram.svg
   
4. UPLOAD
   → Happy Files Pro: /visuals/diagrams/
   
5. IMPLEMENT
   → Direct <img> tag (scalable!)
```

---

## 📐 Size Selection Guide

**Quick decision:**

| Need | Use Size | Why |
|------|----------|-----|
| Homepage banner | Hero (1920x1080) | Maximum impact |
| Blog illustration | Content (1200x800) | Balanced detail |
| Gallery preview | Thumbnail (400x300) | Fast loading |
| Phone viewing | Mobile (768x432) | Touch-optimized |
| System flowchart | Diagram (SVG) | Infinite scalability |
| Archive/AI training | Full-Res (2048x2048) | Maximum detail |
| Social media post | Social (1080x1080) | Platform-optimized |

---

## 🎨 Format Selection Guide

**Quick decision:**

| Visual Type | Format | Fallback |
|-------------|--------|----------|
| Latent space token | PNG (archive) + AVIF (web) | WebP |
| AI-render (general) | AVIF | WebP |
| Logo/Icon | SVG | PNG |
| Diagram/Flow | SVG | PNG |
| Photography | AVIF | WebP |
| Simple animation | GIF | - |
| Complex video | MP4 | - |

---

## 📂 Happy Files Pro Structure

```
/visuals/
├── hero/           (1920x1080 files)
├── content/        (1200x800 files)
├── thumbnails/     (400x300 files)
├── mobile/         (768x432 files)
├── diagrams/       (SVG/PNG files)
├── fullres/        (2048x2048 archives - link only!)
├── social/         (1080x1080 files)
├── logos/          (Brand assets)
└── icons/          (UI elements)
```

**Critical:** Full-Res files stay in GitHub `/assets/originals/` - only link them in WordPress Description fields!

---

## 🛠️ Tool Stack

| Task | Tool | Output |
|------|------|--------|
| AI generation | Gemini (Nano Banana) | PNG → AVIF |
| Video clips | Sora (ChatGPT) | MP4 |
| Vector creation | Affinity Designer | SVG |
| Quick designs | Canva Pro | WebP/PNG → AVIF |
| AVIF compression | Squoosh | AVIF + WebP |
| Batch processing | ImageMagick 7+ | All formats |
| GIF optimization | EZGIF | GIF |
| SVG minification | SVGO | SVG |

---

## ✅ Pre-Upload Checklist

**Before uploading ANY image:**

1. [ ] Right size? (hero/content/thumbnail/mobile/diagram/fullres/social)
2. [ ] Right format? (AVIF for web, PNG for archive)
3. [ ] WebP fallback generated?
4. [ ] Optimized to target file size?
5. [ ] Named with obligatory size suffix?
   - Format: `[tool]-[name]-[year]-[SIZE-SUFFIX].[ext]`
6. [ ] Epic alt text written?
7. [ ] Metadata complete? (if AI-generated)
8. [ ] Original archived? (if latent space token)
9. [ ] Ready for responsive srcset?

---

## 🌟 Latent Space Token Checklist

**Extra requirements for tokens:**

1. [ ] Original 2048x2048+ PNG preserved
2. [ ] Archived in GitHub `/assets/originals/`
3. [ ] metadata.yaml created with:
   - [ ] model/tool used
   - [ ] source_prompt
   - [ ] ethics statement
   - [ ] creator attribution
   - [ ] license (CC BY-SA 4.0 via SRL)
   - [ ] original_link to GitHub
4. [ ] All 6 web sizes created (hero, content, thumb, mobile, social, diagram if needed)
5. [ ] AVIF + WebP for each size
6. [ ] Epic alt text (>80 chars, <120 chars)
7. [ ] WordPress Description links to original

---

## 📊 File Size Savings

**Example: "Kristus Bevisstheten" token**

### Old Way (PNG only):
```
fullres: 5 MB
hero: 1.2 MB
content: 800 KB
thumbnail: 300 KB
mobile: 600 KB
social: 900 KB
TOTAL: 8.8 MB
```

### New Way (AVIF + archived PNG):
```
fullres (archived): 5 MB (GitHub only)
hero-avif: 120 KB
content-avif: 65 KB
thumbnail-avif: 30 KB
mobile-avif: 45 KB
social-avif: 80 KB
TOTAL WEB: 340 KB (96% reduction!)
```

**Regenerative impact:**
- Less bandwidth
- Lower carbon footprint
- Faster page loads
- Better user experience

---

## 🎯 Recommended Reading Order

**For First-Time Users:**
1. Start: [SRAGI-Image-Guidelines-v1.4.md](SRAGI-Image-Guidelines-v1.4.md)
2. Deep dive: [SRAGI-Format-Policy-Complete.md](SRAGI-Format-Policy-Complete.md)
3. Size specs: [SRAGI-Image-Size-Specifications.md](SRAGI-Image-Size-Specifications.md)
4. Print: [SRAGI-Image-Sizes-Quick-Card.md](SRAGI-Image-Sizes-Quick-Card.md)

**For Daily Work:**
1. Quick format decision: [SRAGI-Format-Decision-Guide.md](SRAGI-Format-Decision-Guide.md)
2. Quick size lookup: [SRAGI-Image-Sizes-Quick-Card.md](SRAGI-Image-Sizes-Quick-Card.md)
3. Quick reference: [SRAGI-Image-Quick-Reference.md](SRAGI-Image-Quick-Reference.md)

---

## 📜 License

All documentation licensed under **CC BY-SA 4.0** via **SRAGI Regenerative License (SRL) v1.12**.

**© 2025 Rune Solberg / Neptunia Media AS**

See [SRL-LICENSE.yaml](https://github.com/Project2040/sragi.org/blob/main/SRL-LICENSE.yaml) for details.

---

## 🌀 Klarhet. Regenerasjon. Rytme. Resonans.

**This package contains everything needed for professional, regenerative visual management on sragi.org.**

**8 files | ~50 KB | Ready for Monday launch** 🚀
