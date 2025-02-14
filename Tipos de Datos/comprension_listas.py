numeros = [1,2,3,4,5]
dobles = []
for num in numeros:
    dobles.append(num*2)

print(dobles)

#Ahora con compresion de listas
numeros = [1,2,3,4,5]
dobles = [numero*2 for numero in numeros]

print(dobles)


#pares
numeros = [1,2,3,4,5]
pares = [numero*2 for numero in numeros if numero % 2 == 0]

print(pares)