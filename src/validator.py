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
    for data in dt:
        for key, value in data.items():
            if key == "data":
                unformated_date = value
                formated_date = changeDate(unformated_date)
                data[key] = formated_date

            if key == "categoria" and not value:
                data[key] = "N/A"

            if key == "descricao" and not value:
                data[key] = "N/A"

            if key == "valor":
                unformated_money = value
                formated_money = changeMoney(unformated_money)
                data[key] = formated_money
    return dt
