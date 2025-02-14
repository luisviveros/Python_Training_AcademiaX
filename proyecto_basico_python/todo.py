#Se crea la funcion principal de nuestra aplicación 
#Es la que primera vez se debe de invocar

import os
runProgram = True
todolist =[]

# Funcion para mostrar las opciones del menu
def showMenuOptions ():
    print("")
    print("")
    print("Por favor seleccione una opcion:")
    print("")
    print("")
    print("1. Crear una tarea")
    print("2. Marcar como realizada una tarea")
    print("3. Borrar una tarea")
    print("4. Salir")

# Funcion para mostrar todas las tareas
def ShowTodoList():
    global todolist
    print()
    print()
    print("*******************************")
    for todo in todolist:
        print(f"{todolist.index(todo)+1}. {todo}")
    print("*******************************")
    print()
    print()

# Funcion para guardar las tareas en las variables "todolist"
def createTodo():
    os.system("cls") # limpiar pantalla
    global todolist
    print("Crear una nueva  tarea")
    todo = input("Por favor ingrese el nombre de la tarea: ")
    todolist.append(todo)   
    # Mostrar la lista de tareas
    ShowTodoList() 

# Funcion para marcar una tarea como realizada
def UpdateTodo():
    os.system("cls") # limpiar pantalla
    global todolist
    print("Actualizar una tarea")
    todoId = int(input("Ingrese el numero de la tarea que quiere marcar como hecha: "))
    todolist[todoId - 1] = todolist[todoId - 1] + "👍"
    ShowTodoList()

# Funcion que nos permite borrar una tarea
def DeleteTodo():
    os.system("cls") # limpiar pantalla
    global todolist
    print("Borrar una tarea")
    todoId = int(input("Ingrese el numero de la tarea que quiere borrar: "))
    del todolist[todoId - 1]
    ShowTodoList()

def main():
    global runProgram
    print(".: WELCOME TO  A PYTHON TO DO LIST :.")
    flag = True

    while runProgram:
        while flag:
            showMenuOptions() # Aqui se invoca la funcion para las opciones del menu
            option = int(input("Ingresa el numero de la opción: "))

            match option: 
                case 1:
                    createTodo()
                case 2:
                    UpdateTodo()
                case 3:
                    DeleteTodo()
                case 4:
                    print("Hasta luego!!")
                    runProgram = False
                    flag = False
                case _:
                    print("Opcion no reconocida . Ingrese una opcion valida. ")
        

#Es una condicion que siempre es positiva y siempre ahi inicia el codigo 
if __name__ == "__main__":
    main()

