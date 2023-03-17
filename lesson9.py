addition = 10 + 10  # if 10 + 10.2 = 20.2
print('Addition:', addition)

subtraction = 10 - 5
print('Subtraction:', subtraction)

multiplication = 10 * 10
print('Multiplication:', multiplication)

division = 10 / 3  # float
print('Division:', division)

# If devision with float, will never return decimals, always a float ending with 0
integer_division = 10 // 2.2
print('Integer Division:', integer_division)

exponentiation = 2 ** 10  # Careful with big numbers...
print('Exponentiation:', exponentiation)

modulus = 55 % 2  # returns the remainder or signed remainder of a division
print('Modulus:', modulus)

# To find if a number is divisible by another, which returns the remainder 0
print(10 % 8 == 0)  # false, remainder is 2
print(16 % 8 == 0)  # true
print(10 % 2 == 0)  # true
print(15 % 2 == 0)  # false, remainder is 1
print(16 % 2 == 0)  # true
