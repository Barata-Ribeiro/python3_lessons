"""
repetitions or loops
while (for repetition)
Performs an action while a condition is true
Infinite loop -> When a code has no end
"""
# This exercise is for debugging
# if you want a better understanding of loops.

lines = 5
columns = 5

line = 1
# This loop is a big cog with slow spin
while line <= lines:
    column = 1

    # This loop is a small cog with faster spin
    while column <= columns:
        print(f'{line=} {column=}')
        column += 1

    line += 1

print("It's over!")
