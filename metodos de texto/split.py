#se utiliza para dividir una cadena de texto en lista de subcadenas

#cadena= "hola, soy una cadena de texto"
#lista = cadena.split()
#print(lista)

#Ejemplo

nombre_apellido = input('Ingresa tu nombre y apellido: ')
nombre, apellido = nombre_apellido.split()
print('Nombre:', nombre)
print('Apellido:', apellido)