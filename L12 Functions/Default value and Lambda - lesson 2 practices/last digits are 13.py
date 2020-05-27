def last_digits_13(num):
    ''' Takes an integer and decides whether the last two digits are 13.

    Parameter num can be any integer (positive or negative). If the number is negative,
    it is made positive by multiplying by -1. The last digit and second last digit are
    calculated. Then the function decides whether the result (last digit + second last
    digit) is equal to 13.

    >>> last_digits_13(1829349834913)
    True
    >>> last_digits_13(13)
    True
    >>> last_digits_13(89824)
    False
    >>> last_digits_13(1)
    False
    '''
    if num > 0:
        num = num
    else:
        -1 * num
    last_digit = str(num % 10)
    second_last_digit = str((num - num % 10) // 10 % 10)
    if int(second_last_digit + last_digit) == 13:
        return True
    else:
        return False
