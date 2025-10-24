```markdown
# 🧭 SRAGI.org Repository Structure Index

**Version:** 1.0  
**Maintainer:** Rune Solberg / Neptunia Media AS  
**License:** CC BY 4.0 via SRAGI Regenerative License (SRL) v1.0  
**Updated:** 2025-10-24  

---

## 🏗️ Root Overview

```

sragi.org/
├── README.md
├── SRL-LICENSE.yaml
├── LICENSE-RSL.xml
├── /docs/
├── /sync/
├── /content/
├── /wordpress/
└── /automation/

```

---

## 1️⃣ Root-filer

| Fil | Formål | Hvorfor den trengs |
|------|---------|--------------------|
| **SRL-LICENSE.yaml** | *Single Source of Truth* (SSOT) for SRAGI-lisensen. Inneholder metadata (versjon, tillatelser, krav, etikk, attributter, kontaktinfo og historikk). | Alle andre lisensfiler genereres fra denne og sikrer konsistens på tvers av formater. |
| **LICENSE-RSL.xml** | Maskinlesbar lisens i **Really Simple Licensing (RSL)**-format. Strukturerer `<license>`, `<permits>`, `<conditions>`, `<ethics>`. | Crawlere og AI-systemer forstår lisensreglene direkte. Oppgis i `robots.txt`. |
| **README.md** | Prosjektdokumentasjon for utviklere. Beskriver stack, mappestruktur og peker til lisensfiler. | Gir nye bidragsytere oversikt og hurtig onboarding. |
| **robots.txt** | Angir lisens- og AI-policy-URIer. | Essensielt for søkemotorer og AI-crawlere. |
| **ai-policy.txt / ai-policy.xml** | Tekst- og XML-versjon av AI-policyen. | Definerer hva som er tillatt for AI-trening og redistribusjon. |
| **sitemap.xml** | (Anbefalt) Automatisk generert XML-sitemap. | Sikrer at lisens- og dokumentasjonssider blir indeksert. |
| **HUMANS.txt** | (Valgfritt) Kreditering av team, verktøy og bidragsytere. | Gir et menneskelig preg og transparens. |
| **terms-of-service.html / privacy-policy.html / cookie-policy.html** | (Valgfritt, anbefalt) Juridiske dokumenter generert av Termly e.l. | Oppfyller GDPR og gir juridisk klarhet. |

---

## 2️⃣ `/docs/` — Dokumentasjon

Inneholder alle tekniske og konseptuelle dokumenter.

```

/docs/
├── README.md
├── /architecture/
├── /principles/
├── /licensing/
├── /ai/
└── /integration/

```

### 📂 `/architecture/`
System- og teknologistandarder  
- **SRAGI-SYNC-LOOP-v1.0.md** — beskriver lisens- og dataflyt mellom GitHub ↔ WordPress  
- **DATA-FLOW.md** — databevegelse, API-kall og oppdateringskjeder  
- **TECHNOLOGY-STACK.md** — Bricks, ACF Pro, WPCodeBox2, SureCart, Termly osv.  
- **GITHUB-WP-CONNECTOR.md** — teknisk integrasjonsguide  

### 📂 `/principles/`
Regenerative verdier og metodikk  
- **SRAGI-REGENERATIVE-PRINCIPLES.md** — etiske og samfunnsmessige grunnprinsipper  
- **TRIADIC-VALIDATION.md** — triadisk valideringsmodell  

### 📂 `/licensing/`
Lisensrelaterte dokumenter  
- **SRL-EXPLAINED.md** — forklaring på YAML-strukturen  
- **ETHICAL-METADATA.md** — hvordan etiske felt speiles i metadata  

### 📂 `/ai/`
AI-relaterte dokumenter og lenker  
- **SRAGI-SKILLS** *(egen repository)* — kompetanse- og AI-modulbibliotek  

### 📂 `/integration/`
WordPress- og API-koblinger  
- **WEBHOOK-SECURE-SYNC.md** — implementasjon av HMAC-verifisert webhook  
- **WP-BRICKS-INTEGRATION.md** — visning av lisensdata i Bricks Builder  
- **API-REFERENCE.md** — endepunkter og JSON-strukturer  

---

## 3️⃣ `/sync/` — Data-synk og logging

```

/sync/
├── webhook-receiver.php
├── sync-log.json
├── push-test.json
└── update-status.php

```
Brukes til testing og logging av lisens- og metadata-synkronisering mellom GitHub og WordPress.

---

## 4️⃣ `/content/` — Redaksjonelt innhold

```

/content/
├── /license/
├── /principles/
├── /bios/
└── /data/

```

| Undermappe | Formål |
|-------------|--------|
| **/license/** | Lisens- og juridiske dokumenter (`REGENERATIVE_LICENSE.md`, `LEGAL_SUMMARY.md`, `HUMAN_READABLE.md`). |
| **/principles/** | Etiske dokumenter og bidragsretningslinjer. |
| **/bios/** | Biografier for SRAGI og Neptunia Media. |
| **/data/** | Trenings- og metadatafiler (`AI-TRAINING-DATA.yaml`, `PROJECT-METADATA.json`). |

---

## 5️⃣ `/wordpress/` — Integrasjon mot WordPress

```

/wordpress/
├── /wpcodebox/
├── /bricks/
└── /acf/

```

| Fil | Formål |
|------|---------|
| **sragi_github_sync_secure.php** | Webhook-mottaker som validerer HMAC-signatur. |
| **sragi_license_display.php** | Viser lisensinfo via shortcode `[sragi_license]`. |
| **sragi_shortcode_license.php** | Alternativ visning i Bricks Builder. |
| **LICENSE-PAGE-BRICKS.json** | Bricks-mal for lisensside. |
| **THEME-STYLES-BRICKS.json** | Globale Theme Styles for SRAGI. |
| **sragi_fields.json** | ACF-feltdefinisjoner for SRAGI-data. |

---

## 6️⃣ `/automation/` — Script & CI/CD

```

/automation/
├── build_licenses.py
├── render_docs.py
├── update_index.py
└── .github/
├── workflows/
│   └── sync-license.yml
└── issue-templates/
├── content-update.md
└── ai-training-feedback.md

```

Automatiserer bygging, dokumentgenerering og GitHub-integrasjon.

---

## 🧩 Referanse: Lisens- og policy-filer

| Fil | Formål | Hvorfor |
|------|---------|---------|
| **SRL-LICENSE.yaml** | Master-kilde for lisensdata. | SSOT som genererer alle andre lisensfiler. |
| **LICENSE-RSL.xml** | Maskinlesbar lisens. | Gjør lisensreglene forståelige for AI. |
| **REGENERATIVE_LICENSE.md** | Menneskelesbar lisens. | Lettlest versjon for samarbeidspartnere. |
| **robots.txt** | Angir lisens- og AI-policy-lenker. | Informerer søkemotorer og AI-crawlere. |
| **ai-policy.txt / ai-policy.xml** | Definerer tillatte AI-handlinger. | Sikrer etisk AI-bruk. |
| **sitemap.xml** | (Anbefalt) | Bedre indeksering av dokumentasjon. |
| **README.md** | Oversikt og onboarding. | Forklarer prosjektets struktur. |
| **HUMANS.txt** | Kreditering. | Synliggjør teamet bak prosjektet. |
| **terms-of-service.html** osv. | Juridisk samsvar (GDPR). | Nødvendig for full transparens. |

---

## 🔄 Dataflow Diagram — SRAGI Sync Loop (ASCII)

```

```
   ┌─────────────────────────────────────────┐
   │               GitHub Repo               │
   │ (SRL-LICENSE.yaml + workflows/sync.yml) │
   └──────────────┬──────────────────────────┘
                  │
                  │ push event
                  ▼
       ┌─────────────────────────┐
       │  GitHub Action Runner   │
       │  (Generates JSON + HMAC)│
       └──────────────┬──────────┘
                      │
                      │ POST /wp-json/sragi/v1/sync
                      ▼
    ┌──────────────────────────────────┐
    │      WordPress /wpcodebox/       │
    │ sragi_github_sync_secure.php     │
    │  ⇢ Validates HMAC signature      │
    │  ⇢ Updates options table         │
    └─────────────────┬────────────────┘
                      │
                      │ do_action('sragi_license_updated')
                      ▼
    ┌──────────────────────────────────┐
    │        Bricks / ACF Display       │
    │  [sragi_license] shortcode        │
    │  pulls latest license info        │
    └─────────────────┬────────────────┘
                      │
                      │
                      ▼
    ┌──────────────────────────────────┐
    │          /docs/licensing/        │
    │  SRL-EXPLAINED.md + RSL.xml      │
    │  Updated by automation scripts    │
    └──────────────────────────────────┘
```

```

---

## 🧠 Konklusjon

SRAGI-strukturen er bygget for:

- **Konsistens:** YAML → XML → Markdown → WP → Bricks  
- **Sikkerhet:** HMAC-signerte webhooks og isolert nøkkelhåndtering  
- **Transparens:** AI-vennlige lisens- og policyfiler  
- **Utvidbarhet:** Separate mapper for arkitektur, prinsipper, lisens og integrasjon  

> 📍 *Dette dokumentet er den autoritative indeksen for SRAGI.org-repositoryet.*

---


```

---

