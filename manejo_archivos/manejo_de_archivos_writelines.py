f = open("archivo.txt", "w")

lines = ["Linea 1\n","Linea 2\n","Linea 3\n"] #Esto es para reescribir el archivo de texto
f.writelines(lines)
f.close()
