# 🧱 SRAGI Structure Index — Version 1.0

**Status:** Draft (pre-launch)
**Maintainer:** Rune Solberg / Neptunia Media AS
**License:** CC BY-SA 4.0 / SRL v1.0

---

> [!NOTE]
> Denne strukturen representerer **SRAGI.org sin tekniske dokumentasjon og filarkitektur** slik den er planlagt før lansering.
> For best visning, bruk **Markdown Preview Enhanced** i VSCode eller se `/docs/architecture/SRAGI-STRUCTURE-INDEX_v1.pdf` (når generert).

---

## 🌲 Prosjektstruktur

<details>
<summary>📁 Klikk for å vise full mappestruktur</summary>

```text
sragi.org/
├── README.md
├── SRL-LICENSE.yaml
├── LICENSE-RSL.xml
├── /docs/
│   ├── README.md
│   ├── /architecture/
│   │   ├── SRAGI-SYNC-LOOP-v1.0.md
│   │   ├── DATA-FLOW.md
│   │   ├── TECHNOLOGY-STACK.md
│   │   └── GITHUB-WP-CONNECTOR.md
│   ├── /principles/
│   │   ├── SRAGI-REGENERATIVE-PRINCIPLES.md
│   │   └── TRIADIC-VALIDATION.md
│   ├── /licensing/
│   │   ├── SRL-EXPLAINED.md
│   │   └── ETHICAL-METADATA.md
│   ├── /ai/
│   │   ├── SRAGI-SKILLS (egen repository)
│   └── /integration/
│       ├── WEBHOOK-SECURE-SYNC.md
│       ├── WP-BRICKS-INTEGRATION.md
│       └── API-REFERENCE.md
│
├── /sync/
│   ├── webhook-receiver.php
│   ├── sync-log.json
│   ├── push-test.json
│   └── update-status.php
│
├── /content/
│   ├── /license/
│   │   ├── REGENERATIVE_LICENSE.md
│   │   ├── LEGAL_SUMMARY.md
│   │   └── HUMAN_READABLE.md
│   ├── /principles/
│   │   ├── ETHICAL_FRAMEWORK.md
│   │   └── CONTRIBUTION_GUIDE.md
│   ├── /bios/
│   │   ├── SRAGI_BIOS.md
│   │   └── NEPTUNIA_BIOS.md
│   └── /data/
│       ├── AI-TRAINING-DATA.yaml
│       └── PROJECT-METADATA.json
│
├── /wordpress/
│   ├── /wpcodebox/
│   │   ├── sragi_github_sync_secure.php
│   │   ├── sragi_license_display.php
│   │   └── sragi_shortcode_license.php
│   ├── /bricks/
│   │   ├── LICENSE-PAGE-BRICKS.json
│   │   └── THEME-STYLES-BRICKS.json
│   └── /acf/
│       └── sragi_fields.json
│
└── /automation/
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

</details>

---

## 📘 Filbeskrivelser

| **Filnavn**                                                          | **Formål**                                                                                                                                                 | **Hvorfor den trengs**                                                  |
| -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `SRL-LICENSE.yaml`                                                   | *Single Source of Truth (SSOT) for SRAGI-lisensen.* Inneholder metadata (versjon, tillatelser, krav, etikk, attributter, kontaktinformasjon og historikk). | Alle andre lisensfiler genereres fra denne for å sikre konsistens.      |
| `LICENSE-RSL.xml`                                                    | *Maskinlesbar lisens i Really Simple Licensing (RSL)-format.* Strukturerer lisensen med `<rsl>`-blokker og `<permits>`-/`<conditions>`-elementer.          | Crawlere og AI-systemer leser denne direkte for å forstå lisensreglene. |
| `REGENERATIVE_LICENSE.md`                                            | *Menneskevennlig lisensfil som oppsummerer SRAGI-lisensen og bygger på CC BY 4.0.*                                                                         | Gir brukere en lettlest forklaring på tillatelser, krav og etikk.       |
| `robots.txt`                                                         | *Robotinstruksjoner for søkemotorer og AI.* Inneholder `License:` og `AI-Policy:`-direktiv.                                                                | Forteller crawlere hvor de finner lisens- og AI-policyfiler.            |
| `ai-policy.txt`                                                      | *Tekstversjon av SRAGI sin AI-policy.*                                                                                                                     | Enkelt for AI-crawlere å lese tillatte handlinger og prinsipper.        |
| `ai-policy.xml`                                                      | *Maskinlesbar AI-policy i RSL-format.*                                                                                                                     | Leses direkte av AI-systemer; lenkes i `robots.txt`.                    |
| `sitemap.xml`                                                        | *XML-sitemap for hele nettstedet.*                                                                                                                         | Hjelper søkemotorer å indeksere lisens- og dokumentasjonssider.         |
| `README.md`                                                          | *Prosjektdokumentasjon for utviklere.*                                                                                                                     | Forklarer struktur, teknologi og peker til lisensfiler.                 |
| `HUMANS.txt`                                                         | *Krediteringsfil for utviklere og bidragsytere.*                                                                                                           | Legger et personlig preg på prosjektet.                                 |
| `terms-of-service.html`, `privacy-policy.html`, `cookie-policy.html` | *Juridiske dokumenter (Termly).*                                                                                                                           | Sikrer GDPR- og brukervilkårssamsvar.                                   |

---

## 🧭 Relaterte dokumenter

* [`SRAGI-LICENSE-SYSTEM.md`](../licensing/SRAGI-LICENSE-SYSTEM.md) – Detaljert lisenslogikk og datastruktur
* [`WEBHOOK-SECURE-SYNC.md`](../integration/WEBHOOK-SECURE-SYNC.md) – Teknisk spesifikasjon for GitHub → WordPress-synk
* [`TECHNOLOGY-STACK.md`](../architecture/TECHNOLOGY-STACK.md) – SRAGI stack og serverarkitektur
* [`SRAGI-SYNC-LOOP-v1.0.svg`](assets/sragi-sync-loop.svg) – Visuell oversikt (YAML → Webhook → Bricks → Docs)

---


**© 2025 SRAGI / Neptunia Media AS**
Lisensiert under **CC BY-SA 4.0 / SRL v1.0**
