#Los decoradores recibne una funcion y regresan una funcion 

def decorador_para_imprimir(funcion):
    def contenedor(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        print(resultado)
        return resultado
    return contenedor

@decorador_para_imprimir
def sumar(x,y):
    return x + y

sumar(2,3)