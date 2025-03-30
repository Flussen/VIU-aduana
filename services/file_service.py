import os

from utils.color import send_error, send_info

def save_merchandise_to_txt(filename: str, store: dict):
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