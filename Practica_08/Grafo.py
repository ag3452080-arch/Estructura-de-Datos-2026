from collections import deque

def bfs(grafo, nodo_inicial):
    visitados = [] 
    cola = deque([]) 
    
    print(f"\nEstado inicial{list(cola)}, Visitados: {visitados}\n")
    
    cola.append(nodo_inicial)
    visitados.append(nodo_inicial)
    print(f"Se agrega el nodo de origen '{nodo_inicial}' a la cola.")
    print(f"Cola: {list(cola)}, Visitados: {visitados}\n")

    while cola:
        nodo_actual = cola.popleft()
        print(f"Nodo procesado {nodo_actual}")

        agregados = []
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.append(vecino) 
                cola.append(vecino)
                agregados.append(vecino)
        
        if agregados:
            print(f"Agregados a la cola: {agregados}")
        
        print(f"Estado de la Cola: {list(cola)}")
        print(f"Lista de Visitados: {visitados}\n")

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bfs(grafo, 'A')