"""
Gestión de incidentes relacionados con mercancías.

Este módulo permite registrar, listar y guardar incidentes relacionados con el proceso aduanero.
Los incidentes quedan almacenados en memoria y pueden persistirse en un archivo de texto.
"""

from datetime import datetime
from data.memory_storage import incidents
from utils.cleaner import clear_console
from utils.color import send_blue, send_cyan, send_error, send_grey, send_success, send_yellow
from utils.common import RETURN_BACK_STR

MERCH = "merch"
DESCRIPTION = "descripcion"
DATE = "fecha"
INCIDENTS_FILE = "incidents.txt"

def new_incident_obj(id, date, description):
    """
    Crea un nuevo diccionario que representa un incidente.

    Args:
        id (str): ID del incidente (ingresado por el usuario).
        date (str): Fecha del incidente.
        description (str): Descripción del incidente.

    Returns:
        dict: Incidente representado como diccionario.
    """
    return {
        MERCH: id,
        DESCRIPTION: description,
        DATE: date
    }

def new_incident():
    """
    Permite al usuario registrar un nuevo incidente.

    Retorna:
        int: 0 si se registró correctamente, 1 si el ID ya existe.
    """
    clear_console()
    send_yellow(">> Registrar nueva incidencia")

    send_grey("Ingresa el ID del incidente (por ej. M123):", end=" ")
    incident_id = input().strip()
    if any(i[MERCH] == incident_id for i in incidents):
        send_error("¡Ese ID de incidente ya existe!")
        input(RETURN_BACK_STR)
        return 1

    send_grey("Ingresa la descripción:", end=" ")
    description = input().strip()

    date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    incidents.append(new_incident_obj(incident_id, date, description))

    clear_console()
    send_success("Incidente registrado correctamente.")
    send_yellow("Para guardar los cambios, selecciona 'Salvar incidentes' en el menú.")
    print(" ")
    input(RETURN_BACK_STR)
    return 0

def list_incidents():
    """
    Lista todos los incidentes registrados en memoria.
    """
    clear_console()
    send_cyan("-- Incidentes --")
    if not incidents:
        send_yellow("No hay incidentes registrados.")
        input(RETURN_BACK_STR)
        return 0

    for incident in incidents:
        send_grey(f"ID: {incident[MERCH]}")
        send_grey(f"Descripción: {incident[DESCRIPTION]}")
        send_grey(f"Fecha: {incident[DATE]}")
        print(" ----------------- ")
    input(RETURN_BACK_STR)
    return 0

def save_incidents():
    """
    Guarda los incidentes registrados en el archivo incidents.txt.

    Returns:
        int: 0 siempre (control de flujo del menú).
    """
    if not incidents:
        send_error("No hay incidentes registrados.")
        input(RETURN_BACK_STR)
        return 0
    try:
        with open(INCIDENTS_FILE, 'w', encoding='utf-8') as file:
            file.write("ID;Descripción;Fecha\n")
            for incident in incidents:
                file.write(f"{incident[MERCH]};{incident[DESCRIPTION]};{incident[DATE]}\n")
    except Exception as e:
        send_error(f"Error al guardar los incidentes: {e}")
        input(RETURN_BACK_STR)
        return 0
    send_success("Incidentes guardados exitosamente.")
    input(RETURN_BACK_STR)
    return 0

def incidents_menu():
    """
    Muestra el menú de gestión de incidentes.

    Opciones:
    - 0: Volver al menú principal.
    - 1: Listar incidentes.
    - 2: Registrar nuevo incidente.
    - 3: Guardar incidentes en archivo.

    Returns:
        int: 0 en todos los casos para mantener el flujo del programa.
    """
    clear_console()
    send_blue("Menú > 5. Registro de incidentes")
    print(" ")
    send_grey("0. Volver al menú.")
    send_grey("1. Listar incidentes.")
    send_grey("2. Registrar nuevo incidente.")
    send_grey("3. Salvar incidentes.")
    choice = input("(0-3): ").strip()

    if choice == "0":
        return 0
    elif choice == "1":
        if list_incidents() == 0:
            incidents_menu()
    elif choice == "2":
        if new_incident() == 0:
            incidents_menu()
    elif choice == "3":
        return save_incidents()
    return 0
