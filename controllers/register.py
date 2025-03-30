from utils.cleaner import clear_console
from utils.color import send_error, send_grey, send_success, send_yellow

def register_merchandise():
    """
    Función entrada para gestionar el controlador "Register".
    Para registro de mercancias.
    """

    clear_console()
    send_yellow(">> Registro de nueva Mercancia")
    identifier = input("ID (mín. 3 carácteres):")

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


    clear_console()
    send_success("Registrado exitosamente")
    send_yellow("¿Deseas agregar otro producto?")
    send_grey("0. Volver al menú.")
    send_grey("1. Agregar un nuevo producto.")

    result = input("(0-1): ")
    return result
        

def set_weight_with_exception_handler():
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
    try:
        value = float(input("Valor declarado: "))
        if value <= 0:
            send_error("El valor debe ser mayor que 0.")
            return set_value_with_exception_handler()
        return value
    except ValueError:
        send_error("Valor inválido. Usa un número.")
        return set_value_with_exception_handler()
