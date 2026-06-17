import random
import os
os.system("cls")


def armar_carton ():
    return set(random.sample(range(1,91), 15))

def sacar_num(bol,sal):
    pass

def verif_ganador():
    pass

def estado_carton():
    pass

print ("Empieza el juego")
carton = armar_carton()

print (sorted(carton))

input("Presioná Enter para empezar...")

bolillero = set(range(1,91))
salieron = set()

while not verif_ganador(carton,salieron):
    num = sacar_num(bolillero,salieron)
    if num in carton:
        estado_carton(carton,salieron)

print()