# Nested For Loops

# ? For loops are best when you want to iterate over a known sequence of elements
# ? When you want to operate while a certain condition is true, while loops are the best choice

# Nested loop within a function
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end="")
    print()


# Combining a nested loop with conditionals

teams = ['Dragons', 'Wolves', 'Pandas', "Unicorns"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# ------------------------------------------------

# Iterates over the list and greets each friend


def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)


greet_friends(['Taylor', 'Luis', 'Jamaal', 'Eli'])

# ------------------------------------------------

# greet_friends("Barry") <-- will iterate through each letter of a string
#! If you want it to iterate over the whole string, have that string be a part of a list

# ------------------------------------------------

# greet an individual friend
