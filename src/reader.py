import csv
from pathlib import Path

def csvPath(fileName: str) -> Path | None:
    currentPath: Path = Path.cwd() / fileName

    if currentPath.suffix != ".csv" or not currentPath.exists():
        return None

    return currentPath

def reader(documentPath: str):
    
    path = csvPath(documentPath)
    
    if not path:
        print("O arquivo não existe ou não é CSV")
    
    dataframe = [str]
    
    with open(path, "r") as csvFile:
        reader = csv.reader(csvFile, delimiter=" ", quotechar="|")
        line = 0
        for row in reader:
            string_line = ",".join(row)
            new_list = string_line.split(',')
            print("linha completa com split: ", string_line)
            print("linha completa com split: ", new_list)
            
            line += 1
        #     if line == 0:
            print("linha completa com split: ", new_list[0])
        #         print(" ".join(row))
        #         line += 1
        #     else:
        #         print(f"\t Coluna1 {row[0]}")
        #         line += 1
        # print(f"Readed {line} lines.")
