# Sistema de Gestión de Torneo de Fútbol ⚽  

## Descripción  
Este sistema es una aplicación desarrollada en **Python** que permite gestionar un torneo de fútbol. Incluye funcionalidades para administrar *equipos*, *jugadores*, *árbitros* y *partidos*. Está orientado a facilitar la gestión de eventos deportivos con herramientas de registro, búsqueda y actualización de datos, junto con la generación de reportes.

## Estructura del Proyecto  
```
Proyecto_Futbol/
├── data/                     # Carpeta con los archivos JSON de datos
│   ├── arbitros.json         # Datos de los árbitros
│   ├── equipos.json          # Datos de los equipos
│   ├── jugadores.json        # Datos de los jugadores
│   └── partidos.json         # Datos de los partidos
├── arbitros.py               # Módulo para gestionar los árbitros
├── config.py                 # Configuración del proyecto
├── equipos.py                # Módulo para gestionar los equipos
├── gestion.py                # Lógica general de gestión deportiva
├── jugadores.py              # Módulo para gestionar los jugadores
├── main.py                   # Punto de entrada principal del proyecto
├── partidos.py               # Módulo para gestionar los partidos
├── reportes.py               # Generación de reportes
├── readme.md                 # Documentación del proyecto
└── requirements.txt          # Dependencias del proyecto
```

**---**

## Funcionalidades Principales  

### 1. **Gestión de Equipos**  
- **Registrar equipo:** Nombre, ciudad, director técnico y jugadores.  
- **Buscar equipo:** Por nombre o ID.  
- **Actualizar estadísticas:** Partidos jugados, ganados, empatados, perdidos, goles a favor y en contra.  

### 2. **Gestión de Jugadores**  
- **Registrar jugador:** ID, nombre, número, posición, equipo ID, tarjetas y estadísticas.  
- **Buscar jugador:** Por nombre o ID.  
- **Actualizar estadísticas:** Partidos jugados, goles, asistencias, tarjetas, minutos jugados.  

### 3. **Gestión de Árbitros**  
- **Registrar árbitro:** ID, nombre, categoría, experiencia y partidos dirigidos.  
- **Asignar árbitro:** A un partido específico.  

### 4. **Gestión de Partidos**  
- **Registrar partido:** ID, fecha, árbitro, equipos, alineaciones y resultados.  
- **Actualizar resultados:** Goles y estadísticas de cada equipo.  
- **Registrar eventos:** Minuto, tipo de evento (gol, falta, tarjeta), jugador involucrado.  


### 5. **Generar reportes**
- **Generar reporte de posiciones:** Detalla de las posiciones de los equipos.
- **Generar reporte de goleadores:** Detalle de los goleadores del torneo.
- **Generar reportes árbitros:** Detalle de árbitros y su rendimiento.  

---

## Instalación  
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/usuario/xxxxxx.git
   cd xxxxxx
   ```
2. **Instalar las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Uso  
1. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```
2. **Navegación:** A través del menú principal, puedes acceder a cada sección del sistema (equipos, jugadores, partidos, etc.).

---

## Ejemplo de Código  
Aquí tienes un fragmento de cómo se registraría un equipo de forma manual:

```python
from models.equipo import Equipo
from utils.json_handler import guardar_datos

equipo = Equipo(id=1, nombre="Tigres FC", ciudad="Bogotá", director="Carlos Pérez")
guardar_datos("data/equipos.json", equipo.to_dict())
```

---

## Reportes Disponibles  
- **Tabla de posiciones:** Ordenada por puntos.  
- **Lista de goleadores:** Con el número de goles por jugador.  
- **Estadísticas de equipos:** Comparativa de rendimiento por equipo.  
- **Reportes de árbitros:** Listado y experiencia de los árbitros.  
- **Sanciones activas:** Detalles de sanciones vigentes.  

---

## Tecnologías Utilizadas  
- **Python 3.8+**  
- **JSON:** Almacenamiento de datos.  
- **Git:** Control de versiones.  

---

## Licencia  
Este proyecto está bajo la Licencia MIT. Para más detalles, consulta [LICENSE](LICENSE).  

---

## Contacto  
Desarrollado por xxxxx.
Correo: xxxxxx@example.com  
GitHub: [xxxxx](https://github.com/usuario)  

---

Este `README.md` es una guía completa que organiza toda la información necesaria para tu sistema de gestión de torneo de fútbol. Además, incluye instrucciones claras para la instalación, ejecución y contribuciones, junto con un ejemplo práctico del código que se utilizará.