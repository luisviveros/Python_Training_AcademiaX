def mi_generador(n):
    for i in range(n):
        yield i**2
        
generador_cuadrados = mi_generador(5)

print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))
print(next(generador_cuadrados))

#Ejercicio:  Crear un generador que devuelva solo los nummeros impares de una lista dada

def lista(n):

    for i in range(n):

        if i % 2 == 0:

            yield i


pares = lista(5)



print(next(pares))

print(next(pares))

print(next(pares))
