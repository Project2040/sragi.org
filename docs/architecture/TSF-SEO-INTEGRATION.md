# 🛠️ TSF (The SEO Framework) HEADLESS INTEGRATION

**File:** `/docs/architecture/TSF-SEO-INTEGRATION.md`  
**Status:** PRODUCTION STANDARD  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**Version:** 1.1 (Headless Bridge Definition)  
**Scope:** Technical Architecture (Headless Bridge)

---

## 1. 🧭 Purpose

This document defines the technical architecture required to integrate **The SEO Framework (TSF)** plugin with the **SRAGI Loom Engine** via the WordPress REST API.

Within the Neptunia ecosystem, WordPress + TSF is:

- a **passive database** and **renderer** for SEO metadata  
- **not** the source of truth  

All canonical SEO data lives in:

- frontmatter in Markdown files (Git, e.g. `meta`, `seo`, `visual` blocks) :contentReference[oaicite:0]{index=0}  
- SSOT YAML under `/_CONFIG` (e.g. `VALIDATION_RULES.yaml`) :contentReference[oaicite:1]{index=1}  

**Neptunia Mission Control + Loom** are therefore the SSOT layer.  
**TSF** simply reads and renders what they write.

For editorial rules, see `/docs/standards/SEO-PROTOCOL.md`.  
For machine rules (lengths, patterns), see `/_CONFIG/VALIDATION_RULES.yaml`.

---

## 2. 🔗 The Headless Bridge (PHP)

To allow the Python Publisher Module (Loom) to write SEO metadata to WordPress, TSF’s internal meta keys must be explicitly exposed to the REST API.

Denne koden **MÅ** ligge i aktivt tema (`functions.php`) eller i en sentral snippet-løsning (f.eks. WPCodeBox):

```php
/**
 * 🌀 SRAGI HEADLESS SEO BRIDGE v1.2
 * Expose The SEO Framework meta keys to REST API for Loom Engine access.
 *
 * TSF acts as a passive SEO database and renderer.
 * Loom + frontmatter are the Single Source of Truth.
 */
add_action('rest_api_init', function () {
    // Key → type (for sanitize strategy)
    $tsf_meta = [
        '_genesis_title'           => 'text', // Browser Title (Google)
        '_genesis_description'     => 'text', // Meta Description
        '_genesis_canonical_uri'   => 'url',  // Canonical URL (Authority)
        '_genesis_noindex'         => 'text', // "1"/"0" or empty (robots)
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
**Merk:**

* `show_in_rest: true` gjør at feltet dukker opp under `meta` i `/wp-json/wp/v2/posts/{id}`.

* `auth_callback` sikrer at kun brukere med `edit_posts` (inkl. Loom‑bot) kan lese/skriv.

* URL‑felt bruker `esc_url_raw`, tekstfelt bruker `sanitize_text_field`.

---

## **3\. 💾 Loom Engine Mapping (Frontmatter → TSF)**

Loom Publisher‑modulen leser frontmatter fra innholdsfilene (`.md`) og mapper verdiene til TSF‑feltene via REST API. Frontmatter utvides med en `seo`‑seksjon og en `visual`‑seksjon, i tillegg til eksisterende `meta`/`ia`/`sync` .

### **3.1 Canonical frontmatter schema (SEO‑relatert)**

`meta:`  
  `type: "documentation"`  
  `title_nb: "Systemtenkning i praksis"`  
  `title_en: "Systems Thinking in Practice"`  
  `slug: "systems-thinking-in-practice"`  
  `status: "draft"`

`seo:`  
  `title: "Systems Thinking in Practice – A Regenerative Approach"`  
  `description: "Learn how to apply systems thinking in real projects using the SRAGI OS and Neptunia ecosystem."`  
  `canonical_url: "https://sragi.org/docs/systems-thinking-in-practice"`  
  `noindex: false`

`visual:`  
  `og_image: "assets/social/systems-thinking-hero-1200x630.jpg"`

### **3.2 Mapping-tabell (Loom → TSF)**

| Frontmatter key | TSF meta key | Purpose |
| ----- | ----- | ----- |
| `seo.title` | `_genesis_title` | Primary Google/Browser Title |
| `seo.description` | `_genesis_description` | Primary Meta Description |
| `seo.canonical_url` | `_genesis_canonical_uri` | Canonical authority URL |
| `seo.noindex` | `_genesis_noindex` | Robots signal (index/noindex) |
| `visual.og_image` | `_social_image_url` | SoMe / Open Graph image URL |
| *(later: optional)* | `_open_graph_title` | SoMe title override |
| *(later: optional)* | `_open_graph_description` | SoMe description override |

### **3.3 Bool → string-konvertering for noindex**

TSF forventer ikke en ekte bool, men en “truthy” verdi (typisk `"1"`) for å aktivere noindex.

**Kontrakt:**

* `seo.noindex: true` → `_genesis_noindex = "1"`

* `seo.noindex: false` → `_genesis_noindex = ""` (tom streng) eller `"0"`

Denne konverteringen implementeres i Loom Engine (Python), ikke i WordPress/PHP.

---

## **4\. 🧬 Relationship to SEO-PROTOCOL & VALIDATION\_RULES**

Dette dokumentet beskriver **den tekniske broen** (frontmatter → Loom → TSF).

Relaterte standarder:

* **Editorial & conceptual rules:**  
   `/docs/standards/SEO-PROTOCOL.md`  
   (hvordan skrive gode titler, beskrivelser, slugs, alt-tekst osv.)

* **Machine-level constraints (SSOT):**  
   `/_CONFIG/VALIDATION_RULES.yaml`  
   (lengdegrenser, regex for slugs, påkrevede felt, UU‑krav osv.)

Endringer i:

* felt‑navn (`seo.title`, `visual.og_image`, osv.)

* lengdegrenser og krav

…må alltid oppdateres både i:

1. `CONTENT-SPEC-SCHEMA.yaml` (frontmatter-schema)

2. `VALIDATION_RULES.yaml` (valideringslogikk)

3. denne mappetabellen (hvis det påvirker TSF)

---

## **5\. 📝 Compliance & Debugging**

### **5.1 Auth & permissions**

Hvis Loom feiler med auth‑/permission‑feil ved SEO‑update:

* verifiser at REST‑brukeren (f.eks. `loom-bot`) har `edit_posts`

* sjekk at `auth_callback` i PHP‑broen returnerer `true` for denne brukeren

* verifiser at API‑kallet faktisk sender korrekt auth‑header (Bearer / app-pass)

### **5.2 Felt-eksponering**

Sjekk at TSF‑feltene faktisk er synlige i REST:

1. Opprett/oppdater et innlegg i WP.

Kjør:

 `GET /wp-json/wp/v2/posts/{id}`

2. Se etter:

 `"meta": {`  
  `"_genesis_title": "…",`  
  `"_genesis_description": "…",`  
  `"_genesis_canonical_uri": "…",`  
  `"_social_image_url": "…"`  
`}`

3. Hvis de ikke finnes:

* sjekk at koden i `functions.php` er aktiv

* clear cache (object cache / REST cache).

### **5.3 TSF-innstillinger**

TSF trenger normalt ikke spesialkonfig for å lese sine egne meta‑nøkler, men:

* sørg for at standard SEO‑felt ikke overstyres av andre plugins

* verifiser at TSF er aktivt på aktuell post‑type (pages/posts/custom)

---

© 2025 Rune Solberg / Neptunia Media AS

Licensed under CC BY 4.0 via the SRAGI Regenerative License (SRL).  
 See `SRL-LICENSE.yaml` for full details.

