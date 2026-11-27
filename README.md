# design_andair

Redesign-Entwürfe für die Startseite von [andair.ch](https://andair.ch), Deutsch und Englisch (umschaltbar oben rechts).

| Variante | Richtung | Datei |
|---|---|---|
| A · Werkplan | Hell, technisch, Schweizer Raster (Archivo, Plex Mono) | `varianten/a-werkplan/index.html` |
| B · Bunker | Dunkel, Beton, grosse Versalien (Barlow Condensed) | `varianten/b-bunker/index.html` |
| C · Editorial | Warm, Serifen, Herkunft und Vertrauen (Fraunces, Instrument Sans) | `varianten/c-editorial/index.html` |

`index.html` ist die Übersicht. Die Seiten werden aus `build/build.py` erzeugt (`python3 build/build.py`); Texte, Bilder und Kontaktdaten stammen von andair.ch. Schriften liegen lokal unter `assets/fonts` (SIL Open Font License).

Offen: Die Fotos sind die niedrig aufgelösten Bilder der heutigen Website. Für die Umsetzung braucht es Originale in hoher Auflösung. Links führen in den Entwürfen noch auf Anker der Startseite.

## Design-Skills

Unter `.claude/skills/` liegen drei Claude Design Skills (unveränderte Kopien, Stand 27.11.2026).

| Skill | Aufruf | Wofür | Quelle | Lizenz |
|---|---|---|---|---|
| emil-design-eng | `/emil-design-eng` | UI-Feinschliff, Interaktionen, Animationen | github.com/emilkowalski/skills | MIT |
| impeccable | `/impeccable` | Layout, Typografie, Farbe, Kritik und Audit | github.com/pbakaus/impeccable | Apache 2.0 |
| design-taste-frontend | `/design-taste-frontend` | Visuelle Art-Direction, Anti-Einheitslook | github.com/Leonxlnx/taste-skill | MIT |
