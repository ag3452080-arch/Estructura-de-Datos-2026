# implementacion de un algoritmo que se llama Dijkstra
# Implementacion de la generacion de una tabla 

import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    previos = {nodo: None for nodo in grafo}
    
    cola_prioridad = [(0, inicio)]
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if distancia_actual > distancias[nodo_actual]:
            continue
            
        for vecino, peso in grafo[nodo_actual].items():
            distancia = distancia_actual + peso
            
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                previos[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia, vecino))
                
    return distancias, previos


grafo = {
    0: {1: 9, 4: 6},
    1: {0: 9, 3: 8},
    2: {4: 5, 5: 6},
    3: {1: 8, 5: 1, 7: 7},
    4: {0: 6, 2: 5, 6: 3},
    5: {2: 6, 3: 1},
    6: {4: 3, 7: 2},
    7: {3: 7, 6: 2}
}

distancias, previos = dijkstra(grafo, 0)

print(f"{'Vertex':<8} | {'Cost':<6} | {'Path'}")
print("-" * 25)
for nodo in sorted(distancias.keys()):
    camino = []
    actual = nodo
    while actual is not None:
        camino.append(str(actual))
        actual = previos[actual]
    camino_str = " ".join(reversed(camino))
    
    print(f"{nodo:<8} | {distancias[nodo]:<6} | {camino_str}")