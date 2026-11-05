def groupByCategory(data: list[dict]) -> dict:

    totals: dict = {}

    for category in data:
        key = category["categoria"]
        value = category["valor"]

        totals[key] = totals.get(key, 0) + value

    return totals


def analyser(dt: list[dict]):
    group = groupByCategory(dt)
    
    print(group)

    return dt
