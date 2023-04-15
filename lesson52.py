"""
tuple type - An immutable list
"""
names = ['Drake', 'Rick', 'Julia']
names = tuple(names)  # Converts into a tuple
# names = list(names)  # Converts into a list again
# names[1] = 'Jason'  # Can't change the value of a tuple
print(names[-1])
print(names)
