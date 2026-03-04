class Bicola:
    def __init__(self):
        self.cola = []

    # Insertar por el frente
    def enque_front(self, elemento):
        self.cola.insert(0, elemento)

    # Insertar por el final
    def enque_back(self, elemento):
        self.cola.append(elemento)

    # Eliminar por el frente 
    def dequeue_front(self):
        if self.is_empty():
            raise IndexError("Bicola vacía")
        return self.cola.pop(0)

    # Eliminar por el final
    def dequeue_back(self):
        if self.is_empty():
            raise IndexError("Bicola vacía")
        return self.cola.pop()

    # Consultar frente
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Bicola vacía")
        return self.cola[0]

    # Consultar final
    def peek_back(self):
        if self.is_empty():
            raise IndexError("Bicola vacía")
        return self.cola[-1]

    def is_empty(self):
        return len(self.cola) == 0

    def size(self):
        return len(self.cola)

    def mostrar(self):
        return list(self.cola)


def aplicar_retiro(saldos: Bicola, monto: int, historial: Bicola | None = None) -> None:
    saldo_original = saldos.dequeue_front()   # retiro desde el frente
    if historial is not None:
        historial.enque_back(saldo_original)

    nuevo_saldo = saldo_original - monto
    saldos.enque_back(nuevo_saldo)            # insertar al final

def aplicar_deposito(saldos: Bicola, monto: int, historial: Bicola | None = None) -> None:
    saldo_original = saldos.dequeue_front()   # retiro desde el frente
    if historial is not None:
        historial.enque_back(saldo_original)

    nuevo_saldo = saldo_original + monto
    saldos.enque_back(nuevo_saldo)            # insertar al final


saldos = Bicola()
historial_retiros = Bicola()
historial_depositos = Bicola()

valores_iniciales = [1000, 1000, 1000, 1000, 1000] 
for v in valores_iniciales: saldos.enque_back(v)

monto_retiro = 500
monto_deposito = 300

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_retiros)

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_depositos)

print("Historial (saldos antes del retiro):", historial_retiros.mostrar())
print("Historial (saldos antes del depósito):", historial_depositos.mostrar())
print("Saldos finales:", saldos.mostrar())
