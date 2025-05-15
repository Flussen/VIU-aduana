from data.memory_storage import categories_with_tariffs
from utils.cleaner import clear_console
from utils.color import send_blue, send_cyan, send_error, send_green, send_grey, send_success, send_yellow
from utils.common import RETURN_TO_MENU_STR
from utils.status import APPROVED
from data.memory_storage import merchandise_store
from utils.utils import print_merchandise_info

def calculate_tariff(item):
    return item["value"] * (categories_with_tariffs[item["category"]] / 100)


def list_approved_merchandise():
    return [(item_id, data) for item_id, data in merchandise_store.items()
            if data["status"] == APPROVED and not data.get("tariff")]


def list_merchandise_pending_payment():
    return [(item_id, data) for item_id, data in merchandise_store.items()
            if data["status"] == APPROVED and not data.get("tariff_paid")]


def calculate_tariff_for_merchandise():
    approved_items = list_approved_merchandise()
    if not approved_items:
        send_yellow("¡No hay mercancías aprobadas!")
        input(RETURN_TO_MENU_STR)
        return

    for item_id, data in approved_items:
        send_yellow(f"{item_id}", end="")
        send_grey(": " + data["description"] + " - ", end="")
        send_blue(data["status"])
        print("")

    selected = input("Ingresa el ID de la mercancía a calcular aranceles (M123) o 'none' para salir: ")
    if selected == "none":
        return

    for item_id, data in approved_items:
        if item_id == selected:
            clear_console()
            send_yellow(">> Producto:", "")
            print_merchandise_info(item_id, data)

            send_yellow("¿Deseas calcular los aranceles para este producto?")
            send_grey("0. Volver al menú.")
            send_grey("1. Calcular.")
            confirm = input("(0-1): ")
            if confirm == "1":
                tariff = calculate_tariff(data)
                data["tariff"] = tariff
                send_green(f"Los aranceles para el producto {item_id} son de ", end="")
                send_yellow(f"{tariff}€")

                pay = input("¿Desea pagar el arancel ahora? (0: no, 1: sí): ")
                if pay == "1":
                    data["tariff_paid"] = True
                    send_success("¡Producto pagado!")
                else:
                    send_yellow("El producto queda pendiente de pago.")
                input(RETURN_TO_MENU_STR)
                return
            return
    send_error("¡No existe esa mercancía!")
    input(RETURN_TO_MENU_STR)


def pay_tariff_for_merchandise():
    pending_items = list_merchandise_pending_payment()
    if not pending_items:
        send_yellow("¡No hay mercancías pendientes de pago!")
        input(RETURN_TO_MENU_STR)
        return

    for item_id, data in pending_items:
        send_yellow(f"{item_id}", end="")
        send_grey(": " + data["description"] + " - ", end="")
        send_blue(data["status"])
        send_blue(str(data.get("tariff", "Sin calcular")))
        print("")

    selected = input("Ingresa el ID de la mercancía a pagar el arancel (M123) o 'none' para salir: ")
    if selected == "none":
        return

    for item_id, data in pending_items:
        if item_id == selected:
            clear_console()
            send_yellow(">> Producto:", "")
            print_merchandise_info(item_id, data)

            send_yellow("¿Deseas pagar el arancel para este producto?")
            send_grey("0. Volver al menú.")
            send_grey("1. Pagar.")
            confirm = input("(0-1): ")
            if confirm == "1":
                data["tariff_paid"] = True
                send_success("¡Producto pagado!")
            else:
                send_yellow("Pago cancelado.")
            input(RETURN_TO_MENU_STR)
            return
    send_error("¡No existe esa mercancía!")
    input(RETURN_TO_MENU_STR)

def show_tariff_menu():
    while True:
        clear_console()
        send_blue("Menú > 3. Cálculo de aranceles")
        print(" ")
        send_grey("0. Volver al menú.")
        send_grey("1. Listar productos aprobados y calcular aranceles.")
        send_grey("2. Listar productos pendientes de pago.")
        choice = input("(0-2): ")

        if choice == "1":
            calculate_tariff_for_merchandise()
        elif choice == "2":
            pay_tariff_for_merchandise()
        else:
            break