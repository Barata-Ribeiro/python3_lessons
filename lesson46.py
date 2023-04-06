# i would be the lines
for i in range(10):
    if i == 2:
        print('i is 2, skipping...')
        continue  # moves on...

    if i == 8:
        print('i is 8, your "else" will not execute')
        break  # break out of loop

    # j would be the columns
    for j in range(1, 3):
        print(i, j)
# Will only execute if no "break" statement exists
else:
    print('"for" completed successfully!')
