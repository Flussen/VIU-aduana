"""
Almacenamiento temporal en memoria para el sistema de aduanas.

Este módulo contiene las estructuras principales que simulan una base de datos,
utilizadas para mantener los datos activos durante la ejecución del programa.
"""

# Diccionario que almacena las mercancías registradas.
# Clave: ID de la mercancía | Valor: diccionario con los datos de la mercancía
merchandise_store = {}

# Lista de incidentes registrados durante el proceso aduanero.
# Cada elemento es un diccionario con ID, descripción y fecha.
incidents = []

# Diccionario que relaciona categorías con sus aranceles (%).
# Clave: nombre de la categoría | Valor: porcentaje de arancel
categories_with_tariffs = {}