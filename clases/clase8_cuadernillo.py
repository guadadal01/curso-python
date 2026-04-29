# BLOQUE1
#Ejercicio1
"""Dada la lista numeros = [3, 7, 2, 9, 4, 11, 6], imprimí cada número multiplicado por 2 usando un for.
numeros = [3, 7, 2, 9, 4, 11, 6]
for n in numeros:
    print(n*2)
"""
#Ejercicio2
"""Dada puntajes = [85, 42, 91, 77, 33, 60, 99, 12], encontrá el mayor y el menor valor sin usar max() ni min() (queremos entender el algoritmo).
puntajes = [85, 42, 91, 77, 33, 60, 99, 12]
max = -9999
min = 9999
for p in puntajes:
    if p > max : max = p
    if p < min : min = p
print(f"El maximo es: {max} y el minimo es: {min}")
"""
#Ejercicio3
"""creá una nueva lista con las palabras que tengan más de 4 letras, usando un for clásico (todavía no comprehensions).
palabras = ["sol", "luna", "estrella", "mar", "cometa", "nube"]
cuatro_palabras = []
for palab in palabras:
    if len(palab) > 4: 
        cuatro_palabras.append(palab)
print (cuatro_palabras)
"""
#Ejercicio4
"""calculá la suma total de la lista sin usar sum()
nums = [12, 5, 8, 21, 3, 17]
suma = 0
for n in nums:
    suma += n
print(suma)
"""
