"""
string slicing
  012345678910
  Hello World
-1110987654321
Slicing [i:f:p] [::]
Note: the 'len' function returns the quantity
of characters from 'str'
"""

variable = 'Hello World'
print(variable[6:])  # prints 'World'
print(variable[:5])  # print 'Hello', from the start until 5
print(variable[-8:-2])  # prints 'lo Wor'
print(15 * '-')
print(len(variable))  # Returns 11, for it returns the quantity
print(variable[0:len(variable):2])  # prints 'HloWrd'
print(variable[::-1])  # prints the str backwards 'dlroW olleH'
