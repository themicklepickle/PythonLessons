"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana" or x == "apple":
        continue
    print(x)
