#Le permite a una clase heredar los parametros y atributos de otra clase
#Utilizar el codigo de otra clase


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"Hola, soy un animal llamado {self.nombre}")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre) #super es una funcion te da acceso a la clase animal

    def hablar(self):
        print("Woof, soy un perro y me llamo", self.nombre)


fido = Perro("Fido")
fido.hablar()

#Polimorfismo es una caracteristica que permite a una clase comportarse de manera diferente dependiendo de la situacion
#Una clase puedes definir metodos con el mismo nombre pero con diferentes parametros

#Ejercicio
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre) #super es una funcion te da acceso a la clase animal

    def hablar(self):
        print("Miau, soy un gato y me llamo", self.nombre)

minino = Gato("Fido")
minino.hablar()