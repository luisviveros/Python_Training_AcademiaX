#archivo = open("archivo.txt", "r") #Aqui la r significa read de lectura es decir el archivo lo vas aleer de solo lectura

#contenido = archivo.read()

#print(contenido)

#archivo.close()


# Ejemplo un programa que cuenta las lineas que hay en el archivo

archivo=open("manejo_archivos/archivo.txt","r")
contenido=archivo.read()

#Genera lista con elementos 'linea' separados por saltos de linea '\n'
lista_contenido=contenido.splitlines()
#filtrado de términos vacios usando compresión de listas
lista_filtrada=[componente for componente in lista_contenido if componente]

contador=len(lista_filtrada)


print(f" Se han encontrado {contador} lineas en el texto\n")