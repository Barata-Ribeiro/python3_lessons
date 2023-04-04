""" while/else """

string = 'Any value'

i = 0
while i < len(string):
    letter = string[i]

    if letter == ' ':
        break

    print(letter)
    i += 1
else:
    print('Else was executed.')
print('Here is outside the while/else block.')
