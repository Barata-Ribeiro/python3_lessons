"""
Exercise
Ask the user to type their name
Ask the user to type their age
If name and age are typed:
     Display:
         Your name is {name}
         Your inverted name is {inverted_name}
         Your name contains (or does not contain) spaces
         Your name has {n} letters
         The first letter of your name is {letter}
         The last letter of your name is {letter}
If nothing is entered for name or age:
     display "Sorry, you left fields empty."
"""

name = input('Enter your name: ')
age = input('Enter your age: ')

if name and age:
    print(f'Your name is {name}, and your age is {age}.')
    print(f'Your inverted name is {name[::-1]}.')
    if ' ' in name:
        print(f'Your name contains spaces.')
    else:
        print(f'Your name does NOT contain spaces.')
    # For now, it also counts the spaces...
    # in case your name contains spaces.
    print(f'Your name has {len(name)} letters.')
    print(f'The first letter of your name is {name[0]}.')
    print(f'The last letter of your name is {name[-1]}.')
else:
    print('Sorry, you left fields empty.')
