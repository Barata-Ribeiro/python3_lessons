# Unpacking in method
# and function calls
string = 'ABCD'
new_list = ['Mary', 'Helena', 1, 2, 3, 4, 'Jason']
new_tuple = 'Python', 'is', 'fun!'

rooms = [
    # 0        1
    ['Jason', 'Hector', ],  # 0
    # 0
    ['Mason', ],  # 1
    # 0        1       2
    ['Edson', 'John', 'Elaine',],  # 2
]

# p, b, *_, u = new_list
# print(p, u)

for name in new_list:
    print(name, end=' ')  # Mary, Helena, 1, 2, 3, 4, Jason
print()
# A most simple way to unpack the examples
print(*new_list)  # Mary, Helena, 1, 2, 3, 4, Jason
print(*new_tuple)  # Python is fun!
print(*string)  # A B C D

print(*rooms, sep='\n')  # Prints in the same format as above
