# 🎨 SRAGI Image Quick Reference

**Version 1.4** | For sragi-skills & sragi.org

---

## 📂 Where to Put Images

```
visuals/
├── logos/          → Branding (SVG preferred)
├── diagrams/       → Flowcharts, architectures (SVG/PNG)
├── illustrations/  → Symbolic art (WebP/PNG)
├── ai-renders/     → AI-generated visuals (WebP + PNG original)
└── icons/          → UI elements (SVG)
```

---

## 🎯 Format Cheat Sheet

| Need | Use | Size | Optimize with |
|------|-----|------|---------------|
| Logo/Icon | SVG | N/A | SVGO |
| Diagram with transparency | PNG | ≤2000px | TinyPNG |
| Web visual (AI-render) | WebP | <500KB | Squoosh |
| Latent space token (original) | PNG | <2MB | Lossless |
| Photo (rare) | JPG | <1MB | Squoosh |

---

## ✍️ Naming

```bash
# Good
sragi-logo.svg
core-ai-architecture-diagram.svg
phoenix-evolution-2025.webp

# AI-generated (include tool + ID)
gemini-generated-image-szqr3zqr3szqr3zqr.png
```

---

## 📝 Alt Text Examples

**Basic:**
```
alt="SRAGI logo with fractal spiral design"
```

**Latent space token (epic detail):**
```
alt="A glowing cosmic figure with radiant energy wings emanating from a central sacred geometry core, symbolizing divine consciousness and regenerative awakening against a starry void"
```

---

## 🏷️ Required Metadata (AI-generated only)

```yaml
model: Gemini / DALL-E / Midjourney
creator: Rune Solberg
license: CC BY-SA 4.0 via SRL
source_prompt: "Your exact prompt here"
original_link: https://github.com/.../original.png
```

---

## ✅ Before Commit

- [ ] Right format?
- [ ] Optimized?
- [ ] Epic alt text?
- [ ] Metadata included?
- [ ] Original archived (if AI)?
- [ ] Under 1MB (web version)?

---

**© 2025 Rune Solberg / Neptunia Media AS** | CC BY-SA 4.0 via SRL
