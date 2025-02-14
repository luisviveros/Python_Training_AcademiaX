x = 10

def foo():
    global x
    x = 20
    print ("Dentro: ", x)

foo()
