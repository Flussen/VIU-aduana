# Registro de mercancias. Aquí se crea las mercancias en RAM (diccionario)
# para luego gestionarse en los próximos procesos como inspección.

from models.merchandise import new_merchandise
from utils.cleaner import clear_console
from utils.color import send_blue, send_error, send_grey, send_success, send_yellow
from utils.status import PENDIENTE
from data.memory_storage import merchandise_store

def register_merchandise():
    """
    Función entrada para gestionar el controlador "Register".
    Para registro de mercancias.
    """

    clear_console()
    send_blue("Menú > 1. Registro Mercancia")
    print(" ")
    send_yellow(">> Registro de una nueva Mercancia")
    identifier = input("ID (mín. 3 carácteres): ")

    if len(identifier) < 3:
        send_error("Identificador inválido.")
        register_merchandise()
        return
    
    description = input("Descripción: ")
    origin = input("País de origen: ")
    currency = input("Moneda (USD, EUR, etc.): ")
    category = input("Categoría: ")

    weight = set_weight_with_exception_handler()
    if weight is None:
        send_error("Peso es None!")
        return
    
    value = set_value_with_exception_handler()
    if value is None:
        send_error("Peso es None!")
        return
    

    new_merch = new_merchandise(identifier, description, origin, value, currency, category, weight, PENDIENTE)

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
    Función helper para validar el peso de una mercancia a tipo Float.
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
    Función helper para validar el valor de una mercancia a tipo Float.
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
    