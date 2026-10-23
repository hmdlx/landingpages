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
| Thermo-Scan | `homedeluxe-bf09.kxcdn.com/3d2f402191c8d809c078b9851b80ba9e.gif` |
| CTA-Karten | `homedeluxe-bf09.kxcdn.com/f410213b37e003a7161e55e1789cab54.jpg` (SPLASH), `…/8e40be39af22e4c35d7cfe1572a5b44a.jpg` (DROP) |

## Betreff & Preheader (persönlicher Ton, wie eine direkte Nachricht)

Empfänger: nur Kund:innen, die einen SPLASH oder DROP gekauft haben. Regeln für den persönlichen Eindruck: keine Großbuchstaben-Produktnamen im Betreff, kein Preis, kein Emoji, kein „NEU“, Anrede wie in einer 1:1-Mail. Kein „Re:“/„AW:“ – das täuscht eine Antwort vor (Spamfilter + Vertrauensverlust).

**Empfehlung (im HTML hinterlegt)**
- Absendername: `[Vorname] von Home Deluxe` (z. B. Ansprechpartner aus dem Kundenservice)
- Betreff: `Kurze Frage zu deinem Whirlpool` (31 Zeichen) – passt zur Hero-Frage „Hast du so einen?“
- Preheader: `Du hast bei uns einen SPLASH oder DROP gekauft – dafür haben wir jetzt etwas Neues.` (83 Zeichen)

**Mit Vornamen (wenn das Tool Personalisierung kann, Platzhalter an das Tool anpassen)**
- Betreff: `{{Vorname}}, kurze Frage zu deinem Whirlpool`
- Preheader: `Hallo {{Vorname}}, du hast bei uns einen SPLASH oder DROP gekauft – dafür gibt es jetzt etwas Neues.`
- Fallback ohne Vornamen: Variante oben.

**Alternativen im gleichen Ton**
- `Wir haben an deinen Whirlpool gedacht` / `Gerade jetzt im Herbst wird das für dich wichtig – schau mal kurz rein.`
- Getrennte Listen: `Das habe ich für deinen SPLASH` bzw. `… DROP` / `Passt genau auf deinen Whirlpool und hält die Wärme drin. Schau mal rein.`

## Vor dem Versand

- `{{UNSUBSCRIBE_URL}}` durch den Abmelde-Platzhalter des Newsletter-Tools ersetzen.
- Preise, UVP & kostenlosen Versand prüfen (Stand 22.10.2026 laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop` mit eigenem `utm_content` je Button bzw. Bild.
