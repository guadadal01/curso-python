# BLOQUE1
#Ejercicio1
"""Dada la lista numeros = [3, 7, 2, 9, 4, 11, 6], imprimí cada número multiplicado por 2 usando un for."""
numeros = [3, 7, 2, 9, 4, 11, 6] 
for n in numeros:
    print(n*2)

#Ejercicio2
"""Dada puntajes = [85, 42, 91, 77, 33, 60, 99, 12], encontrá el mayor y el menor valor sin usar max() ni min() (queremos entender el algoritmo). """
puntajes = [85, 42, 91, 77, 33, 60, 99, 12]
max = puntajes [0]
min = puntajes [0]
for i in range(1,len(puntajes)):
    if puntajes[i] > max : max = puntajes [i]
    if puntajes[i] < min : min = puntajes[i]
print(f"El maximo es: {max} y el minimo es: {min}")

#Ejercicio3
"""creá una nueva lista con las palabras que tengan más de 4 letras, usando un for clásico (todavía no comprehensions)."""
palabras = ["sol", "luna", "estrella", "mar", "cometa", "nube"]
cuatro_palabras = []
for palab in palabras:
    if len(palab) > 4: 
        cuatro_palabras.append(palab)
print (cuatro_palabras)

#Ejercicio4
"""calculá la suma total de la lista sin usar sum()"""
nums = [12, 5, 8, 21, 3, 17]
suma = 0
for n in nums:
    suma += n
print(suma)

#Ejercicio5
"""Dada con_repetidos = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6], creá una nueva lista sin elementos duplicados, conservando el orden de aparición. Usá solo lo que sabemos de listas (todavía no vimos set())."""

con_repetidos = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
sin_elem_dup = []
for elem in con_repetidos:
    if elem not in sin_elem_dup:
        sin_elem_dup.append(elem)
print(con_repetidos)
print(sin_elem_dup)

#BLOQUE2
#Ejercicio1
"""Reescribilo como list comprehension"""
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
triples = [n*3 for n in numeros]
print(triples)

#Ejercicio2
"""Dada numeros = list(range(1, 21)) (los números del 1 al 20), generá con una sola línea de comprehension una lista con solo los pares."""
numeros = list(range(1,21))
pares = [num for num in numeros if num % 2 == 0]
print (pares)

#Ejercicio3
"""Generá una lista con los cuadrados de los números pares del 1 al 15, en una sola comprehension."""
cuadrado = [n**2 for n in range(1,16) if n % 2 == 0 ]
print(cuadrado)

#Ejercicio4
"""
Generá una lista con la longitud de cada palabra usando comprehension.
Generá una lista con las palabras en mayúsculas (usá .upper()).
Generá una lista con las palabras que tengan más de 3 letras, en mayúsculas.
"""
palabras = ["python", "es", "un", "lenguaje", "increíble"]
long = [len(p) for p in palabras]
mayuscula = [p.upper() for p in palabras]
mas_tres = [p for p in mayuscula if len(p) > 3]
print (long)
print (mayuscula)
print (mas_tres)

#Ejercicio5
notas = [4, 7, 9, 2, 6, 8, 5, 10, 3]
ap_desap = ["Aprobado" if n >= 6 else "Desaprobado" for n in notas] #OPERADOR TERNARIOS, if/else
print (ap_desap)

#Ejercicio6
"""
Una lista con todas las palabras (usá frase.split()). Una lista con las palabras que empiezan con vocal (usá palabra[0].lower() in "aeiou"). Una lista con la primera letra de cada palabra."""

frase = "El zorro marrón salta sobre el perro perezoso"
palabras = frase.split()
vocal = [p for p in palabras if p[0].lower() in "aeiou"]
primera_letra = [p[0] for p in palabras]
print(palabras)
print(vocal)
print(primera_letra)

#BLOQUE3
#Ejercicio1
"""Imprimí el elemento del centro (debería ser 50), accediendo con doble índice."""
grilla = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(grilla [1][1])

#Ejercicio2
"""Dada la misma grilla del ejercicio anterior, imprimila como tabla, con un espacio entre números y un salto de línea al final de cada fila."""
for fila in range(len(grilla)):
    for colum in range (len(grilla)):
        print(grilla[fila][colum], end=" ")
    print()

#Ejercicio3
"""Calculá e imprimí la suma de cada fila."""
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
for i, lista in enumerate(matriz):
    print(f"fila {i} -> {sum(lista)}")

#Ejercicio4
"""Usando la misma matriz del ejercicio anterior, calculá la suma de cada columna."""

for c in range(len(matriz)):
    suma = 0
    for f in range(len(matriz[0])):
        suma += matriz[f][c]
    print(f"Col {c} → {suma}")

#Ejercicio5
"""
Tenemos una lista de alumnos y una matriz de asistencias. Cada fila representa un alumno; cada columna, una clase. El valor 1 significa "asistió" y 0 significa "faltó".
Imprimí el porcentaje de asistencia de cada alumno, redondeado al entero más cercano.
"""
alumnos = ["Ana", "Beto", "Cami", "Dante"]
asistencias = [
    [1, 1, 0, 1, 1],   # Ana
    [0, 1, 1, 1, 0],   # Beto
    [1, 1, 1, 1, 1],   # Cami
    [0, 0, 1, 0, 1],   # Dante
]
for i, alum in enumerate(alumnos):
    fila = asistencias[i]
    porcentaje = round(sum(fila)/len(fila) * 100)
    print(f"{alumnos}: {porcentaje}%")

#BLOQUE4
#Ejercicio1
"""
Imprimir el promedio de cada alumno, con dos decimales, en formato "Ana: 8.00".
Listar los aprobados (promedio ≥ 6) y los desaprobados por separado.
Encontrar al alumno con el mejor promedio e imprimir su nombre y promedio"""
curso = [
    ["Ana", 8, 7, 9],
    ["Beto", 4, 5, 6],
    ["Cami", 10, 9, 10],
    ["Dante", 3, 5, 4],
    ["Eva", 7, 7, 8],
]

