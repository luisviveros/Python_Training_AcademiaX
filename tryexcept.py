try:
    numero = int(input("Ingresa un numero: "))
    print(f"El numero es {numero}")
except ValueError:
    print("Debes ingresar un numero Valido")