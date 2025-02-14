"""
try: evalua una porción de código
except: manejamos el posible error.
else: se ejecuta cuando no hay un error.
finally: se ejecuta independientemente de si hay o no errores
"""
raise Exception("Error creado a propósito")
try:
    raise Exception("Error creado a propósito")
except:
    print("Hubo un error de nombre")
else:
    print("No hubo error")
finally:
    print("Esto siempre se ejecuta")