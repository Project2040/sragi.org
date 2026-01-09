# 🌀 SRAGI Visual Protocol v1.1 (SSOT)

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

## 📐 Del 1: De 6 Hellige Ratioer (Master Input) + Sosiale media OpenGraph

Dette er de **eneste** formatene vi bruker. Tabellen viser nøyaktig hva du skal taste inn som **Custom Size** i Canva for å skape Master-filen.

| Navn | Ratio | **Canva Design Size (px)** | Bruksområde |
| :--- | :--- | :--- | :--- |
| **Primary** | 3:2 | **3000 x 2000** | Standard for artikler, kort og presentasjoner. |
| **Widescreen** | 16:9 | **3840 x 2160** | Hero-seksjoner, YouTube, filmatiske scener. |
| **Token** | 1:1 | **3000 x 3000** | Latent Space Tokens, symboler, kvadratisk grid. |
| **Social** | 4:5 | **2400 x 3000** | Instagram/LinkedIn feed (maksimal flate). |
| **Story** | 9:16 | **1440 x 2560** | Mobil-først (Stories, Reels, TikTok). |
| **Classic** | 4:3 | **2400 x 1800** | Diagrammer og teknisk dokumentasjon. |

## 🖥️ Social Media OpenGraph

| Navn | Ratio | **Canva Design Size (px)** | Bruksområde |
| :--- | :--- | :--- | :--- |
| **Social-OG** | 120:63 | **1200 x 630** | Sosiale media OpenGraph. Kun .jpg |

## 🎨 Decorative Strips (Optional)

Disse formatene er kun for dekorasjonselementer – seksjons delere, border, ,mønster, marger. Brukes med fornuft.

| Navn | Ratio | **Canva Design Size (px)** | Bruksområde |
| :--- | :--- | :--- | :--- |
| **H-Strip** | 4:1 | **4000 x 1000** | Liggende bannere, seksjons-skillere (Wide). |
| **H-Thin** | 20:1 | **4000 x 200** | Tynne skillelinjer, mønster-striper. |
| **V-Strip** | 1:4 | **1000 x 4000** | Stående søyler, sidebjelker (Tall). |
| **V-Thin** | 1:20 | **200 x 4000** | Vertikale margin-mønstre. |

---

## 💃 Del 2: The SRAGI Workflow (Dansen)

Dette er den slaviske prosessen fra idé til publisering.

### FASE 1: SKAPELSE & MASTER (Atelieret)

1.  **Idé & Prompt:** Generer bildet (AI/Foto).
  
      Tips: For å treffe ratioen perfekt ved AI-generering, bruk disse parameterne:

         - Midjourney: --ar 3:2 (bytt ut med ønsket ratio).

         - DALL-E/Gemini: "Aspect ratio 3:2". (bytt ut med ønsket ratio).

2.  **Metadata (Start):** Opprett `.yaml`-filen lokalt. Se egen mal: TEMPLATE_VISUAL_TOKEN_v1.0.yaml

   
3.  **Prosessering (Affinity/Canva):**
    * *Affinity:* For avansert redigering/utklipp.
    * *Canva:* Opprett design med **Canva Design Size** (se tabell over). Plasser bildet.

4.  **Eksport:** Last ned fra Canva som **PNG** (Maks kvalitet).
   
5.  **Navngivning:** Gi Master-filen navn etter standarden:
    * `[tool]-[navn]-[år]-[ratio].png`
    * *Eks:* `gemini-nebula-strip-2025-4x1.png`

6.  **Navngivning:** Gi Master-filen navn etter standarden:

7.  **Social Media OpenGraph versjon:** 
     * *Canva:* Opprett design med **Canva Design Size** SocialmediaOG-1200x630.
     * Plasser bildet.
     * Gi filen navn etter standarden
     * Last ned .jpg

### **FASE 2: FABRIKKEN (Automatisering)**

5. **Input: Dra Master-filen over SRAGI-STD-FACTORY.bat.**

**Scriptet genererer automatisk hele familien (LEAN Protocol):**

| Suffiks | Maks Bredde | Formater | Mappe (WordPress) | Bruk |
| :---- | :---- | :---- | :---- | :---- |
| **\-hero** | **1920 px** | **AVIF** | **/visuals/hero/** | **Bakgrunner, Hero.** |
| **\-content** | **1200 px** | **AVIF** | **/visuals/content/** | **Featured Image, innhold.** |
| **\-content** | **1200 px** | **JPG** | **/visuals/content/** | **Universal Fallback (Img src).** |
| **\-token** | **600 px** | **AVIF** | **/visuals/tokens/** | **Grid, ikoner, kort.** |
| **\-tiny** | **300 px** | **AVIF** | **/visuals/tokens/** | **Thumbnails/LCP.** |
| **\-og** | **1200 px** | **JPG** | **/visuals/social/** | **Open Graph (SoMe).** |

### **FASE 3: DISTRIBUSJON (Logistikken)**

6. **GitHub (Hvelvet):**  
   * **Last opp .yaml filen til /content/visuals/.**  
   * **Last opp Master PNG til /assets/originals/ (valgfritt/arkiv).**  
7. **WordPress (Scenen):**  
   * **Last opp de 6 genererte filene (AVIF/JPG) via FTP til /wp-content/uploads/visuals/inbox/.**  
   * **Gå til WP Admin \> Media \> 🏭 Visual Factory.**  
   * **Klikk "Kjør Dual-Core Import".**  
8. ***Systemet flytter filene automatisk til riktig HappyFiles-mappe og synkroniserer metadata (Norsk \+ Engelsk).***

### **FASE 4: STYLING (Bricks Builder)**

8. **Bruk: Sett inn shortcoden:**  
   **\[sragi\_picture name="filnavn-uten-suffix" size="content"\]**

---

## **💾 Del 3: Metadata (YAML SSOT)**

**Sjekk alltid .yaml\-filen mot TEMPLATE-VISUAL-v1.2.yaml for å sikre at SEO og Alt-tekster er korrekt utfylt for både Norsk og Engelsk.**

**© 2026 Rune Solberg / Neptunia Media AS Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL).**

