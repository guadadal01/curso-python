#Ejercicio1

resultado = 10 / 2  
print(type(resultado))
#La respuesta es B) Float

#Ejercicio2
"""¿Cuál es el valor de x después de ejecutar este código?"""
x = 17 % 5
#El valor de x es de A) 2

#Ejercio3
"""¿Qué imprime el siguiente programa?"""
for i in range(1, 8):
    if i % 2 == 0:
        print(i)
#Imprime la C) 2,4,6

#Ejercicio4
"""¿Que imprime?"""
frutas = ["manzana", "banana", "naranja", "uva"]
print(frutas[-2])
#Imprime la B) Naranja

#Ejercicio5
"""Explicá con tus palabras cuándo usarías un while y cuándo usarías un for.
Dá un ejemplo concreto de cada uno (no hace falta que funcionen, solo que ilustren la idea)."""

# El while lo usaria cuando no estoy segura de la cantidad de veces que se va a ejecutar un codigo, usando una condicion para la iteracion. En cambio, usaria un for cuando se la cantidad exacta de veces que necesito iterar una/s accion/es

#Ejemplo While
"""quiero leer numeros hasta que el usuario ingrese el numero 3"""
num = int(input("Ingresa un numero: "))
while (num != 3):
    num = int(input("Ingresa un numero: "))
    #Ejemplo For
"""Sumar numeros del 1 al 7"""
suma = 0
for i in range(1,8):
    suma += i 
print(suma)

#Ejercicio6
"""Escribí un programa que le pida al usuario su edad y muestre la categoría correspondiente:
Rango	Categoría
0 – 12	🧒 Niño/a
13 – 17	🎒 Adolescente
18 – 64	🧑 Adulto/a
65 o más	👴 Adulto mayor
Si la edad ingresada es negativa o mayor a 120, mostrá un mensaje de error."""
edad = int(input("Ingrese su edad: "))
if ((edad > 0) and (edad < 120)): 
    if (edad <= 12):
        print("🧒 Niño/a")
    elif (edad >= 13) and (edad <= 17):
        print("🎒 Adolescente")
    elif (edad >= 18) and (edad <= 64):
        print("🧑 Adulto/a")
    else:
        print("👴 Adulto mayor")
else:
    print ("Error")
    
#Ejercicio7
"""Escribí un programa que le pida números al usuario uno por uno y los vaya sumando. El programa termina cuando el usuario ingresa el número 0. Al final, mostrá la suma total y la cantidad de números que ingresó (sin contar el 0)."""
num = int(input("Ingrese un numero: "))
suma = 0
cont = 0
while (num != 0): 
    suma += num
    cont += 1
    num = int(input("Ingrese un numero: "))
print(f"La suma total es de {suma}")
print(f"La cantidad de numeros que fue ingresado es de {cont}")

#Ejercicio8
"""Calcule el promedio de cada alumno.
Imprima solo los alumnos que aprobaron (promedio ≥ 6), con su nombre y promedio redondeado a 1 decimal.
Imprima el nombre del alumno con el mejor promedio."""
curso = [
    ["Lucía", 7, 8, 9],
    ["Tomás", 4, 3, 5],
    ["Valentina", 10, 9, 8],
    ["Mateo", 6, 5, 7],
    ["Sofía", 2, 4, 3],
]
max= 0.0
for alum in curso:
    alumno = alum[0]
    nota = alum[1:]
    promedio = sum(nota)/len(nota)
    if (promedio >= 6): 
        print(f"Alumno que aprobo: {alumno} y {promedio:.2f}")
    if (promedio > max):
        maxProm = alumno
        max = promedio
print(maxProm)


    


