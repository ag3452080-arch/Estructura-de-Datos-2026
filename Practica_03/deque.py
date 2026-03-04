from collections import deque

def enque(q:deque, elemento) -> None:
    q.append(elemento)

def dequeue(q:deque) -> int:
    return q.popleft()

def peek(q:deque) -> int:
    return q[0]

def is_empty(q:deque) -> bool:
    return not q

def size(q:deque) -> int:
    return len(q)

def aplicar_retiro(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue(saldos)   
    if historial is not None:
        enque(historial, saldo_original)

    nuevo_saldo = saldo_original - monto
    enque(saldos, nuevo_saldo)

def aplicar_deposito(saldos: deque[int], monto: int, historial: deque[int] | None = None) -> None:
    saldo_original = dequeue(saldos)   
    if historial is not None:
        enque(historial, saldo_original)

    nuevo_saldo = saldo_original + monto
    enque(saldos, nuevo_saldo)


saldos = deque()
historial_retiros = deque(maxlen=5)
historial_depositos = deque(maxlen=5)

for _ in range(5):
    enque(saldos, 1000)

monto_retiro = 500
monto_deposito = 300

for _ in range(5):
    aplicar_retiro(saldos, monto_retiro, historial_retiros)

for _ in range(5):
    aplicar_deposito(saldos, monto_deposito, historial_depositos)

print("Historial (saldos antes del retiro):", list(historial_retiros))
print("Historial (saldos antes del depósito):", list(historial_depositos))
print("Saldos finales:", list(saldos))
