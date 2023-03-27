# Strings, Lists and Dictionaries

# Manipulate strings using indexing, slicing, and formatting
# Use lists and tuples to store, reference, and manipulate data
# Leverage dictionaries to store more complex data, reference data by keys, and manipulate data stored
# Combine the String, List, and Dictionary data types to construct complex data structures

# String Indexing and Slicing

#! Strings in Python are immutable

# String indexing allows you to access individual characters in a string. You can do this by using square brackets and the location, or index, of the character you want to access. It's important to remember that Python starts indexes at 0. So to access the first character in a string, you would use the index [0]. If you try to access an index that’s larger than the length of your string, you’ll get an IndexError. This is because you’re trying to access something that doesn't exist! You can also access indexes from the end of the string going towards the start of the string by using negative values. The index [-1] would access the last character of the string, and the index [-2] would access the second-to-last character.
