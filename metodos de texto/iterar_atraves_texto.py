#itera por palabra
texto = "Hola esto es un ejemplo de iteración"
for palabra in texto.split():
    print(palabra)

#itera por letra
texto = "Hola esto es un ejemplo de iteración"
for char in texto.split():
    print(char)

#Ejemplo 3
movies_and_series = "'Avengers', 'Black Mirror', 'Harry Potter', 'Stranger Things'"
for item in movies_and_series.split(','):
	print(item)