import subprocess
subprocess.run(["clear"])
""""
# Crear
d = {"clave": "valor", "otra": 42}
d = dict(clave="valor", otra=42)
d = {}            # vacío (¡no set!)

# Acceder
d["clave"]                      # KeyError si no existe
d.get("clave")                  # None si no existe
d.get("clave", "por defecto")   # valor por defecto

# Modificar / agregar
d["nueva"] = 99
d.update({"x": 1, "y": 2})

# Eliminar
del d["clave"]
valor = d.pop("clave")
valor = d.pop("clave", None)    # sin error si no existe
d.clear()

# Verificar
"clave" in d
"val"   in d.values()

# Iterar
for clave in d:                       # solo claves
for valor in d.values():              # solo valores
for clave, valor in d.items():        # pares (lo más común ⭐)

# Comprehension
{k: v * 2 for k, v in d.items() if v > 0}

# Patrón contador
for x in coleccion:
    conteo[x] = conteo.get(x, 0) + 1
"""

#EJERCICIO1
"""
Creá un diccionario agenda con al menos 4 contactos (nombre → teléfono). Luego:
Imprimí el teléfono de uno usando [].
Intentá acceder a un contacto inexistente con .get() y un valor por defecto.
Agregá un contacto nuevo.
Eliminá uno existente con .pop().
Imprimí todos los contactos con for y .items().
contactos ={
    "Guada": 1234567,
    "Maria" : 3680753,
    "Mario" : 45689532,
    "Amalia" : 2468960
}
print(contactos["Maria"])
print(contactos.get("Sol", "No existe"))
contactos["Coni"] = 2213463
print(contactos)
contactos.pop("Mario")
print(contactos)
for nombre, num in contactos.items():
    print(f"{nombre}: {num}")
"""
#EJERCICIO2
"""Usá el patrón "contador con .get()" para construir un diccionario conteo con la cantidad de votos de cada lenguaje."""
votos = ["Python", "Java", "Python", "C++", "Python", "Java", "Go", "Python", "C++"]
conteo = {}
