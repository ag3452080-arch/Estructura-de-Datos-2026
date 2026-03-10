#Supon que la politica del sistema permite un maximo de tres peeticiones 
#por cada diez segundos.Si un usuario realiza solicitudes en los segundos
# 0,2,4,6 y 12, las tres primeras quedarian dentro del limite permitido
# La solicitud del segundo 6 seria conflictiva por que todavia existirian
# tres peticiones activas dentro de la misma ventana.Posteriormente 
# al llegar al segundo 12, la peticion mas antigua ya habria salido del 
# intervalo de control, por que el sistema podria aceptar una nueva solicitud.

from collections import deque

def rate_limiter(solicitudes, max_peticiones, tiempo):
    cola_activa = deque(maxlen=max_peticiones)   
    cola_espera = deque()                        
    resultados = []

    for i, segundo in enumerate(solicitudes, start=1):
        while cola_activa and cola_activa[-1][1] <= segundo - tiempo:
            cola_activa.pop()
            if cola_espera:
                pendiente = cola_espera.popleft()
                cola_activa.appendleft(pendiente)
                resultados.append(
                    f"Petición {pendiente[0]} (segundo {pendiente[1]}): "
                    f"Aceptada desde cola de espera: ventana: {[f'{p[0]}' for p in cola_activa]})"
                )

        if len(cola_activa) < max_peticiones:
            cola_activa.appendleft((i, segundo))
            resultados.append(
                f"Petición {i} (segundo {segundo}): Aceptada. "
                f"ventana: {[f'{p[0]}' for p in cola_activa]})"
            )
        else:
            cola_espera.append((i, segundo))
            resultados.append(
                f"Petición {i} (segundo {segundo}): En espera"
            )
    
    return resultados


solicitudes = [0, 2, 4, 6, 12]
max_peticiones = 3
tiempo = 10

for linea in rate_limiter(solicitudes, max_peticiones, tiempo):
    print(linea)
