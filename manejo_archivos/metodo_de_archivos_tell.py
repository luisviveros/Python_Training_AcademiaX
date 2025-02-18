# es un metodo de python qu devuelve la posicion actual del puntero
# de un archivo

f = open("archivo.txt", "r")

print(f.tell())

linea = f.readline()

print(f.tell())

f.close
