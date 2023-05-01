"""
Introduction to functions (def) in Python:
Functions are blocks of code used to replicate 
a specific action throughout your code. 
They can receive values for parameters (arguments) 
and return a specific value. 
By default, Python functions return None (nothing).
"""


def fPrint(a, b, c):
    print(a)
    print(b)
    print(c)


# Prints the following strings...
fPrint('Hello, world!', 'Hello, universe!', 'Hello, human!')


def nPrint(a, b, c):
    print(a, b, c)


nPrint(1, 2, 3)  # Print 1, 2, 3
nPrint(34, 56, 78)  # Print 34, 56, 78


def greeting(name='John/Jane Doe'):
    # If no parameters are given,
    # the 'name' parameter is set to 'John/Jane Doe'.
    print(f'Hello, {name}!')


greeting('World')  # Prints 'Hello, World!'


print('Random text...')  # This is not part of any functions
