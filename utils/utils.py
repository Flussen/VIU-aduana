from utils.color import send_cyan, send_grey


def print_merchandise_info(item_id, data):
    send_cyan(f" {item_id}")
    send_grey(f"Descripción: {data['description']}")
    send_grey(f"Origen: {data['origin']}")
    send_grey(f"Valor: {data['value']}")
    send_grey(f"Categoría: {data['category']}")
    send_grey(f"Peso: {data['weight']}")
    send_grey(f"Moneda: {data['currency']}")
    if "tariff" in data:
        send_grey(f"Arancel: {data['tariff']}")