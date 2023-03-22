# Useful to colect data. Typed named becomes a variable
name = input('What is your name? ')
# It will show the variable name according to the input
print(f'Your name is: {name}')  # {name=} useful too
number_1 = input('Type your number: ')
number_2 = input('Type another number: ')

# Until learning how to check whether the typed number is a number or a
# string, creates a new variable to convert the input to a number
int_number_1 = int(number_1)
int_number_2 = int(number_2)

# Returns a string instead of the addition of numbers, so it's best
# to use the above variables instead, until learn new ways
print(
    f'The addition of {number_1} and {number_2} is {int_number_1 + int_number_2}')
