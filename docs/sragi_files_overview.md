# Oversikt over filer for sragi.org

Denne oversikten beskriver hvilke filer som bør ligge i rottreet til **sragi.org** for å sikre at lisens, etikk, robotinstrukser og AI‑policyer er tydelige både for mennesker og maskiner. Tabellene under viser navnet på filen, dens rolle, samt hvorfor den er nødvendig og hvordan den peker til andre filer.

## Kjernefiler

| Filnavn | Formål | Hvorfor den trengs |
|--------|--------|------------------|
| **`SRL‑LICENSE.yaml`** | *Single Source of Truth* (SSOT) for SRAGI‑lisensen. Inneholder metadata (versjon, tillatelser, krav, etikk, attributter, kontaktinformasjon og historikk). | Alle andre lisensfiler genereres fra denne. Oppdateres når lisensen endres og sørger for konsistens på tvers av formater. |
| **`LICENSE‑RSL.xml`** | Maskinlesbar lisens i Really Simple Licensing (RSL)–format. Strukturerer lisensen med `<rsl>`‑ og `<license>`‑blokker, `<permits>`‑ og `<conditions>`‑elementer og et etisk rammeverk. | Crawlere og AI‑systemer leser denne filen for å forstå lisensreglene. Oppgis med `License:`‑direktivet i `robots.txt`. |
| **`REGENERATIVE_LICENSE.md`** | Menneskevennlig lisensfil som oppsummerer SRAGI‑lisensen, forklarer at den bygger på CC BY 4.0, lister tillatelser og krav, og beskriver de aspirerende etiske prinsippene. | Gir brukere og samarbeidspartnere en lettlest forklaring på lisensen. |
| **`robots.txt`** | Robotinstruksjoner for søkemotorer og AI. Må minst inneholde: `User‑agent: *`, `License: https://sragi.org/LICENSE‑RSL.xml` og `AI‑Policy: https://sragi.org/ai‑policy.xml`. | Forteller crawlere hvor de finner lisensfilen og AI‑policydokumentene. Uten denne kan robotene anta feil filnavn eller ignorere lisensen. |
| **`ai‑policy.txt`** | Tekstversjon av SRAGIs AI‑policy. Beskriver hvilke AI‑handlinger som er tillatt (f.eks. `training permitted`, `redistribution permitted`) og hvilke som er forbudt, samt etiske prinsipper som «ethically open for regenerative learning». | Gir AI‑crawlere et enkelt format for å lese retningslinjene. |
| **`ai‑policy.xml`** | Maskinlesbar AI‑policy i RSL‑format. Inneholder felter som `<training>permitted</training>` og `<redistribution>permitted</redistribution>`. | AI‑systemer som støtter RSL kan lese dette dokumentet direkte. Lenken legges inn i `robots.txt` med `AI‑Policy:`‑direktiv. |
| **`sitemap.xml`** | (Anbefalt) XML‑sitemap over nettstedet. | Hjelper søkemotorer med å indeksere lisenssider, dokumentasjon og andre viktige sider. |
| **`README.md`** | Prosjektdokumentasjon for utviklere. Forklarer hva `sragi.org` er, beskriver mappestrukturen, teknologivalgene (WordPress, Bricks, ACF Pro osv.), og peker til lisensfilene. | Gir nye bidragsytere oversikt over prosjektet og prosessene. |
| **`HUMANS.txt`** | (Valgfritt) Informasjon om hvem som har bygget og bidratt til nettsiden – f.eks. Rune Solberg, Neptunia Media, og verktøy som Bricks, Bricksforge, ACF Pro og SureCart. | Legger et personlig preg og gir kreditering til teamet. |
| **`terms‑of‑service.html`, `privacy‑policy.html`, `cookie‑policy.html`** | (Valgfritt, men anbefalt) Juridiske dokumenter generert via Termly eller lignende. | Oppfyller lovpålagte krav (GDPR, forbrukerlovgivning) og definerer brukerrettigheter. Disse kan også lenkes via standard `Policy:`‑direktiv i `robots.txt`. |

## Koblinger og avhengigheter

* **Robots.txt** er bindeleddet mellom filene. Uansett hva du kaller lisensfilen, må `robots.txt` inneholde en `License:`‑linje med den eksakte URL‑en til lisensfilen. Hvis filen heter `LICENSE‑RSL.xml`, må du skrive:
  
  ```
  License: https://sragi.org/LICENSE‑RSL.xml
  AI‑Policy: https://sragi.org/ai‑policy.xml
  ```
  
  Det samme gjelder `AI‑Policy:`. Dette sikrer at søkemotorer og AI‑roboter finner filene.

* **AI‑policydokumentene** bør referere tilbake til lisensen, og lisensfilen bør peke til kildematerialet i YAML (via `source`‑ og `rightsHolder`‑felter). Dette gjør det klart hvem som eier rettighetene, og hvor eventuelle endringer må oppdateres.

* **Lisensfilene (XML/MD)** genereres fra `SRL‑LICENSE.yaml` ved hjelp av et script (f.eks. `build_licenses.py`). Hver gang `SRL‑LICENSE.yaml` endres (f.eks. ny versjon), kjør scriptet på nytt og commit de regenererte filene.

* **Versjonsoppgraderinger** håndteres ved å oppdatere `meta.version`, `meta.last_updated` og legge til en ny post i `history` i YAML‑filen. Etterpå genererer du nye versjoner av de andre filene. Husk å oppdatere `robots.txt` hvis du endrer filnavn.

Denne oversikten gir en komplett og konsistent struktur som lar både mennesker og maskiner forstå SRAGI‑lisensen, AI‑policyene og andre juridiske forhold. Sørg for at hver fil holdes oppdatert og at lenkene peker til korrekte steder, så unngår du forvirring og mulig misbruk.
