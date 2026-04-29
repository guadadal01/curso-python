#Posicion
frutas = ["manzana", "banana", "naranja"]

print(frutas[0])   # manzana
print(frutas[1])   # banana
print(frutas[2])   # naranja
print(frutas[-1])  # naranja  (el último)
print(frutas[-2])  # banana   (el anteúltimo)

#Slicing
"""sublista usando la notación lista[inicio:fin]. El elemento en la posición fin no se incluye."""
numeros = [10, 20, 30, 40, 50]

print(numeros[1:4])   # [20, 30, 40]
print(numeros[:3])    # [10, 20, 30]  (desde el inicio)
print(numeros[2:])    # [30, 40, 50]  (hasta el final)
print(numeros[::2])   # [10, 30, 50]  (salta de dos en dos)

#Modificar Listas (son mutables)
frutas = ["manzana", "banana", "naranja"]
frutas[1] = "mango"
print(frutas)  # ["manzana", "mango", "naranja"] 

#Ejercicio 1 — Básico
"""Pedile al usuario 5 números y guardalos en una lista. Luego mostrá el mayor, el menor y la suma."""
lista = []
suma = 0
mayor = -9999
menor = 99999
for i in range(5):
    num = int(input(f"Ingrese un número: "))
    lista.append(num)
    if num < menor : menor = num
    if num > mayor : mayor = num
    suma += num
print(lista)
print(f"El mayor es {mayor} y el menor {menor}")


#Ejercicio 2
"""mostrala ordenada de menor a mayor sin modificar la original."""

lista = [5, 3, 8, 1, 9, 2, 7]
lista2 = sorted(lista) #Diferente sorted y sort
print(lista)
print(lista2)
#NumerosInvertidos para que NO cambie la lista orginial
listaReverse = lista2 [::-1]

#remover un numero
lista = [1,2,3,5,6,7,8,9,10]
print (lista)
i = 0
while i < len(lista) and lista[i]!= 40:
    i = i + 1
if i < len(lista): 
    del lista [i]
print(lista)


#Ejercicio3
"""Creá una lista de 10 números ingresados por el usuario. Luego mostrá solo los que sean mayores que el promedio."""
lista = []
for i in range(10):
    num = int(input("Ingresa numero:"))
    lista.append(num)
promedio = sum(lista) / len(lista)
mayores = [n for n in lista if n > promedio]
print(f"El promedio es: {promedio}")
print (f"los numeros mayores al promedio son: {mayores}")

#Ejercicio4
"""Usando comprensión de listas, generá una lista con los cuadrados de todos los números impares del 1 al 20."""
cuadrados = [n**2 for n in range (1, 21) if n % 2 != 0]
print (cuadrados)

#Ejercicio5
"""Representá una matriz 3×3 con una lista anidada. Calculá la suma de cada fila y mostrala."""
matriz = [
    [1, 2, 3],
    [4, 8, 7],
    [5, 9, 0]
]
suma = 0
for fila in matriz:
    for i in fila:
        suma += i
print(suma)

