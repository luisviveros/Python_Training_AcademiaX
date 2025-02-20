#Crea un programa que permita realizar un registro mensual de gastos en un archivo.txt es decir,mostrary calcular gastos. 
#El programa debera ser capaz de leer y escribir un archivo de python para almacenar la información 
import os

def limpiar_pantalla():
    #"""Limpia la pantalla de la consola, compatible con Windows y Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Gasto:
    def __init__(self, fecha, descripcion, monto):
        self.fecha = fecha
        self.descripcion = descripcion
        self.monto = float(monto)

    def __str__(self):
        return f"{self.fecha} - {self.descripcion} - ${self.monto:.2f}"
    
class RegistroGastos:
    def __init__(self, archivo="gastos.txt"):
        self.archivo = archivo
        #Verifica si el archivo existe si no lo vuelve a crear
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                pass
    

    def registrar_gasto(self, gasto):
    #Con with asegura que el archivo se cierre automáticamente después de escribir.
        with open(self.archivo, "a") as f:
            f.write(f"{gasto.fecha},{gasto.descripcion},{gasto.monto}\n")
    

    def mostrar_gastos(self):
        try:
            with open(self.archivo, "r") as f:
                lineas = f.readlines()
            if not lineas:
                print("No hay gastos registrados.")
                return []
            gastos = []
            print("\nGastos Registrados:")
            for linea in lineas:
                fecha, descripcion, monto = linea.strip().split(",")
                gasto = Gasto(fecha, descripcion, monto)
                gastos.append(gasto)
                print(gasto)
            return gastos
        except FileNotFoundError:
            print("El archivo de gastos no existe.")
            return []

    def calcular_total_gastos(self):
        gastos = self.mostrar_gastos()
        total = sum(gasto.monto for gasto in gastos)
        print(f"\nTotal de gastos: ${total:.2f}")
        return total
    
class menu:
    def __init__(self):
        self.registro = RegistroGastos()

    def mostrar_menu(self):
        while True:
            print("\n*** Registro de Gastos Mensuales ***")
            print("1. Registrar Nuevo Gasto")
            print("2. Mostrar Gastos Registrados")
            print("3. Calcular Total de Gastos")
            print("4. Salir")
            opcion = input("\nSeleccione una opción (1-4): ")

            if opcion == "1":
                limpiar_pantalla()
                self.registrar_nuevo_gasto()
            elif opcion == "2":
                limpiar_pantalla()
                self.registro.mostrar_gastos()
            elif opcion == "3":
                limpiar_pantalla()
                self.registro.calcular_total_gastos()
            elif opcion == "4":
                limpiar_pantalla()
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def registrar_nuevo_gasto(self):
        fecha = input("Ingrese la fecha del gasto (DD/MM/YY): ")
        descripcion = input("Ingrese la descripción del gasto: ")
        try:
            monto = float(input("Ingrese el monto del gasto: "))
            nuevo_gasto = Gasto(fecha, descripcion, monto)
            self.registro.registrar_gasto(nuevo_gasto)
            print("Gasto registrado exitosamente.")
        except ValueError:
            print("Monto inválido. Intente de nuevo.")




    
if __name__ == "__main__":
    menu = menu()
    menu.mostrar_menu()