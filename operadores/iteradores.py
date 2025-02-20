lista = [1,2,3,4,5]

iterador = iter(lista)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

#Ejericio hacer lo mismo pero al final elevandolo al cuadrado
lista = [2,4,6,8,10,12,14,16,18,20]
iterador = iter(lista)

print (next(iterador)**2)
print (next(iterador)**2)
print (next(iterador)**2)