# if / elif      / else
# (portuguese)
# se / se não se / se não

# condition variable
condition = True
# if 'condition' is True, then returns the print
if condition:
    print('This is the "if" code.')
# if 'condition' is False, then returns the other print
else:  # else is always the LAST
    print('The "else" code is opposite to the "if" code.')


condition1 = False
condition2 = False
condition3 = True
condition4 = False

if condition1:
    print('This is the string of the first condition.')
elif condition2:
    print('This is the string of the second condition.')
elif condition3:
    print('This is the string of the third condition')
elif condition4:
    print('This is the string of the fourth condition')
else:
    print('The condition was not met.')


# this is another "if" code, you can have as many as you want
if 10 == 10:
    print('This is another "if" conditional string.')

# Again, a code outside of the conditionals
print('Outside "if" conditional code')
