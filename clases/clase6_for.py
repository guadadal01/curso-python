"""
# Imprimir del 1 al 5
for i in range(1, 6):
    print(i)
# Contar de 2 en 2
for i in range(0, 11, 2):
    print(i)
"""
#Ejercicio1
"""Escribí un programa que imprima los números del 1 al 10 usando for.
for i in range (1, 11):
    print (i)
"""
#Ejercicio2
"""Escribí un programa que imprima solo los números pares entre 1 y 20.
Pista: usá el tercer parámetro de range().
for i in range (2, 21, 2):
    print (i)
"""
#Ejercicio3
"""Pedile al usuario su nombre e imprimí cada letra en una línea distinta.
nombre = input("Ingrese su nombre: ")
for letra in nombre:
    print (letra)
"""
#Ejercicio4
"""Escribí un programa que sume todos los números del 1 al 100 e imprima el resultado.
Resultado esperado: 5050
suma = 0
for i in range (1, 101):
    suma += i 
print (suma)
"""
#Ejercicio5
"""Pedile al usuario un número n y calculá su factorial usando for.
Ejemplo: factorial de 5 = 5 . 4 . 3 . 2 . 1 = 120
n = int(input("Ingrese un numero: "))
factorial = 1
for i in range (1, n+1):
    factorial *= i
print (factorial)
"""
#Ejercicio6
"""Mostrá la tabla de multiplicar de un número que ingrese el usuario (del 1 al 10).
numero = int(input("Ingrese un numero del 1 al 10: "))
mult = 1
for i in range (1, 11):
    mult = numero * i
    print (f"{numero} . {i} = {mult}")
"""
#Ejercicio7
"""Pedile al usuario que ingrese 5 notas (una por vez, usando for) y al final mostrá el promedio.
suma = 0
cant = 1
for i in range (1,6):
    nota = int(input("Ingrese su nota: "))
    suma += nota 
print (f"Su promedio es {suma/5}")
"""
#Ejercicio8
"""Imprimí un triángulo de asteriscos de n filas, donde n lo ingresa el usuario.
*
**
***
****
Pista: vas a necesitar un for dentro de otro for, o bien multiplicar strings."""

asterisco = "*"
filas = int(input("Ingrese cuantas filas quiere que se ejecute: "))
print (asterisco)
for i in range(filas):
    asterisco += "*"
    print (asterisco)