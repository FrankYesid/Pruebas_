import os
import json

import os
import json

def cargar_datos(ruta):
    """Carga datos desde un archivo JSON. Si no existe, crea un archivo vacío."""
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    else:
        print(f"No se encontró {ruta}, creando un archivo vacío.")
        # Crear un archivo vacío JSON
        with open(ruta, 'w') as archivo:
            json.dump([], archivo)  # Escribir una lista vacía en el archivo
        return []

def guardar_datos(ruta, datos):
    """Guarda los datos en un archivo JSON."""
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
