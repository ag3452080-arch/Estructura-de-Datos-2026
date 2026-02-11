#Dado un arreglo unidimensional de numeros enteros, ordenalos crecientemente, escribe un programa que 
#elimine todos los elementos repetidos.Considere que de haber valores repetidos, estos se encontraran en posiciones
#consecutivas del arreglo.

x = [1,2,4,4,5,7,9,10,11,11,13,14,15,16,16]
print("Arreglo original",x)
y = []
for i in x:
    if i not in y:
        y.append(i)
print("Arreglo sin repetidos",y)
