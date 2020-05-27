#seeing the effect of random.seed()

import random #for functions related to random numbers

print("First run: ")
random.seed(7)
for i in range(10):
    print(random.randrange(1,11))

print("Second run: ")
random.seed(7)
for i in range(10):
    print(random.randrange(1,11))
