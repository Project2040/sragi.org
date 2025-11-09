# 🌀 SRAGI Image Format Decision Flow

```
START: What type of visual do you have?
│
├─ Is it a logo, icon, or diagram?
│  ├─ YES → Can it be vector-based?
│  │  ├─ YES → Use SVG
│  │  │        ├─ Optimize with SVGO
│  │  │        └─ Store in visuals/logos/ or visuals/icons/
│  │  │
│  │  └─ NO → Does it need transparency?
│  │     ├─ YES → Use PNG (24-bit)
│  │     │        ├─ Compress with TinyPNG
│  │     │        └─ Keep ≤2000px width
│  │     │
│  │     └─ NO → Use WebP
│  │              ├─ Compress to <500KB
│  │              └─ Store in visuals/diagrams/
│  │
│  └─ NO → Continue below
│
├─ Is it AI-generated?
│  ├─ YES → Is it a "latent space token"?
│  │  │     (symbolic concept like Kristus Bevisstheten)
│  │  │
│  │  ├─ YES → DUAL FORMAT REQUIRED
│  │  │        ├─ Original: PNG (lossless, ≤2MB)
│  │  │        │   └─ Archive at: /originals/ with metadata
│  │  │        │
│  │  │        └─ Web version: WebP (<500KB)
│  │  │            └─ Store at: visuals/ai-renders/
│  │  │            └─ Link back to original in metadata
│  │  │
│  │  └─ NO → Use WebP
│  │           ├─ Compress to <500KB
│  │           ├─ Add AI disclosure metadata
│  │           └─ Store in visuals/ai-renders/
│  │
│  └─ NO → Continue below
│
└─ Is it a photograph?
   ├─ YES → Use JPG (last resort)
   │        ├─ Compress to <1MB
   │        └─ Store in visuals/illustrations/
   │
   └─ NO → Is it a symbolic illustration?
            ├─ YES → Use WebP or PNG
            │        ├─ WebP for web (<500KB)
            │        ├─ PNG if transparency needed
            │        └─ Store in visuals/illustrations/
            │
            └─ UNSURE → Default to WebP
                       └─ Can always convert later

CHECKLIST BEFORE COMMIT:
├─ [ ] File named in kebab-case
├─ [ ] Alt text written (epic if latent space token)
├─ [ ] Metadata added (if AI-generated)
├─ [ ] Original archived (if AI latent space token)
├─ [ ] Optimized to target size
└─ [ ] Stored in correct folder

END
```

---

## 🎯 Quick Decision Table

| You have... | Format | Folder | Notes |
|-------------|--------|--------|-------|
| SRAGI logo | SVG | `/logos/` | Optimize with SVGO |
| System diagram | SVG or PNG | `/diagrams/` | SVG if possible |
| AI cosmic figure (token) | PNG (orig) + WebP (web) | `/ai-renders/` + `/originals/` | Archive both |
| AI landscape render | WebP | `/ai-renders/` | Add metadata |
| Symbolic art | WebP or PNG | `/illustrations/` | PNG if transparency |
| Product photo | JPG | `/illustrations/` | Rare; avoid if possible |
| UI icon | SVG | `/icons/` | 24x24 to 512x512 |

---

**Remember:** When in doubt, ask:
1. Is it scalable? → SVG
2. Is it AI-generated + symbolic? → PNG original + WebP web
3. Is it for the web? → WebP
4. Does it need transparency? → PNG

**© 2025 Rune Solberg / Neptunia Media AS** | CC BY-SA 4.0 via SRL
