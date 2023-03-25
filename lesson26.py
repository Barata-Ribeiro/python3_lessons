"""
Basic string formatting
s - string
d - int
f - float
.<number of digits>f
x or X - Hexadecimal
(Character)(><^)(amount)
> - Left
< - right
^ - center
= - Forces the number to appear before the zeros
- + or - sign
Eg: 0>-100,.1f
Conversion flags - !r !s !a
"""
variable = 'ABC'
print(f'{variable}')
print(f'{variable: >10}')  # Add 10 spaces on the left
print(f'{variable: <10}')  # Add 10 spaces on the right
print(f'{variable:#^9}')  # Add 9 '#' on the center
print(15 * '-')

# This is a bizarre example, but it returns -01,000.23
print(f'{-1000.234823948723948:0=+10,.2f}')
print(15 * '-')

# Returns the hexadecimal of 1500, 000005DC
print(f'The hexadecimal of 1500 is {1500:08X}')
