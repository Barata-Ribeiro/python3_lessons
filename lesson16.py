# if / elif      / else
# (portuguese)
# se / se não se / se não

entry = input('Do you want to "Enter" or to "Exit"? ')

# If typed 'Enter' then return the print
if entry == 'Enter':
    print('You have entered the system')
    print(23489372498)  # Can have many codes inside the if
# Else if typed 'Exit' then return the other print
elif entry == 'Exit':
    print('You have left the system')
# Else if typed none of the above then warns the user
else:
    print('You have made the wrong choice, FOOL!')

print('Outside the if / elif / else blocks.')
