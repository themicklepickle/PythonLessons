#functions
def f():
    print(x)

def g():
    y = "I am local!" #local goes to g
    return y

#starting main program
x = "I am global!" #global variable

f()

print(g())
    
