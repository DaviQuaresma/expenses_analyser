import datetime as datet
from datetime import date
from decimal import Decimal as dc


def change_date(date: str) -> date | bool:
    format_defined = "%Y-%m-%d"

    try:
        return datet.datetime.strptime(date, format_defined).date()
    except:
        return False


def parse_money(money: str) -> dc | bool:

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

    for row in list(dt):
        line += 1
        new_error = {}

        if not row.get("data"):
            new_error["line"] = line
            new_error["field"] = "data"
            new_error["value"] = row.get("data")
            errors.append(new_error)
            dt.remove(row)
            invalid += 1
            continue

        if not row.get("valor"):
            new_error["line"] = line
            new_error["field"] = "valor"
            new_error["value"] = row.get("valor")
            errors.append(new_error)
            dt.remove(row)
            invalid += 1
            continue

        if not row.get("descricao"):
            new_error["line"] = line
            new_error["field"] = "descricao"
            new_error["value"] = row.get("descricao")
            errors.append(new_error)
            dt.remove(row)
            invalid += 1
            continue

        if not row.get("categoria"):
            new_error["line"] = line
            new_error["field"] = "categoria"
            new_error["value"] = row.get("categoria")
            errors.append(new_error)
            dt.remove(row)
            invalid += 1
            continue

        if "data" in row:
            date = row["data"]
            validate = change_date(date)

            if not validate:
                new_error["line"] = line
                new_error["field"] = "data"
                new_error["value"] = date
                errors.append(new_error)
                dt.remove(row)
                invalid += 1
                continue
            else:
                row["data"] = validate

        if "descricao" in row:
            desc = row["descricao"].strip()

            if len(desc) <= 0:
                new_error["line"] = line
                new_error["field"] = "descricao"
                new_error["value"] = None
                errors.append(new_error)
                dt.remove(row)
                invalid += 1
                continue
            else:
                row["descricao"] = desc

        if "categoria" in row:
            cat = row["categoria"].strip()

            if len(cat) <= 0:
                new_error["line"] = line
                new_error["field"] = "categoria"
                new_error["value"] = None
                errors.append(new_error)
                dt.remove(row)
                invalid += 1
                continue
            else:
                row["categoria"] = cat

        if "valor" in row:
            money = row["valor"]
            validate = parse_money(money)

            if not validate:
                new_error["line"] = line
                new_error["field"] = "valor"
                new_error["value"] = money
                errors.append(new_error)
                dt.remove(row)
                invalid += 1
                continue
            else:
                row["valor"] = validate

        valid += 1

    return dt, valid, invalid, errors
