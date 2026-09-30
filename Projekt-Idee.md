Projekt-Idee

Ich will händisch programmiere,
Sprach analyse
input
MCP Plaud

Tranksript

Filter auf Transkript
keine Vorlesugen
kein VOrtrag


dann loop durch die Liste von Transkripten

dann Analyse auf Wort varianz pro Transkript
dann Analyse auf Satzlänge pro Transkript
etc 


dann Ploten der Ergebnisse

dann müssen wir die sauberen lines speichern

    dann brauchen wir wieder die varanz funktion mit def varian

    langer text split ( auf wort basis)
    dann länge bestimmen
    dann mehrfache raus
    dann berechen

    varianz vielfalt

    so und ausgebae
    also graphlib

    x achse zeit ( der Aaufname)
    y achese die WSAEREMOTE

    dann neuer graphlib
    x achte länge der Aufname
    y achse metriken

    x zeitpunkt
    y worltänge

    x zeitpunkt
    y satzlänge

    x zeitpunkt
    y häufigkeit wörter ( ausßer füll Wörter)

## Status Agent

- **Micro-Code:** eine Funktion pro `.py`-Datei (Name = Funktion); Konstanten nur in `constants.py`
- **Run:** `python3 run_analyse.py` (auch `python3 withplot.py` / `python3 analyse_plot.py` / `python3 run_plots.py`)
- **Analyse-CLI:** `python3 run_analyse_cli.py` — interaktiv bei TTY ohne Argumente; ohne TTY und ohne Flags → Exit 2 mit Hinweis (hängt nicht an `input()`)
  - `--list` — Achsen (`axis_registry`) und Metriken (`metric_registry`)
  - `--metric vielfalt,hapax` — Tabelle pro Transkript
  - `--x zeit --y vielfalt --y hapax` — **mehrere `--y` = je eine PNG** (kein Multi-Trace); Dateiname CLI: `plots/{x}_vs_{y}.png`
  - `--all` — volle Pipeline wie `run_analyse.py` (alle Legacy-Plots, Anfang/Abschluss-CSV, Status)
  - `--exclude-titel KEYWORD` (wiederholbar, z. B. `--exclude-titel Vorlesung --exclude-titel Vortrag`); Vorschläge in `EXCLUDE_TITEL_DEFAULTS`
  - `interactive_menu()` liefert dasselbe `argparse.Namespace` wie `parse_analyse_args` (Felder: `metrics`, `x`, `ys`, `all`, `list_only`, `exclude_titel`) — kein Rebuild von `sys.argv`
  - XY-Kern: `plot_xy()`; Legacy-`plot_zeit_*` / `plot_dauer_*` / `plot_scatter_*` sind dünne Wrapper mit `out_name=` für alte PNG-Namen
- **Kern:** `pipeline`, `metriken`, `sammle_records`, `scatter_save`, `load_index_by_datei`, `save_clean_text`, `tokenize_fn` (def `tokenize`, nicht `tokenize.py` — stdlib-Kollision), …
- **Plots:** je eine Funktion in `plot_*.py` (z. B. `python3 plot_zeit_vielfalt.py`)
- **Extra-Metriken:** in `metriken()` — `hapax`, `fuellwort_rate`, `unique_count`, `wiederholungs_rate`, `max_wort_anteil`, `satz_anzahl`; in `sammle_records` zusätzlich `text`, `wpm` (braucht Dauer aus Index)
- **Extra-Plots:** in `run_analyse.py` — `zeit_hapax`, `zeit_fuellwort_rate`, `zeit_wpm`, `zeit_wiederholung`, `scatter_woerter_hapax`, `dauer_hapax`, `dauer_wpm`, `top_inhalt_woerter` (+ Basis-Plots)
- **Input:** `PlaudImport/` · **Output:** `PlaudImportClean/`, `plots/`
- **Index:** optional `python3 plaud_index.py` → `plaud_index.csv`
- **Titel-Filter:** über CLI `--exclude-titel` (siehe Analyse-CLI)

## Plattformen (Mac / Windows / Linux)

- **Analyse-CLI** (`run_analyse_cli.py`, Metriken, Plots): plattformneutral — Python 3 + venv mit `matplotlib` (Backend `Agg`, kein Display nötig). Pfade über `pathlib`.
- **Interaktives Menü:** Terminal/PowerShell mit TTY; ohne TTY und ohne Flags → Exit 2 (hängt nicht).
- **Mac / Linux:** Analyse läuft so; zusätzlich `plaud` im PATH für Download/Index.
- **Windows:** Analyse/Plots in PowerShell/CMD mit Python+venv ok; Plaud-Anbindung nur, wenn `plaud` dort installiert/im PATH ist (sonst WSL oder Hersteller-Support).
- **Kurz:** Analyse-Code = OS-unabhängig; Download/Index hängen am `plaud`-Binary, nicht am Analyse-CLI.

## Lauf: Slice Hypothese 1 — Anfangs- gegen Abschluss-Sprache

- **Marker exakt + Wortgrenzen + case-insensitive**: Anfang = `ich will`, `man könnte`, `neue Idee`, `ich baue`; Abschluss = `fertig`, `geschafft`, `läuft`, `abgeschlossen`.
- **Primärkohorte**: vollständig parsebare Monologe mit einzigem Sprecher `Samuel Flg` (gefiltert via `parse_speakers` + `primary_cohort`); 17 von 223 Dateien.
- **Neue Module**: `parse_speakers.py`, `primary_cohort.py`, `count_anfang_abschluss.py`, `save_anfang_abschluss_csv.py`, `plot_zeit_anfang_abschluss.py`; Konstanten in `constants.py` (`SAMUEL_FLG`, `ANFANG_MARKER`, `ABSCHLUSS_MARKER`, `ANFANG_ABSCHLUSS_CSV`, `ZEIT_ANFANG_ABSCHLUSS_PNG`, `GRAPHIFY_DIR`).
- **Metrik-Erweiterung**: `metriken()` liefert zusätzlich `anfang_raw`, `abschluss_raw`, `anfang_per_1k`, `abschluss_per_1k`, `diff_per_1k`. Berechnung auf allen Records (billig), Plot + CSV nur über Samuel-Flg-Kohorte.
- **Outputs**: `graphify-out/anfang_abschluss.csv`, `plots/zeit_anfang_abschluss.png`.
- **Integration**: `run_analyse.py` ergänzt; bestehende Outputs/Plots unverändert (regressionsfrei).
- **Run**: `python3 run_analyse.py` schreibt CSV + Plot.
- **Smoke**: `parse_speakers` round-trip, Marker-Treffer in 17 Samuel-Flg-Monologen, Wortgrenzen verifiziert (kein "ich willen", `\b` deckt Umlaute).
