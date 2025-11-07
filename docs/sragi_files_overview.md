# 🗂️ Oversikt over filstruktur for sragi.org

**Fil:** `/docs/sragi_files_overview.md`
**Versjon:** 1.2 (Hybrid-Kairos Sync)
**Oppdatert:** November 2025

Denne oversikten beskriver den offisielle filstrukturen for **sragi.org** som sikrer at lisens, etikk, robotinstrukser og AI-policyer er tydelige både for mennesker og maskiner.

Vi bruker en **hybrid-struktur**:
1.  **Roten (`/`)** inneholder kun essensielle "trafikkdirigenter".
2.  **`/content/license/`** inneholder alle selve lisensartefaktene.

---

## 🚦 Rot-filer (Trafikkdirigenter)

Disse filene må ligge fysisk i roten av webserveren for å følge internett-standarder.

| Filnavn | Formål | Hvorfor i roten? |
| :--- | :--- | :--- |
| **`robots.txt`** | Hovedinstruks for alle crawlere (søkemotorer og AI). Peker videre til lisensfiler og sitemap. | Standarden krever at den ligger på `/robots.txt`. |
| **`sitemap.xml`** | Komplett kart over nettstedet, inkludert dype lenker til lisensfiler. | Bør ligge i roten for automatisk oppdagelse av crawlere. |
| **`ai-policy.txt`** | Menneske- og maskinlesbar oppsummering av AI-rettigheter. | Et sterkt signal om åpenhet. Enkel å finne for alle på `/ai-policy.txt`. |

---

## 🏛️ Systeminnhold (`/content/license/`)

Disse filene er generert fra SSOT og utgjør selve det juridiske og tekniske rammeverket.

| Filnavn | Formål |
| :--- | :--- |
| **`LICENSE-RSL.xml`** | Maskinlesbar hovedlisens (RSL-format). Definerer tillatelser, krav og rettighetshaver. |
| **`REGENERATIVE_LICENSE.md`** | Menneskevennlig hovedlisens. Detaljert dokumentasjon av vilkår og etikk. |
| **`ai-policy.xml`** | Maskinlesbar versjon av AI-policyen for systemer som foretrekker XML fremfor TXT. |
| **`license.json`** | Komplett API-respons. Inneholder all metadata fra SSOT i JSON-format for integrasjoner. |
| **`index.html`** | Visuell, web-vennlig presentasjon av lisensen (landingsside for `/content/license/`). |

---

## 🧠 Kilde (Single Source of Truth)

| Filnavn | Plassering (Repo) | Formål |
| :--- | :--- | :--- |
| **`SRL-LICENSE.yaml`** | Rot | Den absolutte kilden. Definerer all metadata, versjonshistorikk og regler som genererer alle filene ovenfor. |

---

## 🔗 Koblinger og avhengigheter

Systemet er bundet sammen av referanser i `robots.txt` og `sitemap.xml`.

### Eksempel fra `robots.txt` (v1.12 standard):
```txt
# Peker til undermappen for selve artefaktene:
License: [https://sragi.org/content/license/LICENSE-RSL.xml](https://sragi.org/content/license/LICENSE-RSL.xml)
AI-Policy: [https://sragi.org/content/license/ai-policy.xml](https://sragi.org/content/license/ai-policy.xml)

# Peker til roten for sitemap:
Sitemap: [https://sragi.org/sitemap.xml](https://sragi.org/sitemap.xml)
