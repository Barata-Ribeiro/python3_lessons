"""
Higher Order Functions - Functions that can receive and/or return other functions

First-Class Functions - Functions that are treated like other common data types (strings, integers, etc...)
"""


# Define a function 'salute' that takes in two parameters, 'msg' and 'name',
# and returns a formatted string containing the message and name.

def salute(msg, name):
    return f"{msg}, {name}..."


# Define a function 'exec' that takes in two or more parameters: a function 'func',
# and any number of arguments in the form of '*args'. This function executes the
# function 'func' with the arguments passed to it, using the *args syntax,
# and returns the result.

def exec(func, *args):
    # The *args syntax is used to pass any number of arguments
    # to the function being executed, which could include 'msg'
    # and 'name' or any other arguments needed by the function.
    return func(*args)


# Assign the 'salute' function to a variable named 'greetings'.
greetings = salute

# Call the 'exec' function, passing in the 'greetings' function, along with
# two string arguments "Good morning" and "Jason". The result of this call is
# assigned to a variable named 'execution'.
execution = exec(greetings, "Hello, there", "Jason")
print(execution)
