# Useful methods of dictionaries in Python
# len - number of keys
# keys - iterable with the keys
# values - iterable with the values
# items - iterable with keys and values
# setdefault - adds a value if the key doesn't exist
# copy - returns a shallow copy
# get - gets a key
# pop - deletes an item with the specified key (del)
# popitem - deletes the last added item
# update - updates a dictionary with another

import copy

person = {'name': 'John', 'age': 25}

print(person.__len__())  # 2
print()

print(person.keys())  # dict_keys(['name', 'age'])
print(list(person.keys()))  # ('name', 'age')
for key in person.keys():
    print(key)
print()

print(person.values())  # dict_values(['John', 25])
print(list(person.values()))  # ('John', 25)
for value in person.values():
    print(value)
print()

print(person.items())  # dict_items([('name', 'John'), ('age', 25)])
print(list(person.items()))  # (('name', 'John'), ('age', 25))
for key, value in person.items():
    print(f'{key}: {value}')
print()

print(person.setdefault('height', 1.84))  # 1.84
print(person)  # {'name': 'John', 'age': 25, 'height': 1.84}
print()

person_copy = person.copy()  # {'name': 'John', 'age': 25, 'height': 1.84}
print(f'This is the original: {person}')
print(f'This is a shallow copy of "person": {person_copy}')
person_deepcopy = copy.deepcopy(person)
print(f'This is a deep copy of "person": {person_deepcopy}')
print()

# Returns msg if the key doesn't exist
print(person.get('favoriteColor', "Doesn't exist"))
print()

print(person.pop('name'))  # John
print(person)  # {'age': 25, 'height': 1.84}
print()

print(person.popitem())  # ('height', 1.84)
print(person)  # {'age': 25}
print()

new_tuple = ('name', 'Jane'), ('age', 30), ('favoriteColor', 'blue')
new_list = [['name', 'Jane'], ['age', 30], ['favoriteColor', 'blue']]
person.update(new_tuple)  # or new_list
print(person)  # {'name': 'Jane', 'age': 30, 'favoriteColor': 'blue'}
