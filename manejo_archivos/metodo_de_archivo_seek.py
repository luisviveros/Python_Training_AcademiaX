#funcion de python que permite mover el puntero de un archivo a una posicion especifica

archivo = open("archivo_3.txt", "r")

archivo.seek(2) #recorre el puntero y imprime despues del cierta parte

contenido= archivo.read()
print(contenido)

archivo.close()