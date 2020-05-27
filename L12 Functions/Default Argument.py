def root(value, index = 2):
    ''' finds the root of a number

    value: the number (float or int) to take the root of
    index: the index of the root (default to two)
    '''

    return value ** (1/index)

print("root(4, 3):", root(4,2))
print("root(8, 3):", root(8,2))
print("root(4):", root(4))
