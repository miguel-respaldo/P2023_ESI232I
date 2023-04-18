# CSV -> Comma Separated Values
import csv

def promedio_por_materia(lector):
    lista_materias = []
    lista_promedio = []
    contador_alumnos = 0
    for fila in lector:
        if fila[0] == "nombre":
            for i in range(len(fila)-1):
                lista_materias.append(fila[i+1])
                lista_promedio.append(0.0)
        else:
            for i in range(len(fila)-1):
                lista_promedio[i] = lista_promedio[i] + float(fila[i+1])
            contador_alumnos = contador_alumnos +1
    for i in range(contador_alumnos):
        lista_promedio[i] = lista_promedio[i] / contador_alumnos
    for i in range(len(lista_materias)):
        print("El promedio de la materia de {:<18s} es {:>5.2f}".format(lista_materias[i], lista_promedio[i]))


def promedio_por_alumno(lector):
    for fila in lector:
        promedio = 0.0
        if fila[0] == "nombre":
            continue
        for i in range(1,5):
            promedio = promedio + float(fila[i])
        promedio = promedio / 4.0
        print("El promedio de {:<8s} es {:>5.2f} ".format(fila[0], promedio))


# Pregutamos por el nombre del archivo
nombre_archivo = input("Escribe el nombre del archivo: ")
archivo = open(nombre_archivo,"r")
lector = csv.reader(archivo)

promedio_por_alumno(lector)

# Uso la funcion seek para irme al principio del archivo
archivo.seek(0)

promedio_por_materia(lector)


