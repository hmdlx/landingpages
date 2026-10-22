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

Farben nur aus der CI (Navy, Weiß, Grautöne); der CI-Warnton `#c9772f` steht durchgehend für **Wärme**.

## Betreffzeilen (Vorschläge)

1. Du heizt gerade für den Himmel.
2. SPLASH oder DROP? Hier verschwindet deine Wärme.
3. Neu: Die Abdeckung, die deinen Whirlpool warm hält

Preheader (im HTML hinterlegt): „SPLASH oder DROP im Garten? Dann verlierst du gerade jede Nacht Wärme – so stoppst du das.“

## Vor dem Versand

- `assets/homedeluxe-logo-white.png` im Newsletter-Tool hochladen und den relativen `src` im Logo-`<img>` durch die gehostete URL ersetzen.
- `{{UNSUBSCRIBE_URL}}` durch den Abmelde-Platzhalter des Newsletter-Tools ersetzen.
- Preise & UVP prüfen (Stand 22.10.2026 laut Shop: je 79 €; UVP SPLASH THERMO 129 €, DROP THERMO 89 €).
- Lieferzeit („ca. 1–2 Werktage“) am Versandtag gegenprüfen.
- Alle Links tragen UTM-Parameter `utm_campaign=thermo-splash-drop` mit eigenem `utm_content` je Button.
