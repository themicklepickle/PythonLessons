# cube root calculator
# Michael Xu & Ryan Lo

# argument 1 (num) is the integer that is taken as an argument
# argument 2 (index) is the index of the radical - default is 3

def cubeRoot(num, index=3):
    return round(num ** (1 / index), 14)
