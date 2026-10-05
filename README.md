# plaud-analyse

Sprachanalyse für Plaud-Transkripte. Liest `.txt`-Dateien aus `PlaudImport/`, berechnet Wort-/Satz-Metriken pro Transkript und erzeugt Plots in `plots/`.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install matplotlib questionary plotext
```

## Run

```bash
# Vollanalyse + alle Preset-Plots
python3 run_analyse.py

# Optional: Startzeit/Dauer je Transkript (für Zeit- und Dauer-Plots)
python3 plaud_index.py

# Plot direkt im Terminal (plotext, kein PNG)
python3 run_analyse_cli.py --x zeit --y vielfalt --terminal

# Freie X/Y-Dimensionen (Achse oder Metrik)
python3 run_analyse_cli.py --x vielfalt --y hapax

# Uhrzeit (0–24 h) vs. Wörter pro Minute (Index mit Startzeit nötig)
python3 run_analyse_cli.py --x uhrzeit --y wpm
```

Ohne Argumente startet das interaktive Menü (TTY, Schleife bis **5) Beenden** oder `q`/`quit`);
Flags (einmalig): `--list`, `--metric`, `--x`/`--y`, `--all`, `--terminal`, `--exclude-titel`.

## Layout

- `PlaudImport/` — Input, read-only, nicht im Repo
- `PlaudImportClean/` — bereinigte Texte (Output)
- `plots/` — PNG-Plots (Output)
- `plaud_index.csv` — optionaler Index mit Startzeit/Dauer (Output)

## Konventionen

- Micro-Code: eine Funktion pro `.py`-Datei (Name = Funktion); Konstanten in `constants.py`.
- Metriken in `metriken()`, Record-Aggregation in `sammle_records()`.

## Status

- Plot-Pipeline läuft (Zeit, Dauer, Scatter, Top-Wörter).
- Anfangs-/Abschluss-Marker (Samuel-Flg-Kohorte) als zusätzlicher Slice dokumentiert in `Projekt-Idee.md`.
- CLI mit interaktivem Menü + Flags: in Planung, siehe `Projekt-Idee.md`.

## Lizenz

[MIT](./LICENSE) — `Copyright (c) 2026 Samuel Fleig`.