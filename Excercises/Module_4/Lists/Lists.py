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


# Example # 2 - define a function that receives a list of people

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result


print(full_emails([("alex@example.com", "Alex Diego"),
      ("shay@example.com", "Shay Brandt")]))

#! word of caution about some common errors when dealing with lists in Python. Because we use the range function so much with for loops, you might be tempted to use it for iterating over indexes of a list and then to access the elements through indexing. You could be particularly inclined to do this if you're used to other programming languages before. Because in some languages, the only way to access an element of a list is by using indexes. Real talk, this works but looks ugly.
#
#! It's more idiomatic in Python to iterate through the elements of the list directly or using enumerate when you need the indexes like we've done so far. There are some specific cases that do require us to iterate over the indexes, for example, when we're trying to modify the elements of the list we're iterating. By the way, if you're iterating through a list and you want to modify it at the same time, you need to be very careful. If you remove elements from the list while iterating, you're likely to end up with an unexpected result. In this case, it might be better to use a copy of the list instead.


def skip_elements(elements):
    # code goes here
    new_list = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            new_list.append(element)
    return new_list


# Should be ['a', 'c', 'e', 'g']
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))

# List Comprehensions - Lets us create new lists based on sequences or ranges

# multiples = []
# for x in range(1, 11):
#     multiples.append(x*7)
# print(multiples)

# More efficient way  using List comprehension

multiples = [x*7 for x in range(1, 11)]
print(multiples)
