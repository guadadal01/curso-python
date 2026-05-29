#¿Cuántas acciones distintas tiene el juego?
    #carton, bolillero, actualizar, turnos
#¿Qué datos necesita cada una? ¿Qué devuelve?
    # el cartón -> lista (15 num) del 1 al 90
    # bolillero -> numero único
    # actualizar cartón -> se recorre marcar el numero, los números q faltan y los marcados
    # contador de turnos ->

#¿Podés simular una partida chica (con 5 números) a mano?
    # mi cartón = 1,5,6,8,10
    # numero random = 5
    # turno = 1
    # se fija si el numero random esta dentro del cartón
    # 	¿5 esta en el cartón? 
    #       si -> actualizar carton
    #          -> numero marcado = 1/5, faltan= 4/5
    # numero random= 2
    # tuno = 2
    # ¿2 esta en el cartón? 
    #   no -> carton no se actualiza
    #      -> numero marcado y numeros que faltan quedan igual
    # (desp de muchos turnos)
    # mi carton = 1(salio), 5 (salio), 6 (salio), 8 , 10(salio)
    # numero random = 8
    # verificar si esta dentro de la lista -> si -> ¿Es el ultimo que falta? -> si = BINGO

#¿Qué funciones vacías escribirías como esqueleto?
    # def generar carton
    # def bolillero
    # def verificar carton
import random
carton = set(random.sample(range(1,91),15))