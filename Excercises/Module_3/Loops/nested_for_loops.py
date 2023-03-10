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

# * Question 2

# Fill in the blanks to make the factorial function return the factorial of n. Then, print the first 10 factorials (from 0 to 9) with the corresponding number. Remember that the factorial of a number is defined as the product of an integer and all integers before it. For example, the factorial of five (5!) is equal to 1*2*3*4*5=120. Also recall that the factorial of zero (0!) is equal to 1.


def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 10):
    print(n, factorial(n+1))

# ------------------------------------------------

# * Question 3

# Write a script that prints the first 10 cube numbers (x**3), starting with x=1 and ending with x=10.

for x in range(1, 11):
    print(x**3)

# ------------------------------------------------

# * Question 4

# Write a script that prints the multiples of 7 between 0 and 100. Print one multiple per line and avoid printing any numbers that aren't multiples of 7. Remember that 0 is also a multiple of 7.

for multiples_of_7 in range(0, 100, 7):
    print(multiples_of_7)

# ------------------------------------------------

# * Question 5

# The retry function tries to execute an operation that might fail, it retries the operation for a number of attempts.  Currently the code will keep executing the function even if it succeeds. Fill in the blank so the code stops trying after the operation succeeded.


def retry(operation, attempts):
    for n in range(attempts):
        if operation():
            print("Attempt " + str(n) + " succeeded")
        if n == 1:
            break
        else:
            print("Attempt " + str(n) + " failed")


retry(create_user, 3)
retry(stop_service, 5)
