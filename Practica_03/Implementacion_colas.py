def enque(elemento, lista):
    lista.append(elemento)

def deque(lista):
    lista.pop(0)

def peek(lista):
    return lista[0] 

def isEmpty(lista):
    if lista == []:
        return True 
    else:
        return False
    
def size (lista):
    return len(lista)

lista = []

print(isEmpty(lista))
enque(1, lista)
print(lista)
print(isEmpty(lista))
deque(lista)
print(isEmpty(lista))
enque(8, lista)
enque(7, lista)
print(peek(lista))
size(lista)
print(size(lista))

