#archivo = open("prueba2.txt","w")
archivo = open("prueba2.txt","wt")
linea_escrita = archivo.write("Estes es un nuevo Archivo\n")

archivo.write("{:<5s}{:<15s}{:>8s}\n".format("No.", "Nombre", "Precio"))
print("{:<5s}{:<15s}{:>8s}".format("No.", "Nombre", "Precio"))
for fila in range(10):
    archivo.write("{:<5d}{:<15s}{:>8.2f}\n".format(fila, str(fila), float(fila)))
    print("{:<5d}{:<15s}{:>8.2f}".format(fila, str(fila), float(fila)))

