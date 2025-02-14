# ARGS
# def func(*args):
#     for item in args:
#         print(item)

# func("EDteam", "Hola Mundo", 1, 2, 3, 4, 5, 6, 8, 9, 7, 11)

# KARGS
days = {"dia1": "Lunes", "dia2": "Martes"}
# def func2(**kargs):
#     print(kargs)

# func2(**days)


def func3(*args, **kargs):
    print(args)
    print(kargs)


func3(1, 2, 3, 4, 5, 6, 7, **days)
