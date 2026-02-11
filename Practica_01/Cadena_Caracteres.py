#Dada una cadena de carecteres como dato, saber el numero de veces que aparecen las letras "a","b"..."z" y "A", "B"..."Z" en dicha cadena.
print("Parte 1: con arreglos")
Cadena = "Parangaricutirimicuaro"
print(Cadena)
minusculas = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


for i in mayusculas:
    contador = 0
    for j in Cadena:
        if i == j:
            contador += 1
    if contador > 0:
        print("La letra ",i," aparece ",contador," veces")

for i in minusculas:
    contador = 0
    for j in Cadena:
        if i == j:
            contador += 1
    if contador > 0:
        print("La letra ",i," aparece ",contador," veces")

print("------------------------------------------------")

print("Parte 2: sin arreglos")
Cadena = "Parangaricutirimicuaro"

Cadena = Cadena.lower()
a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0

for letra in Cadena:
    if letra == "a":
        a += 1
    if letra == "b":
        b += 1
    if letra == "c":
        c += 1
    if letra == "d":
        d += 1
    if letra == "e":
        e += 1
    if letra == "f":
        f += 1
    if letra == "g":
        g += 1
    if letra == "h":
        h += 1
    if letra == "i":
        i += 1
    if letra == "j":
        j += 1
    if letra == "k":
        k += 1
    if letra == "l":
        l += 1
    if letra == "m":
        m += 1
    if letra == "n":
        n += 1
    if letra == "o":
        o += 1
    if letra == "p":
        p += 1
    if letra == "q":
        q += 1
    if letra == "r":
        r += 1
    if letra == "s":
        s += 1
    if letra == "t":
        t += 1
    if letra == "u":
        u += 1
    if letra == "v":
        v += 1
    if letra == "w":
        w += 1
    if letra == "x":
        x += 1
    if letra == "y":
        y += 1
    if letra == "z":
        z += 1

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)
print("g:", g)
print("h:", h)
print("i:", i)
print("j:", j)
print("k:", k)
print("l:", l)
print("m:", m)
print("n:", n)
print("o:", o)
print("p:", p)
print("q:", q)
print("r:", r)
print("s:", s)
print("t:", t)
print("u:", u)
print("v:", v)
print("w:", w)
print("x:", x)
print("y:", y)
print("z:", z)
