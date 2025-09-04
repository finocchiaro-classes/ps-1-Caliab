# Write a function that takes two variables and does all the computations asked
def number_fun(a, b):
# Ask the user for the first number, store the value in a variable
        

# Ask the user for the second number, store the value in a variable

# Repeat back the numbers
    print("You entered", a, "and" ,b)

# Perform calculations. Be careful about string formatting for autograders.
    print(a, "+", b, "=", a + b)
    print(a, "*", b, "=", a * b)
    print(a, "**", b, "=", a ** b)
    print(a, "%", b, "=", a % b)

firstnum = int(input("Enter an integer between 10 and 100: "))
secondnum = int(input("Enter an integer less than 4: "))
number_fun(firstnum, secondnum)
