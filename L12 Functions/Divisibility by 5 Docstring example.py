def divisibility_by_5(num):
    ''' returns a True boolean if the argument is even, otherwise returns a false boolean

    parameter can be any int (positive or negative).

    >>> divisibility_by_5(15)
    True
    >>> divisibility_by_5(16)
    False
'''
    if num % 5 == 0:
        return True
    else:
        return False
