from data.memory_storage import categories_with_tariffs
from utils.cleaner import clear_console
from utils.color import send_green, send_grey, send_yellow
from utils.common import RETURN_TO_MENU_STR
from utils.status import APPROVED


def calculate_tariff(item):
    return item["value"] * (categories_with_tariffs[item["category"]] / 100)

def show_tariff_menu():
    clear_console()
    

def show_tariff_menu_2(item):
    clear_console()
    result = input(f"Para aprobar {item['id']}, debe calcularse los aranceles. ¿Continuar? (0-1): ")
    if result == "1":
        tariff = calculate_tariff(item)
        item["status"] = APPROVED
        item["tariff"] = tariff
        send_grey("Los aranceles para el producto ", "")
        send_green(f"{item['id']} ", "")
        send_grey("son de ", "")
        send_yellow(f"{tariff}€")
        input(RETURN_TO_MENU_STR)
        return 1
    else:
        print("¡No has calculado los aranceles, por ende, no se aprobó!")
        input(RETURN_TO_MENU_STR)
        return 0