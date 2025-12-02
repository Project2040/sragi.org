# 🌀 SRAGI Visual Protocol v2.0 (SSOT)

**Status:** SSOT (Single Source of Truth)
**Fil:** `/docs/visuals/visual-protocol.md`
**Vedlikeholder:** Rune Solberg / Neptunia Media AS
**Sist oppdatert:** Desember 2025
**Lisens:** CC BY-SA 4.0 via SRL v1.12

---

## 🧭 Formål

Dette dokumentet definerer den absolutte standarden for alle visuelle eiendeler i SRAGI-økosystemet. Det forener **kreativ komposisjon** (ratio) med **teknisk leveranse** (filformater og mappestruktur).

Målet er en **regenerativ visuell flyt**: Bevaring av originalkvalitet (Master) kombinert med lynrask, båndbredde-besparende levering på web (AVIF).

---

## 📐 Del 1: De 10 Hellige Ratioer (Master Input)

Dette er de **eneste** formatene vi bruker. Tabellen viser nøyaktig hva du skal taste inn som **Custom Size** i Canva for å skape Master-filen.

| Navn | Ratio | **Canva Design Size (px)** | Bruksområde |
| :--- | :--- | :--- | :--- |
| **Primary** | 3:2 | **3000 x 2000** | Standard for artikler, kort og presentasjoner. |
| **Widescreen** | 16:9 | **3840 x 2160** | Hero-seksjoner, YouTube, filmatiske scener. |
| **Token** | 1:1 | **3000 x 3000** | Latent Space Tokens, symboler, kvadratisk grid. |
| **Social** | 4:5 | **2400 x 3000** | Instagram/LinkedIn feed (maksimal flate). |
| **Story** | 9:16 | **1440 x 2560** | Mobil-først (Stories, Reels, TikTok). |
| **Classic** | 4:3 | **2400 x 1800** | Diagrammer og teknisk dokumentasjon. |
| **H-Strip** | 4:1 | **4000 x 1000** | Liggende bannere, seksjons-skillere (Wide). |
| **H-Thin** | 20:1 | **4000 x 200** | Tynne skillelinjer, mønster-striper. |
| **V-Strip** | 1:4 | **1000 x 4000** | Stående søyler, sidebjelker (Tall). |
| **V-Thin** | 1:20 | **200 x 4000** | Vertikale margin-mønstre. |

---

## 🏭 Del 2: Produksjonslinjen (The Factory)

Når Master-filen kjøres gjennom scriptet `SRAGI-IMAGE-PIPELINE-v2_1.bat`, genereres følgende sett automatisk. Scriptet skalerer kun ned hvis bildet er større enn målet (`>`), så Striper og Thin-formater forblir skarpe.

| Suffiks | Maks Bredde | Formater | HappyFiles Mappe | Bruk |
| :--- | :--- | :--- | :--- | :--- |
| **`-large`** | 1920 px | AVIF + WEBP | `/visuals/hero/` | Bakgrunner, Hero. |
| **`-medium`** | 1200 px | AVIF + WEBP | `/visuals/content/` | **Featured Image**, innhold. |
| **`-small`** | 600 px | AVIF + WEBP | `/visuals/tokens/` | Grid, ikoner, kort. |
| **`-social`** | 1080 px | JPG | `/visuals/social/` | SoMe-deling. |

---

## 💃 Del 3: The SRAGI Workflow (Dansen)

Dette er den slaviske prosessen fra idé til publisering.

### FASE 1: SKAPELSE & MASTER (Atelieret)
1.  **Idé & Prompt:** Generer bildet (AI/Foto).
2.  **Metadata (Start):** Opprett `.yaml`-filen lokalt.
3.  **Prosessering (Affinity/Canva):**
    * *Affinity:* For avansert redigering/utklipp.
    * *Canva:* Opprett design med **Canva Design Size** (se tabell). Plasser bildet.
4.  **Eksport:** Last ned fra Canva som **PNG** (Maks kvalitet).
5.  **Navngivning:** Gi Master-filen navn etter standarden:
    * `[tool]-[navn]-[år]-[ratio].png`
    * *Eks:* `gemini-nebula-strip-2025-4x1.png`

### FASE 2: FABRIKKEN (Automatisering)
6.  **Input:** Dra Master-filen over `SRAGI-IMAGE-PIPELINE-v2_1.bat`.
7.  **Output:** Scriptet genererer web-versjonene i `processed-sragi-v2`.
8.  **Samling:** Flytt *hele familien* (Master + Web-filer + YAML) til din lokale mappe: `E:\1-Neptunia-Media-Visuals\Visual-content-ready\[Filnavn-Mappe]\`.

### FASE 3: DISTRIBUSJON (Logistikken)
9.  **GitHub (Hvelvet):**
    * Last opp **Master PNG** + **YAML** til `assets/originals/`.
10. **WordPress (Scenen):**
    * Gå til HappyFiles.
    * Last opp `*-large` ➔ mappen **Hero**.
    * Last opp `*-medium` ➔ mappen **Content**.
    * Last opp `*-small` ➔ mappen **Tokens**.
    * (Aldri last opp Master PNG til WordPress).

### FASE 4: STYLING (Bricks Builder)
11. **CSS Magic:** Legg til overlays, gradients, borders og skygger i Bricks. Bildet forblir rent; stilen er kode.

---

## 💾 Del 4: Metadata (YAML SSOT)

Mal for `[filnavn].yaml`. Lagres sammen med Master i GitHub og lokalt.

```yaml
# ===========================================================
#  SRAGI VISUAL TOKEN IDENTITY CARD v2.3
#  File: gemini-nebula-strip-2025.yaml
# ===========================================================

meta:
  id: "gemini-nebula-strip-2025"
  version: 2.1
  created_at: "2025-12-02"
  author: "Rune Solberg"

variants:
  # Hardkodede filnavn for entydig kobling (Inkluderer ratio i navnet)
  master:   "gemini-nebula-strip-2025-4x1.png"
  hero:     "gemini-nebula-strip-2025-4x1-large.avif"
  content:  "gemini-nebula-strip-2025-4x1-medium.avif"
  token:    "gemini-nebula-strip-2025-4x1-small.avif"
  social:   "gemini-nebula-strip-2025-
