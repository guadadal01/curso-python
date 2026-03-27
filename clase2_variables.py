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
texto = """
holaa buenass
una poesia?
"""
print (texto)

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

#casteo
nombre = 15 + int("26")
print(f"hola {nombre} sos guada")