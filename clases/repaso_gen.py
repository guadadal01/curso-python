#EJERCICIO 1
""" 
Una fotocopiadora cobra $15 por hoja. Si la cantidad supera las 100 hojas, aplica un descuento del 20% sobre el total.
Escribí un programa que pida la cantidad de hojas y muestre el precio final con 2 decimales. Si hubo descuento, mostralo por separado. 

cant_hojas = int(input("Ingrese la cantidad de hojas: "))
precio_final =  cant_hojas * 15

if (cant_hojas > 100):
    descuento = (precio_final * 20) / 100
    total = precio_final - descuento
    print (f"El subtotal es de: ${precio_final:.2f}")
    print(f"El descuento es de ${descuento:.2f}")
else:
    total = precio_final
print(f"El precio total es de ${total:.2f}")

#EJERCICIO 2
def clasificar_entrada (edad):
    if (edad < 18):
        return "No puede entrar"
    elif (edad <= 25):
        return "Entrada joven: $2000"
    elif (edad <= 59):
        return"Entrada general: $3000"
    else:
        return "Entrada libre"

print(clasificar_entrada (16))
print(clasificar_entrada (22))
print(clasificar_entrada (45))
print(clasificar_entrada (65))

#EJERCICIO 3
deposito = int(input(f"Ingrese la cantidad que quiera depositar: "))

while (deposito < 10000) and (deposito != 0):
    deposito = int(input(f"Ingrese la cantidad que quiera depositar: "))
if (deposito >= 10000):
    print("Felicidades! cumpliste el objetivo")
else:
    print("No cumpliste el objetivo:(")

#EJERCICIO 4

def analizar_ventas (ventas):
    total = sum(ventas)
    promedio = sum(ventas)/len(ventas)
    sobre_promedio = 0
    for i in ventas:
        if (i > promedio):
            sobre_promedio += 1
    return {"total": sum(ventas), "mayor" : max(ventas), "menor": min(ventas), "promedio": promedio, "sobre_promedio": sobre_promedio}
    
ventas = [12500, 8900, 23100, 5400, 18700, 11200, 9800, 30500, 7600, 15300]
print(analizar_ventas(ventas))

#EJERCICIO 5

def es_segura(password):
    cumple_long = False
    if len(password) >= 8: cumple_long = True
    else: return cumple_long
    
    cumple_mayus = False
    cumple_dig = False

    for letra in password:
        if letra.isupper(): cumple_mayus = True
        if letra.isdigit(): cumple_dig = True
    return cumple_mayus and cumple_dig

password = "Hola2"
print(es_segura(password))
"""
#EJERCICIO 6
accesos_lunes  = [12345678, 87654321, 12345678, 55555555, 87654321, 11111111]
accesos_martes = [87654321, 33333333, 55555555, 87654321, 44444444]

lun_set = set(accesos_lunes)
mar_set = set(accesos_martes)

    #¿Cuántas personas distintas entraron el lunes?
print(f"La cantidad de personas distintas que entraron el lunes fueron: {len(lun_set)}")

    #¿Qué personas entraron los dos días?
print(f"Las personas que entraron los dos dias fueron: {lun_set.intersection(mar_set)}")

    #¿Qué personas entraron el lunes pero no el martes? 
print (f"Las personas que entraron el lunes pero no el martes fueron: {lun_set - mar_set}")

    #¿Cuántas personas distintas entraron en alguno de los dos días?
print(f"En alguno de los dos dias entraron: {len(lun_set.union(mar_set))} ")

#EJERCICIO 7 
#buscar(agenda, nombre) → devuelve los datos del contacto, o "No encontrado" si no existe.
def buscar (agenda,nombre):
    if nombre in agenda: return agenda[nombre]
    else: return "No encontrado"

#agregar(agenda, nombre, telefono, ciudad) → agrega el contacto a la agenda.
def agregar (agenda, nombre, telefono, ciudad):
    agenda[nombre] ={"telefono": telefono, "ciudad": ciudad}

#por_ciudad(agenda, ciudad) → devuelve una lista de nombres de los contactos de esa ciudad.
def por_ciudad (agenda, ciudad):
    lista = []
    for nombre, elem in agenda.items():
        if elem["ciudad"] == ciudad:
            lista.append(nombre)
        return lista

agenda = {
    "Ana":  {"telefono": "221-1234", "ciudad": "La Plata"},
    "Beto": {"telefono": "011-5678", "ciudad": "Buenos Aires"},
    "Cami": {"telefono": "221-9012", "ciudad": "La Plata"},
}
print(buscar(agenda, "Ana"))           # → {"telefono": "221-1234", "ciudad": "La Plata"}
print(buscar(agenda, "Dante"))         # → "No encontrado"
print(agregar(agenda, "Dante", "223-3456", "Mar del Plata"))
print(por_ciudad(agenda, "La Plata"))  # → ["Ana", "Cami"]

#EJERCICIO 8
def analizar (texto):
    palabra = len(texto.split())
    