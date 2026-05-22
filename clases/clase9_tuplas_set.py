#Ejercicio 1
"""Creá una tupla llamada cumpleanios con tu día, mes y año de nacimiento.
Imprimí la tupla completa.
Imprimí el año por separado usando un índice.
Desempaquetala en tres variables (dia, mes, anio) e imprimí cada una. """
birthday = 13,12,2005
print(birthday)
print(birthday[-1])
dia, mes, anio = birthday
print(f"dia: {dia}, mes: {mes} y año: {anio}")

#Ejercicio 2
"""Que imprime cada cosa"""
a = (42)
b = (42,)
c = ()
d = tuple([42])

print(type(a), type(b), type(c), type(d)) #a imprime int, b imprime tupla, c imprime tupla, b imprime tupla
print(len(b), len(c), len(d)) #1, 0, 1

#Ejercicio 3
"""Tenés una lista de IPs que se conectaron a un servidor (con repetidos). Usá un set para obtener cuántas IPs
distintas se conectaron."""

ips = [
    "192.168.0.1", "10.0.0.5", "192.168.0.1", "172.16.0.2",
    "10.0.0.5", "192.168.0.1", "8.8.8.8", "172.16.0.2"
]
ips_sin_repetidos = set(ips)
diferentes = (len(ips_sin_repetidos))
print(f"las ips sin repetir que se conectaron fueron {ips_sin_repetidos} y se conectaron {diferentes} ips diferentes")


#Ejercicio4
"""Dado el siguiente listado de números, calculá el mínimo, máximo, promedio y cantidad de pares. Guardá 
los cuatro resultados en una tupla llamada resultado, desempaquetala en cuatro variables e imprimí cada una."""
numeros = [3, 7, 2, 8, 5, 4, 9]
minimo = min(numeros)
maximo = max(numeros)
promedio = sum(numeros)/len(numeros)
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
resultado = (minimo, maximo, promedio, pares)
mini, maxa, prom, par = resultado 
print (f"El maximo es {maxa}, el minimo es {mini}, el promedio es {prom:.2f}, y los pares son {par}")

#Ejercicio 5
"""¿Qué lenguaje conocen los tres?
¿Qué lenguajes conoce al menos uno de ellos?
¿Qué lenguajes solo Cami conoce (que no sepan ni Ana ni Beto)?
¿Qué lenguajes saben Ana y Cami pero no Beto?"""
ana    = {"Python", "JavaScript", "Rust"}
beto   = {"Python", "Java", "C++"}
cami   = {"Python", "JavaScript", "Go", "Rust"}
todos = ana & beto & cami
print(todos)
al_menos_uno = ana | beto | cami
print (al_menos_uno)
solo_cami = cami - ana - beto
print (solo_cami)
cami_y_ana = (ana & cami) - beto
print(cami_y_ana)


#Ejercicio 6
"""Tenés una lista de tuplas (producto, precio, stock).
Imprimí solo los productos que tengan stock > 0 y precio menor a 1000."""
inventario = [
    ("Laptop", 1500, 3),
    ("Mouse", 250, 0),
    ("Teclado", 800, 5),
    ("Monitor", 950, 2),
    ("Webcam", 600, 0),
    ("Auriculares", 400, 8)
]
print("Productos con precios menor a $1000 y un stock mayor a 0")
for producto, precio, stock in inventario:
    if (precio < 1000) and (stock > 0):
        print (f"{producto}: {stock}, {precio}")
        
#Ejercicio 7
"""Cuente la cantidad de palabras totales.
Cuente la cantidad de palabras únicas (sin repetir).
Encuentre las palabras que aparecen en ambos textos siguientes:"""
texto1 = "el zorro marron salta sobre el perro perezoso el sol brilla"
texto2 = "el perro corre rapido sobre el cesped y el zorro escapa"
t1 = texto1.split()
t2 = texto2.split()
print(f"las palabras totales del texto 1 es de {len(t1)} y del texto 2 es de {len(t2)}")
unicas1  = set(t1)
unicas2 = set (t2)
print (f"la cantidad de palabras unicas en el texto 1 son de {len(unicas1)}")
print (f"la cantidad de palabras unicas en el texto 2 son de {len(unicas2)}")
comunes = unicas1 & unicas2 
print(comunes)

#Ejercicio 8
maxi = [
    ("Daft Punk", "Around the World"),
    ("Aphex Twin", "Xtal"),
    ("Boards of Canada", "Roygbiv"),
    ("Daft Punk", "One More Time")
]
ana = [
    ("Aphex Twin", "Xtal"),
    ("Radiohead", "Idioteque"),
    ("Boards of Canada", "Roygbiv"),
    ("Burial", "Archangel")
]
beto = [
    ("Daft Punk", "Around the World"),
    ("Burial", "Archangel"),
    ("Radiohead", "Idioteque")
]

# Convertimos a sets de tuplas
maxi_set = set(maxi)
ana_set = set(ana)
beto_set = set(beto)

# 1. Canciones únicas en total
todas = maxi_set | ana_set | beto_set
print(f"Canciones únicas en total: {len(todas)}")  # 8

# 2. Canciones en al menos 2 playlists
en_al_menos_dos = (maxi_set & ana_set) | (maxi_set & beto_set) | (ana_set & beto_set)
print(f"En al menos 2 playlists: {en_al_menos_dos}")
# {('Daft Punk', 'Around the World'), ('Aphex Twin', 'Xtal'),
#  ('Boards of Canada', 'Roygbiv'), ('Burial', 'Archangel'),
#  ('Radiohead', 'Idioteque')}

# 3. Artistas distintos por usuario (¡con set comprehension!)
artistas_maxi = {artista for artista, cancion in maxi}
artistas_ana  = {artista for artista, cancion in ana}
artistas_beto = {artista for artista, cancion in beto}

print(f"Maxi escucha {len(artistas_maxi)} artistas")  # 3
print(f"Ana escucha {len(artistas_ana)} artistas")    # 4
print(f"Beto escucha {len(artistas_beto)} artistas")  # 3

# 4. Artistas que escuchan los tres
en_los_tres = artistas_maxi & artistas_ana & artistas_beto
print(f"Artistas que los tres escuchan: {en_los_tres}")
# set() → ¡ninguno!