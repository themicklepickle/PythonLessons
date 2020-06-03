# generating random ints

import random  # for functions related to random numbers

lower_bound = int(input("Please enter the lower bound: "))

upper_bound = int(input("Please enter the upper bound: "))

# print the random ints.
# Note that we need upper_bound + 1 because the randrange funtion DOES NOT include the upper bound!

for i in range(10):
    print(random.randrange(lower_bound, upper_bound + 1))

'''
import random

ones = []
twos = []
end = False

while end == False:
    for i in range(10):
        number = random.randrange(1, 3)
        print(number)
        
        






'''
