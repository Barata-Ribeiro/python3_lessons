# Logical operator "not"
# Used to reverse expressions
# not True = False
# not False = True

password = input('Password: ')

# If nothing was typed / 'not' inverse the expression,
# which is a Falsy value in this case
if not password:
    print('Please enter a password...')
# If the password doesn't match the condition
elif password != '123456':
    print('Wrong password. Please try again.')
