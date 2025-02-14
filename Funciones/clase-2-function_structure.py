# Las funciones nos permiten ejecutar varias veces una porción de código.
# parametros => cuando se crea la función
# argumentos => cuando se invoca la función


def fibonacci(n):
    """Esta es una función que nos devuelve la serie de Fibonacci""" #Este te permite poner un comentario en la función
    a, b = 0, 1 #Aqui es una forma de declarar dos variables en una linea de codigo a es igual a 0 y b es igual a 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# invocamos nuestra función
fibonacci(2000)
fibonacci(1000)
fibonacci(5000)


def saludar (nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar("Juan")

#Argumentos arbitrarios
def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola, {nombre}!")

saludar("Juan", "Pedro", "Maria")