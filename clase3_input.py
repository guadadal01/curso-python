"""
#Entrada de datos (input). Siempre devuelve texto
nombre = input ("Ingrese su nombre: ") 
apellido = input("Ingrese su apellido: ")
nombre_completo  = f"{nombre} {apellido}"
print (f"Hola {nombre_completo}")


#Conversion de tipos
edad = int(input("Ingrese su edad: "))
print (f"Tienes {edad} años")

altura = float(input("Ingrese su altura: "))
print (f"medis {altura} cm")
"""
#Ejercicios

#Ej1
nombre = input ("Ingrese su nombre: ")
print (f"Hola {nombre}")

#Ej2 
edad = input("Ingrese su edad: ")
print(f"Tenes {edad}")

#Ej3
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = num1 + num2 

print (f"La suma entre {num1} y {num2} es de {suma}")

#Ej4 
medida = float(input("Ingrese una medida en metros: "))
centimetros = int(medida * 100)

print (f"Su medida en metros a centimetros es de {centimetros} cm")

#Ej5

temp_Celsius = int(input("Ingrese temperatura en Celsius: "))
conv_Fahrenheit = temp_Celsius * 9/5 + 32

print(f"Su temperatura de Celsius a Fahrenheit es de {conv_Fahrenheit}")

#Ej6

precio = int(input("Ingrese el precio de su producto: "))
iva = (precio * 21) // 100
precio_final = precio + iva

print (f"El precio final con IVA es de {precio_final}")

#Ej7
nota1 = int(input("Ingrese la primer nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercer nota: "))

promedio = (nota1 + nota2 + nota3) // 3 

print (f"Tu promedio es de {promedio}")

#Ej8
cant_horas = float(input("Ingrese una hora: "))
conv_minutos = int(cant_horas * 60)

print(f"Tu hora a minutos es de {conv_minutos}")

#Ej9 
pago_por_hora = int(input("Ingrese cuanto cobra por hora: "))
horas_trab = int(input("Ingrese la cantidad de horas trabajadas: "))

sueldo_total = pago_por_hora * horas_trab

print (f"Su total a cobrar es de {sueldo_total}")

#Ej10
nombre = input("Ingrese su nombre: ")
edad =  int(input ("Ingrese su edad: "))
altura = float (input ("Ingrese su altura: "))

print (f"Hola {nombre}, tenes {edad} años y medis {altura} metros")