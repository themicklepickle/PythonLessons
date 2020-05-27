# creating and modifying a dictionary

# creating a dictionary
d = {"a": 1, "b": 2, "test": 3}
print(f"Accessing values by keys: {d['a']}")

# modifying the value of an element
d["a"] = 100
print(f"After modifying a value: {d['a']}")

# different methods of creating a dictionary
d1 = dict({"id": 1948, "name": "Washer", "size": 3})
d2 = dict(id=1948, name="Washer", size=3)
d3 = dict([("id", 1948), ("name", "Washer"), ("size", 3)])
d4 = {"id": 1948, "name": "Washer", "size": 3}
print(d1, d2, d3, d4, sep="\n")
