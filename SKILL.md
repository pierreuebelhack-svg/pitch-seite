---
name: pitch-seite
description: Baut aus einer Format- oder Projektidee eine interaktive Pitch-Webseite statt eines PDF-Decks. Jeder Bildschirm ein Kapitel mit Vollbild-Clip oder -Bild, dazu Mitmach-Elemente (Quiz mit Zeitdruck, Runden zum Antippen, Look-Umschalter) und Zurück-Knopf bei internen Sprüngen. Trigger DE: "pitch als webseite", "pitch-seite", "baue mir eine pitch seite", "format pitchen online", "interaktiver pitch". Trigger EN: "pitch website", "interactive pitch", "pitch page instead of deck", "format pitch site".
---

# Pitch-Seite

Ein Pitch, den man nicht liest, sondern durchklickt. Die Vorlage in `vorlage/` ist
eine fertige, getestete Seite mit sieben Bildschirmen. Du füllst sie mit dem Format
des Nutzers, statt eine Seite neu zu erfinden.

**Grundsatz:** Eine Idee verkauft sich, wenn man sofort Bilder vor Augen hat. Die
Seite soll das Gefühl der späteren Show vermitteln, nicht alles erklären.

## Ablauf

### 1. Format klären (kurz, nicht ausfragen)
Frage nur, was fehlt, höchstens fünf Punkte auf einmal:
- Titel, Logline (ein bis zwei Sätze), Genre, Umfang (Folgen × Minuten)
- Wer tritt an? (drei Figuren mit Rolle und Konflikt)
- Die eine Mechanik, die das Format besonders macht (wird zum Mitspiel-Quiz)
- Der Ablauf einer Folge in vier Stufen (drei Runden plus Finale)
- Absender (Firma, Name, Rolle, Mail) und welche Bilder/Clips es schon gibt

Erfinde keine Fakten über echte Personen, Sender oder Zahlen. Fehlt etwas, frag
oder markiere es als Vorschlag.

### 2. Vorlage kopieren
Kopiere `vorlage/` in den Projektordner des Nutzers (z. B. `web/`). Arbeite nur in
der Kopie. Die Vorlage selbst bleibt unverändert.

### 3. Inhalte einsetzen
In `index.html` ist alles, was ersetzt werden muss, in `[eckigen Klammern]` markiert.
Ein Kommentar über jeder Sektion nennt den Zweck und die erwarteten Dateinamen.
- **Texte:** alle `[...]` ersetzen. `<em>` setzt das Akzentwort in der Signalfarbe.
- **Quiz** (Skript, `var POOL`): mindestens drei, besser acht Fragen zum Thema des
  Formats. **Nur nachprüfbare Fakten**, eine Antwort eindeutig richtig. `SCHATZ` =
  Belohnung je richtiger Antwort, `ERGEBNIS` = Text nach 0 bis 3 richtigen.
- **Ablauf** (Skript, `var STAND`): Überschrift und ein Satz je Runde.
- **Farbe:** `--signal` in `:root` ist die einzige Akzentfarbe. Passend zum Format
  wählen, Kontrast auf Dunkel prüfen.
- Sektionen, die nicht passen, ganz entfernen und die Nummern (Eyebrow, Fußzeile,
  Kapitelzähler `/ 07`) anpassen.

### 4. Bilder und Clips
Dateien mit genau den Namen aus den Kommentaren nach `bilder/` bzw. `clips/` legen,
dann erscheinen sie von selbst; fehlende Dateien zeigen einen dezenten Platzhalter.
- 16:9, Clips stumm, kurz (5 bis 10 s), als Loop. MP4 H.264, `-movflags +faststart`.
- **Ein Element pro Fläche:** Liegt ein Clip auf einer Fläche, kein Standbild darunter.
  Sonst scheint es durch die Verläufe durch (Doppelbild).
- Looks auf Seite 06 müssen **deckungsgleich** sein (gleiche Kamera, nur Material/Licht).
- Mit KI generiert: keine echten Personen, keine Promi-Ähnlichkeit, keine Marken.
  Fußzeile „Demo-Format · alle Bilder KI-generiert“ stehen lassen.

### 5. Lesbarkeit
Text liegt auf Bild. Verläufe gibt es pro Seite im CSS (`::after`). Regel: **so dunkel
wie für die Schrift nötig, so klein wie möglich, sehr weich auslaufen**, damit vom Bild
möglichst viel frei bleibt. Nach jedem neuen Bild prüfen.

### 6. Prüfen, bevor du „fertig“ sagst
Rendere jede Seite auf **Rechner (1440 × 810)** und **Handy (390 px)** und sieh sie an:
- Schrift überall lesbar, nichts abgeschnitten, kein Doppelbild
- Quiz einmal durchspielen, Runden und Looks durchklicken
- Chips auf Seite 02 anklicken: Zurück-Knopf erscheint und führt zur Lesestelle zurück
- Skripte ohne Fehler (z. B. mit `node` jeden `<script>`-Block parsen)

### 7. Veröffentlichen (nur auf Wunsch und nur für eigene Formate)
`python3 bauen.py <öffentliche-url> [goatcounter-name]` erzeugt `_upload/` mit nur den
genutzten Dateien, einer Link-Vorschau für LinkedIn und optional einem cookie-freien
Besucherzähler (GoatCounter). `_upload/` dann z. B. per Netlify hochladen.
Seiten, die im Namen einer echten fremden Firma oder Person auftreten, nicht selbst
veröffentlichen, sondern dem Nutzer den Ordner übergeben.

## Was die Vorlage schon kann
- Jede Seite ein Bildschirm (rastet ein), am Handy Motiv oben, Text darunter
- Kapitelzähler und Fortschrittslinie oben, Pfeiltasten springen seitenweise (zum Vorführen)
- Quiz mit 8-Sekunden-Takt und Ergebnis, direkt auf der Seite
- Vier Runden zum Antippen, Vollbild wechselt mit; beim Betreten startet Runde 1
- Drei Looks zum Umschalten mit weicher Überblendung
- Zurück-Knopf nach jedem internen Sprung, der zur gemerkten Lesestelle zurückführt
- Respektiert „Bewegung reduzieren“
