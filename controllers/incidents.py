"""
Gestión de incidentes relacionados con mercancías.

Este módulo permite registrar, listar y guardar incidentes relacionados con el proceso aduanero.
Los incidentes quedan almacenados en memoria y pueden persistirse en un archivo de texto.
"""

from datetime import datetime
import os
from data.memory_storage import incidents
from utils.cleaner import clear_console
from utils.color import send_blue, send_cyan, send_error, send_grey, send_success, send_yellow
from utils.common import RETURN_BACK_STR

MERCH = "mercancia"
DESCRIPTION = "descripcion"
DATE = "fecha"
INCIDENTS_FILE = "incidents.txt"

def new_incident_obj(date, merch, description):
    """
    Crea un nuevo diccionario que representa un incidente.

    Args:
        date (str): Fecha del incidente.
        merch (str): ID de la mercancía.
        description (str): Descripción del incidente.

    Returns:
        dict: Incidente representado como diccionario.
    """
    return {
        DATE: date,
        MERCH: merch,
        DESCRIPTION: description
        }
    
def new_incident():
    """
    Permite al usuario registrar un nuevo incidente.

    Retorna:
        int: 0 si se registró correctamente, 1 si el ID ya existe.
    """
    clear_console()
    send_yellow(">> Registrar nueva incidencia de mercancia.")
    send_grey("Ingresa el ID de la mercancia (M123):", end=" ")
    merch = input()
    if merch in incidents:
        send_error("La mercancia ya existe!")
        input(RETURN_BACK_STR)
        return 1
    send_grey("Ingresa la descripción:", end=" ")
    description = input()
    date = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    incidents.append(new_incident_obj(date, merch, description))
    clear_console()
    send_success("Incidente registrado!")
    send_yellow("Para persistir los datos del incidente, vuelva al menú y seleccione salvar incidentes!")
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
        send_grey(f"Mercancia: {incident[MERCH]}")
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
        file_exists = os.path.exists(INCIDENTS_FILE)
        with open(INCIDENTS_FILE, 'w', encoding='utf-8') as file:
            if not file_exists:
                file.write(f"{'ID'};{'Mercancia'};{'Descripción'};{'Fecha'}\n")
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
        int: 0 en todos los casos para mantener el flujo de ejecución.
    """
    clear_console()
    send_blue("Menú > 5. Registro de incidentes")
    print(" ")
    send_grey("0. Volver al menú.")
    send_grey("1. Listar incidentes.")
    send_grey("2. Registrar nuevo incidente.")
    send_grey("3. Salvar incidentes.")
    choice = input("(0-2): ")

    if choice == "0": 
        return 0
    elif choice == "1":
        result = list_incidents()
        if result == 0:
            incidents_menu()
    elif choice == "2":
        result = new_incident()
        if result == 0:
            incidents_menu()
        if result == 1:
            result = new_incident()
    elif choice == "3":
        return save_incidents()
    return 0