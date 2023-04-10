# =========================== Dictionaries ==========================

# dictionaries are used to organize elements into collections. Unlike lists, you don't access elements inside dictionaries using their position. Instead, the data inside dictionaries take the form of pairs of keys and values. To get a dictionary value we use its corresponding key. Another way these two vary is while in a list the index must be a number, in a dictionary you can use a bunch of different data types as keys, like strings, integers, floats, tuples, and more. The name dictionaries comes from how they work in a similar way to human language dictionaries. In an English language dictionary the word comes with a definition.

x = {}

print(type(x))


file_counts = {"jpg": 10, "txt": 4, "csv": 2, "py": 23}
print(file_counts)
