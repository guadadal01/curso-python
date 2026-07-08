import random
import os
os.system("cls")

def jugar_bingo_indiv():
    def armar_carton ():
        return set(random.sample(range(1,91), 15))

    def sacar_num(bol,sal):
        num = random.choice(list(bol))
        bol.remove(num)
        sal.add(num)
        return num

    def verif_ganador(carton, sal):
        return carton.issubset(sal)

    def estado_carton(carton,sal):
        marcados = carton & sal #num q ya salieron
        faltan= carton - sal #los que faltan 
        print("_"*40)
        for n in carton:
            if n in sal:
                print(n, "✓", sep=" ", end= " ")
            else:
                print(n, end= "  ")
        print()
        print("_"*40)
        print(f"Marcados: {len(marcados)}/15 | Faltan: {len(faltan)}")

    print ("Empieza el juego")
    carton = armar_carton()

    print (f"Tu carton: {sorted(carton)}")

    input("Presioná Enter para empezar...")

    bolillero = set(range(1,91))
    salieron = set()

    turnos = 0

    while not verif_ganador(carton,salieron):
        turnos += 1
        num = sacar_num(bolillero,salieron)
        print(f"Salio el {num}")
        if num in carton:
            estado_carton(carton,salieron)
        input("Presionar Enter para continuar...")

    print(f"🎉 ¡BINGO! Ganaste en {turnos} turnos.")
