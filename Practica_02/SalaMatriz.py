

F, C = 6, 6
asientos = [[False for _ in range(C)] for _ in range(F)]

def reservar(i, j):
    if not asientos[i][j]:
        asientos[i][j] = True
        return f"OK: reservado ({i+1},{j+1})"
    else:
        return f"RECHAZO: ocupado ({i+1},{j+1})"

def liberar(i, j):
    if asientos[i][j]:
        asientos[i][j] = False
        return f"OK: liberado ({i+1},{j+1})"
    else:
        return f"RECHAZO: ya libre ({i+1},{j+1})"

def consultar(i, j):
    estado = "reservado" if asientos[i][j] else "libre"
    return f"Estado ({i+1},{j+1}) = {estado}"

def resumen_final():
    total_reservados = sum(sum(1 for asiento in fila if asiento) for fila in asientos)
    fila_max = max(range(F), key=lambda f: sum(asientos[f]))
    max_reservados = sum(asientos[fila_max])
    
    print("Total de asientos reservados:", total_reservados)
    print("Fila con más reservados:", fila_max+1, f"({max_reservados})")

operaciones = [
    ("RESERVAR", 1, 1),
    ("RESERVAR", 1, 2),
    ("RESERVAR", 1, 1),
    ("CONSULTAR", 1, 2),
    ("LIBERAR", 1, 2),
    ("LIBERAR", 1, 2),
    ("RESERVAR", 1, 2),
    ("RESERVAR", 6, 6),
    ("CONSULTAR", 6, 6),
    ("RESERVAR", 2, 5)
]

for accion, i, j in operaciones:
    i -= 1  
    j -= 1

    if accion == "RESERVAR":
        print(reservar(i, j))
    elif accion == "LIBERAR":
        print(liberar(i, j))
    elif accion == "CONSULTAR":
        print(consultar(i, j))

    

resumen_final()