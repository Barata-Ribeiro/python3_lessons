# Manipulating keys and values in a dictionary
person = {}

##

##

key = 'name'
person[key] = 'Barack'
person['surname'] = 'Obama'

print(person)
print(person[key])  # Must not try to access a non-existent key

del person['surname']
print(person)

person[key] = 'Donald'
person['surname'] = 'Trump'
print(person)

del person['surname']

if person.get('surname') is None:
    print('No surname found')
else:
    print(person['surname'])

print(person)
