"""
Named and unnamed arguments in Python functions. 
A named argument has a name with an equal sign. 
An unnamed argument only receives the argument value.
"""


def sum(x, y, z):
    # Definition
    print(f'Args: {x=}, {y=}, {z=} | Operation: {x} + {y} + {z} = {x + y + z}')


sum(1, 2, 5)
sum(324, 3456, 6347)

# To invert the parameters in Python, you can use the keyword argument.
sum(y=56, x=78, z=90)

# sum(1, z=2, 5)  # All arguments must be named.
# You either name all arguments or none at all.
