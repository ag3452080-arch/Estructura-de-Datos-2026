#Construccion y analisis de un arbol binario de busqueda 
#  Dada la secuencia de numeros (...), se debe escribir paso a paso
#  como se insertaria cada elemento en un ABB, respetando la propedad clave
#  los valores menores al nodo van a la izquierda y lo mayores a la derecha.
# [1,13,11,5,9,10,1,12,3,6]
# Utilizando un diccionarion

import json

class NodoArbol:
    def __init__(self, clave, valor, izquierdo=None, derecho=None, padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self, clave, valor, hizq, hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

def insertar_paso_a_paso(nodo_actual, nueva_clave):
    if nueva_clave < nodo_actual.clave:
        if nodo_actual.tieneHijoIzquierdo():
            insertar_paso_a_paso(nodo_actual.hijoIzquierdo, nueva_clave)
        else:
            nodo_actual.hijoIzquierdo = NodoArbol(nueva_clave, f"Valor {nueva_clave}", padre=nodo_actual)
    
    elif nueva_clave > nodo_actual.clave:
        if nodo_actual.tieneHijoDerecho():
            insertar_paso_a_paso(nodo_actual.hijoDerecho, nueva_clave)
        else:
            nodo_actual.hijoDerecho = NodoArbol(nueva_clave, f"Valor {nueva_clave}", padre=nodo_actual)
    

def generar_diccionario(nodo):
    if not nodo: return None
    return {
        "clave": nodo.clave,
        "izq": generar_diccionario(nodo.hijoIzquierdo),
        "der": generar_diccionario(nodo.hijoDerecho)
    }

def obtener_ordenado(nodo, lista):
    if nodo:
        obtener_ordenado(nodo.hijoIzquierdo, lista)
        lista.append(nodo.clave)
        obtener_ordenado(nodo.hijoDerecho, lista)

lista_entrada = [1, 13, 11, 5, 9, 10, 1, 12, 3, 6]
raiz = NodoArbol(lista_entrada[0], f"Valor {lista_entrada[0]}") 

for elemento in lista_entrada[1:]: 
    insertar_paso_a_paso(raiz, elemento)

print(f"Lista Original: {lista_entrada}")
print("\nDiccionario del Árbol :")
print(json.dumps(generar_diccionario(raiz), indent=4))

lista_final = []
obtener_ordenado(raiz, lista_final)
print(f"\nLista Final, Ordenada y sin repetidos: {lista_final}")