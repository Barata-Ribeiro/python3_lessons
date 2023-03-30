"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Immutables we saw: str, int, float, bool
"""

string = 'barata Ribeiro'
# I can change the string value with the following code
# but I can't change the previous variable because it is immutable
# thus, the value is being added to a new variable
another_variable = f'{string[:3]}A{string[4:]}'
# Doesn't matter what you do, immutable strings are immutable
# string[3] = 'A'
print(string)
print(string.capitalize())
print(another_variable)
