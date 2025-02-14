#Una clase en python es una estructura de dtos que tienen variables y funciones 
#una clase tiene atributos y metodos es decir los atributos son variables y los metodos son funciones
#Una clase es una plantilla para crear objetos, cualquier tipo de objeto en python

class Persona: #Siempre se pone como parametro la palabra self
    #Funcion Constructora
    #Debe tener __init___
    #Debe tener el objeto self que hace referencia a la instancia a la clse que se ha creado a partir de la persona 
    def __init__(self, nombre, apellido ,edad): #nombre y edad son 2 atributos
        self.nombre = f"{nombre} {apellido}"
        self.edad =edad


    def saludar(self):
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años.")


    
persona = Persona("Juan", "Bautista",20)
persona.saludar()

persona2 = Persona("Jose", "Bautista",18)
persona2.saludar()



#Ejemplo: Crea una clase llamada libro que tenga 2 atributos titulo y autor agrega un metodo llamado mostrar informacion que imprimir el titulo y autor del libro
class Libro: #Siempre se pone comno parametro la palabra self
    def __init__(self, titulo, autor_libro, año_publicacion):
        self.titulo = titulo
        self.autor = autor_libro
        self.año = año_publicacion
    
    def mostrar_informacion(self):
        print(f"El nombre del libro es: {self.titulo} , el autor es: {self.autor} y se publico en el año {self.año}")

libro1 = Libro("El principito", "J.K Rowling", "2012")
libro1.mostrar_informacion()

libro2 = Libro("Corazonada", "David Googings", "2013")
libro2.mostrar_informacion()

class Cuenta:
    def __init__(self, saldo_actual):
        self.saldo_actual = saldo_actual
        self.saldo_anterior = 0
    def depositar(self, cantidad):
        self.saldo_anterior = self.saldo_actual
        self.saldo_actual += cantidad
        print(f"Saldo Anterior: {self.saldo_anterior} y depositaste :{cantidad} Nuevo saldo : {self.saldo_actual}")

# Crear un objeto de la clase Cuenta con un saldo inicial
mi_cuenta = Cuenta(1000)
mi_cuenta.depositar(500)