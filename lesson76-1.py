# Dictionaries in Python (dict type)
# Dictionaries are data structures that consist of a
# pair of "key" and "value".
# Keys can be considered as the "index" we saw in lists
# and can be of immutable types such as: str, int, float, bool, tuple, etc.
# The value can be of any type, including another dictionary.
# We use curly braces - {} - or the dict class to create dictionaries.
# Immutable types: str, int, float, bool, tuple
# Mutable types: dict, list
# person = {
#     'name': 'Luiz',
#     'surname': 'Miranda',
#     'age': 18,
#     'height': 1.8,
#     'addresses': [
#         {'street': 'some street', 'number': 123},
#         {'street': 'another street', 'number': 321},
#     ]
# }
# person = dict(name='Luiz Otávio', surname='Miranda')

person = {
    'name': 'Jason',
    'surname': 'Bourne',
    'age': 45,
    'height': 1.78,
    'addresses': [
        {'street': 'Main Street', 'number': 456},
        {'street': 'Elm Street', 'number': 789},
    ]
}

another_person = dict(name="Ross", surname="Geller", age=27, height=1.85)

print(person, type(person))
print()
print(another_person, type(another_person))
print()
print(person['name'], person['surname'])

# Finding out the keys...
print()
for key in person:
    print(key, person[key])
