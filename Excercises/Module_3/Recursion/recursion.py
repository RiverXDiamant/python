# Recursion: The repeated application of the same procedure to a smaller problem
#   - lets us tackle complex problems by reducing the problem to a simpler one
#   - a way of doing a repetitive task by having a function call itself
#   -  Base Case ( specific condition): A recursive function calls itself usually with a modified parameter until it reaches a specific condition.

# ? A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)

# Example 1: Fill in the blanks to make the is_power_of function return whether the number is a power of the given base. Note: base is assumed to be a positive number.


def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number//base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False

# Example #2: The count_users function recursively counts the amount of users that belong to a group in the company system, by going through each of the members of a group and if one of them is a group, recursively calling the function and counting the members


def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count


print(count_users("sales"))  # Should be 3
print(count_users("engineering"))  # Should be 8
print(count_users("everyone"))  # Should be 18