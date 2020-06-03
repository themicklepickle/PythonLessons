"""
Notes:
- note that a function has access to all variables declared before its definition. However, they should not be used.
- the rest of the program
- return automatically stops the function

Vocabulary:
- Parameter: The variable declared in the function declaration/definition
- Argument: The actual value passed in the program

Syntax:
def FUNCTIONNAME(PAR1, PAR2, ...):
    body
    of
    function
"""

"""
#function which prints out 5 stars in a row
def print_five_stars():
    print(5*"*")

#recall the function
print_five_stars()
"""

"""
#number of arguments must match number of parameters
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
"""

"""
#first and last name
def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "")
"""

"""
#using a variable as an argument
def print_char(char_to_print):
    print(char_to_print)

some_char = "H"
print_char(some_char)
print_char("Blah")
print_char("!" + "?")
"""

"""
#pass by value
def add_one(num):
    num += 1
    print("Value of num in function is", num)

num = 5
print("Value of num in function is", num)
add_one(num)
print("Value of num in function is", num)
"""

"""
#multiplication
def multiply(a, b):
    product = a * b
    return product

x = int(input("Please enter the first number:"))
y = int(input("Please enter the second number:"))
result = multiply(x, y)
print(x, "times", y, "=", result)
"""

"""

#prints 10 newlines
def tenNewLines():
    print(10 * "\n")

tenNewLines()
"""

"""
#takes an int and returns its square
def square(num):
    return num ** 2

integer = int(input("Please enter an integer: "))
result = square(integer)
print("The square of", integer, "is", result)
"""

"""
#shorts or pants
def shortsOrPants(temp):
    if temp > 20:
        return "shorts."
    else:
        return "pants."

temperature = int(input("Please enter the temperature: "))
result = shortsOrPants(temperature)
print("Since the temperature is", str(temperature) + "°, you should wear", result)
"""
