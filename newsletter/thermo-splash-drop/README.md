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

| Stelle | Datei | Hosting |
|---|---|---|
| Logo (Kopf) | Home-Deluxe-Logo | bereits gehostet (`homedeluxe-bf09.kxcdn.com/89c7c3da…png`) |
| 02 · Lösung, Key Visual | `assets/thermo-keyvisual-waerme-bleibt-drin.jpg` | **hochladen** |
| 02 · Lösung, Thermo-Scan | `assets/thermo-scan.gif` (600 px, 0,9 MB, aus dem Video `HomeDeluxe_SPLASH-THERMO_Thermo-Scan_1x1`) | **hochladen** |
| Produktkarte SPLASH | `assets/thermo-splash-masse.jpg` | **hochladen** |
| Produktkarte DROP | `assets/thermo-drop-masse.jpg` (Gegenstück zum SPLASH-Creative, gleiche Gestaltung) | **hochladen** |
| 03 · CTA, Bild-Links | SPLASH-/DROP-Karte aus KW43 | bereits gehostet (`f410213b…jpg`, `8e40be39…jpg`) |

Das Thermo-Scan-GIF ist ein Storyboard aus dem Video: Wärmebild → „Ohne Abdeckung · Wärme entweicht“ → „Mit SPLASH THERMO · Wärme bleibt“ → Maße → Laub & Schmutz → klares Wasser → Endcard. Outlook zeigt nur das erste Bild (Wärmebild).

## Vor dem Versand

- Die vier mit **hochladen** markierten Dateien im Newsletter-Tool hochladen und die relativen `src="assets/…"` durch die gehosteten URLs ersetzen.
- `{{UNSUBSCRIBE_URL}}` durch den Abmelde-Platzhalter des Newsletter-Tools ersetzen.
- Preise, UVP & kostenlosen Versand prüfen (Stand 22.10.2026 laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop` mit eigenem `utm_content` je Button bzw. Bild.
