# 🛃 VIU - Sistema de Gestión Aduanera (CLI) - University project.

Proyecto académico de simulación de un sistema aduanero, desarrollado como aplicación de consola (CLI) en Python. El sistema permite registrar mercancías, calcular aranceles, gestionar incidentes y llevar control del estado de la aduana mediante una interfaz interactiva y modular.

---

## 📦 Funcionalidades principales

- **Registro de mercancías** con información detallada (origen, categoría, valor, peso, etc.)
- **Inspección y estado** de mercancías: pendientes, aprobadas o rechazadas
- **Gestión de incidentes** asociados a mercancías
- **Cálculo automático de aranceles** según reglas aduaneras y categorías
- **Liberación de mercancías** tras aprobación y pago del arancel
- **Visualización del estado del sistema**: estadísticas resumidas
- **Guardar y cargar información** de manera persistente (archivos `.txt`)
- **Interfaz clara y amigable** mediante menú interactivo

---

## Antes de iniciar el proyecto

Antes de iniciar el proyecto, considera las configuraciones:

Puedes y debes configurar las categorías y precios que se cobrará por aranceles. Para ello, crea un archivo `configTasas.txt` en la raíz del proyecto con el siguiente formato:

```
Categoría1:Precio1
Categoría2:Precio2
Categoría3:Precio3
...
```

Considera que el archivo debe tener el mismo nombre que el archivo `configTasas.txt` en la raíz del proyecto.

```bash
Electrónica:15
Ropa:10
Alimentos:5
Productos químicos:20
Otros:12
```
---

## 🧪 Ejecutar el proyecto


Sencillamente ejecuta:
```bash
python main.py
```
o en windows:
```bash
py main.py
```

---

## 🧪 Pruebas con datos simulados (Mock)

Para agilizar las pruebas del sistema, se puede usar el archivo `mock_merchandise.json`, que contiene mercancías precargadas de ejemplo:

```json
{
  "M001": { "description": "Laptop de última generación", "origin": "USA", ... },
  "M002": { "description": "Chaqueta impermeable", "origin": "Alemania", ... },
  ...
}
```

### Cómo usar:

1. Ubica el archivo en la raíz del proyecto o utiliza el mock subido.
2. Esto se escaneará automáticamente y cargará los datos en el sistema. Si no existe solo ignora.

Esto actualizará el sistema con datos de ejemplo listos para luego probarlos en el sistema.

---

## 📁 Estructura del proyecto

```
VIU-aduana/
├── controllers/        # Controladores de cada módulo del menú
├── services/           # Servicios de negocio (cálculo, persistencia)
├── utils/              # Utilidades: limpieza, colores, constantes
├── data/               # Almacenamiento temporal y persistencia (.txt)
├── main_menu.py        # Punto de entrada del menú principal
├── README.md           # Este archivo
```

## 💾 Archivos de datos

El sistema guarda y carga los datos desde archivos `.txt` para persistencia:

- `merchandise.txt`
- `incidents.txt`

Estos pueden ser editados manualmente o manipulados desde el menú 7.
Los datos siguen un formato CSV (separado por punto y coma).

---

## 📌 Requisitos cumplidos

✔️ Proyecto modular  
✔️ Menú CLI con interacción completa  
✔️ Persistencia básica de datos  
✔️ Opcional: uso de `mock_merchandise.json`  
✔️ Cálculo de aranceles  
✔️ Control total del flujo de mercancías e incidentes  

---

## ✍️ Autor

**Alexander Rios**  
Estudiante de Ingeniería Informática
[GitHub: @Flussen](https://github.com/Flussen)
VIU - International University of Valencia.

---

## 🏁 Licencia

Este proyecto es de carácter educativo y libre de uso con fines académicos.