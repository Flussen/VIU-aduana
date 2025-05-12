from utils.color import send_blue, send_error, send_grey, send_success, send_yellow
from utils.common import RETURN_TO_MENU_STR
from utils.status import APPROVED
from data.memory_storage import merchandise_store
import os

RELEASED_ITEMS_FILE = "released_items.txt"


def show_release_menu():
    send_yellow("-- Productos pendientes de liberación --")
    pending_release = [
        (id, data) for id, data in merchandise_store.items()
        if data["status"] == APPROVED and data.get("tariff", 0) > 0
    ]
        
    if not pending_release:
        send_yellow("No hay productos listos para ser liberados.")
        input(RETURN_TO_MENU_STR)
        return 0
    
    for id, data in pending_release:
        send_yellow(f"{id}", end="")
        send_grey(": " + data["description"] + " - ", end="")
        send_blue(f"{data['status']}", end="")
        send_grey(" - ", end="")
        send_blue(f"{data['tariff']}€")
        print("")

    selected = input("Ingresa el ID de la mercancía a liberar (M123) o 'none' para salir: ").strip()

    for id, data in pending_release:
        if id == selected:
            r = input(f"¿Estás seguro que deseas liberar el producto {id}? (0 - No | 1 - Sí): ").strip()
            if r == "1":
                release_item(data)
                return 1
            else:
                return 0
    send_error("¡No existe esa mercancía o no está lista para liberar!")
    input(RETURN_TO_MENU_STR)
    return 0

def release_item(item):
    if item["status"] == APPROVED and item.get("tariff", 0) > 0:
        try:
            file_exists = os.path.exists(RELEASED_ITEMS_FILE)
            with open(RELEASED_ITEMS_FILE, 'a', encoding='utf-8') as file:
                if not file_exists:
                    file.write(f"{'ID':<8} {'Descripción':<30} {'Origen':<15} {'Valor':<10} {'Moneda':<8} {'Categoría':<20} {'Peso':<8} {'Arancel':<8}\n")
                    file.write("=" * 120 + "\n")
                file.write(f"{item['id']:<8} {item['description']:<30} {item['origin']:<15} {item['value']:<10.2f} {item['currency']:<8} {item['category']:<20} {item['weight']:<8.2f} {item['tariff']:<8.2f}\n")


        except Exception as e:
            send_error(f"Error al registrar la mercancía liberada: {e}")
            input(RETURN_TO_MENU_STR)
            return
        item_id = item["id"]
        del merchandise_store[item["id"]]

        send_success(f"¡Producto {item_id} liberado y registrado exitosamente!")
        input(RETURN_TO_MENU_STR)
    else:
        send_error("¡No se puede liberar el producto! No se ha aprobado o no tiene tarifa calculada.")
        input(RETURN_TO_MENU_STR)