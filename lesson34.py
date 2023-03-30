"""
repetitions or loops
while (for repetition)
Performs an action while a condition is true
Infinite loop -> When a code has no end
"""
# The following code is an infinite loop
# but don't worry, it won't freeze the PC
is_true = True
while is_true:
    name = input('What is your name? ')
    print(f'Your name is: {name}')
    # Infinite loop unless you type 'Exit'
    if name == 'Exit':
        break

# After your break the loop, it continues
# with the following codes...
print("I'm free from the loop!!!")
