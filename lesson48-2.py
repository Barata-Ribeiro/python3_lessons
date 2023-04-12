"""
lists in Python
'list' type - Mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods: 
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
(portuguese)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
# Index     0, 1, 2, 3,  4,  5
new_list = [1, 3, 7, 9, 11, 13]

new_list[1] = 300  # replaces the index 1 with a new value

del new_list[3]  # removes the index 3 from the list
print(new_list[2])  # If del [3], then index 2 will now be 7

# Avoid Python to move indexes in between,
# Only add or remove from the end of the list.

# Can add as many as I want with 'append'
new_list.append(15)
new_list.append(17)
last_value = new_list.pop()  # Removes the last item from the list

new_list.append(19)
# It says to be incompatible to add a string to this list, but it still does...
# new_list.append("21")
n_last_value = new_list.pop()  # Removes another item from the list, at the end

# If .pop() with an index, I can remove the

print(new_list, 'Removed:', last_value, '| Also removed:', n_last_value)
