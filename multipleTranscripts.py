
import os

def clean_lines(line):
    if ": " not in line:
        return line
    else:
        return line.split(": ", 1)[1]

folder = "PlaudImport"

sorted_files = sorted(os.listdir(folder))

def pipeline(transcript):
    lines = transcript.splitlines()
    lines = [clean_lines(line) for line in lines]

    text = " ".join(lines)

    return (text)

results = {}
for file in sorted_files:
    if not file.endswith(".txt"):
        continue
    with open(os.path.join(folder, file), encoding="utf-8") as f:
        transcript = f.read()
    results[file] = pipeline(transcript)   # Ergebnis abspeichern, next

print(results)

for file, text in results.items():
    print(file, len(text.split()))

for file, text in results.items():
    text = text.lower()
    woeter = text.split()
    gesamt = (len(woeter))
    verschieden = len(set(woeter))
    vielfalt = (verschieden / gesamt)
    print("Vielfalt", vielfalt, "gesamt", gesamt, "verschieden", verschieden, )
