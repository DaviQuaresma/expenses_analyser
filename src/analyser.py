from decimal import Decimal as dc

def bigger_value(data: dict) -> dict:
    bigger_data: dict = {}
    
    bigger_data["categoria"] = None
    bigger_data["valor"] = dc("-Infinity")
    
    for key, value in data.items():
        if value > bigger_data["valor"]:
            bigger_data["categoria"] = key
            bigger_data["valor"] = value
    
    return bigger_data

def analyser(data: list[dict]):
    totals: dict = {}
    total: dc = dc()
    qtd: dc = dc(len(data))
    
    media: dc = dc()
   
    for category in data:
        # Agrupa as categorias e seus valores
        key = category["categoria"]
        value = category["valor"]
        totals[key] = totals.get(key, 0) + value
        # Fim do agrupamento

        # Total das despesas
        total += value
        # Fim do total

    # Maior despesa
    bigger_data = bigger_value(totals)
    
    # Media
    media = round(total / qtd, 2)
    
    return totals, total, media, bigger_data
