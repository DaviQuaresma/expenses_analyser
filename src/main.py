import argparse
# import unittest

from src import reader, analyser


def exe():
    parser = argparse.ArgumentParser(description="Ler arquivo CSV")
    
    parser.add_argument('filename', type=str, help="O arquivo tem que ter a extensão junto. EX: arquivo.csv")
    args = parser.parse_args()
    
    dataframe = reader(args.filename)
    
    analyser(dataframe)
        
    
if __name__ == "__main__":
    exe()
