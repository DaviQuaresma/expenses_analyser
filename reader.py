import csv
from pathlib import Path

def readerFunc(filePath: Path):
    with open(filePath, newline="") as csvFile:
        reader = csv.reader(csvFile, delimiter=" ", quotechar="|")
        for row in reader:
            print(", ".join(row))
