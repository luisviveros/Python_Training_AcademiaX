
# El nombre de la funcion es entendible y su parametro tambien
# Ya que quiere decir que recibe como parametro una lista

def calcular_promedio(lista_de_notas):
    """Calcula el promedio de una lista de notas.

    Args:
        lista_de_notas (list): lista de notas a promediar
        
    Returns: 
        float: Promedio de las notas 
    """
    promedio = 0
    for nota in lista_de_notas:
        promedio += nota
    return promedio / len(lista_de_notas)