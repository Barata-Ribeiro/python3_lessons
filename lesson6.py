# type conversion, casting
# type convertion, typecasting, coercion
# is the act of converting one type into
# another immutable and primitive type:
# str, int, float, bool
print(1 + 1)  # prints 2
print('a' + 'b')  # prints ab, polymorphism

# Using the class int() it converts a string to an integer
print(int('1'), type(int('1')))

# In case I receive a string, it can be converted to an integer using
# the class int()
print(int('1') + 1)  # prints 2

print(type(float('1') + 1))  # prints <class 'float'>

# Verify if the content is True or False
print(bool(''))  # empty string is False
print(bool('1'))  # This string is True

# converting an integer to string
print(str(16) + 'x')  # return 16x
