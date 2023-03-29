"""
Create a software that asks the user to enter an integer and inform if this number is even or odd. 
If the user does not enter a number integer, report that it is not an integer.
"""
number = input('Please type in the number of your choice: ')
try:
    number_int = int(number)
    if number_int % 2 == 0:
        print(f'The number {number_int} is even.')
    elif number_int % 2 == 1:
        print(f'The number {number_int} is odd.')
except:
    print('This is not a valid number.')

# TEACHER'S RESOLUTION
if number.isdigit():
    number_int = int(number)
    even_odd = number_int % 2 == 0
    even_odd_str = 'odd'

    if even_odd:
        even_odd_str = 'even'

    print(f'The number {number_int} is {even_odd_str}.')
else:
    print('This is not a valid number.')

"""
Create a software that asks the user for the time and displays the appropriate salutation based on the time described. 
Ex. Good morning 0-11, Good afternoon 12-17 and Good evening 18-23.
"""
time = int(input('Please enter the current time: '))
try:
    if time >= 0 and time <= 11:
        print('Good morning!')
    elif time >= 12 and time <= 17:
        print('Good afternoon!')
    elif time >= 18 and time <= 23:
        print('Good evening!')
    else:
        print('This is not a valid time.')
except:
    print("You haven't typed a valid number.")

# The teacher's resolution was the same as mine.

"""
Create a software that asks for the user's first name. 
If the name has 4 letters or minus, write "You have a short name"; 
if it has between 5 and 6 letters, write "You have a normal name"; 
else greater than 6, write "Your name is too long."
"""
name = str(input('Please enter your first name: '))
name_size = len(name)

if name_size > 1:
    if name_size <= 4:
        print('You have a short name.')
    elif name_size >= 5 and name_size <= 6:
        print('You have a normal name.')
    else:
        print('Your name is too long.')
else:
    print("You have to type your name.")

# The teacher's resolution was the same as mine.
