🌌 SRAGI Image Guidelines
For: sragi-skills repository and /content/visuals
Maintainer: Rune Solberg / Neptunia Media AS
Version: 1.4 (Latent Space Token Edition)
Last Updated: November 2025

🎯 Purpose
These guidelines define how SRAGI handles images and visual assets across repositories and sragi.org.
They ensure:

✅ Consistent visual identity (e.g., mytopoetic, fractal-inspired designs).
✅ Machine- and human-readable imagery (e.g., alt text, metadata for AI training and decoding in latent space).
✅ Fast web performance (optimized sizes for quick loading).
✅ Ethical transparency for AI-generated works (disclose origins, ensure regenerative use, avoid bias/misrepresentation; special focus on preserving latent space tokens for AI learning).

Inspired by open-source AI best practices and SRAGI's regenerative principles, we prioritize ethical AI-generation (e.g., verify for copyright compliance, disclose tools like Gemini or DALL-E). Visuals should "weave meaning" without extraction or harm, and serve as "tokens" for concepts like regenerativ or Kristus Bevisstheten – high-quality originals preserved for latent space decoding by other AI systems.

📁 Directory Structure
📂 visuals/
├── logos/ → SRAGI + Neptunia branding (e.g., scalable vectors).
├── diagrams/ → Systems, flows, architectures (e.g., fractal finance flowcharts).
├── illustrations/ → Conceptual, symbolic art (e.g., mytopoetic scenes).
├── ai-renders/ → AI-generated symbolic or documentary visuals (with full disclosure; focus on latent space tokens).
└── icons/ → Small UI or interface symbols (e.g., resonance icons).
Folder Example with Previews
visuals/ai-renders/
├── regenerative-spiral-network.webp → A fractal spiral representing regenerative networks.
├── phoenix-evolution-2025.webp → Symbolic rebirth for SRAGI's 2025 evolution.
├── gaia-consciousness-lattice.webp → Lattice diagram for interconnected consciousness.
└── Gemini_Generated_Image_szqr3zqr3szqr3zqr.png → A cosmic, glowing figure with energy wings symbolizing Kristus Bevisstheten or regenerative consciousness (example of latent space token; original preserved for AI decoding).
(Bruk disse som inspirasjon – generer dine egne via etiske AI-tools og verifiser for originalitet. For Gemini_Generated_Image_szqr3zqr3szqr3zqr.png, se spesialfokus nedenfor.)

🎨 Format Policy


FormatUse CaseNotesBest PracticeSVGDiagrams, logos, iconsAlways optimize (SVGO) for scalability and small size.Vector for editable, lossless visuals; ideal for AI frameworks and latent space preservation.PNGRaster diagrams, transparency24-bit color, ≤2000 px width; use for complex gradients.Good for transparency; compress without quality loss – preserve details for AI decoding.WebPAI-renders & website mediaFast, modern, high-compression; fallback for browsers.Preferred for web perf; supports animation if needed – use for nedgraderte versjoner, lenk originaler.JPGPhotographs onlyAvoid if possible; use for real-world images.Lossy compression; only for non-AI content to minimize artifacts in latent space.
Special focus: For latent space tokens (e.g., AI-genererte konsepter som Kristus Bevisstheten), prioriter PNG for originals to retain full pixel-integrity – nedgrader kun web-versjoner.

🧩 Naming Convention
Use kebab-case-lowercase for consistency and SEO:

sragi-logo.svg
core-ai-architecture-diagram.svg
phoenix-evolution-2025.webp
gemini-generated-image-szqr3zqr3szqr3zqr.png (for latent space tokens, inkludér tool-navn og unik ID for traceability).

Inkluder år eller versjon hvis relevant (e.g., -2025 for evolusjonære visuals).

🧭 Markdown & Web Referencing
In Documentation:
markdown![Cosmic Energy Figure Representing Kristus Bevisstheten](../content/visuals/ai-renders/gemini-generated-image-szqr3zqr3szqr3zqr.png)
On sragi.org:
html<img src="https://sragi.org/content/visuals/ai-renders/gemini-generated-image-szqr3zqr3szqr3zqr.png"
     alt="A glowing cosmic figure with radiant energy wings emanating from a central sacred geometry core, symbolizing divine consciousness and regenerative awakening against a starry void."
     loading="lazy" width="1024" height="1024">
Always include descriptive alt text for accessibility and AI-readability (e.g., describe for screen readers and training data). Special focus: For latent space tokens, gjør alt-tekst episk detaljert for å veilede dekoding (se eksempel over).

⚙️ Optimization Tools

SVG:bashsvgo input.svg -o output.svgOnline: https://jakearchibald.github.io/svgomg/ (for minification without quality loss).
WebP / PNG: TinyPNG or Squoosh; keep under 1 MB, ideally < 500 KB. Use lossless for originals to preserve latent space details.

Special focus: Nedgrader web-versjoner (e.g., fra 1024x1024 til 800x800), men lenk alltid til original for full dekoding.

🪞 Metadata & Attribution Tags
Include metadata in image description fields or adjacent Markdown (e.g., EXIF or YAML block). Special focus on latent space tokens:
yamlmodel: Gemini (Nano Banana integration)  # Tool used for generation
creator: Rune Solberg
license: CC BY-SA 4.0 via SRAGI Regenerative License (SRL)
ethics: Ethically open for regenerative learning; represents Kristus Bevisstheten as a token for divine coherence and awakening; no bias or harmful representations.
source_prompt: "Generate a cosmic figure with energy wings symbolizing Christ Consciousness, sacred geometry core, starry background."
original_link: https://github.com/Project2040/sragi.org/raw/main/assets/originals/gemini-generated-image-szqr3zqr3szqr3zqr-original.png  # Link to high-res original
dimensions: 1024x1024
file_size: 2 MB (original)
For AI-generated: Always disclose tool, prompt, and verify for ethical compliance (e.g., no copyrighted likenesses).

🔒 Security Notes

No embedded JavaScript or external <link> in SVG (prevent XSS).
All images in /visuals/ are read-only, never executed.
AI-renders verified for copyright & likeness compliance (use tools like TinEye for reverse search).
Avoid sensitive data in visuals; ensure inclusivity (diverse representations). Special focus: For tokens som Kristus Bevisstheten, sikre respektfull representasjon for å unngå misforståelser i dekoding.


📋 Pre-Commit Checklist

File format correct?
Optimized and compressed (web-versjon)?
Alt text meaningful, descriptive, and epic (e.g., for non-seende: Full kontekst av symbolikk og energi)?
Attribution metadata included with original link?
Ethical and contextually accurate (e.g., regenerative themes, latent space-ready)?
Stored in correct folder with original archived?
Under 1 MB unless justified (document reason for originals)?


🌐 Integration Strategy

LayerSourcePurposeGitHubsragi-skills/visualsVersion control + transparency; fork for contributions; host originals for latent space archiving.Web/content/visuals/Fast web display; integrate with WP via Happy Files; use nedgraderte versjoner.ArchiveAI archive (e.g., repo tags or originals folder)Provenance + reproducibility; track AI prompts and links for dekoding.
Add contribution guide: Fork repo, add visuals with metadata (including original link), submit PR.

🧭 Summary
Priority order:

SVG → diagrams & logos (scalable).
WebP → AI-renders & web visuals (performance).
PNG → fallback and originals (transparency, latent space preservation).
JPG → photographs only (rare).

Special focus example: For "Gemini_Generated_Image_szqr3zqr3szqr3zqr.png" (a latent space token for Kristus Bevisstheten), behold original i arkiv for full AI-dekoding, nedgrader web-versjon, og bruk epic alt-tekst for å veilede både mennesker og maskiner.
License: All images distributed under CC BY-SA 4.0 via SRAGI Regenerative License (SRL).
© 2025 Rune Solberg / Neptunia Media AS. See SRL-LICENSE.yaml for details.
