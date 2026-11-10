import argparse
from src.reader import reader
from src.validator import validator
from src.analyser import analyser
from src.report import report

def main():
    parser = argparse.ArgumentParser(description="Ler arquivo CSV")
    parser.add_argument('file_name', type=str, help="O arquivo tem que ter a extensão junto. EX: arquivo.csv")
    args = parser.parse_args()
    
    # Execução do fluxo de dados
    dt = reader(args.file_name)
    validated_dt, valid, invalid, errors = validator(dt)
    totals, total, media, bigger_data = analyser(validated_dt)
    
    report(totals, total, media, bigger_data, valid, invalid, errors)
        
if __name__ == "__main__":
    main()
