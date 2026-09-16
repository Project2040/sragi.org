# 🚨 SRAGI INNHOLDSGENERERING — OBLIGATORISK INSTRUKS

**Fil:** `SRAGI-CONTENT-CHECKLIST.md`  
**Status:** AKTIV PRODUKSJONSSTANDARD  
**Versjon:** 1.0  
**Dato:** 2025-12-10  
**Gyldig for:** Alle som genererer innhold til sragi.org

---

## ⚠️ LES DETTE FØR DU SKRIVER ÉN ENESTE LINJE

Denne instruksen er **SSOT-basert** og henter alle regler fra `_CONFIG/VALIDATION_RULES.yaml`.  
Bryter du reglene, vil Loom Validator blokkere publisering.

---

## 1. 📄 FRONTMATTER (Hjernen i Fila)

Hver `.md`-fil **MÅ** ha YAML frontmatter. Her er minimumskravene:

### 1.1 Påkrevde Felt (Alltid)

```yaml
---
meta:
  type: "documentation"        # documentation | reflection | system_doc | profile
  slug: "your-page-slug"       # MÅ matche filnavn (uten .md)
  status: "draft"              # draft | review | published
  
ia:
  pillar: "system_thinking"    # MÅ være gyldig term fra TAXONOMY_GRAPH.yaml
---
```

### 1.2 Påkrevde Felt (For Publisering)

```yaml
meta:
  title_nb: "Norsk tittel"
  title_en: "English title"

seo:
  title: "SEO Title for Google (45-60 tegn)"
  description: "Meta description som vises i søkeresultater (140-170 tegn)"
```

### 1.3 Valgfrie Felt

```yaml
seo:
  canonical_url: "https://sragi.org/..."  # Kun hvis innhold er syndikert
  noindex: false                           # true = skjul fra Google

visual:
  og_image: "path/to/image-social.jpg"    # 1200x630 px

sync:
  auto_publish: false
  wp_id: null
```

---

## 2. 🏷️ SEO-REGLER (Harde Grenser)

| Felt | Min | Maks | Optimal | Eksempel |
|------|-----|------|---------|----------|
| **SEO Title** | 45 | 60 | 50-55 | "Systems Thinking: A Regenerative Approach" |
| **Meta Description** | 140 | 170 | 150-160 | "Learn how systems thinking enables regenerative design..." |
| **Slug** | 3 | 60 | — | `systems-thinking-introduction` |
| **Alt Text** | 5 | 125 | — | "Diagram showing interconnected feedback loops in living systems" |

### 2.1 Slug-regler

✅ **Tillatt:** `a-z`, `0-9`, `-` (bindestrek)  
❌ **Forbudt:** Æ, Ø, Å, store bokstaver, understrek, mellomrom  
❌ **Reserverte ord:** `test`, `tmp`, `draft`

```
✅ systems-thinking-introduction
✅ sragi-core-principles-2025
❌ Systems_Thinking
❌ systemtenkning-øvelse
❌ test-article
```

### 2.2 Slug MÅ Matche Filnavn

```
Fil: systems-thinking.md
Slug i frontmatter: systems-thinking  ✅

Fil: my-article.md
Slug i frontmatter: another-slug      ❌ BLOKKERT
```

---

## 3. 📝 MARKDOWN-STRUKTUR

### 3.1 Overskrifter

| Regel | Beskrivelse |
|-------|-------------|
| **Én H1** | Kun én `# Tittel` per fil |
| **H1 = title_en** | H1 MÅ matche `meta.title_en` i frontmatter |
| **Ingen hopp** | H2 → H4 er forbudt. Må gå H2 → H3 → H4 |
| **Sentence case** | "Core principles", IKKE "CORE PRINCIPLES" |

```markdown
# Systems Thinking in Practice          ← H1 (én gang)

## Understanding Patterns               ← H2

### Feedback Loops                      ← H3

#### Positive Feedback                  ← H4

### Flow Dynamics                       ← H3 (tilbake til nivå 3)
```

### 3.2 Lenker

✅ **Beskrivende tekst:**
```markdown
Learn more about [regenerative principles](/about/principles).
```

❌ **Forbudt:**
```markdown
Click [here](/about/principles) to learn more.
Les [mer](/about/principles).
```

### 3.3 Kodeblokker

**MÅ ha språk-hint:**

```yaml
# ✅ Riktig
code: "example"
```

```
# ❌ Feil (mangler språk)
code: "example"
```

**Tillatte språk:** `yaml`, `json`, `python`, `php`, `bash`, `javascript`, `html`, `css`, `sql`, `markdown`, `text`

---

## 4. 🏛️ TAKSONOMI (Gyldige Verdier)

Alle taksonomi-felt MÅ bruke verdier fra `TAXONOMY_GRAPH.yaml`.

### 4.1 Pillars (Påkrevd)

| Slug | Navn (EN) | Navn (NB) |
|------|-----------|-----------|
| `system_thinking` | Systems Thinking | Systemtenkning |
| `regeneration` | Regeneration | Regenerasjon |
| `adaptivity` | Adaptivity | Adaptivitet |
| `generativity` | Generativity | Generativitet |
| `intelligence` | Intelligence | Intelligens |

### 4.2 Domains (Valgfri)

| Slug | Navn |
|------|------|
| `education` | Education & Learning |
| `technology` | Technology & AI |
| `society` | Society & Culture |
| `ecology` | Ecology & Nature |
| `economy` | Economy & Finance |
| `health` | Health & Wellbeing |
| `art` | Art & Aesthetics |
| `architecture` | Architecture & Design |

### 4.3 Andre Taksonomier (Valgfrie)

- **Contexts:** `philosophical`, `practical`, `technical`, `poetic`, `scientific`, `experiential`, `visionary`
- **Phases:** `emergence`, `growth`, `maturity`, `decline`, `rebirth`, `integration`
- **Scales:** `individual`, `relational`, `organizational`, `societal`, `planetary`, `cosmic`
- **Modes:** `matrix`, `patrix`, `elantrix`

---

## 5. 🖼️ BILDER OG MEDIA

### 5.1 Påkrevd Alt-tekst

**ALLE bilder MÅ ha alt-tekst.**

```markdown
![Diagram of SRAGI's five core pillars arranged in a pentagon](../visuals/content/sragi-pillars-diagram-medium.avif)
```

❌ **Forbudt i alt-tekst:**
- "image", "bilde", "photo", "placeholder"
- Tom streng

### 5.2 Filformat-prioritet

| Format | Bruksområde |
|--------|-------------|
| **AVIF** | Foretrukket for web (hero, content, tokens) |
| **WebP** | Fallback for eldre nettlesere |
| **JPG** | Kun for sosiale medier og OG-bilder |
| **PNG** | Kun for master/original (arkiv) |
| **SVG** | Diagrammer og ikoner |

### 5.3 Navnekonvensjon

```
[tool]-[beskrivelse]-[år]-[ratio]-[størrelse].format

Eksempler:
gemini-sragi-pillars-2025-16x9-large.avif
canva-hero-regeneration-2025-3x2-medium.avif
affinity-logo-icon-1x1-small.avif
```

### 5.4 Størrelser (Fra Pipeline)

| Suffiks | Maks Bredde | Bruk |
|---------|-------------|------|
| `-large` | 1920 px | Hero-seksjoner |
| `-medium` | 1200 px | Featured image, innhold |
| `-small` | 600 px | Tokens, kort, grid |
| `-social` | 1080 px | SoMe-deling |

---

## 6. 🌍 FLERSPRÅKLIGHET

### 6.1 Filstruktur (Twin-File Strategy)

| Språk | Filnavn | Eksempel |
|-------|---------|----------|
| **Engelsk (Master)** | `[slug].md` | `systems-thinking.md` |
| **Norsk** | `[slug]-nb.md` | `systems-thinking-nb.md` |
| **YAML Controller** | `[slug].yaml` | `systems-thinking.yaml` |

### 6.2 Innholdsregel

Den engelske fila er **struktur-master**. Den norske fila MÅ speile samme overskriftshierarki.

---

## 7. ✅ PRE-FLIGHT SJEKKLISTE

Før du committer/sender til review:

### Frontmatter
- [ ] `meta.type` er satt (documentation/reflection/system_doc/profile)
- [ ] `meta.slug` matcher filnavnet
- [ ] `meta.status` er satt
- [ ] `ia.pillar` bruker gyldig term

### For Publisering
- [ ] `meta.title_nb` og `meta.title_en` er utfylt
- [ ] `seo.title` er 45-60 tegn
- [ ] `seo.description` er 140-170 tegn

### Markdown
- [ ] Kun én H1
- [ ] H1 matcher `title_en`
- [ ] Ingen overskriftshopp
- [ ] Alle lenker har beskrivende tekst
- [ ] Alle kodeblokker har språk-hint

### Bilder
- [ ] Alle bilder har meningsfull alt-tekst (5-125 tegn)
- [ ] Bilder følger navnekonvensjonen
- [ ] Bilder er optimalisert (AVIF/WebP foretrukket)

### Taksonomi
- [ ] Alle taxonomy-verdier finnes i `TAXONOMY_GRAPH.yaml`

---

## 8. 🚫 VANLIGE FEIL (Unngå Disse!)

| Feil | Problem | Løsning |
|------|---------|---------|
| Slug med æøå | `regenerativ-øvelse` | `regenerativ-ovelse` |
| Manglende pillar | Frontmatter uten `ia.pillar` | Legg til gyldig pillar |
| For lang tittel | "The Complete and Comprehensive Guide to Understanding Systems Thinking in Regenerative Contexts" (95 tegn) | Kutt til 60 tegn |
| H1-H3 hopp | `# Title` etterfulgt av `### Subsection` | Bruk `## Section` først |
| "Click here" | `Click [here](/page)` | `Read the [full guide](/page)` |
| Generisk alt | `alt="bilde"` | `alt="Solar panel array on green roof"` |

---

## 9. 📚 REFERANSER

| Dokument | Innhold |
|----------|---------|
| `_CONFIG/VALIDATION_RULES.yaml` | Maskinlesbare regler (SSOT) |
| `_CONFIG/TAXONOMY_GRAPH.yaml` | Alle gyldige taksonomi-termer |
| `_CONFIG/CONTENT-TEMPLATE.yaml` | Full frontmatter-schema |
| `docs/standards/SEO-PROTOCOL.md` | Utdypende SEO-veiledning |
| `docs/standards/DOCUMENTATION-STANDARDS.md` | Markdown-konvensjoner |
| `docs/standards/VISUAL-PROTOCOL.md` | Bilde-pipeline og ratioer |

---

## 10. 🆘 NÅR DU ER USIKKER

1. **Sjekk SSOT først:** `_CONFIG/VALIDATION_RULES.yaml` har svaret
2. **Spør Claude:** "Er dette gyldig i henhold til SRAGI-standarder?"
3. **Test lokalt:** Kjør Loom Validator (når tilgjengelig)
4. **Document rot:** Hvis en regel mangler, foreslå oppdatering til SSOT

---

**© 2025 Rune Solberg / Neptunia Media AS**  
Licensed under CC-BY-4.0

---

> **"Kvalitet bygges inn, ikke inspiseres inn."**  
> — SRAGI TQM-filosofi
