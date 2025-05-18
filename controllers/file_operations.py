from utils.cleaner import clear_console
from utils.color import send_blue, send_yellow, send_error
from data.memory_storage import merchandise_store, incidents

from services.file_service import (
    save_merchandise_to_txt,
    load_merchandise_from_txt,
    save_incidents_to_txt,
    load_incidents_from_txt
)

MERCH_FILE = "data/merchandise.txt"
INCIDENTS_FILE = "data/incidents.txt"

def show_file_operations_menu():
    clear_console()
    send_blue("Menú > 7. Cargar y guardar información")
    print(" ")
    print("1. Guardar datos actuales")
    print("2. Cargar datos desde archivos")
    print("0. Volver al menú")

    choice = input("Seleccione una opción: ").strip()

    if choice == "1":
        save_merchandise_to_txt(MERCH_FILE, merchandise_store)
        save_incidents_to_txt(INCIDENTS_FILE, incidents)

    elif choice == "2":
        loaded_merchandise = load_merchandise_from_txt(MERCH_FILE)
        loaded_incidents = load_incidents_from_txt(INCIDENTS_FILE)

        if isinstance(loaded_merchandise, dict):
            merchandise_store.clear()
            merchandise_store.update(loaded_merchandise)

        if isinstance(loaded_incidents, list):
            incidents.clear()
            incidents.extend(loaded_incidents)

    input("Presiona ENTER para volver al menú...")
