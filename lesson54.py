"""
Make a shopping list with lists.
The user must be able to
'insert', 'delete' and 'list' values from your list.
Do not allow the program to break with
errors for non-existent indexes in the list.
"""
import os

# creates an empty list
new_list = []
# while true...
while True:
    # asks the user for an option
    print('Select an option')
    option = input('[i]nsert [e]rase [l]ist:')

    # if the option is 'i'...
    if option == 'i':
        # Clears the screen
        os.system('clear')
        # asks the user for a product and puts into 'value'
        value = input('Enter a product: ')
        # adds the 'value' product to the list with .append()
        new_list.append(value)
    # if the option is 'e'...
    elif option == 'e':
        os.system('clear')
        # asks the user for an index value
        index_value = input('Enter an index: ')
        # checks if the index is valid
        try:
            # Passes the 'index_value' into an integer
            # and puts into 'index'
            index = int(index_value)
            # Then deletes the 'index' value from the list
            del new_list[index]
        # If the index is not valid
        except ValueError:
            # Prints an ValueError message
            print('Invalid index')
        except IndexError:
            # Prints an IndexError message
            print('Index does not exist')
    # if the option is 'l'...
    elif option == 'l':
        os.system('clear')

        # If the list is empty...
        if len(new_list) == 0:
            # Prints an warning message
            print('List is empty')
        # Otherwise... for each index and value in the list
        for i, value in enumerate(new_list):
            # prints the index and value '0 "Product"'
            print(i, value)
    # Else the user enters an invalid option...
    else:
        # Prints an error message
        print('Invalid option')
        # Clears the screen
        os.system('clear')
        # continues the loop
