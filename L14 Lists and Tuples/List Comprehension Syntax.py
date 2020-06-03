# [expression] for [item] in [list]
"""
x = [i ** 2 for i in range(10)]
print(x)

x = []
for i in range(10):
	x.append(i **2)
print(x)
"""

# [expression] for [item] in [list] if [condition]
"""
x = [i ** 2 for i in range(10) if i % 2 == 0]
print(x)
x = []
for i in range(10):
	if i % 2 == 0:
		x.append(i ** 2)
print(x)
"""

# [expression] if [condition] else [condition] for [item] in [list]
"""
x = [i ** 2 if i % 2 == 0 else -i for i in range(10)]
print(x)

x = []
for i in range(10):
	if i % 2 == 0:
		x.append(i ** 2)
	else:
		x.append(-i)
print(x)
"""
