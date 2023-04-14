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


# Best strategy for each event

# - If it's a login we want to add iot to a list of users logged in to that machine
# - If it's a logged out , we want to remove it from the list of users logged into that machine
#   -- Use a set to store the current users; adding new users at login time and removing them at logout time

#! How to know which set corresponds to the machine we're looking for:
#   - Easiest way to store this information is with a dictionary
# Name of the machine as the (key)
# Current users of that machine as the (value)

# So for each event we process, we'll first check in the dictionary to see if the machine is already there. We need to check this because it could be the first time we're processing an event for that machine. If it's not there, we'll create a new entry. If it is, we'll update the existing entry with the action corresponding to the event.

# Which means we either add the user if the event is a login or remove the user if it's a logout. Once we're done processing the events, we'll want to print a report of the information we generated. This is a completely separate task. So it should be a separate function. This function will receive the dictionary regenerated and print the report.

#! It's important to have separate functions; to process the data and to print the data to the screen. This is because if we want to modify how the report is printed, we know we only need to change the function in charge of printing. Or, if we find a bug in our processing the data, we only need to change the processing function. It would also allow us to use the same data processing function to generate a different kind of report, like generating a PDF file, for example.


#! ========== Writing the Script ==========

# Pseudo code
#   - Process the events to generate a report.
#   - Sort the list of events chronologically.
#   - Store the data in a dictionary of sets, which we'll use to keep track of who's logged in where.
#   - Have a function that generates the dictionary and a separate one that prints the dictionary.
