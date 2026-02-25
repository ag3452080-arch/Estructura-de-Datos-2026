A = [
    [4,7,2,9,5,7],
    [1,3,7,6,8,0],
    [9,2,5,7,4,6],
    [8,7,1,3,7,2],
    [5,0,6,4,2,9],
    [7,8,9,2,1,7]
]

listaCoordenadas = []

for i, fila in enumerate(A):
    for j, valor in enumerate(fila):
        if valor == 7:
            listaCoordenadas.append((i+1, j+1))

if listaCoordenadas == []:
    print("No encontrado")
else:
    print(listaCoordenadas)
    