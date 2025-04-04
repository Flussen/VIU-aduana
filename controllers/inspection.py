## Inspección y aprobación de mercancias.

from utils.cleaner import clear_console
from utils.color import send_blue, send_cyan, send_error, send_grey, send_success, send_yellow
from data.memory_storage import merchandise_store
from utils.status import APROBADO, PENDIENTE, RECHAZADO

def inspection_section():
    """
    Función de entrada para gestionar el controlador "Inspection".
    Para inspección y aprobación de mercancias.
    """

    clear_console()
    send_blue("Menú > 2. Inspección y Aprobación")
    print(" ")
    send_yellow(">> Inspección y aprobación de mercancias")
    send_grey("0. Volver al menú.")
    send_grey("1. Listar productos pendientes de inspección.")

    result = input("(0-3): ")
    if result == "0":
        return result
    elif result == "1":
        list_merchandises_to_approve()

def list_merchandises_to_approve():
    clear_console()
    send_yellow("-- Productos pendientes de inspección --")

    pending_items = [
        (id, data) for id, data in merchandise_store.items()
        if data["status"] == PENDIENTE
    ]

    if not pending_items:
        send_yellow("¡No hay mercancias pendientes de inspección!")
        input("\nPulsa ENTER para volver...")
        return
    
    print("")
    for id, data in pending_items:
        send_yellow(f"{id}", end="")
        send_grey(": "+data["description"] + " - ", end="")
        send_blue(data["status"])
    print("")
    selected = input("Ingresa el ID de la mercancia a inspeccionar (M123) o 'none' para salir: ")
    for id, data in pending_items:
        if selected == "none":
            return inspection_section()
        if id == selected:
            clear_console()
            send_yellow(">> Producto:", "")
            send_cyan(" " + id)
            send_grey("Descripción: " + data["description"])
            send_grey("Origen: " + data["origin"])
            send_grey("Valor: " + str(data["value"]))
            send_grey("Categoria: " + data["category"])
            send_grey("Peso: " + str(data["weight"]))
            send_grey("Moneda: " + data["currency"])
            print("")
            send_yellow("¿Deseas aprobar o rechazar este producto?")
            send_grey("0. Volver al menú.")
            send_grey("1. Aprobar.")
            send_grey("2. Rechazar.")
            result = input("(0-2): ")
            if result == "0":
                return
            elif result == "1":
                data["status"] = APROBADO
                send_success("¡Producto aprobado!")
                input("\nPulsa ENTER para volver...")
                return
            elif result == "2":
                data["status"] = RECHAZADO
                send_success("¡Producto rechazado!")
                input("\nPulsa ENTER para volver...")
                return
            break
    else:
        send_error("¡No existe esa mercancia!")
        input("\nPulsa ENTER para volver a intentar...")
        return list_merchandises_to_approve()

def aprove_merchandise():
    pass

def reject_merchandise():
    pass

