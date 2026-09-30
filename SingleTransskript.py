import os

pwd=os.getcwd()
Dateien = os.listdir(f"PlaudImport")
print(Dateien[0])

with open(f"PlaudImport/{Dateien[0]}", encoding="utf-8") as f:
    Transkript = f.read()


zeilen = Transkript.splitlines()
def bereinige_ohne_regex(zeile):
    if ": " not in zeile:
        return zeile
    return zeile.split(": ", 1)[1]

Bereinigt = ([bereinige_ohne_regex(z) for z in zeilen])

text = " ".join(Bereinigt)
text = text.lower()
woeter = text.split()
gesamt = (len(woeter))
verschieden = len(set(woeter))
vielfalt = (verschieden / gesamt)
print("Vielfalt", vielfalt, "gesamt", gesamt, "verschieden", verschieden, )
