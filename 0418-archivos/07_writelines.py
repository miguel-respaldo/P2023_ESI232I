archivo = open("prueba4.txt", "w")
lineas= ["Esta es otra prueba \n", "Esta por terminar el curso"]
archivo.writelines(lineas)
print(archivo)