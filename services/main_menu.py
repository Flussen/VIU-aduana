"""
Menú principal del sistema de aduanas.

Este módulo define la función `showMenu`, encargada de mostrar
las diferentes secciones del sistema mediante una interfaz sencilla
por consola.
"""
from controllers.incidents import incidents_menu
from controllers.inspection import inspection_section
from controllers.register import register_merchandise
from controllers.release import show_release_menu
from controllers.tariff import show_tariff_menu
from utils.cleaner import clear_console
from utils.color import send_blue, send_error, send_grey, send_yellow
from data.memory_storage import merchandise_store
from controllers.system_info import show_system_info
from controllers.file_operations import show_file_operations_menu



def showMenu():
    """
    Muestra el menú principal del sistema de aduanas.

    Permite al usuario registrar mercancías, inspeccionarlas,
    calcular aranceles, liberarlas, registrar incidentes, ver información
    del sistema y realizar operaciones con ficheros.
    """
    while True:
        clear_console()
        send_yellow("\n | Sistema de Aduana  | \n | por Alexander Rios |")
        print("                        ")
        send_grey("1. Registrar mercancia.")
        send_grey("2. Inspección y aprobación.")
        send_grey("3. Cálculo de aranceles.")
        send_grey("4. Liberación de Mercancia.")
        send_grey("5. Registro de incidentes.")
        send_grey("6. Información del sistema.")
        send_grey("7. Gestión de ficheros.")
        send_grey("8. Salir.")

        choice = input("Selecciona una opción (1-8): ")

        if choice == "1": ## Registro de mercancia
            result = register_merchandise()
            if result == "0":
                continue
            elif result == "1":
                result = register_merchandise()
            elif result == "2":
                clear_console()
                send_blue("Menú > 1. Registro Mercancia")
                print(" ")
                send_yellow("-- Productos recientemente agregados --")
                for id, data in merchandise_store.items():
                    send_yellow(f"{id}: ", end="")
                    send_grey(data["description"])
                input("\nPulsa ENTER para ir al menú...")
                continue
        elif choice == "2": ## Inspección y aprobación
            result = inspection_section()
            if result == "0":
                continue
        elif choice == "3": ## Cálculo de aranceles
            result = show_tariff_menu()
            if result == "0":
                continue
        elif choice == "4": ## Liberación de mercancia
            result = show_release_menu()
            if result == "0":
                continue
        elif choice == "5": ## Registro de incidentes
            result = incidents_menu()
            if result == 0:
                continue
            break
        elif choice == "6": ## Información del sistema
            show_system_info()
            continue
        elif choice == "7": ## Gestión de ficheros
            show_file_operations_menu()
            continue
        elif choice == "8": ## Salir
            print("Saliendo...")
            break
        else:
            clear_console()
            send_error("Invalido, elige una opción valida e intentalo nuevamente.")

