"""
Create a game for the user to guess the secret word.

-- You will propose any secret word
and give the user the possibility to
enter only one letter.

-- When the user enters a letter, you
will check if the entered letter is
in the secret word.

-- If the entered letter is in
the secret word; display the letter;
If the entered letter is not
in the secret word; display *.

--Count the number of attempts your
user makes.
"""
import os
import random

words_list = [
    "Aardvark",
    "Broccoli",
    "Cathedral",
    "Dandelion",
    "Elephant",
    "Flamenco",
    "Galaxy",
    "Harmonica",
    "Intrigue",
    "Juxtaposition",
    "Kaleidoscope",
    "Lighthouse",
    "Metamorphosis",
    "Nebula",
    "Orchestra",
    "Pterodactyl",
    "Quicksand",
    "Rhinoceros",
    "Satellite",
    "Tambourine"
]
secret_word = random.choice(words_list)
right_letters = ''
attempts = 0
max_attempts = len(secret_word) + 5

while True:
    # Asks for the user to enter a letter
    input_letter = input("Enter a letter: ")
    attempts += 1

    # Only one letter is allowed
    if len(input_letter) > 1:
        print('Enter only one letter.')
        continue

    # If the entered letter is in the secret word
    if input_letter in secret_word:
        # save the 'input_letter' inside 'right_letters'
        right_letters += input_letter

    formatted_word = ''
    # For the 'secret_letter' in the 'secret_word'
    for secret_letter in secret_word:
        # if the 'secret_letter' is in the 'right_letters'
        if secret_letter in right_letters:
            # Adds the 'secret_letter' to the 'formatted_word'
            formatted_word += secret_letter
        else:
            # If wrong, substitutes the 'formatted_word'
            # with '*' only.
            formatted_word += '*'
    # It will print the 'formatted_word' and continue showing
    # '*' while you have not guessed the word fully
    print('Formatted word: ', formatted_word)

    # If the player has gone past the 'max_attempts'
    # then they've lost the game.
    if attempts >= max_attempts:
        print("Game Over! You have reached the maximum number of attempts.")
        print('The secret word was:', secret_word)

        # Sets a exit game status
        exit_game = False
        while True:
            # Asks the player if they wish to continue the game
            play_or_exit = input('Do you want to continue? [Y/N]').upper()
            if play_or_exit == 'Y':
                secret_word = random.choice(words_list)
                attempts = 0
                right_letters = ''
                formatted_word = ''
                max_attempts = len(secret_word) + 5
                os.system('clear')
                break
            # if 'N' then it breaks the program/game
            elif play_or_exit == 'N':
                os.system('clear')
                print("Thank you for playing. Good bye!")
                exit_game = True
                break
            # if the player types anything other than 'Y' or 'N'
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        # Check if the player chose to exit the game or not
        if exit_game:
            break

    # If the 'formatted_word' equals the 'secret_word'
    # then the player won the game
    if formatted_word == secret_word:
        os.system('clear')
        print("You have won the game!")
        print('The secret word was:', secret_word)
        print('You tried to guess the secret word', attempts, 'times.')
        # Sets a exit game status
        exit_game = False
        while True:
            # Asks the player if they wish to continue the game
            play_or_exit = input('Do you want to continue? [Y/N]').upper()
            if play_or_exit == 'Y':
                secret_word = random.choice(words_list)
                attempts = 0
                right_letters = ''
                formatted_word = ''
                max_attempts = len(secret_word) + 5
                os.system('clear')
                break
            # if 'N' then it breaks the program/game
            elif play_or_exit == 'N':
                os.system('clear')
                print("Thank you for playing. Good bye!")
                exit_game = True
                break
            # if the player types anything other than 'Y' or 'N'
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        # Check if the player chose to exit the game or not
        if exit_game:
            break
