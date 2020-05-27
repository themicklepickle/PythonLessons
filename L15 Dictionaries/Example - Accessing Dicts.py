# accessing dictionaries

d = {"a": 1, "b": 2, "test": 3}

print("Accessing all keys (method 1):")
for k in d:
	print(k, end=" ")

print("\nAccessing all keys (method 2):")
for k in d.keys():
	print(k, end=" ")

print("\nAccessing all values:")
for k in d.values():
	print(k, end=" ")

print("\nAccessing all key/value pairs:")
for k, v in d.items():
	print(k, v)

print("Accessing all key/value pairs (slight modification):")
for i in d.items():
	print(i[0], i[1])
