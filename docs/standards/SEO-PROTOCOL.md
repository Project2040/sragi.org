# 🔍 SRAGI HEADLESS SEO PROTOCOL

**File:** `/docs/standards/SEO-PROTOCOL.md`  
**Version:** 1.3 (SSOT-aligned)  
**Status:** PRODUCTION STANDARD  
**Scope:** Editorial Standards & Technical Architecture  
**Tooling:** Neptunia Mission Control → Loom → The SEO Framework (WordPress)

---

## 1. FILOSOFI: REGENERATIV SYNLIGHET

Vi driver ikke med "Clickbait". Vi driver med **Signalforsterkning**.  
Målet med SEO i SRAGI-økosystemet er å koble rett menneske til rett innsikt med minst mulig friksjon. :contentReference[oaicite:2]{index=2}  

- **Extractive SEO:** Lurer brukeren inn for å vise annonser.  
- **Regenerative SEO:** Gir et presist løfte i søkeresultatet, og leverer på det løftet i innholdet.

---

## 2. REDAKSJONELL STANDARD (Field Guide)

Tall og grenser her er SSOT-definert i `/_CONFIG/VALIDATION_RULES.yaml`.  
Denne fila er **menneskeversjonen** av de reglene.

### 🏷️ Tekstlige Metadata

| Felt          | Lengde (Tegn) | Hensikt                        | Format-regler                                                                 |
| :------------| :------------ | :----------------------------- | :-----------------------------------------------------------------------------|
| **SEO Title**| **45–60**     | Det brukeren klikker på i Google. | *Unngå å skrive "\| SRAGI" til slutt (settes automatisk i temaet).*           |
| **Meta Desc**| **140–160**   | Salgspitchen under lenken.     | Inkluder hovednøkkelordet naturlig i første setning.                          |
| **Slug**     | **Kort (≤ 60)** | URL-adressen.                 | Kun små bokstaver (a–z), tall (0–9) og bindestrek `-`. <br> *Alltid engelsk/latin (ingen æøå), selv for norsk innhold.* |
| **Alt Text** | **Beskrivende** | For blinde og Google Images. | Beskriv motiv + kontekst. Max **125 tegn**. Unngå ord som "bilde av".        |

### 🖼️ Visuelle Metadata (Open Graph)

- **Dimensjoner:** `1200 x 630 px`  
- **Ratio:** `1.91:1` (definert i `VISUAL-PROTOCOL.md`)  
- **Format:** `.jpg` (SoMe), `.png` (grafikk/tekst).  
- **Filstørrelse:** så liten som mulig, helst \< 300 KB (Green Web-prinsipp).

### 🔗 Canonical URL

- Brukes **kun** når innhold er syndikert eller duplisert for å peke til original kilde.  
- Må være full HTTPS‑URL (f.eks. `https://sragi.org/docs/system-thinking`).

---

## 2.1 Anbefalt frontmatter for SEO (Loom-kompatibel)

I tillegg til eksisterende `meta`/`ia`/`sync`-seksjoner i frontmatter :contentReference[oaicite:3]{index=3} utvides filene med egne blokker for SEO og visuelle metadata:

```yaml
meta:
  type: "documentation"
  title_nb: "Systemtenkning i praksis"
  title_en: "Systems Thinking in Practice"
  slug: "systems-thinking-in-practice"
  status: "draft"

seo:
  title: "Systems Thinking in Practice – A Regenerative Approach"
  description: "Learn how to apply systems thinking in real projects using the SRAGI OS and Neptunia ecosystem."
  canonical_url: "https://sragi.org/docs/systems-thinking-in-practice"
  noindex: false

visual:
  og_image: "assets/social/systems-thinking-hero-1200x630.jpg"
```
Prinsipp:

meta.* = generelle felt (tittel/slug/status)

seo.* = søk‑spesifikke felt (tittel, beskrivelse, canonical, noindex)

visual.* = SoMe-/OG‑spesifikke felt (f.eks. og_image)

Loom Publisher leser disse blokkene og oppdaterer TSF‑feltene via WordPress REST API.

## 3. TEKNISK IMPLEMENTERING (WordPress Bridge)

Vi bruker The SEO Framework (TSF) som motor, men styrer den "utenfra" via Loom (loom.py).
WordPress + TSF er renderer og database, ikke “source of truth”.

For redaksjonelle regler, se denne fila.
For teknisk mapping, se også /docs/architecture/TSF-SEO-INTEGRATION.md.

🔧 Server-side code (functions.php eller WPCodeBox)

For at Loom skal kunne lese og skrive SEO-felter over REST må TSF meta keys eksponeres via register_meta:

```PHP
/**
 * 🌀 SRAGI HEADLESS SEO BRIDGE v1.2
 * Expose The SEO Framework meta keys to REST API for Loom Engine access.
 */
add_action('rest_api_init', function () {
    // Key → type (for sanitize-strategi)
    $tsf_meta = [
        '_genesis_title'           => 'text', // Browser Title (Google)
        '_genesis_description'     => 'text', // Meta Description
        '_genesis_canonical_uri'   => 'url',  // Canonical URL (Authority)
        '_genesis_noindex'         => 'text', // "1"/"0" eller tom (robots)
        '_social_image_url'        => 'url',  // Custom OG Image URL
        '_open_graph_title'        => 'text', // SoMe override title
        '_open_graph_description'  => 'text', // SoMe override description
    ];

    foreach ($tsf_meta as $key => $type) {
        register_meta('post', $key, [
            'type'              => 'string',
            'description'       => 'SRAGI Controlled SEO Field via Loom',
            'single'            => true,
            'show_in_rest'      => true,
            'auth_callback'     => function () {
                return current_user_can('edit_posts');
            },
            'sanitize_callback' => $type === 'url'
                ? 'esc_url_raw'
                : 'sanitize_text_field',
        ]);
    }
});
```

Noindex-kontrakt (Loom → TSF):

seo.noindex: true → _genesis_noindex = "1"

seo.noindex: false → _genesis_noindex = "" eller "0"

© 2025 Rune Solberg / Neptunia Media AS
Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).
