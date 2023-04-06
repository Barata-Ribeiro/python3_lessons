# This is an example of how while is actually 'useful'
saved_password = '123456'
typed_password = ''
repetitions = 0

while saved_password != typed_password:
    typed_password = input(f'Your password ({repetitions}x): ')

    repetitions += 1

print(repetitions)
print('The upper block could have infinite repetitions.')

###################

text = 'Python'
new_text = ''
# A much simpler solution for iterations in a str
# the 'letter' variable is defined by "You"
for letter in text:
    new_text += f'*{letter}'
    print(letter)
print(new_text + '*')
