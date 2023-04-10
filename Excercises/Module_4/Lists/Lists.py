# Lists Examples

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[n-1])
    return ("")


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing


# ? We use tuples to store information that refers to a specific thing and does not change; i.e. - someones Full Name

# Tuple Example

def file_size(file_info):
    name, type, size = file_info
    return ("{:.2f}".format(size / 1024))


print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
print(file_size(('Program', 'py', 1239)))  # Should print 1.21
