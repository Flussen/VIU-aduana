from data.memory_storage import categories_with_tariffs
from utils.cleaner import clear_console
from utils.color import send_green, send_grey, send_yellow
from utils.common import RETURN_TO_MENU_STR


def calculate_tariff(item):
    return item["value"] * (categories_with_tariffs[item["category"]] / 100)

def show_tariff_menu(item):
    clear_console()
    result = input("¿Deseas calcular los aranceles para un producto? (S/N): ")
    if result == "S" or result == "s":
        tariff = calculate_tariff(item)
        item["tariff"] = tariff
        send_grey("Los aranceles para el producto ", "")
        send_green(f"{item['id']} ", "")
        send_grey("son de ", "")
        send_yellow(f"{tariff}€")
        input(RETURN_TO_MENU_STR)
        return 1
    else:
        print("¡No has calculado los aranceles!")
        input(RETURN_TO_MENU_STR)
        return 0