"""
Exercise
Display list indexes:
0 Maria
1 Helena
2 Luiz
"""
name_list = ['Maria', 'Helena', 'Luiz']

for name in name_list:
    print(name_list.index(name), name)

print('-----------------------')
# TEACHER'S SOLUTION

# name_list.append('João')

# Generates a list of indexes from the length of 'name_list' with len() as a parameter for range()
indexes = range(len(name_list))
# print(indexes)   # range(0, 3)

for index in indexes:
    print(index, name_list[index])
