# CSV -> Comma Separated Values
import csv

# Pregutamos por el nombre del archivo
nombre_archivo = input("Escribe el nombre del archivo: ")

archivo = open(nombre_archivo,"r")

lector = csv.reader(archivo)

for fila in lector:
    contenido = "  ".join(fila)
    print(contenido)

