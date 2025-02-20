#Tienes una lista de diferentes canciones son canciones de diferentes autores y lo que haras es crear una rokola
# Cada que presiones play te va a regresa una canción
# Tome una cancion de las que tiene al azar y la va a tocar
# Hay una configuracion que le tienes que poner a la rokola es un numero y ese numero lo que dice es que no repitas la cancion que ya tocaste antes despues de cierto numero de turnos 
# Por ejemplo si este numero es 4 y pongo play voy a escoger una cancion y la siguiente vez que toque play esa cancion no se va a repetir va a tomar hasta 4 turnos para que vuelva a tocar esa cancion
import random
class Rocola:
    def __init__(self):
        self.temas = [ 'Heaven', 
            'Another Day in Paradise', 
            'I Want to Break Free', 
            'Bohemian Rhapsody',
            'Persiana Americana',
            'De Musica Ligera',
            'Fast Car',
            'Freedom'
        ] 
        self.queue = []
        
    def play(self, k):
        if len(self.queue) >= k:
            primero = self.queue.pop(0)
            self.temas.append(primero)
        indiceRandom = random.randint(0, len(self.temas)-1)
        tema = self.temas.pop(indiceRandom)
        self.queue.append(tema)
        return tema
        
Rocola = Rocola()
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)
print(Rocola.play(4), Rocola.queue)



        