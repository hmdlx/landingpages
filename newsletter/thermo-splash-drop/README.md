# Newsletter: SPLASH THERMO & DROP THERMO

Mobile-first E-Mail-Newsletter für alle Kund:innen mit Outdoor-Whirlpool **SPLASH** oder **DROP**.
Datei: `newsletter.html` (E-Mail-taugliches Tabellen-HTML, Inline-Styles, max. 600 px breit).

## Roter Faden

| Abschnitt | Inhalt | Visuelles Motiv |
|---|---|---|
| Hero | Hook „Du heizt gerade für den Himmel.“ + Selbst-Segmentierung (SPLASH / DROP) | Nacht-Protokoll: Wärmebalken schrumpft von 20:00 bis 07:00 Uhr |
| 01 · Das Problem | Wärmeverlust über die offene Wasseroberfläche, 4 Pain Points, „Warum gerade jetzt?“ | Schema: Pfeile nach oben ↑ |
| 02 · Die Lösung | SPLASH THERMO / DROP THERMO, dieselben 4 Punkte gespiegelt als Lösung, Produktwahl | Schema mit THERMO-Luftpolster, Pfeile nach unten ↓ |
| 03 · FOMO-CTA | Callback „Hör auf, für den Himmel zu heizen.“, Saison + Vorrat, 2 CTAs, P.S. mit Preisanker | Nacht-Protokoll: Wärmebalken bleibt voll |

Gestaltung strikt nach homedeluxe.de-CI: weißer Hintergrund, nur Navy `#0e2234`, Weiß und Grautöne, Poppins, eckige Kanten. Überschriften im Shop-Stil (fett + normal), Produktkarten und „Deluxe-Faktoren“-Kacheln wie auf der Produktseite. Wärme = volle Navy-Balken, Abkühlung = Grau.

## Betreffzeilen (Vorschläge)

1. Du heizt gerade für den Himmel.
2. SPLASH oder DROP? Hier verschwindet deine Wärme.
3. Neu: Die Abdeckung, die deinen Whirlpool warm hält

Preheader (im HTML hinterlegt): „SPLASH oder DROP im Garten? Dann verlierst du gerade jede Nacht Wärme – so stoppst du das.“

## Creatives

| Stelle | Creative | Hosting |
|---|---|---|
| Logo (Kopf) | Home-Deluxe-Logo | gehostet: `homedeluxe-bf09.kxcdn.com/89c7c3da91206c657d21a846a65f3a97.png` |
| 02 · Lösung, Key Visual | `assets/thermo-keyvisual-waerme-bleibt-drin.jpg` | **noch hochladen** |
| 02 · Lösung, Thermo-Scan | Thermo-Scan-Film SPLASH THERMO (GIF, 11 s) | gehostet: `homedeluxe-bf09.kxcdn.com/3d2f402191c8d809c078b9851b80ba9e.gif` |
| 02 · „Welcher Whirlpool steht bei dir?“ | Maß-Animation SPLASH ⇄ DROP (GIF, 13 s) | gehostet: `homedeluxe-bf09.kxcdn.com/3d52bc307d7eb3344a07944ad26fd74f.gif` |
| 03 · CTA, Bild-Links | SPLASH-/DROP-Karte | gehostet: `f410213b37e003a7161e55e1789cab54.jpg`, `8e40be39af22e4c35d7cfe1572a5b44a.jpg` |

## Vor dem Versand

- Das Key Visual `assets/thermo-keyvisual-waerme-bleibt-drin.jpg` hochladen und den relativen `src` durch die gehostete URL ersetzen.
- `{{UNSUBSCRIBE_URL}}` durch den Abmelde-Platzhalter des Newsletter-Tools ersetzen.
- Preise, UVP & kostenlosen Versand prüfen (Stand 22.10.2026 laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop` mit eigenem `utm_content` je Button bzw. Bild.
