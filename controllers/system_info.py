"""
Resumen del estado del sistema aduanero.

Este módulo permite visualizar información general sobre las mercancías registradas
y los incidentes, proporcionando un resumen útil para el usuario.
"""
from utils.cleaner import clear_console
from utils.color import send_blue, send_yellow, send_grey
from data.memory_storage import merchandise_store, incidents
from utils.status import APPROVED, PENDING

def show_system_info():
    """
    Muestra un resumen general del estado del sistema:
    - Cuántas mercancías están pendientes de inspección.
    - Cuántas están aprobadas pero sin pagar arancel.
    - Cuántas están listas para liberar.
    - Cuántos incidentes han sido registrados.
    """
    clear_console()
    send_blue("Menú > 6. Información del sistema")
    print(" ")

    pendientes = sum(1 for _, data in merchandise_store.items() if data["status"] == PENDING)
    aprobadas_sin_pagar = sum(1 for _, data in merchandise_store.items()
                              if data["status"] == APPROVED and not data.get("tariff_paid"))
    listas_para_liberar = sum(1 for _, data in merchandise_store.items()
                              if data["status"] == APPROVED and data.get("tariff", 0) > 0 and data.get("tariff_paid"))
    total_incidentes = len(incidents)

    send_grey("Estado actual del sistema:")
    print(" ")
    send_yellow(f"- Mercancías pendientes de inspección: {pendientes}")
    send_yellow(f"- Mercancías aprobadas sin pagar: {aprobadas_sin_pagar}")
    send_yellow(f"- Mercancías listas para liberar: {listas_para_liberar}")
    send_yellow(f"- Incidentes registrados: {total_incidentes}")
    print(" ")
    input("Pulsa ENTER para volver al menú...")
