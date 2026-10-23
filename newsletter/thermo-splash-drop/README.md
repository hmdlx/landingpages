# Newsletter: SPLASH THERMO & DROP THERMO

Kompakter, mobile-first E-Mail-Newsletter für alle Kund:innen mit Outdoor-Whirlpool **SPLASH** oder **DROP**.
Datei: `newsletter.html` (E-Mail-taugliches Tabellen-HTML, Inline-Styles, max. 600 px breit, weißer Hintergrund, homedeluxe.de-CI).

## Aufbau (4 Schritte, wenig Text, alles führt zum CTA)

| # | Block | Inhalt |
|---|---|---|
| 1 | Hast du so einen? | Headline + Ambiente SPLASH & DROP (verlinkt) + „Dann haben wir etwas Neues für dich.“ |
| 2 | Problem | „Jede Nacht entweicht deine Wärme.“ + Nacht-Protokoll (Wärmebalken) + 1 Zeile Folgen |
| 3 | Lösung | NEU · „Deckel drauf. Wärme drin.“ + Thermo-Scan-GIF + 3 Kurz-Nutzen |
| 4 | CTA | „Jetzt passende Abdeckung sichern.“ + 2 Produktkarten (Bild, Maß, Preis, Button) + Versand / Vorrat |

## Bilder (alle gehostet, nichts hochzuladen)

| Stelle | Quelle |
|---|---|
| Logo | `homedeluxe-bf09.kxcdn.com/89c7c3da91206c657d21a846a65f3a97.png` |
| Hero SPLASH | Shop-CDN: `32309-…-Splash-Grau-Ambiente-Model02.jpg` |
| Hero DROP | Shop-CDN: `48119-…-Drop-Ambiente-Model01.jpg` |
| Thermo-Scan | aktuell `homedeluxe-bf09.kxcdn.com/66eaa461a7f4b64cee4e98b330e1eb2a.gif` (540 px, 26 s, 16,6 MB) – komprimierte Fassung `assets/thermo-scan-8mb.gif` (8,7 MB, gleiche 260 Frames/Timing, gifsicle `--lossy=60`) hochladen und URL tauschen |
| CTA-Karten | `homedeluxe-bf09.kxcdn.com/f410213b37e003a7161e55e1789cab54.jpg` (SPLASH), `…/8e40be39af22e4c35d7cfe1572a5b44a.jpg` (DROP) |

## Betreff & Preheader (persönlicher Ton, wie eine direkte Nachricht)

Empfänger: nur Kund:innen, die einen SPLASH oder DROP gekauft haben. Regeln für den persönlichen Eindruck: keine Großbuchstaben-Produktnamen im Betreff, kein Preis, kein Emoji, kein „NEU“, Anrede wie in einer 1:1-Mail. Kein „Re:“/„AW:“ – das täuscht eine Antwort vor (Spamfilter + Vertrauensverlust).

**Final (im HTML hinterlegt)**
- Absendername: `[Vorname] von Home Deluxe`
- Betreff: `Dein Whirlpool wird schnell kalt?` (33 Zeichen)
- Preheader: `Wir haben jetzt die Lösung – passgenau für deinen SPLASH oder DROP.` (67 Zeichen)
- Langform als ein Betreff (wird mobil nach ca. 40 Zeichen gekürzt): `Whirlpool wird schnell kalt? Wir haben jetzt die Lösung!`

**Vorherige Empfehlung**
- `Kurze Frage zu deinem Whirlpool` / `Du hast bei uns einen SPLASH oder DROP gekauft – dafür haben wir jetzt etwas Neues.`

**Mit Vornamen (wenn das Tool Personalisierung kann, Platzhalter an das Tool anpassen)**
- Betreff: `{{Vorname}}, kurze Frage zu deinem Whirlpool`
- Preheader: `Hallo {{Vorname}}, du hast bei uns einen SPLASH oder DROP gekauft – dafür gibt es jetzt etwas Neues.`
- Fallback ohne Vornamen: Variante oben.

**Alternativen im gleichen Ton**
- `Wir haben an deinen Whirlpool gedacht` / `Gerade jetzt im Herbst wird das für dich wichtig – schau mal kurz rein.`
- Getrennte Listen: `Das habe ich für deinen SPLASH` bzw. `… DROP` / `Passt genau auf deinen Whirlpool und hält die Wärme drin. Schau mal rein.`

## JUNE-Kompatibilität

Das HTML ist wie ein JUNE-Export aufgebaut (Vorlage: KW43-Export), weil der Import sonst mit „Validation Error – Cannot read properties of undefined (reading 'replace')“ abbrach:
- `<head>` 1:1 aus dem JUNE-Export (JUNE-Kommentar, Meta, Style-Blöcke), nur Titel getauscht und Poppins per `@import` ergänzt; kein eigenes `<link>`/`<style>` mehr.
- `<body>`-Attribute, Wrapper `<div class="a">` und Preheader im JUNE-Format.
- Jeder Bild- und Button-Link trägt `data-trigger-action-id="#{image.actionTriggerId}"` bzw. `#{button.actionTriggerId}` (Klick-Tracking).
- Links mit rohem `&` statt `&amp;` (wie im Export).
- Eigene Texte als `<div>` statt `<p>/<h1>/<h2>`, weil das JUNE-CSS `p` mobil auf 12 px Verdana zwingt.

## Footer

Standard-Footer aus JUNE (wie KW43): Social-Icons, USP-Leiste („Direkt vom Hersteller ✓ · Riesige Auswahl ✓ · Kostenloser Versand* ✓“), Absender-Hinweis, Versand-Fußnote mit Preisstand 22.10.2026, Rechtslinks, Newsletter-Abmeldung, Trusted Shops. UTM-Kampagne auf `thermo-splash-drop` umgestellt, USP-Spalten auf 3 × 200 px (passt in 600 px). Darüber eine Zeile zur UVP-Erklärung.

## Vor dem Versand

- `assets/thermo-scan-8mb.gif` hochladen und die URL `66eaa461…gif` im HTML durch die neue ersetzen.
- Preisstand im Footer („Stand: 22.10.2026“) am Versandtag prüfen.
- Preise, UVP & kostenlosen Versand prüfen (laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop`.
