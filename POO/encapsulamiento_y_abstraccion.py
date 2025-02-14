#Encapsulamiento: Capacidad de ocultar los detalles de implementacion de un objeto
#Abstraccion: La capacidad de representar los objetos de una manera simplificada

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Hola, soy un animal llamado {self.nombre}")

animal = Animal("Fido")
animal1 = Animal("Fido2")
animal2 = Animal("Fido3")
animal3 = Animal("Fido4")

