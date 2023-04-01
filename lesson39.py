"""
Iterating strings with while
"""
#       012345678910111213
name = "Barata Ribeiro"  # Iterable
str_size = len(name)
new_str = ''

index = 0  # Index is 0
while index < str_size:  # Loop through string while
    # index is less than str_size
    # Set the letter to be name through index
    letter = name[index]
    # Put the letter in a new string with the * symbol
    new_str += ('*' + letter)  # Teachers says you can use f'*{name}
    # Adds one to the index
    index += 1

new_str += '*'  # Only to add the last * symbol
print(new_str)

"""
I've forgot the damn 'index' and had
to ask ChatGPT for some help...
Added some additional codes and info 
with the teacher's resolution.
"""
