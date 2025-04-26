## Sistema de gestión de Aduadas
## por Alexander Rios para la asignatura de metodología
## de la programación (Programación II) de VIU.
##
## 2025.

from services.config_loader import load_categories, load_merchandise_mock
from services.main_menu import showMenu

def main():
    load_merchandise_mock()
    load_categories()
    showMenu()

if __name__ == "__main__":
    main()