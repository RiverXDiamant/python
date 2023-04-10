# ========== OOP ==========

# Models concepts using classes and objects
# - A flexible, powerful paradigm where classes represent and define concepts, while objects are an instance of classes.

# In object-oriented programming, concepts are modeled as classes and objects. An idea is defined using a class, and an instance of this class is called an object. Almost everything in Python is an object, including strings, lists, dictionaries, and numbers. When we create a list in Python, we’re creating an object which is an instance of the list class, which represents the concept of a list. Classes also have attributes and methods associated with them. Attributes are the characteristics of the class, while methods are functions that are part of the class.

# Type function examples
#   Tells us which class the value or variable belongs to
print(type({}))
print(type([]))
print(type(""))
print(type(9))

# dir()
# List of all the attributes and methods in a class
#! Special Methods begin and End with double underscores;  they're called by some of the internal Python functions
# print(dir(""))
# print("================================")
# print(dir(9))
# print("================================")
# print(dir({}))
# print("================================")
# print(dir([]))

# When we use the help function on any variable or value, we're showing all the documentation for the corresponding class.
help("")
