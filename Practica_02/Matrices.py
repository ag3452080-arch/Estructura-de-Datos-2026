#Multiplicacion de  matrices
A = [[5, 6, 13],
     [3, 10, 1],
     [2, 11, 3]]

B = [[1, 2, 1],
     [6, 5, 15],
     [3, 11, 12]]

C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C [i][j] += A[i][k] * B[k][j]

for fila in C:
    print(fila)


