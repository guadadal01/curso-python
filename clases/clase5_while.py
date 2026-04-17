#Ejercicio1
"""Escribí un programa que imprima los números del 1 al 10 usando while. """
num = 1
while num <= 10:
    print (num)
    num += 1

#Ejercicio2
"""Escribí un programa que imprima la cuenta regresiva del 10 al 1 y al final imprima "¡Despegue!"."""
num = 10
while num >= 1:
    print (num)
    num -= 1
print ("despegue!")

#Ejercicio3
"""Pedile al usuario un número y mostrá todos los números pares desde 0 hasta ese número."""

num = int(input("Ingrese un numero: "))
cont = 0
while cont <= num:
    print (cont)
    cont += 2

#Ejercicio4
"""Escribí un programa que sume todos los números del 1 al 100 e imprima el resultado.
Resultado esperado: 5050"""

i = 1
suma = 0
while i <= 100:
    suma += i
    i += 1
print (suma)

#Ejercicio5
"""Pedile números al usuario hasta que ingrese un 0. Al final, mostrá cuántos números ingresó (sin contar el 0) y la suma de todos ellos."""

numero = int(input("Ingrese un numero: "))
cant = 0 
suma = 0

while numero != 0:
    cant += 1
    suma = suma + numero
    numero = int(input("Ingrese un numero: "))
print (suma)
print (cant)

#Ejercicio6
"""Simulá un cajero automático simple: el usuario empieza con $1000 de saldo. En cada iteración le preguntás cuánto quiere retirar. El programa termina cuando el saldo llega a 0 o el usuario ingresa un monto mayor al saldo disponible. """

total = 1000

while total > 0:
    print(f"Su saldo disponible es de: ${total}")
    saldo = int(input("Ingrese cuanto quiere retirar: "))
    if saldo > total:
        print ("Saldo insficiente")
        break
    total -= saldo
    print (f"Saldo restante: {total}")

#Ejercicio7
"""Implementá el juego "Adiviná el número": el programa elige un número fijo entre 1 y 100 (podés hardcodearlo), y el usuario tiene que adivinarlo. En cada intento le decís si el número secreto es mayor o menor. Contá cuántos intentos necesitó. """

numero = int (input("Adivina el numero del 1 al 100: "))
numSecreto = 5

while numSecreto != numero:
    if numSecreto > numero:
        print("Mas alto!")
        numero = int (input("Adivina el numero del 1 al 100: "))
    else:
        print ("Mas bajo!!")
        numero = int (input("Adivina el numero del 1 al 100: "))
print ("Lo encontraste!")

#Ejercicio8
"""Pedile al usuario que ingrese notas (de 0 a 10) hasta que ingrese -1. Al final mostrá: - La cantidad de notas ingresadas - El promedio - La nota más alta y la más baja"""
nota = int (input("Ingrese una nota: "))
cantIng = 0
max = -1
min = 11
suma = 0
promedio = 0.0 
while nota != -1:
    cantIng += 1
    suma = nota + suma
    if nota > max:
        max = nota
    if nota < min:
        min = nota 
    nota = int (input("Ingrese una nota: "))
promedio = suma / cantIng
print (f"La cantidad de notas ingresadas son: {cantIng}")
print (f"El promedio es {promedio}")
print (f"La nota mas alta es {max} y la nota mas baja es {min}")