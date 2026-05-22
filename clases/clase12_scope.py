#EJERCICIO 1
# Bloque A
x = 10
def doble():
    return x * 2
print(doble()) #20

# Bloque B
def triple():
    y = 5
    return y * 3
triple()
print()   # y no existe fuera de la funcion

# Bloque C
z = "global"
def cambiar():
    z = "local"
cambiar()
print(z)   # "global"

#EJERCICIO 2
"""Escribí saludar_formal(nombre, titulo="Sr./Sra.", idioma="es") que devuelva:

En español ("es"): "Buenos días, {titulo} {nombre}."
En inglés ("en"): "Good morning, {titulo} {nombre}."
"""
#PASOS
    #hacer funcion saludar
        #recibe por parametro nombre, titulo e idioma
    #devolver:
        #si es español dice buen dia con el titulo y nombre
        #si es ingles dice good morning con el titulo y nombre
def saludar_formal (nombre, titulo= "Sr./Sra.", idioma="es"):
    if idioma =="es":
        return f"Buenos dias, {titulo} {nombre}"
    return f"Good morning, {titulo} {nombre}"

print(saludar_formal("García"))
print(saludar_formal("Smith", titulo="Dr.", idioma="en"))
print(saludar_formal("López", idioma="es", titulo="Ing."))

#EJERCICIO 3 
"""Escribí las siguientes funciones usando *args:
maximo(*nums) → devuelve el mayor sin usar max().
concatenar(*palabras, separador=" ") → une las palabras con el separador.
promedio(*nums) → calcula el promedio; si no recibe números, devuelve 0."""
#Pasos
    #funcion maximo sin usar max()
        #devolver el mayor
    #funcion concatenar 
        #unir palabras con separador
    #funcion promedio
        #calcular promedio
        #si no recibe numeros devuelve 0
def calcular_maximo(*nums):
    max = nums[0]
    for n in nums:
        if n > max:
            max = n
    return max

def concatenar(*palabras, separador = " "):
    return separador.join(palabras)

def promedio (*nums):
    if len(nums) > 0:
        return sum(nums)/len(nums)
    return 0

print(calcular_maximo(3, 7, 2, 9, 4))                    # 9
print(concatenar("hola", "mundo"))               # "hola mundo"
print(concatenar("a", "b", "c", separador="-")) # "a-b-c"
print(promedio(4, 8, 6))                         # 6.0
print(promedio()) 

#EJERCICIO 4
"""Escribí crear_perfil(nombre, **datos) que construya y devuelva un diccionario con nombre como clave fija y el resto de los datos que lleguen por **kwargs.

p = crear_perfil("Maxi", edad=27, ciudad="Ensenada", activo=True)
# {"nombre": "Maxi", "edad": 27, "ciudad": "Ensenada", "activo": True}

p2 = crear_perfil("Ana", materia="Python", nota=9)
# {"nombre": "Ana", "materia": "Python", "nota": 9}"""
#Pasos
    #Hacer funcion crear perfil
        #parametro nombre y **datos
        #construir un diccionario con nombre como clave fija y los datos como valores
        #devolver diccionario
def crear_perfil(nombre, **datos):
    return {"Nombre": nombre, **datos}

print(crear_perfil("Guada", edad=20, ciudad="Ensenada"))
print(crear_perfil("Ana", nacimiento= 2005, dia= 13))

#EJERCICIO 5
"""Escribí log(nivel, *mensajes, separador="\n", prefijo="") que imprima cada mensaje precedido de [{nivel}] {prefijo}, uniendo los mensajes con separador"""
