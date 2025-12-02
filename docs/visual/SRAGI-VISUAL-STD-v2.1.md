🌌 SRAGI Visual Standards v2.1
Fil: /docs/visuals/visual.md Status: SSOT (Single Source of Truth) Vedlikeholder: Rune Solberg / Neptunia Media AS Sist oppdatert: Desember 2025 Lisens: CC BY-SA 4.0 via SRL v1.12

🧭 Formål
Dette dokumentet definerer den absolutte standarden for alle visuelle eiendeler i SRAGI-økosystemet. Det forener kreativ komposisjon (ratio) med teknisk leveranse (filformater og mappestruktur).

Målet er en regenerativ visuell flyt: Bevaring av originalkvalitet (Master) kombinert med lynrask, båndbredde-besparende levering på web (AVIF).

📐 Del 1: De 6 Hellige Ratioer
Vi forholder oss til nøyaktig seks formater for å sikre visuell harmoni på tvers av alle flater.

Format	Ratio	Rolle	Master Oppløsning (Min)	Bruk
Primary	3:2	Featured Standard	2400 x 1600	Artikkelbilder, presentasjoner, "fotografisk" balanse.
Widescreen	16:9	Hero & Video	3840 x 2160 (4K)	Toppseksjoner (Hero), YouTube, filmatiske scener.
Square	1:1	Token & Symbol	2048 x 2048	Latent Space Tokens, avatarer, rutenett.
Portrait	4:5	Social Feed	1600 x 2000	Instagram/LinkedIn feed (gir 35% mer plass enn 1:1).
Story	9:16	Vertical Full	1080 x 1920	Reels, TikTok, Stories. Mobil-først opplevelser.
Classic	4:3	Diagram	1600 x 1200	Tekniske diagrammer, dokumenter.
💾 Del 2: Filstrategi (Master vs. Web)
Vi skiller strengt mellom Kilden (Master) og Leveransen (Web).

1. MASTER (Kilden / Kairos)
Format: .png (Lossless) eller høy-kvalitet .jpg.

Navn: [tool]-[navn]-[år]-[ratio].png

Lagring:

Lokalt: E:\1-Neptunia-Media-Visuals\

GitHub: /assets/originals/

Regel: Slettes aldri. Komprimeres aldri.

2. WEB (Leveransen / Chronos)
Format: .avif (Primær), .webp (Fallback), .jpg (Kun Social).

Navn: [tool]-[navn]-[år]-[ratio]-[suffiks].avif

Lagring: WordPress Media Library (HappyFiles).

Regel: Genereres automatisk av SRAGI-IMAGE-PIPELINE.bat.

🏭 Del 3: Produksjonslinjen (The Factory)
Når en Master-fil kjøres gjennom scriptet, genereres følgende sett automatisk. Dette sikrer at nettsiden alltid er lynrask.

Suffiks	Bredde	Format	HappyFiles Mappe	Bruksområde i Bricks
-large	1920 px	AVIF + WEBP	/visuals/hero/	Bakgrunner, Hero-seksjoner, fullbredde.
-medium	1200 px	AVIF + WEBP	/visuals/content/	Featured Image, bilder inne i artikler.
-small	600 px	AVIF + WEBP	/visuals/tokens/	Grid-visninger, gallerier, ikoner, kort.
-social	1080 px	JPG	/visuals/social/	Deling på LinkedIn/Facebook (teknisk sikring).
> Merk: Høyden beregnes automatisk basert på Master-filens ratio. En 3:2 Master blir f.eks. 1200x800 som Medium fil.

📂 Del 4: HappyFiles Struktur
I WordPress (One.com) skal mappestrukturen speile produksjonslinjen nøyaktig. Vi sorterer etter størrelse/funksjon, ikke innhold.

Plaintext
/visuals/
├── hero/           (Her bor alle *-large filer)
├── content/        (Her bor alle *-medium filer)
├── tokens/         (Her bor alle *-small filer)
└── social/         (Her bor alle *-social filer)
Sjekkliste for opplasting:

Dra Master-filen (f.eks. ...-3x2.png) inn i SRAGI-IMAGE-PIPELINE.bat.

Gå til WordPress Media Library.

Åpne mappen Hero -> Last opp *-large.avif OG *-large.webp.

Åpne mappen Content -> Last opp *-medium.avif OG *-medium.webp.

Åpne mappen Tokens -> Last opp *-small.avif OG *-small.webp.

(Valgfritt) Mappen Social -> Last opp *-social.jpg.

🏷️ Navngivning & Eksempler
Master Fil (Input)
gemini-regenerativ-spiral-2025-3x2.png

Genererte Web Filer (Output)
Hero: gemini-regenerativ-spiral-2025-3x2-large.avif (1920px bred)

Content: gemini-regenerativ-spiral-2025-3x2-medium.avif (1200px bred)

Token: gemini-regenerativ-spiral-2025-3x2-small.avif (600px bred)

Social: gemini-regenerativ-spiral-2025-3x2-social.jpg (1080px bred)

🔧 AI Prompting Guide (For Ratios)
For å treffe ratioene perfekt i genereringen:

3:2 -> --ar 3:2 (Midjourney) eller "Aspect ratio 3:2" (DALL-E/Gemini)

16:9 -> --ar 16:9

4:5 -> --ar 4:5 (Vertical Social)

© 2025 Rune Solberg / Neptunia Media AS Licensed under CC BY 4.0 via SRAGI Regenerative License (SRL).
