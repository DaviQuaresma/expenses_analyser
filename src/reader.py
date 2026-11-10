import csv
from pathlib import Path
import sys


def csv_path(file_name: str) -> Path | None:

    if not file_name:
        return None

    current_path: Path = Path.cwd() / file_name

    if current_path.suffix != ".csv" or not current_path.exists():
        return None

    return current_path


def reader(documentPath: str) -> list[dict]:

    path = csv_path(documentPath)

    if not path:
        print("O arquivo não existe ou não é CSV")
        sys.exit("Código encerrado com sucesso.")

    dataframe: list[dict] = []

    with open(path, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            dataframe.append(row)

    return dataframe
