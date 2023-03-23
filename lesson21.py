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

# if condition is True:
# ...
if entry == 'E' and entered_password == allowed_password:
    print('User has entered.')
# The teacher has not used the elif
# condition to not complicate things
elif entry == 'L':
    print('User has left.')
else:
    print('Error.')

print(True and True)  # Returns True
print(False and False)  # Returns False
print(False and True)  # Returns the value that is falsy
print(bool(0) and bool(1))  # The same as above, but using a falsy value
