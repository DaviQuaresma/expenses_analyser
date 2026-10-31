import csv
from pathlib import Path
import sys


def csvPath(fileName: str) -> Path | None:

    if not fileName:
        return None

    currentPath: Path = Path.cwd() / fileName

    if currentPath.suffix != ".csv" or not currentPath.exists():
        return None

    return currentPath


def reader(documentPath: str) -> list[dict]:

    path = csvPath(documentPath)

    if not path:
        print("O arquivo não existe ou não é CSV")
        sys.exit("Código encerrado com sucesso.")

    dataframe: list[dict] = []

    with open(path, "r", encoding="utf-8", newline="") as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            dataframe.append(row)

    return dataframe
