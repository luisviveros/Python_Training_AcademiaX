def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))


#ejemplo numeros naturales

#Numeros naturales 1+2+3+4 = 10
def suma_de_naturales(n):
    if n == 1:
        return 1
    else:
        return n + suma_de_naturales(n-1)
    
print(suma_de_naturales(4))