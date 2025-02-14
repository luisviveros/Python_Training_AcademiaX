"""
match => Sirve para evaluar un data y con base a ello realizar una acción
"""

status = "gaseoso"

match status:
    case "solido" | "liquido" | "gaseoso":
        print("El estado es solido o es liquido o gaseoso")
    # case "liquido":
    #     print("El estado el liquido")
    # case "gaseoso":
    #     print("El estado el gaseoso")
    case _:
        print("El estado no existe")