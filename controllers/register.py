"""
Controlador de registro de mercancías.

Este módulo permite al usuario registrar nuevas mercancías en memoria (RAM),
que luego podrán ser inspeccionadas, valoradas y liberadas.

Requiere que la categoría esté previamente registrada.
"""

from models.merchandise import new_merchandise
from utils.cleaner import clear_console
from utils.color import send_blue, send_error, send_grey, send_success, send_yellow
from utils.common import RETURN_BACK_STR
from utils.status import PENDING
from data.memory_storage import merchandise_store
from data.memory_storage import categories_with_tariffs

def register_merchandise():
    """
    Inicia el proceso interactivo de registro de mercancías.

    Solicita los datos al usuario y valida que sean correctos.
    Guarda la mercancía en memoria con estado 'PENDING'.
    
    Returns:
        str: Opción del usuario tras registrar (0 = volver, 1 = nuevo, 2 = listar).
    """
    clear_console()
    send_blue("Menú > 1. Registro Mercancia")
    print(" ")
    send_yellow(">> Registro de una nueva Mercancia")
    identifier = input("ID (mín. 3 carácteres, 0 para salir): ")
    
    if identifier == "0":
        return

    if len(identifier) < 3:
        send_error("Identificador inválido.")
        input(RETURN_BACK_STR)
        register_merchandise()
        return
    
    description = input("Descripción: ")
    origin = input("País de origen: ")
    currency = input("Moneda (USD, EUR, etc.): ")
    category = input("Categoría (Solo se permite categorías registradas): ")
    if category not in categories_with_tariffs:
        send_error("¡La categoría no está registrada!")
        input(RETURN_BACK_STR)
        register_merchandise()
        return

    weight = set_weight_with_exception_handler()
    if weight is None:
        send_error("Peso es None!")
        return
    
    value = set_value_with_exception_handler()
    if value is None:
        send_error("Peso es None!")
        return
    

    new_merch = new_merchandise(identifier, description, origin, value, currency, category, weight, PENDING)

    merchandise_store[new_merch["id"]] = new_merch

    clear_console()
    send_blue("Menú > 1. Registro Mercancia")
    print(" ")
    send_success("Registrado exitosamente")

    
    send_yellow("¿Deseas agregar otro producto?")
    send_grey("0. Volver al menú.")
    send_grey("1. Agregar un nuevo producto.")
    send_grey("2. Listar todos los productos agregados.")

    result = input("(0-2): ")
    return result
        

def set_weight_with_exception_handler():
    """
    Solicita y valida el peso de la mercancía ingresado por el usuario.

    Returns:
        float or None: Peso en kg si es válido, None si hay error.
    """
    try:
        weight = float(input("Peso (kg): "))

        if weight <= 0:
            send_error("el peso debe ser mayor que 0.")
            return set_weight_with_exception_handler()
        
        return weight
    except ValueError:
        send_error("Peso inválido. Usa un número.")
        return set_weight_with_exception_handler()

def set_value_with_exception_handler():
    """
    Solicita y valida el valor declarado de la mercancía.

    Returns:
        float or None: Valor si es válido, None si hay error.
    """
    try:
        value = float(input("Valor declarado: "))
        if value <= 0:
            send_error("El valor debe ser mayor que 0.")
            return set_value_with_exception_handler()
        return value
    except ValueError:
        send_error("Valor inválido. Usa un número.")
        return set_value_with_exception_handler()
    