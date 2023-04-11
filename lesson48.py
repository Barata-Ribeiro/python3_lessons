"""
lists in Python
'list' type - Mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods: append, insert, pop, del, clear, extend, +
"""
#         01234
#        -54321
string = 'ABCDE'  # 5 caracteres

# Created a list for the previous exercise by researching on the internet
new_list = [123, True, 'Barata Ribeiro', 1.245, []]
#          0,    1,    2,                3,      4,
#         -5,   -4,   -3,               -2,     -1,

# print(bool(new_list))  # falsy if empty
# print(new_list, type(new _list))  # <class 'list'>

new_list[-3] = 'Strauss'  # Redefining the str for index 2/-3

print(new_list)
print(new_list[2], type(new_list[2]))
