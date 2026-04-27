def hanoi(n, origen, destino, auxiliar):
    if n > 0:
        hanoi(n - 1, origen, auxiliar, destino)
        
        print(f"Disco {n} de {origen} a {destino}\n")
        
        hanoi(n - 1, auxiliar, destino, origen)

numero_de_discos = 5
hanoi(numero_de_discos, 'A', 'C', 'B')