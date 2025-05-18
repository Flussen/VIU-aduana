"""
Sistema de Gestión de Aduanas - Módulo Principal

Este archivo es el punto de entrada del sistema. Se encarga de cargar 
las categorías y mercancías simuladas, y luego muestra el menú principal 
para interactuar con el usuario.

Autor: Alexander Rios
Asignatura: Metodología de la Programación (Programación II) - VIU
Año: 2025
"""

from services.config_loader import load_categories, load_merchandise_mock
from services.main_menu import showMenu

def main():
    """
    Función principal del programa.

    Carga los datos simulados de mercancías y categorías, y luego 
    inicia el menú principal de interacción con el usuario.
    """
    load_merchandise_mock()
    load_categories()
    showMenu()

if __name__ == "__main__":
    main()