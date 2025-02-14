""" 
funcion => Una función siempre devuelve un valor (return)
Una funcion siepre te devuelve un valor y si no hay valor te devuelve un NONE cuando no hay un return
procedimiento => No devuelve un valor
scope => Es el alcance que tiene una variable dentro del código.
"""

# variable global
name = "Kevin"

def func():
    global name # Es para poder acceder a la variable global dentro de la función
    name = name + " Hola"
    print(name)

func()
