# Crear una Clase pila con push, pop, peek, is_empty, size
# Constructores: contengan una lista para la pila, top

class Pila:
    def __init__(self):
        self.pila = []
        self.top = -1


    def push(self, dato):
        self.pila.append(dato)
        self.top +=1
    
    def pop(self):
        if self.is_empty():
            return None
        self.top -= 1
        return self.pila.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        return self.pila[self.top]
    
    def is_empty(self):
        return self.top == -1
    
    def size(self):
        return self.top + 1
    
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)

print("Elemento en la cima:", pila.peek())   
print("Tamaño de la pila:", pila.size())     
print("Pop:", pila.pop())                    
print("Tamaño después de pop:", pila.size()) 
print("¿Está vacía?", pila.is_empty())
