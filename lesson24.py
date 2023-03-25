# 'in' and 'not in' operators
# Strings are iterable
#  0 1 2 3 4 5  // Index
#  B a r a t a
# -6-5-4-3-2-1  // Negative Index

name = 'Barata'
print(name[2])  # returns 'r'
print(name[-4])  # also returns 'r'
print(10 * '-')
print('t' in name)  # returns True, name contains 't'
print('z' in name)  # False, name does not contain 'z'
print('Bar' in name)  # True, name contains 'Bar'
print('arata' not in name)  # False, name does contain 'arata'
print(10 * '-')

input_name = input('Enter your name: ')
find = input('Type what you want to find: ')

# If 'find' is in 'input_name', returns...
if find in input_name:
    # returns message saying that the letter/word
    # was found in the input_name
    print(f'{input_name} contains {find}')
else:
    # returns message saying that the letter/word
    # was not found in the input_name
    print(f'{input_name} does not contain {find}')
