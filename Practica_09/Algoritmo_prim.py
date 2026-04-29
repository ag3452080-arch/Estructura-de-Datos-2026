import heapq

def algoritmo_prim(grafo, inicio):
    
    mst = []                 
    visitados = set()        
    
    
    cola_prioridad = [(0, None, inicio)] 
    
    peso_total = 0

    print(f" Iniciando Prim desde el nodo {inicio}")

    while cola_prioridad:
        peso, u, v = heapq.heappop(cola_prioridad)
        
        if v not in visitados:
            visitados.add(v)
            peso_total += peso
            
            if u is not None:
                mst.append((u, v, peso))
                print(f"Conectando: {u} - {v} con peso {peso}")
            
            for vecino, peso_arista in grafo[v].items():
                if vecino not in visitados:
                    heapq.heappush(cola_prioridad, (peso_arista, v, vecino))
                    
    return mst, peso_total


grafo_imagen = {
    '0': {'2': 20, '1': 10},
    '1': {'0': 10, '4': 10, '3': 50},
    '2': {'0': 20, '4': 33, '3': 20},
    '3': {'1': 50, '2': 20, '4': 20, '5': 2},
    '4': {'2': 33, '1': 10, '3': 20, '5': 1},
    '5': {'4': 1, '3': 2}
}

nodo_inicial = '2'
resultado_mst, total = algoritmo_prim(grafo_imagen, nodo_inicial)

print("Árbol de expansion")
for origen, destino, peso in resultado_mst:
    print(f"Arista: {origen} - {destino} | Peso: {peso}")

print(f"Peso total: {total}")
