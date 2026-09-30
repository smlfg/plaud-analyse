# plaud-analyse

Sprachanalyse für Plaud-Transkripte. Liest `.txt`-Dateien aus `PlaudImport/`, berechnet Wort-/Satz-Metriken pro Transkript und erzeugt Plots in `plots/`.

## Setup

```bash
python3 -m venv .venv
.venv/bin/pip install matplotlib
```

## Run

```bash
# Vollanalyse + alle Preset-Plots
python3 run_analyse.py

# Optional: Startzeit/Dauer je Transkript (für Zeit- und Dauer-Plots)
python3 plaud_index.py
```

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