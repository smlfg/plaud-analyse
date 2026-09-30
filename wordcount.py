
import os

pwd=os.getcwd()
Dateien = os.listdir(f"PlaudImport")
print(Dateien[0])

with open(f"PlaudImport/{Dateien[0]}", encoding="utf-8") as f:
    Transkript = f.read()

Wörter = Transkript.split()
print(len(Wörter))
