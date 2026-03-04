
from collections import deque

def enque_front(q:deque, elemento) -> None:
    q.appendleft(elemento)   # inserta por el frente

def enque_back(q:deque, elemento) -> None:
    q.append(elemento)       # inserta por el final

def dequeue_front(q:deque) -> int:
    return q.popleft()       # elimina por el frente

def dequeue_back(q:deque) -> int:
    return q.pop()           # elimina por el final

def peek_front(q:deque) -> int:
    return q[0]

def peek_back(q:deque) -> int:
    return q[-1]

def is_empty(q:deque) -> bool:
    return not q

def size(q:deque) -> int:
    return len(q)

def aplicar_retiro(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue_front(saldos)   # retiro desde el frente
    if historial is not None:
        enque_back(historial, saldo_original)

    nuevo_saldo = saldo_original - monto
    enque_back(saldos, nuevo_saldo)          # insertar al final

def aplicar_deposito(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue_front(saldos)   # retiro desde el frente
    if historial is not None:
        enque_back(historial, saldo_original)

    nuevo_saldo = saldo_original + monto
    enque_back(saldos, nuevo_saldo)          # insertar al final


saldos = deque()
historial_retiros = deque(maxlen=5)
historial_depositos = deque(maxlen=5)

for _ in range(5):
    enque_back(saldos, 1000)

monto_retiro = 500
monto_deposito = 300

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_retiros)

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_depositos)

print("Historial (saldos antes del retiro):", list(historial_retiros))
print("Historial (saldos antes del depósito):", list(historial_depositos))
print("Saldos finales:", list(saldos))
