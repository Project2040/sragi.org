# **🗂️ SRAGI.org – Offisiell Filstruktur (v2.0)**

**File: `/docs/sragi_files_overview.md`**  
 **Version: 2.0**  
 **Status: PRODUCTION STANDARD**  
 **Updated: Desember 2025**  
 **Aligned with: SRAGI WEB BIOS v2.2, Neptunia OS Architecture, Loom Engine**

---

## **🧭 Purpose**

**Dette dokumentet beskriver den faktiske fil- og mappearkitekturen for sragi.org i Clean SRAGI v2.2-modellen.**

**Strukturen følger tre prinsipper:**

1. **Root \= Internettstandarder (robots, sitemap, AI-policy)**

2. **WordPress \= Renderer for menneskelige sider (f.eks. /licensing/)**

3. **GitHub \= Masterdatakilden (SSOT)**  
    **→ YAML- og Markdown filer**  
    **→ generert → validert → publisert via Loom Engine**

**Denne fila erstatter gamle hybridstrukturer fra SRAGI v1.**

---

# **1\. 🌐 ROOT-NIVÅ (WEB SERVER)**

**Rooten inneholder kun filer som må ligge på toppnivå for at søkemotorer, crawlere og AI-agenter skal finne dem.**

**`/robots.txt`**  
**`/sitemap.xml`**  
**`/ai-policy.txt`**  
**`/licensing/   ← WP-rendered område`**

### **📄 `robots.txt`**

**Instruksjoner til søkemotorer og AI-crawlere.**  
 **Peker eksplisitt til lisens- og policyfiler.**

### **📄 `sitemap.xml`**

**WordPress-generert sitemap.**  
 **Inneholder sider, poster, taksonomier og lisensområdet.**

### **📄 `ai-policy.txt`**

**Menneskelig \+ enkel maskinlesbar policy om AI-bruk.**

---

# **2\. 🏛️ LICENSE-OMRÅDET (WordPress-rendered)**

**URL: `/licensing/`**

**Dette området er ikke en Git-mappe.**  
 **WordPress viser innhold som genereres fra SSOT-data i Git.**

**`/licensing/`**  
   **`index.html              (WP Page – human explanation)`**  
   **`LICENSE-RSL.xml         (Machine-readable rights discovery)`**  
   **`license.json            (API-friendly JSON meta)`**  
   **`ai-policy.xml           (AI-focused machine-policy)`**

### **Hvordan genereres de?**

1. **SRL-LICENSE.yaml → masterdata**

2. **Loom Engine → genererer XML/JSON**

3. **Publisher Module → laster opp filene via WP REST API**

4. **WordPress → serverer dem under `/licensing/`**

**Dette følger modellen i Neptunia Ecosystem Architecture (lisensstandard og transparens) .**

---

# **3\. 📚 DOCUMENTATION & KNOWLEDGE LAYER (Human-facing Markdown)**

**Dette er hele hjertet av SRAGI.org siden, og det som Studio genererer og Loom validerer.**

**`/docs/`**  
   **`core/`**  
   **`standards/`**  
   **`architecture/`**  
   **`sragi_files_overview.md   ← denne filen`**  
**`/content/`**  
   **`pages/`**  
   **`docs/`**  
   **`visuals/`**

### **/docs/ \= Lesbar dokumentasjon**

**For mennesker, ikke maskiner.**

### **/content/ \= Frontmatter Markdown-filer**

**Dette er filene som Loom Engine bruker som kilden til WordPress-innhold:**

**Eksempel (fra faktisk produksjon):**

**`meta:`**  
  **`type: "documentation"`**  
  **`title: "Min første SRAGI test"`**  
  **`slug: "min-forste-test"`**  
  **`published_at: "2025-12-08"`**  
  **`status: "draft"`**  
**`ia:`**  
  **`pillar: "system-thinking"`**  
**`sync:`**  
  **`auto_publish: false`**

---

# **4\. 🧠 SSOT (Single Source of Truth) – Kun YAML**

**Alle maskiner (WP, Loom, AI, Studio) følger disse filene:**

**`/_CONFIG/`**  
   **`TAXONOMY_GRAPH.yaml`**  
   **`VALIDATION_RULES.yaml`**  
   **`CONTENT-SPEC-SCHEMA.yaml`**  
   **`IA-STRUCTURE.yaml`**  
**`SRL-LICENSE.yaml   ← master for lisensarkitektur; artefaktvilkår bestemmer rettighetene`**

### **Eksempler:**

* **TAXONOMY\_GRAPH.yaml**  
   **→ definerer pilarer, domener, faser osv.**

* **VALIDATION\_RULES.yaml**  
   **→ SEO-lengder, slug-regler, bildekrav, UU-krav.**

* **CONTENT-SPEC-SCHEMA.yaml**  
   **→ definisjon av frontmatter (meta, ia, seo, visual, sync).**

* **SRL-LICENSE.yaml**  
   **→ genererer hele lisensområdet.**

**Dette følger også som del av Neptunia-systemets “SSOT-first”-prinsipp:**  
 **“YAML er hjernen, WordPress er muskelen.”**

---

# **5\. 🔄 LOOM ENGINE – OPERASJONELT LAG**

**Loom Engine sjekker filstrukturen slik:**

### **INPUT**

**`/_1_INBOX/`**

### **WORKBENCH**

**`/_2_WORKBENCH/`**

### **LAUNCHPAD (klar for publisering)**

**`/_3_LAUNCHPAD/`**

### **ARCHIVE**

**`/_ARCHIVE/posts/`**

**Dette samsvarer med Sync Loop v1.0-arkitekturen du allerede har tegnet opp.**

---

# **6\. 🧩 KOBLINGER**

### **robots.txt →**

**`# Rights discovery: https://sragi.org/content/license/LICENSE-RSL.xml`**  
**`# AI policy: https://sragi.org/content/license/ai-policy.xml`**  
**`Sitemap: https://sragi.org/sitemap.xml`**

### **WordPress →**

* **renderer sider**

* **serverer lisensfiler**

* **genererer sitemap**

* **mottar frontmatter fra Loom Engine**

### **Loom →**

* **parser frontmatter**

* **validerer mot `_CONFIG/*`**

* **genererer SEO / TSF-data**

* **laster opp lisensfiler, sider, media via REST API**

---

# **7\. 🧱 FULLT DIREKTORI-KART (v2.2)**

**`ROOT/`**  
**`├── robots.txt`**  
**`├── sitemap.xml`**  
**`├── ai-policy.txt`**  
**`├── license/`**  
**`│   ├── LICENSE-RSL.xml`**  
**`│   ├── license.json`**  
**`│   ├── ai-policy.xml`**  
**`│   └── index.html`**  
**`│`**  
**`├── SRL-LICENSE.yaml`**  
**`├── _CONFIG/`**  
**`│   ├── TAXONOMY_GRAPH.yaml`**  
**`│   ├── CONTENT-SPEC-SCHEMA.yaml`**  
**`│   ├── VALIDATION_RULES.yaml`**  
**`│   ├── IA-STRUCTURE.yaml`**  
**`│   └── ENVIRONMENT-CONFIG.yaml`**  
**`│`**  
**`├── content/`**  
**`│   ├── pages/`**  
**`│   ├── docs/`**  
**`│   ├── visuals/`**  
**`│   └── tokens/`**  
**`│`**  
**`├── docs/`**  
**`│   ├── core/`**  
**`│   ├── standards/`**  
**`│   ├── architecture/`**  
**`│   └── sragi_files_overview.md`**  
**`│`**  
**`└── loom/`**  
    **`├── loom.py`**  
    **`├── modules/`**  
    **`├── logs/`**  
    **`└── _content_repos/`**

---

# **8\. ✔️ Oppsummering**

**Din nye filstruktur er:**

* **helt konsistent med Clean SRAGI Architecture**

* **i sync med Neptunia Ecosystem-dokumentet (kapittel om SSOT, WordPress, YAML)**

* **perfekt justert med frontmatter og Studio**

* **kompatibel med Loom Engine, TSF-protokollen og SEO-systemet**

* **fremtidssikker og migrerbar**

---

**© 2025 Rune Solberg / Neptunia Media AS**  
**Licensed under CC-BY-4.0.**
