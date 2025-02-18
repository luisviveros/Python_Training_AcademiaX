#f = open( 'archivo_2.txt', 'w') #se utiliza para escribir W (write)
f = open( 'archivo_2.txt', 'r') 

contenido = f.read()
contenido_modificado = contenido + "\nAdios!"

f = open('archivo_2.txt', 'w')

f.write(contenido_modificado)

f.close()