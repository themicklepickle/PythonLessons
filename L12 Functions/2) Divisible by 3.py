#divisible by 3
#Michael Xu & Ryan Lo

#argument 1 (num) is the integer that is taken
#argument 2 (divisor) is the number in which divisibility of num is checked for - default is 3

def divisibility(num, divisor = 3):
    if num % divisor == 0:
        return True
    else:
        return False
