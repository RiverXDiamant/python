# ========== Final Project Introduction: Writing a Script From the Ground Up ==========

# Problem Statement

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
