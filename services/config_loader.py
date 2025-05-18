"""
Carga de configuración inicial del sistema de aduanas.

Este módulo se encarga de cargar:
1. Las categorías con sus aranceles desde un archivo de configuración.
2. Un conjunto de mercancías simuladas desde un archivo JSON.
"""

from data.memory_storage import categories_with_tariffs
from data.memory_storage import merchandise_store
import json
import os

from utils.status import PENDING

def load_categories(filepath='configTasas.txt'):
    """
    Carga las categorías y sus respectivos aranceles desde un archivo de texto.

    El archivo debe tener el formato:
    Categoría: valor

    Args:
        filepath (str): Ruta al archivo de configuración.
    """
    with open(filepath, 'r', encoding='utf-8') as archive:
        for line in archive:
            if line.strip():
                category, value = line.strip().split(':')
                categories_with_tariffs[category.strip()] = int(value.strip())

def load_merchandise_mock(filepath='mock_merchandise.json'):
    """
    Carga mercancías de prueba desde un archivo JSON.

    Si algún ítem no contiene un estado, se le asigna 'PENDING' por defecto.

    Args:
        filepath (str): Ruta al archivo JSON que contiene las mercancías.
    """
    if not os.path.exists(filepath):
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as archive:
            data = json.load(archive)
            if isinstance(data, dict):
                for key, item in data.items():
                    if "status" not in item:
                        item["status"] = PENDING 
                    merchandise_store[key] = item
            else:
                print("Error: El archivo de mercancías no contiene un diccionario válido.")
    except json.JSONDecodeError:
        print("Error: El archivo JSON de mercancías está mal formado.")
    except Exception as e:
        print(f"Error inesperado al cargar mercancías: {e}")