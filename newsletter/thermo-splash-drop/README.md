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

## Betreff & Preheader

Empfänger: nur Kund:innen, die einen SPLASH oder DROP gekauft haben.

**Empfehlung (im HTML hinterlegt)**
- Betreff: `Dein Whirlpool verliert jede Nacht Wärme` (40 Zeichen)
- Preheader: `Neu für SPLASH & DROP: die Thermoabdeckung für 79 € – solange der Vorrat reicht.` (80 Zeichen)

**A/B-Test-Variante (Neugier, passt zur Hero-Headline)**
- Betreff: `Hast du so einen? 👀`
- Preheader: `Für SPLASH & DROP: Wir haben etwas Neues für deinen Whirlpool.`

**Getrennt nach Segment (falls die Listen getrennt sind)**
- SPLASH: `Neu für deinen SPLASH: Wärme bleibt drin` / `SPLASH THERMO für 79 € statt 129 € – passgenau, solange der Vorrat reicht.`
- DROP: `Neu für deinen DROP: Wärme bleibt drin` / `DROP THERMO für 79 € statt 89 € – passgenau, solange der Vorrat reicht.`

## Vor dem Versand

- `{{UNSUBSCRIBE_URL}}` durch den Abmelde-Platzhalter des Newsletter-Tools ersetzen.
- Preise, UVP & kostenlosen Versand prüfen (Stand 22.10.2026 laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop` mit eigenem `utm_content` je Button bzw. Bild.
