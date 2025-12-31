---
title: Neptunia Media AS – Teknologistack v2.2 (Complete Master)
version: 2.2
updated: 2025-11-29
license: SRL-1.12 (CC BY 4.0)
maintainer: Rune Solberg / SRAGI Muse
---

# 🧭 Neptunia Media AS – Teknologistack (v2.2)

> *“Technology is the soil — Regeneration is the seed.”*
> En hybrid-arkitektur som kombinerer "Headless" innholdsstyring med robust e-handel.

---

## 🖥️ Plattform og Infrastruktur

| Komponent | Status | Beskrivelse |
| :--- | :--- | :--- |
| **Hosting** | ✅ **One.com Guru** | Høyytelse-hosting. PHP 8.x, NGINX. ("Managed WP" avviklet). |
| **CDN** | ⏳ **Bunny.net** | Global levering av media. Klar for aktivering. |
| **Database** | ✅ **MariaDB** | Renset for foreldreløse data og optimalisert. |
| **E-post** | ✅ **Post SMTP** | Sikrer levering av transaksjonelle e-poster (kvitteringer/login). |

---

## 🧱 Kjerne-Verktøy (Bygg & Visning)

| Verktøy | Funksjon |
| :--- | :--- |
| **Bricks Builder** | **Visning.** Henter data direkte fra Native Meta. Ingen bloat. |
| **Bricksforge** | **Magien.** GSAP-animasjoner, Pro Forms og logikk. |
| **HappyFiles Pro** | **Orden.** Strukturering av media og mapper (`/visuals/`). |

---

## 🧠 Dataflyt & Struktur (The Clean Core)

*Her har vi erstattet ACF Pro med en Git-basert arbeidsflyt.*

| Verktøy | Rolle |
| :--- | :--- |
| **CPT UI** | **Skjelettet.** Definerer *Aktører* og *Konsepter* og *Pilarer*. (Erstatter ACF GUI). |
| **WPCodeBox 2** | **Hjernen.** Kjører `SRAGI Sync Engine` (PHP) som bygger siden fra tekstfiler. |
| **WPML** | **Språk.** Multispråklig innhold (NO/EN) og URL-struktur. |
| **Markdown (Git)** | **Kilden (SSOT).** Alt innhold skrives lokalt og synkroniseres opp. |

---

## 💳 E-handel og Medlemskap (Business Logic)

*Disse systemene er beholdt for å drifte kurs og salg.*

| System | Bruksområde |
| :--- | :--- |
| **SureCart** | Checkout for digitale produkter, donasjoner og kurs. |
| **SureMembers** | Tilgangsstyring. Låser innhold (kurs) basert på kjøp. |
| **Presto Player Pro** | Videospiller. GDPR-sikker, støtter kapitler og private videoer. |

---

## 🛡️ Drift, Sikkerhet & Compliance

| Verktøy | Status | Funksjon |
| :--- | :--- | :--- |
| **WPVivid Pro** | 💎 Lifetime | **Backup & Staging.** "Blueprints" og snapshos til skyen. |
| **Adv. DB Cleaner** | 💎 Lifetime | **Vaktmester.** Holder databasen slank og rask. |
| **WP Armour** | Gratis | **Sikkerhet.** Honeypot anti-spam (Erstatter One.com Spam). |
| **Complianz** | 💎 Pro | **Jus (GDPR).** Native cookie-blokkering. (Erstatter Termly). |
| **The SEO Framework** | Gratis | **Synlighet.** Lettvekts SEO. (Erstatter RankMath). |

---

## 🗂️ Designsystem

**Typografi:**
* Headlines: **Bodoni Moda**
* Body: **Didact Gothic**

**Fargepalett (Neptunia):**
| Rolle | Farge | HEX |
| :--- | :--- | :--- |
| Primær | Dyp blå | `#001242` |
| Sekundær | Mørk grønn | `#3A5A40` |
| Aksent | Lys blå | `#0094C6` |
| Energi | Lys grønn | `#85FFC7` |

---

## ⚙️ Konfigurasjon (Bricks)

* ✅ **Global Class Manager:** PÅ
* ✅ **CSS Variables Manager:** PÅ
* 🚫 **Bricks SEO/OG:** AV (Styres av TSF)
* ✅ **Custom Image Sizes:** PÅ (Hero, Content, Thumbnail, etc.)

---

**Status:** ✅ Operativ
**Sist oppdatert:** 29. November 2025
**Vedlikeholdes av:** Rune Solberg / SRAGI Muse

---
