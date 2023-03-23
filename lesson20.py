first_value = input('Enter the first value: ')
second_value = input('Enter the second value: ')
# Converts the first and second values to integers
int_first_value = int(first_value)
int_second_value = int(second_value)

if int_first_value == int_second_value:
    print(f'The {int_first_value=} is equal to the {int_second_value=}.')
elif int_first_value > int_second_value:
    print(f'The {int_first_value=} is greater than the {int_second_value=}.')
elif int_first_value < int_second_value:
    print(f'The {int_first_value=} is smaller than the {int_second_value=}.')
else:
    print('The comparison is not valid.')

"""
The code could be improved by simplifying
the comparisons with 'greater than or equal to.'
or 'less than or equal to' as the teacher's method
below. However, I've chosen to use elif as well.
"""

# TEACHER'S SOLUTION
if first_value >= second_value:
    print(
        f'{first_value=} is greather '
        f'or equal to {second_value=}'
    )
else:
    print(
        f'{second_value=} is greather '
        f'than {first_value=}'
    )
