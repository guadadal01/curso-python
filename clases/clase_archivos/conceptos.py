import os
os.system ("cls")

#Abrir Archivos
# archivo = open("clases/clase_archivos/texto.txt", "r+") #open (path_relativo, modo) - los dos strings 

#hacer algo con el archivo
#print(archivo.read())
#archivo.write("chau")
#print(archivo.read())

#SIEMPRE HAY QUE CERRARLO

#archivo.close() #si hay errrores, no se cierra

#MANERA CORRECTA --- CON WITH (no se necesita usar close), se cierra por mas que haya errores
#Lectura de archivos
"""
with open("clases/clase_archivos/texto.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    lineas = archivo.readlines()
    for linea in archivo:
        print(linea, end="")
"""
#Escrituras de archivos
""""
alum = ["Guada", "Brandon", "Maxi"]
with open("clases/clase_archivos/alumnos.txt", "w", encoding="utf-8") as file:
    for a in alum:
        file.write(a + "\n")  # write() no agrega \n solo
"""
"""
alumnos = ["Roberto", "Mar", "Coni"]
with open("clases/clase_archivos/alumnos.txt", "a", encoding="utf-8") as archivo:
    for a in alumnos:
        print(a, file= archivo)  
"""

#Trabajar con carpetas

from pathlib import Path #Importar modulo para trabajar 

carpeta = Path("clases/clase_archivos/practica_archivos")
for f in carpeta.iterdir():
    print(f.name)
