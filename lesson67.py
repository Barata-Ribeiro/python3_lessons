"""
Default values for parameters
When defining a function, parameters can
have default values. If the value is not
sent to the parameter, the default value will
be used.
Refactor: edit your code.
"""


def multiply(x, y, z=None):
    # Check if 'z' is not 'None', which means it has been provided as a parameter.
    if z is not None:
        # Print the values of x, y, and z, and their product (x * y * z).
        print(f'{x=}, {y=}, {z=} | {x * y * z}')
    else:
        # If 'z' is 'None', print the values of x and y, and their product (x * y).
        print(f'{x=}, {y=} | {x * y}')


multiply(2, 3)
multiply(345, 2)
multiply(7, 9, 0)
"""
In the last function call, 'multiply(7, 9, 0)', the 'z' parameter is explicitly provided as '0'. Since 'z' is not 'None', the function prints the values of 'x', 'y', and 'z' along with their product (7 * 9 * 0).
"""
multiply(z=8, y=6, x=2)
