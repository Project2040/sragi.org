# SRLF 2.0.1 – kvalitetssikring før publisering

Kontrolldato: 21. september 2026. Utgangspunkt: `main` på `afbdc04b68566b43e46d269d3c70553b2b662d0c`, etter merge av PR #10 og #9. Rettelser og dokumentasjon ligger i oppfølgingsbranchen `qa/srlf-2.0.1-prepublication`.

**Vurdering: Kildegrunnlaget er kontrollert og tekniske feil er rettet i oppfølgingsbranchen. Nettstedet er ikke klart til å presentere SRLF 2.0.1 som publisert.** De nye rutene, filene, HTTP-oppsettet og cacheoppdateringen må inngå i en samlet publiseringsjobb. Ingen nettstedspublisering, cachetømming, e-postutsending eller endring av eksisterende rettighetsvalg er utført i denne kontrollen.

## Omfang og bevis

Kontrollen omfatter lisensmasteren, generatoren, standardtekstene, kommersiell LicenseRef, instruksmetadata, innholdsmaler, RSL-projeksjonen, robots/AI-policy, konfigurasjonspekeren, publiseringsveiledningen, rettighetsregisteret og offentlige HTTP-endepunkter. Den omfatter ikke enhver side, produktpakke eller serverinnstilling i hele SRAGI-økosystemet.

- 33 tester passerer i oppfølgingsbranchen.
- Alle 11 genererte filer passerer `build_licenses.py --check`.
- De fem standardlisensene samsvarer med de låste SHA-256-verdiene.
- SSOT-kontrollen passerer; ingen endringer i eksisterende lisensvalg er gjort.
- YAML-filer i publiseringsoppsettet er syntakskontrollert. To eldre syntaksfeil er rettet uten endring av verdiene.
- Den automatiserte HTTP-kontrollen kl. 04:44 UTC kontrollerte 15 endepunkter: 15 avvik mot den nye utgaven, ingen uavklarte nettverksfeil i denne kjøringen. Dette er status før utrulling, ikke 15 uavhengige generatorfeil.
- Full HTTP-evidens med faktiske/forventede hasher, status og utvalgte offentlige headere: [SRLF-2.0.1-LIVE-CHECK.json](SRLF-2.0.1-LIVE-CHECK.json).

## Dokumenterte feil som er rettet

| Funn | Reproduksjon og betydning | Rettelse |
| --- | --- | --- |
| Kommersiell publisering uten rettighetsbekreftelse | Produktmalen godtok `--for-publication` med kommersiell dual-lisens uten noen kommersiell rettighetsbekreftelse eller evidensreferanse. | Publiseringsmodus krever nå `commercial_relicensing_verified: true` og en ikke-tom `commercial_relicensing_evidence`. Referansen bevares i metadata. Åpen lisens alene og utkast krever ikke dette. |
| Manglende generert LicenseRef stoppet gjenoppbygging | Sletting av den genererte referansen førte til feil før generatoren fikk gjenskape den. | Vanlig bygg gjenskaper referansen fra kildene. `--check` feiler fortsatt ved manglende eller endret output. Standardtekstene kontrolleres fortsatt mot sine hasher. |
| Konfigurasjonspeker viste 2.0 | `docs/_CONFIG/SRL-LICENSE.yaml` hadde en egen gammel versjonsverdi. | Pekeren genereres nå fra masteren og omfattes av kontrollen av genererte filer. |
| Utdatert publiseringsveiledning | Veiledningen ba om navngitte robots-grupper. Migrasjonsnotatet beskrev fortsatt en draft-PR og kalte CLA-filen en contributor-notis. | Veiledningen beskriver én wildcard-gruppe, korrekt merge-status og skillet mellom faktisk CLA og contributor-notis. |
| To ugyldige YAML-filer | `actor_role:{...}` manglet mellomrom i `VALIDATION-RULES.yaml`. En uanført Markdown-linje i `TAXONOMY_GRAPH.yaml` ble tolket som en ugyldig YAML-alias. | Rettet syntaksen; ingen lisens-, taksonomi- eller valideringsverdier er endret. Regresjonstest leser konfigurasjonene. |

Evidensfeltet dokumenterer en menneskelig vurdering; en boolsk verdi eller en tekststreng beviser ikke at rettighetene faktisk finnes. Referansen må peke til en reell rettighetsvurdering, overdragelse eller akseptert avtale. Private avtaler og personopplysninger skal ikke kopieres inn i offentlig metadata. WordPress/Loom må bruke samme kontroll; repoet inneholder ikke bevis for at den live integrasjonen allerede gjør dette.

## Live-avvik som må håndteres ved publisering

| Område | Observert tilstand | Konkret publiseringskrav |
| --- | --- | --- |
| `/licensing/` | HTTP 404 etter redirect til www | Opprett/koble WordPress-ruten til den gjeldende lisensoversikten. |
| `/commercial-licensing/` | HTTP 404 etter redirect til www | Opprett kommersiell informasjon med riktig navn, scope, avtalegrunnlag og kontakt. |
| `/content/license/WEBSITE-LICENSE.html` | HTTP 404 | Legg ut den genererte policyen før RSL skal peke på den. |
| RSL-fil og gammel rotalias | Begge leverer gammelt innhold med versjon 1.12 og `application/xml` | Lever den gjennomgåtte RSL 1.0-filen med `application/rsl+xml`. Redirect gammel alias eller lever identiske oppdaterte bytes. |
| AI-policy, robots, JSON, oversikt og sitemap | Eldre innhold, hovedsakelig datert november 2025 | Oppdater filene samlet. Robots må beholde én wildcard-gruppe. Integrer lisens-URL-ene uten å miste resten av nettstedets CMS-sitemap. |
| Norsk prinsippfil | HTTP 404 | Publiser den eksakte filen manifestet viser til. |
| Engelsk prinsippfil | HTTP 200, men annen SHA-256 enn manifestet | Publiser den gjennomgåtte kildefilen med sin eksisterende lisensnotis. |
| HTTP-headere | `X-License: CC-BY-4.0`, `X-License-URL` og `X-AI-Policy` peker til gammelt oppsett | Finn opphavet i server/CDN/CMS. Fjern eller avgrens generelle rettighetspåstander og oppdater oppdagelseslenkene. Kontroller særskilt produkt-/tredjepartsunntak. |
| Cache | TXT/Markdown-responser viser opptil `max-age=2592000` (30 dager) | Tøm berørte origin-/CDN-cacher ved cutover og kontroller faktiske offentlige responser etterpå. |

Den gamle robots-teksten har også en generell formulering om CC BY med regenerative tillegg. Den er ikke konsistent med det nye skillet mellom avgrenset nettstedspolicy, egne produktvilkår og en uforpliktende regenerativ invitasjon. Cache-brytende kontroll med `Cache-Control: no-cache` og en egen query viste fortsatt gammelt robots-/RSL-innhold og 404 for den nye policyen. Dette er ikke grunnlag for å anta at bare en lokal nettlesercache er problemet.

HTTP-probene dokumenterer offentlig respons. De identifiserer ikke sikkert hvilket lag som eier konfigurasjonen. Ingen endringer i server/CDN er gjort.

## Innhold og rettighetsgrenser

| Kontrollpunkt | Vurdering |
| --- | --- |
| Nettsted kontra produkter | Masteren avgrenser CC BY-standard til offentlig innhold Neptunia eier eller kan lisensiere, med egne artifact-vilkår og tredjepartsrettigheter bevart. Ingen lisens for hele repoet utledes. |
| ShareAlike og kommersiell vei | Tekstene avgrenser unntaket til kvalifiserte CC BY-SA-artefakter og avtalt scope. Privat tilpasning alene og kommersiell aktivitet alene fremstilles ikke som kjøpsplikt. Dette følger skillet i [CC BY-SA 4.0 §§2–3](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en#s3b). |
| Avtale, navn og kontakt | Oversikt, kommersiell portal, LicenseRef og de tre kontaktrollene hentes fra masteren. Metadata utgjør ikke en signert kommersiell avtale. |
| Tredjeparts- og bidragsrettigheter | Kommersiell relisensiering krever tilstrekkelige rettigheter. DCO alene presenteres ikke som en relisensieringsrett. Historiske åpne grants er bevart. |
| Varemerke, sertifisering og partnerstatus | Skilt fra copyright-lisens og følger ikke automatisk. |
| AI-tilgang | Teknisk tilgang er åpen; bruksrett følger gjeldende lisens. Tekstene avgjør ikke generelt om trening eller modellutdata utgjør en bearbeidelse. |
| RSL | Den avgrensede projeksjonen er kontrollert mot [RSL 1.0](https://rslstandard.org/rsl): navnerom, kjerneform, scoper, attribution og global robots-discovery. Prosjektets tester er ikke offisiell sertifisering. Offisiell URL-validering og offentlig MIME-kontroll gjenstår etter utrulling. |

To eksisterende dokumenter har fortsatt motstridende CC BY/CC BY-SA-notiser: `docs/core/ETHICAL-CONTACT-PROTOCOL.md` og `docs/standards/VISUAL-PROTOCOL.md`. De står korrekt registrert som `needs_rights_review`. Rettighetshaver må avklare dem før de tas med som avklarte ressurser i en ny publisering; de kan også holdes utenfor denne avgrensede utrullingen. Generatoren skal ikke velge mellom historiske grants.

PHP-utdraget i `BUNNY-CDN-INTEGRATION.md` og dokumentet rundt har separate lisensnotiser. Dette er registrerte scopes, ikke automatisk en konflikt eller en OR-lisens.

CLA v2.1 står som REVIEW. Før avtalen brukes til å innhente bidrag, må Neptunia ferdigstille avtalen og en konkret mekanisme som registrerer aksept av riktig versjon og eventuell arbeidsgiverfullmakt. Dette er et eget driftskrav for bidragsflyten; det er ikke bevis på at eksisterende førsteparts nettsidetekst mangler rettigheter.

## Avgrensninger og åpne kontrollpunkter

- De nyeste BIOS/Core Fullstack-produktfilene er ikke i dette publiseringsgrunnlaget. Det offentlige `sragi-skills`-repoet som ble kontrollert, har BIOS 2.22 og Core AI-OS 1.0 fra oktober 2025. Deres eksisterende åpne lisensnotiser skal ikke omskrives som følge av denne kontrollen. De faktiske filene som skal distribueres i den nye produktutgaven må kontrolleres mot metadataformatet før produktpublisering.
- E-postadressene er konsistente i konfigurasjon og output. Opprettelse og mottak i postkassene er ikke verifisert; ingen testmeldinger er sendt.
- GitHub-repoets beskrivelse avsluttes fortsatt med en bred formulering om RSL og CC BY. Anbefalt tekst: «Official SRAGI® website, open knowledge, regenerative AI frameworks and artifact-level licensing infrastructure under SRLF 2.0.» Det er en metadataforbedring i GitHub-innstillingene, ikke en grunn til å endre artifact-lisenser.
- Visuell og funksjonell kontroll av de to nye WordPress-sidene gjenstår fordi de offentlig tilgjengelige rutene gir 404. HTML-tabeller, escaping og lenker i de genererte oversiktene er kontrollert i tester.

## Anbefalt rekkefølge

1. Gjennomgå og merge de dokumenterte tekniske rettelsene i oppfølgings-PR-en.
2. Klargjør de nye WordPress-rutene, statiske filene, kildefilene, aliasene og headerreglene i staging. Avgrens publiseringspakken fra uavklarte historiske dokumenter og produkter som ikke er kontrollert.
3. Kontroller sidetekster, knapper, kontakter, produktunntak og faktisk CMS-validering i staging. Behold en gjenopprettbar kopi av dagens filer og oppsett.
4. Gjennomfør én koordinert, godkjent utrulling og tøm berørte cacher.
5. Kjør `python tools/check_licensing_deployment.py --output /tmp/sragi-http-check.json`, kontroller det tilsiktede sitemap-oppsettet, og bruk den offisielle RSL-validatoren på den publiserte URL-en. Kontroller også produktnotiser og reell mottaksevne i kontaktkanalene.

**Godkjenningsgrunnlaget for publisering er dermed konkret: sammenhengende kilder og output, fungerende ruter, riktige offentlige responser, avklarte rettigheter for det som faktisk tas med, og gjennomgått WordPress-visning.**
