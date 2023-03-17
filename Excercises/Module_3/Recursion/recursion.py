# Recursion: The repeated application of the same procedure to a smaller problem
#   - lets us tackle complex problems by reducing the problem to a simpler one
#   - a way of doing a repetitive task by having a function call itself
#   -  Base Case ( specific condition): A recursive function calls itself usually with a modified parameter until it reaches a specific condition.

# ? A recursive function will usually have this structure:

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
