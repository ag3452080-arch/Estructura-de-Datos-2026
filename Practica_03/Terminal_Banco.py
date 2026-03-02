#crear una pequeña terminal donde se utilice el enque,peek,size,deque,isEmpty 
#Se debe ralizar tres colas
# para simular una terminal de banco 
#se debe presentar 5 personas con un retiro de 500 pesos y un deposito de 300 pesos
# se debe presentar el saldo de cada persona despues de cada operacion
#En el enque se debe presentar su saldo, retiro,deposito
#A cada persona se le asigna un saldo inicial de 1000 pesos
#Se debe generar al final el slado de cada perosna despues de las 5 operaciones,con el saldo inicial,
#el retiro y el deposito de cada persona

def enque(lista, elemento):
    lista.append(elemento)

def deque(lista, lista2):
    enque(lista2, lista[0])
    lista.pop(0)

def retiros(lista, lista2):
    r = lista[0] - lista2[0]
    deque(lista, lista2)
    enque(lista, r)

def depositos(lista, lista2):
    r = lista[0] + lista2[0]
    deque (lista, lista2)
    enque(lista, r)

def peek(lista):
    return lista[0]

def is_empty(lista):
    return lista == []

def size(lista):
    return len(lista)

saldos   = [1000, 1000, 1000, 1000, 1000]
retiro   = [500]
deposito = [300]

print("Saldos iniciales:", saldos)

retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
retiros(saldos, retiro)
print("Saldos tras retiros:", saldos)

depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
depositos(saldos, deposito)
print("Saldos tras depósitos:", saldos)