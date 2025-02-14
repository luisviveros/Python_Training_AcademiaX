x = 5

def funcion_externa():
    x = 10

    def funcion_interna():
        nonlocal x #Solo esta disponible en python3
        x += 1
        print("Funcion interna", x)

    funcion_interna()
    print("Funcion externa: ", x)

funcion_externa()
print("Global: ", x)