#Generar una pila en la que se inserten todos los valores de dulces acomodados
# de menor (se insertan prrimero) a mayor (se insertan la final)

class Pila:
    def __init__(self):
        self.pila = []
        self.top = -1

    def push(self, dato):
        self.pila.append(dato)
        self.top += 1
        print(f"Push: {dato} -> Pila actual: {self.pila}")
    
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


dulces = [12500.5, 11890.0, 13010.35, 14100.0, 13650.8,
          14999.99, 15800.0, 16250.25, 15120.0, 14780.4,
          13999.0, 15550.75]

dulces_ordenados = sorted(dulces)

pila = Pila()

for valor in dulces_ordenados:
    pila.push(valor)

print("\nElemento en la cima:", pila.peek())   
print("Tamaño de la pila:", pila.size())     
print("Pop:", pila.pop())                    
print("Tamaño después de pop:", pila.size()) 
print("¿Está vacía?", pila.is_empty())

