# Pitch-Seite: ein Claude-Skill

Pitche ein Format als Webseite statt als PDF. Der Skill baut aus deiner Idee eine
interaktive Seite: Jeder Bildschirm ein Kapitel mit Vollbild-Clip, dazu ein Quiz zum
Mitspielen, Runden zum Antippen und Looks zum Umschalten.

**Beispiel, mit diesem Skill gebaut:** [Der letzte Gang](https://pierrestudios-der-letzte-gang.netlify.app),
ein erfundenes Kochshow-Format.

## Installation

Für **Claude Code**: den Ordner `pitch-seite` nach `~/.claude/skills/` kopieren.

```bash
git clone https://github.com/pierreuebelhack-svg/pitch-seite.git ~/.claude/skills/pitch-seite
```

Danach in Claude Code einfach sagen: *„Bau mir eine Pitch-Seite für mein Format …“*

Für **Claude.ai / Claude Desktop**: den Ordner als ZIP packen und unter
Einstellungen → Fähigkeiten (Skills) hochladen.

## Was drin ist

- `SKILL.md`: die Anleitung für Claude (Ablauf, Regeln, Prüfliste)
- `vorlage/index.html`: die Seite, eine Datei, alles markiert mit `[eckigen Klammern]`
- `vorlage/bauen.py`: baut den Upload-Ordner mit Link-Vorschau und optionalem Besucherzähler

Bilder und Clips bringst du selbst mit, zum Beispiel aus einem KI-Videotool.
Fehlende Dateien zeigen einen Platzhalter, die Seite funktioniert trotzdem.

## Lizenz

MIT. Benutzen, ändern, weitergeben. Über einen Hinweis auf
[Pierre Studios](https://www.linkedin.com/in/pierre-uebelhack-4b06b6193/) freue ich mich.
