# import datetime
# import argparse
# import unittest
from reader import readerFunc
from csvPath import csvPath


def exe():
    csvExists = csvPath("despesas.csv")
    
    if not csvExists:
        print("O arquivo não existe ou não é CSV")
    else:
        readerFunc(csvExists)
    
if __name__ == "__main__":
    exe()