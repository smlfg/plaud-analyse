"""Transkript-Analyse und Plots für PlaudImport.

Usage: python3 run_analyse.py
Voraussetzung: .txt in PlaudImport/ (read-only). Optional: plaud_index.csv für Startzeit/Dauer.
"""

from constants import CLEAN_DIR, IMPORT_DIR, PLOTS_DIR
from load_index_by_datei import load_index_by_datei
from plot_dauer_hapax import plot_dauer_hapax
from plot_dauer_inhalt import plot_dauer_inhalt
from plot_dauer_satzlaenge import plot_dauer_satzlaenge
from plot_dauer_vielfalt import plot_dauer_vielfalt
from plot_dauer_wortlaenge import plot_dauer_wortlaenge
from plot_dauer_wpm import plot_dauer_wpm
from plot_scatter_woerter_hapax import plot_scatter_woerter_hapax
from plot_scatter_woerter_vielfalt import plot_scatter_woerter_vielfalt
from plot_top_inhalt_woerter import plot_top_inhalt_woerter
from plot_zeit_anfang_abschluss import plot_zeit_anfang_abschluss
from plot_zeit_fuellwort_rate import plot_zeit_fuellwort_rate
from plot_zeit_hapax import plot_zeit_hapax
from plot_zeit_inhalt import plot_zeit_inhalt
from plot_zeit_satzlaenge import plot_zeit_satzlaenge
from plot_zeit_vielfalt import plot_zeit_vielfalt
from plot_zeit_wiederholung import plot_zeit_wiederholung
from plot_zeit_wortlaenge import plot_zeit_wortlaenge
from plot_zeit_wpm import plot_zeit_wpm
from primary_cohort import primary_cohort
from sammle_records import sammle_records
from save_anfang_abschluss_csv import save_anfang_abschluss_csv


def run_analyse():
    if not IMPORT_DIR.is_dir():
        print(f"Ordner fehlt: {IMPORT_DIR}")
        return

    index = load_index_by_datei()
    index_used = bool(index)
    if not index_used:
        print(
            "Hinweis: plaud_index.csv fehlt — Zeit/Dauer-Plots nutzen nur das Datum aus dem "
            "Dateinamen (Mitternacht); Dauer-Plots entfallen. Index: python3 plaud_index.py"
        )

    PLOTS_DIR.mkdir(exist_ok=True)
    records = sammle_records()
    skipped_hint = " (leere Dateien in sammle_records übersprungen)"
    for r in records:
        print(
            f"{r['datei']}: {r['woerter_gesamt']} Wörter, Vielfalt {r['vielfalt']:.3f}, "
            f"Ø Wort {r['wortlaenge_avg']:.1f}, Ø Satz {r['satzlaenge_avg']:.1f}"
        )

    print(f"\n{len(records)} Transkripte analysiert.{skipped_hint}")
    if not records:
        print("Keine Daten für Plots.")
        return

    plot_scatter_woerter_vielfalt(records, PLOTS_DIR)
    plot_zeit_vielfalt(records, PLOTS_DIR)
    plot_zeit_wortlaenge(records, PLOTS_DIR)
    plot_zeit_satzlaenge(records, PLOTS_DIR)
    plot_zeit_inhalt(records, PLOTS_DIR)
    plot_zeit_hapax(records, PLOTS_DIR)
    plot_zeit_fuellwort_rate(records, PLOTS_DIR)
    plot_zeit_wiederholung(records, PLOTS_DIR)
    plot_scatter_woerter_hapax(records, PLOTS_DIR)
    plot_top_inhalt_woerter(records, PLOTS_DIR)
    plot_zeit_wpm(records, PLOTS_DIR)
    plot_dauer_vielfalt(records, PLOTS_DIR)
    plot_dauer_wortlaenge(records, PLOTS_DIR)
    plot_dauer_satzlaenge(records, PLOTS_DIR)
    plot_dauer_inhalt(records, PLOTS_DIR)
    plot_dauer_hapax(records, PLOTS_DIR)
    plot_dauer_wpm(records, PLOTS_DIR)

    cohort_names = {p.name for p in primary_cohort()}
    cohort_records = [r for r in records if r["datei"] in cohort_names]
    csv_path = save_anfang_abschluss_csv(cohort_records)
    print(f"Anfangs/Abschluss-CSV: {csv_path} ({len(cohort_records)} Samuel-Flg-Monologe)")
    plot_zeit_anfang_abschluss(cohort_records, PLOTS_DIR)

    with_dauer = [r for r in records if r["dauer_sek"] is not None]
    print(f"Plots in {PLOTS_DIR}/")
    if index_used:
        print(f"Index: {len(index)} Einträge geladen, {len(with_dauer)} mit Dauer verknüpft.")
    print(f"Bereinigte Texte: {CLEAN_DIR}/")


if __name__ == "__main__":
    run_analyse()