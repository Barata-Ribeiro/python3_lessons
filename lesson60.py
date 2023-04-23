"""
Ternary operation (one-line conditional)
<value> if <condition> else <other value>
"""
condition = 10 == 11
variable = 'Value' if condition else 'Other value'
print(variable)

print('-------------------')

digit = 9  # > 9 = 0, < 9 = ...
new_digit = digit if digit <= 9 else 0
# The same as above but with a different syntax
new_digit = 0 if digit > 9 else digit
print(new_digit)

print('-------------------')

print('Value' if False else 'Other value' if False else 'End')
