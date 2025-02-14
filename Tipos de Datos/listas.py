# List (listas - array) La lista son  los arreglos y puedes tener dentro diferente variables de diferentes tipos de dato y se declaran con corchete [ ]
name = "Kevin"
number1 = 2

frutas = ["Manzana", "prea", "uva", "Melocotón", "Banano"]
numeros = [1, 2, 3]
# # new_list = frutas + numeros
# frutas[1:4] = ["Uno", "Dos", "Tres"] Este funciona para modificar la lista en esas paosion del rango va de la posicion del 1 al 4 
numeros = frutas[1:4] #
frutas[1] = "Pera" #Este es para poder acceder a la lista y en la posicion 1 poder quitar el nombre de prea y poner el nombre de Pera
print (frutas[0]) # Este es para poder imprimir la palabra que esta dentor de la lista en ese espacio de la lista en 0 
frutas[-3] = "Mazana" # Accedes a la lista pero del lado derecho y en vez empezar en cero empieza en -1 y 

numeros.append(4)
numeros.append(5*4) # Este es para agregar a la lista el numero 20 en la ultima posición del arrgelo
new_list = [frutas, numeros]
print(new_list[0][3])
# print(new_list[1])
print(len(frutas)) # Para saber cuantos elementos hay en la listas
del frutas[0] #sirve para borrar dentro de la lista un elemento

#ordenar listas en python
lista= [3, 4,5,1,4,2]
lista.sort()
print(lista)