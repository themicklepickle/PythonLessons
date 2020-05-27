def f():
    print(y)

def g():
    y = "I am local!"
    print(y)

y = "I am global"

f()

g()
