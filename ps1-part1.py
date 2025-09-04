# Ask the user for the first number, store the value in a variable
number_one = int(input("Enter an integer between 10 and 100: "))


# Ask the user for the second number, store the value in a variable
number_two = int(input("Enter an integer less than 4: "))


# Repeat back the numbers
print("You entered", number_one, "and" ,number_two)


# Perform calculations. Be careful about string formatting for autograders.
print(number_one, "+", number_two, "=", number_one + number_two)
print(number_one, "*", number_two, "=", number_one * number_two)
print(number_one, "**", number_two, "=", number_one ** number_two)
print(number_one, "%", number_two, "=", number_one % number_two)


