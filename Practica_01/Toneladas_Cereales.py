tonelada_cosecha = [12,24,16,15,20,18,6,10,12,11,14,15,12]
tonelada_cosecha.sort()
print(tonelada_cosecha)

suma_toneladas = 0  
for i in tonelada_cosecha:
    suma_toneladas += i
print("Suma de toneladas: ",suma_toneladas)

promedio_toneladas = suma_toneladas / len(tonelada_cosecha)
print("Promedio de toneladas: ",promedio_toneladas)

for i in tonelada_cosecha:    
    if i > promedio_toneladas:
        print(i)

for i in tonelada_cosecha:
    if i < promedio_toneladas:
        print(i) 