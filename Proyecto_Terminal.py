import tkinter as tk
from tkinter import ttk
import subprocess, sys, os, threading, tempfile, textwrap

# PROGRAMAS 
CATS = [
  { "name": "Arreglos", "items": [
    { "name": "1. Arreglo sin duplicados", "file": "Arreglo_Unidimensional.py", "code": """\
x = [1,2,4,4,5,7,9,10,11,11,13,14,15,16,16]
print("Arreglo original:", x)
y = []
for i in x:
    if i not in y:
        y.append(i)
print("Arreglo sin repetidos:", y)
""" },
    { "name": "2. Cadena de caracteres", "file": "Cadena_Caracteres.py", "code": """\
print("Parte 1: con arreglos")
Cadena = "Parangaricutirimicuaro"
print(Cadena)
minusculas = list("abcdefghijklmnopqrstuvwxyz")
mayusculas = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for i in mayusculas:
    contador = 0
    for j in Cadena:
        if i == j: contador += 1
    if contador > 0:
        print("La letra", i, "aparece", contador, "veces")
for i in minusculas:
    contador = 0
    for j in Cadena:
        if i == j: contador += 1
    if contador > 0:
        print("La letra", i, "aparece", contador, "veces")
print("------------------------------------------------")
print("Parte 2: sin arreglos")
Cadena = "Parangaricutirimicuaro".lower()
a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0
for letra in Cadena:
    if letra=="a": a+=1
    if letra=="c": c+=1
    if letra=="g": g+=1
    if letra=="i": i+=1
    if letra=="m": m+=1
    if letra=="n": n+=1
    if letra=="o": o+=1
    if letra=="p": p+=1
    if letra=="r": r+=1
    if letra=="t": t+=1
    if letra=="u": u+=1
print("a:",a,"| c:",c,"| g:",g,"| i:",i,"| m:",m)
print("n:",n,"| o:",o,"| p:",p,"| r:",r,"| t:",t,"| u:",u)
""" },
    { "name": "3. Calificaciones finales", "file": "Calificaciones_Finales.py", "code": """\
Cal_alumnos = [8,8,7,5,0,9,9,5,6,10]
Cal_alumnos.sort()
print("Calificaciones ordenadas:", Cal_alumnos)
suma = 0
for i in Cal_alumnos: suma += i
promedio = suma / len(Cal_alumnos)
print("Promedio:", promedio)
aprobado = reprobado = 0
for i in Cal_alumnos:
    if i >= 7: aprobado += 1
    else: reprobado += 1
print("Aprobados:", aprobado)
print("Reprobados:", reprobado)
print(f"Porcentaje aprobados: {(aprobado/len(Cal_alumnos))*100:.1f}%")
print(f"Porcentaje reprobados: {(reprobado/len(Cal_alumnos))*100:.1f}%")
""" },
    { "name": "4. Toneladas de cereales", "file": "Toneladas_Cereales.py", "code": """\
tonelada_cosecha = [12,24,16,15,20,18,6,10,12,11,14,15,12]
tonelada_cosecha.sort()
print("Cosecha ordenada:", tonelada_cosecha)
suma = 0
for i in tonelada_cosecha: suma += i
promedio = suma / len(tonelada_cosecha)
print("Suma:", suma, "  Promedio:", promedio)
print("Sobre el promedio:")
for i in tonelada_cosecha:
    if i > promedio: print(" ", i)
print("Bajo el promedio:")
for i in tonelada_cosecha:
    if i < promedio: print(" ", i)
""" },
  ]},
  { "name": "Matrices", "items": [
    { "name": "5. Coordenadas en matriz", "file": "CoordenadasMatrices.py", "code": """\
A = [[4,7,2,9,5,7],[1,3,7,6,8,0],[9,2,5,7,4,6],
     [8,7,1,3,7,2],[5,0,6,4,2,9],[7,8,9,2,1,7]]
coords = []
for i, fila in enumerate(A):
    for j, val in enumerate(fila):
        if val == 7: coords.append((i+1, j+1))
print("Coordenadas del valor 7:", coords)
""" },
    { "name": "6. Multiplicacion de matrices", "file": "Matrices.py", "code": """\
A = [[5,6,13],[3,10,1],[2,11,3]]
B = [[1,2,1],[6,5,15],[3,11,12]]
C = [[0,0,0],[0,0,0],[0,0,0]]
print("Matriz A:"); [print(f) for f in A]
print("Matriz B:"); [print(f) for f in B]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
print("Resultado A x B:"); [print(f) for f in C]
""" },
    { "name": "7. Sala de cine", "file": "SalaMatriz.py", "code": """\
F, C = 6, 6
asientos = [[False]*C for _ in range(F)]
def reservar(i,j):
    if not asientos[i][j]: asientos[i][j]=True; return f"OK: reservado ({i+1},{j+1})"
    return f"RECHAZO: ocupado ({i+1},{j+1})"
def liberar(i,j):
    if asientos[i][j]: asientos[i][j]=False; return f"OK: liberado ({i+1},{j+1})"
    return f"RECHAZO: ya libre ({i+1},{j+1})"
def consultar(i,j):
    return f"Estado ({i+1},{j+1}) = {'reservado' if asientos[i][j] else 'libre'}"
ops = [("RESERVAR",1,1),("RESERVAR",1,2),("RESERVAR",1,1),("CONSULTAR",1,2),
       ("LIBERAR",1,2),("LIBERAR",1,2),("RESERVAR",1,2),("RESERVAR",6,6),
       ("CONSULTAR",6,6),("RESERVAR",2,5)]
for accion,i,j in ops:
    i-=1; j-=1
    if accion=="RESERVAR": print(reservar(i,j))
    elif accion=="LIBERAR": print(liberar(i,j))
    elif accion=="CONSULTAR": print(consultar(i,j))
total = sum(sum(1 for a in fila if a) for fila in asientos)
print("Total reservados:", total)
""" },
    { "name": "8. DataFrame estadistico", "file": "dataframe.py", "code": """\
import math
try:
    import pandas as pd
    df = pd.read_csv("Housing1.csv")
    def media(lst): return sum(lst)/len(lst)
    def varianza(lst): m=media(lst); return sum((x-m)**2 for x in lst)/len(lst)
    def desviacion(lst): return math.sqrt(varianza(lst))
    def moda(lst):
        f={}
        for v in lst: f[v]=f.get(v,0)+1
        mx=max(f.values()); return [k for k,v in f.items() if v==mx]
    for col in ["price","bedrooms","bathrooms","sqft_living","sqft_lot"]:
        lst = list(df[col])
        print(f"Columna: {col}")
        print(f"  Media: {media(lst):.2f}  Varianza: {varianza(lst):.2f}  Desv: {desviacion(lst):.2f}")
        print(f"  Moda: {moda(lst)[:3]}")
except FileNotFoundError:
    print("ERROR: No se encontro Housing1.csv")
    print("Coloca el archivo en la misma carpeta que este script.")
except ImportError:
    print("ERROR: pandas no esta instalado.")
    print("Ejecuta:  pip install pandas")
""" },
  ]},
  { "name": "Colas", "items": [
    { "name": "9. Implementacion basica de colas", "file": "Implementacion_colas.py", "code": """\
def enque(e, lista): lista.append(e)
def deque(lista): lista.pop(0)
def peek(lista): return lista[0]
def isEmpty(lista): return lista == []
def size(lista): return len(lista)
lista = []
print("Vacia?", isEmpty(lista))
enque(1, lista); print("Lista:", lista)
print("Vacia?", isEmpty(lista))
deque(lista); print("Vacia despues de deque?", isEmpty(lista))
enque(8, lista); enque(7, lista)
print("Peek:", peek(lista))
print("Size:", size(lista))
""" },
    { "name": "10. Terminal de banco", "file": "Terminal_Banco.py", "code": """\
def enque(lista, e): lista.append(e)
def deque(lista, lista2): enque(lista2, lista[0]); lista.pop(0)
def retiros(lista, lista2):
    r = lista[0] - lista2[0]; deque(lista, lista2); enque(lista, r)
def depositos(lista, lista2):
    s = lista[0] + lista2[0]; deque(lista, lista2); enque(lista, s)
saldos=[1000,1000,1000,1000,1000]; retiro=[500]; deposito=[300]
print("Saldos iniciales:", saldos)
for _ in range(5): retiros(saldos, retiro)
print("Despues de retirar:", saldos)
for _ in range(5): depositos(saldos, deposito)
print("Despues de depositar:", saldos)
""" },
    { "name": "11. Bicola (Deque)", "file": "Bicolas.py", "code": """\
class Bicola:
    def __init__(self): self.cola = []
    def enque_front(self, e): self.cola.insert(0, e)
    def enque_back(self, e): self.cola.append(e)
    def dequeue_front(self): return self.cola.pop(0)
    def dequeue_back(self): return self.cola.pop()
    def mostrar(self): return list(self.cola)
def aplicar_retiro(s, m, h=None):
    orig = s.dequeue_front()
    if h: h.enque_back(orig)
    s.enque_back(orig - m)
def aplicar_deposito(s, m, h=None):
    orig = s.dequeue_front()
    if h: h.enque_back(orig)
    s.enque_back(orig + m)
saldos=Bicola(); hr=Bicola(); hd=Bicola()
for _ in range(5): saldos.enque_back(1000)
for _ in range(5): aplicar_retiro(saldos, 500, hr)
for _ in range(5): aplicar_deposito(saldos, 300, hd)
print("Historial retiros:", hr.mostrar())
print("Historial depositos:", hd.mostrar())
print("Saldos finales:", saldos.mostrar())
""" },
    { "name": "12. Cola circular (clase)", "file": "ColaCircular.py", "code": """\
class colaCircular:
    def __init__(self, cap):
        self.capacidad=cap; self.cola=[None]*cap; self.frente=-1; self.final=-1
    def esta_llena(self): return (self.final+1)%self.capacidad==self.frente
    def esta_vacia(self): return self.frente==-1
    def encolar(self, dato):
        if self.esta_llena(): print("Cola llena"); return
        if self.esta_vacia(): self.frente=0; self.final=0
        else: self.final=(self.final+1)%self.capacidad
        self.cola[self.final]=dato
    def desencolar(self):
        if self.esta_vacia(): print("Cola vacia"); return None
        dato=self.cola[self.frente]
        if self.frente==self.final: self.frente=-1; self.final=-1
        else: self.frente=(self.frente+1)%self.capacidad
        return dato
    def mostrar(self):
        if self.esta_vacia(): print("Cola vacia"); return
        i=self.frente; els=[]
        while True:
            els.append(str(self.cola[i]))
            if i==self.final: break
            i=(i+1)%self.capacidad
        print(" -> ".join(els))
cola = colaCircular(5)
for t in ["Turno 1","Turno 2","Turno 3","Turno 4","Turno 5"]: cola.encolar(t)
print("Cola inicial:"); cola.mostrar()
print("Atendido:", cola.desencolar())
print("Atendido:", cola.desencolar())
print("Cola despues:"); cola.mostrar()
cola.encolar("Turno 6"); cola.encolar("Turno 7")
print("Cola final:"); cola.mostrar()
print("Atendido:", cola.desencolar())
""" },
    { "name": "13. Cola circular con tamano", "file": "Colas_Circulares.py", "code": """\
class ColaCircular:
    def __init__(self, cap):
        self.capacidad=cap; self.cola=[None]*cap; self.frente=0; self.final=-1; self.tamano=0
    def enque(self, e):
        if self.tamano==self.capacidad: raise OverflowError("Cola llena")
        self.final=(self.final+1)%self.capacidad; self.cola[self.final]=e; self.tamano+=1
    def dequeue(self):
        if self.tamano==0: raise IndexError("Cola vacia")
        e=self.cola[self.frente]; self.cola[self.frente]=None
        self.frente=(self.frente+1)%self.capacidad; self.tamano-=1; return e
    def mostrar(self):
        els=[]; idx=self.frente
        for _ in range(self.tamano): els.append(self.cola[idx]); idx=(idx+1)%self.capacidad
        return els
def aplicar_retiro(s,m,h=None):
    orig=s.dequeue()
    if h: h.enque(orig)
    s.enque(orig-m)
def aplicar_deposito(s,m,h=None):
    orig=s.dequeue()
    if h: h.enque(orig)
    s.enque(orig+m)
saldos=ColaCircular(5); hr=ColaCircular(5); hd=ColaCircular(5)
for _ in range(5): saldos.enque(1000)
for _ in range(5): aplicar_retiro(saldos,500,hr)
for _ in range(5): aplicar_deposito(saldos,300,hd)
print("Historial retiros:", hr.mostrar())
print("Historial depositos:", hd.mostrar())
print("Saldos finales:", saldos.mostrar())
""" },
    { "name": "14. Deque (collections)", "file": "deque.py", "code": """\
from collections import deque
def enque(q, e): q.append(e)
def dequeue(q): return q.popleft()
def peek(q): return q[0]
def is_empty(q): return not q
def size(q): return len(q)
def aplicar_retiro(s,m,h=None):
    orig=dequeue(s)
    if h: enque(h,orig)
    enque(s,orig-m)
def aplicar_deposito(s,m,h=None):
    orig=dequeue(s)
    if h: enque(h,orig)
    enque(s,orig+m)
saldos=deque(); hr=deque(maxlen=5); hd=deque(maxlen=5)
for _ in range(5): enque(saldos,1000)
for _ in range(5): aplicar_retiro(saldos,500,hr)
for _ in range(5): aplicar_deposito(saldos,300,hd)
print("Historial retiros:", list(hr))
print("Historial depositos:", list(hd))
print("Saldos finales:", list(saldos))
""" },
    { "name": "15. Rate Limiting", "file": "Rate_Limiting.py", "code": """\
from collections import deque
def rate_limiter(solicitudes, max_pet, tiempo):
    activa=deque(maxlen=max_pet); espera=deque(); res=[]
    for i, seg in enumerate(solicitudes, 1):
        while activa and activa[-1][1] <= seg-tiempo:
            activa.pop()
            if espera:
                p=espera.popleft(); activa.appendleft(p)
                res.append(f"Peticion {p[0]} (s{p[1]}): Aceptada desde espera -> ventana:{[x[0] for x in activa]}")
        if len(activa) < max_pet:
            activa.appendleft((i,seg))
            res.append(f"Peticion {i} (s{seg}): Aceptada -> ventana:{[x[0] for x in activa]}")
        else:
            espera.append((i,seg))
            res.append(f"Peticion {i} (s{seg}): En espera")
    return res
for linea in rate_limiter([0,2,4,6,12], 3, 10):
    print(linea)
""" },
    { "name": "16. Reintento de tareas", "file": "Reintento_Tareas.py", "code": """\
from collections import deque
class Tarea:
    def __init__(self, nombre, fallos, intentos):
        self.nombre=nombre; self.fallos_pendientes=fallos; self.intentos=intentos
    def __repr__(self): return self.nombre
bicola = deque([
    Tarea("T1",1,0),Tarea("T2",0,0),Tarea("T3",2,0),
    Tarea("T4",1,0),Tarea("T5",2,2),Tarea("T6",2,1)
])
print("Estado inicial:", list(bicola))
print()
while bicola:
    t = bicola.popleft()
    print(f"Procesando {t.nombre}")
    if t.fallos_pendientes > 0:
        t.fallos_pendientes -= 1; t.intentos += 1
        bicola.append(t)
        print(f"  Fallo, intento #{t.intentos} -> regresa al final")
    else:
        print(f"  {t.nombre} completada")
    print(f"  Bicola: {list(bicola)}")
    print()
""" },
  ]},
  { "name": "Pilas", "items": [
    { "name": "17. Clase Pila", "file": "Clase_Pila.py", "code": """\
class Pila:
    def __init__(self): self.pila=[]; self.top=-1
    def push(self, dato): self.pila.append(dato); self.top+=1
    def pop(self):
        if self.is_empty(): return None
        self.top-=1; return self.pila.pop()
    def peek(self):
        if self.is_empty(): return None
        return self.pila[self.top]
    def is_empty(self): return self.top==-1
    def size(self): return self.top+1
pila=Pila()
pila.push(1); pila.push(2); pila.push(3)
print("Cima:", pila.peek())
print("Tamano:", pila.size())
print("Pop:", pila.pop())
print("Tamano despues:", pila.size())
print("Vacia?", pila.is_empty())
""" },
    { "name": "18. Dulces en pila", "file": "Dulces_Pila.py", "code": """\
class Pila:
    def __init__(self): self.pila=[]; self.top=-1
    def push(self, dato):
        self.pila.append(dato); self.top+=1
        print(f"Push: {dato:.2f} -> Pila: {[f'{x:.2f}' for x in self.pila]}")
    def pop(self):
        if self.is_empty(): return None
        self.top-=1; return self.pila.pop()
    def peek(self): return self.pila[self.top] if not self.is_empty() else None
    def is_empty(self): return self.top==-1
    def size(self): return self.top+1
dulces = [12500.5,11890.0,13010.35,14100.0,13650.8,
          14999.99,15800.0,16250.25,15120.0,14780.4,13999.0,15550.75]
pila=Pila()
for v in sorted(dulces): pila.push(v)
print("\nCima:", pila.peek())
print("Tamano:", pila.size())
print("Pop:", pila.pop())
print("Tamano despues:", pila.size())
print("Vacia?", pila.is_empty())
""" },
  ]},
  { "name": "Arboles", "items": [
    { "name": "19. Arbol binario de busqueda", "file": "Arbol_Binario_B.py", "code": """\
import json
class NodoArbol:
    def __init__(self, clave, valor, izq=None, der=None, padre=None):
        self.clave=clave; self.cargaUtil=valor
        self.hijoIzquierdo=izq; self.hijoDerecho=der; self.padre=padre
    def tieneHijoIzquierdo(self): return self.hijoIzquierdo
    def tieneHijoDerecho(self): return self.hijoDerecho
def insertar(nodo, clave):
    if clave < nodo.clave:
        if nodo.tieneHijoIzquierdo(): insertar(nodo.hijoIzquierdo, clave)
        else: nodo.hijoIzquierdo=NodoArbol(clave,f"Valor {clave}",padre=nodo)
    elif clave > nodo.clave:
        if nodo.tieneHijoDerecho(): insertar(nodo.hijoDerecho, clave)
        else: nodo.hijoDerecho=NodoArbol(clave,f"Valor {clave}",padre=nodo)
def gen_dict(n):
    if not n: return None
    return {"clave":n.clave,"izq":gen_dict(n.hijoIzquierdo),"der":gen_dict(n.hijoDerecho)}
def inorden(n, lst):
    if n: inorden(n.hijoIzquierdo,lst); lst.append(n.clave); inorden(n.hijoDerecho,lst)
entrada=[1,13,11,5,9,10,1,12,3,6]
raiz=NodoArbol(entrada[0],f"Valor {entrada[0]}")
for e in entrada[1:]: insertar(raiz,e)
print("Lista original:", entrada)
print("\nDiccionario del arbol:")
print(json.dumps(gen_dict(raiz), indent=2))
res=[]; inorden(raiz,res)
print("\nInorden (ordenado sin repetidos):", res)
""" },
    { "name": "20. Recorridos de arbol", "file": "Eje_AborlesBin.py", "code": """\
class Nodo:
    def __init__(self, dato): self.dato=dato; self.izquierda=None; self.derecha=None
    def agregar(self, lista):
        for d in lista: self._rec(self, d)
    def _rec(self, nodo, dato):
        if dato==nodo.dato: return
        if dato < nodo.dato:
            if nodo.izquierda is None: nodo.izquierda=Nodo(dato)
            else: self._rec(nodo.izquierda, dato)
        else:
            if nodo.derecha is None: nodo.derecha=Nodo(dato)
            else: self._rec(nodo.derecha, dato)
def preorden(n):
    if n: print(n.dato, end=", "); preorden(n.izquierda); preorden(n.derecha)
def inorden(n):
    if n: inorden(n.izquierda); print(n.dato, end=", "); inorden(n.derecha)
def postorden(n):
    if n: postorden(n.izquierda); postorden(n.derecha); print(n.dato, end=", ")
elementos=[3,1,4,2,5]
raiz=Nodo(elementos[0]); raiz.agregar(elementos)
print("Preorden:  ", end=""); preorden(raiz); print()
print("Inorden:   ", end=""); inorden(raiz); print()
print("Postorden: ", end=""); postorden(raiz); print()
""" },
  ]},
  { "name": "Grafos", "items": [
    { "name": "21. BFS - Busqueda en anchura", "file": "Grafo.py", "code": """\
from collections import deque
def bfs(grafo, inicio):
    visitados=[]; cola=deque()
    print(f"Inicio: Cola={list(cola)}, Visitados={visitados}\n")
    cola.append(inicio); visitados.append(inicio)
    print(f"Nodo origen '{inicio}' agregado.")
    print(f"Cola: {list(cola)}, Visitados: {visitados}\n")
    while cola:
        actual=cola.popleft()
        print(f"Procesando: {actual}")
        agregados=[]
        for vecino in grafo[actual]:
            if vecino not in visitados:
                visitados.append(vecino); cola.append(vecino); agregados.append(vecino)
        if agregados: print(f"  Agregados: {agregados}")
        print(f"  Cola: {list(cola)}")
        print(f"  Visitados: {visitados}\n")
grafo={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[]}
bfs(grafo,'A')
""" },
    { "name": "22. Dijkstra - Caminos minimos", "file": "Grafos2.py", "code": """\
import heapq
def dijkstra(grafo, inicio):
    dist={n:float('inf') for n in grafo}; dist[inicio]=0
    prev={n:None for n in grafo}; pq=[(0,inicio)]
    while pq:
        d,u=heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in grafo[u].items():
            nd=d+w
            if nd<dist[v]: dist[v]=nd; prev[v]=u; heapq.heappush(pq,(nd,v))
    return dist,prev
grafo={0:{1:9,4:6},1:{0:9,3:8},2:{4:5,5:6},3:{1:8,5:1,7:7},
       4:{0:6,2:5,6:3},5:{2:6,3:1},6:{4:3,7:2},7:{3:7,6:2}}
dist,prev=dijkstra(grafo,0)
print(f"{'Nodo':<6} | {'Costo':<6} | Camino")
print("-"*28)
for n in sorted(dist):
    camino=[]; cur=n
    while cur is not None: camino.append(str(cur)); cur=prev[cur]
    print(f"{n:<6} | {dist[n]:<6} | {' -> '.join(reversed(camino))}")
""" },
    { "name": "23. Algoritmo de Prim", "file": "Algoritmo_prim.py", "code": """\
import heapq
def prim(grafo, inicio):
    mst=[]; visitados=set(); pq=[(0,None,inicio)]; total=0
    print(f"Iniciando Prim desde nodo {inicio}\n")
    while pq:
        peso,u,v=heapq.heappop(pq)
        if v in visitados: continue
        visitados.add(v); total+=peso
        if u is not None:
            mst.append((u,v,peso)); print(f"Conectando: {u} -- {v}  peso={peso}")
        for vecino,p in grafo[v].items():
            if vecino not in visitados: heapq.heappush(pq,(p,v,vecino))
    return mst,total
grafo={'0':{'2':20,'1':10},'1':{'0':10,'4':10,'3':50},
       '2':{'0':20,'4':33,'3':20},'3':{'1':50,'2':20,'4':20,'5':2},
       '4':{'2':33,'1':10,'3':20,'5':1},'5':{'4':1,'3':2}}
mst,total=prim(grafo,'2')
print("\nArbol de Expansion Minima:")
for u,v,p in mst: print(f"  {u} -- {v}  peso={p}")
print(f"Peso total: {total}")
""" },
  ]},
  { "name": "Ordenamiento", "items": [
    { "name": "24. Bubble Sort", "file": "BubbleSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN[:])
def bubbleSort(lista):
    n=len(lista)
    for i in range(n):
        cambio=False
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]: lista[j],lista[j+1]=lista[j+1],lista[j]; cambio=True
        if not cambio: break
    return lista
print("Bubble Sort:", bubbleSort(listaN[:]))
""" },
    { "name": "25. Selection Sort", "file": "SelectionSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN[:])
def selectionSort(lista):
    n=len(lista)
    for i in range(n):
        m=i
        for j in range(i+1,n):
            if lista[j]<lista[m]: m=j
        lista[i],lista[m]=lista[m],lista[i]
    return lista
print("Selection Sort:", selectionSort(listaN[:]))
""" },
    { "name": "26. Insertion Sort", "file": "InsertionSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN[:])
def insertionSort(lista):
    for i in range(1,len(lista)):
        val=lista[i]; j=i-1
        while j>=0 and val<lista[j]: lista[j+1]=lista[j]; j-=1
        lista[j+1]=val
    return lista
print("Insertion Sort:", insertionSort(listaN[:]))
""" },
    { "name": "27. Merge Sort", "file": "MergeSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN[:])
def mergeSort(lista):
    if len(lista)>1:
        mid=len(lista)//2
        L=lista[:mid]; R=lista[mid:]
        mergeSort(L); mergeSort(R)
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]: lista[k]=L[i]; i+=1
            else: lista[k]=R[j]; j+=1
            k+=1
        while i<len(L): lista[k]=L[i]; i+=1; k+=1
        while j<len(R): lista[k]=R[j]; j+=1; k+=1
    return lista
print("Merge Sort:", mergeSort(listaN[:]))
""" },
    { "name": "28. Quick Sort", "file": "QuickSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN)
def quickSort(lista):
    if len(lista)<=1: return lista
    p=lista[len(lista)//2]
    return quickSort([x for x in lista if x<p])+[x for x in lista if x==p]+quickSort([x for x in lista if x>p])
print("Quick Sort:", quickSort(listaN))
""" },
    { "name": "29. Random Quick Sort", "file": "RandomQuickSort.py", "code": """\
import random
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN)
def randomQuickSort(lista):
    if len(lista)<=1: return lista
    p=random.choice(lista)
    return randomQuickSort([x for x in lista if x<p])+[x for x in lista if x==p]+randomQuickSort([x for x in lista if x>p])
print("Random Quick Sort:", randomQuickSort(listaN))
""" },
    { "name": "30. Counting Sort", "file": "CountingSort.py", "code": """\
listaN=[10,50,23,3,43,23,29,49,12,40]
print("Lista original:", listaN)
def countingSort(lista):
    if not lista: return []
    mx=max(lista); count=[0]*(mx+1); output=[0]*len(lista)
    for n in lista: count[n]+=1
    for i in range(1,mx+1): count[i]+=count[i-1]
    for n in lista: output[count[n]-1]=n; count[n]-=1
    return output
print("Counting Sort:", countingSort(listaN))
""" },
  ]},
  { "name": "Recursion", "items": [
    { "name": "31. Torres de Hanoi", "file": "torres_de_hanoi.py", "code": (
        "def hanoi(n, origen, destino, auxiliar):\n"
        "    if n > 0:\n"
        "        hanoi(n-1, origen, auxiliar, destino)\n"
        "        print('Disco', n, ':', origen, '->', destino)\n"
        "        hanoi(n-1, auxiliar, destino, origen)\n"
        "n = 4\n"
        "movimientos = 2**n - 1\n"
        "print('Torres de Hanoi con', n, 'discos (', movimientos, 'movimientos:')\n"
        "print()\n"
        "hanoi(n, 'A', 'C', 'B')\n"
    ) }
  ]},
]

# INTERFAZ
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructuras de Datos - Menu de Programas")
        self.root.geometry("900x600")
        self.root.resizable(True, True)
        self.selected = None
        self.process  = None
        self.running  = False
        self._build()

    def _build(self):
        left = tk.Frame(self.root, width=280, bd=1, relief=tk.SUNKEN)
        left.pack(side=tk.LEFT, fill=tk.Y, padx=4, pady=4)
        left.pack_propagate(False)

        tk.Label(left, text="Programas", font=("Arial", 11, "bold"),
                 pady=6).pack(fill=tk.X)
        tk.Frame(left, height=1, bg="gray").pack(fill=tk.X)

        sb = tk.Scrollbar(left, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(left, yscrollcommand=sb.set, font=("Arial", 10),
                                  activestyle="dotbox", selectbackground="#4a90d9",
                                  selectforeground="white", bd=0, highlightthickness=0)
        sb.config(command=self.listbox.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        self.items_flat = []
        for cat in CATS:
            self.listbox.insert(tk.END, f"  -- {cat['name']} --")
            self.listbox.itemconfig(tk.END, fg="gray", selectbackground="#ccc",
                                    selectforeground="gray")
            for item in cat["items"]:
                self.listbox.insert(tk.END, f"  {item['name']}")
                self.items_flat.append(item)

        right = tk.Frame(self.root)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,4), pady=4)

        top = tk.Frame(right)
        top.pack(fill=tk.X, pady=(0,4))

        self.lbl_prog = tk.Label(top, text="Selecciona un programa de la lista",
                                 font=("Arial", 10), anchor=tk.W, wraplength=450, justify=tk.LEFT)
        self.lbl_prog.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.btn_run = tk.Button(top, text="Ejecutar", width=10, state=tk.DISABLED,
                                 bg="#4a90d9", fg="white", font=("Arial", 10, "bold"),
                                 relief=tk.RAISED, command=self._run)
        self.btn_run.pack(side=tk.RIGHT, padx=(4,0))

        self.btn_stop = tk.Button(top, text="Detener", width=10, state=tk.DISABLED,
                                  bg="#e05c4a", fg="white", font=("Arial", 10),
                                  relief=tk.RAISED, command=self._stop)
        self.btn_stop.pack(side=tk.RIGHT, padx=4)

        self.btn_clear = tk.Button(top, text="Limpiar", width=10,
                                   font=("Arial", 10), relief=tk.RAISED,
                                   command=self._clear)
        self.btn_clear.pack(side=tk.RIGHT)

        tk.Label(right, text="Salida:", font=("Arial", 9), anchor=tk.W).pack(fill=tk.X)

        frame_txt = tk.Frame(right, bd=1, relief=tk.SUNKEN)
        frame_txt.pack(fill=tk.BOTH, expand=True)
        scy = tk.Scrollbar(frame_txt)
        scy.pack(side=tk.RIGHT, fill=tk.Y)
        self.output = tk.Text(frame_txt, font=("Courier", 10), state=tk.DISABLED,
                              bg="black", fg="white", yscrollcommand=scy.set,
                              wrap=tk.WORD, padx=6, pady=6)
        scy.config(command=self.output.yview)
        self.output.pack(fill=tk.BOTH, expand=True)

        self.status = tk.Label(right, text="Listo.", anchor=tk.W,
                               font=("Arial", 9), fg="gray")
        self.status.pack(fill=tk.X, pady=(2,0))

        self._print("Bienvenido. Elige un programa de la lista y presiona Ejecutar.\n")

    def _on_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        text = self.listbox.get(idx)
        if text.strip().startswith("--"):
            self.listbox.selection_clear(0, tk.END)
            return
        count = 0
        for cat in CATS:
            for item in cat["items"]:
                name_in_list = f"  {item['name']}"
                if self.listbox.get(idx) == name_in_list:
                    self.selected = item
                    self.lbl_prog.config(text=f"{item['name']}  ({item['file']})")
                    self.btn_run.config(state=tk.NORMAL)
                    return

    def _print(self, text):
        self.output.config(state=tk.NORMAL)
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.output.config(state=tk.DISABLED)

    def _clear(self):
        self.output.config(state=tk.NORMAL)
        self.output.delete("1.0", tk.END)
        self.output.config(state=tk.DISABLED)

    def _run(self):
        if not self.selected or self.running:
            return
        self._clear()
        item = self.selected
        self._print(f">>> Ejecutando: {item['file']}\n")
        self._print("-" * 50 + "\n")

        tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.py',
                                         delete=False, encoding='utf-8')
        tmp.write(textwrap.dedent(item["code"]))
        tmp.close()
        self._tmpfile = tmp.name

        self.running = True
        self.btn_run.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)
        self.status.config(text=f"Ejecutando {item['file']}...", fg="blue")

        threading.Thread(target=self._exec, args=(tmp.name,), daemon=True).start()

    def _exec(self, path):
        try:
            self.process = subprocess.Popen(
                [sys.executable, "-u", path],
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                text=True, bufsize=1
            )
            for line in self.process.stdout:
                self.root.after(0, self._print, line)
            self.process.wait()
            code = self.process.returncode
            self.root.after(0, self._done, code)
        except Exception as e:
            self.root.after(0, self._print, f"\nError: {e}\n")
            self.root.after(0, self._done, -1)
        finally:
            try: os.unlink(path)
            except: pass

    def _done(self, code):
        self.running = False
        self.process = None
        self._print("-" * 50 + "\n")
        if code == 0:
            self._print("Programa terminado correctamente.\n")
            self.status.config(text="Listo.", fg="gray")
        else:
            self._print(f"Programa terminado con codigo {code}.\n")
            self.status.config(text=f"Termino con error (codigo {code}).", fg="red")
        self.btn_run.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)

    def _stop(self):
        if self.process:
            try: self.process.terminate()
            except: pass
        if self.running:
            self.running = False
            self._print("\n[Detenido por el usuario]\n")
            self.btn_run.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.DISABLED)
            self.status.config(text="Detenido.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()