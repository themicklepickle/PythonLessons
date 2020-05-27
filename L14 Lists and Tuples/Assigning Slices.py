x = list(range(10))
print(x)
x[1:4] = []
print(x)
x[5:] = ['a', 'b', 'c', 'd', 'e', 'f']
print(x)
x[::2] = 6 * [0]
print(x)
x[-1:] = x[::]
print(x)
