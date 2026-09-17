# 🗺️ SRAGI ROADMAP — Q4 2025 → Q1 2026

**Fil:** `SRAGI-ROADMAP-2025-Q4.md`  
**Status:** AKTIV  
**Versjon:** 1.0  
**Oppdatert:** 2025-12-10  
**Eier:** Rune Solberg / Neptunia Media AS

---

## 📊 NÅVÆRENDE STATUS: Desember 2025

```
┌─────────────────────────────────────────────────────────────────┐
│  SRAGI SYSTEM HEALTH                                            │
├─────────────────────────────────────────────────────────────────┤
│  SSOT Layer (_CONFIG/)          ████████████████████  100% ✅   │
│  Standards (docs/standards/)    ████████████████░░░░   80% ✅   │
│  Architecture (docs/arch/)      ██████████████░░░░░░   70% ⚠️   │
│  Sync Engine (Loom)             ████░░░░░░░░░░░░░░░░   20% 🔴   │
│  Content (Actual Pages)         ██░░░░░░░░░░░░░░░░░░   10% 🔴   │
│  WordPress Integration          ████████░░░░░░░░░░░░   40% 🟡   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🎯 MILEPÆLER

### FASE 0: Stabilisering 🔧
**Tidsramme:** Uke 50-51 (Desember 2025)  
**Mål:** Rydde opp i dokumenter med `c` og `r` flagg

| # | Oppgave | Prioritet | Status |
|---|---------|-----------|--------|
| 0.1 | Oppdater `BUNNY-CDN-INTEGRATION.md` (v1.0c → v2.0) | 🔴 | ⬜ TODO |
| 0.2 | Merge/arkiver `VISUAL-PHILOSOPHY.md` (v1.3c) | 🟡 | ⬜ TODO |
| 0.3 | Evaluer `ACCESSIBILITY-STANDARDS.md` (v1.1c) | 🟡 | ⬜ TODO |
| 0.4 | Align `WEB-BIOS.yaml` paths (v2.2.0r) | 🟡 | ⬜ TODO |
| 0.5 | Oppdater `HAPPYFILES-STRUCTURE.md` for Pro 1.9 (v2.1r) | 🟢 | ⬜ TODO |

**Leveranse:** Alle dokumenter på `PRODUCTION READY` status

---

### FASE 1: Pipeline MVP 🔄
**Tidsramme:** Uke 51-52 (Desember 2025)  
**Mål:** Én artikkel fra Git til WordPress (manuelt OK)

| # | Oppgave | Avhenger av | Status |
|---|---------|-------------|--------|
| 1.1 | Kartlegg Loom Engine status (finnes kode?) | — | ⬜ TODO |
| 1.2 | Implementer TSF PHP-snippets i WPCodeBox | — | ⬜ TODO |
| 1.3 | Lag første test-artikkel (`what-is-sragi.md`) | 1.2 | ⬜ TODO |
| 1.4 | Manuell push til WordPress via REST API | 1.2, 1.3 | ⬜ TODO |
| 1.5 | Dokumenter workflow i `CONTENT-CREATION-WORKFLOW.md` | 1.4 | ⬜ TODO |

**Leveranse:** Bevis på ende-til-ende flyt

---

### FASE 2: Kjerneinnhold 📝
**Tidsramme:** Uke 1-4 (Januar 2026)  
**Mål:** 15-20 sider live på sragi.org

#### 2A: About-sider (Kritisk)
| Side | Slug | Pilar | Status |
|------|------|-------|--------|
| What is SRAGI? | `what-is-sragi` | `system_thinking` | ⬜ |
| Core Principles | `core-principles` | `regeneration` | ⬜ |
| Vision 2040 | `vision-2040` | `generativity` | ⬜ |
| The Team | `team` | `intelligence` | ⬜ |

#### 2B: Pilar-sider (Høy)
| Side | Slug | Status |
|------|------|--------|
| Systems Thinking | `pillar-system-thinking` | ⬜ |
| Regeneration | `pillar-regeneration` | ⬜ |
| Adaptivity | `pillar-adaptivity` | ⬜ |
| Generativity | `pillar-generativity` | ⬜ |
| Intelligence | `pillar-intelligence` | ⬜ |

#### 2C: Domene-sider (Medium)
| Side | Slug | Status |
|------|------|--------|
| Technology & AI | `domain-technology` | ⬜ |
| Education & Learning | `domain-education` | ⬜ |
| Society & Culture | `domain-society` | ⬜ |

#### 2D: Første Reflections (Lavere)
| Side | Type | Status |
|------|------|--------|
| SRAGI Launch Reflection | `reflection` | ⬜ |
| AI Orchestration Journey | `reflection` | ⬜ |
| Regenerative Principles in Practice | `reflection` | ⬜ |

**Leveranse:** Navigerbar nettside med kjerneinnhold

---

### FASE 3: Automatisering 🤖
**Tidsramme:** Februar-Mars 2026  
**Mål:** Full Loom Engine + CI/CD

| # | Komponent | Beskrivelse | Status |
|---|-----------|-------------|--------|
| 3.1 | Loom Validator | Python: Les frontmatter, valider mot VALIDATION_RULES.yaml | ⬜ |
| 3.2 | Loom Publisher | Python: REST API push til WordPress | ⬜ |
| 3.3 | GitHub Action | Webhook trigger på push til main | ⬜ |
| 3.4 | QA Dashboard | Statusvisning i Mission Control | ⬜ |

**Leveranse:** Automatisk publisering ved git push

---

### FASE 4: Skalering 📈
**Tidsramme:** Q2 2026  
**Mål:** Community, bidragsytere, sragi-skills

| # | Oppgave | Status |
|---|---------|--------|
| 4.1 | Contributor Guide | ⬜ |
| 4.2 | sragi-skills repository aktivering | ⬜ |
| 4.3 | Community onboarding | ⬜ |
| 4.4 | Partner-integrasjoner | ⬜ |

---

## 📅 KALENDERVISNING

```
2025
────────────────────────────────────────────────────────────────
Desember  │ Uke 50 │ Uke 51 │ Uke 52 │
          │ FASE 0 │ FASE 0 │ FASE 1 │
          │ Stabil │ Stabil │ MVP    │
────────────────────────────────────────────────────────────────

2026
────────────────────────────────────────────────────────────────
Januar    │ Uke 1  │ Uke 2  │ Uke 3  │ Uke 4  │
          │ FASE 1 │ FASE 2 │ FASE 2 │ FASE 2 │
          │ MVP    │ About  │ Pilars │ Domain │
────────────────────────────────────────────────────────────────
Februar   │ Uke 5  │ Uke 6  │ Uke 7  │ Uke 8  │
          │ FASE 2 │ FASE 3 │ FASE 3 │ FASE 3 │
          │ Refl.  │ Loom   │ Loom   │ CI/CD  │
────────────────────────────────────────────────────────────────
Mars      │ Uke 9  │ Uke 10 │ Uke 11 │ Uke 12 │
          │ FASE 3 │ FASE 3 │ FASE 4 │ FASE 4 │
          │ Test   │ Launch │ Scale  │ Scale  │
────────────────────────────────────────────────────────────────
```

---

## 🎪 PARALLELLE SPOR

Mens hovedveien følges, kan disse kjøres parallelt:

| Spor | Ansvarlig | Mål |
|------|-----------|-----|
| **Visuelt innhold** | Canva/AI | Lage hero-bilder for pilar-sider |
| **SEO-research** | Gemini/Grok | Keyword-analyse for domene-sider |
| **WordPress UX** | Bricks | Templating for innholdssider |
| **AI Skills** | Claude | Utvide sragi-skills biblioteket |

---

## 🚨 RISIKO & MITIGERING

| Risiko | Sannsynlighet | Konsekvens | Mitigering |
|--------|---------------|------------|------------|
| Loom Engine mangler | Høy | Manuell publisering | Lag minimal Python-validator |
| WPML-konflikter | Medium | Sync-feil | Bruk YAML-strategi, minimal WPML |
| Overambisiøs roadmap | Høy | Utbrenthet | Kairos-prinsipp: Flyt > Deadlines |
| One.com begrensninger | Lav | Performance | Bunny CDN allerede implementert |

---

## 📏 SUKSESSKRITERIER

### Ved utgangen av Fase 1 (Uke 52):
- [ ] Én artikkel live på sragi.org via Git-workflow
- [ ] TSF-integrasjon fungerer
- [ ] Dokumentert prosess

### Ved utgangen av Fase 2 (Uke 4):
- [ ] 15+ sider live
- [ ] Navigasjon fungerer
- [ ] SEO-grunnlag på plass

### Ved utgangen av Fase 3 (Uke 12):
- [ ] Automatisk publisering fungerer
- [ ] Alle valideringsregler håndhevet
- [ ] Dashboard viser systemhelse

---

## 🌀 KAIROS-PÅMINNELSE

> **Denne roadmapen er en guide, ikke en fengsel.**
> 
> Når flyten er god, akselerér.  
> Når motstanden er stor, reflektér.  
> Når energien mangler, hvil.
> 
> R > 1 gjelder også for deg.

---

**© 2025 Rune Solberg / Neptunia Media AS**  
Licensed under CC-BY-4.0
