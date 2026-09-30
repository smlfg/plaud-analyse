"""Ergebnis-CSV unter graphify-out/anfang_abschluss.csv schreiben."""

import csv

from constants import ANFANG_ABSCHLUSS_CSV


def save_anfang_abschluss_csv(rows, out=None):
    fieldnames = [
        "datei",
        "start",
        "woerter_gesamt",
        "anfang_raw",
        "abschluss_raw",
        "anfang_per_1k",
        "abschluss_per_1k",
        "diff_per_1k",
        "anfang_kontexte",
        "abschluss_kontexte",
    ]
    target = out if out is not None else ANFANG_ABSCHLUSS_CSV
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(target, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(
                {
                    "datei": r["datei"],
                    "start": r["start"].isoformat() if r.get("start") else "",
                    "woerter_gesamt": r["woerter_gesamt"],
                    "anfang_raw": r["anfang_raw"],
                    "abschluss_raw": r["abschluss_raw"],
                    "anfang_per_1k": r["anfang_per_1k"],
                    "abschluss_per_1k": r["abschluss_per_1k"],
                    "diff_per_1k": r["diff_per_1k"],
                    "anfang_kontexte": " | ".join(r.get("anfang_kontexte", [])),
                    "abschluss_kontexte": " | ".join(r.get("abschluss_kontexte", [])),
                }
            )
    return target


if __name__ == "__main__":
    print(save_anfang_abschluss_csv([{"datei": "x.txt", "woerter_gesamt": 1,
                                      "anfang_raw": 0, "abschluss_raw": 0,
                                      "anfang_per_1k": 0.0,
                                      "abschluss_per_1k": 0.0,
                                      "diff_per_1k": 0.0,
                                      "anfang_kontexte": [],
                                      "abschluss_kontexte": []}]))