# Introduction to lambda function (single-line anonymous function)
# The lambda function is a function like any
# other in Python. However, they are anonymous
# functions that contain only one line. In other words,
# everything must be contained within a single
# expression.
# list = [
#     {'name': 'Luiz', 'lastname': 'Miranda'},
#     {'name': 'Maria', 'lastname': 'Oliveira'},
#     {'name': 'Daniel', 'lastname': 'Silva'},
#     {'name': 'Eduardo', 'lastname': 'Moreira'},
#     {'name': 'Aline', 'lastname': 'Souza'},
# ]

lst = [34, 57, 8, 20, 769, 96, 3, 1, 41, 31, 4345, 456, 586, 90]
# lst.sort()  # This sorts the list, but changes the original

name_lst = [
    {'name': 'Luiz', 'lastname': 'Miranda'},
    {'name': 'Maria', 'lastname': 'Oliveira'},
    {'name': 'Daniel', 'lastname': 'Silva'},
    {'name': 'Jason', 'lastname': 'Bourne'},
    {'name': 'Sherlock', 'lastname': 'Holmes'},
    {'name': 'Eduardo', 'lastname': 'Moreira'},
    {'name': 'Aline', 'lastname': 'Souza'},
]


# def name_order(item):
#     return item['name']

# name_lst.sort(key=name_order)

# The same thing as above, but with a lambda function - a single line
name_lst_copy = name_lst.copy()
name_lst_copy.sort(key=lambda item: item['name'])

for item in name_lst_copy:
    print(item)
print()


def show_lst(lst):
    for item in lst:
        print(item)
    print()


lst_1 = sorted(name_lst, key=lambda item: item['name'])
lst_2 = sorted(name_lst, key=lambda item: item['lastname'])

show_lst(lst_1)  # Ordered by name
show_lst(lst_2)  # Ordered by lastname
