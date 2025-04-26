from data.memory_storage import categories_with_tariffs
from data.memory_storage import merchandise_store
import json
import os

from utils.status import PENDING

def load_categories(filepath='configTasas.txt'):
    with open(filepath, 'r', encoding='utf-8') as archive:
        for line in archive:
            if line.strip():
                category, value = line.strip().split(':')
                categories_with_tariffs[category.strip()] = int(value.strip())

def load_merchandise_mock(filepath='mock_merchandise.json'):
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