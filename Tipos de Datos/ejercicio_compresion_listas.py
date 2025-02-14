juegos = ['monopoly', 'ajedrez', 'scrabble']

mayusculas = [juego.upper() for juego in juegos ]
print(mayusculas)
# mayusculas = []
# for juego in juegos:
#	 mayusculas.append(juego.upper())
# print(mayusculas)
num_letras = [len(juego) for juego in juegos ]
print(num_letras)
# num_letras = []
# for juego in juegos:
#	 num_letras.append(len(juego))
# print(num_letras)