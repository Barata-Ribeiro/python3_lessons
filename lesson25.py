"""
Basic string interpolation
s - string
d and i - int
f - float
x and X - Hexadecimal (ABCDEF0123456789)
"""
name = 'Barata'
price = 1000.9485982
variable = '%s, the price is $%.2f' % (name, price)
print(variable)

# Returns 00002710
print('The hexadecimal of %d is %08x' % (10000, 10000))
