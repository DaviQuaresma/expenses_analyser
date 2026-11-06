import datetime as dt
from decimal import Decimal as dc


def changeDate(date: str):
    format_defined = "%Y-%m-%d"
    format_date = dt.datetime.strptime(date, format_defined).date()
    
    return format_date


def changeMoney(money: str) -> dc:
    clear_money = money.replace(",", ".")
    money_converted = dc(clear_money)

    return money_converted


def validator(dt: list[dict]):

    invalid = 0
    valid = 0

    for data in list(dt):
        if not data.get("data") or data.get("data") is None or data.get("data") == "":
            dt.remove(data)
            invalid += 1
            continue

        if (
            not data.get("valor")
            or not data.get("descricao")
            or not data.get("categoria")
        ):
            dt.remove(data)
            invalid += 1
            continue

        if "data" in data:
            unformated_date = data["data"]
            data["data"] = changeDate(unformated_date)

        if "valor" in data:
            unformated_money = data["valor"]
            data["valor"] = changeMoney(unformated_money)

        valid += 1

    return dt, valid, invalid
