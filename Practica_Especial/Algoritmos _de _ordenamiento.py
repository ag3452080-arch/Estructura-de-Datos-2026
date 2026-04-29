#Realizamos una implementacion de bubbleSort
#Realizamos una implementacion de SelectionSort
#Realizamos una implementacion de insertionSort
#Realizamos una implementacion de mergesort

import random
listaN = [10, 50, 23, 3, 43, 23, 29, 49, 12, 40]

def bubbleSort(lista):
    n = len(lista) 
    for i in range(n):
        intercambio = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        
        if not intercambio:
            break      
    return lista

bubbleSort(listaN)
#print("Lista ordenada con Bubble Sort:", listaN)

def SelectionSort(listaN):
    n = len(listaN)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if listaN[j] < listaN[min_index]:
                min_index = j
        listaN[i], listaN[min_index] = listaN[min_index], listaN[i]
    return listaN

SelectionSort(listaN)
#print("Lista ordenada lista ordenada con Selection Sort:", listaN)

def insertionSort(listaN):
    n = len(listaN)
    for i in range(1, n):
        valor_actual = listaN[i]
        j = i -1 
        while j >= 0 and valor_actual < listaN[j]:
            listaN[j + 1] = listaN[j]
            j -= 1
        listaN[j + 1] = valor_actual
    return listaN

insertionSort(listaN)
#print("Lista ordenada con Insertion Sort:", listaN)

def mergeSort(listaN):
    if len (listaN) > 1:
        medio = len(listaN) // 2
        izquierda = listaN[:medio]
        derecha = listaN[medio:]
        
        mergeSort(izquierda)
        mergeSort(derecha)
        
        i = j = k = 0
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                listaN[k] = izquierda[i]
                i += 1
            else:
                listaN[k] = derecha[j]
                j += 1
            k += 1
        
        while i < len(izquierda):
            listaN[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            listaN[k] = derecha[j]
            j += 1
            k += 1
    return listaN

mergeSort(listaN)
#print("Lista ordenada con Merge Sort:", listaN)

def quickSort(listaN):
    if len(listaN) <= 1:
        return listaN
    pivote = listaN[len(listaN) // 2]

    izquierda = [x for x in listaN if x < pivote]
    centro = [x for x in listaN if x == pivote]
    derecha = [x for x in listaN if x > pivote]

    return quickSort(izquierda) + centro + quickSort(derecha)

listaN = quickSort(listaN)
#print("Lista ordenada con Quick Sort:", listaN)

def randomQuickSort(listaN):
    if len(listaN) <= 1:
        return listaN
    pivote =  random.choice(listaN)

    izquierda = [x for x in listaN if x < pivote]
    centro = [x for x in listaN if x == pivote]
    derecha = [x for x in listaN if x > pivote]

    return randomQuickSort(izquierda) + centro + randomQuickSort(derecha)

listaN = randomQuickSort(listaN)
#print("Lista ordenada con Quick Sort:", listaN)

def countingSort(listaN):
    if not listaN:
        return []
    
    max_value = max(listaN)
    count = [0] * (max_value + 1)
    output = [0] * len(listaN)  

    for num in listaN:
        count[num] += 1

    for i in range(1, max_value + 1):
        count[i] += count[i - 1]

    for num in listaN:
        output[count[num] - 1] = num
        count[num] -= 1

    return output

listaN = countingSort(listaN)
print("Lista ordenada con Counting Sort:", listaN)






