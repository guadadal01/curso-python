"""
#Posicion
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])   # manzana
print(frutas[1])   # banana
print(frutas[2])   # naranja
print(frutas[-1])  # naranja  (el último)
print(frutas[-2])  # banana   (el anteúltimo)

#Slicing
sublista usando la notación lista[inicio:fin]. El elemento en la posición fin no se incluye.
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])   # [20, 30, 40]
print(numeros[:3])    # [10, 20, 30]  (desde el inicio)
print(numeros[2:])    # [30, 40, 50]  (hasta el final)
print(numeros[::2])   # [10, 30, 50]  (salta de dos en dos)

#Modificar Listas (son mutables)
frutas = ["manzana", "banana", "naranja"]
frutas[1] = "mango"
print(frutas)  # ["manzana", "mango", "naranja"] 
"""
#Ejercicio 1 — Básico
"""Pedile al usuario 5 números y guardalos en una lista. Luego mostrá el mayor, el menor y la suma."""
lista = []
lista.append(input)
print (sum(lista))
print (max(lista))
print (min(lista))
"""
#Ejercicio 2
mostrala ordenada de menor a mayor sin modificar la original.
lista = [5, 3, 8, 1, 9, 2, 7]
lista.sort()
print(lista)
"""
#remover un numero
lista = [1,2,3,5,6,7,8,9,10]
print (lista)
i = 0
while i < len(lista) and lista[i]!= 40:
    i = i + 1
if i < len(lista): 
    del lista [i]
print(lista)
