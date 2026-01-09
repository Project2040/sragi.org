# 🏭 SRAGI Visual System v1.0

**Status:** PRODUCTION READY  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.0 (Claude + Gemini Unified)  
**Last Updated:** January 2026  
**License:** CC BY-SA 4.0 via SRAGI Regenerative License (SRL)

---

## 🎯 Formål

Et komplett, automatisert system for bildebehandling i SRAGI-økosystemet:

- **Lokal prosessering** → AVIF primary + JPG universal fallback
- **Automatisk sortering** → HappyFiles-kategorier
- **Metadata-synkronisering** → GitHub YAML → WordPress
- **CDN-leveranse** → Bunny.net med optimal caching

---

## 📦 Innhold

| Fil | Beskrivelse | Hvor |
|-----|-------------|------|
| `SRAGI-STD-FACTORY-v3.4.bat` | Windows batch for bildeprosessering | Lokal maskin |
| `sragi-visual-factory-controller-v5.3.php` | WordPress snippet (WPCodeBox) | WordPress |
| `TEMPLATE-VISUAL-v1.1.yaml` | Metadata-mal for hvert bilde | GitHub |

---

## 🔄 Komplett Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SRAGI VISUAL WORKFLOW                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. SKAPELSE (Canva/AI)                                         │
│     └── Master PNG (3000x2000 for 3:2, etc.)                    │
│                                                                  │
│  2. LOKAL PROSESSERING                                          │
│     └── Dra master over SRAGI-STD-FACTORY-v3.4.bat              │
│         ├── bilde-hero.avif     (1920px)                        │
│         ├── bilde-content.avif  (1200px)                        │
│         ├── bilde-content.jpg   (UNIVERSAL FALLBACK)            │
│         ├── bilde-token.avif    (600px)                         │
│         ├── bilde-tiny.avif     (300px)                         │
│         └── bilde-og.jpg        (1200x630 OG)                   │
│                                                                  │
│  3. METADATA                                                     │
│     └── Opprett bilde.yaml (bruk TEMPLATE-VISUAL-v1.1.yaml)     │
│     └── Last opp til GitHub: /content/visuals/bilde.yaml        │
│                                                                  │
│  4. DISTRIBUSJON                                                 │
│     └── FTP alle 6 filer til /wp-content/uploads/visuals/inbox/ │
│                                                                  │
│  5. WORDPRESS                                                    │
│     └── Admin → Media → 🏭 Visual Factory → Kjør Sortering      │
│         ├── hero.avif    → /visuals/hero/                       │
│         ├── content.*    → /visuals/content/                    │
│         ├── token/tiny   → /visuals/tokens/                     │
│         └── og.jpg       → /visuals/social/                     │
│                                                                  │
│  6. BRUK I INNHOLD                                               │
│     └── [sragi_picture name="bilde" size="hero" alt="..."]      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🖼️ Output Struktur (LEAN v3.4)

| Fil | Størrelse | Format | Mappe | Rolle |
|-----|-----------|--------|-------|-------|
| `*-hero.avif` | 1920px | AVIF | /visuals/hero/ | Fullbredde banner |
| `*-content.avif` | 1200px | AVIF | /visuals/content/ | Artikkelbilder |
| `*-content.jpg` | 1200px | JPG | /visuals/content/ | **UNIVERSAL FALLBACK** |
| `*-token.avif` | 600px | AVIF | /visuals/tokens/ | Kort/preview |
| `*-tiny.avif` | 300px | AVIF | /visuals/tokens/ | Thumbnails |
| `*-og.jpg` | 1200x630 | JPG | /visuals/social/ | Open Graph |

### Hvorfor LEAN?

- **Før:** 7+ filer per bilde (hero.jpg, content.jpg, social.jpg...)
- **Nå:** 6 filer (én JPG = fallback for ALT)
- **Besparelse:** ~30% færre filer, samme funksjonalitet

---

## 🔧 Installasjon

### 1. Lokal maskin (Windows)

1. Installer [ImageMagick](https://imagemagick.org/script/download.php#windows)
2. Kopier `SRAGI-STD-FACTORY-v3.4.bat` til ønsket mappe
3. Test: Dra et PNG-bilde over bat-filen

### 2. WordPress

1. Åpne **WPCodeBox** (eller legg til i functions.php)
2. Opprett ny snippet: "SRAGI Visual Factory Controller"
3. Lim inn innholdet fra `sragi-visual-factory-controller-v5.3.php`
4. Aktiver snippet
5. Verifiser: Admin → Media → 🏭 Visual Factory

### 3. GitHub

1. Opprett mappe: `/content/visuals/` i ditt repo
2. Last opp YAML-filer hit (én per bilde)

---

## 📋 Shortcode Referanse

### Basis

```
[sragi_picture name="bilde-navn" size="content" alt="Beskrivelse"]
```

### Alle parametere

| Parameter | Standard | Beskrivelse |
|-----------|----------|-------------|
| `name` | (påkrevd) | Filnavn uten suffix/extension |
| `size` | `content` | `hero` \| `content` \| `token` \| `tiny` |
| `alt` | `""` | Alt-tekst for tilgjengelighet |
| `class` | `""` | CSS-klasser |
| `lazy` | `true` | `false` for above-the-fold bilder |
| `width` | `""` | Eksplisitt bredde |
| `height` | `""` | Eksplisitt høyde |

### Eksempler

```html
<!-- Hero-bilde (ingen lazy loading) -->
[sragi_picture name="frontpage-hero" size="hero" alt="SRAGI landingsside" lazy="false"]

<!-- Artikkel-bilde -->
[sragi_picture name="regenerativ-spiral" size="content" alt="Regenerativ spiral-nettverk"]

<!-- Kort/preview -->
[sragi_picture name="sragi-logo" size="token" alt="SRAGI logo" class="card-image"]
```

### Output HTML

```html
<picture>
  <source srcset="https://media.sragi.org/visuals/hero/frontpage-hero-hero.avif" type="image/avif" sizes="100vw">
  <img src="https://media.sragi.org/visuals/content/frontpage-hero-content.jpg" alt="SRAGI landingsside" fetchpriority="high" decoding="async" sizes="100vw">
</picture>
```

---

## 📐 Ratioer (Visual Protocol)

| Navn | Ratio | Canva Size | Bruk |
|------|-------|------------|------|
| **Primary** | 3:2 | 3000×2000 | Artikler, kort |
| **Widescreen** | 16:9 | 3840×2160 | Hero, YouTube |
| **Token** | 1:1 | 3000×3000 | Symboler, kvadrat |
| **Social** | 4:5 | 2400×3000 | Instagram/LinkedIn |
| **Story** | 9:16 | 1440×2560 | Stories, Reels |
| **OG** | 1.91:1 | 1200×630 | Open Graph (auto) |

---

## 🔗 Integrasjoner

### Bunny CDN

Systemet bruker `SRAGI_CDN_URL` fra wp-config.php:

```php
define('SRAGI_CDN_URL', 'https://media.sragi.org/wp-content/uploads');
```

### The SEO Framework (TSF)

OG-bilder settes automatisk hvis `-og.jpg` finnes for featured image.

### HappyFiles

Filer kategoriseres automatisk:
- Hero → "Hero" kategori
- Content → "Content" kategori
- Tokens → "Tokens" kategori
- Social/OG → "Social" kategori

### Visual Sync Engine

Henter YAML-metadata fra GitHub og populerer:
- Tittel
- Caption
- Beskrivelse
- Alt-tekst
- SEO-metadata

---

## ⚠️ Viktige merknader

### Original-filer

**`*-original.png` lastes IKKE opp til WordPress!**

- Behold lokalt og/eller på GitHub
- Kun for arkiv og gjenbruk
- Sett `deployment.upload_master: true` i YAML for unntak

### Header-IDer (NDS v2.3.1)

Shrinking header-koden har hardkodede Bricks-IDer:
```css
#brxe-ahnjzc, #brxe-kitpyb, #brxe-aczgho...
```

**HUSK:** Oppdater disse til dine faktiske element-IDer i Bricks!

---

## 🧪 Feilsøking

| Problem | Løsning |
|---------|---------|
| Bilder vises ikke | Sjekk at Bunny CDN er konfigurert |
| YAML synker ikke | Verifiser GitHub-sti og filnavn |
| Feil mappe | Sjekk suffix (-hero, -content, etc.) |
| HappyFiles kategoriserer ikke | Opprett kategorier manuelt først |

---

## 📜 Changelog

### v1.0 (2026-01-09)
- Initial release
- Claude + Gemini unified
- LEAN protocol (6 filer)
- Universal JPG fallback
- OG-støtte
- Picture shortcode

---

## 🌿 Credits

- **Rune Solberg** - Arkitekt, Neptunia Media AS
- **Claude (Anthropic)** - LEAN strategi, shortcode
- **Gemini (Google)** - Factory UI, OG-håndtering

---

**© 2025-2026 Neptunia Media AS**  
**Licensed under CC BY-SA 4.0 via SRAGI Regenerative License (SRL)**

🌿 *Klarhet. Regenerasjon. Rytme. Resonans.*
