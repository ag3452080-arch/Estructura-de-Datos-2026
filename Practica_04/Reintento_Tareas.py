from collections import deque

class Tarea:
    def __init__(self, nombre, fallos, intentos):
        self.nombre = nombre
        self.fallos_pendientes = fallos
        self.intentos = intentos

    def __repr__(self):
        return f"{self.nombre}"

bicola = deque([
    Tarea("T1", 1, 0),
    Tarea("T2", 0, 0),
    Tarea("T3", 2, 0),
    Tarea("T4", 1, 0),
    Tarea("T5", 2, 2),
    Tarea("T6", 2, 1)
])

print(f"Estado inicial de la bicola: {list(bicola)}\n")

while bicola:
    tarea_actual = bicola.popleft()
    
    print(f"Procesando {tarea_actual.nombre}")

    if tarea_actual.fallos_pendientes > 0:
        tarea_actual.fallos_pendientes -= 1
        tarea_actual.intentos += 1
        
        bicola.append(tarea_actual)
        print(f"Fallo, reintentos: {tarea_actual.intentos} Lo regresamos al final.")
    else:
        print(f"{tarea_actual.nombre} Completada,sale de la bicola")
    
    print(f"  Bicola actual: {list(bicola)}\n")

