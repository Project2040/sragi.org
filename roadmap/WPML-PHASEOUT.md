# 🚧 WPML-UTFASING (Fjerning av Legacy-Bro)

**Filplassering (SSOT):** `docs/roadmap/WPML-UTFASING.md`
**Status:** Høy Risiko, Aktiv Legacy Avhengighet.
**Mål:** Oppnå 100% SSOT-samsvar ved å fjerne WPML fullstendig i Q1 2026.
**SSOT-Konflikt:** WPMLs eksistens motsier **YAML-som-SSOT**-prinsippet for flerspråklige data, og fører til Vendor Lock-in og database-bloat.

---

## 1. 🔍 Nåværende Funksjonsområder Styrt av WPML

WPML kontrollerer for øyeblikket følgende kritiske områder som må erstattes:

1.  **Post ID-Knytting:** Vedlikeholder koblingen mellom norske (`-nb`) og engelske (base) innholds Post ID-er. (Essensielt for flagg/språksvitsjing).
2.  **UI-Strenger:** Oversettelse av tema- og plugin-spesifikke strenger (knapper, feilmeldinger) som ikke er flyttet til hardkodet kildekode.
3.  **Menyer:** Administrasjon av separate navigasjonsmenyer for hvert språk.

## 2. 🎯 Utfasingsstrategi (Erstatning av WPML-Logikk)

Strategien er å erstatte den databasesentrerte WPML-logikken med Git/YAML-drevet, egendefinert PHP-funksjonalitet.

### Fase I: Forberedelse og Backend ID-knytting (Høyeste Prioritet)

| Oppgave | Beskrivelse | Mål |
| :--- | :--- | :--- |
| **1.1 Egendefinert Metafelt** | Loom må oppdateres for å skrive et egendefinert post-metafelt (f.eks. `sragi_lang_pair_id`) som inneholder den korresponderende sidens Post ID ved publisering. | Skape en varig, WPML-uavhengig språklenke. |
| **1.2 Språksvitsj-funksjon** | Skriv en egendefinert PHP-funksjon (f.eks. `get_paired_lang_url($post_id)`) som leser det nye `sragi_lang_pair_id` metafeltet. | Muliggjøre språkflagg-funksjonalitet. |

### Fase II: UI og Strengadministrasjon

| Oppgave | Beskrivelse | Mål |
| :--- | :--- | :--- |
| **2.1 STRINGS.yaml** | Opprett `_CONFIG/STRINGS.yaml` for å lagre alle UI/tema-strenger (Bunntekst, "Les Mer"-knapper, osv.) i både EN/NB. | SSOT for all UI-tekst, fullt Git-versjonert. |
| **2.2 Strengfunksjon** | Implementer en PHP-funksjon (`get_sragi_string('nøkkel')`) for å lese `STRINGS.yaml` basert på gjeldende språkinnstilling. | Fjerne avhengigheten av WPMLs strengoversetter. |

### Fase III: Meny og Deaktivering

| Oppgave | Beskrivelse | Mål |
| :--- | :--- | :--- |
| **3.1 Meny-Gjenoppbygging** | Bygg WP-menyer manuelt for begge språk etter at WPML-logikken er implementert (siden WPML kontrollerer menyelementene). | Sikre korrekt språkespesifikk navigasjon. |
| **3.2 Full Deaktivering** | Deaktiver WPML og verifiser 100% av all UI, lenke-svitsjing og innholdsaksess på tvers av begge språk. | Eliminere Vendor Lock-in og database-bloat. |

---

## 3. 💡 Konsekvenser for AI-Agenter

* **Ved Koding:** Unngå å referere til eller generere kode som bruker WPML-funksjoner. All ny flerspråklig logikk skal baseres på **YAML-metadata** og de nye egendefinerte feltene (`sragi_lang_pair_id`).
* **Ved Analysen:** Betrakt WPML som en teknisk gjeld som systematisk må elimineres.

---

### 🚀 Neste Steg: Kodeskifte i PHP

WPML-utfasingen er nå dokumentert og isolert. Vi må fikse den umiddelbare feilen i koden.

**Skal vi oppdatere `process.php` nå, slik at Refinery-motoren kan finne `CONTENT-TEMPLATE.yaml`?** 🛠️
