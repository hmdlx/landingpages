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

## Bilder (alle komprimiert und gehostet)

| Stelle | URL (`homedeluxe-bf09.kxcdn.com/…`) | Größe |
|---|---|---|
| Logo | `d165842d053f4fd30f127a7143e5d309.png` | 4 KB |
| Hero SPLASH | `b2e6ddf7050e7ed42414d0c4cad2fefe.jpg` | 74 KB |
| Hero DROP | `c279ef0682a7953651220d6b4217a4f9.jpg` | 85 KB |
| Thermo-Scan-GIF | `0f16e56dacd0c23e662ea34215a4d944.gif` | 2,0 MB |
| CTA-Karte SPLASH THERMO | `1ef0ce689d79c56872e3a48a3efeeacd.jpg` | 13 KB |
| CTA-Karte DROP THERMO | `7ea6654650ea18e26f9daf17e3da2fad.jpg` | 11 KB |
| Footer Instagram / Facebook / YouTube | `2cf8c00d…png` / `2d88e6aa…png` / `a3f8541d…png` | je ~1 KB |
| Footer Trusted Shops | `8b90e531204f06073c688e086883f8d2.png` | 7 KB |
| **Gesamt beim Öffnen** | | **~2,24 MB** (vorher 3,64 MB) |

Die Quelldateien liegen in `assets/`.

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

- Preisstand im Footer („Stand: 22.10.2026“) am Versandtag prüfen.
- Preise, UVP & kostenlosen Versand prüfen (laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop`.
