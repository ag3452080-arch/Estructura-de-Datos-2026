#En lugar de usar un solo dato vas a recibir toda la lista
#Nuestra raiz debe ser 3, lo cual la funcion debe leer el valor y compararlo con la raiz 
#Mandar llamar a recursivo y darel la lista
#En lugar de un solo dato, vamos a recibir una lista y cada elemento debe pasar por un pase de comparacion, dentro de un bucle.
#Los elementos menores a la raiz van a la izquierda y la mayores a la derecha.
# La lista debe estar dentro de la funcion agregar para llamar a recursivo

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    def agregar(self, lista_elementos):
        for dato in lista_elementos:
            self.__agregar_recursivo(self, dato)

    def __agregar_recursivo(self, nodo, dato):
        if dato == nodo.dato:
            return

        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

def preorden(nodo):
    if nodo:
        print(nodo.dato, end=", ")
        if nodo.izquierda is None and nodo.derecha is not None:
            print("None", end=", ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.dato, end=", ")
        if nodo.dato == 3 and nodo.derecha:
            print("None", end=", ")
        inorden(nodo.derecha)

def postorden(nodo):
    if nodo:
        if nodo.izquierda is None and nodo.derecha is not None:
            print("None", end=", ")
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.dato, end=", ")

elementos = [3, 1, 4, 2, 5]
raiz = Nodo(elementos[0])
raiz.agregar(elementos)

print("Preorden: ", end=""); preorden(raiz)
print("\nInorden:  ", end=""); inorden(raiz)
print("\nPostorden:", end=""); postorden(raiz)