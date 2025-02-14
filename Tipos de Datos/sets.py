# Sets 
# Comparten una caracteristica con los diccionarios y es que si la lista tiene repetido el nomobre por ejemplo en este cado Doe solo te va a leer un nombre y el otro se va a remplazar
# Los setes se ponen con corchetes
# En los set no puedes tener valores repetidos un True y un 1 o un false y un 0 
names = {"Kevin", "John", "Doe", "Doe", True, 300, 1, 0, False}
print(names)

frutas = set(("Manzana", "Pera", "Melocotón"))
# print(frutas)

texto = "Este es un ejemplo de texto para mostrar una caracteristicas de los Sets"
print(texto)
print(set(texto))

mi_set = set([1, 2, 3, 4, 4, 5])
mi_frozenset = frozenset(mi_set)
print(mi_frozenset)