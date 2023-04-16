"""
enumerate - enumerates iterables (indexes)
"""
# [(0, 'Jameson'), (1, 'Peter'), (2, 'Rick'), (3, 'Helena)]
new_list = ['Jameson', 'Peter', 'Rick']
new_list.append('Helena')

enumerate_list = enumerate(new_list)

for item in enumerate_list:
    print(item)

print('What exists in the enumerate list?:', enumerate_list)
# NOTHING HAPPENS HERE
# for item in enumerate_list:
#     print(item)
print('---------------------------')

# Creates a list of tuples with the index and the item
print(list(enumerate(new_list)))

# for item in enumerate(new_list)...
for item in enumerate(new_list):
    # a = index, b = item
    # a, b = item
    print(item)

print('---------------------------')
for enumerate_tuple in enumerate(new_list):
    print('FOR of the tuple:')
    for value in enumerate_tuple:
        print(f'\t{value}')