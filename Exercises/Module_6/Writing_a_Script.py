# ========== Final Project Introduction: Writing a Script From the Ground Up ==========

#! ========== Problem Statement ==========

# * We need to process a list of Event objects using their attributes to generate a report that lists all users currently logged in to the machines.

# ? With this information, we want to write a script that generates a report of which users are logged in to which machines at that time. We need to know what information we'll use as input and what information we'll have as output.
# ? Login/Logout event type

# Input = List of events
#           - Each event is an instance of the event class
# *        Event Class:
# *          - Contains the (date) when the event happened
# *          - The (name) of the machine where it happened
# *          - The (user) involved
# *          - The event (type)

#   -Have to know the exact names of the attributes to access them: Date, User, Machine, Type
# Even types are strings:
#   Login: Our script will receive a list of event objects and we'll access the events attributes. We'll then use that information to know if a user is currently logged into a machine or not
#   Logout: We want to generate a report that lists all the machine names and for each machine, lists of the users that are currently logged in. We then want this information printed on the screen

#! ========== Research ==========
# Consider all the tools we have available to help us solve the problem. To find out which users are currently logged into machines, we need to check when they logged in and when they logged out. If a user logged into a machine and then logged out, they're no longer logged into it.

# * sort vs sorted:
# *   - Sorted returns a new list, while sort returns the same list reorganized.

# * Example: sort()

numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)  # : Output: [1, 2, 4, 6, 7]

# * Example: sorted()

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)  # Output: ['Carlos', 'Ray', 'Alex', 'Kelly']
print(sorted(names))  # Output: ['Alex', 'Carlos', 'Kelly', 'Ray']


# Sort using other parameters.

# * Example: Order elements of a list using the return value of a function

# sort() vs sorted(): both sort alphabetically by default
#   - Can take a couple of Parameters:
#       -- Key: lets us use a function as the sorting key

print(sorted(names, key=len))

#! ========== Planning ==========

# * - Our input will be a list of events and we'll sort them by time.
# * - Each event in that list will include a machine name, a username, and tell us whether the event is a login or a logout.
# * - We want our script to keep track of users as they log in and out of machines
