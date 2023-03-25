# Logical operators
# and (e[portuguese]), or (ou[portuguese]), not (não[portuguese])
# and - All conditions need to be True.
# If any value is considered False,
# the entire expression will be evaluated to that value
# Falsy values (that you've seen) are:
# 0 0.0 '' False
# There is also the None type which is
# used to represent a non-value.

entry = input('[E]nter or [L]eave: ')
entered_password = input('Password: ')
allowed_password = '123456'

# Everything within parentheses comes first, followed
# by the other conditionals
if (entry == 'E' or entry == 'e') and entered_password == allowed_password:
    print('User has entered.')
else:
    print('User has left.')

print(True and True and True)  # True
print(True or False or 1 or 'abc')  # True
print('' or False or 0 or 'abc')  # Returns 'abc', which is True

# If nothing is entered, returns 'No Password...'
password = input('Enter password: ') or 'No password...'
print(password)
