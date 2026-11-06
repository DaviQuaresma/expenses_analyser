import datetime as dt
from decimal import Decimal as dc


def changeDate(date: str):
    if not date:
        return dt.datetime.strptime(str(dt.datetime.now().date()), "%Y-%m-%d").date()
    else:
        return dt.datetime.strptime(date, "%Y-%m-%d").date()


def changeMoney(money: str) -> dc:

    if not money:
        return dc(0.0)

    clear_money = money.replace(",", ".")
    money_converted = dc(clear_money)

    return money_converted


def validator(dt: list[dict]):
    
    invalid = 0
    valid = 0
    
    for data in dt:
        if "data" in data:
            unformated_date = data["data"]
            data["data"] = changeDate(unformated_date)

        if not data.get("descricao"):
            print(f"Removendo dicionário inválido: {data}")
            dt.remove(data)
            invalid += 1
            
        if not data.get("categoria"):
            print(f"Removendo dicionário inválido: {data}")
            dt.remove(data)
            invalid += 1

        if "valor" in data:
            unformated_money = data["valor"]
            data["valor"] = changeMoney(unformated_money)
            
        valid += 1
        
    return dt, valid, invalid
