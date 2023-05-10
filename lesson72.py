# Exercises with functions
# Create a function that multiplies all the unnamed arguments received.
# Return the total to a variable and show the value of the variable.

def multiply(*args):
    try:
        if 0 in args:
            return 'You cannot multiply by zero.'

        if not args:
            return 'You must enter at least one number.'

        total = 1
        for arg in args:
            total *= arg

        return total

    except TypeError:
        return 'Invalid input: all arguments must be numeric values.'


numbers = [1, 2, 3, 4, 5]
result = multiply(*numbers)
print(result)

# Create a function that tells if a number is even or odd.
# Return whether the number is even or odd.


def even_or_odd(n):
    try:
        if not isinstance(n, (int, float)):
            return 'Invalid input: the argument must be a numeric value.'

        if n % 2 == 0:
            return f'Even number: {n}'

        return f'Odd number: {n}'

    except TypeError:
        return 'Invalid input: all arguments must be numeric values.'


print(even_or_odd(2))
print(even_or_odd(5))
print(even_or_odd(584))
print(even_or_odd(21))
print(even_or_odd(48))
