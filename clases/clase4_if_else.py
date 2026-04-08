#Ejercicio1 
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print ("Es mayor de edad")
else:
    print("Es menor de edad")

#Ejercicio2 
numero = int(input("Ingrese un numero: "))
if numero >= 0:
    print ("Es un numero positivo!")
else: 
    print ("Es un numero negativo")

#Ejercicio3 
nota = int(input("Ingrese una nota: "))
if nota >= 6:
    print("Estas aprobado/a")
else:
    print("Estas desaprobado/a")

#Ejercicio4
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))

if numero1 > numero2:
    print("El primer numero es el mayor")
elif numero1 < numero2:
    print("El segundo numero es el mayor")
else: 
    print ("los dos numeros son iguales!")

#Ejercicio5
num = int(input("Ingrese su numero: "))
if (num % 2 == 0):
    print("Tu numero es par")
else: 
    print("Tu numero es impar")

#Ejercicio6
temperatura = int(input("Ingrese una temperatura: "))
if temperatura < 15:
    print("Hace mucho frio!!")
elif temperatura > 30:
    print ("Te  estas asando")
else:
    print("Hace calor")

#Ejercicio7 
contraseña = input ("Ingresa tu contraseña: ")
contraseña2 = input ("Vuelva a ingresar su contraseña: ")

if contraseña2 == contraseña:
    print("tu contraseña es correcta!")
else: 
    print("Tu contraseña es incorrecta")

#Ejercicio8
numero = int(input("Ingrese un numero: "))
if numero > 10:
    print("Tu numero es mayor a 10")
elif numero == 10:
    print ("Tu numero es igual a 10")
else:
    print("Tu numero es menor a 10")

#Ejercicio9
nota1 = int(input("Ingresar su primer nota "))
nota2 = int(input("Ingresar su segunda nota "))
nota3 = int(input("Ingresar su tercer nota "))
promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 8:
    print("Promocionaste!!")
elif promedio >= 6:
    print("Aprobaste!")
else:
    print ("Recupera")

#Ejercicio10
numero = int(input("Ingrese un numero: "))
if numero >= 1 and numero <= 100:
    print("Tu numero esta entre 1 y 100")
elif numero < 1:
    print("Tu numero es menor a 1")
else:
    print ("Tu numero es mayor a 100")

#Desafio 
edad = int(input("Ingrese su edad: "))
licencia = int(input("Tiene licencia (ingrese 1 si tiene/ 0 si no tiene)"))
if edad >= 18 and licencia == 1:
    print("Puede conducir")
elif licencia == 0 or edad < 18:
    print("No puede conducir")
