
from controllers.register import register_merchandise
from utils.color import send_error, send_grey, send_yellow


def showMenu():
    while True:
        send_yellow("\n | Sistema de Aduana  | \n | por Alexander Rios |")
        print("                        ")
        send_grey("1. Registrar mercancia")
        send_grey("2. Inspección y aprobación")
        send_grey("3. Cálculo de aranceles")
        send_grey("4. Liberación de Mercancia")
        send_grey("5. Registro de incidentes")
        send_grey("6. Información del sistema")
        send_grey("7. Gestión de ficheros")
        send_grey("8. Salir.")

        choice = input("Selecciona una opción (1-8): ")

        if choice == "1":
            result = register_merchandise()
            if result == "0":
                continue
            elif result == "1":
                result = register_merchandise()
            break
        elif choice == "2":
            break
        elif choice == "3":
            break
        elif choice == "4":
            break
        elif choice == "5":
            break
        elif choice == "6":
            break
        elif choice == "7":
            break
        elif choice == "8":
            print("Saliendo...")
            break
        else:
            send_error("Invalido, elige una opción valida e intentalo nuevamente.")

    