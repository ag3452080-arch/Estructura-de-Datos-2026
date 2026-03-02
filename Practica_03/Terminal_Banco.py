#crear una pequeña terminal donde se utilice el enque,peek,size,deque,isEmpty 
#Se debe ralizar tres colas
# para simular una terminal de banco 
#se debe presentar 5 personas con un retiro de 500 pesos y un deposito de 300 pesos
# se debe presentar el saldo de cada persona despues de cada operacion
#En el enque se debe presentar su saldo, retiro,deposito
#A cada persona se le asigna un saldo inicial de 1000 pesos
#Se debe generar al final el slado de cada perosna despues de las 5 operaciones

def enque(elemento, lista):
    lista.append(elemento)

def deque(lista):
    if not isEmpty(lista):
        return lista.pop(0)

def peek(lista):
    return lista[0]

def isEmpty(lista):
    return lista == []

def size(lista):
    return len(lista)

def retiro(saldo, cantidad):
    return saldo - cantidad

def depositar(saldo, deposito):
    return saldo + deposito


saldos = [] 
enque(1000, saldos) 
enque(1000, saldos) 
enque(1000, saldos) 
enque(1000, saldos) 
enque(1000, saldos)
print("Saldo inicial de cada persona:", saldos)

saldos[0] = depositar(retiro(saldos[0], 500), 300) 
saldos[1] = depositar(retiro(saldos[1], 500), 300) 
saldos[2] = depositar(retiro(saldos[2], 500), 300) 
saldos[3] = depositar(retiro(saldos[3], 500), 300) 
saldos[4] = depositar(retiro(saldos[4], 500), 300)

print("Saldo después de la primera operación:", saldos)