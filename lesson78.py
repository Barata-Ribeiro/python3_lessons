# Sets - Sets in Python (set type)
# Sets are taught in mathematics
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Represented graphically by Venn diagram
# Sets in Python are mutable, but only accept
# immutable types as internal values.

# Creating a set
# set(iterable) or {1, 2, 3}
s1 = set()  # Empty | Looks like a dictionary but it's not
s2 = {'Helen'}  # With data

print(s1, type(s1))  # <class'set'>
print(s2)

# Sets are efficient for removing duplicate values from iterables.
# - They do not accept mutable values;
# - Their values will always be unique;
# - They do not have indexes;
# - They do not guarantee order;
# - They are iterable (for, in, not in)

# Useful methods:
# add, update, clear, discard

# Useful operators:
# union | (union) - Joins sets
# intersection & (intersection) - Items present in both sets
# difference - Items present only in the left set
# symmetric difference ^ - Items that are not present in both sets
