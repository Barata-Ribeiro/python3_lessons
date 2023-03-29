"""
Flag - Mark a location
None = No value
'is' and 'is not' = is or is not (type, value, identity)
id = Identity
"""

v1 = 'a'
v2 = 'a'
# Both values have the same id for they're the same thing
# despite being different variables.
print(id(v1))
print(id(v2))

condition = True  # or True
passed_if = None  # The correct way

if condition:
    # This is bad code, variable must exist
    # outside of the scope of this code
    passed_if = True
    print('Do something.')
else:
    # This makes things even worse!!
    # If you didn't have an else, the error
    # wouldn't go away.
    # passed_if = None  # Could be False
    print("Don't do something.")

if passed_if is None:
    print("Didn't pass the if condition.")
else:
    print('Passed the if condition.')

# If 'Falsy' then it will generate an error
# One does not simply declare a variable
# inside a conditional statement
# print(passed_if)

print(passed_if, passed_if is None)  # None True
print(passed_if, passed_if is not None)  # None False
