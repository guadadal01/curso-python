#Ejericio1
""" Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo. 
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if(num1 > num2): 
    print (num1 + num2)
    print (num1 - num2)
else:
    print(num1 / num2)
    print (num1 * num2)

#Ejercicio2
""" Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado". 
"""
nota1 = int(input("Ingrese su primer nota:"))
nota2 = int(input("Ingrese su segunda nota:"))
nota3 = int(input("Ingrese su tercer nota:"))
promedio = (nota1 + nota2 + nota3) / 3 

if(promedio >= 7):
    print("Promocionado")
else:
    print("No promocionaste")

#Ejercicio3
""" Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos.
(Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero) 
"""

num = int(input("Ingrese un numero del 1 al 99: "))

if (num > 0):
    if (num < 10):
        print("Es un numero de un digito")
    else: 
        print("Es un numero de dos digitos")
else:
    print("No ingresaste un numero positivo")

#Ejercicio4
""""
Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.
"""

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
if (num1 > num2):
    if (num1 > num3):
        print(num1, "es el mayor")
    else: 
        print (num3, "es el mayor")
elif (num2 > num3):
    print (num2, "es el mayor")
else:
    print (num3,"es el mayor")

#Ejercicio5
"""
Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)
"""
val_entero = int(input("Ingrese su numero: "))

if(val_entero > 0):
    print("Es positivo")
elif (val_entero < 0):
    print("Es negativo")
else:
    print("Es nulo")

#Ejercicio6
"""
Confeccionar un programa que permita cargar un número entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras. Mostrar un mensaje de error si el número de cifras es mayor.
"""
num_positivo = int(input("Ingrese un numero entero positivo: "))

if (num_positivo > 0):
    if(num_positivo < 10):
        print("Tu numero es de un digito")
    elif (num_positivo <100): 
        print("Tu numero es de dos digitos")
    elif(num_positivo < 1000):
        print ("Tu numero es de tres digitos")
    else:
        print("Error")
else:
    print("no ingreso un numero positivo")


#Ejercicio7
"""
Un postulante a un empleo, realiza un test de capacitación, se obtuvo la siguiente información: cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contestó correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
	Nivel máximo:	Porcentaje>=90%.
	Nivel medio:	Porcentaje>=75% y <90%.
	Nivel regular:	Porcentaje>=50% y <75%.
	Fuera de nivel:	Porcentaje<50%.
"""
cant_realizadas = int(input("Ingrese la cantidad de preguntas que se realizaron: "))
cant_correctas = int(input("Ingrese la cantidad de preguntas acertadas: "))
porcentaje = cant_correctas * 100 / cant_realizadas

if (porcentaje < 90):
    if (porcentaje >= 75):
        print("Conseguiste el nivel medio")
    else:
        if (porcentaje >= 50):
            print("Conseguiste el nivel regular")
        else: 
            print("Fuera de nivel")
else:
    print ("Conseguiste el nivel maximo")