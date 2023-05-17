# Example of using set()

letters = set()
while True:
    try:
        letter = input("Enter a letter: ")

        if not letter.isalpha():
            print('Not a letter.')
            continue

        if len(letter) > 1:
            print('Not a single letter.')
            continue

        letters.add(letter.lower())

        print(letters)

        if len(letters) == 5:
            print('You have entered all 5 letters.')
            letters = set()  # Reset letters set for the next iteration

    except EOFError:
        letters = set()  # Reset letters set
        continue
