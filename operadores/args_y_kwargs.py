# Ars: Parametro especial que permite recibir un número variable de argumentos posicionales como una tupla
# Kwargs: Parametro especial que permite recibir un número variable de argumentos nombrados

def sueldo(*args, **kwargs):
    total_sueldo = 0
    for arg in args:
        total_sueldo += arg
    
    for key, value in kwargs.items():
        total_sueldo += value
        
    return total_sueldo

print(sueldo(1000,2000,3000, juan=4000, pedro=5000, maria=6000))