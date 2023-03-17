# Variables are used to save something in the computer's memory.
# PEP8: start variables with lowercase letters,
# you can use numbers and underscore _ .
# The = sign is the assignment operator.
# It is used for assign a value to a name (variable).
# Usage: variable_name = expression

full_name = 'João M J Barata Ribeiro'
total_two_plus_two = 2 + 2
int_one = int('1')

print(full_name)  # prints "João M J Barata"
print(total_two_plus_two)  # prints 4

# Instead of using int('1') every time, you declare a variable
# now I can change one item instead of "hundreds"
print(int_one, type(int_one))  # prints 1 <clas 'int'>

name = 'João'
age = 27
of_legal_age = age >= 18
print('Name:', name, 'Age:', age)
print('Is of legal age?', of_legal_age)
