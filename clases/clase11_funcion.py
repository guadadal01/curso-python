#Ejercicio 1
"""Escribí las siguientes funciones y probá que funcionan:

saludar(nombre) → devuelve "Hola, {nombre}!".
es_par(n) → devuelve True si n es par, False si no.
celsius_a_fahrenheit(c) → convierte temperatura (fórmula: c * 9/5 + 32).
valor_absoluto(n) → devuelve el valor absoluto sin usar abs()."""

def saludar (nom):
    return f"Hola, {nom}"

def es_par(n):
    return n % 2 == 0

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def valor_absoluto(n):
    return n if n % 2 == 0 else n * -1

print(saludar("Guada")) 
print(es_par(2), es_par(13))
print(celsius_a_fahrenheit(100))
print(valor_absoluto(4), valor_absoluto(-9))

#Ejercico 2
"""scribí cuatro funciones: sumar(a, b), 
restar(a, b), multiplicar(a, b), dividir(a, b). Para dividir, retorná None si b == 0."""
def suma (a,b):
    return a + b

def multiplicar (a,b):
    return a * b

def restar(a,b):
    return a - b

def dividir (a,b):
    return None if b == 0 else a / b

#Ejercicio 3
"""Tomá el código del ejercicio 3 de diccionarios y extraé las operaciones en funciones:

calcular_promedio(lista_notas) → float.
estado(promedio) → "Aprobado" o "Desaprobado".
mejor_alumno(notas_dict) → nombre del alumno con mejor promedio.
Usá esas funciones para imprimir el boletín."""

def calcular_promedio (lista_notas):
    return sum(lista_notas)/len(lista_notas)

def estado (promedio):
    return "Aprobado" if promedio > 6 else "Desaprobado"

def mejor_alumno(notas_dict):
    mejor, mejor_prom = None, -1
    for alumno, notas in notas_dict.items():
        prom = calcular_promedio(notas)
        if prom > mejor_prom:
            mejor_prom, mejor = prom, alumno
    return mejor

notas = {
    "Ana":   [8, 9, 10],
    "Beto":  [5, 6, 4],
    "Cami":  [7, 8, 9],
    "Dante": [3, 4, 5],
    "Eva":   [10, 10, 9]
}

for nombre, nota in notas.items():
    prom = calcular_promedio(nota)
    print(f"{nombre}: {prom:.2f} — {estado(prom)}")

print(f"El mejor promedio: {mejor_alumno(notas)}")

#Ejercio 4
"""Escribí analizar(numeros) que devuelva una tupla con (minimo, maximo, promedio, cantidad_pares). 
Desempaquetala al llamarla."""
def analizar(num):
    maximo = max(num)
    minimo = min(num)
    prom = sum(num)/len(num)
    cant_pares = sum(1 for n in num if n % 2 == 0) 
    return maximo, minimo, prom, cant_pares

maxi,mini,promed,par = analizar ([1,4,6,3,8,9,6,5,7])
print(f"Min: {mini}, Max: {maxi}, Promedio: {promed:.2f}, Pares: {par}")

#Ejercicio 5
"""Que imprime cada cosa?"""
def limpiar(lista):
    lista.clear()

def limpiar_seguro(lista):
    return []

datos = [10, 20, 30]
limpiar(datos)
print(datos)           # nada

datos2 = [10, 20, 30]
resultado = limpiar_seguro(datos2)
print(datos2)          # [10,20,30]
print(resultado)       # []


#Ejercicio 6
"""Escribí validar_password(password) que devuelva True si la contraseña cumple todas las reglas:
Al menos 8 caracteres.
Al menos una mayúscula.
Al menos un número.
Sin espacios.
Después escribí describir_password(password) que devuelva una lista de errores (vacía si todo está bien)."""

def validar_password (password):
    return ((len(password) > 8) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and " " not in password )

def describir_password (password):
    errores = []
    if len(password) < 8:
        errores.append("Debe tener al menos 8 caracteres")
    if not any(c.isupper() for c in password):
        errores.append("Debe contener al menos una mayúscula")
    if not any(c.isdigit() for c in password):
        errores.append("Debe contener al menos un número")
    if " " in password:
        errores.append("No debe contener espacios")
    return errores

#Ejercicio 7
"""contar_palabras(texto) → int: total de palabras.
palabras_unicas(texto) → set: palabras únicas en minúsculas.
palabra_mas_frecuente(texto) → str: la que más aparece.
palabras_largas(texto, min_largo) → list: palabras de más de min_largo letras (sin repetir).
resumen(texto) → dict con todos los datos anteriores"""

def contar_palabras (texto):
    return len(texto.slipt())

def palabras_unicas(texto):
    return set(texto.lower().split())

def palabra_mas_frecuente(texto):
    palabras = texto.lower().split()
    conteo = {}
    for p in palabras:
        conteo[p] = conteo.get(p, 0) + 1
    return max(conteo, key=conteo.get)

def palabras_largas (texto, min_largo):
    return list({p for p in texto.lower().split() if len(p) > min_largo})

def resumen(texto):
    return {
        "total_palabras":  contar_palabras(texto),
        "palabras_unicas": len(palabras_unicas(texto)),
        "mas_frecuente":   palabra_mas_frecuente(texto),
        "palabras_largas": palabras_largas(texto, 5),
    }

texto = """python es un lenguaje de programacion muy usado
python se usa en ciencia de datos en web y en automatizacion
aprender python es aprender a pensar"""

for clave, valor in resumen(texto).items():
    print(f"{clave}: {valor}")
