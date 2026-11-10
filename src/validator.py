import datetime as dt
from decimal import Decimal as dc


def change_date(date: str):
    format_defined = "%Y-%m-%d"
    format_date = dt.datetime.strptime(date, format_defined).date()

    return format_date


def change_money(money: str) -> dc:
    clear_money = money.replace(",", ".")
    money_converted = dc(clear_money)

    return money_converted


def validator(dt: list[dict]):

    invalid = 0
    valid = 0
    errors: list[dict] = []
    line: int = 0

    for data in list(dt):
        line += 1
        new_error = {}

        if not data.get("data"):
            new_error["line"] = line
            new_error["field"] = "data"
            new_error["value"] = data.get("data")
            errors.append(new_error)
            dt.remove(data)
            invalid += 1
            continue
     
        if not data.get("valor"):
            new_error["line"] = line
            new_error["field"] = "valor"
            new_error["value"] = data.get("valor")
            errors.append(new_error)
            dt.remove(data)
            invalid += 1
            continue
        
        if not data.get("descricao"):
            new_error["line"] = line
            new_error["field"] = "descricao"
            new_error["value"] = data.get("descricao")
            errors.append(new_error)
            dt.remove(data)
            invalid += 1
            continue
        
        if not data.get("categoria"):
            new_error["line"] = line
            new_error["field"] = "categoria"
            new_error["value"] = data.get("categoria")
            errors.append(new_error)
            dt.remove(data)
            invalid += 1
            continue

        if "data" in data:
            unformated_date = data["data"]
            data["data"] = change_date(unformated_date)

        if "valor" in data:
            unformated_money = data["valor"]
            data["valor"] = change_money(unformated_money)

        valid += 1

    return dt, valid, invalid, errors
