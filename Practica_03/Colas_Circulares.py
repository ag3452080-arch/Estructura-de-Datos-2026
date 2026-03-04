class ColaCircular:
    def __init__(self, capacidad:int):
        self.capacidad = capacidad
        self.cola = [None] * capacidad
        self.frente = 0
        self.final = -1
        self.tamano = 0

    def enque(self, elemento:int) -> None:
        if self.tamano == self.capacidad:
            raise OverflowError("Cola circular llena")
        self.final = (self.final + 1) % self.capacidad
        self.cola[self.final] = elemento
        self.tamano += 1

    def dequeue(self) -> int:
        if self.tamano == 0:
            raise IndexError("Cola circular vacía")
        elemento = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.capacidad
        self.tamano -= 1
        return elemento

    def peek(self) -> int:
        if self.tamano == 0:
            raise IndexError("Cola circular vacía")
        return self.cola[self.frente]

    def is_empty(self) -> bool:
        return self.tamano == 0

    def size(self) -> int:
        return self.tamano

    def mostrar(self) -> list:
        elementos = []
        idx = self.frente
        for _ in range(self.tamano):
            elementos.append(self.cola[idx])
            idx = (idx + 1) % self.capacidad
        return elementos


def aplicar_retiro(saldos: ColaCircular, monto: int, historial: ColaCircular | None = None) -> None:
    saldo_original = saldos.dequeue()
    if historial is not None:
        historial.enque(saldo_original)

    nuevo_saldo = saldo_original - monto
    saldos.enque(nuevo_saldo)

def aplicar_deposito(saldos: ColaCircular, monto: int, historial: ColaCircular | None = None) -> None:
    saldo_original = saldos.dequeue()
    if historial is not None:
        historial.enque(saldo_original)

    nuevo_saldo = saldo_original + monto
    saldos.enque(nuevo_saldo)


saldos = ColaCircular(5)
historial_retiros = ColaCircular(5)
historial_depositos = ColaCircular(5)

for _ in range(5):
    saldos.enque(1000)

monto_retiro = 500
monto_deposito = 300

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_retiros)

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_depositos)

print("Historial (saldos antes del retiro):", historial_retiros.mostrar())
print("Historial (saldos antes del depósito):", historial_depositos.mostrar())
print("Saldos finales:", saldos.mostrar())
