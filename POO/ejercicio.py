#1. Define una clase base llamada Empleado con los atributos de nombre, sueldo base y un método para calcular el sueldo actual y uno para mostrar los datos del empleado
#  después crea las clases Gerente y Programador que heredan de Empleado con métodos para agregar un bono al sueldo y para agregar el lenguaje de programación que manejan, 
# respectivamente . 

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
    
    def sueldo_actual(self):
        print("")