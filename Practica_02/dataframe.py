import pandas as pd 
import math


#Leer el archivo cvsdelimitados por comas (por defecto)
df = pd.read_csv("C:/Users/Hogar/OneDrive/Documentos/Estructura de Datos 2026/Housing1.csv")
#Mostrar las primeras 5 filas
print(df.head())
lista = list(df["price"])

print("Media de Los datos") 
suma = 0
moda = 0
varianza = 0
desviacion = 0
for i in lista:
    suma += i
    if i == moda:
        moda += 1
    else:
        moda = i 
    if i > varianza:
        varianza = i
suma_cuadrados = 0
for i in lista:
    suma_cuadrados += (i - suma / len(lista)) ** 2
varianza = suma_cuadrados / len(lista)
desviacion = varianza ** 0.5

print("La media es: ",suma/len(lista))
print("La moda es: ",df["price"].mode())
print("La varianza es: ",varianza)
print("La desviacion es: ",desviacion)


print("Lo mismo pero ahora con otras mas columnas")

# Lista de columnas 
columnas = ["price","bedrooms","bathrooms","sqft_living","sqft_lot",
            "floors","waterfront","view","condition","grade",
            "sqft_above","sqft_basement","yr_built"]

print("Ahora con funciones ")

def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_moda(lista):
    frecuencias = {}
    for valor in lista:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1
    max_frec = max(frecuencias.values())
    modas = [k for k,v in frecuencias.items() if v == max_frec]
    return modas

def calcular_varianza(lista):
    media = calcular_media(lista)
    suma_cuadrados = sum((x - media) ** 2 for x in lista)
    return suma_cuadrados / len(lista)

def calcular_desviacion(lista):
    return math.sqrt(calcular_varianza(lista))

for col in columnas:
    lista = list(df[col])
    media = calcular_media(lista)
    moda = calcular_moda(lista)
    varianza = calcular_varianza(lista)
    desviacion = calcular_desviacion(lista)

    print(f"Columna: {col}")
    print("  Media:", media)
    print("  Moda:", moda)
    print("  Varianza:", varianza)
    print("  Desviación estándar:", desviacion)
    print("-"*40)