import subprocess
subprocess.run(["clear"])
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

#EJERCICIO1
"""
Creá un diccionario agenda con al menos 4 contactos (nombre → teléfono). Luego:
Imprimí el teléfono de uno usando [].
Intentá acceder a un contacto inexistente con .get() y un valor por defecto.
Agregá un contacto nuevo.
Eliminá uno existente con .pop().
Imprimí todos los contactos con for y .items()."""
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

#EJERCICIO 2
"""Usá el patrón "contador con .get()" para construir un diccionario conteo con la cantidad de votos de cada lenguaje."""
votos = ["Python", "Java", "Python", "C++", "Python", "Java", "Go", "Python", "C++"]
conteo = {}

for v in votos:
    conteo[v] = conteo.get(v, 0) + 1

print(conteo)

#EJERECICIO 3
"""Calculá e imprimí el promedio de cada alumno.
Imprimí solo los aprobados (promedio ≥ 6).
Encontrá al alumno con el mejor promedio."""
notas = {
    "Ana":   [8, 9, 10],
    "Beto":  [5, 6, 4],
    "Cami":  [7, 8, 9],
    "Dante": [3, 4, 5],
    "Eva":   [10, 10, 9]
}
promedios = {}
for nombre, nota in notas.items():
    prom = sum(nota)/len(nota)
    promedios[nombre] = prom
    print(f"{nombre}: {prom:.2f} ")

print("APROBADOS")
for alum, prom in promedios.items():
    if (prom > 6):
        print(f"{alum}: {prom:.2f}")

mejor_prom = max(promedios, key= promedios.get)
print(f"El alumno con mayor promedio es {mejor_prom}")


#EJERCICIO 4
numeros = list(range(1,11))
impar_par = {n: "par" if n % 2 == 0 else "impar" for n in numeros}
print(impar_par)

precios = {"manzana": 150, "banana": 80, "naranja": 120, "uva": 200}
baratas = {f: p for f, p in precios.items() if p < 130}
print(baratas)
aumento = {f: round(p * 1.10) for f, p in precios.items()}
print(aumento)

#EJERCICIO 5
"""Imprimí todos los productos disponibles (stock > 0) con su precio.
Calculá el valor total del inventario (precio stock de cada producto).
Imprimí cuántos productos hay por categoría.
Encontrá el producto más caro disponible"""
inventario = {
    "laptop":      {"precio": 1500, "stock": 3, "categoria": "electronica"},
    "mouse":       {"precio": 250,  "stock": 0, "categoria": "electronica"},
    "teclado":     {"precio": 800,  "stock": 5, "categoria": "electronica"},
    "silla":       {"precio": 1200, "stock": 2, "categoria": "muebles"},
    "escritorio":  {"precio": 2500, "stock": 1, "categoria": "muebles"},
    "auriculares": {"precio": 400,  "stock": 8, "categoria": "electronica"},
}
for prod, d in inventario.items():
    if d["stock"] > 0:
        print(f"{prod}: ${d['precio']} (stock: {d['stock']})")
total = sum(d["precio"] * d["stock"] for d in inventario.values())
print(f"\nValor total: ${total}")

categorias = {}
for d in inventario.values():
    cat = d["categoria"]
    categorias[cat] = categorias.get(cat, 0) + 1
print(f"\nPor categoría: {categorias}")

disponibles = {p: d for p, d in inventario.items() if d["stock"] > 0}
mas_caro    = max(disponibles, key=lambda p: disponibles[p]["precio"])
print(f"\nMás caro disponible: {mas_caro} (${disponibles[mas_caro]['precio']})")

#EJERCICIO 6
partidos = [
    {"local": "Boca",        "visitante": "River",       "goles_local": 2, "goles_visitante": 1},
    {"local": "River",       "visitante": "San Lorenzo", "goles_local": 0, "goles_visitante": 0},
    {"local": "Boca",        "visitante": "Independiente","goles_local": 3, "goles_visitante": 1},
    {"local": "San Lorenzo", "visitante": "Boca",        "goles_local": 1, "goles_visitante": 2},
    {"local": "Independiente","visitante": "River",      "goles_local": 2, "goles_visitante": 2},
    {"local": "River",       "visitante": "Boca",        "goles_local": 1, "goles_visitante": 0}
]

tabla = {}

def init(tabla, equipo):
    tabla.setdefault(equipo, {"pts": 0, "pj": 0, "gf": 0, "gc": 0})

for p in partidos:
    loc, vis = p["local"], p["visitante"]
    gl, gv   = p["goles_local"], p["goles_visitante"]
    init(tabla, loc); init(tabla, vis)
    tabla[loc]["pj"] += 1;  tabla[vis]["pj"] += 1
    tabla[loc]["gf"] += gl; tabla[loc]["gc"] += gv
    tabla[vis]["gf"] += gv; tabla[vis]["gc"] += gl
    if   gl > gv: tabla[loc]["pts"] += 3
    elif gl == gv: tabla[loc]["pts"] += 1; tabla[vis]["pts"] += 1
    else:          tabla[vis]["pts"] += 3

print(f"{'Equipo':<15} {'PJ':>3} {'PTS':>4} {'GF':>4} {'GC':>4} {'DIF':>4}")
print("-" * 36)
for equipo, s in sorted(tabla.items(), key=lambda x: x[1]["pts"], reverse=True):
    dif = s["gf"] - s["gc"]
    print(f"{equipo:<15} {s['pj']:>3} {s['pts']:>4} {s['gf']:>4} {s['gc']:>4} {dif:>+4}")