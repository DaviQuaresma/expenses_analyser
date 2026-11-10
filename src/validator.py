import datetime as dt
from decimal import Decimal as dc


def change_date(date: str) -> bool:
    format_defined = "%Y-%m-%d"

    try:
        dt.datetime.strptime(date, format_defined).date()
        return True
    except:
        return False


def change_money(money: str) -> dc | bool:

    try:
        clear_money = money.replace(",", ".")
        money_converted = dc(clear_money)
        return money_converted
    except:
        return False


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
            date = data["data"]
            validate = change_date(date)

            if not validate:
                new_error["line"] = line
                new_error["field"] = "data"
                new_error["value"] = date
                errors.append(new_error)
                dt.remove(data)
                invalid += 1
                continue
            else:
                data["data"] = date

        if "valor" in data:
            money = data["valor"]
            validate = change_money(money)

            if not validate:
                new_error["line"] = line
                new_error["field"] = "valor"
                new_error["value"] = money
                errors.append(new_error)
                dt.remove(data)
                invalid += 1
                continue
            else:
                data["valor"] = validate

        valid += 1

    return dt, valid, invalid, errors
