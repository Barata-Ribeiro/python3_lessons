"""
Function Scope in Python
Scope refers to the location where that code can be accessed.
There are global and local scopes.
The global scope is the scope where all the code is reachable.
The local scope is the scope where only names from the same local area can be accessed.
We do not have access to names from internal scopes in external scopes.
The global keyword makes a variable from the external scope be the same in the internal scope.
"""
# DEBUGGER TEST #

x = 2  # variable must be defined before calling the function

print(x)  # First


def new_function():
    # x = 1  # this variable can't be used outside of the function
    y = 3
    global x  # Now the 'x' bellow is global
    x = 6  # This 'x' is/was different from the 'x' from outside

    def another_function():
        z = 5
        print(x, y, z)  # Second

    another_function()
    print(x, y)  # Third


new_function()
print(x)  # Fourth, this 'x' is the one from inside 'new_function'
