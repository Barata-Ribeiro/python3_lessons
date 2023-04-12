"""
lists in Python
'list' type - Mutable
Supports multiple values of any type
Reusable knowledge - indexes and slicing
Useful methods:
     append - Adds an item to the end
     insert - Adds an item at the chosen index
     pop - Remove from the end or chosen index
     del - delete an index
     clear - clears the list
     extend - extends the list
     + - concatenate lists
Create Read Update   Delete
(portuguese)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#            0,  1,  2,  3,  4
new_list = [10, 20, 30, 40, 50]

# new_list.append('Barata')
# name = new_list.pop()
new_list.append(60)
del new_list[-1]  # delete the last item, -1 will always be the last index
# new_list.clear()  # clears the list completely
new_list.insert(0, 5)  # Insert a new value at the beginning
# If the insert() has an bigger index than the list size,
# it will add the new value to the end anyway, but the index
# itself will not exist and cannot be accessed.

print(new_list)  # I could use new_list.pop() inside the print

# Concatenation of lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
# list_d = ... (the line bellow)
# None, the method extend() returns nothing if inside a variable
list_a.extend(list_b)
print(list_a)  # This is the way, list_d cannot exist with the previous line
print(list_c)
