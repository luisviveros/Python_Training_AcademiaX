x = 'global'

def foo():
    x = 'local'
    print(x)
    
foo()
print(x)