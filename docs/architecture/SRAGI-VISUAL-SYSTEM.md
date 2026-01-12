# **🏭 SRAGI Visual System v1.0**

**Status:** PRODUCTION READY

**Maintainer:** Rune Solberg / Neptunia Media AS

**Version:** 1.0 (Dual Core Edition)

**Last Updated:** January 2026

**License:** CC BY-SA 4.0 via SRAGI Regenerative License (SRL)

---

## **🎯 Formål**

Et komplett, automatisert system for bildebehandling i SRAGI-økosystemet med støtte for tospråklig innhold (Dual Core):

* **Lokal prosessering** → AVIF primary \+ JPG universal fallback (LEAN)  
* **Automatisk sortering** → HappyFiles-kategorier  
* **Metadata-synkronisering** → GitHub YAML → WordPress (NO \+ EN)  
* **Smart leveranse** → Shortcode som tilpasser seg språk automatisk  
* **CDN-leveranse** → Bunny.net med optimal caching

---

## **📦 Innhold (Kjernekomponenter)**

| Fil | Versjon | Beskrivelse | Hvor |
| :---- | :---- | :---- | :---- |
| SRAGI-STD-FACTORY.bat | **v3.4** | Windows batch for bildeprosessering | Lokal maskin |
| sragi-visual-factory-controller.php | **v5.5** | Dual Core Import & Shortcode Logic | WPCodeBox |
| TEMPLATE-VISUAL.yaml | **v1.2** | Metadata-mal (SSOT) med SEO | GitHub |
| HAPPYFILES-STRUCTURE.md | **v2.2** | Mappestruktur og sorteringsguide | Docs |

---

## **🔄 Komplett Workflow**

Plaintext

```
┌─────────────────────────────────────────────────────────────────┐
│                    SRAGI VISUAL WORKFLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. SKAPELSE (Canva/AI)                                         │
│     └── Master PNG (3000x2000 for 3:2, etc.)                    │
│     └── bilde-og.jpg (1200x630 Open Graph) Maks. 300kb          │
│                                                                 │
│  2. LOKAL PROSESSERING (The Factory)                            │
│     └── Dra master over SRAGI-STD-FACTORY.bat                   │
│        ├── bilde-hero.avif      (1920px)                        │
│        ├── bilde-content.avif   (1200px)                        │
│        ├── bilde-content.jpg    (UNIVERSAL FALLBACK)            │
│        ├── bilde-token.avif     (600px)                         │
│        ├── bilde-tiny.avif      (300px)                         │
│        └── bilde-og.jpg         (1200x630 Open Graph)           │
│                                                                 │
│  3. METADATA (SSOT)                                             │
│     └── Opprett bilde.yaml (bruk TEMPLATE-VISUAL-v1.2.yaml)     │
│     └── Fyll inn Title/Alt/Desc på Norsk + Engelsk              │
│     └── Last opp til GitHub: /content/visuals/bilde.yaml        │
│     └── Master PNG (3000x2000 for 3:2, etc.)                    │
│                                                                 │
│  4. DISTRIBUSJON                                                │
│     └── FTP alle 6 filer til /wp-content/uploads/visuals/inbox/ │
│                                                                 │
│  5. WORDPRESS (Dual Core Import)                                │
│     └── Admin → Media → 🏭 Visual Factory → Kjør Import         │
│        ├── Flytter filer til korrekte mapper                    │
│        ├── Henter NO + EN data fra GitHub                       │
│        └── Sletter filer fra Inbox                              │
│                                                                 │
│  6. BRUK I INNHOLD (Smart Shortcode)                            │
│     └── [sragi_picture name="bilde" size="hero"]                │
│        └── Viser automatisk Norsk ALT-tekst på norsk side       │
│        └── Viser automatisk Engelsk ALT-tekst på engelsk side   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## **🖼️ Output Struktur (LEAN Protocol)**

Alle filer lagres under /wp-content/uploads/content/visuals/.

| Fil-suffix | Størrelse | Format | Mappe | Rolle |
| :---- | :---- | :---- | :---- | :---- |
| \-hero.avif | 1920px | AVIF | /hero/ | Fullbredde banner |
| \-content.avif | 1200px | AVIF | /content/ | Artikkelbilder |
| \-content.jpg | 1200px | JPG | /content/ | **UNIVERSAL FALLBACK** |
| \-token.avif | 600px | AVIF | /tokens/ | Kort/preview |
| \-tiny.avif | 300px | AVIF | /tokens/ | Thumbnails/LCP |
| \-og.jpg | 1200x630 | JPG | /social/ | Open Graph (SoMe) |

### **Hvorfor LEAN?**

* **Før:** 7+ filer per bilde (hero.jpg, content.jpg, social.jpg...)  
* **Nå:** 6 filer (én JPG \= fallback for ALT)  
* **Besparelse:** \~30% færre filer, samme funksjonalitet.  
* **WP Media Settings:** Alle standardstørrelser (Thumbnail, Medium, Large) er satt til 0 for å hindre bloat.

---

## **🔧 Installasjon**

### **1\. Lokal maskin (Windows)**

1. Installer [ImageMagick](https://imagemagick.org/script/download.php#windows).  
2. Kopier SRAGI-STD-FACTORY.bat til ønsket mappe.  
3. Test: Dra et PNG-bilde over bat-filen.

### **2\. WordPress (WPCodeBox)**

1. Opprett ny snippet: "SRAGI Visual Factory Controller".  
2. Lim inn koden for **v5.5 (Dual Core)**.  
3. **VIKTIG:** Sjekk at du ikke har gamle versjoner (v4.x) aktive samtidig.  
4. Verifiser UI: Admin → Media → 🏭 Visual Factory.

### **3\. GitHub**

1. Mappestruktur: /content/visuals/.  
2. Last opp YAML-filer her (navngitt nøyaktig som bildefilen uten suffix).

---

## **📋 Shortcode Referanse**

### **Basis**

```
[sragi_picture name="bilde-navn" size="content"]
```

### **Smart Language Logic (v5.5)**

Hvis du *ikke* spesifiserer alt="..." i shortcoden:

1. Shortcoden sjekker språket på nettsiden (f.eks. nb-NO).  
2. Den henter \_sragi\_alt\_no fra databasen hvis språket er norsk.  
3. Den henter \_sragi\_alt\_en hvis språket er engelsk (eller annet).  
4. **Resultat:** Full automasjon.

### **Alle parametere**

| Parameter | Standard | Beskrivelse |
| :---- | :---- | :---- |
| name | (påkrevd) | Filnavn uten suffix/extension (ID) |
| size | content | hero |
| alt | (auto) | Overstyr automatisk tekst manuelt ved behov |
| class | "" | CSS-klasser |
| lazy | true | Sett false for hero-bilder (LCP optimalisering) |
| width | "" | Eksplisitt bredde (hvis nødvendig) |
| height | "" | Eksplisitt høyde (hvis nødvendig) |

### **Output HTML**

HTML

```
<picture>
  <source srcset="https://cdn.../visuals/hero/bilde-hero.avif" type="image/avif" sizes="100vw">
  <img src="https://cdn.../visuals/content/bilde-content.jpg" alt="Norsk tekst her" fetchpriority="high" decoding="async" sizes="100vw">
</picture>
```

---

## **📐 Ratioer (Visual Protocol)**

| Navn | Ratio | Canva Size | Bruk |
| :---- | :---- | :---- | :---- |
| **Primary** | 3:2 | 3000×2000 | Artikler, kort |
| **Widescreen** | 16:9 | 3840×2160 | Hero, YouTube |
| **Token** | 1:1 | 3000×3000 | Symboler, kvadrat |
| **Social** | 4:5 | 2400×3000 | Instagram/LinkedIn |
| **OG** | 1.91:1 | 1200×630 | Open Graph (auto) |

---

## **⚠️ Viktige merknader**

### **Bloat Control**

For å holde serveren ren:

1. Gå til WP Admin \> Settings \> Media.  
2. Sett Thumbnail, Medium og Large size til **0**.  
3. Sjekk at "Organize my uploads into month- and year-based folders" er **PÅ** (men systemet vårt bruker /content/ utenfor dette for visuals).

### **Sikkerhet**

Controller v5.5 har en function\_exists wrapper. Dette hindrer at siden krasjer ("Fatal Error") hvis scriptet lastes to ganger ved uhell.

---

## **🧪 Feilsøking**

| Problem | Løsning |
| :---- | :---- |
| "White Screen" / Krasj | Sjekk om du har duplikat snippet i WPCodeBox (v4.2 vs v5.5). |
| Bilder vises ikke | Sjekk SRAGI\_CDN\_URL i wp-config.php. |
| Feil språk på tekst | Sjekk at YAML-filen har title\_no/title\_en og at importen er kjørt på nytt. |
| Innboks tømmes ikke | Sjekk filrettigheter (755) på /uploads/visuals/inbox/. |

---

## **📜 Changelog**

### **v1.0 (2026-01-09) \- Dual Core Release**

* **Unified Controller v5.5:** Import av både NO og EN data i én operasjon.  
* **Auto-Routing:** Filene flyttes automatisk basert på suffix.  
* **Crash Proof:** Sikkerhetsmekanismer mot duplikat kjøring.  
* **Smart Shortcode:** Språkavhengig visning uten ekstra plugins.

---

## **🌿 Credits**

* **Rune Solberg** \- Systemarkitekt, Neptunia Media AS  
* **Claude (Anthropic)** \- LEAN strategi, konseptutvikling  
* **Gemini (Google)** \- Kodeimplementasjon (PHP/Batch), Debugging

---

**© 2026 Neptunia Media AS** **Licensed under CC BY-SA 4.0 via SRAGI Regenerative License (SRL)**


