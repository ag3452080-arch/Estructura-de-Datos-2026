class colaCircular:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = -1
        self.final = -1

    def esta_llena(self):
        return (self.final + 1) % self.capacidad == self.frente

    def esta_vacia(self):
        return self.frente == -1

    def encolar(self, dato):
        if self.esta_llena():
            print("La cola está llena")
            return
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            self.final = (self.final + 1) % self.capacidad
        
        self.cola[self.final] = dato
    
    def desencolar(self):
        if self.esta_vacia():
            print("La cola está vacía")
            return None
        dato = self.cola[self.frente]
        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            self.frente = (self.frente + 1) % self.capacidad
        return dato
    
    def ver_frente(self):
            if self.esta_vacia():
                return None
            return self.cola[self.frente]
    
    def mostrar(self):
        if self.esta_vacia():
            print("Cola vacía")
            return
        i = self.frente
        elementos = []
        while True:
            elementos.append(str(self.cola[i]))
            if i == self.final:
                break
            i = (i + 1) % self.capacidad
        print(" -> ".join(elementos))

cola = colaCircular(5)


cola.encolar("Turno 1")
cola.encolar("Turno 2")
cola.encolar("Turno 3")
cola.encolar("Turno 4")
cola.encolar("Turno 5")

cola.mostrar()

print("Atendido:", cola.desencolar())
print("Atendido:", cola.desencolar())

cola.mostrar()

cola.encolar("Turno 6")
cola.encolar("Turno 7")

cola.mostrar()

print ("Atendido:", cola.desencolar())