def new_merchandise(id: str,
                    description: str,
                    origin: str,
                    value: str,
                    currency: str,
                    category: str,
                    weight: int,
                    status: str,
                    ):
    merch = {
        "id": id,
        "description": description,
        "origin": origin,
        "value": value,
        "currency": currency,
        "category": category,
        "weight": weight,
        "status": status,
    }
    return merch

def new_merchandise_to_save(id: str,
                    description: str,
                    origin: str,
                    value: str,
                    currency: str,
                    category: str,
                    weight: int,
                    status: str,
                    tariff: int,
                    ):
    merch = {
        "id": id,
        "description": description,
        "origin": origin,
        "value": value,
        "currency": currency,
        "category": category,
        "weight": weight,
        "status": status,
        "tariff": tariff
    }
    return merch
