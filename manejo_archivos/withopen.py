#Sentencia de control de contexto de python que se utiliza para abrir un archivo y poderse modificarcr

with open('archivo.txt', 'r') as f:
    contenido = f.read()
    print(contenido)