"""
Módulo para gestión de archivos del sistema aduanero.

Incluye funciones para guardar y cargar tanto mercancías como incidentes
desde archivos de texto. Cada línea representa una entrada separada por punto y coma.
"""
import os

from controllers.incidents import DATE, DESCRIPTION, MERCH, new_incident_obj
from utils.color import send_error, send_info

def save_merchandise_to_txt(filename: str, store: dict):
    """
    Guarda las mercancías en un archivo de texto, una por línea.

    Args:
        filename (str): Nombre del archivo destino.
        store (dict): Diccionario con los datos de las mercancías.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for id, data in store.items():
                line = f"{id};{data['description']};{data['origin']};{data['value']};{data['currency']};{data['category']};{data['weight']};{data['status']};{data.get('tariff', '')}\n"
                f.write(line)
        send_info(f"[✓] Datos guardados correctamente en {filename}")
    except Exception as e:
        send_error(f"[✗] Error al guardar los datos: {e}")
        return e

def load_merchandise_from_txt(filename: str) -> dict:
    """
    Carga las mercancías desde un archivo de texto.

    Args:
        filename (str): Ruta del archivo de texto a cargar.

    Returns:
        dict: Diccionario con las mercancías cargadas.
    """
    store = {}

    if not os.path.exists(filename):
        send_error(f"[!] El archivo '{filename}' no existe.")
        return store

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) >= 8:
                    id = parts[0]
                    store[id] = {
                        "description": parts[1],
                        "origin": parts[2],
                        "value": float(parts[3]),
                        "currency": parts[4],
                        "category": parts[5],
                        "weight": float(parts[6]),
                        "status": parts[7],
                        "tariff": float(parts[8]) if len(parts) > 8 and parts[8] else None
                    }
        send_info(f"[✓] Datos cargados correctamente desde {filename}")
    except Exception as e:
        send_error(f"[✗] Error al leer los datos: {e}")
        return e

    return store

def save_incidents_to_txt(filename: str, incident_list: list):
    """
    Guarda una lista de incidentes en un archivo de texto.

    Args:
        filename (str): Nombre del archivo destino.
        incident_list (list): Lista de incidentes, cada uno con 'id', 'mercancia', 'descripcion' y 'fecha'.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("ID;Mercancia;Descripción;Fecha\n")
            for incident in incident_list:
                f.write(f"{incident[MERCH]};{incident[DESCRIPTION]};{incident[DATE]}\n")
        send_info(f"Incidentes guardados correctamente en {filename}")
    except Exception as e:
        send_error(f"Error al guardar los incidentes: {e}")
        return e


def load_incidents_from_txt(filename: str) -> list:
    """
    Carga una lista de incidentes desde un archivo de texto.

    Args:
        filename (str): Ruta del archivo.

    Returns:
        list: Lista de incidentes como diccionarios con 'id', 'mercancia', 'descripcion' y 'fecha'.
    """
    incident_list = []

    if not os.path.exists(filename):
        send_error(f"[!] El archivo '{filename}' no existe.")
        return incident_list

    try:
        with open(filename, "r", encoding="utf-8") as f:
            next(f)
            for line in f:
                parts = line.strip().split(";")
                if len(parts) == 3:
                    incident_list.append(new_incident_obj(parts[0], parts[2], parts[1]))
        if not incident_list:
            send_info("No se encontraron incidentes en el archivo.")
            return incident_list
        send_info(f"Incidentes cargados correctamente desde {filename}")
    except Exception as e:
        send_error(f"Error al leer los incidentes: {e}")
        return e

    return incident_list

