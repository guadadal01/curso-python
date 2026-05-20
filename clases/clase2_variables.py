#Ejemplo
nombre = "Guada"
edad = 20
altura = 0.0
es_profesor = True
print (nombre)
print (edad)


#combinaciones
print("Hola", nombre, end= " ")
print("tenes", edad, "años")
print(f"Hola {nombre}, tenes {edad} años")

#tipos de datos
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(es_profesor))

#complejos
print (2j + 3j +5)

#operadores aritmeticos
a= 10
b= 3
print(a + b)  # suma
print(a - b)  # resta
print(a * b)  # multiplicación
print(a / b)  # división
print(a // b) # división entera
print(a % b)  # resto
print(a ** b) # potencia

#operadores de compracion
a = 10
b = 5

print(a > b)
print(a < b)
print(a == b)
print(a != b)

#operadores logicos
x = True
y = False

print(x and y)
print(x or y)
print(not x)

#OPERACIONES CON STRING

#concatenacion
saludo = "Hola" + " " + "Maxi"
print(saludo)      # Hola Maxi

separador = "-" * 20
print(separador)   # --------------------

#longitud
nombre = "Maxi"
print(len(nombre))  # 4

texto = "hola mundo"

#Mayusculas y Minusculas
print(texto.upper())       # HOLA MUNDO
print(texto.lower())       # hola mundo
print(texto.capitalize())  # Hola mundo
print(texto.title())       # Hola Mundo

#limpiar espacios
texto = "   Hola   "
print(texto.strip())   # "Hola"  — elimina espacios de ambos lados

#reemplazar
frase = "Hola Mundo"
print(frase.replace("Mundo", "Python"))  # Hola Python

#Dividir y unir
frase = "Hola Maxi Perez"
palabras = frase.split(" ") #divide el string en una lista
print(palabras)   # ['Hola', 'Maxi', 'Perez']


nombres = ["Maxi", "Ana", "Luis"]
resultado = "-".join(nombres) #une una lista en un string
print(resultado)  # Maxi-Ana-Luis

#Buscar
frase = "Python es genial"

print(frase.find("es"))        # 7  — posición donde aparece
print(frase.count("a"))        # 1  — cuántas veces aparece
print(frase.startswith("Py"))  # True
print(frase.endswith("ial"))   # True
print("genial" in frase)       # True — pertenencia

#Acceso por indice y slicing
nombre = "Python"
print(nombre[0])    # P   — primer carácter
print(nombre[-1])   # n   — último carácter
print(nombre[0:3])  # Pyt — desde índice 0 hasta 2

#casteo
nombre = 15 + int("26")
print(f"hola {nombre} sos guada")

#Ej1
nombre = "Guada"
edad = 20
print (nombre)
print (edad)

#Ej2
num1 = 12
num2 = 2
suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
div = num1 / num2
print (suma)
print (resta)
print(mult)
print (div)

#Ej3
altura = 1.56
print(type(altura))

#Ej4
num1 = 12
num2 = 15
es_mayor = num2 > num1
print (f"Entre {num1} y {num2} el mayor es {es_mayor}")

#Ej5
es_verdad = True
print(type(es_verdad))

#Ej 6- tabla de multiplicar de un numero
numero = 3
print (numero * 1)
print (numero * 2)
print (numero * 3)
print (numero * 4)
print (numero * 5)
print (numero * 6)
print (numero * 7)
print (numero * 8)
print (numero * 9)
print (numero * 10)