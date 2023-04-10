# Lists Examples

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[n-1])
    return ("")


# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing
# print(get_word("Now we are cooking!", 1))  # Should print: Now
# print(get_word("Now we are cooking!", 5))  # Nothing


# ? We use tuples to store information that refers to a specific thing and does not change; i.e. - someones Full Name

# Tuples
# As we mentioned earlier, strings and lists are both examples of sequences. Strings are sequences of characters, and are immutable. Lists are sequences of elements of any data type, and are mutable. The third sequence type is the tuple. Tuples are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.

# You might be wondering why tuples are a thing, given how similar they are to lists. Tuples can be useful when we need to ensure that an element is in a certain position and will not change. Since lists are mutable, the order of the elements can be changed on us. Since the order of the elements in a tuple can't be changed, the position of the element in a tuple can have meaning. A good example of this is when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.

# Tuple Example

def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}".format(size / 1024))


# print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
# print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
# print(file_size(('Program', 'py', 1239)))  # Should print 1.21

# Iterating over Lists and Tuples

# Using enumerate function; Get the index of an element while going through a list

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))

# Output - the enumerate function returns a tuple for every element in a list

# 1 - Ashley
# 2 - Dylan
# 3 - Reese
