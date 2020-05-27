total = 0

while True:
    number = input("enter a number (0 to exit): ")
    number =  list(number)

    if "/" in number:
        number1 = []
        number2 = []
        
        position = int(number.index("/"))
        length = len(number)
        
        for i in range(position):
            number1.append(number[i])
        number1 = "".join(number1)
        number1 = float(number1)

        for i in range(position + 1, length):
            number2.append(number[i])
        number2 = "".join(number2)
        number2 = float(number2)

        number = number1 / number2
        total += number
        
    else:
        number = "".join(number)
        number = float(number)
        total += number

    if number == 0:
        break

total = str(round(total))
print("The sum is " + total + ". Goodbye!")
