# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

calc_1 = 1 + 1 ** 5 + 5
print(calc_1)  # Why 7??? BECAUSE: 1 ** 5 first, then 1 + 1 + 5 = 7
calc_2 = (1 + 1) ** (5 + 5)
print(calc_2)  # Parentheses first, then 2 ** 5 = 1024
calc_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(calc_3)  # Parentheses first, then 1 + int(1.0) = 2, then 2 ** 5 = 1024
