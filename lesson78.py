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

print('----------------')
# Sets are efficient for removing duplicate values from iterables.
# - They do not accept mutable values;
# - Their values will always be unique;
# - They do not have indexes;
# - They do not guarantee order;
# - They are iterable (for, in, not in)
l1 = [1, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 1]
s3 = set(l1)
l2 = list(s3)
print(l2)
print(4 in s3)  # True
print(2 not in s3)  # False

for number in s3:
    print(number)

print('----------------')
# Useful methods:
# add, update, clear, discard
s4 = set()
s4.add(1)
s4.add(2)
s4.update((3, 4, 'Hello World'))
s4.update('Jason')
# s4.clear()  # Clears the set completely
s4.discard('Hello World')
print(s4)

print('----------------')
# Useful operators:
# union | (union) - Joins sets
# intersection & (intersection) - Items present in both sets
# difference - Items present only in the left set
# symmetric difference ^ - Items that are not present in both sets
s5 = {1, 2, 3, 4, 5}
s6 = {2, 4, 3, 5, 6, 7}
s7 = s5 | s6
s8 = s5 & s6
s9 = s5 - s6
s10 = s5 ^ s6


print(s7)  # {1, 2, 3, 4, 5, 6, 7}
print(s8)  # {2, 3, 4, 5}
print(s9)  # {1}
print(s10)  # {1, 6, 7}
