# import datetime
import argparse
# import unittest

from src import reader


def exe():
    # document = input(str('Qual é o nome do arquivo (ex: document.csv)?\n'))
    parser = argparse.ArgumentParser(description="Ler arquivo CSV")
    
    parser.add_argument('filename', type=str, help="O arquivo tem que ter a extensão junto. EX: arquivo.csv")
    args = parser.parse_args()
    
    # Aqui você chama a função reader que foi importada do seu __init__.py
    reader(args.filename)
        
    
if __name__ == "__main__":
    exe()
