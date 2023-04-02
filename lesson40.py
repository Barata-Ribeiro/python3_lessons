""" Calculator using 'while' """

# This isn't like regular a calculator and
# is probably not a good idea to use practically.
while True:
    # Get input from user
    num_1 = input('First number: ')
    operator = input('Operator (+ - / *): ')
    num_2 = input('Second number: ')

    num_1_float = 0
    num_2_float = 0

    # Validate input numbers
    valid_num = None
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_num = True
    # Prints the error message
    except Exception as error:
        valid_num = None
        print(error)
        # Obs: I have not reached the 'try' and 'except'
        # statements yet, and will not use 'ValueError' for now...

    # Check for valid input number
    if valid_num is None:
        print('One or both of the numbers is invalid.')
        continue

    # Validate operator
    valid_operators = "+-/*"
    if operator not in valid_operators:
        print('The typed character is not a valid operator.')
        continue

    # Checks if the user entered more than one operator
    if len(operator) > 1:
        print('You must specify only one operator.')
        continue

    # Perform the calculation
    result = 0
    if operator == '+':
        result = num_1_float + num_2_float
    elif operator == '-':
        result = num_1_float - num_2_float
    elif operator == '*':
        result = num_1_float * num_2_float
    elif operator == '/':
        # Check for divide by zero
        if num_2_float == 0 or num_1_float == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num_1_float / num_2_float
    else:
        print('Something is wrong...')

    # Print the result
    print(f'The result is: {result}')

    # Check if user wants to exit
    exit = input(
        'Do you want to exit? [y]es / [n]o ').lower().startswith('y')
    if exit:
        break
    else:
        continue
