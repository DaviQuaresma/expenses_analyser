from decimal import Decimal as dc

def report(totals: dict, total: dc, media: dc, bigger_data: dict, valid: int, invalid: int, errors: list[dict]):
    
    print("==============================================")
    print("           RELATORIO DE DESPESAS")
    print("==============================================")
    
    print("\n\n")
    print("Transacoes válidas: ", valid)
    print("Transacoes inválidas: ", invalid)
    print("\n")
    
    print("Total de despesas: R$", total)
    print("Media por transacao: R$", media)
    print("Maior despesa: R$", bigger_data["valor"])
    print("\n")
    
    print("----------------------------------")
    print("DESPESAS POR CATEGORIA")
    print("----------------------------------")
    for key, value in totals.items():
        print(key, "=>", f"R$ {value}")
   
    print("\n----------------------------------")
    print("ERROS")
    print("----------------------------------")
    for erro in errors:
        print(f"\nErro na linha {erro.get("line")}")
        print(f"- Campo do erro: {erro.get("field")}")
        print(f"- Valor do campo: {erro.get("value")}")
    
    print("\n\n==============================================")