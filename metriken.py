from avg_satzlaenge import avg_satzlaenge
from avg_wortlaenge import avg_wortlaenge
from count_anfang_abschluss import count_anfang_abschluss
from fuellwort_rate import fuellwort_rate
from hapax import hapax
from inhalt_woerter_anteil import inhalt_woerter_anteil
from max_wort_anteil import max_wort_anteil
from satz_anzahl import satz_anzahl
from tokenize_fn import tokenize
from unique_count import unique_count
from varianz import varianz
from wiederholungs_rate import wiederholungs_rate


def metriken(text):
    woerter = tokenize(text)
    aa = count_anfang_abschluss(text)
    return {
        "woerter_gesamt": len(woerter),
        "vielfalt": varianz(text),
        "wortlaenge_avg": avg_wortlaenge(woerter),
        "satzlaenge_avg": avg_satzlaenge(text, woerter),
        "inhalt_anteil": inhalt_woerter_anteil(woerter),
        "hapax": hapax(text),
        "fuellwort_rate": fuellwort_rate(text),
        "unique_count": unique_count(text),
        "wiederholungs_rate": wiederholungs_rate(text),
        "max_wort_anteil": max_wort_anteil(text),
        "satz_anzahl": satz_anzahl(text),
        "anfang_raw": aa["anfang_raw"],
        "abschluss_raw": aa["abschluss_raw"],
        "anfang_per_1k": aa["anfang_per_1k"],
        "abschluss_per_1k": aa["abschluss_per_1k"],
        "diff_per_1k": aa["diff_per_1k"],
        "anfang_kontexte": aa["anfang_kontexte"],
        "abschluss_kontexte": aa["abschluss_kontexte"],
    }


if __name__ == "__main__":
    print(metriken("Ein kurzer Test. Noch ein Satz."))
