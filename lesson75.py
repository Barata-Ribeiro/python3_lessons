# Exercises...
# Create functions that double, triple and quadruple
# the number received as a parameter.

def multiplier(factor):  # Multiplier function receives a factor
    def multiply(number):  # Multiply function receives a number
        return number * factor  # Multiply the number by the factor
    return multiply  # Return the multiply function


# Create functions that doubles, triple and quadruple using closures...
double = multiplier(2)  # Assign 2 as the factor
triple = multiplier(3)  # Assign 3 as the factor
quadruple = multiplier(4)  # Assign 4 as the factor

# Call the functions...
# Variable with numbers from 1 to 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# For each number, call the function using number as a parameter
doubles = [double(number) for number in numbers]
triples = [triple(number) for number in numbers]
quadruples = [quadruple(number) for number in numbers]

print(doubles)
print(triples)
print(quadruples)
