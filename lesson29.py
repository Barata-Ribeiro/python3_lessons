"""
Introduction to try/except <<< IMPORTANT!!!
try -> try to run the code
except -> an error occurred when trying to execute
"""
# print(123)
# The following code will stop the program completely
# printing the error message, and therefore, the other
# codes will not be executed...
# int('a')
# print(456)

number_str = input('I will double the number you entered: ')

try:
    number_int = int(number_str)
    print(f'The double of {number_str} is {number_int * 2}')
except:
    print('This is not a valid number.')


# if number_str.isdigit():
#     number_int = int(number_str)
#     print(f'The double of {number_str} is {number_int * 2}')
# else:
#     print('This is not a valid number.')
