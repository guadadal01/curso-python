#¿Que me dan? lista de notas
#¿que devuelve? lista de notas que son mayor al promedio
#¿Como lo hago a mano?
    #Tener lista de notas 
    #sumar toda las notas de las listas y divido por la cantidad de notas
    #comparar cada nota con el promedio
        #si es mayor al promedio, lo devuelvo en forma de lista

#Partir en pasos (modularizar):
    #Tener lista de notas 
    #funcion que calcule el promedio
    #funcion que compare el promedio con las notas

#Esqueleto:
    #funcion calcular promedio: sumo la lista y la divido por su longitud
    #funcion comparar cuales: recorro la lista, si la nota es mayor a promedio se guarda en una lista y se devuelve


def calcular_promedio (nota):
    return sum(nota)/len(nota)

def comparar_notas (nota):
    resultado = []
    for n in nota:
        if n > calcular_promedio(nota):
            resultado.append(n)
    return resultado

notas= [3,6,8,4,5,9]
print(calcular_promedio(notas))
print(comparar_notas(notas))