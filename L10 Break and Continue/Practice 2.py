number  = int(input("Please enter a number: "))

for i in range(1, number):
    if i % 3 == 0:
        continue
    print(i)
