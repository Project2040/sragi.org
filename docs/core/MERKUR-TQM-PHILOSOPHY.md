# 💎 Merkur Consulting: Regenerativ TQM-Filosofi

**Fil:** `/docs/philosophy/MERKUR-TQM-PHILOSOPHY.md`  
**Status:** CORE DOCTRINE  
**Versjon:** 1.1  
**Ansvarlig:** Rune Solberg  
**Inspirasjon:** W. Edwards Deming, Joseph Juran, Naturens egne systemer  

---

## 1. Definisjon av Kvalitet

I Merkur Consulting definerer vi ikke kvalitet som bare "fravær av feil".  
For oss er kvalitet: **Fitness for Future.**

Det er evnen til å levere innsikt, systemer og innhold som ikke bare løser dagens problem, men som styrker mottakerens evne til å møte morgendagen.

> **"Kvalitet er når kunden kommer tilbake, men produktet ikke gjør det (fordi det virker)."**

---

## 2. De 5 Pilarene i Vårt Kvalitetssystem

### I. Mennesket i Loopen (Human-in-the-Loop)
Vi tror ikke på blind automasjon, men på symbiose.
* **Prinsipp:** AI utvider perspektivet, mennesket velger retningen.
* **Praksis:** Vi bruker AI som en aktiv dialogpartner i designfasen (Kairos) og som en streng kontrollør i leveransefasen (Loom). Mennesket har alltid siste ord (vetorett).

### II. Systemisk Integritet (Single Source of Truth)
Kvalitet oppstår når alle deler av organisasjonen navigerer etter samme kart.
* **Prinsipp:** Aldri dupliser informasjon; referer til kilden.
* **Praksis:** Vi bruker YAML-baserte SSOT-filer (`TAXONOMY_GRAPH`, `SRL-LICENSE`) for å sikre at sannheten flyter friksjonsfritt fra strategi til kode.

### III. Kaizen (Kontinuerlig Forbedring)
Et system som står stille, dør. Vi forventer ikke perfeksjon i første iterasjon, men vi krever evolusjon.
* **Prinsipp:** "Fail fast, learn faster, fix forever."
* **Praksis:** Hver gang en feil oppdages i produksjon, oppdaterer vi ikke bare innholdet, men også *Regelboken* (`VALIDATION_RULES.yaml`) slik at systemet lærer av feilen.

### IV. Faktabasert Beslutningstaking
Vi stoler på intuisjon for retning, men bruker data for korreksjon.
* **Prinsipp:** Mål det som betyr noe, ikke bare det som er lett å telle.
* **Praksis:** Vi bruker Mission Control for å visualisere status på innholdsproduksjonen i sanntid.

### V. Regenerativ Leveranse
Vi etterlater systemene renere enn vi fant dem.
* **Prinsipp:** R > 1. Verdien vi skaper skal være større enn ressursene vi forbruker.
* **Praksis:** Vi optimaliserer bilder for lavt energiforbruk (Green Web), bruker åpne standarder, og deler kunnskap under eksplisitte artefaktlisenser innen SRLF-rammeverket.

---

## 3. Kvalitetssikring i Praksis (The Merkur Flow)

Vår produksjonslinje er designet etter TQM-prinsippet om at **kvalitet må bygges inn, ikke inspiseres inn**.

1.  **Design (Plan):** Vi definerer strukturen i `content-template.yaml` før vi skriver et ord.
2.  **Produksjon (Do):** Vi bruker *Neptunia Mission Control* og AI-partnere til å generere og raffinere innholdet, mens mennesket sikrer intensjon og tone.
3.  **Verifikasjon (Check):** *Loom Validator* sjekker automatisk mot SSOT (Regelboken).
4.  **Publisering (Act):** Innholdet går live kun når det oppfyller "Definition of Done".

---

## 4. Definition of Done (DoD)

For at et leveranseobjekt skal godkjennes i Merkur-økosystemet, må det passere følgende sjekkliste (håndhevet av `VALIDATION_RULES.yaml`):

**✅ Struktur & Integritet**
* Alle påkrevde felt i YAML er utfylt.
* Taksonomi-begreper (Pillar, Domain) matcher SSOT.

**✅ Kvalitet & SEO**
* Tittel er optimalisert (45-60 tegn).
* Tilgjengelighet er ivaretatt (Alt-tekst på bilder).
* Markdown-struktur er logisk (ingen hopp i overskriftsnivåer).

**✅ Regenerativ Standard**
* Bilder er optimalisert (WebP/AVIF, <300KB).
* Kildekode følger åpne standarder.
* Ingen "dead links" eller foreldet informasjon.

---

## 5. Avvikshåndtering

Når kvaliteten svikter (for det vil den), følger vi denne protokollen:

1.  **Identifiser:** Hva gikk galt? (Root Cause Analysis).
2.  **Isoler:** Stopp "blødningen" (Rollback via Git).
3.  **Korriger:** Fiks feilen.
4.  **Forebygg:** Oppdater systemet (Loom/Regler) slik at systemet selv fanger dette neste gang.

---

## 6. Vårt Løfte

Til våre kunder og partnere:
Vi leverer ikke "godt nok". Vi leverer systemer som er robuste, transparente og bygget for å vare.

> **"Kvalitet er ikke en handling, det er en vane."**
> — Aristoteles (Merkur-parafrase)

---

## 7. Frontmatter

title_nb: "Merkur Consulting: Regenerativ TQM-filosofi"

title_en: "Merkur Consulting: Regenerative TQM Philosophy"

type: "system_doc"

slug: "merkur-tqm-philosophy"

status: "published"

pillar: "system_thinking"

domain: "economy"

phase: "maturity"

mode: "elantrix"

seo_title: "Merkur Consulting – Regenerativ TQM-filosofi"

seo_desc: "Hvordan Merkur Consulting definerer kvalitet som 'Fitness for Future' og bygger regenerativ kvalitet inn i systemet gjennom SSOT, Human-in-the-Loop og kontinuerlig forbedring."

hero_image: null

ai_contributors: 
  - "Gemini (Drafting & Synthesis)"
  - "Claude (Architecture & Validation)"
  - "ChatGPT (Validation)"

human_lead: "Rune Solberg"

qa_status: "approved"

version: "1.1"
---

**© 2025 Merkur Consulting** a part of **Neptunia Media AS** contact: **rune@merkur-consulting.com**
