# 🔍 SRAGI HEADLESS SEO PROTOCOL

**Version:** 1.0  
**Status:** ACTIVE  
**Scope:** Editorial Standards & Technical Architecture  
**Tooling:** Neptunia Mission Control → Loom → The SEO Framework (WordPress)

---

## 1. FILOSOFI: REGENERATIV SYNLIGHET

Vi driver ikke med "Clickbait". Vi driver med **Signalforsterkning**.
Målet med SEO i SRAGI-økosystemet er å koble rett menneske til rett innsikt med minst mulig friksjon.

* **Extractive SEO:** Lurer brukeren inn for å vise annonser.
* **Regenerative SEO:** Gir et presist løfte i søkeresultatet, og overleverer på det løftet i innholdet.

---

## 2. REDAKSJONELL STANDARD (Field Guide)

Disse reglene er kodet inn i Mission Control sin valideringslogikk.

### 🏷️ Tekstlige Metadata

| Felt | Lengde (Tegn) | Hensikt | Format Regler |
| :--- | :--- | :--- | :--- |
| **SEO Title** | **45 - 60** | Det brukeren klikker på i Google. | `Nøkkelord først: Fengende undertittel` <br> *Unngå å skrive "| SRAGI" til slutt (skjer automatisk).* |
| **Meta Desc** | **140 - 160** | Salgspitchen under lenken. | Inkluder hovednøkkelordet. Avslutt med en verdi ("Lær hvordan..."). |
| **Slug** | **Kort** | URL-adressen. | `kun-smaa-bokstaver-og-bindestrek` <br> *Alltid på engelsk, selv for norsk innhold.* |
| **Alt Text** | **Beskrivende** | For blinde og Google Images. | Beskriv motivet + kontekst. Ikke spam nøkkelord. |

### 🖼️ Visuelle Metadata (Open Graph)

Dette er bildene som vises når lenken deles på sosiale medier (LinkedIn, Slack, Facebook).

* **Dimensjoner:** `1200 x 630 px`
* **Ratio:** `1.91:1`
* **Format:** `.jpg` (foto) eller `.png` (grafikk/tekst). Max 300KB.
* **Safe Zone:** Hold viktig tekst/logo sentrert. Kantene kan kuttes på mobil.

---

## 3. TEKNISK IMPLEMENTERING (WordPress Bridge)

Vi bruker **The SEO Framework (TSF)** som motor, men vi styrer den "utenfra" (Headless) via Python-scriptet vårt (`loom.py`).

### 🔧 Server-Side Code (`functions.php`)

For at WordPress skal godta SEO-data fra romstasjonen, må denne koden ligge i temaets `functions.php`:

```php
/**
 * 🌀 SRAGI HEADLESS SEO BRIDGE v1.1
 * Expose The SEO Framework meta keys to REST API.
 */
add_action('rest_api_init', function () {
    $tsf_keys = [
        '_genesis_title',          // Browser Title (Google)
        '_genesis_description',    // Meta Description (Google)
        '_genesis_canonical_uri',  // Canonical URL (Authority)
        '_genesis_noindex',        // Skjul fra søk
        '_social_image_url',       // Custom OG Image
        '_open_graph_title',       // LinkedIn/FB Title override
        '_open_graph_description'  // LinkedIn/FB Desc override
    ];

    foreach ($tsf_keys as $key) {
        register_meta('post', $key, [
            'type'              => 'string',
            'description'       => 'SRAGI Controlled SEO Field',
            'single'            => true,
            'show_in_rest'      => true, 
            'auth_callback'     => function() { return current_user_can('edit_posts'); },
            'sanitize_callback' => 'sanitize_text_field'
        ]);
    }
});
