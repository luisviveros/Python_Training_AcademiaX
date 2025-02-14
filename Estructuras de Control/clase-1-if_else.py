# condicion = (if) True => ejecuta codigo
# condicion = (else) False => ejecuta otra porcion de codigo

edad_persona = int(input("Ingresa tu edad por favor: "))
EDAD_BASE = 18

if edad_persona > EDAD_BASE:
    print("Eres mayor de edad y mayor a 18 años")
    if edad_persona == 50:
        print("Tienes 50 años de edad")
elif edad_persona == 18:
    print("Tienes 18 años de edad")
else:
    print("Eres menor de edad")