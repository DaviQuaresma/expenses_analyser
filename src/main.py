import argparse
# import unittest

from src import reader, validator, analyser


def exe():
    parser = argparse.ArgumentParser(description="Ler arquivo CSV")
    
    parser.add_argument('filename', type=str, help="O arquivo tem que ter a extensão junto. EX: arquivo.csv")
    args = parser.parse_args()
    
    dt = reader(args.filename)
    
    validated_dt = validator(dt)
    
    analyser(validated_dt)
        
    
if __name__ == "__main__":
    exe()
