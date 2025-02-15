#1. Define una clase base llamada Empleado con los atributos de nombre, sueldo base y un método para calcular el sueldo actual y uno para mostrar los datos del empleado
#  después crea las clases Gerente y Programador que heredan de Empleado con métodos para agregar un bono al sueldo y para agregar el lenguaje de programación que manejan, 
# respectivamente . 

class Empleado:
    def __init__(self, nombre, sueldo_base):
        self.nombre = nombre
        self.sueldo_base = sueldo_base
    
    def sueldo_actual(self,dias_trabajados):
        sueldo_actual = self.sueldo / 30 * dias_trabajados
        return sueldo_actual

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre} Salario Base: {self.sueldo_base}")
        print("----------------------------------------------------")

class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base,bono):
        super().__init__(nombre, sueldo_base)
        self.bono = bono

    def salario_total(self):
        total_salario =  self.sueldo_base + self.bono
        return total_salario


    def mostrar_datos(self):
        print(f"Gerente - Nombre: {self.nombre}, Salario Base:{self.sueldo_base}, Bono: {self.bono} Salario Total: {self.salario_total()} ") 
        print("----------------------------------------------------")


class Progrmador(Empleado):
    def __init__(self, nombre, sueldo_base,lenguaje):
        super().__init__(nombre, sueldo_base)
        self.lenguaje = lenguaje

    def mostrar_datos(self):
       print(f"Gerente - Nombre: ${self.nombre}, Salario Base: ${self.sueldo_base}, Lenguaje: {self.lenguaje} Salario Total: ${self.sueldo_base} ") 
       print("----------------------------------------------------")
        

    

Nombre_1 = Empleado("Juan Perez", 50000)
Nombre_1.mostrar_datos()

Nombre_2 = Gerente("Ana Gomez", 70000, 10000)
Nombre_2.mostrar_datos()

Nombre_3 = Progrmador("Carlos Rodriguez", 60000, "Python")
Nombre_3.mostrar_datos()
        

