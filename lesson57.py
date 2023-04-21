"""
List inside other lists and their indexes
"""
rooms = [
    # 0        1
    ['Jason', 'Hector', ],  # 0
    # 0
    ['Mason', ],  # 1
    # 0        1       2
    ['Edson', 'John', 'Elaine',],  # 2
]

print(rooms[0][1])
print(rooms[1][0])
print(rooms[2][2])
# print(rooms[2][3][2])  the tuple (0, 10, 20, 30, 40)

for room in rooms:
    print(f'The room is: {room}')
    for person in room:
        print(person)

"""
The first 'for' is for each main list.
The second 'for' is for each item in each list.
"""
